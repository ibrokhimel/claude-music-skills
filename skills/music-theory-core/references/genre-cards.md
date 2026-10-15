# Genre parameter cards

One-line summary: ~40 genres as compact parameter vectors (tempo, feel, snare, swing, key, chords, sub owner, signature, section lengths), plus tie-breakers between close relatives — each card points to the sibling skill that holds the detail.

Contents
1. How to read and use a card
2. Hip hop, urban and global (17 cards)
3. Electronic, pop and cinematic (24 cards)
4. Close relatives: how to tell them apart
5. Emotion overrides
6. Sources

---

## 1. How to read and use a card

- **BPM**: default first, range in brackets. "HT" = half-time feel (snare on beat 3, step 9).
- **Snare**: where the backbeat sits. "2&4" = steps 5 and 13.
- **Swing** on the MPC/Linn scale (50 = straight, 66 = triplet). Values marked FL are on FL's own 0–100 knob and are not interchangeable. Bake exact MPC values into MIDI with `swing16()` (see `fl-delivery.md`).
- **Sub owner**: the ONE part allowed to carry energy below ~100 Hz. Everything else gets high-passed or kept out of that register.
- **Sections**: bar counts of the main blocks. Full templates and energy curves: `music-arrangement`.
- Evidence: rows mix sourced tutorial values and **(convention)**. Tempo ranges and the trap/drill/boom-bap/house/UKG/afrobeats specifics are **(sourced)** at tutorial or Wikipedia level; swing values without a source and most section lengths outside rap, EDM and DnB are **(convention)** — tune by ear against a reference track.

Where the detail lives:
- 16-step drum grids, hat rolls, velocities, fills → `music-drums-groove`
- 808/bassline patterns, glides, kick–bass strategy → `music-bass-808`
- Progressions, voicings, harmonic rhythm, comping → `music-chords-voicing`
- Lead/topline style, motifs, hooks → `music-melody-hooks`
- Song forms, energy curve, builds/drops → `music-arrangement`
- Mix template, loudness targets → `music-mix-master`

## 2. Hip hop, urban and global

