# Hi-hats, rolls, fills, build-ups, kit choice and the drum MIDI template

Hi-hat programming (density, velocity, triplets, 1/32 and 1/24 rolls, pitched rolls, open/closed choke), percussion and cymbal placement, the 4/8/16-bar fill schedule with fill grids, build-ups and drops, drum sound choice/layering/tuning, and a tested Python/mido template for drum MIDI files.

## Contents
1. Hat density sets the energy
2. Hat velocity patterns
3. Trap/drill hat bar templates
4. Rolls: types, tick math, placement, shapes, pitch
5. Open hats and the choke group
6. Percussion, rides and crashes
7. Fill schedule (4/8/16 bars) and fill grids
8. Build-ups, drops and breakdowns
9. Kit choice, layering and tuning
10. Drum MIDI template (tested)

---

## 1. Hat density sets the energy

| Hat layer | Feel | Genres |
|---|---|---|
| Quarters / none | Sparse, heavy | dubstep, deep house (often no closed hat) |
| 8ths | Relaxed | boom bap (or swung 16ths), lo-fi, rock, pop verses |
| 3+3+2 grouped 16ths with gaps | Bouncy, skippy | UK/NY drill, phonk cowbell |
| 16ths | Driving | R&B, house, techno, trap hooks, synthwave |
| 16ths + rolls/triplets | Excited, urgent | trap, drill, future bass, hyperpop |

Event density raises groove (sourced, Senn 2018), so the hat layer is the main energy control. Change density at section boundaries (8ths in verse → 16ths in hook) rather than inside a phrase (convention).

## 2. Hat velocity patterns

- **16ths default (convention):** on-beat ≈ 110, "&" ≈ 95, "e"/"a" 60–70.
- **R&B (sourced, Audeobox):** 8th positions 89–102, in-between 16ths 38–64; open hat step 7 at ~83.
- **Lo-fi (sourced, Audeobox):** 8ths alternating ~89 / ~51.
- **Trap 8ths (convention):** 100 on beats, 75–80 on "&".
- **Drill (sourced, NI):** 3+3+2 groups at 100, second hit of each group 87, ghost 52 on b1 step 16.
- **House (sourced, Attack):** 16ths with varying velocity; shaker velocity variation "plays a very important role" (deep tech house).
- **Afrobeats shaker (sourced, Audeobox):** 60-40-70-40% per beat (76, 51, 89, 51).
- **Rule:** hats that land on kick or snare steps can drop 10–20 (convention); delete closed hats that duplicate kick transients in kick-heavy styles (sourced, Beatstorapon Jersey club).

## 3. Trap/drill hat bar templates

High-pass trap hats ~500 Hz and sit them low as texture (sourced, Audeobox). `r` = roll start, described per row. Rows with `r` must be MIDI.

```
A 8ths     x . x . | x . x . | x . x . | x . x .   1010101010101010
B 16ths    x g x g | x g x g | x g x g | x g x g   1111111111111111
C roll b4  x . x . | x . x . | x . x . | r . . .   1010101010101000
D gap+roll x x x x | r . . . | x x x x | x . x x   1111100011111011
E NI end   x . x . | x . x . | x . x . | x . r .   1010101010101010
F triplets x . x g | x . x . | r . . . | . . . .   1011101010000000
G drill    x . . x | . . x . | x . . x | . . x .   1001001010010010
```

