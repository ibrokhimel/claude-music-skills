# Bass/808 MIDI delivery: tested script template and checks

On FL 21 the piano-roll MCP tools only queue notes and do not apply them. Every bass or 808 part with pitch, length, velocity or slides is therefore delivered as a MIDI file written with `mido`. The user drags it onto the channel or piano roll. This file holds a tested template (run on 2026-10-16; output checked: 22 notes, slides overlapping by 12 ticks, file exactly 4 bars).

## Contents
1. Delivery rules
2. Choosing the pitch mode
3. The template (`make_bass.py`)
4. How to adapt it
5. Pre-delivery checklist
6. What to tell the user

## 1. Delivery rules

- PPQ 96; 1/16 = 24 ticks; 1 bar = 384 ticks; 1/16 triplet = 16 ticks. Pattern: `C:\Users\User\Documents\flstudio\ny-drill-midi\make_midi.py`.
- One .mid per channel: `808.mid`, `bass.mid`, `sub.mid`, `reese.mid`. Never put two instruments in one file.
- **No note may end past the last bar**, or FL adds an extra bar to the pattern. The template clamps and reports any overrun. A slide cannot wrap from the last bar to bar 1; finish the loop-end slide by the bar line.
- `end_of_track` is placed exactly at BARS x 384 ticks, so the clip length is exact.
- Note-offs are sorted before note-ons on the same tick, so touching notes retrigger cleanly.
- **Slides = overlap.** The previous note (different pitch) is extended OVERLAP ticks past the slide target's start. Non-slide notes are trimmed so they never overlap, which prevents accidental glides on a Mono channel.
- **Never overlap two notes of the same pitch**: the note-off becomes ambiguous. Same-pitch legato = touching notes.
- Swing: bake it into ticks to match the drums. Delay even steps by `round(48 x S/100) - 24` ticks, where S is the MPC/Linn %: 54% -> 2, 58% -> 4, 62% -> 6, 66% -> 8. Use exactly the drums' value (see `music-drums-groove`).
- Run: `uv run --with mido --no-project python make_bass.py` (mido is not installed globally; `uv` is).
- Pure on/off one-pitch 808 rows on a pre-tuned sample can instead go to `fl_set_step_sequencer` (see `808-guide.md` section 5).

## 2. Choosing the pitch mode

