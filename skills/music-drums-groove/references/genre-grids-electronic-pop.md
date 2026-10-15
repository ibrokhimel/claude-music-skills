# Genre drum grids: electronic, pop, rock and funk

16-step grids with FL binary strings, BPM, swing and velocities for house, deep/tech/afro house, techno (peak, rolling, hard), trance, DnB (incl. Amen-style), dubstep/riddim, UK garage and 2-step, future bass, synthwave, pop, rock, funk, breakbeat and hyperpop.

## Contents
1. Reading the grids
2. House (classic / Chicago)
3. Deep house
4. Tech house / deep tech house
5. Afro house
6. Techno (peak-time, rolling, hard)
7. Trance
8. Drum & bass (two-step, Amen-style, liquid, neuro, jungle)
9. Dubstep / riddim
10. UK garage (4x4 and 2-step)
11. Future bass
12. Synthwave
13. Pop (dance-pop, mid-tempo, trap-pop)
14. Rock
15. Funk
16. Breakbeat
17. Hyperpop
18. Sources

---

## 1. Reading the grids

Same notation as `genre-grids-hiphop-global.md`: `X` 110–127, `x` 85–105, `g` 35–60, `o` open hat, `r` roll start, `.` rest; the 16-char string = `fl_set_step_sequencer` pattern (non-`.` = `1`); concatenate `b1`+`b2` for 2-bar patterns. Swing is MPC/Linn scale unless marked "DAW scale". Ghost/velocity rows need MIDI delivery to sound right. Evidence tags: (sourced), (sourced, snippet) = seen only in a search summary, (convention), (derived).

---

## 2. House (classic / Chicago)

- **BPM:** 120–125 (sourced, Attack "21st-century Chicago house"); classic 120–126; default 124.
- **Swing:** 55–60% (sourced, Attack); swing on the rimshot "dramatically affects groove". FL: start ~20–30% on rim/hats/perc channels.
- **Elements (sourced, Attack/MusicRadar):** four-on-the-floor kick; 16th closed hats with varying velocity; open hat on offbeats with length set to ease into the clap; tambourine on every offbeat (two detuned copies panned L/R); syncopated rim; layered 909+707 clap.

```
Kick      X . . . | X . . . | X . . . | X . . .   1000100010001000
Clap      . . . . | X . . . | . . . . | X . . .   0000100000001000
ClHat     x g . g | x g . g | x g . g | x g . g   1101110111011101
OpHat     . . o . | . . o . | . . o . | . . o .   0010001000100010
Tamb      . . x . | . . x . | . . x . | . . x .   0010001000100010
Rim       . . . x | . . x . | . . . . | . x . .   0001001000000100
Kick b4   X . . . | X . . . | X . . . | X . g .   1000100010001010
```

- **Velocities:** kick 115–120; clap 110; closed hats 90 on beats, 50–60 on e/a; open hat 95; tamb 70; rim 80 (positions convention).
- **Turnaround (sourced, Attack):** in the last bar of the phrase add a reduced-velocity kick on the final offbeat (`Kick b4`, step 15 at ~80).
- **Choke:** open hat in the same cut group as the closed hat (optional, sourced).

## 3. Deep house

- **BPM:** 110–125 (sourced, Wikipedia); default 120–122.
- **Swing:** 55–62% (convention).
- **Character (sourced, Wikipedia):** spacious 909 percussion, muted bass, steady hypnotic repetition that avoids big build/release moments.

```
Kick      X . . . | X . . . | X . . . | X . . .   1000100010001000
Clap      . . . . | x . . . | . . . . | x . . g   0000100000001001
OpHat     . . o . | . . o . | . . o . | . . o .   0010001000100010
Shaker    x g x g | x g x g | x g x g | x g x g   1111111111111111
Rim       . . . g | . . x . | . g . . | . . x .   0001001001000010
```

- **Velocities:** kick 110; soft clap/rim 90, ghost 45; open hat 80 (low-passed); shaker 70/40 with varied velocity; closed hats often absent.

## 4. Tech house / deep tech house

- **BPM:** tech house 123–126 (sourced, snippet); deep tech house 125–130 (sourced, Attack). Default 126.
- **Swing:** 55–65% (snippet); deep tech house 60–65% (sourced, Attack).
- **Elements (sourced, Attack "Deep Tech House"):** 909 kick on quarters, open hat every offbeat, 16th shaker whose velocity variation "plays a very important role", 707 clap on 2 and 4 high-passed below 120 Hz, low ghost snares, ~4 dB drum-bus compression. Closed hats on the 1st, 2nd and 4th 16th of each beat, leaving the 3rd for the open hat (sourced, snippet).

