# Turning Music Theory Into Programmable Beat Rules

Music that sounds good to listeners raised on Western pop is built from a small rule set, and almost all of it can be written as numbers. The pieces are twelve semitones (MIDI integers, with **C4 = 60, which FL Studio labels "C5"**), seven-note modes that each differ by one characteristic note, and chords voiced wide at the bottom and close at the top. Melodies move mostly by step toward a single climax. Drums sit on a 16-step grid where a few strong-beat anchors are decorated with medium syncopation. The research literature explains why this works:

- **Consonance** is largely learned harmonicity.
- **Pleasure** peaks when a surprise lands in a predictable context, or a confirmation lands after uncertainty.
- **Groove** peaks at medium syncopation, with low frequencies carrying the beat.
- **Dopamine** is released both during anticipation and at the payoff, which is why builds and drops work.

Genres differ less in theory than in a handful of parameters: tempo band, whether the snare lands on 2 and 4 or on 3, swing amount, which single part owns the sub below roughly 100 Hz, chord vocabulary (triads versus 7ths and 9ths), and section lengths in multiples of 4, 8 and 16 bars. A Claude skill set for FL Studio can therefore be largely deterministic. It needs a coordinate system, a scale and chord library, a nearest-voicing algorithm, melody-scoring heuristics, genre parameter cards with 16-step grids, a role and register allocator, and a mix template built on stock plugins.

The main caveat is evidence quality. Academic support is strong for consonance, expectation, groove, chills and streaming loudness normalisation. Most of the specific numbers in genre recipes (grids, velocities, swing percentages, bar counts) come from producer tutorials or practitioner convention. Several important values are unverified and must be tuned by ear, including the mapping between MPC-style and FL Studio swing, the low-interval limits, and 808 glide times.

## One coordinate system makes every rule programmable: MIDI, the 16-step grid and tempo math

