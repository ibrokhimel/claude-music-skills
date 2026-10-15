# Harmony for Modern Production: Scales, Modes, Keys, Chords, Voicings, Progressions

Conventions used throughout these notes:
- MIDI numbers use the scientific convention **C4 = 60 (middle C)**, A4 = 69 = 440 Hz. **FL Studio labels MIDI 60 as "C5"**, so FL's displayed octave = scientific octave + 1 (FL "C6" = MIDI 72, FL "C5" = 60, FL "C4" = 48, FL "C3" = 36). Formula: `MIDI = 12 * (sci_octave + 1) + pitch_class`; in FL terms `MIDI = 12 * FL_octave + pitch_class`.
- Pitch classes: C0 C#/Db1 D2 D#/Eb3 E4 F5 F#/Gb6 G7 G#/Ab8 A9 A#/Bb10 B11.
- Quick lookup: C2=36, C3=48, C4=60, C5=72; E1=28, A1=33, C1=24 (typical 808 territory).
- Voicings are written `bass | upper notes`.
- Anything labelled "Derived" is arithmetic computed from the cited formulas (not a quoted claim).

---

## 1. Pitch basics: notes, octaves, semitones, intervals, consonance/dissonance, enharmonics

### Takeaway
Twelve equal semitones per octave; an octave doubles frequency. Consonance tracks simple frequency ratios / coinciding harmonics (octave 2:1, fifth 3:2, fourth 4:3, major third 5:4), which is why fifths and octaves are safe low in the mix while seconds, sevenths and tritones create tension that "wants" to resolve. Octave-number conventions differ between manufacturers, so always reason in MIDI numbers.

