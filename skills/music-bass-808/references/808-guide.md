# 808 guide: tuning, register, slides, length, saturation, genre patterns

Everything needed to write an 808 line that is in tune, sits in the right octave, slides musically and survives phone speakers, plus 16-step 808 patterns for trap, drill, plugg, rage, phonk and boom bap.

## Contents
1. What an 808 is (and why it behaves differently from a bass)
2. Note-to-Hz table, MIDI 24-48, with FL labels and harmonics
3. Register window and the key-root picker
4. Tuning the sample by its tail
5. Writing mode: pitched notes vs drum-style one-shot at MIDI 60
6. Long vs short 808s
7. Slides: FL settings, overlap rules, recipes, budgets
8. Kick + 808 layering options
9. Saturation and phone translation
10. Genre 808 patterns (trap, drill, plugg, rage, phonk, boom bap)
11. Sources

Grid legend (bass rows): `R` root, `O` octave up (R+12), `L` octave down, `3` chord 3rd (b3 in minor), `4` 4th, `5` 5th, `2` 2nd/b2 as stated, `6` 6th/b6 as stated, `7` chord 7th (b7 in minor/dominant), `9` 9th, `A` approach tone, `N` next chord's root, `-` note held, `.` rest. A `Glide` row marks where a slide target starts: `^` up, `v` down (the previous note must overlap it). Kick rows use the family drum notation and give the FL binary string for `fl_set_step_sequencer`. Exact MIDI numbers are in each note list; the list is authoritative.

---

## 1. What an 808 is

- Trap's bass drums are tuned with a long decay so they act as the bass; the technique comes from the Roland TR-808 **(sourced)**.
- An 808 is mostly sine energy with a fundamental around 30-80 Hz depending on the note **(sourced)**. A sine has no harmonics, so a clean 808 is nearly inaudible on phones and laptop speakers. That is the reason for saturation (section 9).
- Most 808 one-shots have a fast downward pitch drop ("knock") in the first ~50-100 ms and then settle. The settled tail is the pitch that matters **(convention)**.
- An out-of-tune 808 and uncontrolled sub energy are among the top reasons hip-hop mixes fall apart **(sourced)**.

## 2. Note-to-Hz table, MIDI 24-48

f = 440 x 2^((m - 69)/12). Scientific name uses C4 = MIDI 60; FL label = scientific octave + 1. Harmonics are the 2nd, 3rd and 4th partials (2f, 3f, 4f), which are what a phone actually plays. All values computed **(derived)**.

| MIDI | Sci | FL label | Hz | 2nd | 3rd | 4th |
|---|---|---|---|---|---|---|
| 24 | C1 | C2 | 32.7 | 65.4 | 98.1 | 130.8 |
| 25 | C#1 | C#2 | 34.6 | 69.3 | 103.9 | 138.6 |
| 26 | D1 | D2 | 36.7 | 73.4 | 110.1 | 146.8 |
| 27 | D#1 | D#2 | 38.9 | 77.8 | 116.7 | 155.6 |
| 28 | E1 | E2 | 41.2 | 82.4 | 123.6 | 164.8 |
| 29 | F1 | F2 | 43.7 | 87.3 | 131.0 | 174.6 |
| 30 | F#1 | F#2 | 46.2 | 92.5 | 138.7 | 185.0 |
| 31 | G1 | G2 | 49.0 | 98.0 | 147.0 | 196.0 |
| 32 | G#1 | G#2 | 51.9 | 103.8 | 155.7 | 207.7 |
| 33 | A1 | A2 | 55.0 | 110.0 | 165.0 | 220.0 |
| 34 | A#1 | A#2 | 58.3 | 116.5 | 174.8 | 233.1 |
| 35 | B1 | B2 | 61.7 | 123.5 | 185.2 | 246.9 |
| 36 | C2 | C3 | 65.4 | 130.8 | 196.2 | 261.6 |
| 37 | C#2 | C#3 | 69.3 | 138.6 | 207.9 | 277.2 |
| 38 | D2 | D3 | 73.4 | 146.8 | 220.2 | 293.7 |
| 39 | D#2 | D#3 | 77.8 | 155.6 | 233.3 | 311.1 |
| 40 | E2 | E3 | 82.4 | 164.8 | 247.2 | 329.6 |
| 41 | F2 | F3 | 87.3 | 174.6 | 261.9 | 349.2 |
| 42 | F#2 | F#3 | 92.5 | 185.0 | 277.5 | 370.0 |
| 43 | G2 | G3 | 98.0 | 196.0 | 294.0 | 392.0 |
| 44 | G#2 | G#3 | 103.8 | 207.7 | 311.5 | 415.3 |
| 45 | A2 | A3 | 110.0 | 220.0 | 330.0 | 440.0 |
| 46 | A#2 | A#3 | 116.5 | 233.1 | 349.6 | 466.2 |
| 47 | B2 | B3 | 123.5 | 246.9 | 370.4 | 493.9 |
| 48 | C3 | C4 | 130.8 | 261.6 | 392.4 | 523.3 |

