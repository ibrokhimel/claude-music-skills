# Theory tables: deterministic pitch, interval, scale, chord, key and time math

One-line summary: every lookup table Claude needs to turn note names, scales, chords, keys and tempos into exact MIDI numbers, Hz values and tick positions. All numbers are **(derived)** arithmetic or standard theory unless marked otherwise.

Contents
1. Pitch coordinates (MIDI, scientific, FL labels)
2. Note-to-MIDI-to-Hz grid
3. Register map
4. Intervals (simple and compound)
5. Harmonic series
6. Scales and modes
7. Chord formulas
8. Roman numerals and semitone offsets
9. Keys and the circle of fifths
10. Diatonic chords: major, natural minor, harmonic minor, modal colour chords
11. Tempo, grid and tick math

---

## 1. Pitch coordinates

- Pitch classes: C=0, C#/Db=1, D=2, D#/Eb=3, E=4, F=5, F#/Gb=6, G=7, G#/Ab=8, A=9, A#/Bb=10, B=11.
- Scientific octave: `MIDI = 12 × (octave + 1) + pc`. C4 = 60 (middle C), A4 = 69 = 440 Hz.
- **FL Studio label = scientific octave + 1**: `MIDI = 12 × FL_octave + pc`. FL shows MIDI 60 as "C5", MIDI 36 as "C3".
- Inverse: `pc = MIDI % 12`, `sci_octave = MIDI // 12 − 1`, `FL_octave = MIDI // 12`.
- Frequency: `f = 440 × 2^((m − 69)/12)`. Inverse: `m = 69 + 12 × log2(f/440)`.
- Cents between two frequencies: `1200 × log2(f2/f1)`; 100 cents = 1 semitone.
- Always write registers as "MIDI 48 (C3, FL: C4)".
- Spell flats in flat keys (F, Bb, Eb, Ab, Db, Gb and their relative minors), sharps in sharp keys. The MIDI number is the same either way.

## 2. Note-to-MIDI-to-Hz grid

Cell = `MIDI / Hz`. Column header = scientific octave (FL octave in brackets).

| PC | oct 0 (FL 1) | oct 1 (FL 2) | oct 2 (FL 3) | oct 3 (FL 4) | oct 4 (FL 5) | oct 5 (FL 6) | oct 6 (FL 7) | oct 7 (FL 8) |
|---|---|---|---|---|---|---|---|---|
| C | 12 / 16.4 | 24 / 32.7 | 36 / 65.4 | 48 / 130.8 | 60 / 261.6 | 72 / 523.3 | 84 / 1047 | 96 / 2093 |
| C# | 13 / 17.3 | 25 / 34.6 | 37 / 69.3 | 49 / 138.6 | 61 / 277.2 | 73 / 554.4 | 85 / 1109 | 97 / 2217 |
| D | 14 / 18.4 | 26 / 36.7 | 38 / 73.4 | 50 / 146.8 | 62 / 293.7 | 74 / 587.3 | 86 / 1175 | 98 / 2349 |
| D# | 15 / 19.4 | 27 / 38.9 | 39 / 77.8 | 51 / 155.6 | 63 / 311.1 | 75 / 622.3 | 87 / 1245 | 99 / 2489 |
| E | 16 / 20.6 | 28 / 41.2 | 40 / 82.4 | 52 / 164.8 | 64 / 329.6 | 76 / 659.3 | 88 / 1319 | 100 / 2637 |
| F | 17 / 21.8 | 29 / 43.7 | 41 / 87.3 | 53 / 174.6 | 65 / 349.2 | 77 / 698.5 | 89 / 1397 | 101 / 2794 |
| F# | 18 / 23.1 | 30 / 46.2 | 42 / 92.5 | 54 / 185.0 | 66 / 370.0 | 78 / 740.0 | 90 / 1480 | 102 / 2960 |
| G | 19 / 24.5 | 31 / 49.0 | 43 / 98.0 | 55 / 196.0 | 67 / 392.0 | 79 / 784.0 | 91 / 1568 | 103 / 3136 |
| G# | 20 / 26.0 | 32 / 51.9 | 44 / 103.8 | 56 / 207.7 | 68 / 415.3 | 80 / 830.6 | 92 / 1661 | 104 / 3322 |
| A | 21 / 27.5 | 33 / 55.0 | 45 / 110.0 | 57 / 220.0 | 69 / 440.0 | 81 / 880.0 | 93 / 1760 | 105 / 3520 |
| A# | 22 / 29.1 | 34 / 58.3 | 46 / 116.5 | 58 / 233.1 | 70 / 466.2 | 82 / 932.3 | 94 / 1865 | 106 / 3729 |
| B | 23 / 30.9 | 35 / 61.7 | 47 / 123.5 | 59 / 246.9 | 71 / 493.9 | 83 / 987.8 | 95 / 1976 | 107 / 3951 |