| Genre | BPM | Feel / snare | Swing | Key / mode | Chord vocabulary | Sub owner | Signature sounds | Sections (bars) |
|---|---|---|---|---|---|---|---|---|
| Trap | 140 (130–160; NI up to 200) | HT, snare/clap step 9 | 50; triplets written explicitly | natural/harmonic minor, Phrygian | 2–4 minor triads; i–VI–v–i, i–v–iv; Andalusian | long 808 following the kick, optional slides, saturated | 8th hats with 1/32 and triplet rolls; clap decay ~280 ms; bells/piano counter-melody from 1, 5, b7, 8 | intro 4–8, hook 8, verse 16 |
| UK drill | 142 (138–151) | HT; bar 1 snare step 9, bar 2 snare step 13 | 50–54; "skippy" comes from 3+3+2 hat placement | dark minor, b2, harmonic minor | i–v–VI, i–VII–VI, i–iv–VII–III; sus and dim colour | sliding 808 that carries the melody | 3+3+2 hats with hand-cut gaps; cold 2–4-note motifs, strings/choir | intro 8, hook 8, verse 16, bridge 8 |
| NY / Brooklyn drill | 144 (140–150) | same skeleton, punchier | ~50 | minor triads | simple minor loops, harmonic-minor V | heavy 808 with long tuned glides | harder, louder drums; hook-forward repetition | as UK drill |
| Chicago drill | 140 grid, 70 feel (130–145) | trap-like HT | 50 | minor | static minor loops | sustained, mostly static 808 | heavy, direct; fewer slides | rap default |
| Plugg / pluggnb | 145 (130–150) | HT, soft clap step 9 | 50 | warm minor | 2–3 chords; pluggnb: EP block chords with m7/add9, close inversions | clean, sine-like 808 | sine leads, glassy bells, gospel chops | rap default |
| Rage | 155 (140–170) | HT, snare step 9 | 50 | minor | 1–2-chord minor loops | distorted, clipped 808 | short looping stereo-wide supersaw lead, video-game arps | rap default |
| Boom bap | 90 (85–95) | 2&4; clap layer late | 57 kick/snare (8ths), 74 hats (16ths), MPC 3000 **(sourced)** | sample key; minor/Dorian jazz-soul | sampled chords, m7/9, 1–2 per bar | simple bass doubling the kick roots | chopped vinyl samples, layered kicks, cowbell/open hat answers | intro 8, verse 16, hook 8 |
| Lo-fi hip hop | 78 (60–90) | 2&4, soft, late snare | ~58–64 MPC (FL 20–30% **sourced**) | Dorian/minor, major 7ths | maj7/m7/9; ii–V–I; VI–i–V7; loops that avoid I | soft low-passed bass | LP ~3.1 kHz, vinyl, bitcrush, loose timing, velocity 60–90 keys | 2–3 min loop; changes every 4/8 |
| Modern R&B | 75 (60–90; or 120–140 HT) | 2&4 or step 9, rim ghosts | ~55–58 (FL 15–20% **sourced**) | minor/Dorian, major 7ths | 7th–13th chords, passing and secondary dominants | 808 tuned to chord roots, smooth glides | Rhodes, pitched vocal chops, rolled chords | intro 4–8, verse 16, hook 8, bridge 8 |
| Afrobeats | 108 (95–115) | soft 2&4; kick 1, &2, 3, (&4) — no four-floor | 54–58 gentle 16th swing | major (C, G, F, D typical) | simple triads, I–IV–V–vi colours | round bass, roots MIDI 24–40 | 16th shaker 60-40-70-40%, 3-2 clave, congas, muted guitar | intro 4–8, verse 16, hook 8, bridge 8 |
| Amapiano | 112 (108–115) | restrained four-floor, rim 2&4 | 55–60 on shakers | minor/modal | m9/maj7/6-9, jazz ii–V–I | log drum (tuned, pitch-glide) | log drum bouncing between kicks, offbeat open hat, constant 16th shaker, long piano/pad chords | intro 8–16, foundation 16, development 16–32, breakdown 8–16, outro 8–16 |
| Reggaeton | 94 (85–100) | dembow 3+3+2: snare steps 4, 7, 12, 15 over four-floor kick | 50 | minor | i–VI–III–VII | sustained sub on roots, sidechained | "boom-ch-boom-chick" dembow | intro 4–8, verse 16, hook 8 |
| Dominican dembow | 122 (115–130) | dembow | 50 | minor/loop-based | 1–2-chord loops | heavy, distorted 808/bass | rapid chant vocals, dense percussion | 8-bar blocks |
| Phonk (drift / Brazilian) | 145 (130–160) | 2&4 or step 9 (Memphis) | 50–54 | minor/Phrygian | minimal, 1–2 chords | distorted 808 | tuned 808 cowbell melody (tresillo), Memphis vocal chops | 8-bar blocks, short |
| Jersey club | 140 (130–145) | kick 1, 5, 9, 12, 15; snare 9, 12 (+11 alt bars) | 50 | minor/major chops | chopped hooks, sparse stabs | short-envelope mono sub | five-kick run, bed squeak, vocal chops as drums | 8-bar blocks, layer every 8 |
| West Coast ratchet | 100 (95–105, estimate) | 2&4, clap flurries | 50–54 | minor | minimal, 1–2 chords | thumping 808 | clap flurries, reverberated "hey" shouts, sparse synth bounce | rap default |
| Detroit (Sada Baby era) | 175 (165–190, estimate) | 2&4 at full tempo | 50 | minor | "murderous" piano loops | thumping 808 | fast menacing piano loops, punchy claps | rap default |

**Rap default form (convention):** intro 8, hook 8, verse 16, hook 8, verse 16, hook 8, outro 4–8; drop drums/808 for 1 bar before hooks. Drill variant (sourced, beatstorapon): intro 8, hook 8, verse 16, hook 8, verse 16, bridge 8, hook 8, outro 8; noticeable change every 4 or 8 bars.