Reference points: electric bass open E = MIDI 28 (41.2 Hz); 5-string low B = MIDI 23 (30.9 Hz).

## 3. Register window and the key-root picker

No authoritative published number exists for the "right" 808 octave. The window below is **(derived)** from the sourced 30-80 Hz fundamental range plus playback limits. Tune by ear.

| Zone | MIDI | Hz | Use |
|---|---|---|---|
| Hard floor | 24 (C1) | 32.7 | Nothing below. Under ~32 Hz most systems lose output and the note becomes inaudible rumble that eats headroom. |
| Root zone | 26-38 (D1-D2) | 36.7-73.4 | Where the key root and chord roots live. |
| Sweet spot | 28-35 (E1-B1) | 41-62 | Best balance of weight and audibility. |
| Note window | 24-40 (C1-E2) | 32.7-82.4 | All normal 808 notes. |
| Body ceiling | 43-48 (G2-C3) | 98-131 | Only brief visits (octave up-slides). Above this the 808 stops feeling like sub and fights the low-mids. |

**Key-root picker (26-37 rule, derived):** put the key's tonic in the octave that falls inside MIDI 26-37. Each pitch class has exactly one answer:

| Key root | MIDI | Sci (FL) | Hz | Other option |
|---|---|---|---|---|
| C | 36 | C2 (C3) | 65.4 | 24 = C1, 32.7 Hz: deep, only with saturation |
| C#/Db | 37 | C#2 (C#3) | 69.3 | 25 = 34.6 Hz, deep |
| D | 26 | D1 (D2) | 36.7 | 38 = D2, 73.4 Hz, punchier |
| D#/Eb | 27 | D#1 (D#2) | 38.9 | 39 = 77.8 Hz |
| E | 28 | E1 (E2) | 41.2 | 40 = 82.4 Hz |
| F | 29 | F1 (F2) | 43.7 | 41 = 87.3 Hz |
| F#/Gb | 30 | F#1 (F#2) | 46.2 | 42 = 92.5 Hz |
| G | 31 | G1 (G2) | 49.0 | 43 = 98.0 Hz (body ceiling) |
| G#/Ab | 32 | G#1 (G#2) | 51.9 | none in range |
| A | 33 | A1 (A2) | 55.0 | none in range |
| A#/Bb | 34 | A#1 (A#2) | 58.3 | none in range |
| B | 35 | B1 (B2) | 61.7 | none in range |