| Instrument | MODE | Written note |
|---|---|---|
| 808 sample in Sampler, root left at FL "C5" (the user's usual setup) | `"sample"`, SAMPLE_PITCH = measured tail pitch | `60 + (real - SAMPLE_PITCH)` |
| Sampler with root note set to the measured pitch | `"pitched"` | real MIDI |
| 3x Osc / FLEX / Sytrus / GMS / VST synth bass | `"pitched"` | real MIDI |

In `"sample"` mode with a C1 sample (24), real G1 (31) is written as 67. The template's validator always checks the REAL pitch against the register window (default 24-40 for 808s; pass `lo=28, hi=52` for a synth or electric bass).

## 3. The template (`make_bass.py`)

The example writes the 4-bar G minor drill 808 from `808-guide.md` (bars 1-3 with slides, bar 4 without: 3 slides per 4 bars).

```python
"""Bass/808 MIDI for FL Studio: one .mid per channel, slides by overlap.

Key: G minor. Tempo 142. 808 = Sampler one-shot measured at C1 (MIDI 24),
root left at FL C5 -> MODE "sample" (MIDI 60 = sample's own pitch).
Channel: Mono + Porta, Slide ~40. Only overlapping notes glide.

Run:  uv run --with mido --no-project python make_bass.py
"""
from pathlib import Path

import mido

PPQ = 96                 # FL default; 1 beat = 96 ticks
STEP = PPQ // 4          # 1/16 = 24 ticks
BAR = 16 * STEP          # 384 ticks
BARS = 4                 # loop length; no note may end past BARS * BAR
BPM = 142
OVERLAP = STEP // 2      # slide overlap 12 ticks (1/32); any overlap > 0 glides
SWING_TICKS = 0          # delay for even steps; match the drums (0 = straight)
OUT = Path(__file__).resolve().parent

MODE = "sample"          # "pitched" = true MIDI pitch; "sample" = relative to 60
SAMPLE_PITCH = 24        # measured pitch of the 808 tail (C1); used in "sample"


def out_pitch(real):
    return real if MODE == "pitched" else 60 + (real - SAMPLE_PITCH)


def from_grid(bar, row, pitch, glide="", vel=110, vels=None):
    """Grid row -> events. row: 16 cells ('R - . O | ...'); pitch: symbol ->
    real MIDI; glide: same shape, '^'/'v' marks a slide target."""
    cells = row.replace("|", " ").split()
    gl = glide.replace("|", " ").split() if glide else ["."] * 16
    assert len(cells) == 16 and len(gl) == 16, f"bad grid: {row}"
    vels = vels or {}
    ev, i = [], 0
    while i < 16:
        c = cells[i]
        if c in ".-~":
            i += 1
            continue
        j = i + 1
        while j < 16 and cells[j] == "-":
            j += 1
        ev.append((bar, i + 1, pitch[c], j - i, vels.get(c, vel), gl[i] in "^v"))
        i = j
    return ev


def build(events):
    """events: (bar 1-based, step 1-16, real_midi, len_steps, vel, slide).
    slide=True marks a glide TARGET: the previous note is extended to overlap
    it by OVERLAP ticks. Other notes are trimmed so they never overlap."""
    notes = []
    for bar, step, real, ln, vel, slide in sorted(events, key=lambda e: (e[0], e[1])):
        start = (bar - 1) * BAR + (step - 1) * STEP
        if step % 2 == 0:
            start += SWING_TICKS
        notes.append([start, real, int(ln * STEP), vel, slide])
    for prev, cur in zip(notes, notes[1:]):
        if cur[4]:
            assert cur[1] != prev[1], "slide needs a pitch change"
            assert cur[2] > OVERLAP, "slide target shorter than overlap"
            prev[2] = cur[0] + OVERLAP - prev[0]
        elif prev[0] + prev[2] > cur[0]:
            prev[2] = cur[0] - prev[0]
    end = BARS * BAR                       # clamp anything past the loop end
    for n in notes:
        if n[0] + n[2] > end:
            print(f"  clamped note at tick {n[0]} to the loop end")
            n[2] = end - n[0]
    return notes


def validate(name, notes, lo=24, hi=40):
    slides = {}
    for start, real, ln, vel, slide in notes:
        assert ln > 0, f"{name}: zero-length note at tick {start}"
        assert start + ln <= BARS * BAR, f"{name}: note ends past bar {BARS}"
        assert 1 <= vel <= 127
        if not lo <= real <= hi:
            print(f"  NOTE {name}: real pitch {real} outside {lo}-{hi}")
        if slide:
            b = start // BAR + 1
            slides[b] = slides.get(b, 0) + 1
    for b, n in sorted(slides.items()):
        if n > 2:
            print(f"  WARN {name}: {n} slides in bar {b} (budget 1-2)")


def write(name, notes, lo=24, hi=40):
    validate(name, notes, lo, hi)
    ev = []
    for start, real, ln, vel, _ in notes:
        p = out_pitch(real)
        assert 0 <= p <= 127, f"{name}: written pitch {p} out of MIDI range"
        ev.append((start, 1, mido.Message("note_on", note=p, velocity=vel)))
        ev.append((start + ln, 0, mido.Message("note_off", note=p, velocity=0)))
    ev.sort(key=lambda e: (e[0], e[1]))   # note-offs before note-ons at a tick
    tr = mido.MidiTrack()
    tr.append(mido.MetaMessage("track_name", name=name, time=0))
    tr.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(BPM), time=0))
    now = 0
    for tick, _, msg in ev:
        tr.append(msg.copy(time=tick - now))
        now = tick
    tr.append(mido.MetaMessage("end_of_track", time=max(0, BARS * BAR - now)))
    mid = mido.MidiFile(ticks_per_beat=PPQ)
    mid.tracks.append(tr)
    mid.save(OUT / f"{name}.mid")
    print(f"{name}.mid: {len(notes)} notes, mode={MODE}")


# ---- Drill 808, G minor: G1 31, Bb A#1 34, C2 36, Eb D#1 27, F1 29 ----------
P = {"R": 31, "3": 34, "4": 36, "6": 27, "7": 29}
B1 = ("R - - R | 4 - . R | - - 3 - | - - R -", ". . . . | ^ . . . | . . . . | . . . .")
B2 = ("R - 3 - | . . R - | - - 6 - | - - 7 -", ". . ^ . | . . . . | . . . . | . . . .")
ev = []
ev += from_grid(1, B1[0], P, B1[1], vel=115)
ev += from_grid(2, B2[0], P, B2[1], vel=115)
ev += from_grid(3, B1[0], P, B1[1], vel=115)
ev += from_grid(4, B2[0], P, "", vel=115)       # bar 4: no slide -> 3 per 4 bars
write("808", build(ev))
```

## 4. How to adapt it

1. Set the docstring: key, tempo, instrument, MODE and the measured sample pitch.
2. Set BPM, BARS, MODE, SAMPLE_PITCH and SWING_TICKS (copy from the drums).
3. Map grid symbols to REAL MIDI for each chord, e.g. per bar: `{"R": 33, "O": 45, "5": 40, "A": 32}`. Rebuild the dict per chord, or call `from_grid` per bar with that bar's dict.
4. Write rows with `from_grid(bar, row, pitch, glide, vel, vels)`. Use `vels={"g": 30}` for funk ghosts, or accents per symbol. For anything the grid can't express (16th-triplet pickups, half-step lengths), append raw tuples `(bar, step, real, len_steps, vel, slide)`. Fractional steps and lengths are allowed (e.g. `len 0.5`).
5. For layered basses (sub + mid), call `write("sub", ...)` and `write("mid", ..., lo=28, hi=60)` from the same events, transposed, so both share identical timing.
6. Run it and read the output. Any `NOTE`/`WARN`/`clamped` line is a decision to revisit, not noise.

## 5. Pre-delivery checklist

- [ ] Every chord change has the chord's root (or the intended slash-chord bass note) on its first step.
- [ ] Real pitches: 808s in 24-40 (root zone 26-38; brief slide peaks up to 48); synth/electric bass in 28-52.
- [ ] Slides: at most 2 per bar (drill: 2-3 per 4 bars); both notes in key; every slide written as an overlap with a pitch change.
- [ ] No same-pitch overlaps; no unintended overlaps; mono line (one note at a time apart from slide overlaps).
- [ ] Last note ends at or before the last bar line; file length = BARS x 384 ticks.
- [ ] Bass starts relative to the kick match the chosen strategy (K1 lock / K2 gaps / K3 hybrid).
- [ ] 808 velocities steady (100-120); ghost notes only where the style uses them.
- [ ] Swing ticks identical to the drums.
- [ ] Docstring states key, tempo, mode, sample pitch and the channel settings needed.

## 6. What to tell the user (template message)

- Which file goes on which channel; drag it into the piano roll (or onto the channel).
- Channel settings for slides: Miscellaneous functions tab (FUNC) > Polyphony: Mono on, Porta on, Slide ~40. If separated notes glide too, turn Porta off and keep Mono.
- Slides work only on FL native instruments (Sampler, 3x Osc, FLEX, Sytrus, GMS), not on VST/AU synths.
- The tuning applied: cents set via `fl_set_channel_pitch_pan_vol`, or the root note they need to set.
- The mixer steps they must do by hand: sidechain routing, EQ, saturation (see `music-mix-master`).
- Check the low end on phone or laptop speakers before calling it done.
