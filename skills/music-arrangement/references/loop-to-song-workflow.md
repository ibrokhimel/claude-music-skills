# Loop to song: the subtractive workflow in FL Studio

How Claude turns an 8-bar loop into a full arrangement and gets it into the user's FL Studio 21, given that the MCP bridge cannot place playlist clips.

## Contents
1. Workflow overview (why subtraction)
2. Step-by-step procedure
3. Section derivation rules (what to mute where)
4. B variants and the 4/8-bar change rule
5. MCP audition procedure (mute/solo)
6. Delivery A: per-variant patterns + placement table
7. Delivery B: full-length arranged MIDI per role (script)
8. Playlist steps to give the user
9. Worked example: trap loop to 80-bar song
10. Sources

## 1. Workflow overview

The dominant workflow builds the densest section first, duplicates it, strips drums for the breakdown and strips further for the intro, because "subtraction is faster than addition" (Inspired by Beatz; Mixed In Key) **(sourced)**. Mixed In Key: map the strongest section first, create contrast by subtraction (mute bass, remove percussion layers) before adding effects, and rough out a 64-bar version with four labelled sections (intro, main, contrast, return) **(sourced)**.

Attack Magazine's four ways out of the loop **(sourced)**:
1. **Jam it out:** record clip launches or mutes live into the arrangement.
2. **Copy it out:** drop a reference track in and mirror its decisions (it adds a kick, you add one; it cuts the bass, you cut yours).
3. **Turn it out:** start with the kick, add an element every 8-16 bars, subtract approaching the end (house/techno).
4. **Mark it out:** place markers (Intro, Breakdown 1, Drop 1, Breakdown 2, Drop 2, Cool Down, Outro) as scaffolding first.

Claude's default is subtractive (3 for club tracks), with markers (4) always, and reference mirroring (2) when the user names a reference.

## 2. Step-by-step procedure (convention)

1. **Split the full loop into role patterns.** One pattern (and one channel/mixer track) per role: kick, snare/clap, hats, perc, 808/bass, chords, lead, counter, FX. If the user's loop is one pattern with many channels, tell them to use the pattern menu's "Split by channel" so each channel becomes its own pattern.
2. **Check the loop is the fullest section:** 3-4 focal elements, one low-end owner, slotting rules met (`references/roles-and-frequency-slotting.md`). Fix before arranging.
3. **Pick the template** (`references/song-form-templates.md`), compute the bar map and times, check first-peak timing.
4. **Write the element matrix** (sections x roles; X / ~ / - / variant).
5. **Paste the full loop into every peak section** (hook/chorus/drop).
6. **Subtract to make the other sections** (section 3 below).
7. **Make B variants** of each pattern and alternate them so no 8-bar block repeats more than twice in a row (section 4).
8. **At every 8-bar boundary something enters, leaves or changes; at every 4-bar end a micro-variation.**
9. **Insert transitions** at section boundaries: riser/roll into peaks, crash/impact on beat 1, reverse cymbal or vocal pickup before hooks, a beat to a bar of silence before the biggest hit, downlifter or filter close when leaving peaks (`references/energy-builds-transitions.md`).
10. **Automate** filter cutoff, reverb sends, volume swells and pans so repeats evolve (user steps).
11. **Verify per section:** 3-4 focal elements, one low-end owner, energy matches the curve, adjacent sections differ on 2+ axes.

## 3. Section derivation rules (convention)

| Section | Keep | Remove / change |
|---|---|---|
| Intro (rap beat) | melody/sample or chords, filtered (low-pass ~1-2 kHz), maybe hats | kick, 808, snare, counter |
| Intro (club/DJ) | kick + hats + perc | all musical parts; add clap/bass at bar 9 or 17 |
| Verse | kick, snare, 808/bass, chords, simpler hats | lead layer and counter (the vocal takes the lead slot); octave doubles; busiest perc |
| Pre-chorus | verse + pad or rhythm layer | kick may thin in the last bar; roll/riser at the end |
| Hook / chorus / drop | everything | - ; repeats add one layer (octave double, extra perc, counter) |
| Post-chorus | hook instrument or chop + drums | vocal, some harmony |
| Bridge | chords/pad, lead or vocal | kick and 808 (or 808 partial); new chord or texture |
| Breakdown | pads, exposed lead/theme, vocal, FX | kick and bass; most drums |
| Build | snare roll, riser, high-passed music | kick and bass in the last 1-2 bars (or the whole build) |
| Outro (rap/pop) | melody/chords fading, or the intro mirrored | drums, 808 |
| Outro (club) | kick + hats + perc for the last 16 | musical parts in reverse order of entry |

