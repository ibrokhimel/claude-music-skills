# Bassline styles: note-choice rules and 15 genre patterns

The detailed note-choice rules (root on change, interval priority, approach tones, walking, pedals, 3rds), followed by 15 bassline styles. Each style gives a 16-step grid against its kick, exact MIDI notes in a worked key, lengths, velocities, sound and pitfalls.

## Contents
1. Legend
2. Note-choice rules in detail
3. Styles 1-15: pop/rock root 8ths; house offbeat (+ tech-house rolling); techno rumble; funk/slap; disco octaves; reggae one drop; Motown/walking; R&B/neo-soul; DnB reese; dubstep wobble; UK garage; afrobeats; amapiano log drum; synthwave arp bass; lo-fi upright
4. Sources

## 1. Legend

Grid cells: `R` root, `O` octave up, `L` octave down, `3` chord 3rd, `5` 5th, `7` chord 7th (b7 in minor/dominant), `9` 9th, `2` 2nd (b2 where stated), `6` 6th (b6 where stated), `A` approach tone, `g` ghost note (vel 20-40), `-` held, `.` rest. Kick rows use the family notation plus the FL binary string. Positions are steps 1-16. Lengths are in steps (1 step = 24 ticks at PPQ 96). Worked examples give true MIDI pitch (mode P, see `808-guide.md` section 5). Step placements are **(convention)** unless marked; MIDI numbers are computed.

Bass (non-808) register: MIDI 28-52 (E1-E3); a sub layer can sit an octave below the mid-bass **(derived)**.

## 2. Note-choice rules in detail

**Why:** the bass decides which chord the listener hears. C-E-G-B in the pads over an A in the bass is heard as Am9, not Cmaj7 **(derived)**. The kick is purely rhythmic; the bass is rhythm plus the melodic foundation **(sourced)**.

| Rule | Do this | Why / source |
|---|---|---|
| R1 Root on change | Play the new chord's root on the first step of every chord (usually step 1, or step 9 for two chords per bar). | Root and 5th state the chord most strongly; beats 1 and 3 matter most because chords change there **(sourced)**. |
| R2 Interval priority | For other notes: root > octave (+12) > 5th (+7) > 4th (+5) / b7 (+10) > 3rd > other scale tones > chromatic. | Stability ranking **(convention)**. |
| R3 Octave bounce | Alternate R and R+12 for motion without new harmony. | Disco, house, trap slides **(convention)**. |
| R4 Approach tone | On step 15 or 16 before a change (or step 7/8 before a mid-bar change), play a short note leading into the NEXT root. | Walking recipe: chromatic approach on beat 4 from a half step above or below **(sourced)**. |
| R5 Pedal tone | Hold or repeat one note (tonic, sometimes the 5th) while chords move above. | Builds, intros, techno, drill **(convention)**. Best when the chords contain or resolve to that note. |
| R6 No low doubled 3rd | Keep pads' lowest note at or above MIDI 48 when the bass is busy. | Mud in 200-400 Hz **(convention)**; voicing is in `music-chords-voicing`. |
| R7 Walking | One note per beat: R, 3rd or scale step, 5th, approach. | **(sourced recipe)** |
| R8 Pentatonic riff | In trap, drill and lo-fi, a riff from 1, b3, 4, 5, b7 can imply the chords loosely. | **(convention)** |

