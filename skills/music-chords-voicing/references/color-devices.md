# Chromatic colour devices and the surprise budget

This file covers the small set of chromatic moves that create most of the "emotional" moments in modern music, each spelled in MIDI, with when to use it and how much surprise it spends. Pitches use C4 = 60 (FL Studio shows "C5"). Spellings are `bass | upper`, written in C major unless noted, and were checked by script.

## Contents
1. The surprise budget (why one device per context)
2. Genre baselines: what counts as a surprise
3. Device catalogue: modal interchange, secondary dominants, tritone sub, chromatic mediants, pedals, line cliché, sus, Neapolitan, Picardy, planing
4. Modulation routes
5. Placement recipes
6. Sources

---

## 1. The surprise budget

- **The evidence (sourced):** Cheung et al. (2019) modelled about 80,000 Billboard chords. Pleasure was highest for a **surprising chord in a low-uncertainty context**, and for an **expected chord after a high-uncertainty context**. Huron's ITPRA theory explains why a surprise that is quickly reappraised as "fine" feels good (contrastive valence).
- **The rule (derived):** spend **one surprise per predictable context.**
  - A predictable context is about 4–8 bars, or 2–3 passes of a loop.
  - After an ambiguous or wandering passage, land on the expected chord: tonic, a plain triad, a downbeat.
  - **Never stack surprises.** Don't put a borrowed chord, a melody leap and a drum dropout on the same bar.
  - Save the biggest twist (a key change, or a chromatic mediant into the final chorus) for late in the song.
- **Coordinate with the melody:** if the melody spends its surprise on a bar (a big leap or a borrowed note, see `music-melody-hooks`), keep the harmony diatonic there, and the reverse.
- Surprise is measured against the listener's genre model, so check the baseline below before choosing a device.

## 2. Genre baselines: what counts as a surprise (inference, convention)

| Genre | Normal (no surprise) | Mild surprise | Big surprise |
|---|---|---|---|
| Pop | I, IV, V, vi, add9, sus | iv, bVII, bVI, V/vi (E7 in C) | key change up 1–2 semitones for the last chorus; chromatic mediant |
| Rock | I, IV, V, bVII, bIII, power chords | iv, bVI | chromatic mediant, Picardy |
| Trap / drill | i, iv, v, VI, VII, m(add9), sus | harmonic-minor V, a dim stab, b2 over the pedal | a major chord outside VI/VII, Picardy major tonic |
| Lo-fi / R&B / neo-soul | 7ths to 13ths, ii–V, rootless voicings | secondary dominant, tritone sub, backdoor | line cliché under a static chord, modulation up a minor 3rd |
| House / deep house | 2-chord m7/m9 vamp, pedal bass | borrowed chord in the breakdown, new bass note under the same stab | key lift after the breakdown |
| EDM / trance / future bass | I–V–vi–IV family, i–VI–III–VII | bVI–bVII–I into the drop, sus held one bar long | +1/+2 semitone key lift in the last drop **(sourced as trance convention, Orphiq summary)** |
| Cinematic | triads, pedals, i–bVI | chromatic mediant, Lydian #4 | Picardy, chromatic mediant on the reveal, silence then tutti |

## 3. Device catalogue

### Modal interchange (borrowing from the parallel key)
Borrowed chords come from the parallel key: the same tonic in the other mode **(sourced: Wikipedia, Borrowed chord)**.

| Device | Spelling | Character | When |
|---|---|---|---|
| Borrowed iv (minor plagal) | `C 48 | 60 64 67` → `F 41 | 60 65 69` → `Fm 41 | 60 65 68` → back to C | tears, nostalgia: the A→Ab→G line | the last bar of a ballad phrase; the outro; the second pass of a chorus |
| bVII (Mixolydian) | `C 48 | 60 64 67` → `Bb 46 | 62 65 70` → `F 41 | 60 65 69` | swagger, open, rock | pop and rock choruses, gospel vamps |
| bVI–bVII–I ("Mario") | `Ab 44 | 56 60 63` → `Bb 46 | 53 58 62` → `C 48 | 55 60 64` | triumph | EDM build payoffs, trailers, synthwave, game wins |
| bIII | `Eb 39 | 58 63 67` | soul and rock colour, slightly dark | swap it for iii or I in a bridge |
| iiø7 from minor | `Dm7b5 38 | 53 56 60` → `G7 43 | 53 55 59` → `C 48 | 52 55 60` | yearning predominant | an R&B or jazz ii–V–I that should feel sadder |
| Backdoor iv7–bVII7–I | `Fm7 41 | 56 60 63` → `Bb7 46 | 56 62 65` → `Cmaj7 48 | 55 59 64` | soft, soulful landing | gospel, neo-soul, a final cadence without V **(sourced: Wikipedia, Backdoor progression)** |
| Dorian IV in minor | `Am9 45 | 55 59 60 64` → `D9 38 | 54 57 60 64` | cool, hopeful minor | neo-soul, deep house, funk vamps |