## 3. Register map

Anchors are derived; "typical occupant" and the zone limits are **(convention)** — details live in the sibling skills.

| Zone | MIDI | Scientific (FL) | Hz | Occupant / rule |
|---|---|---|---|---|
| Sub floor | 24–28 | C1–E1 (FL C2–E2) | 33–41 | practical floor for 808 roots; deep 808 |
| 808 sweet spot | 28–35 | E1–B1 | 41–62 | pick a key whose tonic lands here (F, F#, G, A minor) — see `music-bass-808` |
| Bass | 28–52 | E1–E3 | 41–165 | bass guitar/synth bass; root, 5th, octave only below 48 |
| Low harmony floor | 48 | C3 (FL C4) | 131 | lowest note for chord 3rds when an 808/sub owns the root |
| Harmony core | 52–76 | E3–E5 | 165–659 | keys/pads voicing window — see `music-chords-voicing` |
| Lead / topline | 60–84 | C4–C6 | 262–1047 | melody sits highest among prominent parts — see `music-melody-hooks` |
| Bells, arps, sparkle | 72–96 | C5–C7 | 523–2093 | trap/drill bells, plucks, arps |
| Presence band | — | — | ~920–4400 | where chills-related loudness rises (Nagel 2008) — keep headroom here for climaxes |

Drum samples in FL's Sampler play at their own pitch on MIDI 60 (FL "C5"). A sampled 808 follows `heard_pitch = sample_root + (note − 60)`, so if the 808 sample sounds at C1 (24), MIDI note 63 plays Eb1 (27).

## 4. Intervals

`ET−just` = how far the equal-tempered interval sits from the just ratio, in cents. Character column is **(convention)**.

| St | Interval | Inversion | Just ratio | ET−just (¢) | Production character |
|---|---|---|---|---|---|
| 0 | unison | octave | 1:1 | 0 | doubling, thickness, phasing risk if detuned |
| 1 | minor 2nd (m2) | M7 | 16:15 | −11.7 | harshest; Phrygian trap/drill grind; resolve by step |
| 2 | major 2nd (M2) | m7 | 9:8 | −3.9 | mild; sus2 / add9 air |
| 3 | minor 3rd (m3) | M6 | 6:5 | −15.6 | minor quality, dark |
| 4 | major 3rd (M3) | m6 | 5:4 | +13.7 | major quality, bright |
| 5 | perfect 4th (P4) | P5 | 4:3 | +2.0 | open, hollow; sus4; quartal |
| 6 | tritone (TT) | TT | 45:32 (≈√2) | +9.8 | maximal instability; core of V7 |
| 7 | perfect 5th (P5) | P4 | 3:2 | −2.0 | most stable after the octave; power chords; safe low |
| 8 | minor 6th (m6) | M3 | 8:5 | −13.7 | bittersweet; the Aeolian colour note (b6) |
| 9 | major 6th (M6) | m3 | 5:3 | +15.6 | warm; the Dorian colour note |
| 10 | minor 7th (m7) | M2 | 16:9 (harmonic 7th 7:4 = 968.8¢) | +3.9 | bluesy, soft tension; fuses because it approximates 7:4 |
| 11 | major 7th (M7) | m2 | 15:8 | +11.7 | lush when wide; harsh when inverted to a m2 |
| 12 | octave (P8) | unison | 2:1 | 0 | identity, doubling |
| 13 | minor 9th (b9) | — | 32:15 | — | dark; dominant chords only |
| 14 | major 9th (9) | — | 9:4 | — | colour, R&B/lo-fi warmth |
| 15 | minor 10th (#9 / m3+8) | — | 12:5 | — | "Hendrix" #9 on dominants |
| 16 | major 10th | — | 5:2 | — | warm left-hand spread (48 \| 64) |
| 17 | perfect 11th (11) | — | 8:3 | — | sus/m11 colour; avoid over major 3rd |
| 18 | augmented 11th (#11) | — | ≈45:16 | — | Lydian shimmer |
| 20 | minor 13th (b13) | — | 16:5 | — | altered dominant |
| 21 | major 13th (13) | — | 10:3 | — | soulful dominant |

Rules of thumb: wide intervals low, close intervals high; m2 and TT need a reason (tension) and a resolution; m2/M7 clashes are the main "wrong note" sound. Low-interval limits (how low each interval stays clear) are in `music-chords-voicing`.

## 5. Harmonic series (on C2 = MIDI 36)

| Partial | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Note | C2 | C3 | G3 | C4 | E4 | G4 | Bb4 (−31¢) | C5 | D5 | E5 |
| MIDI | 36 | 48 | 55 | 60 | 64 | 67 | ~70 | 72 | 74 | 76 |

Octave and 5th at the bottom, 3rds and 2nds only higher up: copy this layout for clear voicings.

## 6. Scales and modes

Mood/use column is **(convention)**; trap, lo-fi and drill scale links are **(sourced)** only at tutorial level (Production Music Live, SampleFocus, Orphiq).

| Scale | Semitones from root | Steps | Characteristic note | Mood and typical use |
|---|---|---|---|---|
| Ionian (major) | 0 2 4 5 7 9 11 | W W H W W W H | natural 4 and 7 | bright; pop, house, EDM drops, afrobeats |
| Dorian | 0 2 3 5 7 9 10 | W H W W W H W | **M6** | cool, hopeful minor; lo-fi, neo-soul, deep house, funk |
| Phrygian | 0 1 3 5 7 8 10 | H W W W H W W | **b2** | menacing; trap, drill, phonk, horror |
| Lydian | 0 2 4 6 7 9 11 | W W W H W W H | **#4** | floating, wonder; cinematic, future bass, ambient |
| Mixolydian | 0 2 4 5 7 9 10 | W W H W W H W | **b7** | laid-back major; funk, gospel vamps, rock |
| Aeolian (natural minor) | 0 2 3 5 7 8 10 | W H W W H W W | **b6** | sad, serious; trap, synthwave, trance, trailers |
| Locrian | 0 1 3 5 6 8 10 | H W W H W W W | **b5** | unstable; brief dread only |
| Harmonic minor | 0 2 3 5 7 8 11 | W H W W H A2 H | **natural 7** (A2 gap from b6) | dramatic; trap/drill bells, V–i pull |
| Melodic minor (asc.) | 0 2 3 5 7 9 11 | W H W W W W H | M6 + M7 | sophisticated minor; neo-soul, jazz |
| Phrygian dominant | 0 1 4 5 7 8 10 | H A2 H W H W W | b2 + M3 | "eastern" trap/drill leads; flamenco (5th mode of harmonic minor) |
| Double harmonic | 0 1 4 5 7 8 11 | H A2 H W H A2 H | b2 + M7 | exotic/Middle-Eastern colour; use sparingly |
| Hungarian minor | 0 2 3 6 7 8 11 | W H A2 H H A2 H | #4 + natural 7 | villainous; drill, horror |
| Major pentatonic | 0 2 4 7 9 | — | no half steps | can't-miss toplines, afrobeats, pop hooks |
| Minor pentatonic | 0 3 5 7 10 | — | no half steps | hip hop hooks, R&B riffs, safe 808 melodies |
| Minor blues | 0 3 5 6 7 10 | — | b5 blue note | boom bap, gospel licks |
| Major blues | 0 2 3 4 7 9 | — | b3→3 slide | gospel, funk, country-soul |
| Whole-tone | 0 2 4 6 8 10 | all W | symmetrical | dreamlike, flashback; over aug/7#5 |
| Diminished (half-whole) | 0 1 3 4 6 7 9 10 | H W ... | symmetrical | over 7b9 chords; suspense |
| Diminished (whole-half) | 0 2 3 5 6 8 9 11 | W H ... | symmetrical | over dim7 chords; horror/suspense |

**Brightness ladder** (each step flattens exactly one note): Lydian → Ionian → Mixolydian → Dorian → Aeolian → Phrygian → Locrian. To darken a part by one notch, flatten the next note in the ladder (Ionian→Mixolydian: b7; Dorian→Aeolian: b6).

**Mode from a parent major** (same notes, different home): Dorian = major scale 2 semitones below (D Dorian = C major notes); Phrygian = 4 below; Lydian = 5 below; Mixolydian = 7 below; Aeolian = 9 below; Locrian = 11 below.

**Modal colour is audible only if** (a) the tonic is established by a pedal/vamp that keeps returning home and (b) the characteristic note actually sounds, ideally in a chord (C Dorian: the F major chord carries the A natural) **(convention)**.

## 7. Chord formulas

On C4 = 60. Formulas are standard; colours are **(convention)**.

| Symbol | Formula (st) | On C (MIDI) | Colour / use |
|---|---|---|---|
| maj (C) | 0 4 7 | 60 64 67 | stable, bright |
| m (Cm) | 0 3 7 | 60 63 67 | stable, dark |
| dim (C°) | 0 3 6 | 60 63 66 | tense, passing |
| aug (C+) | 0 4 8 | 60 64 68 | unresolved, eerie |
| sus2 | 0 2 7 | 60 62 67 | open, ambiguous |
| sus4 | 0 5 7 | 60 65 67 | wants 4→3 |
| 5 (power) | 0 7 12 | 48 55 60 | neutral; safe very low |
| 6 | 0 4 7 9 | 60 64 67 69 | vintage |
| m6 | 0 3 7 9 | 60 63 67 69 | noir, Dorian |
| add9 | 0 4 7 14 | 60 64 67 74 | pop shimmer |
| m(add9) | 0 3 7 14 | 60 63 67 74 | sad-beautiful trap piano |
| 6/9 | 0 4 7 9 14 | 60 64 67 69 74 | open final chord |
| maj7 | 0 4 7 11 | 60 64 67 71 | lush, dreamy |
| 7 (dominant) | 0 4 7 10 | 60 64 67 70 | dominant, bluesy |
| m7 | 0 3 7 10 | 60 63 67 70 | mellow minor |
| m(maj7) | 0 3 7 11 | 60 63 67 71 | spy, noir |
| m7b5 (ø7) | 0 3 6 10 | 60 63 66 70 | yearning ii in minor |
| dim7 (°7) | 0 3 6 9 | 60 63 66 69 | symmetrical suspense |
| 7sus4 | 0 5 7 10 | 60 65 67 70 | gospel/house suspended dominant |
| aug7 (7#5) | 0 4 8 10 | 60 64 68 70 | whole-tone dominant |
| maj9 | 0 4 7 11 14 | 60 64 67 71 74 | R&B/lo-fi tonic |
| 9 | 0 4 7 10 14 | 60 64 67 70 74 | funk dominant |
| m9 | 0 3 7 10 14 | 60 63 67 70 74 | deep house / neo-soul minor |
| 9sus4 | 0 5 7 10 14 | 60 65 67 70 74 | gospel/house; = Bb/C sound |
| m11 | 0 3 7 10 14 17 | 60 63 67 70 74 77 | airy minor |
| maj7#11 | 0 4 7 11 18 | 60 64 67 71 78 | Lydian shimmer |
| 13 (no 5, 11) | 0 4 10 14 21 | 60 64 70 74 81 | soulful dominant |
| 7b9 | 0 4 7 10 13 | 60 64 67 70 73 | dark dominant (V in minor) |
| 7#9 | 0 4 7 10 15 | 60 64 67 70 75 | funky/rock dominant |
| slash Bb/C | bass + foreign triad | 48 \| 58 62 65 | C9sus sound; gospel, house |

Avoid-note conventions **(convention)**: natural 11 over a major or dominant chord clashes a m9 above the 3rd — use #11. b9 only on dominant chords. On 5+ note chords drop the 5th first, then the root (the bass has it). A rootless chord is named by its bass: C–E–G–B over bass A is heard as Am9.

Inversions of C: root 60 64 67; 1st inv 64 67 72 (C/E); 2nd inv 67 72 76 (C/G). Voicing algorithms, shells, drop-2, rootless and quartal shapes: `music-chords-voicing`.

## 8. Roman numerals and semitone offsets

Use these offsets to transpose any progression: `chord_root = key_tonic + offset`.

| Offset | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| In major | I | bII | ii | bIII | iii | IV | #iv° | V | bVI | vi | bVII | vii° |
| In minor | i | bII (Neapolitan/Phrygian) | ii° | III | — | iv | — | v / V | VI | — | VII | vii° (harm.) |

Case convention: upper case = major triad, lower case = minor, ° = diminished, + = augmented, "7"/"maj7" etc. appended. In minor-key loops write the flat-free form (i–VI–III–VII); the same chords in a major-key frame are i–bVI–bIII–bVII.

## 9. Keys and the circle of fifths

Clockwise: C G D A E B F#/Gb Db Ab Eb Bb F. Neighbours differ by one note; relative minor = major tonic − 3 semitones (shares the key signature); parallel minor = same tonic (source of borrowed chords).

| Major key | Signature | Relative minor | Diatonic triads I ii iii IV V vi vii° |
|---|---|---|---|
| C | 0 | Am | C Dm Em F G Am B° |
| G | 1# | Em | G Am Bm C D Em F#° |
| D | 2# | Bm | D Em F#m G A Bm C#° |
| A | 3# | F#m | A Bm C#m D E F#m G#° |
| E | 4# | C#m | E F#m G#m A B C#m D#° |
| B | 5# | G#m | B C#m D#m E F# G#m A#° |
| F# / Gb | 6# / 6b | D#m / Ebm | F# G#m A#m B C# D#m E#° (= Gb Abm Bbm Cb Db Ebm F°) |
| Db | 5b | Bbm | Db Ebm Fm Gb Ab Bbm C° |
| Ab | 4b | Fm | Ab Bbm Cm Db Eb Fm G° |
| Eb | 3b | Cm | Eb Fm Gm Ab Bb Cm D° |
| Bb | 2b | Gm | Bb Cm Dm Eb F Gm A° |
| F | 1b | Dm | F Gm Am Bb C Dm E° |

Minor keys with an 808 root in the MIDI 24–35 window (choose the one in 28–33 when the sample allows — **(convention)**):

| Minor key | Natural-minor triads i ii° III iv v VI VII | Harmonic V | 808 tonic MIDI |
|---|---|---|---|
| Am | Am B° C Dm Em F G | E | 33 (A1, 55.0 Hz) |
| Em | Em F#° G Am Bm C D | B | 28 (E1, 41.2 Hz) |
| Bm | Bm C#° D Em F#m G A | F# | 35 (B1, 61.7 Hz) |
| F#m | F#m G#° A Bm C#m D E | C# | 30 (F#1, 46.2 Hz) |
| C#m | C#m D#° E F#m G#m A B | G# | 25 (C#1, 34.6 Hz) |
| G#m | G#m A#° B C#m D#m E F# | D# | 32 (G#1, 51.9 Hz) |
| Ebm | Ebm F° Gb Abm Bbm Cb Db | Bb | 27 (Eb1, 38.9 Hz) |
| Bbm | Bbm C° Db Ebm Fm Gb Ab | F | 34 (Bb1, 58.3 Hz) |
| Fm | Fm G° Ab Bbm Cm Db Eb | C | 29 (F1, 43.7 Hz) |
| Cm | Cm D° Eb Fm Gm Ab Bb | G | 24 (C1, 32.7 Hz) or 36 |
| Gm | Gm A° Bb Cm Dm Eb F | D | 31 (G1, 49.0 Hz) |
| Dm | Dm E° F Gm Am Bb C | A | 26 (D1, 36.7 Hz) |

Hooktheory (~1,300 sections) **(sourced)**: C major / A minor most common (transcription artefact); IV and V appear in more progressions than I; after iii the next chord is vi or IV ~93% of the time.

## 10. Diatonic chords

### C major (closed root position from MIDI 60)

| Degree | Triad | 7th chord | Function |
|---|---|---|---|
| I | C 60 64 67 | Cmaj7 60 64 67 71 | tonic |
| ii | Dm 62 65 69 | Dm7 62 65 69 72 | predominant |
| iii | Em 64 67 71 | Em7 64 67 71 74 | weak tonic substitute |
| IV | F 65 69 72 | Fmaj7 65 69 72 76 | predominant |
| V | G 67 71 74 | G7 67 71 74 77 | dominant |
| vi | Am 69 72 76 | Am7 69 72 76 79 | tonic substitute |
| vii° | B° 71 74 77 | Bm7b5 71 74 77 81 | weak dominant |

### C natural minor and harmonic minor

| Degree | Natural triad | Natural 7th | Harmonic-minor version |
|---|---|---|---|
| i | Cm 60 63 67 | Cm7 60 63 67 70 | Cm(maj7) 60 63 67 71 |
| ii° | D° 62 65 68 | Dm7b5 62 65 68 72 | same |
| III | Eb 63 67 70 | Ebmaj7 63 67 70 74 | Eb+ 63 67 71; Ebmaj7#5 63 67 71 74 |
| iv | Fm 65 68 72 | Fm7 65 68 72 75 | same |
| v | Gm 67 70 74 | Gm7 67 70 74 77 | **V = G 67 71 74; G7 67 71 74 77** |
| VI | Ab 68 72 75 | Abmaj7 68 72 75 79 | same |
| VII | Bb 70 74 77 | Bb7 70 74 77 80 | **vii° = B° 71 74 77; B°7 71 74 77 80** |

Function in minor: tonic i (and VI as substitute); predominant iv, ii°; dominant V/V7 (harmonic) or v / VII (modal, softer pull). Use harmonic V7→i at cadences and turnarounds; keep natural v in loops that should cycle without "ending".

### Modal colour chords (on C; swap one chord to get the mode)

| Mode | Diatonic triads | Signature chord(s) |
|---|---|---|
| Dorian | Cm Dm Eb F Gm A° Bb | **IV major (F 65 69 72)** — i–IV vamp = neo-soul/lo-fi |
| Phrygian | Cm Db Eb Fm G° Ab Bbm | **bII major (Db 61 65 68)** — i–bII menace |
| Lydian | C D Em F#° G Am Bm | **II major (D 62 66 69)** — I–II float |
| Mixolydian | C Dm E° F Gm Am Bb | **bVII (Bb 70 74 77)**, v minor — I–bVII–IV |
| Aeolian | Cm D° Eb Fm Gm Ab Bb | **bVI (Ab)**, bVII — i–VI–VII epic |

Borrowed chords (from the parallel key), secondary dominants, tritone subs, mediants, cadences, voice leading and the progression library: `music-chords-voicing`.

## 11. Tempo, grid and tick math

### Grid positions (4/4, 16 steps per bar = one FL Channel Rack bar)

| Position | Steps | Beat offset within bar |
|---|---|---|
| Beats 1, 2, 3, 4 | 1, 5, 9, 13 | 0, 1, 2, 3 |
| 8th offbeats ("&") | 3, 7, 11, 15 | 0.5, 1.5, 2.5, 3.5 |
| 16th "e" | 2, 6, 10, 14 | 0.25, 1.25, ... |
| 16th "a" | 4, 8, 12, 16 | 0.75, 1.75, ... |

`beat = (bar − 1) × 4 + (step − 1) / 4` (bars and steps 1-based). Half-time feel = snare on beat 3 (step 9) instead of 2 and 4 (steps 5, 13).

### Ticks at PPQ 96 (FL default; check project settings)

| Value | Beats | Ticks | FL snap |
|---|---|---|---|
| Bar (4/4) | 4 | 384 | Bar |
| Half | 2 | 192 | — |
| Quarter (beat) | 1 | 96 | Beat |
| 8th | 1/2 | 48 | 1/2 beat |
| 8th triplet | 1/3 | 32 | 1/3 beat |
| 16th (step) | 1/4 | 24 | 1/4 beat (Step) |
| 16th triplet | 1/6 | 16 | 1/6 beat |
| 32nd | 1/8 | 12 | 1/8 beat |
| 32nd triplet | 1/12 | 8 | — |
| 64th | 1/16 | 6 | — |

Triplets do not fit the 16-step Channel Rack grid — write them as MIDI notes.

### Tempo table

`quarter ms = 60000/BPM`; `16th ms = 15000/BPM`; `bar s = 240/BPM`; `bars → seconds = bars × 240/BPM`.

| BPM | 1/4 ms | 1/8 ms | dotted 1/8 ms | 1/16 ms | 1/8T ms | bar s | 8 bars s | 16 bars s |
|---|---|---|---|---|---|---|---|---|
| 60 | 1000 | 500 | 750 | 250.0 | 333 | 4.00 | 32.0 | 64.0 |
| 70 | 857 | 429 | 643 | 214.3 | 286 | 3.43 | 27.4 | 54.9 |
| 75 | 800 | 400 | 600 | 200.0 | 267 | 3.20 | 25.6 | 51.2 |
| 80 | 750 | 375 | 562 | 187.5 | 250 | 3.00 | 24.0 | 48.0 |
| 85 | 706 | 353 | 529 | 176.5 | 235 | 2.82 | 22.6 | 45.2 |
| 90 | 667 | 333 | 500 | 166.7 | 222 | 2.67 | 21.3 | 42.7 |
| 95 | 632 | 316 | 474 | 157.9 | 211 | 2.53 | 20.2 | 40.4 |
| 100 | 600 | 300 | 450 | 150.0 | 200 | 2.40 | 19.2 | 38.4 |
| 105 | 571 | 286 | 429 | 142.9 | 190 | 2.29 | 18.3 | 36.6 |
| 110 | 545 | 273 | 409 | 136.4 | 182 | 2.18 | 17.5 | 34.9 |
| 115 | 522 | 261 | 391 | 130.4 | 174 | 2.09 | 16.7 | 33.4 |
| 120 | 500 | 250 | 375 | 125.0 | 167 | 2.00 | 16.0 | 32.0 |
| 124 | 484 | 242 | 363 | 121.0 | 161 | 1.94 | 15.5 | 31.0 |
| 128 | 469 | 234 | 352 | 117.2 | 156 | 1.88 | 15.0 | 30.0 |
| 130 | 462 | 231 | 346 | 115.4 | 154 | 1.85 | 14.8 | 29.5 |
| 135 | 444 | 222 | 333 | 111.1 | 148 | 1.78 | 14.2 | 28.4 |
| 140 | 429 | 214 | 321 | 107.1 | 143 | 1.71 | 13.7 | 27.4 |
| 145 | 414 | 207 | 310 | 103.4 | 138 | 1.66 | 13.2 | 26.5 |
| 150 | 400 | 200 | 300 | 100.0 | 133 | 1.60 | 12.8 | 25.6 |
| 160 | 375 | 188 | 281 | 93.8 | 125 | 1.50 | 12.0 | 24.0 |
| 170 | 353 | 176 | 265 | 88.2 | 118 | 1.41 | 11.3 | 22.6 |
| 174 | 345 | 172 | 259 | 86.2 | 115 | 1.38 | 11.0 | 22.1 |

Half-time and double-time: a 140 BPM half-time beat feels like 70; a 2 Hz pulse (~120 BPM) is the preferred-tempo centre (Moelants), so slow genres add 16th hats and fast genres use half-time snares to keep a ~2 Hz layer available.

### Swing math (MPC/Linn scale)

MPC swing S% delays every second 16th inside each 8th: the off-16th starts at `S/100 × (8th length)` instead of 50%.
- Delay in beats: `(S − 50)/100 × 0.5`. Ticks at PPQ 96: `(S − 50) × 0.48`.
- 54% → +1.9 ticks (loosens without sounding swung); 57% → +3.4; 60% → +4.8; 62% → +5.8; 66% → +7.7 (≈ triplet = 8 ticks); 70% → +9.6.
- 16th-note swing = apply to even steps (2, 4, 6...). 8th-note swing (boom bap kick/snare 57%) = delay the "&" 8ths (steps 3, 7, 11, 15) by `(S − 50)/100 × 1 beat`.
- FL Channel Rack swing is a different 0–100 scale with no verified mapping; start ~15–30% FL and match by ear; it only acts when **both** global and channel swing are > 0. Exact MPC values can be baked into MIDI with `swing16()` in `make_midi_template.py`.

### Other conversions

- FL velocity % → MIDI: `MIDI ≈ % × 1.27`; MIDI → %: `÷ 1.27`. Drum velocity bands (X/x/g) are in `music-drums-groove`.
- Microtiming: 10 ms at 90 BPM ≈ 6% of a 16th ≈ +6% in FL's step Shift (100% ≈ one 16th).
- Polymeter: a 12-step loop against 16 steps realigns every 3 bars (LCM 48 steps).
- Delay/reverb sync times = tempo-table values; send design is in `music-mix-master`.

Sources: Wikipedia (Scientific pitch notation, Interval, Mode, Circle of fifths, Borrowed chord); Plomp & Levelt 1965; Hooktheory 1,300-song analysis (hooktheory.com/blog); Attack Magazine Roger Linn interview; Image-Line Channel Rack manual.