**Approach-tone types** (all weak-step, short):
- Chromatic below: next root - 1 (G#1 32 into A1 33).
- Chromatic above: next root + 1 (A#1 34 into A1 33).
- Double chromatic from above: next root +2, +1, then the root (B, A#, A) **(sourced)**.
- Dominant: the next root's 5th (E into A).
- Diatonic: the scale step next to the next root.

**3rds in the bass:** they sound melodic or inverted. Use them as passing notes on weak steps, or deliberately for a first-inversion slash chord (C/E) to make a stepwise descending line (C - C/B - Am - Am/G). Never hold a 3rd under a chord change by accident.

**Pedal tones:** hold the tonic through i-VI-VII-i for an 8-bar intro, then release to moving roots at the hook. That gives contrast at almost no cost. In builds, repeat the pedal as 8ths, then 16ths (see `music-arrangement` for build schedules).

**Minor vs major colour:** "3" means b3 in minor chords and natural 3 in major chords. "7" means b7 in minor and dominant chords and natural 7 in maj7 chords. Always read the chord symbol.

---

## 3. Styles

### 1. Pop/rock root 8ths (90-130 BPM; K1 lock)
```
Kick   X . . . | . . . . | X . x . | . . . .     1000000010100000
Bass   R - R - | R - R - | R - R - | R - A -
```
- Notes: R on every odd step, length 1.5 steps (36 ticks), slightly detached. New root exactly on the change. An optional A on step 15 before a change.
- Worked, C major I-V-vi-IV (C | G | Am | F): C2 36, G1 31, A1 33, F1 29. Approaches on step 15: into G = F#1 30; into A = G#1 32; into F = E1 28; into C (loop) = B1 35.
- Velocity 100-110, downbeats +10. Sound: electric bass or a saw/square bass low-passed ~800 Hz-1.5 kHz.
- Variation: the octave on steps 7 and 15 (R R R O pattern) for chorus lift.

### 2. House offbeat (120-128; K2 gaps) + tech-house rolling
```
Kick   X . . . | X . . . | X . . . | X . . .     1000100010001000
Bass   . . R - | . . R - | . . R - | . . R -
Alt    . . R - | . . O - | . . R - | . . O -     (two-note alternation)
```
- The offbeat bass sits between four-on-the-floor kicks and descends from disco and hi-NRG. It often alternates only two notes while still supporting chord changes **(sourced)**. It is one of the most-used tech-house patterns **(sourced)**.
- Worked, A minor (Am | F | C | G): A1 33 / A2 45, F1 29 / F2 41, C2 36 / C3 48, G1 31 / G2 43.
- Length 1-2 steps, vel 100-115. Sound: saw, sharp attack, ADSR sweeping a low-pass downward, release raised slightly to avoid clicks **(sourced)**. Little sidechain needed.
- **Tech-house rolling:**
  ```
  Bass   . R R R | . R R R | . R R R | . R R R
  ```
  One note (e.g. G1 31), length 1, accents (110) on 3/7/11/15, others 85. Short filter-envelope pluck, heavy sidechain.

### 3. Techno rumble (130-140; hard techno 145-160)
```
Kick    X . . . | X . . . | X . . . | X . . .    1000100010001000
Rumble  . ~ ~ ~ | . ~ ~ ~ | . ~ ~ ~ | . ~ ~ ~    (tail ducked by each kick)
```
- Not a note pattern. The rumble is the kick fed into reverb, then distortion, then EQ (high-pass ~30 Hz, low-pass ~150-250 Hz), sidechained to the dry kick so it swells in the gaps **(sourced: rumble kick = reverb into distortion; filter values convention)**.
- Pitch: tune the kick to the track's tonic so the rumble is a pedal, e.g. F1 29 (43.7 Hz). A synth version plays a pedal note on steps 2-4, 6-8, 10-12 and 14-16, gated by the kick.
- One pedal for 8-16 bars. Change via filter and FX automation, not notes. Peak-time adds 303-style acid lines above the rumble (separate part).

### 4. Funk / slap (95-115; interlocks with the drums)
```
Kick   X . . x | . . . . | . . x . | . . . .     1001000000100000
Snare  . . . . | X . . . | . . . . | X . . .
Bass   R - g O | . g 7 O | . . R g | . 5 7 A
```
- Worked, E7 / Em7 vamp: (1, E1 28, len 2, vel 120), (3, 28, len 0.5, ghost 30), (4, E2 40, len 1, 100), (6, 40, len 0.5, ghost 30), (7, D2 38, len 1, 105), (8, E2 40, len 1, 95), (11, E1 28, len 1, 110), (12, 28, len 0.5, ghost 30), (14, B1 35, len 1, 100), (15, D2 38, len 1, 105), (16, F1 29, len 1, 95). The final F1 is a chromatic approach from above into E1 on the next downbeat.
- Ghost notes are muted percussive plucks before real notes; they act like a second drum part **(sourced)**. Velocity contrast is the style: accents 110-127, ghosts 20-40.
- Rests on the snare steps (5, 13) leave the backbeat clear. Sound: bright electric or slap bass, fast attack, presence around 900 Hz-1.5 kHz.

### 5. Disco octaves (115-125; K1 on kicks, octaves on offbeats)
```
Kick   X . . . | X . . . | X . . . | X . . .     1000100010001000
Bass   R - O O | R - O O | R - O O | R - O O
```
- Octaves are the disco signature, often an 8th followed by a 16th on the upper note **(sourced)**.
- Worked, A dorian vamp Am7 | D7: bar 1 R = A1 33, O = A2 45; bar 2 R = D2 38, O = D3 50. Approach on the last step of bar 2 into A1: G#1 32 replaces the final O.
- Lengths: R 2 steps, O 1 step, vel R 110, O 95-100. Sound: round, picked electric bass or a pluck synth.

### 6. Reggae one drop (65-80; bass avoids beat 1)
```
Kick+Rim . . . . | . . . . | X . . . | . . . .   0000000010000000
Bass     . . R - | - - . . | R - 3 5 | - . 7 -
```
- Reggae bass gets its character from avoiding beat 1 and using rests. The one drop puts the weight on beat 3 **(sourced)**.
- Worked, A minor (Am | D, dorian): bar Am: (3, A1 33, len 4), (9, 33, len 2, vel 115), (11, C2 36, len 1), (12, E2 40, len 2), (15, G1 31, len 2). Bar D: (3, D2 38, len 4), (9, 38, len 2), (11, F#2 42, len 1), (12, A2 45, len 2), (15, B1 35, len 2), which steps down into the A on the next bar.
- Sound: round, low-passed ~600-1000 Hz, soft attack, the loudest element. **Dub:** the same with more space, 1-2 bar bass dropouts, echo on other parts (never on the sub).

### 7. Motown / walking (100-130; one note per beat)
```
Kick   X . . . | . . . . | X . . . | . . . .     1000000010000000
Bass   R - - - | 3 - - - | 5 - - - | A - - -
```
- Worked, C | Am | Dm | G (I-vi-ii-V), quarter notes, legato:
  - C: C2 36, E2 40, G2 43, G#2 44 (into A)
  - Am: A2 45, G2 43, E2 40, D#2 39 (into D)
  - Dm: D2 38, F2 41, A2 45, G#2 44 (into G)
  - G: G2 43, F2 41, D2 38, B1 35 (into C)
- Beats 1 and 3 carry the root and 5th in every bar. Every beat 4 is a half step from the next root (R7, **sourced recipe**).
- Motown feel: add an 8th pickup on step 15 and syncopated 8ths; Jamerson-style lines are busier than strict walking. Vel 95-110, finger bass tone.

### 8. R&B / neo-soul (65-95; sparse, behind the beat)
```
Kick   X . . . | . . . x | . . x . | . . . .     1000000100100000
Bass   R - - - | - - . 5 | - . R - | - . 9 A
```
- Worked, Fmaj7 | Em7 | Dm7 | Cmaj7 (IV-iii-ii-I in C):
  - Fmaj7: (1, F2 41, len 6), (8, C2 36, len 2), (11, 41, len 3), (15, G2 43, len 1), (16, F2 41: approach from above into E)
  - Em7: 40, B1 35, 40, F#2 42, D#2 39 (into D)
  - Dm7: 38, A1 33, 38, E2 40, C#2 37 (into C)
  - Cmaj7: 36, G1 31, 36, D2 38, E2 40 (into F, from below)
- Root on the change always, even under extended chords. 9ths and 7ths only as passing notes. Swing 55-60% (MPC scale) or late placement +5-15 ms. Optional 1-2 semitone slides into the change (synth bass or a Mono/Porta 808).
- Sound: warm synth bass, Moog-style, or an 808 tuned to chord roots **(sourced)**.

### 9. DnB reese (170-176; sub + reese, notes change every 1-2 bars)
```
Kick   X . . . | . . . . | . . x . | . . . .     1000000000100000
Snare  . . . . | X . . . | . . . . | X . . .
Sub    R - - - | - - - - | - - - - | - - - -
Reese  R - - - | - - . R | - . R - | - - - -
```
- Worked, F minor, Fm (2 bars) | Ab | Bbm: sub = F1 29, G#1 32, A#1 34, whole bars. Reese = the same notes +12 (F2 41, G#2 44, A#2 46): (1, len 6), (8, len 2), (11, len 6).
- The Reese came from Kevin Saunderson's late-1980s "Reese" project: two detuned oscillators, commonly saws at about +/-25 cents **(sourced)**. Movement comes from filter, detune and automation, not from the note grid.
- Sub = mono sine. Reese high-passed ~100-150 Hz, can be wide. Neurofunk resamples and edits the mid bass every half bar over a constant low component **(sourced)**.

### 10. Dubstep wobble (140, half-time; snare on 9)
```
Kick    X . . . | . . . . | . . . . | . . . .    1000000000000000
Snare   . . . . | . . . . | X . . . | . . . .
Sub     R - - - | - - - - | . . R - | - - - -
Wobble  R - - - | - - - - | . . R - | 2 - - -
```
LFO rate on the wobble: 1/8 for steps 1-8, 1/16 for steps 11-12, 1/8T for steps 13-16.
- Worked, F minor/phrygian: wobble F2 41 (1, len 8), (11, len 2), then F#2 42 (b2) (13, len 4). Sub = F1 29 (1, len 8), (11, len 6). The sub either doubles each mid note an octave down or holds the root as a pedal when the mid moves chromatically.
- Wobble = filter cutoff (or volume/distortion) modulated by a tempo-synced LFO **(sourced)**; change the LFO rate per bar (1/4, 1/8, 1/8T, 1/16).
- Keep the sub a separate clean sine. **Riddim:** one simple mid-bass motif, often in triplets, with deliberate gaps **(sourced)**.

### 11. UK garage / 2-step (128-134; syncopated, swung)
```
Kick   X . . . | . . . . | . . x . | . . . .     1000000000100000
Bass   R - - O | - . 5 - | . . R - | - . A -
```
- Worked, G minor, Gm7 | Ebmaj7:
  - Gm7: (1, G1 31, len 3), (4, G2 43, len 2), (7, D2 38, len 2), (11, 31, len 3), (15, F1 29, len 2: into Eb)
  - Ebmaj7: (1, D#1 27, len 3), (4, D#2 39, len 2), (7, A#1 34, len 2), (11, 27, len 3), (15, F1 29, len 2: into G)
- 2-step = a kick that skips beats and syncopated basslines **(sourced)**. Octave and 5th jumps, often with short portamento: Mono/Porta on, overlap the jump to step 4. Match the drums' heavy swing (see `music-drums-groove`).
- Sound: deep sub or warm filtered reese (future garage) **(sourced)**; speed-garage organ bass for the bouncy variant.

### 12. Afrobeats (95-115, default ~108; tresillo feel)
```
Kick   X . . . | . . x . | x . . . | . . . .     1000001010000000
Bass   R - - - | . . R - | - . . . | 5 - A .
```
- Worked, G major I-V-vi-IV (G | D | Em | C):
  - G: (1, G1 31, len 4), (7, 31, len 3), (13, D2 38, len 2), (15, C#2 37, len 1: into D)
  - D: 38, 38, A1 33, D#2 39 (into E)
  - Em: 40, 40, B1 35, C#2 37 (into C, from above)
  - C: 36, 36, G1 31, F#1 30 (into G)
- Steps 1, 7 and 13 are the pure tresillo (3+3+2). Afrobeats bass is warm and round, between C1 and E2 (MIDI 24-40), on chord roots **(sourced)**. Short-to-medium notes, vel 95-110, gentle swing matching the shakers.

### 13. Amapiano log drum (108-115, default ~112; between the kicks)
```
Kick     X . . . | X . . . | X . . . | X . . .   1000100010001000
Log A    . . . R | - . L - | . . 5 - | . R . 7   (bar 1: call)
Log B    . . R - | . 3 - . | R - L - | . . . 5   (bar 2: answer)
```
- The log drum is a hybrid of kick, 808, synth bass and percussion. It bounces between kicks, not on them, with pitch variation; "without the log drum, it's not amapiano" **(sourced)**. Two-bar phrase: bar 1 states, bar 2 answers **(sourced)**. Pattern A uses steps 4, 7, 11, 14, 16; pattern B is the research card's 3, 6, 9, 11, 16 **(convention)**.
- Worked, Em9 (2 bars) | Cmaj7 (2 bars):
  - Em, bar A: (4, E2 40, len 2), (7, E1 28, len 2), (11, B1 35, len 2), (14, 40, len 1), (16, D2 38, len 1)
  - Em, bar B: (3, 40, len 2), (6, G2 43, len 2), (9, 40, len 2), (11, 28, len 2), (16, 35, len 1)
  - Cmaj7: R = C2 36, L = C1 24, 3 = E2 40, 5 = G1 31, 7 = B1 35, same rhythms
- Sound: Fruity DX10 contains the original log-drum preset **(sourced)**. Alternatively layer a synth kick, sine and marimba/synth bass with a fast pitch drop. Layer a sub with identical ADSR, phase-aligned. Don't cut the log drum's lows. Drive with Fruity WaveShaper or a soft clipper **(sourced)**. An untuned log drum destabilises the track, so tune it **(sourced)**. A separate sub bass is sparse or absent.

### 14. Synthwave arp bass (80-118, default ~100; straight, no swing)
```
Kick   X . . . | X . . . | X . . . | X . . .     1000100010001000
Bass   R O R O | R O R O | R O R O | R O R O     (16th R/O)
Alt    R - R - | R - R - | R - R - | R - R -     (straight 8ths)
```
- Worked, A minor i-VI-III-VII (Am | F | C | G): A1 33 / A2 45, F1 29 / F2 41, C2 36 / C3 48, G1 31 / G2 43.
- Octave-pulsing 8th or 16th saw bass that follows the roots exactly **(sourced)**. Length 1 step (90% gate), vel 100 / 90 alternating.
- Sound: saw, low-pass with a tight filter envelope, light sidechain. A square-wave pulse bass is the alternative **(sourced, snippet-level)**.

### 15. Lo-fi upright (70-90; swung, sparse root-5th)
```
Kick   X . . . | . . . x | . . x . | . . . .     1000000100100000
Bass   R - - - | . . . 5 | - . R - | . . A .
```
- Worked, Dm7 | G7 | Cmaj7 | A7 (ii-V-I-VI7):
  - Dm7: (1, D2 38, len 4), (8, A1 33, len 2), (11, 38, len 2), (15, G#1 32, len 1: into G)
  - G7: 31, D2 38, 31, C#2 37 (into C)
  - Cmaj7: 36, G1 31, 36, A#1 34 (into A)
  - A7: 33, E2 40, 33, C#2 37 (into D; also A7's 3rd)
- Swing 55-65% (MPC scale). Velocity 70-110, varied. Upright sound: low-passed ~800 Hz, soft attack, short release, slight pitch drift **(convention)**.
- Boom bap is the same idea with shorter notes, roots and 5ths only, locked to the kick (see `808-guide.md`).

---

## 4. Sources

- The Jazz Piano Site, walking bass lines (root/5th importance, beats 1 and 3): https://www.thejazzpianosite.com/?p=483
- TalkingBass, walking bass lines made easy: https://www.talkingbass.net/walking-bass-lines-made-easy/ ; disco octaves: https://www.talkingbass.net/disco-bass-octaves/ ; ghost notes: https://www.talkingbass.net/bass-technique-ghost-notes/
- Bass Musician Magazine (double chromatic approach): https://bassmusicianmagazine.com/?p=110823
- Attack Magazine, eight bassline styles (offbeat bass): https://www.attackmagazine.com/technique/tutorials/low-end-theory-exploring-eight-common-bassline-styles/
- The Producer School, tech-house bass: https://theproducerschool.com/blogs/featured-blogs/master-modern-tech-house-bass-lines-complete-tutorial-guide
- Soundfingers, reggae/dub bass: https://soundfingers.com/techniques/authentic-reggae-dub-bass-tutorial/
- Wikipedia, Drum and bass (Reese origin): https://en.wikipedia.org/wiki/Drum_and_bass ; eMastered, Reese bass: https://emastered.com/blog/reese-bass
- Dubspot, dubstep wobble: https://blog.dubspot.com/video-tutorial-making-a-dubstep-bass-in-ableton-live ; Wikipedia, Dubstep / 2-step garage / UK garage / Neurofunk
- Futureproof Music School, hard techno rumble kick (via `genres_electronic_pop_cinematic.md`)
- Beatstorapon, amapiano: https://beatstorapon.com/blog/how-to-make-amapiano-beat/ ; RouteNote amapiano: https://create.routenote.com/blog/beatmakers-guide-how-to-make-an-amapiano-beat/ ; Splice, amapiano (DX10 log drum): https://splice.com/blog/what-is-amapiano-music/
- Audeobox, Afrobeats in FL Studio (round bass C1-E2): https://www.audeobox.com/learn/fl-studio/how-to-make-afrobeats-in-fl-studio/
- Violet Recording, R&B beats (808 tuned to chord roots): https://violetrecording.com/how-to-make-rnb-beats/
- Step placements for amapiano, afrobeats, synthwave, lo-fi, reggae and garage are a synthesis of genre descriptions, not verbatim from a published chart.