### Secondary dominants (tonicise a chord other than I)
The added sharp is a leading tone to the target root **(sourced: Wikipedia, Secondary chord)**.

| Device | Spelling | Leading tone | Use |
|---|---|---|---|
| V/V | `D7 50 | 54 57 60` → `G 43 | 55 59 62` | F#→G | brighter approach to V; pre-chorus |
| V/vi | `E7 40 | 56 59 62` → `Am 45 | 57 60 64` | G#→A | R&B and gospel favourite; I–E7–Am |
| V/ii | `A7 45 | 55 61 64` → `Dm 50 | 57 62 65` | C#→D | turnarounds (I–VI7–ii–V) |
| V/IV | `C7 48 | 58 64 67` → `F 41 | 57 65 69` | Bb→A (7th falls) | blues and gospel push into IV |
| Secondary ii–V | `Am7 45 | 55 60 64` → `D9 38 | 54 60 64` → `G 43 | 55 59 62` | F#→G | jazz and neo-soul chains |

### Tritone substitution
Replace V7 with bII7. Both chords share the same tritone, so the bass slides down by semitones **(sourced: Wikipedia, Tritone substitution)**:
`Dm9 38 | 53 57 60 64` → `Db9#11 37 | 53 55 59 63` → `Cmaj9 36 | 52 55 59 62`
- In Db9#11, F is the 3rd, G is the #11, Cb (= B) is the b7 and Eb is the 9.
- Character: slinky, sophisticated. Use it in R&B, neo-soul, lo-fi and jazz.
- In trap or pop it is a big surprise, so use it at most once per song there.

### Chromatic mediants
These are roots a 3rd apart with the same quality and chromatically related notes. They keep one common tone **(sourced: Wikipedia, Chromatic mediant)**.

| From C | Spelling | Common tone | Feel |
|---|---|---|---|
| → E (III) | `C 48 | 60 64 67` → `E 52 | 59 64 68` | E | wonder, reveal, sci-fi lift |
| → A (VI) | `C 48 | 60 64 67` → `A 45 | 61 64 69` | E | bright heroic lift |
| → Ab (bVI) | `C 48 | 60 64 67` → `Ab 44 | 60 63 68` | C | epic, darkening awe |
| → Eb (bIII) | `C 48 | 60 64 67` → `Eb 51 | 58 63 67` | G | bold, filmic swerve |

- Use them for cinematic reveals, trailer hits, the last chorus of a ballad, or a game "level up".
- One mediant per section is the ceiling.
- Minor-key film staple: alternate i ↔ bVI over a pedal, `Am 45 | 57 60 64` → `F 41 | 57 60 65`.

### Pedal points
A pedal holds one note, usually in the bass, while the harmonies above it change, including some that clash with it **(sourced: Wikipedia, Pedal point)**.
- **Tonic pedal:** `C 36 | 60 64 67` → `Bb/C 36 | 58 62 65` → `Ab/C 36 | 60 63 68` → `Bb/C 36 | 58 62 65` → back to C.
  - The 808 or bass holds the root while tension builds above it.
  - Use it for trap and drill (the 808 never leaves the root), house (organ or bass pedal), and film builds.
- **Dominant pedal (build before a drop):** `C/G 43 | 60 64 67` → `F/G 43 | 60 65 69` → `Dm/G 43 | 62 65 69` → `G7 43 | 62 65 71` → drop on `C 48 | 64 67 72`.
- During builds, hold a pedal so the rising tension comes from rhythm, filter and risers, not from new chords (`music-arrangement`).

### Line cliché (a moving inner voice over a static chord)
`Am 45 | 57 60 64` → `Am(maj7) 45 | 56 60 64` → `Am7 45 | 55 60 64` → `Am6 45 | 54 60 64`
- The inner voice falls by semitone, A–G#–G–F#.
- Character: noir, spy films, instant sophistication without moving the bass.
- Use one bar per chord, as an intro or a verse turnaround. Led Zeppelin's "Stairway to Heaven" intro is the famous descending example (k).