- **C:** beat 4 = eight 1/32s (12 ticks) or six 1/16-triplets (16 ticks), into the next bar.
- **D:** beat 2 = 16th-triplet roll into the snare on step 9; beat 4 thinned for the snare's tail — the "skip" feel.
- **E (sourced, NI trap):** the last hat becomes a 3-note 32nd roll (steps 15 + 2 more 32nds), middle note quieter.
- **F:** beats 3–4 = six 8th-triplets (32 ticks) — the drill/NY "triplet bar" (user's `make_midi.py`).
- **G (sourced, NI drill):** start from this, then delete hits for gaps and add triplet bursts before snares.
- **Rotation (convention):** alternate 2–4 templates over a 4-bar phrase, e.g. A, C, A, D or F, G, F, roll — never the same roll every bar.

## 4. Rolls: types, tick math, placement, shapes, pitch

| Roll | Hits per beat | Ticks apart (PPQ 96) | FL snap | Use |
|---|---|---|---|---|
| 8th triplet | 3 | 32 | 1/3 beat | drill/trap triplet bars, "lazy" bounce |
| 16th (straight) | 4 | 24 | 1/4 beat | step-sequencer-safe burst |
| 16th triplet ("1/24") | 6 | 16 | 1/6 beat | the classic trap/drill roll |
| 32nd | 8 | 12 | 1/8 beat | fast trap roll, EDM build last bar |
| 64th | 16 | 6 | 1/16 beat | stutter/glitch, DnB fills (Violet: 1/32–1/64 repeats) |

**Placement (convention):** every 1–2 bars, replace one beat (or half-beat) with a roll: on beat 4 heading into the next bar, or on beat 2 heading into a beat-3 snare. Max one roll per bar under a rap verse; more in instrumental hooks. End a roll on or just before the target hit, not over it.

**Velocity shapes (convention):** crescendo 60 → 110 (into a downbeat); decrescendo 110 → 60 (after a snare); alternating 110/70 (stutter); NI 3-note 32nd roll with the middle note lower (sourced).

**Pitched rolls:** in MIDI, raise the note number per hit (Sampler keytracks: MIDI 61 = +1 semitone). Typical: +1 to +12 semitones across the roll, or up-down. In the step sequencer, graph-editor Fine pitch gives only ±100 cents per step (sourced, Image-Line) — enough for a subtle tilt, not a ramp. Keep pitched rolls to accents (1 per 4 bars).

**Duration:** each roll note ~half its spacing (e.g. 6 ticks for 1/32s) so hits stay distinct.

## 5. Open hats and the choke group

- Open hats go on offbeats for lift: every "&" in house/trance/amapiano (sourced), step 7 in R&B/afrobeats (sourced), occasional step 7 or 15 in trap (convention), bar-2 beat 4 in boom bap (sourced, Attack).
- Remove the closed hat on the open hat's step (the grids above do this).
- **Length:** set the open hat's decay to ease into the next clap/snare without covering it (sourced, Attack house) — typically ending before the next backbeat.
- **Choke:** put closed and open hats in the same cut group so the closed hat silences a ringing open hat (sourced, Attack: "optionally use a choke group"; FL: Channel settings > Misc, "Cut" and "Cut by" — set by the user, not via MCP).
- 2-step garage uses one hat on every offbeat with decay between closed and open (sourced, Attack).

## 6. Percussion, rides and crashes

- **Shakers/tambourine:** continuous 16ths (afrobeats, amapiano, deep house) or offbeat 8ths (house tamb, 2-step shaker), velocity-varied, low in the mix (sourced).
- **Rim/clave/conga:** the "conversation" layer — syncopated answers between kick and snare (house rim, afro clave/conga, 2-step rims).
- **Answer rule:** one answering element (open hat, rim, perc, vocal chop) closes each 2-bar phrase, e.g. a perc hit on bar-2 step 11 or an open hat on bar-2 step 15 (convention).
- **Ride:** 8ths or offbeats in choruses/peaks for an energy lift; liquid DnB ride over the top (convention/sourced).
- **Crash:** step 1 of each new 8/16-bar section, vel 100–120; the Amen break closes its 4-bar phrase with an early crash (sourced, Wikipedia); Jersey club crash on beat 1 marks sections (sourced, NI). Do not crash every 4 bars.
- **Reverse cymbal:** ends exactly on step 1 of the new section (lo-fi transitions: sourced, NI).

## 7. Fill schedule (4/8/16 bars) and fill grids

**Schedule (convention):** bar 4 = small variation; bar 8 = bigger fill; bar 16 = full fill + crash on the next bar's step 1. Avoid identical fills at every boundary (sourced, Mixed In Key). A 4-bar Amen phrase is the model: two bars main beat, bar 3 delays a snare, bar 4 leaves beat 1 empty, syncopates, crashes early (sourced, Wikipedia).

Bar 4 — pickup (backbeat genres):
```
Snare      . . . . | X . . . | . . . . | X . g g   0000100000001011
```
Two ghost snares on 15–16 (45, 60) lead into the next downbeat.

Bar 8 — snare run, kick cleared under the fill:
```
Kick       X . . . | . . . . | . . . . | . . . .   1000000000000000
Snare      . . . . | X . . . | x . x . | x x x x   0000100010101111
```
Velocity ramp 80 → 120 over steps 9–16.

Bar 16 — tom run (then crash on the next step 1):
```
Snare      . . . . | X . . . | . . . . | . . . .   0000100000000000
TomHi      . . . . | . . . . | x x . . | . . . .   0000000011000000
TomMid     . . . . | . . . . | . . x x | . . . .   0000000000110000
TomLo      . . . . | . . . . | . . . . | x x x x   0000000000001111
```

Trap last-bar fill (sourced, NI: straight-8th snare fill in the last bar of a 4-bar loop):
```
Snare      x . x . | x . x . | X . x . | x . x .   1010101010101010
```
Ramp velocity up across the bar; keep the beat-3 snare accented.

House turnaround (sourced, Attack): reduced-velocity kick on step 15 of the phrase's last bar:
```
Kick       X . . . | X . . . | X . . . | X . g .   1000100010001010
```

Hip-hop pre-hook dropout (convention): mute the kick (and 808) for the last half bar before the hook:
```
Kick       X . . . | . . x . | . . . . | . . . .   1000001000000000
```

Other phrase marks:
- **Drill:** displace the bar-2 snare relative to bar 1 (beat 3 → beat 4) and judge whether it feels early, centered or late (sourced, NI/Beatstorapon).
- **Synthwave:** gated tom fill in the last bar of each 8-bar phrase (convention).
- **EDM/DnB:** 1/32 or 1/64 snare repeats with rising velocity (sourced, Violet).
- **Stutter:** 808 or snare 1/16 or 1/32 repeats on the last beat; reverse cymbal into step 1.

## 8. Build-ups, drops and breakdowns

**EDM 8-bar build (convention; trance/DnB snare-roll builds are sourced):**
```
Bars 1-4   X . . . | X . . . | X . . . | X . . .   1000100010001000
Bars 5-6   x . x . | x . x . | x . x . | x . x .   1010101010101010
Bar 7      x x x x | x x x x | x x x x | x x x x   1111111111111111
Bar 8      r . . . | r . . . | r . . . | . . . .   1000100010000000
```
- Bar 8: 32nd or 16th-triplet rolls on beats 1–3, beat 4 empty (the gap before the drop).
- Velocity ramp 60 → 120 across all 8 bars; high-pass filter sweep on the drum/music bus (user sets it in FL; see `music-mix-master`).
- Remove the kick during the build or from bar 5 (future bass: kick removed in the build — convention).

**Trance:** 8–16-bar snare roll rising in velocity, density and volume (sourced, Wikipedia), out of a beatless 16–32 bar breakdown.

**DnB:** risers, snare rolls and "a beat of silence right before each drop" (sourced, Violet).

**Hip hop / trap / drill:** no EDM build; mark the hook with a 1-beat to half-bar kick+808 dropout, a snare/808 stutter or a reverse cymbal, then crash + kick on step 1 (convention). Rap songs: thin drums in verses, restore at hooks (sourced, Beatstorapon Jersey club).

**Drop / re-entry:** crash + kick + 808 together on step 1; the first bar of a drop should be the most familiar pattern, not a variation.

**Breakdown:** remove kick (and 808) for 4–16 bars, keep hats/perc or go beatless; contrast by subtraction before adding FX (sourced, Mixed In Key). Deep house avoids big builds and drops (sourced, Wikipedia). Bar counts and energy curves: see `music-arrangement`.

## 9. Kit choice, layering and tuning

**Choose by role and frequency space** (sourced: Afrobeats "each element its own frequency range"):

| Element | Choice / layering | Evidence |
|---|---|---|
| Kick with separate 808 | Short, punchy kick; shorten/filter its low tail so only one sub plays | sourced (Beatstorapon) |
| Kick as bass (house/techno) | Long 909-style kick; hard techno "rumble" = reverb tail into distortion, sidechained | sourced (Futureproof) |
| Kick layering | Sub/body layer (~40–100 Hz) + click/top layer (~2–5 kHz); align transients; high-pass the top layer; one sub only | convention (frequencies unverified) |
| Boom bap kick | Two layered samples; small boost ~60 Hz, big dip ~150 Hz | sourced (Attack) |
| Snare + clap | Layer for snap and width; drill: short clap panned slightly L or R | sourced (Audeobox) |
| House clap | 909 + 707 layered, saturated, low end cut; deep tech house 707 clap high-passed below 120 Hz | sourced (Attack) |
| Trap clap | Envelope sustain 0, decay ~280 ms | sourced (NI) |
| Trap hats | High-pass ~500 Hz, low in the mix | sourced (Audeobox) |
| UKG closed hat | Soft, high-passed at 750 Hz; kick tight and punchy, not an EDM sub kick | sourced (Attack; Producer School) |
| Boom bap kit | Dusty, warm, bit-reduced, saturated, filtered highs | sourced (Audeobox) |
| Synthwave | LinnDrum-style kit, gated-reverb snare | sourced (snippet) |
| Phonk | TR-808 kit, cowbell pitched in key, distorted | sourced (Wikipedia) |
| Amapiano log drum | Fruity DX10 preset or layered synth kick + sine + marimba; soft clip | sourced (Splice/Roland) |

**Tuning (convention):** tune the kick fundamental (and 808) to the song's root or fifth; tune the snare body to a chord tone; keep log drums and pitched cowbells in key. In FL, set it directly with `fl_set_channel_pitch_pan_vol(channel, pitch=<cents>)` (±1200 cents): e.g. a kick sample measured at A1 in a G-minor beat → −200 cents. Per-note or per-hit pitch (cowbell melodies, pitched rolls) = MIDI note numbers. 808 tuning and kick/808 strategy: see `music-bass-808`. EQ/compression of drums: see `music-mix-master`.

**Kick–808 lock:** 808 notes start on (or just after) kick steps; sidechain the 808 from the kick (sourced, Audeobox trap/drill).

## 10. Drum MIDI template (tested)

Tested with `uv run --with mido --no-project python make_drums.py` (4 bars at 140 BPM = 6.857 s, no note past the last bar). One .mid per drum channel; all notes at MIDI 60 (FL "C5") so Sampler drums play at their own pitch. Grid rows use the same notation as the reference grids. Swing is baked in (MPC scale); `ms()` converts systematic offsets.

```python
"""Drum MIDI writer: one .mid per drum channel, notes at MIDI 60 (FL "C5").
Run:  uv run --with mido --no-project python make_drums.py
"""
from pathlib import Path
import mido

PPQ, BPM, BARS = 96, 140, 4
STEP = PPQ // 4          # 1/16 = 24 ticks
T16 = PPQ // 6           # 1/16 triplet (FL "1/24") = 16 ticks
T32 = PPQ // 8           # 1/32 = 12 ticks
T8T = PPQ // 3           # 1/8 triplet = 32 ticks
BAR = 16 * STEP
DRUM, HIT = 60, STEP // 2
VEL = {"X": 118, "x": 95, "g": 48, "o": 92, "r": 100}
OUT = Path(__file__).resolve().parent

def s(bar, step, sub=0):            # step 1-16 in bar (0-based) + extra ticks
    return bar * BAR + (step - 1) * STEP + sub

def swing(tick, pct=50, res=STEP):  # MPC-scale: delay 2nd note of each pair
    pair = 2 * res
    return tick + round(pair * (pct - 50) / 100) if tick % pair == res else tick

def ms(x):                          # milliseconds -> ticks
    return round(x / 1000 * BPM / 60 * PPQ)

def grid(row, bar, vel=VEL, pct=50, offset=0, length=HIT):
    cells = row.replace("|", " ").split()
    assert len(cells) == 16, row
    return [(max(0, swing(s(bar, i + 1), pct) + offset), DRUM, length, vel[c])
            for i, c in enumerate(cells) if c != "."]

def roll(start, count, unit, v0=60, v1=110, semis=0):
    out = []
    for i in range(count):
        f = i / max(1, count - 1)
        out.append((start + i * unit, DRUM + round(semis * f),
                    max(1, unit // 2), round(v0 + (v1 - v0) * f)))
    return out

def write(name, notes, bars=BARS):
    end = bars * BAR
    events = []
    for start, pitch, length, vel in notes:
        assert 0 <= start and start + length <= end, f"{name}: note past last bar"
        events.append((start, 1, mido.Message("note_on", note=pitch, velocity=vel)))
        events.append((start + length, 0, mido.Message("note_off", note=pitch, velocity=0)))
    events.sort(key=lambda e: (e[0], e[1]))       # note-offs first at equal ticks
    tr = mido.MidiTrack()
    tr.append(mido.MetaMessage("track_name", name=name, time=0))
    tr.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(BPM), time=0))
    now = 0
    for t, _, msg in events:
        tr.append(msg.copy(time=t - now))
        now = t
    tr.append(mido.MetaMessage("end_of_track", time=end - now))
    mid = mido.MidiFile(ticks_per_beat=PPQ)
    mid.tracks.append(tr)
    mid.save(OUT / f"{name}.mid")
    print(f"{name}.mid: {len(notes)} notes")

# Example: 4-bar trap hats (rolls alternate) + snare 8 ms late with ghost
hats = []
for bar in range(BARS):
    row = "x . x . | x . x . | x . x . | x . . ." if bar % 2 == 0 else \
          "x . x . | x . x . | x . x . | . . . ."
    hats += grid(row, bar, vel={"x": 95})
    if bar % 2 == 0:
        hats += roll(s(bar, 15), 4, T32, 100, 70)            # 1/32 roll, steps 15-16
    else:
        hats += roll(s(bar, 13), 6, T16, 60, 110, semis=5)   # 1/24 roll, pitched up
write("hihat", hats)

snare = []
for bar in range(BARS):
    snare += grid(". . . . | . . . . | X . . . | . . . g", bar, offset=ms(8))
write("snare", snare)
```

Usage notes:
- Swung hats: `grid(row, bar, pct=58)`; swing kick/snare at 8th resolution with `res=2*STEP` if wanted (Attack boom bap: 57% 8ths on kick/snare, 74% 16ths on hats).
- Early hats: `offset=-ms(5)` (clamped at tick 0). Late snare: `offset=ms(10)`.
- Bar variations: build rows per bar from a list, as in the example; add fills by replacing the last bar's row.
- A note that ends past `BARS` makes FL add an extra bar — the `assert` catches it; shorten the roll or the last note.
- Write files next to the script (project folder, e.g. `C:\Users\User\Documents\flstudio\<beat-name>\`), then tell the user which .mid goes on which channel.