Placing the other notes:
- **Chord roots:** start from the tonic above, then put each next root in the octave nearest the previous note, staying inside 24-40. On a tie, go down.
- **Riff notes:** build mostly within one octave **(sourced)**. If the root is high in the window (A#, B, C, C#), put riff notes *below* the root (b7, 5th under it) instead of leaving the window **(derived)**.
- **Worked check:** G minor, i-VI-VII = Gm-Eb-F. G1 = 31. Eb nearest 31 is D#1 = 27 (4 away), not 39 (8 away). F nearest 27 is F1 = 29. Line: 31, 27, 29. All inside the sweet spot.

## 4. Tuning the sample by its tail

Raw 808 one-shots are often not tuned to a clean pitch. Most default to C, but verify **(sourced)**.

1. Load the 808 in FL's Sampler (a channel). Play MIDI 60 (FL "C5"): that is the sample at its own pitch.
2. Measure the **sustained tail**, not the attack. Skip the first ~50-100 ms of pitch drop. Use a tuner plugin on the 808's mixer track, or pitch detection in Edison/NewTone, or match by ear against a sine at the target Hz from the table in section 2. The tool names are **(convention; verify in the user's FL 21)**. The file name (e.g. "808 - F") is a hint, not proof.
3. Record the result as a MIDI number plus cents, e.g. "C1 = MIDI 24, -12 cents".
4. Fix the cents offset with `fl_set_channel_pitch_pan_vol(channel_index, volume, pan, pitch)`. Pitch is in cents, so +12 corrects -12 cents. The call also sets volume and pan, so pass the current values (default volume 0.78, pan 0). Leave whole-semitone offsets to the note numbers (section 5).
5. Re-check with a held note at the key root: the tail should read in tune.
6. Every note now lands in key, and slides resolve cleanly **(sourced)**.

Transposition costs tone. The Sampler resamples by default, so pitching up shortens the tail and thins the tone, and pitching down lengthens and darkens it. Keep most notes within about +/-7 semitones of the sample's own pitch, and pick a sample whose root is near the key root **(convention)**.

## 5. Writing mode: pitched notes vs drum-style one-shot at MIDI 60

State the mode and the measured sample pitch in the script's docstring every time.

| Mode | When | What MIDI numbers mean |
|---|---|---|
| **P: pitched** | Synth 808/bass (3x Osc, FLEX, Sytrus, GMS), or a Sampler whose root note has been set to the sample's measured pitch | True pitch. Write F1 as 29. The register checks apply directly. |
| **S: sample-relative (drum-style)** | Sampler one-shot left at FL's default root C5 (MIDI 60). This is the user's usual 808 setup (see `ny-drill-midi/make_midi.py`, BULLY 808 measured at C1). | MIDI 60 = the sample's own pitch. Write `60 + (target - sample_pitch)`. |

Mode S math, with the sample measured at C1 (MIDI 24):
- To sound F1 (29), write 60 + 5 = 65.
- To sound G1 (31), write 67.
- To sound A#0 (22), write 58. That is below the floor, so use A#1 (34) and write 70 instead.
- To sound C2 (36), write 72.

Check the **real** pitch against the window, not the written number. Example from the user's drill script: it wrote Ab as 56 with a C1 sample. The real pitch is MIDI 20 (G#0, 26 Hz), below the floor. G#1 (written 68, real 32, 51.9 Hz) sits in the sweet spot.

Setting the root note (mode P on a Sampler) is done by the user. On the Channel settings keyboard strip, right-click the key matching the measured pitch and choose the set-root-note option **(convention; verify in FL 21)**. Remember the FL label is one octave number higher: MIDI 24 = FL "C2".

**One-pitch shortcut:** if a pattern uses only the root and the sample is already tuned to the key root, the 808 can go through `fl_set_step_sequencer` like a drum. Each hit rings its natural decay, and Mono cuts it at the next hit. Anything with more than one pitch, set lengths or slides goes in a MIDI file.

## 6. Long vs short 808s