Low-end rule per section: exactly one low-end owner when the low end is on; none in breakdowns and most intros.

## 4. B variants and the change rule

Make at least one B variant per active role (convention):

| Role | A | B variant ideas |
|---|---|---|
| Kick | main pattern | pickup kick into bar 1; kick removed on bar 8 beat 4 |
| Snare/clap | backbeat | ghost or flam on bar 4/8 end; moved hit; roll on bar 8 |
| Hats | main pattern | rolls (1/32, triplets), pattern switch, open hat added |
| Perc | layer 1 | new layer or swapped sample every 8 bars |
| 808/bass | main line | slides, octave jumps, rhythm change, rest bar (`music-bass-808`) |
| Chords | voicing 1 | inversion, extension, stab vs sustain, borrowed chord in bar 8 (`music-chords-voicing`) |
| Lead | phrase | different ending (melody tail), octave up, sparse version (`music-melody-hooks`) |
| Counter | answer | moved to the other half of the phrase |

Alternation patterns for a 16-bar section: `A B` (8 + 8), or `A A'` where A' = A with a bar-8 fill. For 32 bars: `A B A C` or `A B A' B'`. Each repeat of a section uses at least one different variant than its previous instance.

## 5. MCP audition procedure (mute/solo)

The bridge can loop and mute; use it to let the user hear section derivations before committing.

1. `fl_check_bridge_status`; `fl_list_channels` to get channel indexes and names.
2. Route roles to their own mixer tracks: `fl_assign_channel_to_mixer(channel, track)`; name/colour them with `fl_set_track_name_color` (e.g. tracks 1 Kick, 2 Snare, 3 Hats, 4 Perc, 5 808, 6 Chords, 7 Lead, 8 Counter, 9 FX).
3. `fl_set_loop_mode` to pattern mode with the full loop selected, `fl_play`.
4. Audition each section by muting its removed roles: verse = `fl_mute_track` Lead + Counter (+ swap hats to the B pattern if the user selects it); breakdown = mute Kick + 808 (+ Snare, Hats); intro = mute everything except Chords/Lead. Use `fl_solo_track` on the 808 and kick tracks to confirm a single low-end owner.
5. Optional: `fl_diagnose_mix` while playing for peak/balance sanity (it misses short one-shot drum peaks).
6. Unmute everything, `fl_stop`. Report what each section will contain, then deliver.

`fl_set_step_sequencer` writes into the currently selected pattern only. To create drum variants, ask the user to select (or create) the target pattern first, then write the 16-64-step row.

## 6. Delivery A: per-variant patterns + placement table (recommended for editing)

1. Write one .mid per role per variant, each exactly 8 bars (e.g. `hats_A.mid`, `hats_B_rolls.mid`, `808_A.mid`, `808_B_slides.mid`, `build_snare_roll.mid`), following `ny-drill-midi/make_midi.py` conventions: PPQ 96, 1/16 = 24 ticks, drums at MIDI 60, no note ending past bar 8.
2. User creates one pattern per file (name it like the file) and drags each .mid onto its channel / piano roll.
3. Give a placement table: rows = playlist tracks (one per role), columns = sections with bar ranges, cells = pattern name or blank. Example row: `Hats | Intro 1-8: - | Hook 9-16: hats_B | Verse 17-24: hats_A | Verse 25-32: hats_B | ...`.
4. Give time markers (name + bar) and transition one-shots with exact bars.

## 7. Delivery B: full-length arranged MIDI per role (fastest)

One song-length .mid per role with the arrangement already applied: silent sections simply have no notes. The user drags each file onto its channel and places that one pattern at playlist bar 1 on its own track. Trade-off: fast and exact, but less convenient to edit per section. Note: if a role's first note is late in the song, check that FL kept the leading silence after import (it should, since notes keep their tick positions); if not, place the clip at the section's start bar instead.

Script (tested pattern; adapt LOOPS, SECTIONS, MATRIX):