```
Kick      X . . . | X . . . | X . . . | X . . .   1000100010001000
Clap      . . . . | X . . . | . . . . | X . . g   0000100000001001
ClHat     x x . x | x x . x | x x . x | x x . x   1101110111011101
OpHat     . . o . | . . o . | . . o . | . . o .   0010001000100010
Shaker    g x g x | g x g x | g x g x | g x g x   1111111111111111
GhostSn   . . . . | . . . g | . g . . | . . . .   0000000101000000
Tom       . . . x | . . x . | . . . . | . x . .   0001001000000100
```

- **Velocities:** kick 120; clap 110, ghost clap step 16 at 50; closed hats 90/70/–/60 per beat; open hat 90; shaker 45/75 alternating plus ±10 variation; ghost snares 40; filtered toms 85 (positions convention, vary per bar).
- **Bass:** rolling 16th offbeat bounce, sidechained — see `music-bass-808`.

## 5. Afro house

- **BPM:** Wikipedia range 80–122, up to 160; modern club afro house ~118–124 (convention). Default 122.
- **Swing:** 52–58% (convention).
- **Signature:** 3+3+2 conga/tom figures, organic shakers, call-and-response vocals (convention, drawing on the tresillo sources).

```
Kick      X . . . | X . . . | X . . . | X . . .   1000100010001000
Rim       . . . . | x . . . | . . . . | x . . .   0000100000001000
Shaker    g x g x | g x g x | g x g x | g x g x   1111111111111111
OpHat     . . o . | . . o . | . . o . | . . o .   0010001000100010
Conga     x . . x | . . x . | . . x . | . x . .   1001001000100100
TomLo     . . . . | . . . x | . . . . | . . x .   0000000100000010
```

- **Velocities:** kick 110; rim 85; shaker accents on offbeat 16ths 75, others 45; congas 80–95; low tom 90. Vary conga in a 2-bar call/answer.

## 6. Techno (peak-time, rolling, hard)

- **BPM:** 120–150 overall (sourced, Wikipedia); Detroit 125–135 (default 128); peak-time 130–140; hard techno 145–160 (sourced, Futureproof), measured median 146, IQR 136–155 over 9,988 tracks (sourced, Mixgraph).
- **Swing:** 50–54% (convention); Attack's rolling techno uses 20% on a DAW scale (not MPC).

Peak-time / Detroit (convention grid):
```
Kick      X . . . | X . . . | X . . . | X . . .   1000100010001000
OpHat     . . o . | . . o . | . . o . | . . o .   0010001000100010
Hat16     x g x g | x g x g | x g x g | x g x g   1111111111111111
Clap      . . . . | x . . . | . . . . | x . . .   0000100000001000
Ride      . . x . | . . x . | . . x . | . . x .   0010001000100010
```
Velocities: kick 127; open hat 90; 16th hats 70/45 alternating; clap 100 (optional); ride 85 in peak sections only.

Rolling techno (sourced, Attack, 131 BPM, 20% DAW swing; clap positions convention):
```
Kick      X . . g | . . . . | X . . g | . . . .   1001000010010000
TomLo     x . x . | x . x . | x . x . | x . x .   1010101010101010
TomHi     . x . x | . x . x | . x . x | . x . x   0101010101010101
Clap      . . g . | x . . . | . . . g | . . g .   0010100000010010
Hat16     x g x g | x g x g | x g x g | x g x g   1111111111111111
OpHat     . . . . | o . . . | . . . . | o . . .   0000100000001000
```
Kicks on beats 1 and 3 with ghost kicks just before 2 and 4 give a "pendulum"; low-passed toms alternate on every 16th for low-end roll; open hats on 2 and 4, some pushed late at ~50% velocity.

Hard techno: peak-time grid at 145–160 with a distorted "rumble kick" (kick into reverb into distortion, sidechained to the kick) as the bass; clap sometimes on every beat or absent (sourced, Futureproof).

## 7. Trance

- **BPM:** 125–150 (sourced, Wikipedia); uplifting ~138 (sourced, Orphiq). Default 138.
- **Swing:** 50% straight (convention).
- **Elements (sourced, Wikipedia):** kick on every downbeat, open hat on every upbeat; builds foreshadowed by long snare rolls rising in velocity and density.