| Type | Length | Genres | Rule |
|---|---|---|---|
| Long / legato | Until the next 808 note (fills gaps), 1-8 beats | Melodic trap, drill, phonk, rage, R&B | Continuous sub; needs sidechain or a short kick (section 8) |
| Medium | 2-6 steps | Plugg, afrobeats-trap, boom bap | Leaves the kick room |
| Short / punchy | An 8th or less (~150-300 ms decay) | Bouncy hip hop, Memphis, Jersey club, rage stabs, Brazilian funk | When the kick is busy or vocals need space; must not overlap the next kick |

Sources: the long and short categories and the ~150-300 ms figure are **(convention)** from the research synthesis. Jersey club short envelopes are **(sourced)**.

- Notes closer than ~1 step: cut the first (Mono does this) so the tails don't click **(convention)**.
- Note length in MIDI only matters up to the sample's natural decay. A 4-beat note on a 1-second sample at 70 BPM is silent for part of it, so check the sample length.
- Velocity: keep 808 velocities steady (100-120). An 808 whose notes vary by ~6 dB keeps hitting the master limiter and ducks the whole track **(sourced)**. Use velocity for accent, not dynamics.

## 7. Slides

### FL settings (the user sets these; there is no API for channel settings)
- Channel settings > Miscellaneous functions tab (the manual calls it "Misc"; recent FL versions label the tab FUNC) > **Polyphony**: **Mono** on, **Porta** on, **Slide** knob ~40 (lower = faster) for 140-150 BPM. Use a longer slide at slow tempos **(sourced, producer blog; the knob is unitless)**.
- **Mono** = one voice; overlapping notes transition smoothly. **Porta** = notes slide from the previous note. The **Slide** knob sets glide time **(sourced, Image-Line manual)**.
- **Family rule:** only OVERLAPPING notes are guaranteed to glide. Write every slide as an overlap and every non-slide as a gap or exact touch (end == next start). If separated notes also glide (the manual says Porta glides every new note), switch Porta off and keep Mono: overlapping notes still slide at the Slide time, and separated notes retrigger **(verify by ear on the user's FL 21)**.
- **Native instruments only.** Overlap portamento works on FL's own generators and the Sampler (3x Osc, FLEX, Sytrus, GMS, Sampler). It does NOT work on VST/AU plugins **(sourced)**. For Serum, Vital and similar, use the plugin's own mono/legato/glide settings instead.
- FL piano-roll **slide notes** (glide to the slide note's pitch over the slide note's length) are FL-only data and do not survive a standard MIDI file. Delivered MIDI uses overlap plus Mono/Porta. The user can toggle a note to Slide by hand after import if a timed bend is wanted **(sourced)**.
- The 808 sample needs enough sustain to carry the glide **(sourced)**.

### Writing a slide in MIDI
- Slide target note B starts on the step where the glide should begin. The previous note A (different pitch) is extended to end OVERLAP ticks after B starts. Default overlap is 12 ticks (1/32). Any overlap greater than 0 glides; the glide time comes from the Slide knob.
- Overlap length (a sourced FL slide-note fact): a 1/16 overlap gives a tight slide; a full beat gives a slow bend.
- Never overlap two notes of the **same pitch**: the MIDI note-off becomes ambiguous. Same-pitch legato = touching notes.
- The last slide before the loop end must finish inside the last bar. A note may not end past the last bar, or FL adds a bar. A slide cannot wrap from bar 4 into bar 1, so put the loop-end slide on step 15 or 16 with the target ending exactly at the bar line.

### Budgets and musical rules
- **1-2 slides per bar at most**, used as punctuation at turnarounds and lead-ins. Both notes must be in key **(sourced)**.
- **Drill:** 2-3 slides per 4-bar phrase, mostly upward by a **minor 3rd or perfect 4th**. Signature move: a quick upward slide, then a sustained low note **(sourced)**.
- 1-2 semitone slides sound vocal and subtle; octave slides sound dramatic. Upward slides build tension; downward slides resolve **(sourced)**.
- Faster tempos want snappier glides **(sourced)**.

### Recipes
| ID | Name | Write |
|---|---|---|
| S1 | Octave up-slide | A = root on step 15 (or the held note), B = root+12 on step 16, len 1, A overlaps B. Lead-in to the next bar or loop end. |
| S2 | Drop slide | Hold root+12, slide down to root on the next downbeat. The resolve must stay inside the loop. |
| S3 | Drill whoop | Root on step 4, len 1; target b3 or 4th on step 5, len 1-2; then root again on 8, sustained. |
| S4 | Chord-change glide | Last 16th before a change: the current root slides 1-2 semitones to the next root (plugg, R&B). |
| S5 | 5th lift | Root slides up +7 on an offbeat, then retriggers the root (drill, trap fills). |

## 8. Kick + 808 layering options

**(convention)**. Choose one per section. Strategy detail is in `kick-bass-low-end.md`.

| Option | How | When |
|---|---|---|
| A: kick on every 808 start | Kick high-passed ~40-50 Hz so the 808 owns the sub; the kick gives click and punch. Align transients: trim the 808 start or nudge so the first cycles reinforce. | Trap and drill default; long 808s |
| B: 808 is the kick | No separate kick on 808 hits; the 808's own knock is the transient. | Classic 808, phonk, sparse beats |
| C: sidechain | 808 ducks a few dB under each kick (Fruity Limiter sidechain). | Busy kick under sustained 808s |

The sourced foundation: an 808 hit under each kick, plus 1-2 syncopated notes in the gaps. Fewer, well-placed notes sound bigger **(sourced)**.

## 9. Saturation and phone translation

- A clean sub fundamental can vanish on a phone. Saturation adds upper harmonics that make the line audible; keep the deepest bass centred **(sourced)**.
- The ear infers a missing fundamental from its harmonics, so 98/147/196 Hz implies a 49 Hz G1 that the phone cannot play **(sourced; harmonic numbers derived)**.
- Small speakers roll off hard below ~150-200 Hz **(sourced)**. Phone translation depends on the 2nd-4th harmonics in the table in section 2.
- **Clean sub + saturated layer (derived from sourced advice):** route the 808 channel to mixer track "808". Send it (`fl_route_track`) to two child tracks:
  - "808 SUB": low-pass ~100 Hz, no distortion, mono.
  - "808 DRIVE": high-pass ~100-150 Hz, then Fruity Blood Overdrive / Fruity WaveShaper / Fruity Soft Clipper, then low-pass ~2-5 kHz to remove fizz.
  The user dials the EQ and plugins in; there is no mixer-EQ API.
- **One-track version:** gentle saturation or soft clip on the whole 808 (phonk, rage, drill style "dirty 808").
- Genre amount: plugg and R&B = clean or light; trap and drill = moderate; rage, phonk and Brazilian funk = heavy, clipped **(sourced genre descriptions; amounts convention)**.
- Always do the phone check: play the loop on a phone or laptop speaker. If the 808 line disappears, add drive or the mid layer.
- Mixing detail (levels, clipper settings, loudness): see `music-mix-master`.

## 10. Genre 808 patterns

Tempo in BPM. All grids are one bar unless shown as two. The kick row is the reference the 808 is written against; the full drum kit lives in `music-drums-groove`. Placements are **(convention)** except where marked.

### Trap basic: follows the kick (K1 lock), 130-150, default 140
Example in A minor: Am | F | G | Am, roots 33 / 29 / 31 / 33.
```
Kick   X . . . | . . . x | . . x . | . . . .     1000000100100000
808    R - - - | - - - R | - - R - | - - - O
Glide  . . . . | . . . . | . . . . | . . . ^     (bars 2 and 4 only)
```
Notes per bar: (1, R, len 7, vel 120), (8, R, len 3, 110), (11, R, len 5, 112). In bars 2 and 4, step 11 overlaps (16, R+12, len 1, 115, slide). Bar 2 slide: F1 29 to F2 41; bar 4: A1 33 to A2 45. The slide note ends exactly on the bar line. Sourced shape: 808 on 1, 8 or 9 and 11, following the kick, with the last note sliding up an octave **(sourced)**.

### Trap sparse: space for vocals, 130-150
Example in F minor: Fm, root F1 29; b7 below = D#1 27; octave = F2 41.
```
Kick   X . . . | . . . . | . . x . | . . . .     1000000000100000
808    R - - - | - - . . | . . 7 - | - R O -
Glide  . . . . | . . . . | . . . . | . . ^ .
```
Notes: (1, 29, len 6), (11, 27, len 3), (14, 29, len 1 + overlap), (15, 41, len 2, slide). Variant: replace the b7 with the 5th (C2 36 or C1 24).

### Drill (UK/NY): 138-151, default 142; slides essential
Example in G minor (G1 31; b3 Bb = A#1 34; 4th C = C2 36; b6 Eb = D#1 27; b7 F = F1 29). Drill keys are most often C or G minor **(sourced)**.
```
            Bar 1                                       Bar 2
Kick   X . . . | . . . . | . . x . | . . . .    X . . . | . . x . | . . . . | . . x .
808    R - - R | 4 - . R | - - 3 - | - - R -    R - 3 - | . . R - | - - 6 - | - - 7 -
Glide  . . . . | ^ . . . | . . . . | . . . .    . . ^ . | . . . . | . . . . | . . . .
Kick FL (2 bars): 10000000001000001000001000000010
```
- Bar 1: (1, 31, len 3), (4, 31, len 1 + overlap), (5, 36, len 2, slide = P4 up), (8, 31, len 3: sustained low note after the whoop), (11, 34, len 4), (15, 31, len 2).
- Bar 2: (1, 31, len 2 + overlap), (3, 34, len 2, slide = m3 up), (7, 31, len 4, with kick), (11, 27, len 4, b6 implies VI), (15, 29, len 2, b7 leads home).
- In a 4-bar phrase, bar 3 = bar 1 and bar 4 = bar 2 with the step-3 slide removed (plain note). That gives 3 slides per 4 bars **(sourced budget)**. This exact 4-bar line is the tested example in `bass-midi-delivery.md`.
- 808 notes land with the kick or one 16th after; kicks are not placed under every 808 note **(sourced)**.
- UK drill uses longer, controlled glides and colder motifs; NY/Brooklyn uses heavier glides and simpler minor-triad loops; Chicago keeps the 808 sustained and fairly static with fewer slides **(sourced)**.

### Plugg / pluggnb: 130-150; clean, sine-like 808, short slides into chord changes
Example in G major, descending: Cmaj9 | Bm7 | Am9 | Gmaj9, roots C2 36, B1 35, A1 33, G1 31.
```
Kick   X . . . | . . . . | . . x . | . . x .     1000000000100010
808    R - - - | - - . . | . . R - | - - R N
Glide  . . . . | . . . . | . . . . | . . . v     (bars 1-3; bar 4 retriggers)
```
Notes per bar: (1, R, len 6), (11, R, len 4), (15, R, len 1 + overlap), (16, next root, len 1, slide). Slides: 36 to 35 (-1), 35 to 33 (-2), 33 to 31 (-2). Bar 4 has no slide (G to C is a P4 leap; let it retrigger). Pluggnb often puts slash-chord bass notes under extended chords; follow the chord symbol's bass note if one is given (see `music-chords-voicing`).

### Rage: 140-170, loops ~150-160; distorted, long, often doubled with kick hits
Example in E minor: E1 28 (41.2 Hz; heavy drive puts harmonics at 82/124/165 Hz).
```
Kick   X . . . | . . . . | . . X . | . . . .     1000000000100000
808    R - - - | - - - - | - - R - | - - 5 -
```
Notes: (1, 28, len 10), (11, 28, len 4), (15, B1 35, len 2). Every 4th bar, change step 15 to an octave slide (E2 40). Rage 808s are pitched to the lead melody: when the lead loop outlines b3/5/b7, let the 808 follow those notes (G1 31, B1 35, D2 38) **(sourced: "pitched to melody"; notes derived)**.

### Phonk: drift 130-160, Memphis ~120-140 (often slower), Brazilian 130-150; distorted, long
Drift example in F phrygian: F1 29, b2 = F#1 30, b7 = D#1 27.
```
Kick   X . . . | . . x . | X . . . | . . x .     1000001010000010
808    R - - - | - - R - | R - - - | - - 2 -
```
Notes: (1, 29, len 6), (7, 29, len 2), (9, 29, len 6), (15, 30, len 2: the b2 tension). Alternate bars: step 15 = b7 (27). Locked to every kick (K1), or option B (the 808 is the kick).

Brazilian / funk-style:
```
Kick   X . . x | . . x . | X . . x | . . x .     1001001010010010
808    R - . R | - . R - | R - . R | - . 7 -
```
Short 808 hits (len 1-2) on every kick, root with b7/b2 pickups, heavily clipped.

Memphis: slower, darker, long 808s on 1 and 9 with the cowbell carrying the melody. The cowbell line is a lead, so see `music-melody-hooks`.

### Boom bap: 85-95; short, roots and 5ths
```
Kick   X . . . | . . . x | . . x . | . . . .     1000000100100000
Bass   R - - . | . . . 5 | - . R - | . . . .
```
Notes: (1, R, len 3), (8, 5th, len 2), (11, R, len 2). Bass and kick lock. Upright or electric bass tone suits boom bap better than an 808 (see the lo-fi style in `bassline-styles.md`).

### Quick genre table
| Genre | 808 length | Slides | Saturation | Strategy |
|---|---|---|---|---|
| Trap | long | 0-1 per bar, octave lifts | moderate | K1 / option A |
| Drill | long + whoops | 2-3 per 4 bars, m3/P4 up | moderate | 808 with or just after kick |
| Plugg | medium | short, 1-2 st into changes | clean | K1 |
| Rage | long | rare | heavy, clipped | doubled with kick |
| Phonk | long (drift), short (Brazilian) | rare | heavy | K1 / option B |
| Jersey club | short, must not overlap the next kick (sourced) | none | moderate | K1 |
| Boom bap | short | none | light | K1 |

## 11. Sources

- Wikipedia, "Trap music": https://en.wikipedia.org/wiki/Trap_music
- Amped Studio, 808 bass (search summary): https://www.ampedstudio.com/blog/secrets-of-808-bass/
- Violet Recording, 808 slides / patterns / hit harder / mix 808s / master hip hop: https://violetrecording.com/how-to-make-808-slides/ , /how-to-make-808-patterns/ , /how-to-make-808s-hit-harder/ , /how-to-mix-808s/ , /how-to-master-hip-hop/
- Image-Line manual, Channel settings Misc (Mono/Porta/Slide, VST limitation): https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/chansettings_misc.htm
- Image-Line manual, Piano roll slide notes: https://flstudio.image-line.com/help/html/pianoroll.htm
- Audeobox, trap / drill in FL Studio: https://www.audeobox.com/learn/fl-studio/how-to-make-trap-beats-in-fl-studio/ , /how-to-make-drill-beats-in-fl-studio/
- Beatstorapon, drill beat (saturation for phones): https://beatstorapon.com/blog/how-to-make-a-drill-beat-bpm-808s-drums/
- Wikipedia, "Missing fundamental": https://en.wikipedia.org/wiki/Missing_fundamental
- Genre descriptions (drill lanes, plugg, rage, phonk, Jersey club): orphiq.com, splice.com, Wikipedia "Rage rap" and "Phonk", via the research notes `genres_hiphop_urban_global.md`.
- Producer-blog numbers (Slide ~40, slide budgets) are rules of thumb, not standards.