## 3. Electronic, pop and cinematic

| Genre | BPM | Feel / snare | Swing | Key / mode | Chord vocabulary | Sub owner | Signature sounds | Sections (bars) |
|---|---|---|---|---|---|---|---|---|
| Classic / Chicago house | 124 (120–126) | four-floor, clap 2&4 | 55–60 **(sourced)** | minor/Dorian vamps; gospel major | m7/m9 vamps, 7sus4, slash chords | simple offbeat bass | 909 kick + 707 claps, tambourine on offbeats (two copies L/R), syncopated rim | intro 16+16, groove 32, breakdown 16, build 8, drop 32, outro 32 |
| Deep house | 120 (110–125) | four-floor, clap 2&4 | 55–62 | minor/Dorian | m7/m9 parallel stabs; Am9–Dm9–Gmaj7–Cmaj7 | muted, round bass | hypnotic repetition, avoids big build/release | DJ blocks of 16/32 |
| Deep tech house | 127 (125–130) | 909 on quarters | 60–65 **(sourced)** | minimal minor | 0–1 chords | rolling bass | 16th shaker velocity shaping, clap HP below 120 Hz | DJ blocks of 16/32 |
| Tech house | 125 (123–126) | four-floor, clap 2&4 | 55–65 | minor | 0–1 chords | rolling 16th offbeat bass, heavy sidechain | dry percussion, vocal one-shots | intro 32, groove 32, break 16, drop 32 |
| Afro house | 120 (118–124 club; 80–122 overall) | four-floor | 52–58 | modal minor (Dorian/Aeolian) | 2-chord modal vamps | warm syncopated sub | 3+3+2 congas and toms, chants, marimba/kalimba plucks, flute | long evolving 16/32 blocks |
| Techno | 130 (120–150) | four-floor, often no snare | ~50; rolling techno 20% DAW-scale **(sourced)** | atonal / one-note | often none | rumble bass or 303 acid line | rhythm and timbre over harmony, filter automation | intro 32, A 32, tension 16–32, B 32–64, outro 32 |
| Hard techno | 146 (145–160; median 146 of 9,988 tracks **sourced**) | four-floor | 50 | atonal | none | the distorted rumble kick IS the bass | everything clipped, "attitude over BPM" | 16/32 blocks |
| Trance | 138 (125–150) | four-floor, open hat every upbeat | 50 | natural minor | i–VI–III–VII; Am–F–C–G; sus held one bar too long | rolling offbeat bass | supersaw leads, beatless breakdown, snare-roll builds, 1–2 peaks | intro 32, groove 32, breakdown 16–32, build 8–16, climax 32, climax 2 32, outro 32 |
| Drum & bass | 174 (170–180) | two-step: kick 1 + step 11, snare 2&4 | 50, slight late lean | minor; liquid: jazz 7ths/9ths | liquid ii–V–I; neuro atonal | clean sub (+ reese mid layer) | chopped Amen/Think breaks, 1/32–1/64 fills, one beat of silence before drops | intro 32, build 8–16, drop 32, breakdown 16–32, drop 2 32, outro 32 |
| Liquid DnB | 174 (172–176) | two-step | 50 | minor/major 7ths | ii–V–I, m9/maj9 | smooth sub | pads, vocals, rides and shakers forward | as DnB |
| Neurofunk | 174 (172–176) | two-step | 50 | atonal | none | sub under FM/wavetable mid-bass | technical bass design | as DnB |
| Jungle | 165 (160–170) | chopped breaks | 50–54 | minor, ragga | minimal | dub sub | dense break edits, ragga samples | as DnB |
| Dubstep | 140 HT | snare step 9 | 50 | minor/Phrygian | minimal; 1–2 chords | sub under wobble/growl mid | bass call-and-response in kick–snare gaps | intro 16–32, build 8, drop 16–32, breakdown 16, build 8, drop 2 16–32, outro 16 |
| Riddim | 145 HT (140–150) | snare step 9 | 50 | one note | none | sub under looping mid-bass | one 1/8T mid-bass motif, silence as an instrument | as dubstep, evolve one loop |
| Future bass | 150 HT (130–175) | snare/clap step 9, big reverb | 50 | major-leaning | maj7/m7/add9 (triads too thin unless doubled); royal road IVmaj7–V–iii7–vi | long sub/808 under short chords | pitch-bent supersaw chord chops, heavy pumping, twinkly risers | intro 8, verse 16, build 8, drop 16, verse 8–16, build 8, drop 2 16, outro 8 |
| UK garage (4x4 / shuffled) | 130 (124–132) | kick 1 + &3 area, snare 2&4 | 68–69 MPC16 **(sourced)** | minor | m7/m9 R&B chords | syncopated sub / organ bass | rimshots, cabasa offbeats, chopped vocals | intro 16, verse 16, hook 16, break 8, verse 16, hook 16, dub 16, outro 16 |
| 2-step garage | 130 (122–132) | no kick on beat 1 of bar 2; snare 2&4 | 60–65 **(sourced)** | minor | m7/m9 | syncopated sub | skipping kick, shuffled rims | as UKG |
| Synthwave | 100 (80–118; upbeat 128–140) | 2&4, gated reverb snare | 50 | Aeolian | i–VI–III–VII, i–VII–VI–VII | octave-pulsing 8th/16th saw bass | arps, gated snare, 80s pads, sax/guitar solo | intro 8–16, verse 16, chorus 16, solo 16, outro 8–16 |
| Modern pop (dance) | 110 (95–125) | 2&4 or four-floor | 50–54 | major or minor | I–V–vi–IV family; IV and V more common than I | sub/808 locked to kick | hook by 30–45 s; median length 3:13 | intro 4, verse 8, pre 4–8, chorus 8, post 4–8, bridge 8, final chorus 8–16 |
| Pop ballad | 75 (70–90) | 2&4, soft | 50–54 | major, minor turns | I–V–vi–IV, borrowed iv, minor plagal | bass / piano left hand | piano + strings, exposed vocal | as pop |
| Hyperpop | 160 (135–205) | NI 2-bar pattern, all velocity 100 | 50 | major "saccharine" | bright triads, fast changes | distorted 808 | pitched vocals, glitches, clipping | short pop form, 2:00–2:30 |
| Ambient | beatless (or 60–90) | none | — | Lydian, major, modal | drones, maj7/sus, slow pads | none or drone | texture over structure, long reverbs | phrase-based, 2–8 bar chords |
| Cinematic trailer | free → 120–150 in act 3 | taiko 3+3+2 drive | 50 | Aeolian; Phrygian b2 for threat | i–VI–III–VII over a pedal | braams, sub drops | 16th string ostinati, choir, hits on downbeats, 1–2 beats of silence before the final hit | act 1 0:00–0:40, act 2 to 1:30, act 3 to 2:15, button |
| Lo-fi house | 120 (115–125) | four-floor, soft clap 2&4 | 55–60 | Dorian/minor | m7/m9 sampled chords | warm filtered bass | dusty saturated drums, LP filtering **(convention)** | 16/32 blocks |

