# Energy, tension, builds, drops, transitions and variation

How to plan the song's shape: energy and tension as separate controls, per-genre energy curves, build recipes, the transition menu and the 4/8/16-bar variation schedule.

## Contents
1. Energy vs tension
2. Why builds and drops work (science)
3. Energy mapping method and the six contrast axes
4. Energy curves per genre
5. Build recipes (8-bar EDM, 4-bar, hip hop pre-hook, cinematic)
6. Transition menu (risers, rolls, filter sweeps, pitch rises, silence, reverse crash, downlifters)
7. Drops and breakdowns
8. Variation schedule (every 4/8/16 bars) and B variants
9. FL Studio how-to for transitions
10. Sources

## 1. Energy vs tension

EDMProd defines two separate controls **(sourced)**:
- **Tension** = expectation of release, a felt need for resolution.
- **Energy** = intensity and momentum. A steady four-on-the-floor kick has energy but little tension. Types: overall (genre/tempo), rhythmic (kick + bass groove), sonic (mix quality).

Energy knobs (convention): element count, low-end presence, drum density and hat subdivision, register span, stereo width, loudness, brightness (filter cutoff), lead type (vocal vs instrument vs octave-doubled).

Tension knobs: risers (noise, pitched, rhythmic), snare/clap rolls with acceleration, high-pass filter automation, kick removal, repeated single notes, held dominant or suspended chords, pedal tones, leaps larger than a 5th, deceptive cadences, silence **(sourced: EDMProd)**. Harmonic tension devices: `music-chords-voicing`.

Tension scales **(sourced: EDMProd)**:
- **Macro** (section scale): risers, 4-8-bar snare rolls, filter automation, pitched risers rising 5-24 semitones, melodic shifts.
- **Micro** (bar scale): short fills, kick removals, reverse crashes, one-bar breaks, chord/melody changes.

Combinations (convention):

| Energy | Tension | Section type |
|---|---|---|
| low | low | intro, outro, breakdown start |
| low | high | breakdown into build; beatless riser; cinematic Act 2 end |
| high | low | groove, drop body, hook body, techno main section |
| high | high | last bars of a build with drums still in; final pre-chorus |

## 2. Why builds and drops work

- Salimpoor et al. 2011: dopamine released in the striatum at peak emotion; caudate tied to anticipation, nucleus accumbens to the peak **(sourced)**. So design two phases: a clearly signalled lead-in, then a payoff.
- Cheung et al. 2019: pleasure highest for low uncertainty + high surprise, or high uncertainty + low surprise **(sourced)**. A build creates near-certainty that a hit is coming; a short silence or fake-out is a small surprise inside that certainty **(derived)**.
- Chill passages show loudness increases in the 920-4400 Hz band (Grewe/Nagel group) **(sourced)**: a climax should open the presence range (filters open, upper harmonies, lead forward), not only add sub.
- De Fleurian & Pearce 2021: chill songs are on average sadder, slower, less intense and more instrumental than matched tracks **(sourced)**: an exposed melody in a sparse breakdown can be the emotional peak.
- Gold et al. 2019: preference peaks at intermediate complexity; repetition lowers liking but keeps that peak **(sourced)**: add one dimension of novelty per change, not five.
- Vickers 2010 and related work: loudness does not win preference; dynamic contrast drives peaks **(sourced)**: keep verses quieter than choruses.

## 3. Energy mapping method and contrast axes

EDMProd method **(sourced)**: rate each section of a reference track 1 (lowest) to 9 (highest), draw the curve, then arrange to your own planned curve before writing transitions.

Procedure (convention):
1. Write the section list with bars.
2. Give each section an energy score 1-9 and a tension trend (flat, rising, release).
3. For each score, set the knobs: element count roughly = score / 2 + 1 focal-plus-support parts; low end on for 6+; hats at 1/16 or rolls for 7+; octave doubles for 8+; widest stereo at 9.
4. Each repeat of a section sits at or slightly above its previous instance (add a layer, octave double or new percussion).
5. Check adjacent sections differ on at least 2 of the 6 axes:

| Axis | Low setting | High setting |
|---|---|---|
| Element count | 1-3 parts | 6-9 parts |
| Low-end presence | no kick/808 | kick + 808/bass |
| Hat subdivision | none or 1/4 | 1/16 + rolls |
| Register span | 2 octaves | 5+ octaves (sub to bells) |
| Stereo width | narrow/mono | wide pads, spread perc |
| Lead type | none / instrument | vocal / octave-doubled hook |