```
Kick      X . . . | X . . . | X . . . | X . . .   1000100010001000
Clap      . . . . | x . . . | . . . . | x . . .   0000100000001000
ClHat     . g . g | . g . g | . g . g | . g . g   0101010101010101
OpHat     . . o . | . . o . | . . o . | . . o .   0010001000100010
Ride      . . x . | . . x . | . . x . | . . x .   0010001000100010
```

- **Velocities:** kick 127; clap 100; closed hats 50 (e/a only, so kick / open hat / closed hat never collide); open hat 95; ride 85 (climax only).
- **Build:** 8–16 bar snare roll quarters → 8ths → 16ths → 32nds with velocity ramp; beatless 16–32 bar breakdown (see `hats-fills-builds.md`).

## 8. Drum & bass

- **BPM:** 160–180, mostly 170–180 since ~1996, mid-170s hallmark (sourced, Wikipedia); 172–176 (sourced, Violet); 174 "a good tempo to kick off" (snippet). Default 174. Jungle 160–170.
- **Swing:** "a touch of swing so the off-beat hats lean late" (sourced, Violet) → MPC 52–55% on hats (convention).
- **Two-step skeleton (sourced, snippet):** kick on 1, second kick pushed to the 8th before the second snare (step 11); snares on 2 and 4 (steps 5, 13).

```
Kick b1   X . . . | . . . . | . . x . | . . . .   1000000000100000
Kick b2   X . . . | . . . . | . . x . | . . g .   1000000000100010
Snare     . . . . | X . . . | . . . . | X . . .   0000100000001000
Ghost b1  . . . . | . . . g | . g . . | . . . g   0000000101000001
Ghost b2  . . g . | . . . g | . g . . | . . . .   0010000101000000
Hat       x . x . | x . x . | x . x . | x . x .   1010101010101010
```

- **Velocities:** kick 120; snare 127; ghost snares 35–50 (from a chopped break; positions convention); hats 80/60; ghost kick 65.
- **Breaks (sourced, Violet):** get the 2-bar skeleton grooving, then layer a chopped Amen/Think/Apache break sliced at transients, slices nudged off-grid; vary hat and ghost velocities; fills = 1/32 or 1/64 repeats with rising velocity. DnB producers commonly alternate two breaks bar by bar (sourced, Wikipedia).