Build toolkit shared by all club genres: remove kick and bass 4–16 bars before the drop; accelerate the snare (4ths → 8ths → 16ths → 32nds); rise spectrally (HP filter, noise, pitch risers); leave 1/2–1 beat of silence (sourced for DnB); land with crash + sub drop + kick on beat 1; vary the second drop. Detail: `music-arrangement`.

## 4. Close relatives: how to tell them apart

- **Trap vs drill**: both ~140 HT. Trap keeps the snare on step 9 every bar, straight hats with rolls, optional slides. Drill moves the bar-2 snare to step 13, groups hats 3+3+2 with gaps, and its 808 slides carry the melody. UK = colder, more syncopated, longer controlled glides; NY = punchier, simpler triads, heavier glides; Chicago = trap-like with static 808s.
- **Trap vs plugg vs rage**: same drum chassis. Plugg swaps dark bells for soft sine leads and EP chords; rage swaps them for short stereo-wide supersaw loops and distorted 808s.
- **Boom bap vs lo-fi**: boom bap ~90 with hard swung drums and chopped samples; lo-fi ~78 with soft late snares, low-pass filtering and jazzy 7ths.
- **Afrobeats vs amapiano**: Afrobeats has a syncopated kick (no four-floor), 3-2 clave, guitars and pop song form; amapiano keeps a restrained house pulse, the log-drum bass as hook, long jazzy chords and DJ-length forms.
- **Dembow family**: reggaeton (~94), Dominican dembow (115–130) and afro styles all use 3+3+2.
- **Deep house vs tech house**: deep = slower, jazzier, hypnotic m9 stabs; tech = drier, percussive, rolling bass, almost no chords.
- **DnB vs jungle**: DnB = programmed two-step at ~174; jungle = chopped breakbeats, ragga/dub, 160–170.
- **Dubstep vs riddim**: dubstep varies bass sound design across the drop; riddim loops one triplet mid-bass motif with lots of space.
- **UKG vs 2-step**: UKG may keep a 4x4 kick with heavy shuffle; 2-step skips the bar-2 downbeat kick.