## 4. Energy curves per genre (1-9; convention unless noted)

| Genre | Curve |
|---|---|
| Pop | Intro 3, V1 4, Pre 5, Ch1 7, Post 6, V2 5, Pre 6, Ch2 8, Bridge 4-5, Final Ch 9, Outro 3 |
| Trap / rap beat | Intro 3, Hook 8, Verse 6, Hook 8, Verse 6-7, Bridge 4, Hook 9, Outro 3 |
| Drill | Intro 3, Hook 8, Verse 6 (switch at bar 8: 7), Hook 8, Verse 7, Bridge 4, Hook 9, Outro 2 |
| Boom bap | Intro 3, V 5, H 7, V 5-6, H 7, V 6, H 8, Outro 3 (flatter; groove carries) |
| R&B | Intro 2, V 4, Pre 5, H 7, V 4-5, Pre 6, H 7, Bridge 4, H 8, H 9, Outro 3 |
| EDM | Intro 3, Break 4, Build 5->7, Drop 9, Breakdown 3, Build 5->8, Drop 2 9, Outro 3 |
| House (club) | Intro A 4, Intro B 5, Groove 6->7, Breakdown 3, Build 4->7, Drop 8, Groove 3 7, Outro 5->3 |
| Deep house | 4, 5, 6, 4, 6, 6, 4 (shallow; no big build) |
| Techno | Intro 4, Main A 6->7, Tension 5 (rising tension, falling energy), Main B 8, Outro 4 |
| Trance | Intro 4, Main 6, Breakdown 3 (tension rising), Build 5->8, Climax 9, Mid 5, Climax 2 9, Outro 4 |
| DnB | Intro 3->4, Build 5->7, Drop 1 9 (switch-up 9), Breakdown 3, Build 6->8, Drop 2 9, Outro 4 |
| Dubstep / future bass | Intro 3, Build 5->7, Drop 9, Breakdown/verse 3-4, Build 6->8, Drop 2 9, Outro 3 |
| Lo-fi | 2, 4, 5, 4, 2 (narrow range; change by texture, not size) |
| Afrobeats | Intro 3, V 5, H 7, V 5-6, H 7, Bridge 4, H 8, Outro 3 |
| Amapiano | Intro 3, Foundation 5, Development 6->7, Breakdown 3, Development 2 8 (log drum return), Outro 4 |
| Cinematic | Act 1 2-3, Act 2 4->7, silence, Act 3 9, Button (single hit) |

## 5. Build recipes

### 8-bar EDM build (convention, combining EDMProd and genre practice)

| Bars | Drums | Riser layer | Filter / pitch | Low end |
|---|---|---|---|---|
| 1-4 | snare/clap on quarters, vel 60-80 | white-noise riser starts quiet | music bus high-pass starts opening (~100 Hz -> 300 Hz) | kick in or on quarters, bass out or filtered |
| 5-6 | 8ths, vel 80-95 | + pitched riser (12 st over the build) | high-pass to ~600 Hz | kick may drop |
| 7 | 16ths, vel 95-110 | + rhythmic riser / repeated single lead note | high-pass ~1 kHz, reverb send up | kick and bass out |
| 8 | 32nds or 16th triplets, vel 110-127; last beat empty | riser peaks | full high-pass; vocal tag or pickup | silence on beat 4, or the whole bar |
| Drop beat 1 | crash + full drums | impact + sub drop | filters reset | 808/bass + kick return |

Roll programming and exact velocity ramps: `music-drums-groove`. Trance/DnB sourced: long snare rolls rising in velocity, frequency and volume; DnB uses "a beat of silence right before each drop".

### EDMProd worked example (sourced, bar numbers)
Intro 1-32: layer 1 drum additions (clap at bar 8, filtered hat from bar 12); layer 2 at bar 16 (noise sweep + subtle pitched riser); layer 3 at bar 24 (snare roll starts, kick removed, rhythmic riser at full volume). Verse 32-64: no new tension for the first 8 bars, new instrument at bar 16 of the section, build in the last 8. Breakdown 64-96: main idea, 3-chord progression. Build 96-104: reuse the intro build, repeat the dominant chord, **one bar of silence before the drop**. Drop 104-136.