```python
"""Turn 8-bar role loops into full-length arranged MIDI, one .mid per role.
Run:  uv run --with mido --no-project python arrange_song.py
"""
from pathlib import Path
import mido

PPQ = 96
STEP = PPQ // 4            # 1/16 note = 24 ticks
BAR = 16 * STEP
BPM = 140
LOOP_BARS = 8
OUT = Path(__file__).resolve().parent

SECTIONS = [("intro", 8), ("hook1", 8), ("verse1", 16), ("hook2", 8),
            ("verse2", 16), ("bridge", 8), ("hook3", 8), ("outro", 8)]

# One entry per section: a variant name for every 8-bar block, or a list of names.
MATRIX = {
    "kick":  ["-", "A", ["A", "B"], "A", ["A", "B"], "-", "A", "-"],
    "808":   ["-", "A", ["A", "B"], "A", ["B", "B"], "-", "B", "-"],
    "hats":  ["-", "B", ["A", "B"], "B", ["A", "B"], "-", "B", "-"],
    "lead":  ["A", "A", "-", "A", "-", "A", "A", "A"],
}

def drum_row(steps, vel=100, pitch=60, bars=LOOP_BARS):
    """Repeat a 16-char step string ('1' = hit) every bar -> note list."""
    return [(b * BAR + i * STEP, pitch, STEP // 2, vel)
            for b in range(bars) for i, c in enumerate(steps) if c == "1"]

# Replace these with the real loop notes (start_tick, pitch, length, velocity).
LOOPS = {
    "kick": {"A": drum_row("1000000010100000"),
             "B": drum_row("1000000010100000")[:-1]},        # last kick removed
    "808": {"A": [(b * 2 * BAR, 36, 2 * BAR - STEP, 110) for b in range(4)],
            "B": [(b * BAR, 36 if b % 2 == 0 else 43, BAR - STEP, 110) for b in range(8)]},
    "hats": {"A": drum_row("1010101010101010", 85),
             "B": drum_row("1111101011111010", 85)},
    "lead": {"A": [(b * BAR, (72, 70, 67, 70)[b % 4], 4 * STEP, 100) for b in range(8)]},
}

def section_notes(loop, start_bar, n_bars):
    """Place the first n_bars of a loop at start_bar; clip notes at the block end."""
    end = (start_bar + n_bars) * BAR
    return [(start_bar * BAR + t, p, min(l, end - (start_bar * BAR + t)), v)
            for t, p, l, v in loop if t < n_bars * BAR]

def arrange(role):
    notes, bar = [], 0
    for (name, bars), entry in zip(SECTIONS, MATRIX[role]):
        blocks = -(-bars // LOOP_BARS)                        # ceil
        names = entry if isinstance(entry, list) else [entry] * blocks
        for i in range(blocks):
            block_bars = min(LOOP_BARS, bars - i * LOOP_BARS)
            v = names[i] if i < len(names) else names[-1]
            if v != "-":
                notes += section_notes(LOOPS[role][v], bar + i * LOOP_BARS, block_bars)
        bar += bars
    return notes, bar

def write(name, notes, total_bars):
    events = []
    for start, pitch, length, vel in notes:
        events.append((start, 1, mido.Message("note_on", note=pitch, velocity=vel)))
        events.append((start + length, 0, mido.Message("note_off", note=pitch, velocity=0)))
    events.sort(key=lambda e: (e[0], e[1]))           # offs before ons at same tick
    track = mido.MidiTrack()
    track.append(mido.MetaMessage("track_name", name=name, time=0))
    track.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(BPM), time=0))
    now = 0
    for tick, _, msg in events:
        track.append(msg.copy(time=tick - now))
        now = tick
    track.append(mido.MetaMessage("end_of_track", time=max(0, total_bars * BAR - now)))
    mid = mido.MidiFile(ticks_per_beat=PPQ)
    mid.tracks.append(track)
    mid.save(OUT / f"{name}.mid")
    print(f"{name}.mid: {len(notes)} notes, {total_bars} bars")

def bar_map():
    bar = 1
    for name, bars in SECTIONS:
        t = (bar - 1) * 240 / BPM
        print(f"{name:8s} bars {bar:3d}-{bar + bars - 1:3d}  starts {int(t // 60)}:{t % 60:04.1f}")
        bar += bars

if __name__ == "__main__":
    for r in MATRIX:
        assert len(MATRIX[r]) == len(SECTIONS), f"{r}: one entry per section"
        notes, total = arrange(r)
        write(r, notes, total)
    bar_map()
```

Script notes:
- Sections shorter than 8 bars (4-bar intros) use the first half of the variant; notes are clipped at block ends so nothing spills past the last bar.
- 808 glides need OVERLAPPING notes and a Mono + Porta channel; clipping at a section end can shorten a glide tail, so put slides inside blocks (`music-bass-808`).
- For a one-bar silence before a drop, add a variant whose last bar is empty (filter notes with `t < 7 * BAR`) and use it in the build's last block.
- Verified output for the example: 80 bars per file, bar map Intro 1-8 (0:00), Hook 9-16 (0:13.7), Verse 17-32 (0:27.4), Hook 33-40 (0:54.9), Verse 41-56 (1:08.6), Bridge 57-64 (1:36.0), Hook 65-72 (1:49.7), Outro 73-80 (2:03.4), end 2:17.1.