### Suspension and resolution
`G7sus4 43 | 53 60 62` → `G7 43 | 53 59 62` → `C 48 | 52 60 64`
- The 4th (C) falls to the 3rd (B), and the dominant then resolves.
- Use it in gospel, house and pop "lift" moments. Trance holds a sus chord one bar longer than feels comfortable before resolving **(Orphiq summary)**.

### Neapolitan (bII6) in minor (C minor)
`Cm 48 | 55 60 63` → `Db/F 41 | 56 61 65` → `G7 43 | 55 59 65` → `Cm 48 | 55 60 63`
- Character: tragic, operatic, dark grandeur.
- Use it in cinematic music, dark trap intros and drill bridges. It is the functional cousin of the Phrygian b2.

### Picardy third
End a minor section on the **major** tonic **(sourced: Wikipedia, Picardy third)**. In A minor: `E 40 | 56 59 64` → `A 45 | 57 61 64` (C# replaces C).
- Character: sudden light, hope after sadness.
- Use it for a cinematic or lo-fi outro, the last chord of a sad ballad, or the end of a trap intro before the drop (rare, so it is a big surprise).

### Planing (parallel shapes)
Move one voicing shape in parallel: deep-house chord memory (`Am9 45 | 60 64 67 71` → `Dm9 50 | 65 69 72 76`), power chords, or brass fanfares (`Ab 44 | 60 63 68` → `Bb 46 | 62 65 70` → `C 48 | 64 67 72`). It breaks the parallel-5ths rule on purpose. Use it as the sound of the genre, not by accident.

## 4. Modulation routes (convention)

| Route | Example | Effect | When |
|---|---|---|---|
| Pivot chord | `C 48 | 60 64 67` → `Am 45 | 60 64 69` (vi in C = ii in G) → `D7 50 | 57 60 66` → `G 43 | 59 62 67` | smooth; you only notice afterwards | bridges, long-form pieces |
| New key's V7 | `D7` → G (entering G from C) | clear signpost | pre-chorus into a new-key chorus |
| "Truck-driver" lift | `G 43 | 59 62 67` (V of C) → `Ab7 44 | 60 63 66` (V7 of Db) → `Db 49 | 61 65 68` | big, cheesy-effective energy | last chorus of pop; trance's last drop (+1 or +2 semitones) |
| Direct lift, no pivot | jump straight up 1–2 semitones on the downbeat after a fill or silence | abrupt and exciting | EDM final drop, pop key change |
| Relative switch | A-minor verse → C-major chorus (same notes, new home) | "the sun comes out" | pop and EDM verse → chorus |
| Parallel switch | `Cm 48 | 55 60 63` → `C 48 | 55 60 64` (C-minor verse → C-major chorus) | dramatic brightening | cinematic, pop bridges |

After a key change, transpose every part, the 808 included. Re-check the 808's register (`music-bass-808`) and the chord floor of about MIDI 48.

## 5. Placement recipes (convention)

1. **8-bar loop with a turnaround:** bars 1–7 diatonic. On bar 8, swap one chord: IV→iv, V→V/vi, or V→bII7 (tritone sub).
2. **Pop chorus repeat:** the first chorus is plain I–V–vi–IV. On the second pass, make its last IV a borrowed iv. The final chorus is the same loop with the key lifted a semitone.
3. **Trap loop:** keep i–VI–v for 7 bars. Bar 8 brings a harmonic-minor V (major) or a diminished stab before the loop restarts. In a busy-drum section, stay diatonic.
4. **Build into a drop:** use a dominant pedal or a held sus chord through the build, then bVI–bVII–I (or i) on the drop.
5. **Lo-fi or R&B:** spend extensions freely (they are the norm). Spend one tritone sub or secondary dominant per 4–8 bars. Use the line cliché as an intro.
6. **Cinematic:** pedal and i–bVI for 8–16 bars, a chromatic mediant on the reveal, and a Picardy or Mario finish at the end.

## 6. Sources
- Cheung, Harrison, Meyer, Pearce, Haynes & Koelsch (2019), *Current Biology*: uncertainty × surprise and pleasure (about 80,000 Billboard chords).
- Huron, *Sweet Anticipation* (ITPRA), via the Music & Letters review: https://academic.oup.com/ml/article/89/3/396/1135734
- Wikipedia: Borrowed chord; Backdoor progression; Secondary chord; Tritone substitution; Chromatic mediant; Pedal point; Picardy third.
- Orphiq, trance (via search summary): https://orphiq.com/resources/what-is-trance-music