MAKJ "Springen" layered build analysis (sourced): layer 1 riff + noise sweeps/subtle pitch risers; layer 2 adds snare roll + pluck riser; layer 3 repeats a single note of the riff, speeds up the roll and adds vocal samples.

### 4-bar build (pop pre-chorus, short EDM, convention)
Bar 1-2 eighth-note clap/snare, bar 3 sixteenths, bar 4 roll + riser + kick out on beats 3-4; reverse crash ending on the chorus downbeat.

### Hip hop / trap pre-hook (convention)
Mute kick and 808 for the last beat or last bar before the hook (or the whole bar 16 of a verse); optional hat roll or vocal tag; reverse cymbal into beat 1; hook lands with crash + 808 on beat 1. Fill schedule at drum level: bar 4 small, bar 8 bigger, bar 16 crash + full fill (`music-drums-groove`).

### Cinematic build (sourced: ostinato practice, Open Music Theory crescendo)
Ostinato alone -> add low drone/pad -> add melody -> add brass/percussion and widen the range (sub octave + top octave) -> shorten note values (8ths -> 16ths -> tremolo) -> riser -> 1-2 beats of silence -> Act 3 hit.

## 6. Transition menu

| Tool | Use | Settings / rules |
|---|---|---|
| White-noise riser | macro, into drops/choruses | 4-16 bars; volume and high-pass rising; stop exactly at the downbeat or 1 beat early before silence |
| Pitched riser | macro | rises 5-24 semitones **(sourced)**; 12 st default over 8 bars; 24 st for big drops; 5-7 st for subtle |
| Rhythmic riser | macro | saw/square gated in 8ths -> 16ths **(sourced: EDMProd)** |
| Snare/clap roll | macro | 4-8 bars typical **(sourced)**; quarters -> 8ths -> 16ths -> 32nds; optional pitch automation up |
| Filter sweep (HPF up) | macro, into drops | music bus high-pass opening 20 Hz -> ~1 kHz over the build; reset on the drop |
| Filter sweep (LPF) | intros, outros, breakdowns | low-pass closing on exit (downlift), opening on entry |
| Silence | biggest drop only | half a beat to 1 bar **(sourced: EDMProd 1 bar; DnB 1 beat)**; save the longest gap for the biggest moment |
| Reverse crash | 8/16/32-bar boundaries | reverse a copy of the crash, end it slightly before the real hit, keep it quieter, add reverb before reversing for a better swell **(sourced: EDMProd)** |
| Crash / impact | downbeat of new section | crash + sub drop/impact on beat 1; kick returns on beat 1 |
| Downlifter / sub drop | leaving high-energy sections, trailer buttons | falling noise or pitch over 1-4 bars |
| Kick removal | micro | last beat, half bar or bar before a section |
| Drum drop-out | micro | everything but the lead for 1-2 beats at a 4/8-bar end |
| Reverb / delay throw | phrase ends | send the last word or note to a long reverb or delay, then cut |
| Vocal pickup / tag | into hooks | producer tag, ad-lib or a chopped syllable in the gap |
| Tape stop / stutter | hyperpop, trap, lo-fi | 1 beat; use once or twice per song |

Rules (sourced: Mixed In Key; Inspired by Beatz): save the strongest signal for the biggest change; do not repeat the same fill at every boundary; signal transitions with fills, held notes or gaps.

## 7. Drops and breakdowns

- **A drop only hits if the breakdown before it cleared space** (Inspired by Beatz) **(sourced)**. Classic mistakes: everything at once, no breakdown, second drop identical to the first.
- **Subtract first:** remove kick/bass 4-16 bars before the drop (convention).
- **Breakdown contents:** no kick or bass; pads, exposed lead/theme, vocal; tension rising toward the build. Trance: beatless, a suspended chord held "one bar longer than feels comfortable" (snippet-level source).
- **Drop 2 must differ:** new bass patch or pattern, an added layer, a key lift (+1/+2 st in trance), a switch-up halfway (DnB "VIP" style), or a half-time/double-time switch (convention).
- **Hip hop hooks** act as drops: verse simpler, hook fullest; a 1-beat to 1-bar drop-out before the hook does the clearing.

## 8. Variation schedule and B variants

Schedule (convention, from DJ phrasing and the drum fill schedule):

