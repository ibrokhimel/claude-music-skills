# Genre drum grids: hip hop, urban and global styles

16-step grids with FL binary strings, BPM, swing and velocities for trap, UK drill, NY drill, boom bap, lo-fi, R&B, plugg/pluggnb, rage, phonk, reggaeton/dembow, afrobeats, amapiano and Jersey club.

## Contents
1. How to read and deliver these grids
2. Trap
3. UK drill
4. NY / Brooklyn drill (and Chicago)
5. Boom bap
6. Lo-fi hip hop
7. Modern R&B
8. Plugg / pluggnb
9. Rage
10. Phonk (drift, Memphis, Brazilian)
11. Reggaeton / dembow
12. Afrobeats
13. Amapiano
14. Jersey club
15. Sources

---

## 1. How to read and deliver these grids

- Steps `1 2 3 4 | 5 6 7 8 | 9 10 11 12 | 13 14 15 16`. Beats = steps 1, 5, 9, 13.
- Symbols: `X` accent (110–127), `x` normal (85–105), `g` ghost (35–60), `o` open hat, `r` roll start (roll described below the grid), `.` rest.
- The 16-char string after each row is the `fl_set_step_sequencer` pattern: every non-`.` cell = `1`. For 2-bar patterns (`b1`, `b2`), concatenate in bar order (32 chars; max 64 = 4 bars).
- The step sequencer only writes on/off at default velocity. Rows with `g`, velocity shapes, rolls (`r`) or triplets must go out as MIDI (one .mid per channel, notes at MIDI 60) or the ghosts will play as loud as accents. See SKILL.md "FL Studio delivery".
- Evidence tags: **(sourced)** = from a cited guide/study; **(sourced, low-authority)** = tutorial/aggregator site; **(convention)** = standard practice, tune by ear; **(derived)** = arithmetic.
- Swing is on the MPC/Linn scale (50% straight, 66% triplet). FL's swing knob is a different 0–100 scale with no verified mapping: start at ~15–30% FL and match by ear; it only acts when BOTH the global and the channel swing are > 0.

---

## 2. Trap

- **BPM:** 130–160, default 140, felt as 70 (sourced: Audeobox; NI cites 130–200 overall; Wikipedia: programmed at 140 in half-time).
- **Swing:** 50% straight; triplets and rolls programmed explicitly (convention). FL global swing 0.
- **Skeleton:** clap/snare on beat 3 only (sourced); 8th closed hats with 32nd rolls at bar ends, three notes per roll with quieter middle notes (sourced, NI); kick placement (convention).

```
Kick b1   X . . . | . . . x | . . x . | . . . .   1000000100100000
Kick b2   X . . x | . . . . | . . x . | . . x .   1001000000100010
Snare b1  . . . . | . . . . | X . . . | . . . .   0000000010000000
Snare b2  . . . . | . . . . | X . . . | . . . g   0000000010000001
Hat b1    x . x . | x . . . | x . x . | x . r .   1010100010101010
Hat b2    x . x . | x x x x | x . x . | r . . .   1010111110101000
OpHat b1  . . . . | . . o . | . . . . | . . . .   0000001000000000
```