## 5. Emotion overrides (convention, from the music-emotion literature)

If the brief names a mood instead of (or as well as) a genre, bias the card:

| Mood | Tempo | Mode / harmony | Register / timbre | Articulation |
|---|---|---|---|---|
| Happy / uplifting | faster end of range | major, Lydian, I-based loops | higher, bright | short, bouncy |
| Sad / melancholic | slower end; or HT | minor/Aeolian, start on i or vi, borrowed iv | lower, dark, soft | legato, sparse, lush reverb |
| Dark / menacing | mid | Phrygian b2, harmonic minor, b6→5 | low bells, detuned, metallic | sparse, staccato stabs |
| Tension | any | dim, aug, pedal point, chromatic lines | extreme registers | irregular rhythm, sudden dynamics |
| Triumphant / epic | mid–fast | bVI–bVII–I, i–VI–III–VII | full range, brass/supersaw | sustained, big downbeats |
| Dreamy / nostalgic | slow–mid | maj7, add9, Lydian, I–vi float | soft keys, tape/vinyl | rolled chords, long tails |

Tempo and loudness carry emotion more robustly across cultures than major/minor (Fritz 2009); see `science-of-beauty.md`.

## 6. Sources (compact)

Hip hop/global: Wikipedia (Trap music, UK drill, Rage rap, Dembow, Phonk, Mustard); Native Instruments blog (trap, drill, lo-fi, jersey club, hyperpop); beatstorapon (drill, amapiano, jersey club); Attack Magazine (90s boom bap); Audeobox (boom bap, afrobeats, lo-fi, R&B in FL Studio); Violet Recording (R&B, 808 patterns); Splice (amapiano, pluggnb); Roland articles (amapiano); Reason Studios (plugg); Orphiq (drill chords, reggaeton, dembow); Okayplayer (Detroit). Electronic/pop/cinematic: Attack Magazine (Chicago house, deep tech house, UK garage, rolling 2-step, rolling techno); Wikipedia (Deep house, Tech house, Afro house, Techno, Trance, DnB, Neurofunk, Liquid funk, Dubstep, Future bass, Synthwave, Hyperpop, Ambient); Futureproof + Mixgraph (hard techno BPM); Violet Recording (DnB, future bass, trailers); FeelYourSound (future bass); Hooktheory (pop chords); DEV analysis of Hot 100 lengths; Mixed In Key (arrangement); BassGorilla (riddim). Low-authority or snippet-level: musicproductionwiki (rage), tunee.ai (phonk), Loopmasters (tech house).