Every rule in this report uses one shared frame of reference, because software disagrees about octave names. Scientific pitch notation calls middle C "C4" (MIDI 60), with A4 = 440 Hz. Manufacturers label middle C variously as C3, C4 or C5, which is why **MIDI numbers are the only unambiguous reference** ([Wikipedia: Scientific pitch notation](https://en.wikipedia.org/wiki/Scientific_pitch_notation)). FL Studio's piano roll shows MIDI 60 as "C5", so **FL's octave label is always the scientific octave plus one**.

The arithmetic follows from that offset:
- Scientific octave: `MIDI = 12 × (octave + 1) + pitch_class`.
- FL octave: `MIDI = 12 × FL_octave + pitch_class`.
- Pitch classes: C=0, C#=1, D=2, D#=3, E=4, F=5, F#=6, G=7, G#=8, A=9, A#=10, B=11.
- Frequency: `f = 440 × 2^((n − 69)/12)`.

The table below lists the anchors a composing skill needs. All values are derived arithmetic.

| MIDI | Scientific | FL label | Hz | Typical occupant |
|---|---|---|---|---|
| 24 | C1 | C2 | 32.7 | practical floor for 808 roots |
| 28 | E1 | E2 | 41.2 | bass guitar open E, deep 808 |
| 31 | G1 | G2 | 49.0 | G-minor 808 root |
| 33 | A1 | A2 | 55.0 | sub zone |
| 36 | C2 | C3 | 65.4 | bass, upper 808 |
| 48 | C3 | C4 | 130.8 | floor for chord 3rds; pad bottom |
| 60 | C4 | C5 | 261.6 | middle C, harmony core |
| 69 | A4 | A5 | 440.0 | lead and topline zone |
| 72 | C5 | C6 | 523.3 | bells, leads |
| 84 | C6 | C7 | 1046.5 | upper leads and arps |

Time works the same way. **One 4/4 bar is 16 steps, which equals one FL Channel Rack bar**:

| Position | Steps |
|---|---|
| Beats 1, 2, 3, 4 | 1, 5, 9, 13 |
| 8th-note offbeats ("and") | 3, 7, 11, 15 |
| 16th "e" positions | 2, 6, 10, 14 |
| 16th "a" positions | 4, 8, 12, 16 |

Channel Rack patterns can be anywhere from 1 to 512 steps long ([Image-Line manual: Channel Rack](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/channelrack.htm)). So a 12-step percussion loop running against a 16-step kick creates a polymeter that realigns every three bars (derived).

Triplets do not fit the 16-step grid and must be written in the piano roll. In FL snap terms (convention):
- 1/3 beat = 8th-note triplet.
- 1/6 beat = 16th-note triplet.
- 1/8 beat = 32nd note.

Tempo math is all derived:
- One 16th lasts `15000/BPM` ms: 166.7 ms at 90 BPM, 107 ms at 140, 86 ms at 174.
- A quarter note lasts `60000/BPM` ms.
- A bar lasts `240/BPM` seconds, so a 16-bar verse is 27.4 s at 140 BPM and 42.7 s at 90 BPM, and 32 bars is 60 s at 128 BPM and 44.1 s at 174 BPM.
- At FL's commonly used 96 PPQ, one beat is 96 ticks and one step is 24 ticks (FL convention; check against project settings).
- FL displays velocity as a percentage. The MIDI value is roughly `% × 1.27` (arithmetic).

Swing needs one more definition. In Roger Linn's MPC convention, swing delays every second 16th within each 8th: **50% means straight and 66% means a perfect triplet shuffle** ([Attack Magazine: Roger Linn on swing](https://www.attackmagazine.com/features/interview/roger-linn-swing-groove-magic-mpc-timing/)).

FL Studio's Channel Rack swing works on the same principle. It holds the odd 16ths and shifts the even ones. A channel only swings when **both** Global Swing and that channel's own Swing setting are above zero ([Image-Line manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/channelrack.htm)). FL's 0–100% scale is not the MPC scale, and no official mapping between them was found. The working estimate is that MPC 57% roughly equals FL 20–30%, and MPC 62% or more roughly equals FL 40–50%. That estimate is unsourced practitioner convention and must be tuned by ear.

Throughout this report, claims carry one of three labels. A **linked citation** means the claim is sourced. **(convention)** marks producer practice that the researchers synthesised but did not verify against a primary source. **(derived)** marks arithmetic.

## Harmony reduces to seven modes, a few dozen chord formulas and register-aware voicing

### Consonance follows the harmonic series, so wide intervals belong low

Twelve equal semitones make up an octave, and an octave doubles the frequency. Consonance has historically been tied to simple frequency ratios and to partials (harmonics) that coincide. Dissonance has been tied to beating or roughness between partials that are close together ([Wikipedia: Consonance and dissonance](https://en.wikipedia.org/wiki/Consonance_and_dissonance)). In just intonation the ratios are octave 2:1, fifth 3:2, fourth 4:3 and major third 5:4. Dissonant intervals create tension and a desire to resolve, but which intervals count as consonant depends on style. Renaissance theory, for example, treated the fourth above the bass as dissonant ([Wikipedia: Interval](https://en.wikipedia.org/wiki/Interval_(music))).

The physical point that matters most for production comes from Plomp and Levelt (1965). Two pure tones are consonant when their separation exceeds the critical bandwidth, and roughness peaks at about a quarter of a critical band. In Bach and Dvořák chords, partials thin out in the bass in step with the way the critical band widens, measured in semitones, at low frequencies ([Plomp & Levelt 1965](https://www.math.miami.edu/~armstrong/592sp15/Plomp_Levelt_1965.pdf)).

**An interval that sounds sweet at C5 turns to mud at C2.** The harmonic series of C2 (MIDI 36) shows the pattern nature uses:

| Partial | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Note | C2 | C3 | G3 | C4 | E4 | G4 | Bb4 (flat) | C5 | D5 | E5 |
| MIDI | 36 | 48 | 55 | 60 | 64 | 67 | ~70 | 72 | 74 | 76 |

The octave and fifth sit at the bottom, and thirds and seconds only appear higher up (derived). Voicings that copy this layout sound clear. Voicings that invert it sound muddy.

The table below gives each interval's size, its just-intonation ratio, and its conventional character in production. The character column reflects standard teaching, not a cited perception study.

| Semitones | Interval | Just ratio | Production character (convention) |
|---|---|---|---|
| 1 | minor 2nd | 16:15 | harshest; Phrygian trap/drill "grind"; resolve by step |
| 2 | major 2nd | 9:8 | mild; sus2/add9 "air" |
| 3 | minor 3rd | 6:5 | minor quality, dark |
| 4 | major 3rd | 5:4 | major quality, bright |
| 5 | perfect 4th | 4:3 | open, hollow; sus4 |
| 6 | tritone | ≈√2 | maximal instability; the core of V7 |
| 7 | perfect 5th | 3:2 | most stable after the octave; power chords |
| 8 | minor 6th | 8:5 | bittersweet; the Aeolian colour note |
| 9 | major 6th | 5:3 | warm; the Dorian colour note |
| 10 | minor 7th | 16:9 (harmonic 7th 7:4) | bluesy, soft tension |
| 11 | major 7th | 15:8 | lush when voiced wide; harsh when inverted to a minor 2nd |
| 12 | octave | 2:1 | identity, doubling |

One detail explains why the dominant seventh sounds smooth rather than harsh. Its minor 7th approximates the "harmonic seventh" (7:4) of the overtone series, so the chord fuses ([Wikipedia: Consonance and dissonance](https://en.wikipedia.org/wiki/Consonance_and_dissonance)).

### Seven modes and a dozen exotic scales, each identified by one characteristic note

All seven diatonic modes are rotations of the major scale ([Wikipedia: Mode](https://en.wikipedia.org/wiki/Mode_(music))). Lydian and Locrian are the only modes with a tritone above the tonic ([Wikipedia: Lydian mode](https://en.wikipedia.org/wiki/Lydian_mode)).

**Phrygian dominant** is the 5th mode of harmonic minor. Its steps are H, A2, H, W, H, W, W (H = half step, W = whole step, A2 = augmented 2nd). Flamenco, Middle Eastern and Jewish music use it ([Unison](https://unison.audio/phrygian-dominant-scale/); [Wikipedia: Phrygian dominant](https://en.wikipedia.org/wiki/Phrygian_dominant_scale)). **Hungarian minor** is harmonic minor with a raised 4th, which adds a second augmented-2nd gap ([Wikipedia: Hungarian minor](https://en.wikipedia.org/wiki/Hungarian_minor_scale)).

The table below gives each scale's formula on C4 = 60. Formulas are derived. Mood and genre associations are convention, except where the text after the table cites them.

| Scale | Semitones from root | Characteristic note | Mood and typical use |
|---|---|---|---|
| Ionian (major) | 0 2 4 5 7 9 11 | natural 4 and 7 | bright; pop, house, EDM drops |
| Dorian | 0 2 3 5 7 9 10 | **M6** | cool, hopeful minor; lo-fi, neo-soul, deep house |
| Phrygian | 0 1 3 5 7 8 10 | **b2** | menacing; trap, drill, horror |
| Lydian | 0 2 4 6 7 9 11 | **#4** | floating, wonder; cinematic, future bass |
| Mixolydian | 0 2 4 5 7 9 10 | **b7** | laid-back major; funk, gospel vamps |
| Aeolian (natural minor) | 0 2 3 5 7 8 10 | **b6** | sad, serious; trap, synthwave, trailers |
| Locrian | 0 1 3 5 6 8 10 | **b5** | unstable; brief dread only |
| Harmonic minor | 0 2 3 5 7 8 11 | **natural 7** (A2 gap from b6) | dramatic; trap and drill bells |
| Melodic minor | 0 2 3 5 7 9 11 | M6 + M7 | sophisticated minor; neo-soul |
| Phrygian dominant | 0 1 4 5 7 8 10 | b2 + M3 | "eastern" trap and drill leads |
| Hungarian minor | 0 2 3 6 7 8 11 | #4 + natural 7 | villainous; drill, horror |
| Major pentatonic | 0 2 4 7 9 | no half steps | can't-miss toplines |
| Minor pentatonic | 0 3 5 7 10 | no half steps | hip hop hooks, R&B riffs |
| Minor blues | 0 3 5 6 7 10 | b5 blue note | boom bap, gospel licks |
| Whole-tone | 0 2 4 6 8 10 | all major 2nds | dreamlike, "flashback" |
| Half–whole diminished | 0 1 3 4 6 7 9 10 | symmetrical | over 7b9 chords; suspense |

The modes form a brightness ladder. Each step down flattens exactly one note: **Lydian → Ionian → Mixolydian → Dorian → Aeolian → Phrygian → Locrian** (derived). A skill can therefore darken or brighten a part with a single substitution. Raising F to F# in A minor, for example, turns A Aeolian into A Dorian.

Modal colour is only audible under two conditions. The tonic must be established, usually by a bass pedal or a vamp that keeps returning home. The characteristic note must also actually sound. In a C Dorian i–IV vamp (Cm–F), the F major chord carries the Dorian A natural (convention).

Sourced genre-scale links are thinner than the table suggests:
- **Trap:** most melodies use natural minor, harmonic minor or Phrygian ([Production Music Live](https://productionmusiclive.com/blogs/news/trap-beat-guide-melodies-3-essential-scales-for-making-melodies)).
- **Lo-fi and producer contexts:** Dorian is recommended over minor-7th chords ([SampleFocus](https://samplefocus.com/blog/the-dorian-scale-producers-guide/)).
- **UK drill:** sparse minor melodies with eerie lines over sus and diminished chords ([Orphiq](https://orphiq.com/resources/drill-chords), via search summary).

No corpus statistics on scale use by genre were found.

### Keys and diatonic chords form the palette a progression generator draws from

On the circle of fifths, neighbouring keys differ by one note, and relative major and minor keys share a key signature ([Wikipedia: Circle of fifths](https://en.wikipedia.org/wiki/Circle_of_fifths)).
- Clockwise order: C, G, D, A, E, B, F#/Gb, Db, Ab, Eb, Bb, F.
- Relative minor: the major tonic minus 3 semitones (C 60 → A 57).

Borrowed chords come from the **parallel** key, which has the same tonic in the other mode ([Wikipedia: Borrowed chord](https://en.wikipedia.org/wiki/Borrowed_chord)).

Hooktheory analysed about 1,300 popular-song sections and reported these patterns ([Hooktheory](https://www.hooktheory.com/blog/i-analyzed-the-chords-of-1300-popular-songs-for-patterns-this-is-what-i-found/)):
- **C major and A minor** were by far the most common keys. This is partly an artefact of transcribing everything into C.
- **IV and V appear in more progressions than I.**
- After iii, the next chord is vi or IV about **93%** of the time.

The diatonic chords below are written in closed root position on MIDI 60 and up. They are derived arithmetic.

| Degree (C major) | Triad | 7th chord | Function |
|---|---|---|---|
| I | C 60 64 67 | Cmaj7 60 64 67 71 | tonic |
| ii | Dm 62 65 69 | Dm7 62 65 69 72 | predominant |
| iii | Em 64 67 71 | Em7 64 67 71 74 | weak tonic substitute |
| IV | F 65 69 72 | Fmaj7 65 69 72 76 | predominant |
| V | G 67 71 74 | G7 67 71 74 77 | dominant |
| vi | Am 69 72 76 | Am7 69 72 76 79 | tonic substitute |
| vii° | Bdim 71 74 77 | Bm7b5 71 74 77 81 | weak dominant |

| Degree (C minor) | Triad | 7th chord | Harmonic-minor alteration |
|---|---|---|---|
| i | Cm 60 63 67 | Cm7 60 63 67 70 | Cm(maj7) 60 63 67 71 |
| ii° | Ddim 62 65 68 | Dm7b5 62 65 68 72 | — |
| III | Eb 63 67 70 | Ebmaj7 63 67 70 74 | — |
| iv | Fm 65 68 72 | Fm7 65 68 72 75 | — |
| v | Gm 67 70 74 | Gm7 67 70 74 77 | **V = G 67 71 74; G7 67 71 74 77** |
| VI | Ab 68 72 75 | Abmaj7 68 72 75 79 | — |
| VII | Bb 70 74 77 | Bb7 70 74 77 80 | vii° = Bdim 71 74 77 |

Two modal substitutions carry most of the genre colour (derived):
- **Dorian:** the iv chord becomes **F major (65 69 72)**. A major IV in a minor key is the single most recognisable neo-soul sound.
- **Mixolydian:** **bVII (Bb 70 74 77)** becomes diatonic, which produces the rock and gospel I–bVII–IV.

A production heuristic, not a theory rule, also affects key choice in 808 genres. Pick a key whose tonic falls where the 808 sample sounds best, roughly MIDI 28–33 (41–55 Hz). That makes F, F#, G and A minor practical defaults (convention).

### Chord formulas and voicing rules decide whether a progression sounds expensive or muddy

The chord library below is built on C4 = 60. Formulas are standard. Colour descriptions are convention.

| Symbol | Formula (semitones) | On C (MIDI) | Colour |
|---|---|---|---|
| maj | 0 4 7 | 60 64 67 | stable, bright |
| m | 0 3 7 | 60 63 67 | stable, dark |
| dim | 0 3 6 | 60 63 66 | tense, passing |
| aug | 0 4 8 | 60 64 68 | unresolved, eerie |
| sus2 | 0 2 7 | 60 62 67 | open, ambiguous |
| sus4 | 0 5 7 | 60 65 67 | wants to resolve 4→3 |
| 5 (power) | 0 7 12 | 48 55 60 | neutral; safe very low |
| 6 / m6 | 0 4 7 9 / 0 3 7 9 | 60 64 67 69 / 60 63 67 69 | vintage / noir-Dorian |
| add9 / m(add9) | 0 4 7 14 / 0 3 7 14 | 60 64 67 74 / 60 63 67 74 | pop shimmer / sad-beautiful trap piano |
| 6/9 | 0 4 7 9 14 | 60 64 67 69 74 | open final chord |
| maj7 | 0 4 7 11 | 60 64 67 71 | lush, dreamy |
| 7 | 0 4 7 10 | 60 64 67 70 | dominant, bluesy |
| m7 | 0 3 7 10 | 60 63 67 70 | mellow minor |
| m(maj7) | 0 3 7 11 | 60 63 67 71 | spy and noir |
| m7b5 | 0 3 6 10 | 60 63 66 70 | yearning ii in minor |
| dim7 | 0 3 6 9 | 60 63 66 69 | symmetrical suspense |
| 7sus4 | 0 5 7 10 | 60 65 67 70 | gospel/house suspended dominant |
| maj9 | 0 4 7 11 14 | 60 64 67 71 74 | R&B/lo-fi tonic |
| 9 | 0 4 7 10 14 | 60 64 67 70 74 | funk dominant |
| m9 | 0 3 7 10 14 | 60 63 67 70 74 | deep house / neo-soul minor |
| m11 | 0 3 7 10 14 17 | 60 63 67 70 74 77 | airy minor |
| maj7#11 | 0 4 7 11 18 | 60 64 67 71 78 | Lydian shimmer |
| 13 (omit 5, 11) | 0 4 10 14 21 | 60 64 70 74 81 | soulful dominant |
| 7b9 / 7#9 | 0 4 7 10 13 / 0 4 7 10 15 | 60 64 67 70 73 / 75 | dark / funky dominant |
| slash Bb/C | bass + foreign triad | 48 \| 58 62 65 | C9sus sound; gospel, house |

The minor-9th chord (C Eb G Bb D), transposed in parallel as a full five-note shape, is a defining deep-house sound ([MusicRadar](https://musicradar.com/how-to/how-to-create-deep-house-minor-ninth-chords), via search summary).

Avoid-note conventions (convention):
- A natural 11 over a major or dominant chord clashes a minor 9th above the 3rd, so use #11 instead.
- b9 belongs on dominant chords only.
- On chords of five or more notes, drop the 5th first and then the root, because the bass already has it.

**Most of a chord's beauty comes from voicing, not from its name.** Low-interval limits mark the lowest register where an interval sounds before it turns to mud. Consonant intervals can sit lower than dissonant ones. They are guidelines, not absolutes, and the threshold shifts with dynamics and timbre: soft strings forgive more than loud brass ([Robin Hoffmann: Low Interval Limits](https://www.robin-hoffmann.com/dfsb/low-interval-limits); [Sleepfreaks](https://sleepfreaks-dtm.com/en/music-theory-beginner/voicing-arpeggio/)). Wider intervals belong in the bass register and smaller gaps higher up. Close voicing gives density, and open voicing gives clarity ([Open Music Theory](https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_(Gotham_et_al.)/10%3A_Orchestration/10.01%3A_Core_Principles_of_Orchestration)).

The commonly reproduced Berklee-style values below give the lowest recommended note of each interval. They are **approximate**: the source chart is an image that could not be machine-read, and sources differ.

| Interval | Lowest note (≈) |
|---|---|
| minor 2nd | E3 (52) |
| major 2nd | Eb3 (51) |
| minor 3rd | C3 (48) |
| major 3rd | Bb2 (46) |
| perfect 4th | Bb2 (46) |
| tritone | B2 (47) |
| perfect 5th | Bb1 (34) |
| minor 6th | G2 (43) |
| major 6th, minor 7th, major 7th | F2 (41) |
| minor 9th | E2 (40) |
| major 9th | Eb2 (39) |
| major 10th | Bb1 (34) |

These collapse into five programmable voicing rules (convention, derived from the above):
1. When an 808 or sub plays the root, keep chord instruments mostly above about **MIDI 48** and never double the sub's octave.
2. Below MIDI 48, use only root, 5th and octave.
3. Place 3rds and 10ths around 48–60, 7ths and 9ths above about 55, and clusters above about 60.
4. A spread 10th in the left hand (48 | 64) sounds warmer than a close 3rd down low.
5. **The top voice is heard as the melody.** Choose it deliberately and move it by step.

The standard voicing shapes follow (derived):
- **Inversions of C:** root 60 64 67; 1st inversion 64 67 72 (C/E); 2nd inversion 67 72 76 (C/G).
- **Open Cmaj7:** 48 55 64 71.
- **Drop-2 Cmaj7:** take closed 60 64 67 71 and drop the second-highest note an octave, giving 55 60 64 71.
- **Shells (root + 3rd + 7th):** Cmaj7 48 59 64; G7 43 | 53 59.
- **Rootless voicings,** for when a bass carries the root:
  - Dm9 = 53 57 60 64.
  - G13 = 53 57 59 64.
  - Cmaj9 = 52 55 59 62.
- **Quartal stacks:** D G C F = 62 67 72 77, giving a modal "So What" or ambient colour.

The rootless shapes show why the bass names the chord. A rootless Am9 (C E G B) is literally a Cmaj7, so pads playing C–E–G–B over a bass A are heard as Am9.

### Function, cadences and smooth voice leading create tension and release

Chords fall into three families: tonic (I, vi, iii), predominant (IV, ii) and dominant (V, vii°). Cadences punctuate phrases ([Wikipedia: Cadence](https://en.wikipedia.org/wiki/Cadence)):
- **Authentic (V→I):** a full stop.
- **Half (ending on V):** a comma.
- **Plagal (IV→I):** a soft "amen".
- **Deceptive (V→vi):** a surprise.

V7→I resolves because of its tritone. G7 is 67 71 74 77. B rises a semitone to C (71→72), and F falls a semitone to E (77→76), so the tritone B–F collapses inward onto the third C–E (derived).

Spelled as bass | upper (derived):
- **Perfect authentic:** G7 43 | 59 65 67 → C 48 | 60 64 67.
- **Deceptive:** G7 → Am 45 | 60 64. The upper voices resolve exactly as before, but the bass steps up G→A.
- **Minor plagal:** Fm 41 | 60 65 68 → C 48 | 60 64 67. The A→Ab→G line is the emotional engine.
- **Phrygian half cadence:** Dm/F 41 | 57 62 → E 40 | 56 59 64. The bass semitone F→E is the flamenco pull.

Loop genres usually avoid a full authentic cadence so the loop never "ends". Native Instruments' lo-fi examples deliberately omit I or end on V7 to keep the loop cycling ([Native Instruments](https://blog.native-instruments.com/lo-fi-chord-progressions/)). A skill should save strong V7→I for endings, pre-chorus-to-chorus lifts and R&B or gospel moments.

**Voice leading** is what makes a progression sound polished. Common-practice conventions favour smooth, mostly stepwise lines and avoid parallel fifths and octaves, because they reduce the independence of the voices ([Wikipedia: Voice leading](https://en.wikipedia.org/wiki/Voice_leading)). Guide tones show the principle at its smallest. In ii–V–I, and in its tritone-substitute version, the 3rds and 7ths descend by semitone ([Wikipedia: Tritone substitution](https://en.wikipedia.org/wiki/Tritone_substitution)).

A **nearest-voicing algorithm** encodes this for a composer skill (convention):
1. For each new chord, enumerate every inversion and octave placement of its pitch classes inside a target window, such as MIDI 52–76 for keys.
2. Choose the placement that minimises total semitone movement from the previous voicing.
3. Penalise these cases:
   - voice crossings;
   - parallel perfect 5ths or octaves between the outer voices;
   - intervals below the low-interval limit;
   - a top-voice leap larger than a 4th.
4. Exempt the bass from the motion penalty. The bass may leap by 4ths and 5ths, and contrary motion against the top voice is what makes progressions feel strong.

Common tones guide the choice (derived):
- Roots a 3rd apart share two notes.
- Roots a 5th apart share one.
- Roots a step apart share none, so move the upper voices against the bass.

The algorithm reduces C–Am–F–G to upper-voice moves of 1–3 semitones (derived):

C 48 | 60 64 67 → Am 45 | 60 64 69 → F 41 | 60 65 69 → G 43 | 59 62 67

### A short list of chromatic devices produces most "emotional" moments

The borrowed iv and the bVI and bVII from the parallel minor sound bittersweet or epic. Common rock progressions are built from borrowed chords, and the backdoor progression **iv7–bVII7–I** (Fm7–Bb7–C) is the jazz alternative to ii–V–I ([Wikipedia: Borrowed chord](https://en.wikipedia.org/wiki/Borrowed_chord); [Wikipedia: Backdoor progression](https://en.wikipedia.org/wiki/Backdoor_progression)). Five other devices round out the list:
- **Secondary dominants** briefly tonicise a degree other than the tonic. Example: Am7–D7–G in C ([Wikipedia: Secondary chord](https://en.wikipedia.org/wiki/Secondary_chord)).
- **Tritone substitution** replaces V7 with bII7, because both share the same tritone. Dm7–Db7–Cmaj7 then walks the bass D–Db–C ([Wikipedia: Tritone substitution](https://en.wikipedia.org/wiki/Tritone_substitution)).
- **Chromatic mediants** are chords with roots a third apart, related chromatically. C major moves to E, A, Eb or Ab major and keeps one common tone ([Wikipedia: Chromatic mediant](https://en.wikipedia.org/wiki/Chromatic_mediant)).
- A **pedal point** holds one tone, usually in the bass, while the harmonies above it change ([Wikipedia: Pedal point](https://en.wikipedia.org/wiki/Pedal_point)).
- The **Picardy third** ends a minor section on a major tonic ([Wikipedia: Picardy third](https://en.wikipedia.org/wiki/Picardy_third)).

Spelled in C (derived), each device has a production use:

| Device | Spelling | Use |
|---|---|---|
| bVI–bVII–I ("Mario cadence") | Ab 44 \| 60 63 68 → Bb 46 \| 62 65 70 → C 48 \| 64 67 72 | triumphant resolution; trailers, synthwave, EDM |
| Secondary dominant V/V | D7 50 \| 54 57 60 → G | the F# acts as a leading tone into G |
| Secondary dominant V/vi | E7 40 \| 56 59 62 → Am | the G# pulls to A; an R&B and gospel favourite |
| Tritone sub | Dm9 38 \| 53 57 60 64 → Db9(#11) 37 \| 53 55 59 63 → Cmaj9 36 \| 52 55 59 62 | slinky R&B |
| Chromatic mediant | C 48 \| 60 64 67 → E 52 \| 59 64 68 | wonder, reveal |
| Pedal | upper chords C → Bb/C → Ab/C → Bb/C → C over a held C2 (36) | the 808 stays on the root while tension builds; drill, house, film builds |
| Line cliché | Am 57 60 64 → Am(maj7) 56 60 64 → Am7 55 60 64 → Am6 54 60 64 | instant noir sophistication |

Modulation has five standard routes (convention):
1. **Pivot chord.** Am is vi in C and ii in G, so it can carry the music into G.
2. **The new key's V7.**
3. **"Truck-driver" lift** of a semitone or tone for the final chorus. Trance often uses this lift on its final drop.
4. **Relative switch.** An A-minor verse moves to a C-major chorus.
5. **Parallel switch.** A C-minor verse moves to a C-major chorus.

### Twenty loops cover most modern music

The sourced progression facts:
- **I–V–vi–IV** (the "Axis" progression) and its rotations are everywhere in pop. **I–V–bVII–IV** swaps vi for bVII to add a bluesy flavour ([Wikipedia: I–V–vi–IV](https://en.wikipedia.org/wiki/I%E2%80%93V%E2%80%93vi%E2%80%93IV_progression)).
- The **Andalusian cadence** (i–bVII–bVI–V) descends stepwise and dates back to the Renaissance ([Wikipedia: Andalusian cadence](https://en.wikipedia.org/wiki/Andalusian_cadence)).
- The **royal road** (IVmaj7–V7–iii7–vi) is a J-pop staple. Producer Seiji Kameda called it the "little devil" progression, likening the move from major V to minor iii to playful heartbreak ([Wikipedia: Royal road](https://en.wikipedia.org/wiki/Royal_road_progression)).
- The **quick-change 12-bar blues** runs I IV I I | IV IV I I | V IV I I ([Wikipedia: Twelve-bar blues](https://en.wikipedia.org/wiki/Twelve-bar_blues)).
- **Lo-fi staples** ([Native Instruments](https://blog.native-instruments.com/lo-fi-chord-progressions/); [Audeobox](https://www.audeobox.com/learn/fl-studio/how-to-make-lofi-beats-in-fl-studio/)):
  - Cmaj7–Am7.
  - Fmaj7–Em7–Am7, which has no tonic.
  - Am7–F–E7, where the dominant restarts the loop instead of resolving.
  - Dm9–G13–Cmaj9–Am7.
  - Cmaj7–A7–Dm7–G7.
- **Trap minor loops:** i–VI–v–i and i–v–iv (Cm–Ab–Gm–Cm) ([eMastered](https://emastered.com/blog/trap-chord-progressions)).
- **Drill loops:** i–v–VI, i–VII–VI and i–iv–VII–III ([Orphiq](https://orphiq.com/resources/drill-chords), via search summary).

The voicings below are derived and voice-led, written bass | upper.

| # | Progression | Spelled voicing | Mood and genre |
|---|---|---|---|
| 1 | I–V–vi–IV (C) | C 48\|60 64 67 → G 43\|59 62 67 → Am 45\|60 64 69 → F 41\|60 65 69 | anthemic; pop, EDM |
| 2 | vi–IV–I–V (C) | Am9 45\|59 60 64 67 → Fmaj9 41\|57 60 64 67 → Cadd9 48\|55 62 64 67 → G6 43\|55 59 62 64 | melancholic-hopeful; future bass |
| 3 | ii–V–I (C) | Dm9 38\|53 57 60 64 → G13 43\|53 57 59 64 → Cmaj9 36\|52 55 59 62 | warm resolution; lo-fi, neo-soul |
| 4 | minor ii–V–i (Cm) | Dm7b5 38\|53 56 60 → G7b9 43\|53 56 59 → Cm9 36\|51 55 58 62 | dark sophistication |
| 5 | i–VI–III–VII (Cm) | Cm 48\|60 63 67 → Ab 44\|60 63 68 → Eb 39\|58 63 67 → Bb 46\|58 62 65 | epic minor; trance, synthwave, trailers |
| 6 | i–bVI–bVII–i (Cm) | Cm → Ab 44\|60 63 68 → Bb 46\|62 65 70 → Cm 48\|63 67 72 | heroic |
| 7 | Andalusian (Cm, 808 version) | Cm 36\|60 63 67 → Bb 34\|58 62 65 → Ab 32\|60 63 68 → G 31\|59 62 67 | fateful; trap, drill |
| 8 | Trap i–VI–v (Cm) | Cm 36\|60 63 67 → Ab 44\|60 63 68 → Gm 43\|58 62 67 | dark with a lift |
| 9 | Drill i–v–VI / i–VII–VI | Cm → Gm 43\|58 62 67 → Ab 44\|60 63 68; Cm → Bb 34\|58 62 65 → Ab 32\|60 63 68 | tense, circular |
| 10 | Royal road (C) | Fmaj7 41\|57 60 64 → G7 43\|59 62 65 → Em7 40\|59 62 67 → Am7 45\|60 64 67 | nostalgic; anime, future bass |
| 11 | Dorian vamp (C) | Cm9 36\|51 55 58 62 → F9 41\|51 55 57 60 | cool minor; neo-soul, deep house |
| 12 | Lo-fi I–vi | Cmaj9 48\|52 55 59 62 → Am9 45\|55 59 60 64 | endless float |
| 13 | IV–iii–vi (no tonic) | Fmaj7 41\|57 60 64 → Em7 40\|55 59 62 → Am7 45\|55 60 64 | unresolved |
| 14 | Backdoor (C) | Fm7 41\|56 60 63 → Bb7 46\|56 62 65 → Cmaj7 48\|55 59 64 | soulful landing |
| 15 | 12-bar shells (C) | C7 48\|58 64 → F7 41\|57 63 → G7 43\|59 65 | boom bap, funk |
| 16 | Gospel walk-up | Cmaj9 → C7/E 52\|58 60 64 → Fmaj7 → F#dim7 42\|57 60 63 → C/G → A7 → Dm9 → G13 | R&B fingerprint |
| 17 | Deep-house stab chain (Am) | Am9 45\|60 64 67 71 → Dm9 50\|60 64 65 69, or the same shape shifted in parallel | deep house |
| 18 | Minor plagal ballad | C → F → Fm 41\|60 65 68 → C | tears |

The emotional conventions condense into a short cheat sheet (convention):
- **Loops built on I** sound optimistic.
- **Starting on vi or i** sounds melancholic.
- **Ending the loop on V** sounds restless.
- **Ending on IV** sounds open.
- **Borrowed iv or bVI** sounds bittersweet.
- **bVI–bVII–I** sounds triumphant.
- **A chromatic mediant** sounds like awe.
- **b2 or b6→5 semitones** sound like menace.
- **maj7 and 9 colours** sound like warmth and late-night nostalgia.

### Harmonic rhythm and comping differ more by genre than progression choice does

Harmonic rhythm is the rate at which chords change, and whether it counts as "fast" is relative ([Wikipedia: Harmonic rhythm](https://en.wikipedia.org/wiki/Harmonic_rhythm)). The table below gives the convention defaults per genre; none of them are measured.

| Genre | Typical BPM | Chord changes | Loop |
|---|---|---|---|
| Trap | 130–160 half-time | 1 per 1–2 bars | 2–4 chords over 4–8 bars |
| Drill | 138–145 | 1 per 1–2 bars | 4–8 bars |
| Boom bap | 85–95 | from the sample, 1–2 per bar | 1–4 bars |
| Lo-fi | 70–90 | 1 per bar | 2–4 bars |
| R&B / neo-soul | 60–100 | 1–2 per bar plus passing chords | 4–8 bars |
| Pop | 90–130 | 1 per bar; doubles in the pre-chorus | 4 bars |
| House | 118–126 | 1 per 1–2 bars | 2–8 bars |
| Future bass | 140–160 | 1 per bar in the drop | 4–8 bars |
| Cinematic | free | 1 per 2–8 bars, or a pedal | phrase-based |

Comping rhythms follow genre too (convention):
- **Pads:** whole notes played legato.
- **Pop:** 8th-note pulses, with chord changes anticipated a 16th or 8th early.
- **R&B:** the next chord arrives on step 15 of the previous bar, and chords are rolled bottom-to-top over 10–30 ms.
- **Lo-fi:** half or whole notes, humanised ±10–30 ms, with velocity 60–90.
- **House:** short stabs on the offbeats, steps 3, 7, 11 and 15.
- **Future bass:** a supersaw chord on the downbeat, then gated 16th chops with pitch-bend swells.
- **Trap and drill:** keys often become arpeggios or bells outlining the chord tones, while the 808 marks each chord change.

Four design rules apply across genres:
1. Change chords on the bar downbeat.
2. Speed up harmonic rhythm going into a section change.
3. Hold a pedal during builds so the tension comes from rhythm and filtering.
4. Let the melody move faster than the chords.

## Beautiful melodies are mostly steps, one climax and one surprise

### Contour and interval statistics give a measurable grammar

Corpus research supplies the defaults. Huron analysed 6,251 melodies from the European subset of the Essen folksong corpus. Across datasets, contours fall into four broad shapes: convex (arch), concave, descending and ascending. **The arch predominates in Essen, followed by ascending and then descending**, and pitch tends to hold steady at the start of a phrase and fall at the end ([arXiv 2604.13119](https://arxiv.org/pdf/2604.13119)). Ableton's teaching adds three practical rules ([Ableton: Contour](https://makingmusic.ableton.com/creating-melodies-1-contour)):
- Balance each rise with a fall of roughly the same size.
- Give most melodies **one highest note that occurs once**, often on a strong beat.
- Treat both rules as tendencies. Good melodies do not obey them every time.

Interval sizes are just as regular. **Most melodic motion is by steps of 2 semitones or less, and the whole step is more common than the half step**, probably because scales contain more whole steps ([Patel 2007](https://acousticslab.org/RECA293/293Files/293Downloads/Patel2007_MelodicStatsAndContour.pdf)). Steps also tend to continue in the same direction ([Music & Science summary](https://doaj.org/article/43b320953f444935a677d6cec2cb74f8)).

After a leap, melodies usually reverse direction. Von Hippel and Huron showed that this "gap-fill" tendency is largely regression to the mean. Leaps tend to land near the edge of a melody's range, and from there the melody "has little choice but to retreat". The pattern held in vocal melodies from four continents ([von Hippel & Huron, Sonicfield entry](https://labs.sonicfield.org/library/why-do-skips-precede-reversals-the-effect-of-tessitura-on-melodic-structure)).

A melody generator can encode this grammar directly (convention):
- **Interval mix.** About 65–80% of intervals should be steps of 0–2 semitones, 15–25% thirds, and no more than 10% leaps of 5 or more semitones. Allow one signature leap per hook.
- **Gap-fill.** After any leap of 5 or more semitones, move the next 2–4 notes stepwise in the opposite direction.
- **Regression to the mean.** Track the phrase's running mean pitch. When the line drifts more than 7 semitones from it, bias the next move back toward it.
- **Climax placement.** Put the climax 55–75% of the way through the phrase, for example the downbeat of bar 5 or 6 in an 8-bar phrase. The next section may peak 2–5 semitones higher.

Contour should also follow the section's job:
- **Dark loops** in trap, drill and lo-fi favour descending or inverted-arch shapes.
- **Pre-choruses** rise.

Ranges are practical approximations, not sourced figures (convention):

| Part | Total range | Typical register |
|---|---|---|
| Pop topline | 9–14 semitones | male A2–A4 (45–69); female F3–F5 (53–77) |
| Verse topline | narrower 5–9 semitones | chorus sits 3–5 semitones higher |
| Instrumental hook motif | 5–9 semitones | octave doubling adds width |
| Bells and leads | up to 24 semitones, including doubling | — |
| Bass-register melody (808, log drum) | — | E1–E3 (28–52) |

### Motifs, development and 8-bar templates

A motif is "the smallest structural unit possessing thematic identity", and it can be melodic, harmonic or rhythmic. Beethoven's Fifth reuses a four-note short-short-short-long cell in many permutations ([Wikipedia: Motif](https://en.wikipedia.org/wiki/Motif_(music))).

Two 8-bar templates do most of the structural work. **The period** pairs an antecedent phrase, which ends on an unstable degree (2, 5 or 7) over V, with a consequent phrase that ends on 1 over I. **The sentence** states a basic idea, repeats it or sequences it, then condenses toward a cadence. Schoenberg considered the sentence the higher form because it starts developing immediately ([Wikipedia: Sentence](https://en.wikipedia.org/wiki/Sentence_(music))). In bars, the sentence is 2 + 2 + 4: a 2-bar idea, its 2-bar repetition, then 2 bars of fragments climbing in energy and a 2-bar cadence (convention).

Phrase grouping also carries emotion. Pattison's prosody teaching treats even numbers of phrases with matched lengths as stable, and odd numbers or mismatched lengths as unstable ([Coursera: Pattison, Berklee](https://www.coursera.org/learn/songwriting-lyrics)). That makes a 3- or 5-bar pre-chorus a deliberate destabilising device.

Development operations can be applied directly to a list of (offset, MIDI, duration) notes. Operations are standard theory; the effects are convention.

| Technique | Operation | Effect |
|---|---|---|
| Repetition | copy at +N bars | identity, memorability |
| Diatonic sequence | shift by k scale steps | stays in key; the pop/EDM default |
| Real transposition | all MIDI ± k | same shape, new colour |
| Inversion | MIDI′ = 2·axis − MIDI | mirrored "answer" |
| Augmentation / diminution | durations ×2 / ×0.5 | half-time drops / build-ups |
| Rhythmic displacement | offsets ±0.25 or ±0.5 beat | syncopated renewal; common in trap and afro |
| Fragmentation | repeat the head or tail cell | continuations, builds |
| Tail change | keep the first ~70%, alter the last 1–2 notes | question → answer |
| Interval expansion | widen one interval | the climax "surprise" |

The rule of three ties these together (convention): state the motif, repeat it, then break the pattern on the third statement (A A A′ B).

### Chord tones on strong beats, resolving dissonance on weak ones

Non-chord tones have fixed mechanics ([Wikipedia: Nonchord tone](https://en.wikipedia.org/wiki/Nonchord_tone)):
- **Passing tones** move step–step in one direction.
- **Neighbour tones** step away and step back.
- **Appoggiaturas** are approached by leap and resolved by step. They are accented.
- **Suspensions** are tied over the chord change and resolve down by step: 4–3, 7–6 or 9–8.
- **Anticipations** sound the next chord's tone early.

The appoggiatura is where much of melody's emotional force lives. In Sloboda's study, 83 listeners identified passages that gave them physical reactions. Tears were linked most reliably to **melodic appoggiaturas and sequences** ([NPR summary](https://www.npr.org/2012/02/13/146818461/the-ballad-of-the-tearful-why-some-songs-make-you-cry)). One caveat: only passages that worked were analysed, so we do not know how often the device fails.

Real songs vary widely in how strictly they follow chord tones. Hooktheory's TheoryTab analyses show individual songs with **45–69%** of melody notes on chord tones ([Hooktheory](https://www.hooktheory.com/theorytab/view/harry-styles/pop)).

Placement and targeting follow convention:
- **Strong beats.** Use a chord tone on beats 1 and 3 about 75–85% of the time.
- **Weak positions.** Non-chord tones are free on off-beats and 16ths if they resolve by step.
- **Target priority:** the **3rd** for emotion, the **root** for cadences, the **5th** for neutral openness, and the **7th or 9th** for R&B colour.
- **Chord changes.** Move by step to the nearest 3rd or 7th of the new chord.

The expressive tensions are just as consistent (convention):
- The 9th sounds airy and modern.
- A sus4 resolving to the 3rd conveys longing.
- b6→5 in minor is the sorrowful trap staple.
- b2→1 sounds menacing.
- The maj7 over IV sounds dreamy, lo-fi.

### Rhythm carries the hook as much as pitch does

Earworm research gives the strongest evidence on catchiness. Jakubowski, Finkel, Stewart and Müllensiefen compared 100 frequently named earworms with 100 non-earworm tunes matched for chart popularity and recency. About 3,000 participants named the earworms, and the songs spanned pop, rock, rap and R&B from data collected in 2010–2013 ([Goldsmiths](https://research.gold.ac.uk/19405); [Neuroscience News](https://neurosciencenews.com/song-stuck-in-head-5423/)). Earworms had three features:
- **Faster tempi.**
- **More common global contours.** The typical rise-and-fall shape of "Twinkle Twinkle", which "Moves Like Jagger" also follows.
- **Less common interval patterns between turning points.** Unexpected leaps, or more repeated notes than usual.

Chart success and recency also predicted earworm status ([Durham repository](https://durham-repository.worktribe.com/OutputFile/1371487); [APA](https://www.apa.org/news/press/releases/2016/11/earworms)). The most-named earworms were "Bad Romance", "Can't Get You Out of My Head", "Don't Stop Believin'", "Somebody That I Used to Know" and "Moves Like Jagger".

Producer guidance arrives at the same formula from experience:
- Simple ideas with few notes, refined by subtraction ([Lost Stories Academy](https://loststoriesacademy.com/blogs-and-tutorials/the-science-behind-catchy-edm-hooks)).
- One element that becomes the drop's identity ([Lost Stories Academy](https://loststoriesacademy.com/blogs-and-tutorials/the-secret-to-writing-drops-that-people-actually-remember)).
- Only one lead sound at a time in a drop ([Bax-shop](https://www.bax-shop.co.uk/blog/dj-gear/edm-tips-tricks-how-to-make-the-ultimate-drop/)).

A hook-scoring checklist for a skill follows (convention):
- **Contour.** The global shape is common: an arch, or a descent to 1, 3 or 5.
- **Size.** The motif lasts 2–4 beats, uses 3–7 distinct notes, and spans 9 semitones or less.
- **Repetition.** It repeats at least twice within the hook, and the hook recurs 4–8+ times in the song.
- **Surprise.** There is **exactly one surprise**: a 6th, 7th or octave leap, a borrowed note, a displacement, or a run of repeated notes broken by a leap.
- **Note rate.** The rate is lively; use 8ths or 16ths at slow BPMs.
- **Lyric placement.** The title lands on the climax or on the longest note.

Rhythm should be written first (convention):
- Use 4–8 onsets per bar, at least one syncopation, and at least one rest of half a beat or more.
- Pull arrival notes earlier as "pushes": an 8th early (−0.5 beat) or a 16th early (−0.25 beat).
- Use stock cells:
  - **Tresillo:** onsets at 0, 0.75 and 1.5 beats, repeated each half bar. Afro, dancehall and trap bells use it.
  - **Charleston:** onsets at 0 and 0.75.
  - **House offbeat stabs:** 0.5, 1.5, 2.5 and 3.5.

Note density depends on the part's role:

| Part | Onsets per bar |
|---|---|
| Verse topline | 4–10 |
| Chorus | 3–8, with longer notes |
| EDM drop riff | 4–12 |
| Trap bells | 4–8, with lots of space |
| Counter-melody | about half the lead's density |

### Counter-melodies stay independent through contrary motion and complementary rhythm

Parallel 5ths and octaves are avoided in classical writing because they erase the independence of the voices. Contrary and oblique motion preserve it. Parallel fifths remain idiomatic in rock power chords and folk ([Wikipedia: Consecutive fifths](https://en.wikipedia.org/wiki/Consecutive_fifths)).

That gives two production modes (convention):
- **Thicken a single line.** Use octave doubling, or diatonic 3rds or 6ths. Drop the doubled layer's velocity 10–20%.
- **Write a true counter-melody.** It should:
  - fill the lead's rests;
  - move contrary at phrase boundaries and against the lead's leaps;
  - stay at least 3 semitones from the lead and never cross it;
  - use about half the lead's density, or the opposite density (long notes under a busy lead);
  - favour 3rds, 6ths and 10ths on strong beats.

Outer voices (melody against 808) should mostly move contrary or oblique.

### An 11-step melody algorithm for the piano roll

The researchers condensed the methods above into a pipeline (convention, built from the cited Ableton, Bax-shop, Lost Stories, RouteNote and MusicGurus guidance):
1. **Set the context.** Key and scale by genre:
   - trap: minor, harmonic minor or Phrygian;
   - pop: major or Aeolian;
   - lo-fi: Dorian;
   - afro: major pentatonic.

   Also set the BPM, a loop length of 2, 4 or 8 bars, and the chords.
2. **Write the rhythm first.** 4–8 onsets per bar, with one syncopation and one rest.
3. **Place the pitch skeleton.** Put a chord tone on each strong onset. Prefer the 3rd, then the 5th, then the 7th or 9th; keep the root for the cadence.
4. **Fill.** Connect the skeleton with passing and neighbour tones, keeping 65–80% steps and applying gap-fill after leaps.
5. **Call and response.** Bars 1–2 end on 2, 5 or 7. Bars 3–4 answer with a tail change that ends on 1 or 3.
6. **Climax.** Make exactly one note the highest, at 55–75% of the phrase, and make it the surprise.
7. **Range check.** Toplines span 14 semitones or less. Leads stay above about MIDI 52 to keep clear of the 808.
8. **Develop across the song.** Verse low and narrow, pre-chorus rising, chorus higher with longer notes. Use augmentation for half-time drops and diminution for builds.
9. **Layer.** Add octave doubling and a counter-line.
10. **Subtract.** Remove 10–20% of the notes, then confirm the motif is still recognisable after four repeats and still implies the harmony when soloed.
11. **Humanise by genre.** Tight for EDM and trap. For lo-fi and R&B, ±10–20 ms timing and velocity variation of ±10–15.

The trap guidance also says melodies should stay simple and repetitive so the 808 has room ([RouteNote](https://create.routenote.com/blog/how-to-make-trap-melodies/)).

A worked trap bell loop shows the result (convention, original):
- **Setup:** A harmonic minor over Am | F | Dm | E, at 140 BPM.
- **Bar 1:** A4 69, C5 72, E5 76, C5 72, B4 71, A4 69, E4 64.
- **Bar 2:** F5 77 (the dark b6), E5 76, C5 72, B4 71, G#4 68 (the leading tone over E, held), then a rest.
- **Range:** 64–77.
- **Layers and register:** an optional −12 doubling, with everything kept above 52 for the 808.

## Drums groove when clear anchors meet medium syncopation

### Meter, backbeat, half-time and the tresillo explain nearly every beat style

Almost every genre covered here runs in 4/4 on a 16-step grid. Feel comes from three things: where the accents fall relative to the strong beats, how much syncopation there is, and which cross-rhythms are layered on top.

**Half-time** moves the snare from beats 2 and 4 to beat 3, so quarter notes start to feel like 8ths in one giant bar ([Wikipedia: Half-time](https://en.wikipedia.org/wiki/Half-time_(music))). That is why one drill track can be listed at both 70 and 140 BPM, with both figures correct ([Tracklib](https://www.tracklib.com/blog/drill-beat)). It also explains the trap default: 140 BPM lets vocalists switch between double-time and half-time flows ([Audeobox: Trap](https://www.audeobox.com/learn/fl-studio/how-to-make-trap-beats-in-fl-studio/)). Trap is partly defined by "double-time, triple-time, and similarly divided" hi-hats over deep 808 kicks ([Wikipedia: Trap music](https://en.wikipedia.org/wiki/Trap_music)).

The **tresillo** is the other key building block. It can be written as dotted-8th, dotted-8th, 8th, or additively as 3+3+2 sixteenths. It is found across Africa and from Morocco to Indonesia ([Wikipedia: Tresillo](https://en.wikipedia.org/wiki/Tresillo_(rhythm))). On the grid, hats on steps 1, 4 and 7 make a basic tresillo ([Native Instruments: Drill](https://blog.native-instruments.com/drill/)). Dembow's bounce is a looped 3+3+2 cross-rhythm ([Wikipedia: Dembow](https://en.wikipedia.org/wiki/Dembow)). The full-bar version over 8ths falls on steps 1, 7 and 13 (derived). Four genre families rest on this 3+3+2 grouping:
- drill hats;
- reggaeton snares;
- afrobeats and afro-house percussion;
- the Jersey club kick run (steps 1, 5, 9, 12, 15, grouped 4-4-3-3-2).

### Each drum role owns a job, and the parts interlock rather than stack

Boom bap is literally named after its two anchors: the "boom" (a deep, round kick) and the "bap" (a tight, snapping snare) ([Audeobox: Boom bap](https://www.audeobox.com/learn/fl-studio/how-to-make-boom-bap-beats-in-fl-studio/)). Each drum has a defined role:
- **Kick:** the pulse. Four-on-the-floor (a kick on every quarter) is the core of disco and house ([Wikipedia: Four on the floor](https://en.wikipedia.org/wiki/Four_on_the_floor_(music))).
- **Snare or clap:** the backbeat anchor.
- **Hats and shakers:** subdivision energy.
- **Open hats:** offbeat lift.
- **Ghost notes:** quiet in-between strokes ([Wikipedia: Ghost note](https://en.wikipedia.org/wiki/Ghost_note)).
- **Crashes:** mark phrase boundaries. In the Amen break the drummer closes the 4-bar phrase with an early crash ([Wikipedia: Amen break](https://en.wikipedia.org/wiki/Amen_break)).

Afrobeats inverts the hierarchy. It builds upward from interlocking percussion, and five core elements each own a frequency and rhythmic space ([Audeobox: Afrobeats](https://www.audeobox.com/learn/fl-studio/how-to-make-afrobeats-in-fl-studio/)):
- continuous 16th shaker;
- offbeat open hat;
- clave;
- congas;
- tuned log drum.

The sourced interlock principles are concrete:
- **Build around the kick, not over it.** Delete hats that duplicate kick transients ([Beatstorapon: Jersey club](https://beatstorapon.com/blog/how-to-make-a-jersey-club-beat/)).
- **Sidechain the 808 from the kick** so it ducks on each hit ([Audeobox: Trap](https://www.audeobox.com/learn/fl-studio/how-to-make-trap-beats-in-fl-studio/)).
- **Start drill 808 notes on or just after kicks** ([Audeobox: Drill](https://www.audeobox.com/learn/fl-studio/how-to-make-drill-beats-in-fl-studio/)).
- **Leave silence.** Drill wants a top line "with more silence in it than notes" ([Tracklib](https://www.tracklib.com/blog/drill-beat)), and boom bap "strips back" where trap stacks ([Audeobox](https://www.audeobox.com/learn/fl-studio/how-to-make-boom-bap-beats-in-fl-studio/)).

Five programmable interlock rules follow (convention):
1. Never put the kick and snare on the same step unless it is a deliberate accent.
2. A kick just before a snare pushes; a kick just after it bounces. For a snare on step 5, step 4 pushes and step 6 bounces.
3. Hats that coincide with kicks or snares can drop in velocity.
4. One answering element (open hat, rim or perc) closes each 2-bar phrase.
5. Three or four rhythmic layers carry the groove. Any extra layer must differ in register and subdivision.

Default velocity bands (convention, partly anchored to the drill ghost-note figure in [Audeobox: Drill](https://www.audeobox.com/learn/fl-studio/how-to-make-drill-beats-in-fl-studio/)):

| Element | MIDI velocity |
|---|---|
| Kick | 100–120 |
| Snare / clap | 105–127 |
| Ghost snare | 30–60 (drill: 40–50% ≈ 51–64) |
| 16th hats, on-beat | ≈110 |
| 16th hats, "&" | ≈95 |
| 16th hats, "e" and "a" | 60–70 |
| Open hat | 80–100 |
| Shaker | 50–80, accented on the offbeat |
| Crash | 100–120, on step 1 of a new section |

### Groove research says "medium syncopation, clear beat, dense subdivisions, little random jitter"

The most useful study for a drum skill is Witek et al. (2014). Sixty-six web participants rated 50 synthesised funk breaks at 120 BPM. **Medium syncopation produced the most desire to move and the most pleasure**, an inverted U (R² = .347 for wanting to move and .427 for pleasure, p < .001). People who enjoy dancing rated the beats higher, and audio entropy was a poor predictor. Witek's explanation is that medium syncopation leaves the meter predictable while still violating expectations. The body "fills in" the missing beat, and pleasure follows ([Witek et al. 2014, PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0094446)).

Senn et al. (2018) scaled this up to 248 reconstructed drum patterns, 665 participants and 8,329 ratings. **Syncopation and event density predicted groove positively. Beat salience, residual microtiming and rhythmic variability had no effect** ([Senn et al. 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6025871)). Madison et al., as reported by Witek, did find beat salience positive, so the role of beat salience remains unsettled across studies ([Witek 2014](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0094446)). The same Senn study found that familiarity with a drum pattern raised groove ratings, so genre-standard templates earn a familiarity bonus.

Matthews et al. (2019) found the rhythm-complexity effect was strongest alongside **medium-complexity chords**. Harmony mainly affected the pleasure component ([Matthews et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6328141)). The practical pairing for maximum groove is a medium-syncopation beat under 7th-chord-level harmony.

Microtiming is genuinely contested:
- **Davies et al. (2013).** Fully quantised versions earned the highest groove ratings, and systematic microtiming lowered ratings, except for the simple jazz shuffle ([INESC TEC](https://repositorio.inesctec.pt/handle/123456789/3901?mode=full)).
- **Senn et al. (2016).** With 79 expert and 81 non-expert listeners, a **"high groove zone" ran from fully quantised to the original performance timing**. Exaggerated microtiming lowered ratings, and experts were more sensitive ([Senn et al. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5050221)).
- **Kilchenmann and Senn (2015).** They measured body movement instead of ratings. Experts moved less to quantised clips than to a "tight" level of 60% reduced microtiming. At 80% reduction, the timing deviations spanned about −13/+17 ms for swing and −9/+12 ms for funk ([Frontiers 2015](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.01232/full)).

The defensible rule for a skill is to **quantise by default and treat swing as a structured, consistent ratio**. Keep any humanisation within about ±10–20 ms and make it systematic: a consistently late snare reads as laid back, and slightly early hats read as pushing. Random large offsets reduce groove. At 90 BPM, 10 ms is about 6% of a 16th, or roughly +6% in FL's graph-editor Shift, where 100% is about one 16th (derived).

**Low frequencies carry the beat in both brain and body.** In Lenc et al. (2018), rhythms played with low tones (130 Hz) produced stronger EEG tracking at the beat frequency than the same rhythms with high tones (1236.8 Hz), especially for syncopated rhythms ([Lenc et al. 2018, PNAS](https://doi.org/10.1073/pnas.1801421115)). Hove et al. (2014) found timing deviations were detected better in the lower of two streams, and tapping followed the lower stream. They traced the effect to the cochlea, and noted that across cultures melody tends to be high and rhythm low ([Hove et al. 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4104866)). Timing precision therefore matters most in the kick and bass.

Tempo preference clusters around 2 Hz. Moelants analysed DJ BPM lists covering over 70,000 pieces, plus tapping data. Tempos concentrated at **115–127 BPM, peaking near 125**, within a preferred range of roughly 67–150 BPM ([Frontiers 2022 paper citing Moelants](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.952488/pdf)). Half-time and double-time feels are how slower and faster genres keep a 2 Hz pulse available.

### Swing values: the Linn scale, the FL implementation and sourced genre settings

Roger Linn gives the clearest reference points. 50% is straight and 66% is a perfect triplet. **54% loosens straight-16th beats without sounding swung.** At 90 BPM, 62% feels looser than 66%. Useful settings run from 50% to about 70% ([Attack Magazine: Roger Linn](https://www.attackmagazine.com/features/interview/roger-linn-swing-groove-magic-mpc-timing/)). In jazz, swing ratios run from 1:1 to 3:1 and tend to be wider at slow tempos ([Wikipedia: Swing](https://en.wikipedia.org/wiki/Swing_(jazz_performance_style))).

FL Studio's step graph editor (Ctrl+K) offers per-step Velocity, Release, Fine pitch (±100 cents), Pan, Mod X (filter cutoff), Mod Y (resonance) and **Shift (start offset, 100% ≈ one 16th)** ([Image-Line manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/channelrack.htm)). Shift is FL's per-step microtiming tool.

The sourced genre swing values are listed below. MPC-scale and FL-scale figures are not interchangeable.

| Genre | Swing | Scale | Source |
|---|---|---|---|
| Chicago house, 120–125 BPM | 55–60% | MPC-style | [Attack](https://www.attackmagazine.com/technique/beat-dissected/21st-century-chicago-house/) |
| Deep tech house, 125–130 BPM | 60–65% | MPC-style | [Attack](https://www.attackmagazine.com/technique/beat-dissected/deep-tech-house/) |
| UK garage, 124–132 BPM | 68/69 | MPC16 | [Attack](https://www.attackmagazine.com/technique/beat-dissected/uk-garage/) |
| Rolling 2-step, 122–128 BPM | 60–65% | MPC-style | [Attack](https://www.attackmagazine.com/technique/beat-dissected/rolling-2-step-garage/) |
| Rolling techno, 131 BPM | 20% | DAW scale, not MPC | [Attack](https://www.attackmagazine.com/technique/beat-dissected/rolling-techno/) |
| 90s boom bap | 57% on 8ths (kick/snare); 74% on 16ths (hats) | MPC 3000 | [Attack](https://www.attackmagazine.com/technique/beat-dissected/90s-boom-bap-hip-hop/) |
| Lo-fi | 20–30% | FL quantise | [Audeobox](https://www.audeobox.com/learn/fl-studio/how-to-make-lofi-beats-in-fl-studio/) |
| R&B | 15–20% | FL quantise | [Audeobox](https://www.audeobox.com/learn/fl-studio/how-to-make-rnb-beats-in-fl-studio/) |
| Drums and 808 together | 8–15% | shared value | [Violet Recording](https://violetrecording.com/how-to-make-808-patterns/) |

Trap and drill hats are essentially straight; triplets are programmed explicitly (convention).

### Hi-hat programming is where trap and drill energy lives

Hats set the energy level (convention):
- **8ths** feel relaxed: boom bap, lo-fi, rock.
- **16ths** drive: R&B, house, trap verses.
- **Rolls and triplets** add excitement in trap and drill.

Sourced recipes:
- **Lo-fi:** 8th hats alternating 40–70% velocity ([Audeobox: Lo-fi](https://www.audeobox.com/learn/fl-studio/how-to-make-lofi-beats-in-fl-studio/)).
- **R&B:** 16ths at 70–80% on the 8ths and 30–50% in between ([Audeobox: R&B](https://www.audeobox.com/learn/fl-studio/how-to-make-rnb-beats-in-fl-studio/)).
- **Trap (Native Instruments):** 8th closed hats, with the bar-end hats turned into three-note 32nd rolls and the middle notes quieter ([Native Instruments: Trap](https://blog.native-instruments.com/how-to-make-a-trap-beat/)).
- **Trap mix:** hats high-passed around 500 Hz and sitting low ([Audeobox: Trap](https://www.audeobox.com/learn/fl-studio/how-to-make-trap-beats-in-fl-studio/)).
- **Drill (Native Instruments, 146 BPM):** hats on steps 1, 4, 7, 9, 12 and 15. The second hit of each 3-note group drops from velocity 100 to 87, and a ghost hat at velocity 52 sits on step 16 of bar 1 ([Native Instruments: Drill](https://blog.native-instruments.com/drill/)).
- **Drill hat feel:** start from 8ths, then delete hits and add triplet bursts before the snares ([eMastered](https://emastered.com/blog/how-to-make-a-drill-beat); [Beatstorapon](https://beatstorapon.com/blog/how-to-make-a-drill-beat/)).
- **House:** 16th closed hats with varying velocity, and open-hat length set "to ease into the clap without obscuring it" ([Attack](https://www.attackmagazine.com/technique/beat-dissected/21st-century-chicago-house/)).

Roll construction (convention):
- **Frequency and placement:** every 1–2 bars, replace one beat with a roll, on beat 4 heading into the next bar or on beat 2 heading into the snare.
- **Roll types:** 32nds (8 hits per beat), 16th triplets (6 per beat, snap 1/6) or 8th triplets (3 per beat).
- **Velocity shape:** a ramp from 60 to 110, or alternating 110/70.
- **Pitch:** optionally ramp up to +12 semitones, or apply small step Fine-pitch tilts.

Put the open and closed hats in the same FL cut group so the closed hat chokes the open one (FL feature, convention).

### Fills, phrase marks and build-ups follow a 4/8/16-bar schedule

The Amen break is the model 4-bar phrase ([Wikipedia: Amen break](https://en.wikipedia.org/wiki/Amen_break)):
- Bars 1–2: the main beat.
- Bar 3: a delayed snare.
- Bar 4: an empty beat 1, then syncopation and an early crash.

Two more sourced phrase marks:
- **Chicago house turnaround:** an extra reduced-velocity kick on the phrase's final offbeat ([Attack](https://www.attackmagazine.com/technique/beat-dissected/21st-century-chicago-house/)).
- **Drill:** the bar-2 snare moves relative to bar 1 ([Native Instruments](https://blog.native-instruments.com/drill/)).

The fill schedule (convention):
- Bar 4: a small variation.
- Bar 8: a bigger fill.
- Bar 16: a crash plus a full fill.

In hip hop, mute the kick for the last beat or half bar before the hook. The EDM build is an 8-bar rhythmic acceleration:
- Bars 1–4: snare on quarters.
- Bars 5–6: 8ths.
- Bar 7: 16ths.
- Bar 8: 32nds or 16th triplets.

The velocity ramps from 60 to 120, the drums are high-passed, and the last beat is empty before the drop.

## Bass and 808s work when one part owns the sub and every note names the chord

### Note choice: roots on changes, fifths and octaves as safe motion, approach tones on weak steps

The bass decides which chord the listener hears. In walking-bass practice, **the root and 5th are the most important notes**, and beats 1 and 3 should target them because chords usually change there ([The Jazz Piano Site](https://www.thejazzpianosite.com/?p=483)). A basic walking recipe plays the triad on beats 1–3, then a chromatic approach on beat 4, a half step above or below the next root ([TalkingBass](https://www.talkingbass.net/walking-bass-lines-made-easy/)). The bass is also the melodic foundation, while the kick is purely rhythmic ([iZotope](https://www.izotope.com/en/learn/7-tips-for-mixing-the-low-end)). Two more sourced rules:
- 808 lines should be built on the progression's roots, stay in key, and move mostly within one octave ([Violet Recording](https://violetrecording.com/how-to-make-808-patterns/)).
- Offbeat house basslines often support chord changes with only two notes ([Attack](https://www.attackmagazine.com/technique/tutorials/low-end-theory-exploring-eight-common-bassline-styles/)).

These become programmable rules (convention):
1. **Root on every chord change.** If the bass plays anything else, the chord becomes a slash or inversion chord.
2. **Stability ranking for other notes:** root, then octave (+12), then 5th (+7), then 4th or b7, then 3rd, then other scale tones, then chromatic tones.
3. **Octave bounce.** Alternating root and root+12 adds motion without adding harmony.
4. **Approach tone** on step 15 or 16 before a change. Use a chromatic, dominant or diatonic approach, and keep it short.
5. **Pedal tone** for drones and builds.
6. **No doubled low 3rds.** Pads should start at or above MIDI 48 when the bass is busy.
7. **Minor-pentatonic riff option.** In trap, drill and lo-fi, a riff built from 1, b3, 4, 5 and b7 can imply the chords loosely.

### Kick and bass: choose lock, gaps or hybrid, and tune them apart

The frequency facts come from Sonarworks ([Sonarworks](https://www.sonarworks.com/blog/learn/eliminate-competition-between-the-kick-and-bass)):
- An acoustic kick's fundamental sits at roughly **40–80 Hz**, with "thickness" around 70 Hz.
- Electric bass fundamentals reach almost 400 Hz.
- Tune the kick so its fundamental does not coincide with the bass roots of the key, then EQ the two in a complementary way. For example, boost the kick tightly at 50 Hz and cut gently at 100–250 Hz, then do the opposite on the bass.
- The kick's click lives at 3–5 kHz, and the bass gains audibility at 900 Hz–1.5 kHz.

The classic sidechain is a compressor on the bass keyed from the kick, with fast attack and a fast-to-moderate release ([Sonarworks](https://www.sonarworks.com/blog/learn/eliminate-competition-between-the-kick-and-bass)). **The short element should key the sustained one** ([iZotope](https://www.izotope.com/en/learn/7-tips-for-mixing-the-low-end)). A sidechained dynamic EQ at 40–80 Hz is the surgical alternative ([McDSP](https://mcdsp.com/2021/12/08/011-sidechain-kick-and-bass/)). The most contested bands are **40–60 Hz** and **70–100 Hz** ([iZotope](https://www.izotope.com/en/learn/7-tips-for-mixing-the-low-end)). For 808s, a sourced foundational move is to put a hit under each kick plus one or two syncopated notes in the gaps. Fewer notes sound bigger ([Violet Recording](https://violetrecording.com/how-to-make-808-patterns/)).

A skill should pick one of three strategies per section (convention):

| Strategy | How it works | Where it fits | Typical settings |
|---|---|---|---|
| **K1 Lock** | bass starts on the kick's steps | the 808 *is* the low end (trap, drill), or root 8ths in pop and rock | needs a short kick, ducking or layering |
| **K2 Gaps** | bass plays where the kick is silent | house offbeats 3/7/11/15, garage, amapiano log drum | little sidechain needed |
| **K3 Hybrid** | kick and bass share hits; the bass is ducked 50–150 ms | EDM, pop | ratio 4:1 or more, attack 0–5 ms, release 80–200 ms, back to full level by the next 8th |

Two long sub sources must never overlap on the same step without ducking. Their phase relationship changes on every hit and produces volume flutter (convention).

### 808 rules: tune it, keep it between about MIDI 24 and 40, slide sparingly, saturate for phones

Trap's bass drums are tuned with a long decay so they act as the bass, a technique that began with the Roland TR-808 ([Wikipedia: Trap](https://en.wikipedia.org/wiki/Trap_music)). An 808 is mostly sine energy, with a fundamental around **30–80 Hz** depending on the note ([Amped Studio](https://www.ampedstudio.com/blog/secrets-of-808-bass/), via search summary).

Raw 808 one-shots are often not tuned to a clean pitch, so check the sustained tail with a tuner and correct it until the root reads true ([Violet Recording: slides](https://violetrecording.com/how-to-make-808-slides/)). Most samples default to C ([Violet Recording: patterns](https://violetrecording.com/how-to-make-808-patterns/)). An out-of-tune 808 and uncontrolled sub energy are among the top reasons hip-hop mixes fall apart ([Violet Recording](https://violetrecording.com/how-to-make-808s-hit-harder/)).

The working register (convention, synthesised from the 30–80 Hz figure; no authoritative number exists):

| Zone | MIDI | Notes | Hz |
|---|---|---|---|
| Root window | 26–38 | D1–D2 | 37–73 |
| Hard floor | ≈24 | C1 | 32.7 |
| "Body" ceiling | ≈43–48 | — | 98–131 |

Pick the octave of the key root that lands in the window:
- F minor: F1 = 29 (43.7 Hz).
- G minor: G1 = 31 (49 Hz).
- C minor: C1 = 24 or C2 = 36, depending on the sample.

If the root sits awkwardly, keep the root and move riff notes below it rather than leaving the window.

**Slides and glides depend on FL-specific mechanics.** In Channel settings > Misc > Polyphony:
- **Mono** allows one voice, so overlapping notes transition smoothly.
- **Porta** makes every note slide from the previous one.
- The **Slide** knob sets the glide time.
- **Crucially, overlap portamento does not work for VST/AU instruments.** It only works for FL's native generators and samplers ([Image-Line: Channel Misc](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/chansettings_misc.htm)).

FL's piano roll also has **slide notes**, which glide the note below or above to the slide note's pitch. The slide note's length sets the slide time ([Image-Line: Piano roll](https://flstudio.image-line.com/help/html/pianoroll.htm)).

Audeobox's trap workflow puts these together ([Audeobox: Trap](https://www.audeobox.com/learn/fl-studio/how-to-make-trap-beats-in-fl-studio/)):
1. Enable Porta with Slide around 40, and set Mono.
2. Draw an overlapping second note and mark it as a Slide note.
3. Choose the overlap: 1/16 gives a tight slide, a full beat gives a slow bend.
4. Use an octave slide for the signature sweep.

Violet Recording adds usage guidance ([Violet Recording: slides](https://violetrecording.com/how-to-make-808-slides/)):
- Start with a short glide and lengthen it until audible.
- Use snappier glides at faster tempos.
- **1–2 semitone slides sound vocal; octave slides sound dramatic.**
- Upward slides build tension and downward slides resolve.
- Limit slides to **one or two per bar**, used as punctuation, with both notes in key.

Drill 808s have their own sourced conventions ([Audeobox: Drill](https://www.audeobox.com/learn/fl-studio/how-to-make-drill-beats-in-fl-studio/)):
- Most often in **C or G minor**.
- Slides of a **minor 3rd or perfect 4th**, mostly upward.
- **2–3 slides per 4-bar phrase**, with some notes sustaining a full beat.
- The signature move is a quick upward slide followed by a sustained low note.

**Translation to small speakers** depends on harmonics. A clean sub can vanish on a phone, but saturation adds upper harmonics that make the 808 line audible ([Beatstorapon](https://beatstorapon.com/blog/how-to-make-a-drill-beat-bpm-808s-drums/)). The ear infers a missing fundamental from its harmonic series ([Wikipedia: Missing fundamental](https://en.wikipedia.org/wiki/Missing_fundamental)). Small speakers roll off hard below about 150–200 Hz, so split the 808 into a clean sub layer and a saturated, high-passed layer ([Violet Recording](https://violetrecording.com/how-to-make-808s-hit-harder/)). For a 49 Hz root, the 2nd, 3rd and 4th harmonics sit at 98, 147 and 196 Hz (derived).

808 length and pattern defaults (convention):
- **Long, legato 808s** suit melodic trap and drill.
- **Short 808s** (an 8th or less, roughly 150–300 ms decay) suit bouncy hip hop, Memphis, Jersey club and rage.
- **Trap basic:** 808 on steps 1, 8 or 9, and 11, following the kick, with the last note sliding up an octave into the next bar.
- **Trap sparse:** 808 on 1, held about 1.5 beats; then 11 (the b7 or 5th); then 15 (an octave up-slide).
- **Drill:** 808 on 1, 4 (or 5), 8 and 11.
- **Boom bap:** bass on 1 and 8, short notes, roots and 5ths only.

There are three ways to layer kick and 808 (convention):
- **A:** a kick on every 808 start, high-passed at about 40–50 Hz.
- **B:** no kick; the 808's own transient serves as the kick.
- **C:** sidechain the 808 a few dB under a busy kick.

### Fifteen bassline styles reduce to where notes sit relative to the kick and how long they last

The sourced bass styles:
- **Offbeat bass** sits between four-on-the-floor kicks. It descends from disco and hi-NRG, uses a saw with a downward low-pass envelope sweep, and often alternates two notes ([Attack](https://www.attackmagazine.com/technique/tutorials/low-end-theory-exploring-eight-common-bassline-styles/)). It is one of the most-used patterns in tech house ([The Producer School](https://theproducerschool.com/blogs/featured-blogs/master-modern-tech-house-bass-lines-complete-tutorial-guide)).
- **Disco bass** relies on octaves, often an 8th followed by a 16th on the upper note ([TalkingBass](https://www.talkingbass.net/disco-bass-octaves/)).
- **Funk** ghost notes act like a second drum part ([TalkingBass](https://www.talkingbass.net/bass-technique-ghost-notes/)).
- **Reggae one drop** gets its character from avoiding beat 1 ([Soundfingers](https://soundfingers.com/techniques/authentic-reggae-dub-bass-tutorial/)).
- **The Reese** came from Kevin Saunderson's late-1980s "Reese" project. It is two detuned oscillators, commonly saws at about ±25 cents ([Wikipedia: DnB](https://en.wikipedia.org/wiki/Drum_and_bass); [eMastered](https://emastered.com/blog/reese-bass)).
- **Wobble** modulates the filter cutoff with a tempo-synced LFO ([Dubspot](https://blog.dubspot.com/video-tutorial-making-a-dubstep-bass-in-ableton-live)).
- **The amapiano log drum** is a hybrid of kick, 808, synth bass and percussion. It bounces between kicks rather than on them, with pitch variation ([Beatstorapon](https://beatstorapon.com/blog/how-to-make-amapiano-beat/); [RouteNote](https://create.routenote.com/blog/beatmakers-guide-how-to-make-an-amapiano-beat/)).

The step placements below are convention. R = root, O = octave, A = approach tone.

| Style | Steps and shape |
|---|---|
| Pop/rock root 8ths | R on odd steps, about 1.5 steps long |
| House offbeat | R on 3, 7, 11, 15 |
| Tech-house rolling | 2–4, 6–8, 10–12, 14–16, short, heavy sidechain |
| Disco octave | R / O / O per beat pair |
| Funk | R on 1, ghosts at velocity 20–40, b7 on 11, A on 16 |
| Motown walking | one note per beat |
| Reggae | rest on 1, phrase landing on 9, low-pass around 600–1000 Hz |
| UK garage | 1 (long), 4 or 7, 11, with portamento |
| DnB | long sine R plus reese on top; notes change every 1–2 bars |
| Dubstep | clean sub on 1 plus an LFO mid-bass at 1/4, 1/8, 1/8T or 1/16 |
| Amapiano log drum | 4, 7, 11, 14, 16 |
| Afrobeats | 1, 4 or 7, 11 |
| Synthwave | straight 8th or 16th R/O |
| Lo-fi | root–5th with 55–65% swing, low-pass around 800 Hz |

Sound design starting points (convention):
- **Sub:** sine, attack 0–5 ms, release 30–80 ms.
- **Pluck bass:** saw, low-pass at 200–400 Hz, filter-envelope decay 100–300 ms.
- **Layered bass:** a mono sine sub below about 100 Hz plus a mid layer high-passed at 100–150 Hz.
- **Synth 808:** sine with a +12 to +24 semitone pitch envelope over 20–60 ms, decay 0.5–3 s, then saturation.

The waveform roles are sourced: sine has only the fundamental, saw has all harmonics, and square has odd harmonics only ([Beat Kitchen](https://beatkitchen.io/guides/synthesist/02-oscillators/)).

## Arrangement makes sense when every part has a role, a register and a plane

### Five roles, three or four focal elements, three planes

Bobby Owsinski's framework names five arrangement elements ([Bobby Owsinski](https://bobbyowsinskiblog.com/song-arrangement-elements/)):
- **Foundation:** bass and drums.
- **Pad:** sustained notes or chords.
- **Rhythm:** parts that play counter to the foundation, such as shakers, strums and congas.
- **Lead.**
- **Fills:** answers placed in the lead's gaps.

Owsinski adds that **no more than four should play at once**. Three often works best, and five rarely does.

The "rule of three" says the brain can follow about three elements at once. A heard element can be several tracks: several drum tracks, or several guitars playing the same rhythm, count as one ([Music Factory](https://musicfactory.davejohnston.nz/p/less-is-more-using-the-rule-of-three?r=11vles)).

Orchestration teaching sorts sound into **foreground, middleground and background planes**. The foreground is louder, more characteristic in colour and prominently placed ([Andy Brick, Stevens](https://personal.stevens.edu/~abrick/orchestration2/files/HMU398_notes_02.html)). In melody-and-accompaniment textures, the melody sits in its best range, often at the top, and contrasts through timbre, register and rhythm ([Open Music Theory](https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_(Gotham_et_al.)/10%3A_Orchestration/10.01%3A_Core_Principles_of_Orchestration)).

Perception research supports the same placement. Pitch is encoded better for higher sounds and timing for lower ones, so the highest prominent voice is heard as the tune ([Hove et al. 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4104866)).

The rule for the skill (convention): **every new part gets a role and a plane before any notes are written.** If it would become a fifth foreground element, it must replace something or be pushed back, meaning lower in level, filtered, panned wider and less active.

### Frequency and register slotting is the physical reason instruments fit together

iZotope's cheat sheet gives starting ranges by instrument ([iZotope EQ cheat sheet](https://izotope.com/en/learn/eq-cheat-sheet)):
- **Kick:** low end 60–80 Hz, body 100–200 Hz, box 200–500 Hz, click 1–5 kHz.
- **Snare:** body 150–250 Hz, attack 2–3.5 kHz.
- **Hats:** 3–7 kHz.
- **Bass:** 40–120 Hz low end, 120–250 Hz body, 300–500 Hz mud, 800 Hz–1 kHz presence.
- **Vocals:** high-pass at 100–250 Hz, nasal 500 Hz–1.2 kHz, presence 5–8 kHz, air above 10 kHz.
- **Strings:** cut below 100 Hz, presence 1–4 kHz.
- **FX returns:** cut below 500 Hz.

Frequency charts show only fundamentals. Harmonics extend to the limit of hearing, which is how we tell instruments apart, so charts should be read cautiously ([Audio Masterclass](https://www.audiomasterclass.com/blog/what-frequencies-do-different-instruments-produce)).

Masking is an arrangement problem first and a mix problem second. Sonarworks calls low parts getting in each other's way "a fundamental arranging mistake" that no plug-in fully fixes ([Sonarworks](https://www.sonarworks.com/blog/learn/eliminate-competition-between-the-kick-and-bass)). Plomp and Levelt's critical band is the underlying unit: sounds with dominant energy in the same band interact strongly ([Plomp & Levelt](https://www.math.miami.edu/~armstrong/592sp15/Plomp_Levelt_1965.pdf)).

The register map below is derived from frequency math. It is not a cited chart.

| Zone | Fundamentals | MIDI (scientific) | FL label | Occupants |
|---|---|---|---|---|
| Sub | 30–60 Hz | 23–34 | B1–A#2 | 808/sub fundamentals, kick body |
| Bass | 60–130 Hz | 35–48 | B2–C4 | basslines, upper 808, kick punch |
| Low-mid | 130–260 Hz | 48–60 | C4–C5 | chord roots and 5ths, piano left hand |
| Mid | 260 Hz–1 kHz | 60–83 | C5–B6 | pads, chords, vocals, most leads |
| Upper-mid | 1–4 kHz | 84–107 | C7–B8 | bell tops, plucks, arps, presence harmonics |
| High | 4 kHz+ | harmonics and noise | — | hats, shakers, cymbals, air |

Eight slotting rules follow (convention):
1. **One owner below about 100 Hz** at any moment.
2. **Bass and 808** at roughly MIDI 28–47.
3. **No chords below MIDI 48**, except root, octave or 5th.
4. **Pads and chords** mostly at MIDI 48–76.
5. **Lead** above the chord bed at about MIDI 60–84, or contrasting with it in timbre.
6. **Counter-melody** in a different octave, played in the lead's rests.
7. **Busy needs sustained.** A busy part needs a sustained or sparse neighbour in the same register.
8. **Shared registers must contrast** in timbre (soft pad versus bright pluck) or in stereo (wide pad versus centred lead).

### Orchestration's lessons: double for weight, but not constantly; crescendo by adding families

Alan Belkin warns against both extremes: independent counterpoint everywhere tires the ear, and heavy doubling sounds "grey". Composers sketch clear leading lines first, and most of the time only part of the orchestra plays ([Alan Belkin](https://alanbelkinmusic.com/orchestration-basic-notions-pt-2/)).

A crescendo is built in three ways ([Open Music Theory](https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_(Gotham_et_al.)/10%3A_Orchestration/10.01%3A_Core_Principles_of_Orchestration)):
- add instrument families (strings, then winds, then brass, then percussion);
- widen the total range;
- mix sustained notes with short figures.

Film scoring builds tension from a quiet ostinato with layers added gradually ([IRPR glossary](https://sounddesign.irpr.agency/glossary/ostinato/)).

In production terms (convention):
- **Octave-double the hook** in choruses and drops (for example a lead at 72 plus 60 or 84), and remove the double in verses.
- **Spread the chord across instruments.** The bass takes the root, the pad the 3rd, 7th and extensions in the middle, and the keys the upper voicing. Never double the 3rd in low parts.
- **Build in stages.** Add a family, then a sub octave and a top octave, then shorter note values (8ths, 16ths, 32nd rolls) over sustains.

### Sections come in 4/8/16-bar blocks, with sourced templates per genre

Electronic arrangements move in **multiples of 8 bars**, and 7- or 9-bar deviations work only as a deliberate effect ([Inspired by Beatz](https://www.inspiredbybeatz.com/en/edm-arrangement-from-loop-to-exciting-track/)). Dance tunes progress in 16-bar sections, with elements changing every 4 or 8 bars ([Wikipedia: Phrasing (DJ)](https://en.wikipedia.org/wiki/Phrasing_(DJ))). Intros are kick plus percussion so DJs can beatmatch, and outros mirror them ([Home DJ Studio](https://homedjstudio.com/edm-song-structure/)). Mixed In Key deliberately treats 8- and 16-bar phrases as starting points, not mandatory lengths ([Mixed In Key](https://mixedinkey.com/?p=5367)).

| Genre | Sourced section lengths | Source |
|---|---|---|
| EDM | Intro 16–32, Build 8–16, Drop 16–32, Breakdown 16–32, Outro 16–32; 6–8 sections; streaming drop within 30–60 s; radio edit 3.5–4 min; club 5–7 min | [Inspired by Beatz](https://www.inspiredbybeatz.com/en/edm-arrangement-from-loop-to-exciting-track/) |
| Hip hop | Verse 16 (simpler beat), Hook 8 (most elements), Bridge 8; Intro-V-H-V-H-V-H-Outro; R&B adds a bridge | [HipHopMakers](https://hiphopmakers.com/how-to-make-beats-song-arrangements) |
| Drill | Intro 1–8, Hook 9–16, Verse 17–32, Hook 33–40, Verse 41–56, Bridge 57–64, Hook 65–72, Outro 73–80; change something every 4 or 8 bars | [Beatstorapon](https://beatstorapon.com/blog/how-to-make-a-drill-beat/) |
| Trap | Intro 8, Verse 16, Hook 16 with a bigger 808 (snippet only) | [WA Production](https://blog.waproduction.com/arrangement-blueprints-10-proven-song-maps-that-just-work) |
| Afrobeats | Intro 4–8, Verse 16, Hook 8, Bridge 8 | [Audeobox](https://www.audeobox.com/learn/fl-studio/how-to-make-afrobeats-in-fl-studio/) |
| Amapiano | Intro 8–16, Foundation 16, Development 16–32, Breakdown 8–16, Outro 8–16 | [Beatstorapon](https://beatstorapon.com/blog/how-to-make-amapiano-beat/) |
| Jersey club | elements layer in every 8 bars; lead drops at bar 41 and returns at 49 | [Native Instruments](https://blog.native-instruments.com/jersey-club/) |
| Lo-fi | 4-bar sections looped; 64–96 bars total | [Lunacy Audio](https://lunacy.audio/how-to-make-lofi-music/) (search summary) |
| DnB | Intro 16, Build 8, Drop 1 32, Breakdown 16, Drop 2 32, Outro 8–16; drop at ~1:00 | [Violet Recording](https://violetrecording.com/how-to-make-drum-and-bass/); [Beatportal](https://www.beatportal.com/articles/818379-step-by-step-guide-to-producing-drum-and-bass-like-sub-focus-a-m-c-and-delta-heavy) |
| Trailer | Act 1 quiet, Act 2 builds, Act 3 full climax, ending on a button or stinger | [Violet Recording](https://violetrecording.com/sound-design-for-trailers/) |

Pop length and timing figures are softer than they look:
- **Song length.** The **2025 Billboard Year-End Hot 100 median hit runs 3:13** (mean 3:24). The share of hits over 3:30 rose from 22% in 2019 to 37% in 2025 ([DEV Community analysis](https://dev.to/tonywangca/are-songs-really-getting-shorter-6618-hot-100-hits-1959-2025-4cdg)). Spotify-charting songs averaged about 3:00 in 2024 ([Hypebot](https://www.hypebot.com/hypebot/2025/04/songs-are-getting-shorter-and-the-surprising-truth-behind-it.html)). The two figures measure different populations.
- **First chorus.** Hot 100 number-ones in 2020–2023 reportedly reached the first chorus at about **38 s**, versus 55 s or more in earlier decades, and ABABCB appears in 67% of number-one pop hits. These figures came through an aggregator and were not verified on the primary reports ([Hit Songs Deconstructed PDF](https://hitsongsdeconstructed.com/wp-content/uploads/2024/04/The-Taylor-Swift-Evolution-Structure.pdf); [djwillgill aggregator](https://djwillgill.com/how-to-write-band-music-in-2026/)).

### Energy and tension are separate controls, and drops only hit after a clearing

EDMProd distinguishes two controls ([EDMProd](https://edmprod.com/tension)):
- **Tension** is the expectation of release.
- **Energy** is intensity and momentum. A steady four-on-the-floor kick has energy but little tension.

Tension works at two scales:
- **Macro:** risers, 4–8-bar snare rolls, filter automation, pitched risers rising 5–24 semitones.
- **Micro:** short fills, kick removals, reverse crashes, one-bar breaks.

EDMProd's method is to rate each section of a reference track from 1 to 9 and draw an energy curve before arranging. Its worked example ends a build with **one bar of silence before the drop**.

For reverse crashes, reverse a copy of the crash, end it slightly before the real hit, keep it quieter, and add reverb before reversing for a better swell ([EDMProd](https://edmprod.com/tension)).

Energy is relative. **A drop only hits if the breakdown before it cleared space**, and the classic mistakes are everything playing at once, no breakdown, and a second drop identical to the first ([Inspired by Beatz](https://www.inspiredbybeatz.com/en/edm-arrangement-from-loop-to-exciting-track/)). Mixed In Key advises saving the strongest transition signal for the biggest change and not repeating the same fill at every boundary ([Mixed In Key](https://mixedinkey.com/?p=5367)).

Default energy curves on the 1–9 scale (convention):

| Genre | Section-by-section curve |
|---|---|
| Pop | Intro 3, Verse 4, Pre 5, Chorus 7, Verse 5, Pre 6, Chorus 8, Bridge 4–5, Final Chorus 9, Outro 3 |
| EDM | Intro 3, Break 4, Build 5→7, Drop 9, Breakdown 3, Build 5→8, Drop 9, Outro 3 |
| Trap | Intro 3, Hook 8, Verse 6, Hook 8, Verse 6–7, Bridge 4, Hook 9, Outro 3 |

Adjacent sections should differ on at least two of these six axes (convention):
- element count;
- low-end presence;
- hat subdivision;
- register span;
- stereo width;
- lead type.

### Turning a loop into a song is mostly subtraction

The dominant workflow builds the densest section first. Duplicate it, strip drums for the breakdown, then strip further for the intro, because "subtraction is faster than addition" ([Inspired by Beatz](https://www.inspiredbybeatz.com/en/edm-arrangement-from-loop-to-exciting-track/); [Mixed In Key](https://mixedinkey.com/?p=5367)). Attack Magazine lists four ways out of the loop ([Attack Magazine](https://www.attackmagazine.com/technique/tutorials/4-ways-to-break-out-of-the-loop/)):
- **Jam it out live.**
- **Copy a reference track's decisions.** When it adds a kick, you add one.
- **Add an element every 8–16 bars, then subtract toward the end.**
- **Place section markers as scaffolding.**

The full workflow for FL (convention):
1. Build the full 8-bar loop as separate patterns per role:
   - kick;
   - snare/clap;
   - hats;
   - perc;
   - 808;
   - chords;
   - lead;
   - counter;
   - FX.
2. Compute the section bars from the genre template and place playlist markers.
3. Paste the full loop into every peak section.
4. Subtract to make the other sections:
   - **Intro:** 1–2 elements.
   - **Verse:** no lead layer, simpler hats.
   - **Breakdown:** no kick or bass.
5. Make "B" variants of each pattern:
   - hat rolls;
   - 808 slides;
   - chord inversions;
   - melody tails.

   No 8-bar block should repeat more than twice in a row.
6. At every 8-bar boundary, something enters, leaves or changes. At every 4-bar end, add a micro-variation.
7. Insert transitions at the boundaries: risers, crashes, reverse cymbals, a beat to a bar of silence before the biggest hit, and downlifters.
8. Automate filters, sends and pans so repeats evolve.
9. Verify there are 3–4 focal elements and one low-end owner in every section.

A trap element matrix shows the result (convention):

| Section (bars) | Kick | 808 | Snare | Hats | Perc | Chords | Lead | Counter | FX |
|---|---|---|---|---|---|---|---|---|---|
| Intro (8) | – | – | – | filtered | – | filtered | filtered | – | riser |
| Hook (8) | X | X | X | rolls | X | X | X | X | crash on 1 |
| Verse 1 (16) | X | X | X | simpler | partial | X | – | fills at bars 8/16 | drop-out on bar 16 |
| Hook (8) | X | X | X | X | X | X | X | X | reverse cymbal |
| Verse 2 (16) | X | new pattern | X | variation | new | X | partial | X | – |
| Bridge (8) | – | partial | – | partial | – | X | X | – | silence and impact |
| Hook (8) | X | X | X | X | X | X | + octave layer | X | – |
| Outro (8) | – | – | – | – | – | fading | partial | – | downlifter |

## Mixing a beat means gain staging near −18 dBFS, carving lanes, and mastering to the platform

### Gain staging and the static mix come first

Gain staging has three sourced reference points:
- **Track level.** Many analog-modelled plugins are designed for input around **−18 to −12 dBFS** and distort when fed near 0 dBFS ([Boris FX](https://borisfx.com/blog/gain-staging-cheat-sheet/)). A common practice is an average near −18 dBFS with peaks between −12 and −6 dBFS ([Imagineer](https://blog.imagineersystems.com/blog/gain-staging-cheat-sheet/)).
- **Mix print.** Many mastering services ask for about **−6 dB of peak headroom** and no processing on the master bus ([Studio 11 Chicago](https://mastering.studio11chicago.com/mastering-6db/)).
- **Kick anchor.** In kick- and bass-driven music, one forum-derived convention sets the kick peaking around −6 dBFS and mixes everything else around it ([Studio 11 Chicago](https://mastering.studio11chicago.com/mastering-6db/)).

The static mix uses only faders, pan and polarity. Start from the densest section, bring up the primary group first, and aim to finish in about five minutes. One iZotope author targets about −20 LUFS for the mix to protect mastering headroom ([iZotope](https://www.izotope.com/en/learn/7-tips-for-a-balanced-static-mix.html)). In hip hop and electronic music, the **kick and snare are the usual anchors** ([Violet Recording](https://violetrecording.com/how-to-balance-levels-in-a-mix/)).

Two monitoring checks round this out:
- Monitor at **75–85 dB SPL** ([Sweetwater](https://www.sweetwater.com/insync/monitor-volume-2/)).
- Check at very low volume, where anything too loud jumps out ([Violet Recording](https://violetrecording.com/how-to-mix-at-low-volume/)).

The typical trap loudness order runs from kick and 808 (trading off), to snare/clap, to vocal or lead, to the music bed, to hats, percussion and FX (convention; no source gave dB offsets). FL's mixer meters show sample peak, so use a loudness meter for LUFS.

### EQ regions and lanes

iZotope's region map ([iZotope EQ cheat sheet](https://www.izotope.com/en/learn/eq-cheat-sheet.html)):

| Region | Range | Character |
|---|---|---|
| Sub | 20–60 Hz | foundation |
| Bass | 40–250 Hz | body |
| Low-mids | 200–500 Hz | box and mud |
| Mids | 500 Hz–2 kHz | presence, nasal |
| Presence | 2–8 kHz | clarity, harshness |
| Air | 8–12 kHz+ | sparkle |

Other sources draw the boundaries slightly differently. Mastering.com and Audient put mud and fullness at 250–450 Hz and presence at 4–6 kHz ([Mastering.com](https://mastering.com/how-to-use-eq); [Audient](https://audient.com/tutorial/frequency-ranges-explained/)). The general rule is to **cut before boosting and high-pass anything that does not need low end** ([iZotope](https://www.izotope.com/en/learn/eq-cheat-sheet.html)).

For kick against 808, give the kick a slightly higher punch frequency and let the 808 own the deep sub, or notch the 808 where the kick lives ([Violet Recording: mix 808s](https://violetrecording.com/how-to-mix-808s/)).

Starting high-pass points and moves (convention; confirm in context):
- **High-pass filters:**
  - hats and cymbals: 200–400 Hz;
  - pads, keys and leads: 100–200 Hz;
  - snare/clap: 80–100 Hz;
  - vocals: 80–150 Hz.
- **Complementary dip:** cut pads 2–4 dB at 1–4 kHz to make room for the lead.
- **Q settings:** wide-Q boosts of 1–3 dB; narrow cuts for resonances.

### Compression and sidechain in FL Studio

Sourced starting settings:
- **Kick:** attack 10–20 ms, ratio 4:1 (up to 6–8:1).
- **Snare:** attack 20–30 ms to emphasise the crack ([Music Guy Mixing](https://www.musicguymixing.com/?p=3896)).
- **Group bus glue:** about 2:1 with 2–5 dB of gain reduction, slow attack ([Mastering.com cheat sheet](https://mastering.com/wp-content/uploads/2017/07/COMPRESSION-CHEAT-SHEET.pdf)).
- **Parallel compression** on the drum bus adds impact without audible cymbal pumping ([Scraps Audio](https://scrapsaudio.com/blogs/scraps-blog/mastering-drum-compression-your-complete-guide)).
- **808 compression:** a slower attack passes the transient, while very fast settings react to individual waveform cycles and distort ([Violet Recording](https://violetrecording.com/how-to-mix-808s/)).
- **808 sidechain:** fast attack, with release set so the 808 recovers before its next note ([Violet Recording](https://violetrecording.com/how-to-mix-808s/)).

FL's tools are documented in the manual:
- **Fruity Limiter** has LIMIT, COMP and NOISE GATE modes ([Image-Line: Fruity Limiter](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Limiter.htm)):
  - 0 ms attack is recommended to avoid latency issues, unless Plugin Delay Compensation is on.
  - Releases that are too short distort.
  - CEIL at +12 dB effectively bypasses the limiter stage.
- **Fruity Limiter sidechain setup** ([Image-Line](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Limiter.htm); [Mixelite](https://mixelite.com/blog/top-3-ways-to-sidechain-in-fl-studio/)):
  1. Select the kick's mixer track.
  2. Right-click the destination track's send arrow and choose "Sidechain to this track".
  3. On the COMP tab, set SIDECHAIN to the kick's track.
  4. Lower the threshold and raise the ratio.
- **Starting ratio:** about 2.5:1 ([Slooply](https://slooply.com/blog/how-to-sidechain-kick-and-bass-in-fl-studio-fruity-limiter-method/)).
- **Fruity Peak Controller** is an alternative for ducking. It works as volume automation, with Volume set negative (range −200% to +200%), Decay setting the return time and Tension the curve ([Image-Line: Peak Controller](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Peak%20Controller.htm)).

Starting presets for the skill (convention):

| Use | Settings |
|---|---|
| Kick → 808 duck | 2.5–4:1, attack 0–1 ms, release 50–150 ms, 3–6 dB GR |
| Pumping pads | 6–10 dB GR, release ≈ one 8th (`30000/BPM` ms) |
| Drum glue | 2:1, attack 10–30 ms, 2–3 dB GR |
| Parallel bus | 6–10:1, 8–12 dB GR, blended under the dry drums |

### Stereo, space and saturation

**Keep the sub mono and centred** ([Violet Recording](https://violetrecording.com/how-to-mix-808s/)). Bass below roughly 100–120 Hz should stay mono, with width only above a 100–150 Hz split ([Future Proof](https://futureproofmusicschool.com/blog/how-do-i-preserve-mono-low-end-while-adding-stereo-width-to-highs); [Mastering The Mix](https://www.masteringthemix.com/blogs/learn/how-to-add-width-to-bass-without-losing-mono-compatibility)). When widening with M/S or short delays, high-pass the side signal at 100–150 Hz. **Haas delays of about 1–30 ms sound wide but are often not mono-compatible** ([Sound On Sound](https://www.soundonsound.com/sound-advice/q-how-can-create-fake-ms-setup-mono-compatible); [eMastered](https://emastered.com/blog/haas-effect)).

Pan defaults (convention):
- **Centre:** kick, snare, 808, lead and vocal.
- **Hats:** 10–30% off centre, with the open hat opposite.
- **Percussion:** 20–50%, alternating sides.
- **Doubles:** 50–100%.

Reverb and delay timing is pure tempo math: **a quarter note lasts 60000/BPM ms** ([Omni Calculator](https://www.omnicalculator.com/other/delay-reverb-times)). Pre-delay of about 1/64 to 1/16 of a note keeps transients clear. Decay can end by the next beat for a tight sound or the next bar for a lush one ([Violet Recording](https://violetrecording.com/tools/reverb-calculator/)).

Fruity Reeverb 2 should sit on a send track with **Dry at 0% and Wet at 100%**. Drums want shorter decays, and reverb should not go on the master ([Image-Line: Reeverb 2](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Reeverb%202.htm)). Fruity Delay 3 offers tempo sync, ping-pong, per-echo filters and modulation up to 20 Hz ([Image-Line: Delay 3](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Delay%203.htm)).

Note lengths in milliseconds (derived):

| BPM | 1/4 | 1/8 | dotted 1/8 | 1/8T | 1/16 | 1/32 |
|---|---|---|---|---|---|---|
| 70 | 857 | 429 | 643 | 286 | 214 | 107 |
| 90 | 667 | 333 | 500 | 222 | 167 | 83 |
| 120 | 500 | 250 | 375 | 167 | 125 | 63 |
| 140 | 429 | 214 | 321 | 143 | 107 | 54 |
| 160 | 375 | 188 | 281 | 125 | 94 | 47 |

Reverb types by role (convention):

| Type | Decay | Pre-delay | Use |
|---|---|---|---|
| Room | 0.3–0.8 s | — | drums |
| Plate | 1–2 s | 20–40 ms | snare, vocals, leads |
| Hall | 2–4 s | — | pads, FX |

High-pass reverb returns at 200–400 Hz and low-pass them at 6–10 kHz.

For saturation, Fruity Limiter has a SAT control and Maximus includes per-band saturation ([Image-Line: Maximus](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Maximus.htm)). **An 808 whose notes vary by about 6 dB will repeatedly hit the limiter and duck the whole track**, so control sub energy before mastering ([Violet Recording: master hip hop](https://violetrecording.com/how-to-master-hip-hop/)).

### Mastering targets follow the platforms

Platform loudness targets:
- **Spotify** normalises to **−14 LUFS integrated** and recommends a true peak below −1 dBTP, or below −2 dBTP for masters louder than −14 LUFS ([Spotify for Artists](https://support.spotify.com/artists/article/loudness-normalization/)).
- **AES TD1008** recommends −16 LUFS for music, with peaks no higher than −1 dBTP ([Production Advice](https://productionadvice.co.uk/td1008/)).
- **Apple Music** Sound Check uses −16 LUFS ([Production Expert](https://www.production-expert.com/production-expert-1/apple-choose-16lufs-loudness-level-for-apple-music-heres-why?format=amp)).
- **YouTube** uses −14 LUFS and turns loud tracks down but does not raise quiet ones ([Mastering The Mix](https://masteringthemix.com/blogs/learn/76296773-mastering-audio-for-soundcloud-itunes-spotify-and-youtube)).

Competitive hip-hop masters still often land around **−8 to −10 LUFS** ([Violet Recording](https://violetrecording.com/how-to-master-hip-hop/)), and normalisation will turn them down.

FL's mastering tools ([Image-Line: Maximus](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Maximus.htm); [Image-Line: Soundgoodizer](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Soundgoodizer.htm)):
- **Maximus** is a three-band maximiser designed as the master's last effect. Its manual warns against over-compression.
- **Soundgoodizer** runs on the Maximus engine with four presets and one amount knob.

A controllable master chain for a skill (convention):
1. Optional gentle Parametric EQ 2.
2. Glue at 1.5–2:1 with 1–2 dB of gain reduction.
3. Limiter with the ceiling at −1 to −1.5 dB. Fruity Limiter is not a true-peak limiter, so leave the margin.
4. Loudness meter.
5. Target −14 LUFS for streaming-safe masters, or −10 to −8 LUFS for competitive beat leases.

The routing template (convention):
- **Inserts:** one per channel (kick, 808, snare, hats, percs, lead, chords, vocal).
- **Buses:** Drums, Music and Vocal, feeding the master.
- **Sends:** short verb, long verb, and a dotted-8th delay.
- **Sidechain:** the kick is set as a sidechain-only source to the 808 and the music bus.

The mix-check heuristics a skill should flag (convention):
- any track peaking above −3 dBFS;
- the master above −3 dBFS before the limiter;
- kick, 808 or bass panned off centre;
- hats louder than the snare;
- reverb inserted at 100% wet instead of on a send;
- stereo wideners on bass;
- Soundgoodizer slammed during mixing;
- more than about three elements dominating 1–5 kHz.

## Genre recipes are parameter vectors over the same theory

The genre research shows that most styles are separated less by music theory than by a short list of parameters:
- kick placement: four-on-the-floor, broken or half-time;
- the snare's position;
- swing;
- the bass's job;
- chord vocabulary;
- arrangement shape.

The tables give each genre's parameter card. The grids that follow use `X` for an accent (velocity about 100–127), `x` for a normal hit (75–100), `g` for a ghost (30–60), `o` for an open hat and `r` for a roll, with steps grouped `|1-4|5-8|9-12|13-16|`. Grids are researcher derivations from the cited descriptions plus convention, unless a specific step placement is attributed to a source.

### Hip hop, urban and global styles

| Genre | BPM (default) | Snare | Swing | Harmony and scale | Bass / 808 | Signature | Key sources |
|---|---|---|---|---|---|---|---|
| Trap | 130–160 (140); NI notes 130–200 | beat 3 (half-time) | straight; explicit triplets | natural/harmonic minor, Phrygian; 2–4-chord minor loops | long 808 following the kick, slides, saturated | 8th hats with 32nd and triplet rolls; clap decay ~280 ms; counter-melody from root, octave, 5th and m7 | [Wikipedia](https://en.wikipedia.org/wiki/Trap_music); [NI](https://blog.native-instruments.com/how-to-make-a-trap-beat/) |
| UK drill | 138–151 (142–144) | bar 1 beat 3; bar 2 beat 4 | swung, "skippy" | dark minor, b2; 2–4-note cold motifs | sliding 808 carries the melody | 3+3+2 hats with hand-edited gaps | [Wikipedia: UK drill](https://en.wikipedia.org/wiki/UK_drill); [NI](https://blog.native-instruments.com/drill/) |
| NY/Brooklyn drill | 140–150 | same skeleton | less swing | simpler minor triads | heavier, longer glides | punchier, hook-forward | [Beatstorapon](https://beatstorapon.com/blog/how-to-make-a-drill-beat/); [Orphiq](https://orphiq.com/resources/drill-chords) |
| Chicago drill | 60–75 feel (130–145 grid) | trap-like | — | minor | sustained, static 808 | heavy, direct | [Beatstorapon](https://beatstorapon.com/blog/how-to-make-a-drill-beat/) |
| Plugg / pluggnb | 130–150 half-time | beat 3, soft clap | — | warm 2–3-chord minor; pluggnb uses EP block chords with m7/add9 and close inversions | clean, sine-like | sine leads, glassy bells, gospel chops | [Reason](https://www.reasonstudios.com/news/post/how-to-make-plugg-beats); [Splice](https://splice.com/blog/what-is-pluggnb/) |
| Rage | 140–170 (≈150–160) | beat 3 | — | minor | distorted, clipped | short looping stereo-wide future-bass synth leads, game-music feel | [Wikipedia: Rage](https://en.wikipedia.org/wiki/Rage_rap); [musicproductionwiki](https://musicproductionwiki.com/articles/how-to-make-rage-beats) (low authority) |
| Boom bap | 85–95 (88–94) | 2 & 4 | MPC 57% kick/snare, 74% hats | sample key; minor/Dorian jazz-soul | simple roots doubling the kick | chopped vinyl, layered kicks, clap nudged late | [Attack](https://www.attackmagazine.com/technique/beat-dissected/90s-boom-bap-hip-hop/); [Audeobox](https://www.audeobox.com/learn/fl-studio/how-to-make-boom-bap-beats-in-fl-studio/) |
| Lo-fi | 60–90 (70–85) | 2 & 4, soft and late | loose; FL 20–30% | maj7/m7/9; ii–V–I; VI–i–V7 | sparse, low-passed | low-pass ~3.12 kHz, vinyl, bitcrush | [NI: Lo-fi](https://blog.native-instruments.com/lo-fi-hip-hop/) |
| Modern R&B | 60–90 (120–140 half-time) | 2 & 4 or 3 | swung, with ghosts | 7th–13th chords | 808 tuned to chord roots, smooth glides | Rhodes, pitched vocal chops | [Violet Recording](https://violetrecording.com/how-to-make-rnb-beats/) |
| Afrobeats | 95–115 (108) | soft 2 & 4 | gentle 16th swing | C/G/F/D major triads | round bass, C1–E2 roots | 16th shaker, 3-2 clave, congas, muted guitar | [Audeobox](https://www.audeobox.com/learn/fl-studio/how-to-make-afrobeats-in-fl-studio/) |
| Amapiano | 108–115 (112) | rim 2 & 4 | swung shakers | m9/maj7/6-9 jazz ii–V–I | log drum (no log drum, no amapiano) | offbeat open hat, constant 16th shaker | [Splice](https://splice.com/blog/what-is-amapiano-music/); [Roland](https://articles.roland.com/?p=67237) |
| Reggaeton | 85–100 (92–96) | 3+3+2 dembow | — | minor i–VI–III–VII | sustained sub on roots, sidechained | "boom-ch-boom-chick" | [Wikipedia: Dembow](https://en.wikipedia.org/wiki/Dembow_beat); [Orphiq](https://orphiq.com/resources/what-is-reggaeton) |
| Dominican dembow | 115–130 | dembow | — | loop-based | heavy, distorted | rapid chant vocals | [Orphiq](https://orphiq.com/resources/what-is-dembow) |
| Phonk | drift 130–160; Brazilian 130–150 | 2 & 4 or 3 | — | minor/Phrygian | distorted 808 | TR-808 cowbell melodies, Memphis chops | [Wikipedia: Phonk](https://en.wikipedia.org/wiki/Phonk); [tunee.ai](https://www.tunee.ai/music-generator/phonk) (low authority) |
| Jersey club | 130–145 (140) | 9, 12 (+11) | straight | chopped hooks | short envelopes, mono sub | five-kick run, bed squeak | [NI](https://blog.native-instruments.com/jersey-club/); [Beatstorapon](https://beatstorapon.com/blog/how-to-make-a-jersey-club-beat/) |
| West Coast ratchet / Detroit | ratchet ≈95–105; Detroit ≈165–190 (estimates) | 2 & 4 | — | — | thumping 808 | ratchet: clap flurries, a reverberated "hey"; Detroit: "murderous" piano loops | [Wikipedia: Mustard](https://en.wikipedia.org/wiki/Mustard_(music_producer)); [Okayplayer](https://www.okayplayer.com/originals/helluva-interview-sada-baby-tee-grizzly-first-day-out-producer.html) |

A few distinctions matter most when choosing between close relatives:
- **Trap versus drill.** Both run around 140 BPM in half-time. Trap's snare stays on beat 3 every bar, its hats run on a straight grid with rolls, and slides are optional. Drill moves the bar-2 snare to beat 4, groups hats 3+3+2 with gaps, and its 808 slides carry the melody ([Wikipedia: UK drill](https://en.wikipedia.org/wiki/UK_drill)).
- **Afrobeats versus amapiano.** Afrobeats uses a syncopated kick that avoids four-on-the-floor. Amapiano keeps a restrained house pulse under the log-drum hook.
- **Dembow family.** Reggaeton, Dominican dembow and afro styles all use 3+3+2.

```
TRAP 140 (half-time) — snare on 3; 808 starts on kicks
Kick   |X...|...x|..x.|....|   bar 2 variant: 1, 4, 11, 15
Snare  |....|....|X...|....|   + ghost on step 16 (~55) in bar 2
Hat    |x.x.|x.x.|x.x.|x.rr|   8ths 100/75; 1/32 or 1/16T roll into the bar end
OpHat  occasional on step 7 or 15

UK DRILL 142-146 — Native Instruments 2-bar pattern
Bar 1 Kick  |X...|...x|....|....|   (1, 8)
      Snare |....|....|X...|....|   (9)
      Hat   |x..x|..x.|x..x|..xg|   vel 100,87,100 | 100,87,100 | g = 52
Bar 2 Kick  |X..x|..x.|....|..x.|   (1, 4, 7, 15; step 15 vel 96)
      Snare |....|....|....|X...|   (13 = beat 4)
      Hat   |x..x|..x.|x..x|..x.|
808: follows kicks, 2-3 upward slides of a m3/P4 per 4 bars, C or G minor

BOOM BAP 90 — MPC swing ~57% (kick/snare), hats heavier
Kick   |X...|..x.|x...|..xg|   1, "&2", 3, "&4" (+ ghost kick 16)
Snare  |....|X...|....|X...|   clap layer nudged a few ms late
Hat    |x.x.|x.x.|x.x.|x.x.|   95/70 (or 16ths with ghosts)
Bar 2: cowbell on beat 1, open hat on beat 4 (Attack)

LO-FI 78 — swing ~58-64% MPC / 20-30% FL
Kick   |X...|....|..x.|....|
Snare  |....|X...|....|X...|   +3-8% late (Shift)
Hat    |x.x.|x.x.|x.x.|x.x.|   alternate ~89 / ~51

R&B 60-100
Kick   |X...|....|.x..|....|
Snare  |....|X...|....|X...|   + rim ghosts ~40
Hat    |xxxx|xxox|xxxx|xxxx|   8ths 89-102; between 38-64; open on 7 ~83

PLUGG 140-150 (half-time)
Kick   |X...|....|..x.|..x.|
Clap   |....|....|X...|....|
Hat    |x.x.|x.x.|x.x.|x.x.|   occasional triplet roll; open hat on 7

AFROBEATS 108 — Audeobox
Kick   |X...|..x.|x...|..x.|   1, "&2", 3 (vel 75-85), "&4" on alternate bars
Rim/Cl |....|x...|....|xg..|   2 & 4; 40% ghost on step 14 every other bar
Hat    |x.g.|x.g.|x.g.|x.g.|   70-80% down / 50-60% up
OpHat  |....|..o.|....|....|   "&2", choked
Shaker |xgxg|xgxg|xgxg|xgxg|   16ths, velocity cycle 60-40-70-40%
Clave  |x.x.|..x.|....|x.x.|   3-2: 1, 3, 7, 13, 15 (80-90%)

AMAPIANO 112 — Roland example 1 + convention
Kick   |X...|X...|X...|X...|   restrained 4-floor (modern: sparser, syncopated)
Rim    |....|x...|....|x...|
OpHat  |..o.|..o.|..o.|..o.|   third 16th of each beat (Roland)
Shaker |xgxg|xgxg|xgxg|xgxg|   constant, swung
Conga  |....|x..x|..x.|x...|   beat 2, "a" of 2, "&" of 3, beat 4 (Roland)
LogDrm |...x|..x.|..x.|.x.x|   between kicks, pitch-glide, 2-bar call/answer (convention; placements vary)

REGGAETON 94 — dembow
Kick   |X...|X...|X...|X...|
Snare  |...x|..x.|...x|..x.|   steps 4, 7, 12, 15 = 3+3+2
Hat    |..x.|..x.|..x.|..x.|

JERSEY CLUB 140 — Native Instruments
Kick   |X...|X...|X..X|..X.|   1, 5, 9, 12, 15 (4-4-3-3-2)
Snare  |....|....|x..x|....|   bars 1 & 3: 9, 12; bars 2 & 4: 9, 11, 12
Hat    |....|x...|....|x...|   beats 2 and 4
Bed squeak / vocal chops on the 16ths after kicks

PHONK (drift) 140-150 — convention
Kick   |X...|..x.|X...|..x.|
Snare  |....|X...|....|X...|   (beat-3 half-time in Memphis style)
Cowbell|x..x|..x.|x..x|..x.|   tuned 808 cowbell melody, tresillo-based, distorted
```

### Electronic, pop and cinematic styles

| Genre | BPM (default) | Swing | Kick | Harmony | Bass | Signature | Key sources |
|---|---|---|---|---|---|---|---|
| Classic / Chicago house | 120–126 (124) | 55–60% | 4-floor | minor/Dorian vamps; gospel major | simple offbeat | 909+707 claps, tambourine on every offbeat (two copies panned L/R), syncopated rim | [Attack](https://www.attackmagazine.com/technique/beat-dissected/21st-century-chicago-house/) |
| Deep house | 110–125 | 55–62% (convention) | 4-floor | "advanced chord structures", m7/m9 | muted, round | **avoids build/release**; hypnotic repetition | [Wikipedia: Deep house](https://en.wikipedia.org/wiki/Deep_house) |
| Deep tech house | 125–130 | 60–65% | 909 on quarters | minimal | rolling | 16th shaker velocity "plays a very important role"; clap high-passed below 120 Hz; ~4 dB bus compression | [Attack](https://www.attackmagazine.com/technique/beat-dissected/deep-tech-house/) |
| Tech house | 123–126 | 55–65% | 4-floor | 0–1 chords | rolling 16th offbeat bounce | percussive, dry, vocal one-shots | [Wikipedia: Tech house](https://en.wikipedia.org/wiki/Tech_house); Loopmasters snippet |
| Afro house | 80–122 (club ≈118–124, convention) | 52–58% | 4-floor | modal minor vamps | warm syncopated sub | 3+3+2 congas and toms, chants | [Wikipedia: Afro house](https://en.wikipedia.org/wiki/Afro_house) |
| Techno | 120–150 | ≈straight; rolling techno 20% | 4-floor | often none | rumble or 303 | rhythm and timbre over harmony | [Wikipedia: Techno](https://en.wikipedia.org/wiki/Techno); [Attack](https://www.attackmagazine.com/technique/beat-dissected/rolling-techno/) |
| Hard techno | 145–160; **median 146 (IQR 136–155, n = 9,988)** | ≈straight | distorted rumble kick | atonal | the rumble kick is the bass | everything clipped; "attitude matters more than BPM" | [Futureproof](https://futureproofmusicschool.com/blog/what-is-hard-techno); [Mixgraph](https://www.mixgraph.io/bpm-for/hard-techno) |
| Trance | 125–150 (uplifting ≈138) | straight | 4-floor; open hat on every upbeat | natural minor i–VI–III–VII | rolling offbeat bass | JP-8000 supersaw (7 detuned saws), beatless breakdowns, rising snare-roll builds, 1–2 peaks | [Wikipedia: Trance](https://en.wikipedia.org/wiki/Trance_music); [Orphiq](https://orphiq.com/resources/what-is-trance-music) |
| DnB | 160–180, mostly 170–180 (174) | slight late lean | two-step | liquid: jazz 7ths/9ths | clean sub + reese | chopped Amen/Think breaks, 1/32–1/64 fills, a beat of silence before drops | [Wikipedia: DnB](https://en.wikipedia.org/wiki/Drum_and_bass); [Violet Recording](https://violetrecording.com/how-to-make-drum-and-bass/) |
| Neurofunk / liquid / jungle | 172–176 / 172–176 / 160–170 | — | two-step / two-step / chopped breaks | atonal / soulful / ragga | FM-wavetable mid over sub / smooth / dub sub | neuro: technical; liquid: more harmony; jungle: dense polyrhythm | [Wikipedia: Neurofunk](https://en.wikipedia.org/wiki/Neurofunk); [Wikipedia: Liquid](https://en.wikipedia.org/wiki/Liquid_funk) |
| Dubstep / riddim | 140 half-time / 140–150 | straight | sparse | minor/Phrygian / one note | wobble or growl / one looping mid-bass motif in triplets | silence as an instrument (riddim) | [Wikipedia: Dubstep](https://en.wikipedia.org/wiki/Dubstep); [BassGorilla](https://bassgorilla.com/what-is-riddim-dubstep/) (snippet) |
| Future bass | 130–175 (140–160 half-time) | ≈straight | half-time | major-leaning maj7/m7/add9; triads too thin unless doubled | long sub under short chords | pitch-bent supersaw chords, heavy pumping, "twinkly" risers | [Wikipedia: Future bass](https://en.wikipedia.org/wiki/Future_bass); [Violet Recording](https://violetrecording.com/how-to-make-future-bass/); [FeelYourSound](https://feelyoursound.com/articles/future-bass-tutorial/) |
| UK garage / 2-step | 124–132 / 122–128 | MPC 68–69 / 60–65% | downbeat + offbeat of beat 3 / no kick on beat 1 of bar 2 | m7/m9 R&B | syncopated sub, organ bass | rimshots as snare substitute, cabasa offbeats | [Attack: UKG](https://www.attackmagazine.com/technique/beat-dissected/uk-garage/); [Attack: 2-step](https://www.attackmagazine.com/technique/beat-dissected/rolling-2-step-garage/) |
| Synthwave | 80–118; upbeat 128–140 | straight | 4-floor or rock | Aeolian i–VI–III–VII | octave-pulsing 8th/16th saw | gated snare, arps | [Wikipedia: Synthwave](https://en.wikipedia.org/wiki/Synthwave) |
| Modern pop | 95–125 dance; 70–90 ballad | — | 4-floor or trap | I–V–vi–IV family; IV and V more common than I | sub/808 locked to the kick | hook within ~30–45 s; median length 3:13 | [Hooktheory](https://www.hooktheory.com/blog/i-analyzed-the-chords-of-1300-popular-songs-for-patterns-this-is-what-i-found/); [DEV](https://dev.to/tonywangca/are-songs-really-getting-shorter-6618-hot-100-hits-1959-2025-4cdg) |
| Hyperpop | 135–170+ (NI: 205) | — | NI 2-bar, all velocity 100 | "saccharine" progressions | distorted 808 | Auto-Tune, glitches, clipping | [Wikipedia: Hyperpop](https://en.wikipedia.org/wiki/Hyperpop); [NI](https://blog.native-instruments.com/hyperpop/) |
| Ambient | beatless | — | none | drones, maj7/sus, Lydian | none | texture over structure (Eno, 1978) | [Wikipedia: Ambient](https://en.wikipedia.org/wiki/Ambient_music) |
| Cinematic trailer | free → 120–150 | — | taiko 3+3+2 | Aeolian, Phrygian threat | braams, sub drops | three acts; "the quiet before a hit matters as much as the hit" | [Violet Recording](https://violetrecording.com/sound-design-for-trailers/) |

```
CLASSIC HOUSE 124 — swing 55-60%
Kick   |X...|X...|X...|X...|   115-120
Clap   |....|X...|....|X...|
CH     |xxxx|xxxx|xxxx|xxxx|   beats 90, "&" 75, e/a 55
OH     |..o.|..o.|..o.|..o.|
Tamb   |..x.|..x.|..x.|..x.|   two detuned copies, L/R
Rim    |...x|..x.|....|.x..|   syncopated; bar 4 adds a kick on step 15 (~80) as a turnaround

TECH HOUSE 126 — swing 55-65%
Kick   |X...|X...|X...|X...|
Clap   |....|X...|....|X..g|
CH     |xx.x|xx.x|xx.x|xx.x|   1st, 2nd, 4th 16th of each beat (snippet-level)
OH     |..o.|..o.|..o.|..o.|
Bass   |..xx|..xx|..xx|..xx|   16th offbeat bounce, heavy sidechain

TECHNO 128-135 — near straight
Kick   |X...|X...|X...|X...|
CH     |..x.|..x.|..x.|..x.|   + 16th layer 70/45
Ride   |..x.|..x.|..x.|..x.|   peak sections
Rolling variant (Attack, 131 BPM): kicks on 1 and 3 + ghost kicks before 2 and 4;
low-passed toms alternate on every 16th; claps scattered with ghost velocities

TRANCE 138 — straight
Kick   |X...|X...|X...|X...|
Clap   |....|x...|....|x...|
OH     |..o.|..o.|..o.|..o.|   every upbeat
Bass   |.xxx|.xxx|.xxx|.xxx|   rolling (or offbeat 8ths)
Build: snare roll 4ths -> 8ths -> 16ths -> 32nds over 8-16 bars, velocity ramp

UK GARAGE 2-STEP 130 — MPC swing 60-69%
           bar 1                  bar 2
Kick   |X...|....|..x.|....|  |.x..|....|..x.|....|
Snare  |....|X...|....|X...|  |....|X...|....|X...|
Rim    |...g|...x|.g..|..x.|  |..g.|...x|....|.gx.|
OH     |..o.|..o.|..o.|..o.|  (offbeats; decay between closed and open)

DRUM & BASS 174 — two-step
Kick   |X...|....|..x.|....|  |X...|....|..x.|..g.|
Snare  |....|X...|....|X...|  |....|X...|....|X...|
Ghost  |....|...g|.g..|...g|  (from a chopped break, slices nudged off-grid)
Hat    |x.x.|x.x.|x.x.|x.x.|  (liquid: ride and shaker forward)

DUBSTEP 140 (half-time)
Kick   |X...|....|....|....|   (+ step 11 or 12 variant)
Snare  |....|....|X...|....|
CH     |..x.|..x.|..x.|..x.|
Bass fills the kick-snare gaps in 1-bar call-and-response; riddim = 1/8T stabs with rests

FUTURE BASS 150 (half-time)
Kick   |X...|....|..x.|....|
Snare  |....|....|X...|....|   clap + snare, big reverb
CH     |x.x.|x.x.|x.x.|x.x.|   + 1/32 rolls, triplet runs
Chords |x..x|..x.|x..x|..x.|   supersaw stabs, heavy sidechain, pitch-bend swells

SYNTHWAVE 100 — straight
Kick   |X...|X...|X...|X...|   (or rock: |X...|....|X.x.|....|)
Snare  |....|X...|....|X...|   gated reverb
CH     |xgxg|xgxg|xgxg|xgxg|
Bass   |xxxx|xxxx|xxxx|xxxx|   root/octave 16ths; gated tom fill in the last bar of each 8

HYPERPOP 205 — Native Instruments, all velocity 100
           bar 1                  bar 2
Kick   |X...|....|....|X...|  |....|....|....|X.X.|
Snare  |....|....|X...|....|  |....|....|X...|....|

TRAILER ACT 3 ~120-140
Taiko  |X..x|..x.|X..x|..x.|   3+3+2 drive
Snare  |....|X...|....|X...|   or 16th string ostinato
Hits on section downbeats; 1-2 beats of silence before the final hit; "button" ending
```

The harmony conventions for electronic styles (convention unless cited):
- **Deep house:** loops such as Am9–Dm9–Gmaj7–Cmaj7.
- **Trance:** Am–F–C–G, with a sus chord held "one bar longer than feels comfortable", and an optional semitone or whole-tone key lift in the final drop (snippet-level, not verified).
- **Future bass:** royal-road IVmaj7–V–iii7–vi, or a minor chord moving to its relative major ([Violet Recording](https://violetrecording.com/how-to-make-future-bass/)).
- **Liquid DnB:** jazz ii–V–I.
- **Synthwave:** i–VI–III–VII and i–VII–VI–VII.
- **Trailers:** i–VI–III–VII epics over 16th string ostinati on a pedal, with Phrygian b2 for threat.
- **Techno, riddim and hard techno:** largely atonal. Melody lives in timbre, filter and modulation ([Wikipedia: Techno](https://en.wikipedia.org/wiki/Techno)).

Arrangement templates (convention, built on the cited bar-length findings):

| Genre | Template |
|---|---|
| House, extended mix | Intro A 16 (drums only), Intro B 16, Groove 32, Breakdown 16, Build 8 (with a 1-beat gap), Drop 32, Groove 16–32, Outro 32 |
| Trance | Intro 32, Groove 32, Breakdown 16–32, Build 8–16, Climax 32, Mid 16–32, Climax 2 32, Outro 32 |
| Dubstep | Intro 16–32, Build 8, Drop 16–32, Breakdown 16, Build 8, Drop 2 16–32, Outro 16 |
| Future bass | Intro 8, Verse 16, Build 8, Drop 16, Verse 8–16, Build 8, Drop 2 16, Outro 8 |
| UK garage | Intro 16, Verse 16, Hook 16, Break 8, Verse 16, Hook 16, Dub 16, Outro 16 |
| Pop (target 2:45–3:15) | Intro 4, Verse 8, Pre 4–8, Chorus 8, Post-chorus 4–8, Verse 8, Pre 4, Chorus 8, Post 4–8, Bridge 8, Final chorus 8–16 |
| Trailer | Act 1 0:00–0:40, Act 2 to 1:30, Act 3 to 2:15, then a button |

The cross-genre build toolkit:
- Subtract the kick and bass 4–16 bars out.
- Accelerate the snare.
- Rise spectrally with high-pass filters, noise and pitch risers.
- Leave half a beat to one beat of silence (cited for DnB).
- Land with a crash, sub drop and the kick on beat 1.
- Vary the second drop.

## The science explains why these rules work

### Consonance is learned harmonicity, not pure physics

McDermott, Lehr and Oxenham (2010) tested more than 250 listeners. Listeners disliked beating and liked harmonic spectra, but **only the harmonicity preference correlated with liking consonant chords**, and it grew with years of playing an instrument ([McDermott et al. 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2885564)).

McDermott and colleagues (2016) then tested the Tsimane' of Bolivia, who have minimal exposure to Western music. They rated consonant and dissonant chords as **equally pleasant**, even though they disliked roughness in other contexts. Groups with more Western exposure showed progressively stronger consonance preferences ([MIT McGovern](https://mcgovern.mit.edu/?p=13810); [Brandeis](https://www.brandeis.edu/now/2016/july/music-biology-tsimane.html)).

Bowling, Purves and Gill (2018) found that consonance across every chromatic dyad, triad and tetrad within an octave was predicted by **similarity to the harmonic spectra of voiced speech** ([Duke](https://scholars.duke.edu/publication/1292995)).

For a skill, this means "consonant = pleasant" is a style setting tuned for Western pop listeners, not a law of nature. Warm, human-sounding parts favour harmonically aligned voicings, and tension can come from inharmonic intervals or timbres such as bells, FM and metallic sounds. Timbre and harmony interact: a consonant chord on a heavily distorted or inharmonic patch can still sound rough (inference from both accounts).

### Pleasure peaks at intermediate predictability

Huron's ITPRA theory names five response systems: Imagination, Tension, Prediction, Reaction and Appraisal. Accurate predictions are rewarded. Surprises trigger a fast negative reaction that slower appraisal can reframe as pleasant, which Huron calls "contrastive valence" ([Music & Letters review](https://academic.oup.com/ml/article/89/3/396/1135734)).

Cheung et al. (2019) gave this a quantitative form. They modelled uncertainty and surprise for about 80,000 chords from Billboard songs. **Pleasure was highest for two combinations: low uncertainty with high surprise, and high uncertainty with low surprise.** The amygdala, hippocampus and auditory cortex tracked the interaction ([Cambridge](https://cms.mus.cam.ac.uk/publications/cheung-uncertainty-surprise/); [Neuroscience News](https://neurosciencenews.com/pop-music-surprise-15181/)).

Gold et al. (2019) found that listeners preferred musical fragments of **intermediate complexity**, an inverted U. Repetition lowered liking but did not remove that preference ([Gold et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6867811)). Matthews et al. (2019) found the same inverted U for rhythm, strongest with medium-complexity harmony ([Matthews et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6328141)).

Together these give a usable two-axis rule:
- **After a highly predictable context, spend one surprise.** Three loops of I–V–vi–IV followed by a bVII, iv or bVI is the pattern.
- **After an ambiguous passage, land on the most expected chord.**
- **Never stack surprise on surprise.**
- **Spread complexity across dimensions** rather than maximising any one. Busy syncopation wants moderate harmony.

The surprise baseline is genre-relative: a bVII is mildly surprising in pop and a cliché in rock (inference).

### Builds and drops exploit a two-phase dopamine reward

Salimpoor et al. (2011) used PET imaging and found **dopamine released in the striatum at peak emotion**. Caudate activity was tied to anticipation and nucleus accumbens activity to the chill itself ([Salimpoor et al. 2011](https://www.zlab.mcgill.ca/publications/docs/salimpoor_2011_nn.pdf)). Grewe et al. (2007) showed that chills mark individual emotional peaks, aligned with peaks in physiological measures ([Wicri record](https://wicri-demo.istex.fr/Wicri/Musique/explor/MozartV1/Site/fr/Main/Exploration/bibRecord.php?hk=000D40)). The same research group found that chill excerpts showed a loudness increase specifically in the **920–4400 Hz band (8–18 Bark)** ([JYX](https://jyx.jyu.fi/handle/123456789/19439?show=full)). A climax should therefore raise presence-range energy (open filters, upper harmonies, lead forward), not just sub-bass.

Chills are not only for bombast. De Fleurian and Pearce (2021) compiled more than 700 chill-inducing songs. Compared with matched tracks by the same artists, they were on average **sadder, slower, less intense and more instrumental** ([QMRO](https://qmro.qmul.ac.uk/xmlui/handle/123456789/75159)).

The synthesis is an inference, since no EDM-specific study was retrieved:
- A build raises certainty that a big event is coming, which lengthens the anticipation phase.
- The drop delivers that event with a large contrast in loudness, bass and texture.
- A brief silence before the drop is a small surprise inside a high-certainty context, exactly Cheung's high-pleasure combination.
- Risers should be predictable in direction, and the payoff should add something new.

### Emotion uses partly universal cues, and sad music pleases because it is safe

Fritz et al. (2009) found that Mafa listeners in Cameroon, with no prior exposure to Western music, recognised happy, sad and fearful piano pieces above chance ([ScienceDaily](https://sciencedaily.com/releases/2009/03/090319132909.htm)). Juslin's BRECVEMA framework lists eight mechanisms by which music induces emotion ([Emotion Researcher](https://emotionresearcher.com/music-and-emotion-there-is-more-to-music-than-meets-the-ear/)):
- **B**rain-stem reflex to sudden loud events;
- **R**hythmic entrainment;
- **E**valuative conditioning;
- **C**ontagion from voice-like melody;
- **V**isual imagery;
- **E**pisodic memory;
- **M**usical expectancy;
- **A**esthetic judgement.

Sachs, Damasio and Habibi (2015) reviewed why sad music is often enjoyed and pointed to the aesthetic distance of a safe context ([Sachs et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4513245/)).

The practical cue map comes from consensus in the literature; the specific cue tables were not retrieved this session, so treat it as convention:

| Emotion | Cues |
|---|---|
| Happy | fast, major, high register, bright articulation |
| Sad | slow, minor, low register, legato, soft, dark timbre |
| Tension | irregular rhythm, dissonance, sudden dynamics, extreme registers |
| Anger | fast, loud, distorted |

Tempo and loudness are more robust drivers than mode, which is a strong Western convention. A reliable recipe for "pleasurable sadness" is a minor ballad with consonant voicings, lush reverb and a resolving cadence.

### Repetition makes sound into music, and over-repetition still bores

Margulis argues that repetition is much of what makes a sound register as music. She cites Huron's estimate that **over 90%** of the music people hear is music they have heard before ([OUP blog](https://blog.oup.com/2014/01/music-repetition-neuroscience/)).

Deutsch's speech-to-song illusion shows repetition at work directly. A spoken phrase repeated about ten times starts to sound sung, but the effect disappears if the repeats are transposed or jumbled ([Deutsch, UCSD](https://deutsch.ucsd.edu/psychology/pages.php?i=212)). For hooks, this means **exact-pitch repetition of a vocal chop makes it melodic**.

Gold et al. (2019) showed that repeating identical stimuli lowers liking ([Gold et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC6867811)). The resolution is to keep the hook constant and vary its surroundings, such as drums, harmony and register, on each return. Familiarity also raises groove ratings for drum patterns ([Senn et al. 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6025871)). So a skill should innovate on top of a recognisable genre template, not abandon it.

### Loudness does not win preference, and dynamic contrast drives peaks

Vickers reviewed the loudness war and reported three findings ([AES e-library](https://aes2.org/publications/elibrary-page/?id=15598)):
- loudness does not correlate with sales;
- loudness has little effect on preference between songs;
- listeners tend to dislike the side effects of hypercompression.

The direct evidence is mixed. An Aalborg study found no effect of compression on preference ([Aalborg](https://vbn.aau.dk/da/publications/perceptual-effects-of-dynamic-range-compression-in-popular-music-)). A Goldsmiths study found that heavier compression lowered quality judgements ([Goldsmiths SysMus14](https://bjmh.gold.ac.uk/index.php/sysmus14/article/view/236)).

The defensible position is that moderate compression is harmless, while heavy limiting that removes section-to-section contrast throws away the loudness and presence jump that chills depend on. Since the platforms normalise anyway, the payoff from slamming the master is small.

## The research implies a seven-skill architecture with tunable defaults

The findings map onto a modular skill set. Each skill below should expose its numbers as editable defaults rather than hard-coded truths, because most of them are practitioner convention.

| Skill | Core encoded rules | Strongest evidence | Most fragile parameters |
|---|---|---|---|
| Theory core | MIDI/FL octave mapping, scale and mode formulas, chord formulas, diatonic tables, circle of fifths, Hz math | arithmetic plus standard theory | none (deterministic) |
| Chords & voicing | progression library; nearest-voicing algorithm; low-interval rules; register floors (chords ≥ MIDI 48 with an 808 present); harmonic-rhythm defaults per genre | Plomp & Levelt; voice-leading conventions | low-interval-limit values (approximate) |
| Melody & hook | contour (arch, one climax at 55–75%); 65–80% steps; gap-fill; chord tones on strong beats; motif operations; earworm checklist; counter-melody rules | Patel; von Hippel & Huron; Jakubowski; Sloboda | step/leap ratios; density targets |
| Drums & groove | 16-step genre grids; velocity bands; Linn swing; roll templates; fill schedule; medium-syncopation rule | Witek; Senn; Davies; Lenc; Hove; Linn | MPC↔FL swing mapping; exact grids for unsourced genres |
| Bass & 808 | root on change; K1/K2/K3 strategies; 808 window MIDI 24–40; slide rules (native instruments only); saturation layer | Image-Line manual; Violet/Audeobox; missing-fundamental | glide times; the "safe" 808 floor |
| Arrangement | role and plane assignment; max 3–4 focal elements; register map; genre bar templates; energy curves; subtractive loop-to-song workflow | Owsinski; rule of three; Inspired by Beatz; EDMProd | per-genre bar counts outside EDM, hip hop and DnB |
| Mix & master | gain staging −18 dBFS; EQ lanes; kick→808 sidechain via Fruity Limiter; pan map; tempo-synced sends; master to −14 LUFS / −1 dBTP or −8 to −10 LUFS for beats; error checks | Spotify; AES TD1008; Image-Line manuals | element dB offsets; sidechain release times |

Two FL-specific constraints shape implementation:
- **Slides need native instruments.** Overlap portamento and slide behaviour do not work on VST/AU instruments ([Image-Line](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/chansettings_misc.htm)). An 808 skill should target FL's sampler, FLEX or 3x Osc when slides are required.
- **Swing must be set on both levels.** Channel Rack swing only takes effect when both global and per-channel swing are above zero ([Image-Line](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/channelrack.htm)).

The FL Studio MCP bridge in this workspace exposes note, chord-progression, step-sequencer, tempo, mixer-volume, pan, routing and mix-diagnosis tools. Plugin parameter control is likely unavailable there. So the mix skill can apply level, pan and routing conventions directly but should describe plugin settings for the user to set.

## Conclusion

The most useful finding for automation is that beauty in this music is governed less by rare rules than by **budgets**. There is a budget of attention: three or four focal elements and one owner of the sub. There is a budget of surprise: one unexpected chord or leap per predictable context, as both the Cheung and Jakubowski results imply. And there is a budget of complexity across dimensions: medium syncopation pairs with medium harmonic richness. A composer skill that tracks these budgets explicitly, rather than only generating notes, will make different and better choices. It will hold the progression steady when the drums get busy. It will save the borrowed chord for the fourth loop. It will clear the low end and the presence band before a drop so the payoff has headroom.

The second takeaway concerns trust in the numbers. The theory layer (intervals, scales, voicings, MIDI and Hz math) is deterministic and safe to hard-code. The perceptual layer is well supported on direction (consonance, groove, expectation, chills) but rarely on exact values. The genre layer is mostly convention, with several known conflicts or gaps:
- MPC versus FL swing scales;
- drill bar-2 snare placement;
- amapiano log-drum placements;
- pop timing statistics from aggregators;
- an unverified 808 floor.

The right design is a deterministic core wrapped in tunable genre cards. Each card should be marked with its evidence level and checked against a reference track and by ear before it is treated as canon.
