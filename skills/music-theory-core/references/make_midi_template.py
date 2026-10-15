"""Reusable MIDI writer for FL Studio: one .mid per part, ready to drag into a channel.

Copy this file into a project folder (e.g. Documents/flstudio/<beat-name>/make_midi.py),
edit SETTINGS and build_parts(), then run:

    uv run --with mido --no-project python make_midi.py [out_dir]

Conventions (music-theory-core):
- Notes are tuples (start_beat, midi, length_beats, velocity). Beat 0 = bar 1 beat 1.
- pos(bar, step) converts 1-based bar and 16-step positions to beats.
- MIDI 60 = C4 (FL "C5"). Drum samples in FL's Sampler play at their own pitch on 60.
- A sampled 808 sounds at sample_root + (note - 60): write 808 roots relative to 60.
- PPQ 96 (1/16 = 24 ticks, 1/16 triplet = 16, 1/8 triplet = 32).
- Note ends are clamped to the last bar so FL never adds an extra bar.
- Same-pitch overlaps are trimmed (MIDI cannot hold two identical notes at once);
  different-pitch overlaps are kept, which is what makes 808 slides glide (Mono + Porta).
"""
from pathlib import Path
import sys

import mido

# ---- SETTINGS -----------------------------------------------------------------
BPM = 140
BARS = 4                 # total length; every note is clamped to end by here
PPQ = 96
BEATS_PER_BAR = 4
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent

STEP = 0.25              # 1/16 note in beats
TRIP16 = 1 / 6           # 1/16 triplet
TRIP8 = 1 / 3            # 1/8 triplet
HIT = STEP / 2           # one-shot drum length
DRUM = 60                # sampler drums play at their own pitch on MIDI 60
VEL = {"X": 118, "x": 95, "g": 48, "o": 90}   # drum grid symbols -> velocity

SCALES = {"major": [0, 2, 4, 5, 7, 9, 11], "minor": [0, 2, 3, 5, 7, 8, 10],
          "harmonic_minor": [0, 2, 3, 5, 7, 8, 11], "dorian": [0, 2, 3, 5, 7, 9, 10],
          "phrygian": [0, 1, 3, 5, 7, 8, 10], "minor_pent": [0, 3, 5, 7, 10]}
CHORDS = {"maj": [0, 4, 7], "m": [0, 3, 7], "dim": [0, 3, 6], "sus2": [0, 2, 7],
          "sus4": [0, 5, 7], "maj7": [0, 4, 7, 11], "7": [0, 4, 7, 10], "m7": [0, 3, 7, 10],
          "m9": [0, 3, 7, 10, 14], "maj9": [0, 4, 7, 11, 14], "madd9": [0, 3, 7, 14]}


# ---- helpers --------------------------------------------------------------------
def pos(bar, step=1, ticks=0):
    """1-based bar and 16-step position (+ extra ticks) -> beats."""
    return (bar - 1) * BEATS_PER_BAR + (step - 1) * STEP + ticks / PPQ