Amen-style bar (common transcription of the Winstons' "Amen, Brother" break; convention — check against the sample):
```
Kick      X . x . | . . . . | . . x x | . . . .   1010000000110000
Snare     . . . . | X . . g | . g . . | X . . g   0000100101001001
Ride      x . x . | x . x . | x . x . | x . x .   1010101010101010
```
The 4-bar Amen phrase (sourced, Wikipedia): bars 1–2 main beat; bar 3 delays a snare; bar 4 leaves beat 1 empty, plays a syncopated figure and an early crash.

- **Liquid:** softer kick/snare, ride and 16th shaker forward. **Neurofunk:** tight, compressed, gated kick/snare, minimal hats, bass edits every half bar (sourced, Wikipedia). **Jungle:** replace the skeleton with a re-sequenced Amen at 160–170, dense ghosts and rolls, dub sub at half-time.

## 9. Dubstep / riddim

- **BPM:** 138–142, half-time feel (~71 at 142) (sourced, Wikipedia). Riddim 140–150 (sourced, snippet). Default 140.
- **Swing:** 50% (convention); classic UK dubstep sometimes uses triplet hats.
- **Character:** sparse kick/snare/hats; the sub can carry the pulse the kick omits (sourced, Wikipedia).

```
Kick      X . . . | . . . . | . . . . | . . . .   1000000000000000
Kick b2   X . . x | . . . . | . . . . | . . . .   1001000000000000
Snare     . . . . | . . . . | X . . . | . . . .   0000000010000000
ClHat     . . x . | . . . . | . . x . | . . . .   0010000000100000
OpHat     . . . . | . . o . | . . . . | . . o .   0000001000000010
Perc      . . . . | . g . . | . . . . | . . . g   0000010000000001
```

- **Velocities:** kick 127; snare 127; hats 70; open hat 75; perc ghosts 45. Optional extra kick on step 11 or 12.
- **Riddim:** same skeleton; the bass motif is a repeated 1/8-triplet stab pattern with empty rests — silence is the instrument (sourced, snippet).

## 10. UK garage (4x4 and 2-step)

- **BPM:** UK garage 124–132 (sourced, Attack "UK Garage"); rolling 2-step 122–128 (sourced, Attack); future garage 130–140 (sourced, Wikipedia). Default 130.
- **Swing:** MPC16 68/69 (sourced, Attack UKG); 60–65% (sourced, Attack rolling 2-step). This is the swing-heaviest genre here: FL start ~40–50% and match by ear.
- **Elements (sourced, Attack):** UKG — kick on the downbeat of each bar plus the offbeat of beat 3, double hit at the start of bar 2 (pitched +3 st, short decay); two rimshots as a syncopated snare substitute (second pitched +2 st); soft closed hat high-passed at 750 Hz; cabasa on offbeats; crash at section starts. Rolling 2-step — no kick on beat 1 of bar 2; snare 2 and 4; a hat on every offbeat with decay between closed and open; offbeat shaker; 16th tambourine kept low. 2-step = kicks that skip beats, removing the 2nd and 4th kick (sourced, Wikipedia).

4x4 / speed garage (convention):
```
Kick      X . . . | X . . . | X . . . | X . . .   1000100010001000
Snare     . . . . | X . . . | . . . . | X . . .   0000100000001000
Rim       . . . g | . . x . | . g . . | . . x .   0001001001000010
ClHat     g x g x | g x g x | g x g x | g x g x   1111111111111111
OpHat     . . o . | . . o . | . . o . | . . o .   0010001000100010
```

2-step (rolling 2-step version; exact 16th positions convention):
```
Kick b1   X . . . | . . . . | . . x . | . . . .   1000000000100000
Kick b2   . x . . | . . . . | . . x . | . . . .   0100000000100000
Snare     . . . . | X . . . | . . . . | X . . .   0000100000001000
Rim b1    . . . g | . . . x | . g . . | . . x .   0001000101000010
Rim b2    . . g . | . . . x | . . . . | . g x .   0010000100000110
Hat       . . x . | . . x . | . . x . | . . x .   0010001000100010
Tamb      g g g g | g g g g | g g g g | g g g g   1111111111111111
```

- **Velocities:** kick 115 (tight, punchy, not an EDM sub kick — sourced, Producer School); snare 110; rims 50–90 varied; offbeat hat 85; tamb 35–55 varied.
- **Attack UKG variant:** `Kick b2` = `X x . . | . . . . | . . x . | . . . .` = `1100000000100000` (double hit at the start of bar 2, second hit pitched +3 st).

## 11. Future bass

- **BPM:** 130–175 (sourced, Wikipedia); usually 140–160 felt half-time with the snare on beat 3 (sourced, Violet). Default 150.
- **Swing:** 50% (convention).
- **Signature:** sidechain pumping is "a defining part of the bounce" (sourced, Violet); rhythmic pitch-bent supersaw chord stabs.

```
Kick      X . . . | . . . . | . . x . | . . . .   1000000000100000
Snare     . . . . | . . . . | X . . . | . . . .   0000000010000000
Hat       x . x . | x . x . | x . x . | x . r .   1010101010101010
Chords    x . . x | . . x . | x . . x | . . x .   1001001010010010
```

- **Velocities:** kick 120; layered clap+snare 127 with big reverb; hats 90/70, 1/32 roll on step 15 and triplet hat runs every 2 bars; chord stabs are MIDI chords (see `music-chords-voicing`).

## 12. Synthwave

- **BPM:** 80–118, upbeat 128–140 (sourced, Wikipedia). Default 100.
- **Swing:** 50% straight (convention).
- **Elements (snippet):** steady 4/4 kick, gated-reverb snare on 2 and 4, crisp 16th hats, LinnDrum-style kits.

```
Kick      X . . . | X . . . | X . . . | X . . .   1000100010001000
Snare     . . . . | X . . . | . . . . | X . . .   0000100000001000
ClHat     x g x g | x g x g | x g x g | x g . g   1111111111111101
OpHat     . . . . | . . . . | . . . . | . . o .   0000000000000010
```

- **Velocities:** kick 115; snare 120 (gated reverb); hats 90/55; open hat 90. Rock-style alternative kick: steps 1, 9, 11. Gated tom fill in the last bar of each 8-bar phrase.

## 13. Pop

- **BPM (convention):** dance-pop 118–124 (4x4); mid-tempo pop 95–110 (backbeat, use the rock grid with electronic sounds); trap-pop 140–150 half-time (use the trap grid); ballad 70–90.
- **Swing:** 50–54% (convention).

Dance-pop:
```
Kick      X . . . | X . . . | X . . . | X . . .   1000100010001000
Clap      . . . . | X . . . | . . . . | X . . .   0000100000001000
OpHat     . . o . | . . o . | . . o . | . . o .   0010001000100010
```

- **Velocities:** kick 115–120; clap 120; open hat 85; add 16th closed hats at 80/50 in choruses only (density = energy).
- **Pop rule:** keep the drums familiar (Senn 2018 familiarity bonus) and put variation in drops/fills at section changes.

## 14. Rock

- **BPM:** 90–140 (convention); backbeat on 2 and 4 (sourced, Wikipedia: Backbeat). Default 120.
- **Swing:** 50% (convention).

```
Kick      X . . . | . . . . | X . x . | . . . .   1000000010100000
Snare     . . . . | X . . . | . . . . | X . . .   0000100000001000
Hat       x . x . | x . x . | x . x . | x . x .   1010101010101010
Crash     X . . . | . . . . | . . . . | . . . .   1000000000000000
```

- **Velocities:** kick 115; snare 120; hats 100/80; crash 110 on step 1 of each new section only (choruses swap hats for ride on 8ths).

## 15. Funk

- **BPM:** 95–115 (convention). Default 105.
- **Swing:** 52–56% (convention).
- **Why it matters:** Witek 2014's groove stimuli were funk breaks; this grid sits in the medium-syncopation sweet spot (anchors on 1, 5, 13; syncopated kicks on 3, 11, 14; ghost snares on 8, 10, 16).

```
Kick      X . x . | . . . . | . . x . | . x . .   1010000000100100
Snare     . . . . | X . . g | . g . . | X . . g   0000100101001001
Hat       x g x g | x g x g | x g x g | x g x g   1111111111111111
```

- **Velocities:** kick 110; snare 120, ghosts 35–50 (low-volume in-between strokes — sourced, Wikipedia: Ghost note); hats 100 on beats, 85 on "&", 50 on e/a.

## 16. Breakbeat

- **BPM:** nu skool breaks 130–140 (sourced, Wikipedia). Default 135.
- **Swing:** 50–54% (convention).

```
Kick      X . . . | . . . . | . . x . | . . . .   1000000000100000
Snare     . . . . | X . . . | . g . . | X . . g   0000100001001001
Hat       x . x . | x . x . | x . x . | x . x .   1010101010101010
```

- **Velocities:** kick 115; snare 120, ghosts 45; hats 90/65. Variants: extra kick on step 8 or 15; layer a chopped break under the programmed kit.

## 17. Hyperpop

- **BPM:** NI tutorial 205 BPM (sourced); other guides 140–170+ or "135 or higher" (sourced, eMastered). Default 160 (or 200+ for the NI feel).
- **Swing:** 50% (convention).
- **Skeleton (sourced, NI, 2 bars, all velocities 100):** snare on beat 3 of each bar; kicks on beats 1 and 4 of bar 1 and on the final two 8ths of bar 2.

```
Kick b1   x . . . | . . . . | . . . . | x . . .   1000000000001000
Kick b2   . . . . | . . . . | . . . . | x . x .   0000000000001010
Snare     . . . . | . . . . | x . . . | . . . .   0000000010000000
```

- **Additions (convention):** 16th hats with triplet and 1/32 rolls; distorted/clipped kick, metallic snare (sourced, eMastered); glitch stutters (1/32–1/64 repeats) at transitions.
- **Delivery:** all velocities are 100, so the whole kit can go through `fl_set_step_sequencer`; only rolls need MIDI.

---

## 18. Sources

- Attack Magazine Beat Dissected (attackmagazine.com/technique/beat-dissected/...): 21st-century Chicago house, deep tech house, rolling techno, UK garage, rolling 2-step garage.
- Wikipedia: Deep house, Tech house, Afro house, Techno, Trance music, Drum and bass, Amen break, Neurofunk, Liquid funk, Dubstep, UK garage, 2-step garage, Future bass, Synthwave, Hyperpop, Backbeat, Ghost note, Four on the floor.
- Futureproof Music School: What is hard techno. Mixgraph: BPM for hard techno (mixgraph.io/bpm-for/hard-techno).
- Violet Recording: How to make drum and bass; How to make future bass. The Producer School: UK garage drums. Orphiq: trance.
- Native Instruments blog: Hyperpop production 101 (blog.native-instruments.com/hyperpop/); drum and bass. eMastered: hyperpop.
- Snippet-level (treat as convention): Loopmasters tech house, Computer Music / MusicRadar DnB grooves, BassGorilla/DJ.Studio riddim, Output synthwave, MusicRadar classic house.