### Cited Findings
- Scientific pitch notation names middle C as C4 (MIDI 60) and A4 = 440 Hz; octave numbering conventions vary between manufacturers/software (some label middle C as C3 or C5), which is why MIDI note numbers are the unambiguous reference — [Wikipedia: Scientific pitch notation](https://en.wikipedia.org/wiki/Scientific_pitch_notation)
- Consonance has historically been associated with simple numerical frequency ratios, with tonal fusion, and with the coincidence of partials (harmonics) of the two tones; dissonance with beating/roughness between close partials — [Wikipedia: Consonance and dissonance](https://en.wikipedia.org/wiki/Consonance_and_dissonance)
- Dissonant intervals create tension and a desire to resolve to consonant ones; the classification is style-relative (e.g., Renaissance theory counted only unisons, octaves, fifths, thirds and sixths as consonant; the perfect fourth was treated as dissonant against the bass; later styles accepted minor sevenths in context) — [Wikipedia: Interval (music)](https://en.wikipedia.org/wiki/Interval_(music))
- The dominant seventh's minor 7th approximates the "harmonic seventh" of the harmonic series, one reason it sounds fused rather than harsh — [Wikipedia: Consonance and dissonance](https://en.wikipedia.org/wiki/Consonance_and_dissonance)

### Inferences
Derived interval table (semitones / name / just ratio / role):

| st | Interval | Just ratio | Character / production use |
|---|---|---|---|
| 0 | unison P1 | 1:1 | doubling, layering |
| 1 | minor 2nd m2 | 16:15 | harshest; tension, horror, Phrygian "trap/drill" grind; resolve by step |
| 2 | major 2nd M2 | 9:8 | mild dissonance; sus2/add9 "air" |
| 3 | minor 3rd m3 | 6:5 | minor quality, dark/sad |
| 4 | major 3rd M3 | 5:4 | major quality, bright (ET third is ~14 cents sharp of 5:4) |
| 5 | perfect 4th P4 | 4:3 | open, hollow; sus4 |
| 6 | tritone TT (A4/d5) | 45:32 (~√2 in ET) | maximal instability; heart of V7; Lydian #4 / Locrian b5 |
| 7 | perfect 5th P5 | 3:2 | most stable after octave; power chords, bass+5 |
| 8 | minor 6th m6 / aug5 | 8:5 | bittersweet; b6 = Aeolian colour |
| 9 | major 6th M6 | 5:3 | warm, sweet; Dorian colour; "6" chords |
| 10 | minor 7th m7 | 16:9 or 9:5 (harmonic 7th 7:4) | bluesy, soft tension (dom7, m7) |
| 11 | major 7th M7 | 15:8 | dreamy/lush when voiced wide (maj7); harsh as a m2 if inverted |
| 12 | octave P8 | 2:1 | identity |
| 13/14 | b9 / 9 | — | b9 = dark tension (only on dominants); 9 = lush colour |
| 15/16 | #9 / 10th | — | #9 = "Hendrix"/bluesy; 10th = spread 3rd (best way to voice a 3rd low) |
| 17/18 | 11 / #11 | — | 11 on minor chords = soft; #11 on major = Lydian shimmer |
| 20/21 | b13 / 13 | — | b13 dark dominant colour; 13 = soulful dominant |

- Why it works (harmonic series): the overtones of C2 (MIDI 36) are approximately C2 36, C3 48, G3 55, C4 60, E4 64, G4 67, Bb4 70 (flat), C5 72, D5 74, E5 76, F#5 ~78, G5 79... Nature places wide intervals (octave, fifth) at the bottom and close intervals (thirds, seconds) at the top. Voicings that imitate this (wide low, close high) sound clear and "expensive"; voicings that invert it (close thirds/seconds in the bass) sound muddy. This is the physical basis of the low interval limit (section 4).
- Enharmonics: in 12-TET C#=Db, F#=Gb, B#=C, E#=F, Cb=B. They are the same MIDI number; spelling only matters for reading function (e.g., in the tritone sub Db7, the 7th is Cb, sounding as B = the 3rd of G7). A composer-AI can ignore spelling for MIDI output but should spell by function when explaining.
- Frequency anchors (derived from f = 440·2^((n−69)/12)): C1 (24) 32.7 Hz, E1 (28) 41.2 Hz, A1 (33) 55 Hz, C2 (36) 65.4 Hz, C3 (48) 130.8 Hz, C4 (60) 261.6 Hz.

### Gaps
- No single authoritative psychoacoustic ranking of interval consonance was retrieved; the table's "character" column reflects standard pedagogy rather than a cited study.

---

## 2. Scales and modes (formulas, characteristic notes, moods, genre usage)

### Takeaway
All seven diatonic modes are rotations of the major scale; each is identified by one "characteristic note" relative to major or natural minor. Modern beat genres lean minor: trap melodies overwhelmingly use natural minor, harmonic minor and Phrygian (semitone tensions), drill similarly with dark minor/harmonic-minor colour, while lo-fi, R&B and neo-soul favour Dorian and extended 7th/9th harmony.

### Cited Findings
- Modern Dorian = M2, m3, P4, P5, **M6**, m7 above the tonic (D–E–F–G–A–B–C on white keys) — [Wikipedia: Mode (music)](https://en.wikipedia.org/wiki/Mode_(music))
- Lydian = major scale with **raised 4th** (1 2 3 #4 5 6 7); Lydian (#4) and Locrian (b5) are the only modes with a tritone above the tonic — [Wikipedia: Lydian mode](https://en.wikipedia.org/wiki/Lydian_mode)
- Phrygian dominant = 5th mode of harmonic minor; intervals H, A2 (3 semitones), H, W, H, W, W; characteristic raised (major) 3rd versus ordinary Phrygian; also called Spanish Phrygian / Freygish / "Jewish scale"; used in flamenco, Middle Eastern and Jewish music — [Unison: Phrygian dominant](https://unison.audio/phrygian-dominant-scale/); [Wikipedia: Phrygian dominant scale](https://en.wikipedia.org/wiki/Phrygian_dominant_scale)
- Hungarian minor (double harmonic minor, Gypsy minor, harmonic minor #4) on C = C D Eb F# G Ab B: harmonic minor with raised 4th, adding a second augmented-second gap — [Wikipedia: Hungarian minor scale](https://en.wikipedia.org/wiki/Hungarian_minor_scale)
- Most trap melodies use one of three scales: natural minor, harmonic minor (raised 7th) and Phrygian (lowered 2nd, creating tension between degrees 2 and 1) — [Production Music Live: trap melody scales](https://productionmusiclive.com/blogs/news/trap-beat-guide-melodies-3-essential-scales-for-making-melodies)
- Trap producers favour Dorian, Phrygian, natural and harmonic minor, with focus on scale degrees a semitone apart for tension and a "spooky" sound (forum/community claim) — [Native Instruments community thread](https://community.native-instruments.com/discussion/2836/root-keys-and-scales-for-trap-lofi-beats-composition)
- Dorian is recommended for melodies over minor-7th chords (e.g., D Dorian over Dm7) in lo-fi/producer contexts — [SampleFocus: Dorian producer's guide](https://samplefocus.com/blog/the-dorian-scale-producers-guide/)
- UK drill is built on sparse minor-key melodies (≈138–145 BPM), with eerie melodies over suspended and diminished chords and orchestral textures — summarized from [Orphiq: Drill chords](https://orphiq.com/resources/drill-chords) and [Unison: how to make drill beats](https://unison.audio/how-to-make-drill-beats/) (via search summaries, pages not fully read)

### Inferences
Derived scale table (semitones from root; MIDI spelled on C4 = 60):

| Scale / mode | Formula (st) | On C (MIDI) | Characteristic note | Mood / typical use |
|---|---|---|---|---|
| Ionian (major) | 0 2 4 5 7 9 11 | 60 62 64 65 67 69 71 | natural 4 & 7 | bright, resolved; pop, house, EDM drops |
| Dorian | 0 2 3 5 7 9 10 | 60 62 63 65 67 69 70 | **M6** (A) | minor but hopeful/cool; lo-fi, neo-soul, funk, deep house, Daft-Punk-style grooves |
| Phrygian | 0 1 3 5 7 8 10 | 60 61 63 65 67 68 70 | **b2** (Db) | dark, menacing; trap, drill, metal, horror |
| Lydian | 0 2 4 6 7 9 11 | 60 62 64 66 67 69 71 | **#4** (F#) | floating, wonder; film/cinematic, dream-pop, future bass |
| Mixolydian | 0 2 4 5 7 9 10 | 60 62 64 65 67 69 70 | **b7** (Bb) | major but laid-back/bluesy; rock, funk, gospel vamps |
| Aeolian (natural minor) | 0 2 3 5 7 8 10 | 60 62 63 65 67 68 70 | **b6** (Ab) | sad/serious; trap, pop ballads, synthwave, epic |
| Locrian | 0 1 3 5 6 8 10 | 60 61 63 65 66 68 70 | **b5** (Gb) | unstable; rarely a home key; use for brief dread |
| Harmonic minor | 0 2 3 5 7 8 11 | 60 62 63 65 67 68 71 | **natural 7** (B) + A2 gap Ab–B | dramatic, "exotic"; trap/drill bells, cinematic |
| Melodic minor (jazz) | 0 2 3 5 7 9 11 | 60 62 63 65 67 69 71 | M6 + M7 | sophisticated minor; jazz/neo-soul |
| Phrygian dominant | 0 1 4 5 7 8 10 | 60 61 64 65 67 68 70 | b2 + M3 | flamenco/Middle-Eastern; trap/drill "eastern" leads |
| Hungarian minor | 0 2 3 6 7 8 11 | 60 62 63 66 67 68 71 | #4 + natural 7 | villainous, gothic; drill/horror/cinematic |
| Double harmonic major | 0 1 4 5 7 8 11 | 60 61 64 65 67 68 71 | b2 + natural 7 | "Arabic"/Byzantine colour |
| Major pentatonic | 0 2 4 7 9 | 60 62 64 67 69 | no half steps | can't-miss melodies; pop, country, future bass toplines |
| Minor pentatonic | 0 3 5 7 10 | 60 63 65 67 70 | no half steps | hip hop hooks, rock, R&B riffs; safe over any minor chord |
| Blues (minor) | 0 3 5 6 7 10 | 60 63 65 66 67 70 | b5 "blue note" | blues, boom bap, gospel licks |
| Major blues | 0 2 3 4 7 9 | 60 62 63 64 67 69 | b3→3 slide | soul, gospel, country |
| Whole-tone | 0 2 4 6 8 10 | 60 62 64 66 68 70 | all M2s | dreamlike, suspended, "flashback" |
| Diminished (half–whole) | 0 1 3 4 6 7 9 10 | 60 61 63 64 66 67 69 70 | symmetrical | over 7b9 chords; tension/suspense |
| Lydian dominant | 0 2 4 6 7 9 10 | 60 62 64 66 67 69 70 | #4 + b7 | over 7#11, tritone subs; "Simpsons"/fusion colour |

- Brightness ladder (each step flattens one note): Lydian → Ionian → Mixolydian → Dorian → Aeolian → Phrygian → Locrian. A composer-AI can "darken" or "brighten" a part by swapping one characteristic note (e.g., A natural minor → A Dorian by raising F to F#).
- Relative modes share notes; parallel modes share a tonic. Modal colour is only audible if the tonic is established (drone/bass pedal on the tonic, or a vamp that keeps returning to it), and if the characteristic note appears in chords or melody (e.g., Dorian vamp i–IV: Cm–F, where F major contains the Dorian A natural).
- Genre-to-scale map (synthesis of the cited sources plus standard practice): trap = natural minor, harmonic minor, Phrygian, occasional Phrygian dominant/Hungarian minor for "dark eastern" bells; drill = natural/harmonic minor with semitone (b2, b6→5) slides, often 3-note motifs; boom bap = minor pentatonic/blues, Dorian, jazz/soul samples; lo-fi/R&B/neo-soul = Dorian, major with maj7/9, melodic minor; pop = major/Aeolian with pentatonic hooks; house/deep house = Dorian and Aeolian m7/m9 stabs; future bass = major/Lydian with maj7/9; synthwave = Aeolian; cinematic = Aeolian, harmonic minor, Lydian (wonder), Phrygian (threat), whole-tone (mystery).

### Gaps
- No quantitative corpus statistics on scale/mode usage per genre (e.g., percentage of trap songs in minor) were found; genre-scale associations come from producer-education blogs and community posts, not measurement.

---

## 3. Keys, circle of fifths, relative/parallel keys, diatonic chords

### Takeaway
Adjacent keys on the circle of fifths differ by a single note, so moves between neighbours (and between relative major/minor) are smooth; diatonic chord qualities follow fixed patterns (major: I ii iii IV V vi vii°; natural minor: i ii° III iv v VI VII; harmonic minor adds a major V and vii°), which is the "palette" a progression generator should draw from.

### Cited Findings
- Each pitch can be the tonic of a major or minor key; the circle of fifths shows the number of sharps/flats per key signature, and major and minor keys sharing a signature are relative keys — [Wikipedia: Circle of fifths](https://en.wikipedia.org/wiki/Circle_of_fifths)
- Borrowed chords come from the parallel key (same tonic, other mode) — [Wikipedia: Borrowed chord](https://en.wikipedia.org/wiki/Borrowed_chord)
- Hooktheory's analysis of ~1300 popular-song sections found **C major / A minor** the most common keys by far (likely partly a transcription-normalisation artefact) and Bb only ~4% — [Hooktheory blog: 1300 songs](https://www.hooktheory.com/blog/i-analyzed-the-chords-of-1300-popular-songs-for-patterns-this-is-what-i-found/)

### Inferences
Circle of fifths (clockwise = +1 sharp / −1 flat):
`C(0) – G(1#) – D(2#) – A(3#) – E(4#) – B(5#) – F#/Gb(6) – Db(5b) – Ab(4b) – Eb(3b) – Bb(2b) – F(1b)`
Relative minors in the same order: `Am – Em – Bm – F#m – C#m – G#m – D#m/Ebm – Bbm – Fm – Cm – Gm – Dm`. Order of sharps F C G D A E B; flats B E A D G C F. Relative minor = major tonic − 3 semitones (C 60 → A 57).

Diatonic chords, **C major** (triads / 7ths, closed root-position MIDI):

| Deg | Triad | MIDI | 7th chord | MIDI | Function |
|---|---|---|---|---|---|
| I | C | 60 64 67 | Cmaj7 | 60 64 67 71 | tonic |
| ii | Dm | 62 65 69 | Dm7 | 62 65 69 72 | predominant |
| iii | Em | 64 67 71 | Em7 | 64 67 71 74 | tonic substitute (weak) |
| IV | F | 65 69 72 | Fmaj7 | 65 69 72 76 | predominant |
| V | G | 67 71 74 | G7 | 67 71 74 77 | dominant |
| vi | Am | 69 72 76 | Am7 | 69 72 76 79 | tonic substitute |
| vii° | Bdim | 71 74 77 | Bm7b5 | 71 74 77 81 | dominant (weak) |

Diatonic chords, **C minor** (natural minor; harmonic-minor alterations in brackets):

| Deg | Triad | MIDI | 7th chord | MIDI |
|---|---|---|---|---|
| i | Cm | 60 63 67 | Cm7 [Cm(maj7) 60 63 67 71] | 60 63 67 70 |
| ii° | Ddim | 62 65 68 | Dm7b5 | 62 65 68 72 |
| III | Eb | 63 67 70 | Ebmaj7 [Ebmaj7#5 63 67 71 74] | 63 67 70 74 |
| iv | Fm | 65 68 72 | Fm7 | 65 68 72 75 |
| v [V] | Gm [G 67 71 74] | 67 70 74 | Gm7 [G7 67 71 74 77] | 67 70 74 77 |
| VI | Ab | 68 72 75 | Abmaj7 | 68 72 75 79 |
| VII [vii°] | Bb [Bdim 71 74 77] | 70 74 77 | Bb7 [Bdim7 71 74 77 80] | 70 74 77 80 |

- Dorian minor (C Dorian) changes: IV becomes **F major** (65 69 72) and ii becomes Dm (62 65 69); vi° = Adim. The major IV in a minor key is the single most recognizable "Dorian/neo-soul" sound.
- Mixolydian (C Mixolydian) changes: v = Gm, and **bVII = Bb** (70 74 77) is diatonic — the rock/gospel "I–bVII–IV" sound.
- Relative vs parallel: relative (C major ↔ A minor) = same notes, different home; parallel (C major ↔ C minor) = same home, different notes. Borrowing (section 7) uses parallel keys; "minor loops that feel major" use relative keys.
- Choosing a key in production: for 808-heavy genres pick a key whose tonic lands where the sub sounds best (roughly E1–A1, MIDI 28–33, ~41–55 Hz, depending on the 808 sample), e.g., F minor, F# minor, G minor, A minor; this is a practical production heuristic, not a theory rule.

### Gaps
- The Hooktheory key statistics are dated and from a transcribed (possibly transposed) database; no current per-genre key distribution was found.

---

## 4. Chord construction, inversions and voicings (open/closed, drop-2, shell, spread, low interval limit)

### Takeaway
Chords are stacked thirds (with sus/add/altered variants); quality comes from the 3rd and 7th. Beauty in production comes mostly from **voicing**: keep the low register to roots/fifths/octaves, put thirds above roughly C3 (MIDI 48) and seconds/clusters above roughly E3–F3 (MIDI 52–53), drop the 5th and root from upper voices in rich chords, and voice-lead between chords rather than jumping root-position blocks.

### Cited Findings
- Low interval limits are guidelines giving the lowest register in which each interval can sound without becoming muddy; more consonant intervals (e.g., perfect fifth) can sit lower than dissonant ones (e.g., minor second); they are not absolute rules — [Robin Hoffmann: Low Interval Limits](https://www.robin-hoffmann.com/dfsb/low-interval-limits)
- How much mud a low voicing produces depends on dynamics and harmonic content: soft string voicings are more forgiving than loud brass — [Robin Hoffmann: Low Interval Limits](https://www.robin-hoffmann.com/dfsb/low-interval-limits)
- Low notes stacked close together lose clarity; the low-interval-limit concept defines how far apart bass notes must be (Sleepfreaks demonstrates a muddy low Cmaj7 vs a clear one, and notes horror scores may deliberately violate the limits) — [Sleepfreaks: Voicing, arpeggio, low interval limit](https://sleepfreaks-dtm.com/en/music-theory-beginner/voicing-arpeggio/)
- Arranging guidance surfaced in search: below the middle of the bass staff, keep intervals consonant, ideally 10ths, 5ths or octaves — [Robin Hoffmann](https://www.robin-hoffmann.com/dfsb/low-interval-limits) / [Evan Rogers: Voicings part 2](https://www.evanrogersmusic.com/blog-contents/big-band-arranging/voicings-part2) (search summary; exact attribution between the two not confirmed)
- Minor 9th chord on C = C Eb G Bb D (5 notes); the full m9 voicing transposed in parallel is a defining deep-house sound — [MusicRadar: deep house minor ninth chords](https://musicradar.com/how-to/how-to-create-deep-house-minor-ninth-chords) (via search summary)

### Inferences
**Chord formula table (semitones from root; on C = MIDI 60):**

| Symbol | Formula | On C (MIDI) | Colour |
|---|---|---|---|
| C (maj) | 0 4 7 | 60 64 67 | stable, bright |
| Cm | 0 3 7 | 60 63 67 | stable, dark |
| Cdim | 0 3 6 | 60 63 66 | tense, passing |
| Caug (+) | 0 4 8 | 60 64 68 | unresolved, dreamy/creepy |
| Csus2 | 0 2 7 | 60 62 67 | open, ambiguous |
| Csus4 | 0 5 7 | 60 65 67 | suspended; wants 4→3 |
| C5 (power) | 0 7 (12) | 48 55 60 | neutral, heavy; safe very low |
| C6 | 0 4 7 9 | 60 64 67 69 | vintage, sweet |
| Cm6 | 0 3 7 9 | 60 63 67 69 | noir, Dorian |
| Cadd9 | 0 4 7 14 | 60 64 67 74 | pop shimmer |
| Cm(add9) | 0 3 7 14 | 60 63 67 74 | sad-beautiful (trap/emo rap pianos) |
| C6/9 | 0 4 7 9 14 | 60 64 67 69 74 | open, final chord in neo-soul/jazz |
| Cmaj7 | 0 4 7 11 | 60 64 67 71 | lush, dreamy |
| C7 | 0 4 7 10 | 60 64 67 70 | dominant, bluesy |
| Cm7 | 0 3 7 10 | 60 63 67 70 | mellow minor |
| Cm(maj7) | 0 3 7 11 | 60 63 67 71 | spy/noir, tense minor |
| Cm7b5 (ø7) | 0 3 6 10 | 60 63 66 70 | ii in minor, yearning |
| Cdim7 (°7) | 0 3 6 9 | 60 63 66 69 | symmetrical, suspense, passing |
| C7sus4 | 0 5 7 10 | 60 65 67 70 | gospel/house suspended dominant |
| Cmaj9 | 0 4 7 11 14 | 60 64 67 71 74 | R&B/lo-fi tonic |
| C9 | 0 4 7 10 14 | 60 64 67 70 74 | funk/neo-soul dominant |
| Cm9 | 0 3 7 10 14 | 60 63 67 70 74 | deep house / neo-soul minor |
| Cm11 | 0 3 7 10 14 17 | 60 63 67 70 74 77 | airy minor (11 is consonant on minor) |
| Cmaj7#11 | 0 4 7 11 18 | 60 64 67 71 78 | Lydian shimmer, cinematic |
| C13 | 0 4 7 10 14 21 (omit 11) | 60 64 70 74 81 | gospel/neo-soul dominant |
| Cm13 | 0 3 7 10 14 21 | 60 63 70 74 81 | lush Dorian minor |
| C7b9 | 0 4 7 10 13 | 60 64 67 70 73 | dark dominant (to minor) |
| C7#9 | 0 4 7 10 15 | 60 64 67 70 75 | bluesy/funky dominant |
| C7#5 / C7b13 | 0 4 8 10 / 0 4 10 20 | 60 64 68 70 | dark, cinematic dominant |
| C7alt | 0 4 10 + b9/#9/#11/b13 | e.g. 60 64 70 75 80 | max tension before resolution |
| C/E (slash) | chord over non-root bass | 52 \| 60 64 67 | smooth bass lines (1st inversion) |
| Bb/C (slash) | triad over foreign bass | 48 \| 58 62 65 | = C9sus/C11 sound; gospel, house |

- Avoid-note heuristics: the natural 11 over a major or dominant chord clashes a minor 9th above the 3rd (use #11 instead); b9 belongs on dominant chords only; the 11 is fine on minor chords. When a chord has 5+ notes, drop the 5th first, then the root (bass already has it).
- **Inversions of C major:** root 60 64 67; 1st 64 67 72 (C/E); 2nd 67 72 76 (C/G). Seventh chords add a 3rd inversion (7th in bass, e.g., C7/Bb = 58 | 60 64 67 — strong pull down to F/A).
- **Closed vs open:** closed = all upper voices within an octave (60 64 67 71); open/spread = spaced over more than an octave (48 55 64 71 for Cmaj7: C3 G3 E4 B4) — open voicings sound bigger, are more piano/strings-like, and keep lows clear.
- **Drop-2:** take a closed 4-note voicing and drop the 2nd-highest note an octave. Cmaj7 closed 60 64 67 71 → drop-2 = 55 60 64 71 (G3 C4 E4 B4). Drop-3: 52 60 67 71. Drop-2 is the guitar/keys standard for smooth 4-voice comping.
- **Shell voicings:** root + 3rd + 7th (or root + 7th + 3rd). Cmaj7 shells: 48 52 59 (C3 E3 B3) or 48 59 64 (C3 B3 E4 — preferred, spread). G7 shell: 43 | 53 59 (G2 | F3 B3). Shells are the minimum for clear function; layer pads/extensions above.
- **Rootless (Bill Evans-style A/B) voicings** for when a bass/808 carries the root: Dm9 = 53 57 60 64 (F A C E); G13 = 53 57 59 64 (F A B E); Cmaj9 = 52 55 59 62 (E G B D). Note that a rootless Am9 (C E G B) equals Cmaj7 — the bass decides the chord name.
- **Quartal voicings** (stacked 4ths, e.g., D G C F = 62 67 72 77 over a C/Dm bass) give modern, modal, "So What"/neo-soul/ambient colour without strong major/minor identity.
- **Low interval limit — commonly reproduced arranging guideline (scientific octave numbers; lowest recommended position of the lower note):** m2 ≈ E3 (52), M2 ≈ Eb3 (51), m3 ≈ C3 (48), M3 ≈ Bb2 (46), P4 ≈ Bb2 (46), tritone ≈ B2 (47), P5 ≈ Bb1 (34), m6 ≈ G2 (43), M6/m7/M7 ≈ F2 (41), m9 ≈ E2 (40), M9 ≈ Eb2 (39), M10 ≈ Bb1 (34). Treat these as approximate (values reproduced from Berklee-style arranging pedagogy; the cited chart is an image that could not be machine-read, and sources differ slightly).
- **Practical production rules (derived):** (1) If an 808/sub plays the root, chord instruments should mostly live above ~C3 (MIDI 48) and should not double the sub's octave. (2) Below MIDI ~48, use only root, 5th, octave (power-chord territory). (3) Put 3rds/10ths around 48–60, 7ths/9ths above ~55, clusters (2nds) above ~60 for clarity. (4) Spread voicings (10ths in the left hand: C3–E4, 48–64) sound warmer than close 3rds low. (5) The top voice of a voicing is heard as melody — choose it deliberately and move it by step.

### Gaps
- Exact low-interval-limit values could not be verified in text form from a primary source (chart images only; one alternative source was inaccessible, HTTP 403); values above are approximate.

---

## 5. Functional harmony, tension/resolution, cadences

### Takeaway
Chords group into tonic (rest: I, vi, iii), predominant (departure: IV, ii) and dominant (tension: V, vii°) families; tension comes from the dominant's tritone (leading tone + 7th) resolving by semitones to the tonic. Cadences punctuate phrases: authentic (V–I) = full stop, half (–V) = comma, plagal (IV–I) = soft "amen", deceptive (V–vi) = surprise.

### Cited Findings
- Cadence terms: authentic/perfect cadence = V→I or V7→I; half/imperfect cadence ends on V; plagal = IV→I; deceptive/interrupted = V→vi (or other non-tonic) — [Wikipedia: Cadence](https://en.wikipedia.org/wiki/Cadence)
- A dominant seventh and its tritone substitute share the same 3rd and 7th (tritone), and in ii–V–I those guide tones descend by step (in C: F/C → F/Cb → E/B) — [Wikipedia: Tritone substitution](https://en.wikipedia.org/wiki/Tritone_substitution)
- Picardy third = ending a minor/modal section on a major tonic by raising the third — [Wikipedia: Picardy third](https://en.wikipedia.org/wiki/Picardy_third)
- In popular-song data, after the iii chord (E minor in C) the next chord was vi (Am) or IV (F) about 93% of the time; IV and V appear more often than I in the analysed sections — [Hooktheory blog: 1300 songs](https://www.hooktheory.com/blog/i-analyzed-the-chords-of-1300-popular-songs-for-patterns-this-is-what-i-found/)

### Inferences
- Why V7→I resolves (C major): G7 = G B D F (67 71 74 77). B→C rises a semitone (71→72), F→E falls a semitone (77→76): the tritone B–F collapses inward to the major third C–E. Root motion down a 5th (G→C) is the strongest root motion.
- Root-motion strength heuristic: down a 5th / up a 4th (strong, "forward"), down a 3rd (smooth, shares 2 notes), up a step (rock-like IV–V, bVI–bVII), up a 5th / down a 4th (retrogressive, softer, e.g., plagal, pop "IV–I").
- Cadences spelled in C (bass | upper):
  - Perfect authentic: G7 43 | 59 65 67 → C 48 | 60 64 67 (soprano lands on tonic 60/72).
  - Imperfect authentic: same, but soprano ends on E or G, or chords inverted — less final.
  - Half: … Dm 50 | 62 65 69 → G 43 | 62 67 71 (ends open; great for end of verse / pre-chorus).
  - Plagal: F 41 | 60 65 69 → C 48 | 60 64 67 (gospel "amen"; also the pop loop "IV–I"). Minor plagal: Fm 41 | 60 65 68 → C 48 | 60 64 67 — very emotional (borrowed iv).
  - Deceptive: G7 43 | 59 65 (B F) → Am 45 | 60 64 (C E) — the upper voices resolve exactly as in V7–I (B→C, F→E) but the bass steps G→A instead of falling to C: surprise, extends phrases.
  - Phrygian half cadence (minor): iv6→V, e.g., in A minor Dm/F 41 | 57 62 → E 40 | 56 59 64 — the bass semitone F→E is the "Andalusian/flamenco" pull.
  - Backdoor: Fm7–Bb7–C (iv7–bVII7–I) — a soft, soulful alternative to V–I (section 7).
- Loop-based genres (trap, drill, lo-fi, house) often **avoid** a clear authentic cadence so the loop never "ends" — the NI lo-fi article explicitly notes progressions that omit I or end on V7 to keep cycling (section 8). A composer-AI should reserve strong V7–I cadences for song endings, pre-chorus → chorus lifts, or R&B/gospel moments.

### Gaps
- No corpus statistic was found on how often modern hip hop loops contain a V→i cadence.

---

## 6. Voice leading: rules and why smooth voice leading sounds good

### Takeaway
Keep common tones, move other voices by the smallest interval (ideally semitone/whole tone), let the bass and top voice move in contrary motion where possible, and avoid parallel fifths/octaves in exposed textures. Smooth voice leading lets the ear hear several continuous "lines" rather than a series of jumping blocks, which is why it sounds polished.

### Cited Findings
- Common-practice conventions: melodic lines should be smooth (primarily stepwise/conjunct) and independent; leaps are approached/followed carefully; parallel fifths and octaves between voices are avoided because they reduce independence — [Wikipedia: Voice leading](https://en.wikipedia.org/wiki/Voice_leading)
- Teaching focuses on connecting adjacent harmonies because it underpins larger structural goals — [Wikipedia: Voice leading](https://en.wikipedia.org/wiki/Voice_leading)
- In ii–V–I with a tritone sub, guide tones (3rds/7ths) move down by semitone, illustrating minimal-motion voice leading — [Wikipedia: Tritone substitution](https://en.wikipedia.org/wiki/Tritone_substitution)

### Inferences
- Algorithm for a composer-AI ("nearest-voicing" rule): for each new chord, enumerate inversions/octave placements of its pitch classes within a target range (e.g., MIDI 52–76 for keys), and pick the one minimizing total semitone movement from the previous voicing, with penalties for (a) voices crossing, (b) parallel P5/P8 between outer voices, (c) intervals below the low interval limit, (d) top voice leaping more than a 4th unless intentional.
- Common-tone facts (derived): chords with roots a 3rd apart share 2 notes (C↔Am, C↔Em, F↔Dm); roots a 5th apart share 1 (C↔G, C↔F); roots a step apart share 0 (F↔G, Ab↔Bb) — move upper voices **contrary** to the bass for these.
- Example (C major I–vi–IV–V, top voice smooth): C 48 | 60 64 67 → Am 45 | 60 64 69 → F 41 | 60 65 69 → G 43 | 59 62 67 → back to C (59→60, 62→64, 67→67). Total upper-voice motion is just 1–3 semitones per change.
- Production-specific: in pads and synth chords, smooth voice leading also prevents audible "jumps" in filter/brightness; with glide/portamento synths it creates the legato chord-morph sound used in future bass and synthwave.
- Bass is the exception: bass may leap by 4ths/5ths (root motion) — the "independent" contrary motion against the top voice is what makes progressions feel strong.

### Gaps
- Perceptual explanations (auditory stream segregation, e.g., Huron's work) were not retrieved from a primary source in this session.

---

## 7. Colour techniques: modal interchange, secondary dominants, tritone subs, chromatic mediants, pedal points, modulation, Picardy third

### Takeaway
Most "beautiful/emotional" moments in modern production come from a small set of chromatic devices: the borrowed iv and bVI/bVII in major (bittersweet, epic), secondary dominants (forward pull), tritone subs and backdoor dominants (smooth chromatic bass), chromatic mediants (cinematic "wonder"), pedal points (tension over a static bass), and the Picardy third (sudden light).

### Cited Findings
- Borrowed chords (modal interchange) are taken from the parallel key; the backdoor progression's bVII7 is borrowed from the parallel minor; common rock progressions are built from borrowed chords — [Wikipedia: Borrowed chord](https://en.wikipedia.org/wiki/Borrowed_chord)
- Backdoor progression = iv7–bVII7–I (in C: Fm7–Bb7–C), a jazz alternative to ii–V–I — [Wikipedia: Backdoor progression](https://en.wikipedia.org/wiki/Backdoor_progression)
- Secondary chords temporarily tonicize a degree other than the tonic (e.g., V/V); a secondary ii–V such as Am7–D7–G in C (ii7/V–V/V–V) — [Wikipedia: Secondary chord](https://en.wikipedia.org/wiki/Secondary_chord)
- Tritone substitution replaces V7 with bII7 (Db7 for G7 in C); it works because both share the same tritone (3rd and 7th); in Dm7–Db7–Cmaj7 the bass moves chromatically D–Db–C — [Wikipedia: Tritone substitution](https://en.wikipedia.org/wiki/Tritone_substitution)
- Chromatic mediants: chords with roots a third apart related chromatically; conservative definition requires same quality (C major ↔ E, A, Eb, Ab major) sharing one common tone; a broader definition also includes opposite-quality "doubly chromatic" mediants with no common tones (C major ↔ Eb minor, Ab minor) — [Wikipedia: Chromatic mediant](https://en.wikipedia.org/wiki/Chromatic_mediant)
- Pedal point = sustained tone, typically in the bass, against which harmonies change, including some dissonant to it — [Wikipedia: Pedal point](https://en.wikipedia.org/wiki/Pedal_point)
- Picardy third: major tonic ending a minor/modal section by raising the third — [Wikipedia: Picardy third](https://en.wikipedia.org/wiki/Picardy_third)
- I–V–bVII–IV variation replaces vi with bVII, giving two stacked I–V pairs a whole step apart and a bluesy flavour — [Wikipedia: I–V–vi–IV progression](https://en.wikipedia.org/wiki/I%E2%80%93V%E2%80%93vi%E2%80%93IV_progression)

### Inferences
Spelled examples in **C major** (bass | upper, MIDI):
- **Borrowed iv** (minor plagal, "tears"): F 41 | 60 65 69 → **Fm 41 | 60 65 68** → C 48 | 60 64 67. The A→Ab→G semitone line is the emotional engine.
- **bVI and bVII** (epic/heroic, "Mario cadence" bVI–bVII–I): **Ab 44 | 60 63 68** → **Bb 46 | 62 65 70** → C 48 | 64 67 72. Used for triumphant endings, film trailers, synthwave and EDM build resolutions.
- **bIII** (rock/soul colour): Eb 39 | 58 63 67. **ii°/iiø7 from minor**: Dm7b5 38 | 56 60 65 → G7 → C.
- **Secondary dominants** in C: V/V = **D7** 50 | 54 57 60 (D F# A C) → G; V/vi = **E7** 40 | 56 59 62 (G# B D) → Am; V/ii = **A7** 45 | 55 61 64 (G C# E) → Dm; V/IV = **C7** 48 | 58 64 67 → F. The added sharp (F#, G#, C#) is a leading tone to the target root — R&B and gospel love I–E7–Am, and "I–V/vi–vi".
- **Secondary ii–V chains** (neo-soul / jazz turnaround): Cmaj7 – A7 – Dm7 – G7 (I–VI7–ii–V) — matches the "classic turnaround" listed in lo-fi guidance ([Audeobox lo-fi in FL Studio](https://www.audeobox.com/learn/fl-studio/how-to-make-lofi-beats-in-fl-studio/)).
- **Tritone sub** in C: Dm9 38 | 53 57 60 64 → **Db9(#11)** 37 | 53 55 59 63 (F G Cb Eb = 3rd, #11, b7, 9; Cb sounds as B) → Cmaj9 36 | 52 55 59 62. Chromatic bass D–Db–C is the signature slinky R&B/neo-soul move.
- **Chromatic mediants** (cinematic): C 48 | 60 64 67 → **E 52 | 59 64 68** (common tone E; C→B, G→G#) → back to C; or C → **Ab 44 | 60 63 68** (common tone C). Minor-key film staple: **Am → F → Dm... or i → bVI → (major) VI**; "Hans Zimmer-style" alternation i ↔ bVI over a pedal. Use for "wonder", "reveal", sci-fi, heroic lifts.
- **Pedal point**: tonic bass C2 (36) held while upper chords move C (60 64 67) → Bb/C (58 62 65) → Ab/C (60 63 68) → Bb/C → C. Tension builds without changing the 808/bass note — ideal for trap/drill (808 stays on the root), house (organ/bass pedal) and film builds. Dominant pedal (G in bass under C, F, Dm/G) builds anticipation before a drop.
- **Modulation** options: (1) pivot chord — find a chord diatonic to both keys (Am is vi in C and ii in G) and continue in G; (2) secondary-dominant entry — play the new key's V7 (D7 → G); (3) direct/"truck-driver" key change up a semitone or whole tone for the last chorus (e.g., C → Db: bass 48 → 49), optionally preceded by the new key's V (Ab7); (4) relative switch — verse in A minor, chorus in C major using the same notes (feels like the sun comes out); (5) parallel switch — verse in C minor, chorus in C major.
- **Picardy third** in A minor: … E 40 | 56 59 64 → **A major 45 | 57 61 64** (C# instead of C) as the final chord — hopeful ending for sad pieces, intros/outros in cinematic and lo-fi.
- **Line clichés** (descending chromatic inner voice over a static chord): Am 57 60 64 → Am(maj7) 56 60 64 → Am7 55 60 64 → Am6 54 60 64 — instant film-noir/James Bond/R&B sophistication without changing the bass.
- **Sus resolution**: Csus4 60 65 67 → C 60 64 67; G7sus4 → G7 → C — gospel, house and pop "lift" moments.

### Gaps
- No quantitative data on how often each borrowed/chromatic chord appears in hip hop or EDM specifically; Hooktheory Trends data (75,000+ songs) exists but the interactive statistics did not render in a static fetch ([Hooktheory Trends](https://www.hooktheory.com/trends)).

---

## 8. The most-used progressions, emotional character, spelled in concrete keys

### Takeaway
A handful of loops cover most modern music: the four-chord axis family (I–V–vi–IV and its rotations), minor four-chord loops (i–VI–III–VII, i–VI–VII), ii–V–I with extensions (R&B/lo-fi/neo-soul), descending tetrachords (Andalusian), the 12-bar blues, and the Japanese "royal road" IV–V–iii–vi. Each can be re-coloured with 7ths/9ths, inversions and borrowed chords.

### Cited Findings
- I–V–vi–IV ("Axis progression") is ubiquitous in pop, demonstrated by the Axis of Awesome's "Four Chords" medley (2008); rotations include vi–IV–I–V and IV–I–V–vi (e.g., Rihanna "Umbrella", Jay Sean "Down"); a common variant substitutes ii for vi (I–V–ii–IV: The Cure "Just Like Heaven", Smash Mouth "All Star", Semisonic "Closing Time") — [Wikipedia: I–V–vi–IV progression](https://en.wikipedia.org/wiki/I%E2%80%93V%E2%80%93vi%E2%80%93IV_progression)
- Andalusian cadence = four chords descending stepwise, i–bVII–bVI–V in minor (iv–III–II–I in Phrygian), traceable to the Renaissance; pop examples include "Stray Cat Strut", "Good Vibrations", "Happy Together"; "Walk, Don't Run" uses its bass line but starts on A major — [Wikipedia: Andalusian cadence](https://en.wikipedia.org/wiki/Andalusian_cadence)
- Royal road (ōdō shinkō) = IVmaj7–V7–iii7–vi, a staple of contemporary J-pop; also called the koakuma ("little devil") progression by producer Seiji Kameda, who likened the move from the major V to the minor iii to a moment of playful heartbreak; Rachmaninoff's Symphony No. 2 uses IV–V7–iii–vi–ii7–V7–I — [Wikipedia: Royal road progression](https://en.wikipedia.org/wiki/Royal_road_progression)
- 12-bar blues "quick-change" variant: I IV I I | IV IV I I | V IV I I — [Wikipedia: Twelve-bar blues](https://en.wikipedia.org/wiki/Twelve-bar_blues)
- Lo-fi staples (in C/Am): Cmaj7–Am7 (I–vi; cyclical, unresolved "floating"), Dm7–Am7–Dm7–Am7–C (iv–i… with passing III), C–Em–Am–G (I–iii–vi–V), Fmaj7–Em7–Am7 (IV–iii–vi; no tonic so it never resolves), Am7–F–E7 (i–VI–V7; dominant restarts the loop instead of resolving) — [Native Instruments blog: lo-fi chord progressions](https://blog.native-instruments.com/lo-fi-chord-progressions/)
- Additional lo-fi/jazz progressions: Dm9–G13–Cmaj9–Am7 (late-night), Am7–Dm7–Gmaj7–Cmaj7 (cycle of fourths), Cmaj7–A7–Dm7–G7 (turnaround) — [Audeobox: lo-fi beats in FL Studio](https://www.audeobox.com/learn/fl-studio/how-to-make-lofi-beats-in-fl-studio/)
- The jazz ii–V–I (Dm7–G7–Cmaj7) is cited as the most common lo-fi progression, alongside I–vi–ii–V and I–vi–IV–V in 7ths — [eMastered: lofi chord progressions](https://emastered.com/blog/lofi-chord-progressions) (via search summary)
- Trap staples: i–VI–v–i and i–v–iv (e.g., Cm–Ab–Gm–Cm; Cm–Gm–Fm; Am–F–Em–Am), with the major VI giving lift before falling back; the article associates this family with Future's "Mask Off" — [eMastered: trap chord progressions](https://emastered.com/blog/trap-chord-progressions)
- UK drill progressions: i–v–VI (Cm–Gm–Ab, tense/circular), i–VII–VI (Cm–Bb–Ab, descending/cinematic), i–iv–VII–III (Cm–Fm–Bb–Eb, darker, wider) — [Orphiq: drill chords](https://orphiq.com/resources/drill-chords) (via search summary)

### Inferences
All spelled as `bass | upper` with smooth voice leading (derived).

1. **I–V–vi–IV (C major)** — uplifting, anthemic, "everyone knows it" (pop, EDM, future bass, country).
   C 48 | 60 64 67 → G 43 | 59 62 67 → Am 45 | 60 64 69 → F 41 | 60 65 69
2. **vi–IV–I–V (A minor feel / C major)** — melancholic-hopeful, "emotional pop/EDM/rap hook".
   Am 45 | 60 64 69 → F 41 | 60 65 69 → C 48 | 60 64 67 → G 43 | 59 62 67
   With 7ths/9ths (future bass/lo-fi): Am9 45 | 59 60 64 67 → Fmaj9 41 | 57 60 64 67 → Cadd9 48 | 55 62 64 67 → G6 43 | 55 59 62 64
3. **IV–I–V–vi (C)** — "Umbrella"-type rotation, starts open/lifted: F 41 | 60 65 69 → C 48 | 60 64 67 → G 43 | 59 62 67 → Am 45 | 60 64 69
4. **ii–V–I (C) with neo-soul extensions** — warm, sophisticated, resolved.
   Dm9 38 | 53 57 60 64 → G13 43 | 53 57 59 64 → Cmaj9 36 | 52 55 59 62 (only 1–2 voices move per change)
   Minor ii–V–i (C minor): Dm7b5 38 | 53 56 60 → G7b9 43 | 53 56 59 (F Ab B) → Cm9 36 | 51 55 58 62
5. **I–vi–ii–V turnaround (C)**: Cmaj7 48 | 52 55 59 → Am7 45 | 52 55 60 → Dm7 38 | 53 57 60 → G7 43 | 53 59 62 (secondary version: A7 45 | 55 61 64 for vi)
6. **i–VI–III–VII (C minor)** — epic, yearning, "anthem in minor" (pop, EDM, synthwave, trap melodies).
   Cm 48 | 60 63 67 → Ab 44 | 60 63 68 → Eb 39 | 58 63 67 → Bb 46 | 58 62 65 (A-minor version: Am F C G — same shapes as #2 but felt as minor home)
7. **i–iv–v / i–iv–V (A minor)** — dark, folk/blues, classic minor; harmonic-minor V adds drama.
   Am 45 | 57 60 64 → Dm 50 | 57 62 65 → Em 52 | 59 64 67 (or E 52 | 56 59 64 with G#) → Am
8. **i–bVI–bVII(–i) (C minor)** — heroic, cinematic, rock/epic trap; "Mario cadence" when it lands on major I.
   Cm 48 | 60 63 67 → Ab 44 | 60 63 68 → Bb 46 | 62 65 70 → Cm 48 | 63 67 72 (or C major 48 | 64 67 72 for a Picardy/Mario finish)
9. **Andalusian cadence i–bVII–bVI–V (A minor)** — dramatic, Spanish/flamenco, fateful.
   Am 45 | 60 64 69 → G 43 | 59 62 67 → F 41 | 60 65 69 → E 40 | 59 64 68 → (Am)
   Trap/drill version in C minor: Cm 36 | 60 63 67 → Bb 34 | 58 62 65 → Ab 32 | 60 63 68 → G 31 | 59 62 67 (808 slides down the tetrachord C–Bb–Ab–G)
10. **12-bar blues (C), dominant 7ths, guide-tone shells** — boom bap, funk, soul samples.
    Bars: C7 C7 C7 C7 | F7 F7 C7 C7 | G7 F7 C7 G7 (quick-change: bar 2 = F7)
    C7 48 | 58 64 (Bb E) → F7 41 | 57 63 (A Eb) → G7 43 | 59 65 (B F): guide tones move by semitone.
11. **Royal road IVmaj7–V7–iii7–vi (C)** — bittersweet, nostalgic, anime/J-pop/future bass.
    Fmaj7 41 | 57 60 64 → G7 43 | 59 62 65 → Em7 40 | 59 62 67 → Am7 45 | 60 64 67 (optionally → Dm7–G7–C as Rachmaninoff/J-pop extension)
12. **Dorian vamp i7–IV7/IV9 (C Dorian)** — cool, groovy, hopeful-minor (neo-soul, funk, deep house, lo-fi).
    Cm9 36 | 51 55 58 62 → F9 41 | 51 55 57 60 (Bb→A is the Dorian natural 6; D→C)
13. **Trap i–VI–v (C minor)** — dark with a lift: Cm 36 | 60 63 67 → Ab 44 | 60 63 68 → Gm 43 | 58 62 67 → Cm
14. **Drill i–v–VI / i–VII–VI (C minor)**: Cm 36 | 60 63 67 → Gm 43 | 58 62 67 → Ab 44 | 60 63 68; Cm → Bb 34 | 58 62 65 → Ab 32 | 60 63 68. Add a harmonic-minor G major (59 B) or Ddim/Bdim stab for menace.
15. **Lo-fi I–vi (C)**: Cmaj9 48 | 52 55 59 62 → Am9 45 | 55 59 60 64 — two chords, endless.
16. **IV–iii–vi (C), no tonic**: Fmaj7 41 | 57 60 64 → Em7 40 | 55 59 62 → Am7 45 | 55 60 64 — floating, unresolved.
17. **Minor plagal / borrowed iv pop ballad (C)**: C → Fm → C (see section 7) or I–IV–iv–I: C 48 | 60 64 67 → F 41 | 60 65 69 → Fm 41 | 60 65 68 → C.
18. **Deep house m9 stab chain (A minor)**: Am9 45 | 60 64 67 71 → Dm9 50 | 60 64 65 69 (keep the shape or voice-lead) → or parallel-shifted shape (same intervals moved by a 4th/5th, "chord memory" style).
19. **Backdoor (C)**: Fm7 41 | 56 60 63 → Bb7 46 | 56 62 65 → Cmaj7 48 | 55 59 64 — soulful, Stevie-Wonder-ish landing.
20. **Gospel/R&B "1–4–5 with passing" (C)**: Cmaj9 → C7/E (52 | 58 60 64) → Fmaj7 → F#dim7 (42 | 57 60 63) → C/G (43 | 60 64 67) → A7 → Dm9 → G13 — chromatic bass walk-ups are the R&B fingerprint.

Emotional cheat sheet (derived): major I-based loops = optimistic; starting on vi or i = melancholic; ending loop on V/V7 = restless/forward; ending on IV = open/floating; any borrowed iv/bVI = bittersweet/nostalgic; bVI–bVII–I = triumphant; chromatic mediant = awe/mystery; b2 (Phrygian) or Ab–G semitone in C minor = menace; maj7/9 colours = warmth, nostalgia, "late night".

### Gaps
- Hooktheory's current "Popular Progressions" rankings (from its 80k-song database) did not render in static fetch; therefore no up-to-date ranking with percentages is included.
- "Mask Off" attribution to i–VI–v comes from a producer blog; the actual sample's harmony was not independently verified.

---

## 9. Genre harmony tendencies

### Takeaway
Hip hop sub-genres keep harmony narrow and loop-based (2–4 chords, minor, dark colours, tension without resolution); R&B/neo-soul/lo-fi are where extended chords, ii–V motion and chromatic bass lines live; pop and EDM rely on the four-chord axis family with big voicings; house uses m7/m9 stabs and Dorian vamps; cinematic uses modal mixture, chromatic mediants and pedals.

### Cited Findings
- Trap: built on minor keys, with the VI (major) giving "unexpected lift before falling into darker territory"; progressions keep the beat front and centre; used by producers for artists like Metro Boomin, Future, Travis Scott — [eMastered: trap chord progressions](https://emastered.com/blog/trap-chord-progressions)
- Trap melodies: natural minor, harmonic minor, Phrygian; simple question/answer (A/B) phrase structure; 2nd, 4th and 6th scale degrees generate the most tension — [Production Music Live: trap scales](https://productionmusiclive.com/blogs/news/trap-beat-guide-melodies-3-essential-scales-for-making-melodies)
- Drill: minor keys, sparse voicings, dark choices; UK drill favours eerie melodies over sus and diminished chords with orchestral textures; harmonic language is "narrow on purpose", creating tension and atmosphere rather than resolution; sliding 808s tuned to the melody's root notes (often in keys like A minor or G minor) — [Orphiq: drill chords](https://orphiq.com/resources/drill-chords); [Beatstorapon: how to make a drill beat](https://beatstorapon.com/blog/how-to-make-a-drill-beat/) (via search summaries)
- Lo-fi: few chords repeated cyclically, little traditional resolution, 7th extensions for sophistication; add 9ths/11ths once comfortable — [Native Instruments blog](https://blog.native-instruments.com/lo-fi-chord-progressions/)
- Lo-fi chords use maj7, m7, dominant 9ths with loose timing and warm, filtered tones — [eMastered: lofi chord progressions](https://emastered.com/blog/lofi-chord-progressions) (via search summary)
- Deep house: dusty stabs, jazzy minor 9ths, warm 7ths, classic organ/piano voicings; full 5-note m9 transposed in sequence defines the deep-house vibe — [MusicRadar: deep house minor ninth chords](https://musicradar.com/how-to/how-to-create-deep-house-minor-ninth-chords); [Mode Audio: house chords](https://modeaudio.com/magazine/turn-any-synth-into-a-deep-house-chord) (via search summary)
- Future bass uses 7th/9th extended chords for a richer feel — [Unison: future bass chord progressions](https://unison.audio/future-bass-chord-progressions/); [PML: future bass chords](https://www.productionmusiclive.com/blogs/news/12-tips-for-writing-future-bass-chords-and-melodies) (via search summary)
- Neo soul is rooted in jazz-influenced, extended harmony within R&B/hip hop — [Wikipedia: Neo soul](https://en.wikipedia.org/wiki/Neo_soul)
- Royal road progression is a J-pop/anime staple — [Wikipedia: Royal road progression](https://en.wikipedia.org/wiki/Royal_road_progression)

### Inferences
| Genre | Typical key/scale | Chord vocabulary | Signature moves | Notes for a composer-AI |
|---|---|---|---|---|
| Trap | natural/harmonic minor, Phrygian; often keys with sub-friendly roots (F–A minor) | minor triads, m(add9), sus2, occasional dim / harmonic-minor V | i–VI–v, i–iv, i–VI–VII, Andalusian; b2/b6 semitone motifs; bell/pluck arps | 2–4 chord loops over 8 bars; melody carries harmony; keep chords above MIDI ~48 so the 808 owns the low end |
| Drill (UK/NY) | natural/harmonic minor, Phrygian, Hungarian minor | sparse triads, sus, dim, orchestral strings/choir | i–v–VI, i–VII–VI, i–iv–VII–III; descending semitone lines; sliding 808 following roots | very sparse; tension over resolution; 140–145 BPM half-time feel |
| Boom bap | minor/Dorian, blues | sampled jazz/soul chords, m7, 9, 7#9 | 1–2 chord loops, ii–V fragments, blues | harmony usually from samples: chop 2-bar loops; dusty 7ths/9ths |
| Lo-fi | major/Dorian | maj7, m7, 9, 11, 13, 6/9 | ii–V–I, I–vi, IV–iii–vi, I–VI7–ii–V | loose timing, rolled chords, few chords, avoid hard cadences |
| R&B / neo-soul | Dorian, major, melodic minor | m9, m11, maj9, 13, 7#9, slash chords, quartal | tritone subs, backdoor iv–bVII, chromatic walk-ups, secondary dominants, ii–V chains | voice-lead every chord; rootless voicings over separate bass; anticipations |
| Pop | major (or Aeolian) | triads, add9, sus, occasional borrowed iv/bVI | I–V–vi–IV family, IV–I–V–vi, i–VI–III–VII; key change last chorus | big, simple, clear; 1 chord per bar |
| House / deep house | Dorian/Aeolian minor | m7, m9, m11, 7sus4, organ/piano stabs | parallel m9 stabs, Dorian i–IV vamp, 2-chord loops, tonic pedal | chord memory (same shape transposed), offbeat stab rhythm |
| EDM / future bass | major/Lydian, Aeolian | maj7, maj9, add9, sus2/4, supersaw stacks | I–V–vi–IV, IV–V–iii–vi (royal road), vi–IV–I–V | wide voicings, pitch-bent "chord chops", sidechained swells |
| Synthwave | Aeolian | triads, add9, sus | i–VI–III–VII, i–bVI–bVII, bVI–bVII–i | arpeggiated chords, pedal bass, 80s brightness on minor |
| Cinematic / epic | Aeolian, harmonic minor, Lydian, Phrygian | triads (power), sus, maj7#11, add9 | i–bVI–bIII–bVII, chromatic mediants, pedal points, Picardy endings | slow harmonic rhythm, ostinato over pedal, big orchestral spacing following the harmonic series |

### Gaps
- No primary-source genre corpus (e.g., chord statistics restricted to trap/drill) was located. Synthwave and cinematic tendencies above rest on standard practice rather than retrieved citations; the chromatic-mediant/film association is documented in general (Wikipedia chromatic mediant) but specific film-composer usage claims were not verified.

---

## 10. Harmonic rhythm and chord rhythm/comping patterns

### Takeaway
Harmonic rhythm (how often chords change) is relative and stylistic: loop-based hip hop and lo-fi change slowly (one chord per bar or per two bars, short loops), pop typically changes once per bar, jazz/neo-soul ii–Vs often change twice per bar, and cinematic music can sit on one chord or pedal for many bars. Faster harmonic rhythm adds momentum (pre-chorus/turnarounds); slower lets melody and drums lead.

### Cited Findings
- Harmonic rhythm is the rate at which chords change; "fast" or "slow" is relative and analysts compare pace and variation between and within pieces; e.g., Bach's C-major Prelude (BWV 846) keeps a steady one chord per measure while the surface rhythm is much faster; Classical-era music varies harmonic rhythm more than Baroque even with simpler harmony — [Wikipedia: Harmonic rhythm](https://en.wikipedia.org/wiki/Harmonic_rhythm)
- Lo-fi chords are commonly played with loose timing — [eMastered: lofi chord progressions](https://emastered.com/blog/lofi-chord-progressions) (via search summary)
- Drill sliding 808s are automated/pitch-bent between notes, typically hitting on beats 2 and 4 of the bar (claim from a producer blog) — [Beatstorapon: drill beat guide](https://beatstorapon.com/blog/how-to-make-a-drill-beat/) (via search summary)

### Inferences
Typical harmonic-rhythm defaults (derived from common practice; use as starting points):

| Genre | Tempo (typical) | Chord changes | Loop length |
|---|---|---|---|
| Trap | 130–160 BPM (half-time feel) | 1 chord per 1–2 bars (often per 2 bars at fast tempos) | 2–4 chords → 4–8 bars |
| Drill | 138–145 BPM | 1 chord per bar or 2 bars; sometimes 2 chords per bar in fills | 4–8 bars |
| Boom bap | 85–95 BPM | sample loop 1–2 bars; 1–2 chords per bar | 1–4 bars |
| Lo-fi | 70–90 BPM | 1 chord per bar (sometimes 2) | 2–4 bars |
| R&B / neo-soul | 60–100 BPM | 1–2 chords per bar, plus passing chords | 4–8 bars |
| Pop | 90–130 BPM | 1 chord per bar; doubling speed in pre-chorus | 4 bars (axis loop) |
| House / deep house | 118–126 BPM | 1 chord per 1–2 bars | 2–8 bars |
| Future bass / EDM | 128–160 BPM | 1 chord per bar (drop), slower in breakdown | 4–8 bars |
| Cinematic | free | 1 chord per 2–8 bars, or static pedal | phrase-based |

Comping/rhythm patterns (MIDI-friendly, 4/4, 16 steps per bar):
- **Sustained pad / whole note**: chord on step 1, length 16 (trap pads, cinematic). Overlap/legato into next chord for pads.
- **Pop pulse**: 8th-note chords (steps 1,3,5,…,15) or "1, 2&, 4" anticipations; push the chord change a 16th or 8th early (anticipation) to create urgency in choruses.
- **R&B/neo-soul anticipation**: play the next bar's chord on the "4&" (step 15) of the previous bar; roll chords (strum 10–30 ms bottom-to-top); ghost voicings/grace-note slides into chords.
- **Lo-fi**: whole-note or half-note chords, humanized (±10–30 ms timing, velocity 60–90), slight late placement ("behind the beat"), occasional swing 55–60%.
- **House stab**: short chord on the off-beat 8ths (steps 3, 7, 11, 15), or the "and of 2 / and of 4"; classic Chicago/deep house rhythmic chord patterns mix 8th and dotted-8th placements.
- **Future bass**: supersaw chord on downbeat, then rhythmic chops (16th/8th gated, sidechained), with pitch-bend swells into chord changes.
- **Trap/drill keys**: chords often replaced by arpeggios or bell melodies outlining the chord tones (1-5-8-b3-5 patterns), with the chord change marked by the 808 root note.
- **Ballad/cinematic piano**: left hand root–5th–octave (e.g., 36 43 48) arpeggio, right-hand close voicing on top; strings sustain spread voicings following the harmonic series.
- Harmonic-rhythm design tips: (1) change chords where the drums are strongest (bar downbeat), (2) accelerate harmonic rhythm into a section change (two chords per bar in the last bar of a pre-chorus), (3) hold one chord (or a pedal) during builds so tension comes from rhythm/filter rather than harmony, (4) let the melody move faster than the chords — melody notes on strong beats should usually be chord tones, passing tones on weak beats.

### Gaps
- No measured, sourced statistics on chord-change rates per genre were found; the tempo and change-rate table is a practitioner synthesis, not cited data.
- Swing percentages and humanization values are common producer defaults, not sourced from a retrieved study.