def scale_note(root, scale, degree, octave=0):
    """Degree 0 = root; wraps into higher/lower octaves. root is a MIDI number."""
    s = SCALES[scale]
    return root + s[degree % len(s)] + 12 * (degree // len(s) + octave)


def chord(root, quality, start, length, vel=80):
    """Block chord as notes. Voicing/inversion choice belongs to music-chords-voicing."""
    return [(start, root + iv, length, vel) for iv in CHORDS[quality]]


def grid(row, bars, pitch=DRUM, length=HIT, vel=None):
    """Drum-grid string -> notes. row like 'X... ..x. X... ....' (16 symbols per bar,
    '|' and spaces ignored; a 32-symbol row = a 2-bar pattern). Repeats over `bars`
    (1-based start bars; for a 2-bar row pass range(1, BARS + 1, 2)). Symbols not in
    VEL ('.', 'r') are rests; write rolls explicitly with TRIP16 / STEP / 2 offsets."""
    cells = [c for c in row if c not in "| "]
    assert len(cells) % 16 == 0, f"grid row needs 16 symbols per bar, got {len(cells)}"
    out = []
    for b in bars:
        for i, c in enumerate(cells):
            if c in VEL:
                out.append((pos(b + i // 16, i % 16 + 1), pitch, length, vel or VEL[c]))
    return out


def swing16(notes, mpc_percent):
    """Apply MPC/Linn 16th swing (50 = straight, 66 = triplet) to notes on even 16ths."""
    delay = (mpc_percent - 50) / 100 * 0.5
    out = []
    for start, p, length, v in notes:
        steps = start / STEP
        on_even = abs(steps - round(steps)) < 1e-6 and round(steps) % 2 == 1
        out.append((start + delay, p, length, v) if on_even else (start, p, length, v))
    return out


def write(name, notes, bpm=BPM, bars=BARS):
    """Write <name>.mid with one track. Clamps, de-overlaps and reports issues."""
    end = bars * BEATS_PER_BAR * PPQ
    cleaned, dropped = [], 0
    for start, pitch, length, vel in notes:
        s = round(start * PPQ)
        e = min(round((start + length) * PPQ), end)
        if s < 0 or s >= end or not 0 <= pitch <= 127:
            dropped += 1
            continue
        cleaned.append([s, max(e, s + 1), int(pitch), max(1, min(127, int(vel)))])
    cleaned.sort()
    last = {}
    for n in cleaned:                       # trim same-pitch overlaps
        prev = last.get(n[2])
        if prev and prev[1] > n[0]:
            prev[1] = n[0]
        last[n[2]] = n
    cleaned = [n for n in cleaned if n[1] > n[0]]
    events = []
    for s, e, p, v in cleaned:
        events.append((s, 1, mido.Message("note_on", note=p, velocity=v)))
        events.append((e, 0, mido.Message("note_off", note=p, velocity=0)))
    events.sort(key=lambda ev: (ev[0], ev[1]))   # offs before ons at the same tick
    track = mido.MidiTrack()
    track.append(mido.MetaMessage("track_name", name=name, time=0))
    track.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(bpm), time=0))
    track.append(mido.MetaMessage("time_signature", numerator=4, denominator=4, time=0))
    now = 0
    for tick, _, msg in events:
        track.append(msg.copy(time=tick - now))
        now = tick
    track.append(mido.MetaMessage("end_of_track", time=max(0, end - now)))
    mid = mido.MidiFile(ticks_per_beat=PPQ)
    mid.tracks.append(track)
    OUT.mkdir(parents=True, exist_ok=True)
    mid.save(OUT / f"{name}.mid")
    note = f" ({dropped} out-of-range notes dropped)" if dropped else ""
    print(f"{name}.mid: {len(cleaned)} notes{note}")


# ---- PARTS: replace with the real composition -----------------------------------
def build_parts():
    """Demo: 4-bar trap skeleton in C minor, i-VI-III-VII (Cm Ab Eb Bb), 140 BPM HT."""
    bars = range(1, BARS + 1)
    parts = {
        "kick": grid("X... .... ..x. ....", bars),
        "snare": grid(".... .... X... ....", bars),
        "hihat": grid("x.x. x.x. x.x. x.x.", bars),
    }
    for i in range(6):                                   # 1/16-triplet roll into bar 1
        parts["hihat"].append((pos(BARS, 13) + i * TRIP16, DRUM, HIT, 55 + i * 10))
    roots = [0, -4, 3, -2]                    # C, Ab, Eb, Bb as offsets from C
    parts["808"], parts["keys"] = [], []
    for bar, r in zip(bars, roots):           # 808 sample tuned to C: note 60 = its root
        parts["808"] += [(pos(bar, 1), 60 + r, 2.5, 120), (pos(bar, 11), 60 + r, 1.5, 105)]
        quality = "m" if r == 0 else "maj"    # i, VI, III, VII in C minor
        parts["keys"] += chord(60 + r, quality, pos(bar, 1), 4, 72)
    parts["hihat"] = swing16(parts["hihat"], 50)  # 50 = straight; try 54-58 for looseness
    return parts


if __name__ == "__main__":
    for part, notes in build_parts().items():
        write(part, notes)