## 8. Playlist steps to give the user

Phrase these as numbered steps with exact bars. Menu names are FL 21; if a shortcut differs on the user's build, the menu path still applies.

1. Set the song tempo (Claude can do this with `fl_set_tempo`).
2. Add time markers at each section start: right-click the playlist's time ruler / use the playlist menu's time-marker option (Alt+T adds one at the song position), and name them Intro, Hook 1, Verse 1, ...
3. One playlist track per role, named like the mixer tracks (Kick, Snare, Hats, ...).
4. Place patterns: pick the pattern in the playlist's clip selector and click at the section's start bar on the role's track (Delivery A), or place each full-length pattern at bar 1 (Delivery B).
5. Duplicate peak sections: select the hook clips across all tracks and press Ctrl+B to duplicate the selection to the right, or copy-paste to the next hook's start bar.
6. Subtract: delete or mute clips for roles that sit out (per the matrix). If a clip must differ, use the clip menu's "Make unique" before editing its notes, so the other copies stay unchanged.
7. Transitions: drop riser / reverse-crash samples on an FX track so they END at the target downbeat; slice clips to make the silence gap before the drop.
8. Automation: right-click a knob (e.g. Fruity Filter cutoff on the music bus) > Create automation clip, then draw the ramp across the build bars.
9. Switch to song mode and play from bar 1; check each boundary.

## 9. Worked example: trap loop to an 80-bar song (140 BPM, C minor)

Input: 8-bar loop with kick, clap, hats, perc, 808, dark pad, bell lead, counter pluck.

Bar map: Intro 1-8 | Hook 9-16 | Verse 17-32 | Hook 33-40 | Verse 41-56 | Bridge 57-64 | Hook 65-72 | Outro 73-80 (2:17).

| Role | Intro | Hook 1 | Verse 1 | Hook 2 | Verse 2 | Bridge | Hook 3 | Outro |
|---|---|---|---|---|---|---|---|---|
| Kick | - | A | A, B | A | A, B | - | A | - |
| Clap | - | A | A, A+fill | A | A, A+fill | - | A | - |
| Hats | ~ filtered A | B rolls | A, B | B | A2 (new), B | ~ A | B | - |
| Perc | - | A | - , A | A | B (new layer) | - | A + B | - |
| 808 | - | A | A, B | A | B, B | - | B + slides | - |
| Pad | ~ low-passed | X | X | X | X | X | X | X fading |
| Bell lead | ~ filtered | X | - | X | ~ sparse | X | X + octave 84 | ~ |
| Counter | - | X | fills bars 24, 32 | X | X | - | X | - |
| FX | riser bars 5-8 | crash bar 9 | 808/kick drop-out bar 32 | rev crash into 33 | - | silence beat 4 bar 64, impact 65 | crash 65 | downlifter 73-76 |

Energy: 3, 8, 6, 8, 6-7, 4, 9, 3. Focal count in hooks: lead + beat + hats (+ counter) = 3-4; verses leave space for the vocal.

## 10. Sources

- Inspired by Beatz: https://www.inspiredbybeatz.com/en/edm-arrangement-from-loop-to-exciting-track/
- Mixed In Key: https://mixedinkey.com/?p=5367
- Attack Magazine, 4 ways to break out of the loop: https://www.attackmagazine.com/technique/tutorials/4-ways-to-break-out-of-the-loop/
- Wikipedia, Phrasing (DJ) (changes every 4 or 8 bars): https://en.wikipedia.org/wiki/Phrasing_(DJ)
- Beatportal (automation keeps tracks evolving): https://www.beatportal.com/articles/818379-step-by-step-guide-to-producing-drum-and-bass-like-sub-focus-a-m-c-and-delta-heavy
- Lo-fi variation (loop drums/bass, vary keys), search summaries of Lunacy Audio / MusicRadar: https://lunacy.audio/how-to-make-lofi-music/
- Owsinski (fills answer the lead): https://bobbyowsinskiblog.com/song-arrangement-elements/
- User's delivery pattern: `C:\Users\User\Documents\flstudio\ny-drill-midi\make_midi.py`