- **Velocities:** kick 115–120 (the 808 doubles it); snare+clap layer 127; hats 100 on beats, 80 on "&", 16ths in b2 beat 2 at 100/60/80/60; ghost snare b2 step 16 at ~55.
- **Rolls:** b1 step 15 = 1/32 roll over steps 15–16 (4 hits, 12 ticks apart, vel 100-70-70-100, or NI's 3-note version). b2 step 13 = 1/16-triplet roll over beat 4 (6 hits, 16 ticks apart, ramp 60 to 110).
- **Interlock:** kick on 8 pushes into the snare on 9; kick on b2 step 4 bounces; open hat on 7 replaces the closed hat there (choke group).
- **Fill:** NI uses a straight-8th snare fill in the last bar of a 4-bar loop (see `hats-fills-builds.md`).
- **Delivery:** kick, snare (minus ghost), open hat via step sequencer; hats always via MIDI (rolls).

## 3. UK drill

- **BPM:** 138–151 (sourced, Wikipedia); 140–144 (sourced, Tracklib); default 142. NI's example is 146.
- **Swing:** grid stays straight; the bounce comes from 3+3+2 hat grouping and off-beat kicks. Optional light swing on hats only, MPC 52–55% (convention). Tracklib calls UK drill "swing-heavy" but gives no number.
- **Skeleton (sourced, NI 2-bar pattern):** snare beat 3 in bar 1, beat 4 in bar 2; kick b1 steps 1, 8; b2 steps 1, 4, 7, 15; hats on 1, 4, 7, 9, 12, 15 with a ghost on b1 step 16.

```
Kick b1   X . . . | . . . x | . . . . | . . . .   1000000100000000
Kick b2   X . . x | . . x . | . . . . | . . x .   1001001000000010
Snare b1  . . . . | . . . . | X . . . | . . . .   0000000010000000
Snare b2  . . . . | . . . . | . . . . | X . . .   0000000000001000
Hat b1    x . . x | . . x . | x . . x | . . x g   1001001010010011
Hat b2    x . . x | . . x . | x . . x | . . x .   1001001010010010
```

- **Velocities (sourced, NI):** kicks 100, b2 step 15 = 96; hats 100 on steps 1, 7, 9, 15 and 87 on steps 4, 12; ghost hat b1 step 16 = 52. Snare 100–120.
- **Additions:** optional ghost snare on b1 step 15 ("and" of 4) at 51–64 (sourced, Audeobox 40–50%); 16th-triplet hat bursts (snap 1/6 beat) before the main snares every 2 bars (sourced, Beatstorapon/eMastered, placement convention); snare layered with a short clap panned slightly L or R (sourced, Audeobox).
- **808:** lands on or just after kicks, 2–3 upward slides (minor 3rd / 4th) per 4 bars, C or G minor common — see `music-bass-808`.
- **Space:** delete hat hits to leave gaps; the top line should hold "more silence than notes" (sourced, Tracklib).

## 4. NY / Brooklyn drill (and Chicago)

- **BPM:** 140–150 Brooklyn (sourced, Tracklib); 140–145 NY (sourced, Audeobox); default 142–143.
- **Swing:** less than UK; keep 50% (sourced qualitatively: "harder, less swing").
- **Character:** same half-time skeleton as UK; harder layered snares/claps, heavier distorted 808 with long glides, simpler minor-triad loops, hook-forward repetition (sourced, Beatstorapon/orphiq). Exact NY grids are not documented in sources.
- **Grid (from the user's working `ny-drill-midi/make_midi.py`, 142 BPM; convention):**

```
Kick b1   X . . . | . . x . | . . . . | x . . .   1000001000001000
Kick b2   . . x . | . . . . | x . . . | . . . .   0010000010000000
Snare b1  . . . . | . . . . | X . . . | . . g .   0000000010000010
Snare b2  . . . . | . . . . | . . . . | X . . .   0000000000001000
Hat b1    x . x g | x . x . | r . . . | . . . .   1011101010000000
Hat b2    x . x g | x . x . | x . x . | x . x .   1011101010101010
Perc b2   . . . . | . . . . | . . x . | . . . .   0000000000100000
```

- **Velocities:** kick b1 120/105/100, b2 105/110; snare 120 (+ clap layer 95); ghost snare 50; hats 105, 70, 55, 95, 70 then 100/70/95/70; perc 85.
- **Hat b1 step 9 roll:** beats 3–4 as 8th-note triplets (6 hits, 32 ticks apart, vel 100 on each triplet start, 65 between). Alternate per bar: triplets / plain / triplets / 1/16-triplet roll on beat 4 (6 hits, 16 ticks, ramp 55 to 100).
- **Phrase marks:** extra kick pickup on step 15 of bars 4 and 8 (vel 90–95); in bar 8, snare flam on steps 15–16 (70, 85) into the loop restart.
- **Chicago drill (one line):** 130–145 BPM (60–75 felt), trap-like straight hats, sustained static 808s, fewer slides (sourced, Tracklib/orphiq). Use the trap grid with a drill snare (b2 snare on 13).

## 5. Boom bap

- **BPM:** 85–95, classic 88–94, default 90 (sourced, Audeobox/violetrecording).
- **Swing:** MPC 3000: 57% at 8th resolution on kick and snare, 74% at 16th resolution on hats (sourced, Attack "90s boom bap"); typical range MPC 54–62% (sourced, violetrecording summary). FL: start channel swing ~20–35% (convention).
- **Skeleton:** kick on 1, "and" of 2 (step 7), sometimes 3, and a ghost kick on "and"/"e" of 4 (sourced, Audeobox); snare on 2 and 4; 16th hats; cowbell on beat 1 of bar 2 and open hat on beat 4 of bar 2 (sourced, Attack).

```
Kick b1   X . . . | . . x . | x . . . | . . . .   1000001010000000
Kick b2   X . . . | . . x . | . . x . | . . g .   1000001000100010
Snare     . . . . | X . . . | . . . . | X . . .   0000100000001000
Hat b1    x g x g | x g x g | x g x g | x g x g   1111111111111111
Hat b2    x g x g | x g x g | x g x g | . . . .   1111111111110000
OpHat b2  . . . . | . . . . | . . . . | o . . .   0000000000001000
Cowbl b2  x . . . | . . . . | . . . . | . . . .   1000000000000000
```

- **Velocities:** kicks constant 115–125 (sourced: "90–100%", "the pattern creates the groove, not the dynamics"); ghost kick ~70; snare 120; hats 95 on 8ths, 45–55 on in-between 16ths.
- **Feel:** clap layer nudged a few ms late (sourced, Attack); swing the hats harder than kick/snare.
- **Sound:** two layered kicks, small boost ~60 Hz and big dip ~150 Hz on the kick (sourced, Attack); dusty, saturated, bit-reduced, rolled-off highs (sourced, Audeobox).

## 6. Lo-fi hip hop

- **BPM:** 70–90, 78 typical (sourced, Audeobox); 60–90 (sourced, NI; tutorial at 65).
- **Swing:** FL quantize swing 20–30% (sourced, Audeobox; FL scale) ≈ MPC 58–64% (convention). Timing intentionally "not fully quantised" (sourced, NI) — implement as a systematic late snare, not random jitter.

```
Kick      X . . . | . . x . | . . x . | . . . .   1000001000100000
Snare     . . . . | x . . . | . . . . | x . . .   0000100000001000
Hat       x . g . | x . g . | x . g . | x . g .   1010101010101010
```

- **Velocities:** kick 100; snare/rim 90–100, placed +10–20 ms late (+2 to +3 ticks at 78 BPM, PPQ 96) (derived); hats alternate ~89 / ~51 (sourced: 70% / 40%).
- **Options:** add a hat on step 16 at ~60 before the loop restart; swap snare for a rim on quieter sections.
- **Sound:** soft thumpy kick, loose snare, acoustic hats; low-pass ~3 kHz, vinyl crackle (sourced, NI) — see `music-mix-master`.

## 7. Modern R&B

- **BPM:** 60–90 (sourced, violetrecording); trap-R&B 120–140 in half-time; neo-soul 68–95. Default 75.
- **Swing:** FL quantize swing 15–20% (sourced, Audeobox; FL scale) ≈ MPC 55–58% (convention).
- **Hats (sourced, Audeobox):** 16ths with 8th positions at 70–80% (89–102) and in-between 16ths at 30–50% (38–64); open hat on "and" of 2 (step 7) at 65% (~83).

```
Kick      X . . . | . . . . | . . x . | . . . g   1000000000100001
Snare     . . . . | X . . . | . . . . | X . . .   0000100000001000
Rim       . . . g | . . . . | . g . . | . . . .   0001000001000000
ClHat     x g x g | x g . g | x g x g | x g x g   1111110111111111
OpHat     . . . . | . . o . | . . . . | . . . .   0000001000000000
```

- **Velocities:** kick 100, ghost kick step 16 ~55; snare 105; rim ghosts 40; hats as above.
- **Half-time variant (120–140 BPM):** move the snare to step 9 only and use trap-style hats with one triplet roll per 2 bars.
- **Feel:** swung drums with ghost notes (sourced); snare slightly late is idiomatic (convention).

## 8. Plugg / pluggnb

- **BPM:** 130–150 half-time (sourced, Reason Studios via search summary); plugg default 140–150, pluggnb ~130–140 (convention).
- **Swing:** 50% (convention).
- **Character:** trap drums but simpler hats; soft clap/snap; the sound is in the soft sine leads, bells and e-piano chords (sourced, Splice).

```
Kick      X . . . | . . . . | . . x . | . . x .   1000000000100010
Clap      . . . . | . . . . | x . . . | . . . .   0000000010000000
Hat       x . x . | x . . . | x . x . | x . x .   1010100010101010
OpHat     . . . . | . . o . | . . . . | . . . .   0000001000000000
```

- **Velocities:** kick 110; clap/snap 100 (softer than trap); hats 90/70; one triplet roll every 2–4 bars, not every bar.

## 9. Rage

- **BPM:** 140–160, or 150–170 half-time (sourced, low-authority: musicproductionwiki); example loops at 154–155 (sourced, Looperman). Default 155.
- **Swing:** 50% (convention).
- **Character:** basic energetic trap rhythm under short looping stereo-wide synth leads and distorted, clipped 808s (sourced, Wikipedia). The drums are simple on purpose; energy comes from loudness and the lead.

```
Kick      X . . . | . . . . | . . X . | . . . .   1000000000100000
Snare     . . . . | . . . . | X . . . | . . . .   0000000010000000
Hat       x . x . | x . x . | x . x . | x . x .   1010101010101010
```

- **Velocities:** kick 120–127 (doubled by 808 hits); snare 127; hats 95 flat or 16ths at 95/70 in hooks.
- **Variation:** switch hats to 16ths in the hook; one 1/32 roll per 4 bars.

## 10. Phonk (drift, Memphis, Brazilian)

- **BPM:** drift 130–160 (sourced, low-authority: tunee.ai); Memphis/classic ~120–140, often slower (convention estimate); Brazilian funk/mandelão 130 or 140, up to ~150 (sourced, ABCdoABC/Suno summaries, low-authority). Defaults: drift 145, Memphis 130 (half-time), Brazilian 130.
- **Swing:** 50% (convention).
- **Signature:** TR-808 cowbell melodies, Memphis vocal chops, distorted 808 (sourced, Wikipedia). The cowbell is pitched: deliver it as MIDI with notes in the key (cowbell sample tuned per note).

Drift phonk (convention grid):
```
Kick      X . . . | . . x . | X . . . | . . x .   1000001010000010
Clap      . . . . | X . . . | . . . . | X . . .   0000100000001000
Hat       x . x x | x . x . | x . x x | x . x .   1011101010111010
Cowbell   x . . x | . . x . | x . . x | . . x .   1001001010010010
```

Memphis / classic phonk (half-time, convention):
```
Kick      X . . . | . . . . | . . x . | . . . .   1000000000100000
Snare     . . . . | . . . . | X . . . | . . . .   0000000010000000
Hat       x . x . | x . x . | x . x . | x x x x   1010101010101111
Cowbell   x . . x | . . x . | x . . x | . . x .   1001001010010010
```

Brazilian phonk / tamborzão-derived (convention):
```
Kick      X . . x | . . x . | X . . x | . . x .   1001001010010010
Snare     . . x . | . . x . | . . x . | . . x .   0010001000100010
```

- **Velocities:** kick 120; clap 115; hats 90; cowbell 100 with accents on the tresillo starts (steps 1, 9).

## 11. Reggaeton / dembow

- **BPM:** reggaeton 85–100, modern radio ~92–96 (sourced, orphiq); Dominican dembow 115–130 (sourced, orphiq). Default 94.
- **Swing:** 50–54% (convention).
- **Skeleton (sourced, FaderPro via search summary; Wikipedia):** kick on every quarter (minimum 1 and 9), snare on the last 16th of beats 1 and 3 and halfway through beats 2 and 4 = steps 4, 7, 12, 15 — gaps of 3, 3, 2 per half bar.

```
Kick      X . . . | X . . . | X . . . | X . . .   1000100010001000
Snare     . . . x | . . x . | . . . x | . . x .   0001001000010010
Hat       . . x . | . . x . | . . x . | . . x .   0010001000100010
```

- **Velocities:** round dull kick 110–115; snare 105–110 (step 4 and 12 slightly softer than 7 and 15 is common); hats 75–80 (drop to ~60 where they coincide with snares on 7 and 15).
- **Dominican dembow:** same 3+3+2 at 115–130, drum-forward, distorted bass, faster perc fills.
- **Perc:** timbales/congas fills at phrase ends; shakers on 16ths (convention).

## 12. Afrobeats

- **BPM:** 95–115, 105–110 most common, 108 sweet spot (sourced, Audeobox); median ~110 (sourced, mixgraph summary). Default 108.
- **Swing:** gentle 16th swing on shakers/percs (sourced); MPC 52–56% (convention).
- **Skeleton (sourced, Audeobox):** kick on 1, "and" of 2, beat 3 (75–85%), plus "and" of 4 on alternate bars; snare/rim 2 and 4 with a 40% ghost on the "e" of 4 every other bar; closed hats straight 8ths (70–80% down, 50–60% up); open hat on "and" of 2 with choke; shaker 16ths cycling 60-40-70-40%; clave on 1, and-of-1, and-of-2, 4, and-of-4; congas accents 90%, ghosts 35–50%.

```
Kick b1   X . . . | . . x . | x . . . | . . . .   1000001010000000
Kick b2   X . . . | . . x . | x . . . | . . x .   1000001010000010
Rim b1    . . . . | x . . . | . . . . | x . . .   0000100000001000
Rim b2    . . . . | x . . . | . . . . | x g . .   0000100000001100
ClHat     x . g . | x . . . | x . g . | x . g .   1010100010101010
OpHat     . . . . | . . o . | . . . . | . . . .   0000001000000000
Shaker    x g x g | x g x g | x g x g | x g x g   1111111111111111
Clave     x . x . | . . x . | . . . . | x . x .   1010001000001010
Conga     . . . . | . x . x | . . . . | . x x .   0000010100000110
```

- **Velocities (from the sourced %s, ×1.27):** kick 110, step 9 at 95–108; rim 85, ghost 51; hats 89–102 / 64–76; open hat 80; shaker 76-51-89-51 per beat; clave 102–114; congas 114 accents, 44–64 ghosts (conga positions are convention).
- **Textbook alternative clave (son 3-2, convention):** `x . . x | . . x . | . . x . | x . . .` = `1001001000101000`.
- **Layer note:** this is the one style where 6+ layers is normal: each sits in its own register and subdivision at low velocity. Kick, rim and shaker carry; the rest decorate. Patterns develop over 4-bar cycles (sourced).

## 13. Amapiano

- **BPM:** 108–115 (sourced, Roland/Beatstorapon), 110–115 (Splice); 112 practical start. Default 112.
- **Swing:** swung 16th shakers (sourced); MPC 54–58% (convention).
- **Skeleton (sourced, Roland example 1):** four-on-the-floor kick (restrained), constant 16th shaker, open hat on the offbeats (third 16th of each beat), conga on beat 2, "a" of 2, "and" of 3, and beat 4. Log drum = pitched percussive bass that bounces between kicks in a 2-bar call/answer (sourced, Beatstorapon; exact steps convention). "Without the log drum, it's not amapiano" (Splice).

```
Kick      x . . . | x . . . | x . . . | x . . .   1000100010001000
Rim       . . . . | x . . . | . . . . | x . . .   0000100000001000
Shaker    x g x g | x g x g | x g x g | x g x g   1111111111111111
OpHat     . . o . | . . o . | . . o . | . . o .   0010001000100010
Conga     . . . . | x . . x | . . x . | x . . .   0000100100101000
Log b1    . . x . | . . . x | . . x . | . x . .   0010000100100100
Log b2    . . x . | . . x . | . . . x | . . x .   0010001000010010
```

- **Velocities:** kick ~95 ("restrained"); rim 80–85; shaker 70 / 45 / 85 / 45 per beat (accent the offbeat); open hat 80; conga 85–95; log drum 100 with pitch moves on later hits.
- **Log drum:** pitched — deliver as MIDI in key with a fast pitch glide; FL's Fruity DX10 holds the original log-drum preset (sourced, Splice). Bass detail: see `music-bass-808`.
- **Modern variant:** sparser, syncopated kick (Roland example 2) — e.g. drop kicks on beats 2 and 4 in breakdowns.

## 14. Jersey club

- **BPM:** 130–140, start at 140 (sourced, Beatstorapon); NI example 142.
- **Swing:** straight 16th grid (sourced).
- **Skeleton (sourced, NI):** kick on 1, 5, 9, 12, 15 (4-4-3-3-2: two quarters, two dotted 8ths, one 8th); snare on 9 and 12 in bars 1 and 3, on 9, 11, 12 in bars 2 and 4, with velocity variation; closed hats on beats 2 and 4; crash on beat 1 to mark sections.

```
Kick      X . . . | X . . . | X . . X | . . X .   1000100010010010
Snare b1  . . . . | . . . . | x . . x | . . . .   0000000010010000
Snare b2  . . . . | . . . . | x . x x | . . . .   0000000010110000
Hat       . . . . | x . . . | . . . . | x . . .   0000100000001000
```

- **Velocities:** kick 120 (short, hard, readable on all five attacks); snares 90–110 varied; hats 80.
- **Interlock exception:** kick and snare share steps 9 and 12 on purpose (stacked accents are the genre). Beatstorapon's alternative is a stable clap backbeat on 5 and 13 instead.
- **Rules (sourced, Beatstorapon):** build other drums around the kick; delete closed hats that duplicate kick transients; short bass/808 envelopes that end before the next kick; bed-squeak sample and one-syllable vocal chops played like percussion on the 16ths after kicks; 8-bar blocks.

---

## 15. Sources

- Native Instruments blog: trap (blog.native-instruments.com/how-to-make-a-trap-beat/), drill (/drill/), Jersey club (/jersey-club/), lo-fi (/lo-fi-hip-hop/), amapiano (/amapiano-music/).
- Audeobox FL Studio guides (audeobox.com/learn/fl-studio/...): trap, drill, boom bap, lo-fi, R&B, afrobeats.
- Attack Magazine Beat Dissected: 90s boom bap (attackmagazine.com/technique/beat-dissected/90s-boom-bap-hip-hop/).
- Tracklib: drill beat (tracklib.com/blog/drill-beat). Wikipedia: Trap music, UK drill, Dembow, Phonk, Rage rap, Tresillo.
- Beatstorapon: drill, Jersey club, amapiano. orphiq: drill, dembow, reggaeton. Splice: pluggnb, amapiano. Roland Articles: amapiano production hacks (articles.roland.com/?p=67237).
- Lower-authority (treat as convention): musicproductionwiki (rage), tunee.ai (phonk), violetrecording, Reason Studios plugg summary, FaderPro summary, ABCdoABC/Suno (Brazilian funk).
- User project: `C:\Users\User\Documents\flstudio\ny-drill-midi\make_midi.py` (NY drill grid above).