| Boundary | What happens |
|---|---|
| Every 2 bars | call/response within the loop (lead bars 1-2, answer bars 3-4) |
| Every 4 bars | micro-variation: fill, last-beat drop-out, 808 slide, hat roll, reverse cymbal, melody tail change |
| Every 8 bars | something enters, leaves or changes (new perc, pad in/out, hat pattern B, octave double, filter state) |
| Every 16 bars | section change or a crash + full fill; bigger transition |
| Every repeat of a section | at or above its previous energy; never identical |

No identical 8-bar block more than twice in a row. A 16-bar verse = 8 bars of variant A + 8 bars of variant B (or A with B in bars 7-8 and 15-16).

B-variant list per role (convention):
- Kick: added pickup kick before bar 1; one kick removed in bar 4/8.
- Snare/clap: flam or extra ghost at bar end; moved hit (drill bar-2 snare).
- Hats: rolls (1/32, triplets), pattern switch (straight vs 3+3+2), open hat added.
- Perc: new layer every 8 bars; swap rim for snap.
- 808/bass: slides, octave jumps, rhythm change, a rest bar (`music-bass-808`).
- Chords: inversion change, added extension, rhythm (sustained -> stabs), borrowed chord on bar 8 (`music-chords-voicing`).
- Lead: answer phrase with a different ending, octave up, sparser version for verses (`music-melody-hooks`).
- FX/texture: filter automation, reverb send rides, pan movement so repeats evolve.

## 9. FL Studio how-to for transitions (user steps; MCP cannot draw automation or place clips)

- **Riser / reverse crash:** drag the sample into a new Channel Rack sampler channel; place its clip so its end aligns with the target downbeat. For a reverse crash: Channel settings > Sample > Reverse (check the "Reverse" option), add Fruity Reeverb 2 on the channel first if you want a swell, then align the end slightly before the downbeat.
- **Filter sweep:** put Fruity Filter (or the mixer EQ) on a music bus (all non-drum tracks routed to it with `fl_route_track`); right-click the cutoff knob > Create automation clip; draw the ramp over the build bars; reset at the drop.
- **Silence gap:** in the playlist, cut all clips at the gap start (slice tool) and delete the region, or mute the clips for that beat/bar.
- **Snare roll:** deliver as MIDI (`music-drums-groove`); simple 16-step versions can be written with `fl_set_step_sequencer` into a dedicated "build" pattern the user selects first (64 steps = 4 bars max per call).
- **Kick/808 removal for one bar:** easiest as a separate pattern variant (e.g. "808 B: bar 8 empty") or by slicing the playlist clip.
- MCP can audition: `fl_mute_track` the kick/808 mixer tracks while looping the build pattern to hear the clearing before committing.

## 10. Sources

- EDMProd, advanced guide to tension and energy: https://edmprod.com/tension
- Inspired by Beatz: https://www.inspiredbybeatz.com/en/edm-arrangement-from-loop-to-exciting-track/
- Mixed In Key: https://mixedinkey.com/?p=5367
- Violet Recording, DnB: https://violetrecording.com/how-to-make-drum-and-bass/ ; trailers: https://violetrecording.com/sound-design-for-trailers/
- Wikipedia, Trance music: https://en.wikipedia.org/wiki/Trance_music
- Open Music Theory, orchestration (crescendo): https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_(Gotham_et_al.)/10%3A_Orchestration/10.01%3A_Core_Principles_of_Orchestration
- Salimpoor et al. 2011, Nature Neuroscience: https://www.zlab.mcgill.ca/publications/docs/salimpoor_2011_nn.pdf
- Cheung et al. 2019, Current Biology: https://cms.mus.cam.ac.uk/publications/cheung-uncertainty-surprise/
- Gold et al. 2019, J. Neuroscience: https://pmc.ncbi.nlm.nih.gov/articles/PMC6867811
- Grewe/Nagel group, chills and 920-4400 Hz loudness: https://jyx.jyu.fi/handle/123456789/19439?show=full
- de Fleurian & Pearce 2021, Psychological Bulletin: https://qmro.qmul.ac.uk/xmlui/handle/123456789/75159
- Vickers 2010, loudness war (AES): https://aes2.org/publications/elibrary-page/?id=15598
- Wikipedia, Phrasing (DJ): https://en.wikipedia.org/wiki/Phrasing_(DJ)
