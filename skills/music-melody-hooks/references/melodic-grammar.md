# Melodic grammar: contour, intervals, range, chord tones, non-chord tones, rhythm

The measurable rules a melody generator follows, each with its evidence level and the reason behind it. Pitches use MIDI with C4 = 60 (FL labels one octave higher). Beats are 0-based, and steps run 1–16 per bar.

## Contents
1. Contour
2. Steps, leaps, gap-fill, regression to the mean
3. Interval character
4. Range and register
5. Chord tones vs non-chord tones (placement, targets, guide tones)
6. Non-chord tone table with emotional effect
7. Tension notes cheat-sheet
8. Rhythm of melody (rhythm first, syncopation, pushes, rests, repeated notes, cells, density)
9. Articulation, velocity, humanizing
10. Sources

---

## 1. Contour

**Findings.** Huron's analysis of 6,251 European folk melodies (Essen corpus) and later corpus work find four broad phrase shapes: convex (arch), concave (inverted arch), descending and ascending. **The arch predominates, followed by ascending, then descending.** Pitch tends to hold steady at a phrase's start and fall at its end **(sourced: arXiv 2604.13119)**. Earworms have *more common* global contours than matched non-earworms **(sourced: Jakubowski et al. 2017)**. A familiar overall shape is therefore an asset, not a cliché.

**Shape menu.** Choose the shape by the section's job **(convention)**:

| Shape | Profile | Use for |
|---|---|---|
| Arch (convex) | rise to one peak, fall back | default hook, chorus, theme, EDM lead |
| Inverted arch (concave) | dip, then return | dark loops (trap/drill/lo-fi), verse answers |
| Descending | starts high, falls to 1/3/5 | sad or resolving phrases, trap bells, R&B run endings, cadences |
| Ascending | rises throughout | pre-chorus, build-up, the call of a call-and-response |
| Stationary | hovers around 1–3 pitches | rap-adjacent toplines, afro chants, tech-house one-shots, repeated-note hooks |

**Climax rules** **(convention, from Ableton teaching plus the corpus ordering)**:
- Give each 4- or 8-bar phrase **one highest note that occurs once**.
- Put it **55–75% of the way through the phrase**, on a strong beat (beat 1 or 3):
  - 8 bars (32 beats): bar 6 beat 1 (beat 20 = 62.5%) is the default. The usable window runs from bar 5 beat 3 (56%) to bar 7 beat 1 (75%). The bar-5 downbeat (50%) is a common, slightly early option.
  - 4 bars: bar 3 beat 3 (beat 10 = 62.5%) or bar 4 beat 1 (75%).
  - 2-bar loop: bar 2 beat 1 (50%) or bar 2 beat 3 (75%).
- Make the climax the place you spend the "one surprise": a leap, a borrowed note, an appoggiatura or a long hold.
- The next section may peak **2–5 semitones higher** (chorus above verse, final chorus above chorus).
- Balance each rise with a fall of about the same size, then end within about 5 semitones of the start, unless the phrase is a deliberate build.

**Contour as a target function** **(derived)**. For position `x` in 0..1 across the phrase, aim the skeleton pitch at:
`target(x) = low + span * sin(pi * min(x / c, 1) / 2)` while `x <= c`, then descend toward the cadence pitch after `c`, where `c` = 0.55–0.75. This is a planning aid. Snap every target to the nearest chord tone (strong beats) or scale tone (weak positions).

## 2. Steps, leaps, gap-fill, regression to the mean

**Findings.**
- "Most melodic motion is by small steps (of 2 semitones or less)." The whole step is more common than the half step, probably because scales contain more whole steps **(sourced: Patel 2007)**.
- **Step inertia:** a step tends to continue in the same direction **(sourced: Music & Science summary)**.
- **Post-skip reversal (gap-fill):** after a large leap, melodies usually change direction. Von Hippel & Huron (Music Perception, 2000) show this is largely **regression to the mean**: leaps land near the edge of the melody's range, from which the line "has little choice but to retreat". The pattern held in vocal melodies from four continents **(sourced)**.

**Generator rules** **(convention unless marked)**:

| Rule | Value |
|---|---|
| Steps (0–2 semitones, repeats included) | 65–80% of intervals |
| Thirds (3–4 semitones) | 15–25% (arpeggio motifs and pentatonic lines can reach 30%) |
| Leaps (≥ 5 semitones) | ≤ 10%; one "signature leap" per hook |
| After a leap ≥ 5 | next 2–4 notes move stepwise in the opposite direction, and fill at least half the gap before the phrase ends |
| Running mean | when the line sits > 7 semitones from the phrase's running mean pitch, bias the next move back toward it |
| Pentatonic lines | count steps in scale degrees, because the 3-semitone gaps (e.g. B–D, E–G in G pentatonic) are scale steps **(derived)** |
| Augmented 2nd (b6–#7 in harmonic minor) | avoid in singable lines; allowed as a deliberate "exotic" colour in drill, phonk or Middle-Eastern flavours |
| Two leaps in a row in the same direction | only when outlining one chord (arpeggio), then reverse |

Gap-fill example: C4 60 → A4 69 (major-6th leap) → G4 67 → F4 65 → E4 64.

## 3. Interval character

These are conventional Western associations, not research findings **(convention)**. Use them to choose the signature leap.

| Interval | Semitones | Typical effect |
|---|---|---|
| Unison / repeat | 0 | rhythmic emphasis, chant; hooky in rap, afro, pop |
| Minor 2nd | 1 | tension, dark, menacing (Phrygian b2→1, b6→5) |
| Major 2nd | 2 | neutral flow, the default step |
| Minor 3rd | 3 | sad, soulful; core of minor pentatonic and blues |
| Major 3rd | 4 | bright, open |
| Perfect 4th | 5 | strong, announcing (pickup 5→1) |
| Tritone | 6 | unstable, wants resolution |
| Perfect 5th | 7 | open, stable, heroic; cinematic opening leap |
| Minor 6th | 8 | yearning, bittersweet |
| Major 6th | 9 | warm, expansive, nostalgic |
| Minor 7th | 10 | bluesy, unresolved, dramatic |
| Major 7th | 11 | rarely leapt; striking, dreamy |
| Octave | 12 | big lift, the "drop" leap; also doubling |

Ascending leaps read as effort and energy. Descending steps read as release. Cadences are most often approached by a descending step (2→1, 4→3), less often by the rising leading tone (7→1) **(convention)**.

## 4. Range and register

Ranges are practical approximations; no corpus source was found **(convention)**.

| Part | Total range | Register (MIDI, scientific; FL name = octave + 1) |
|---|---|---|
| Pop topline | 9–14 semitones | male ≈ A2–A4 (45–69); female ≈ F3–F5 (53–77) |
| Verse topline | 5–9 semitones | chorus sits 3–5 semitones higher |
| Instrumental hook motif | 5–9 semitones | octave doubling adds width |
| Bells, plucks, leads | up to ~24 including doubling | keep the main line ≥ MIDI 52 (E3) to stay clear of the 808 |
| Trap/drill bells | 12–14 | ≈ 64–84 (E4–C6) |
| Lo-fi keys or R&B melody | 8–14 | ≈ 57–77 |
| EDM drop lead | 10–15 | ≈ 64–84, stacked ±12 |
| Counter-melody | ≤ 10 | one band below or above the lead, ≥ 3 semitones away |
| Bass-register melody (808, log drum) | — | E1–E3 (28–52), see `music-bass-808` |

Register slotting against other parts (pads, chords ≥ 48 with an 808) is covered in `music-arrangement`.

## 5. Chord tones vs non-chord tones

**Findings.** Hooktheory TheoryTab analyses show individual songs with **45–69%** of melody notes on chord tones. No aggregate statistic was found **(sourced: Hooktheory)**. Strict chord-tone writing is therefore not required. The non-chord tones carry much of the colour.

**Placement rules** **(convention)**:
- On beats 1 and 3, sound a chord tone **75–85%** of the time. The remainder are deliberate accented non-chord tones (appoggiaturas, suspensions), which are the expressive moments.
- Weak beats, off-beats and 16ths: non-chord tones are free if they resolve by step.
- **Target priority on strong beats:** the 3rd for emotion (it defines major or minor), then the 5th for neutral openness, then the 7th or 9th for R&B/lo-fi colour. Keep the **root for cadences** and phrase endings.
- **Guide-tone voice leading at chord changes:** move by step (or hold) to the nearest 3rd or 7th of the new chord. In ii–V–I, the 7th of each chord falls a half step to the 3rd of the next: Dm7 (C) → G7 (B) → Cmaj7 (B held as the maj7, or → C).
- **Implied harmony test:** solo the melody. If the chord changes are audible (chord tones arpeggiated on strong beats, passing tones between), the melody implies its harmony. If not, move more strong-beat notes onto 3rds.

## 6. Non-chord tone table with emotional effect

The mechanics are standard theory **(sourced: Wikipedia, Nonchord tone)**. The effects are convention, except the appoggiatura row, which has research support **(Sloboda 1991)**. Examples are over a C major chord (C E G) in C major.

| Type | Approach → leave | Accent | Effect | Example |
|---|---|---|---|---|
| Passing tone | step → step, same direction | weak (accented variant exists) | smooth motion, connective tissue | E4 64 → **F4 65** → G4 67 |
| Neighbor tone | step → step back | weak | decoration, "turn", hooky wobble | E4 64 → **F4 65** → E4 64 |
| Appoggiatura | **leap** → step (usually down) | **strong** | ache, longing, the "tear" device | G4 67 → **D5 74** (on beat 1) → C5 72 |
| Suspension | held/tied from previous chord → step **down** (4–3, 7–6, 9–8) | strong | longing, delayed release, cinematic | F4 65 tied from F chord into C chord → E4 64 |
| Retardation | held → step **up** (7–8) | strong | yearning upward push | B4 71 tied into C → C5 72 |
| Anticipation | step → same pitch (it is the next chord's tone, early) | weak | forward motion, "push", pop/R&B/afro | over G: **C4 60** on the "and" of 4, then the C chord |
| Escape tone (échappée) | step → leap opposite | weak | sigh, ornament at cadences | E4 64 → **F4 65** → C4 60 |
| Changing tones (double neighbor) | step → leap to the other side → resolve | weak | ornamental turn around a target | D5 74 → B4 71 → C5 72 |
| Pedal point | held through changing chords | — | hypnotic tension (trailer ostinati, trance) | G held under C–F–C |

**Accented vs unaccented.** Accented non-chord tones (appoggiatura, suspension, accented passing tone) create the expressive "lean", and resolving them gives release. Unaccented ones only decorate.

## 7. Tension notes cheat-sheet

**(convention)**

| Note over chord | Effect | Where |
|---|---|---|
| 9th (degree 2 over I) | airy, modern | pop, R&B, lo-fi phrase endings |
| sus4 → 3 | longing, then relief | pop choruses, trance holds |
| leading tone 7 → 1 (raised 7 in minor) | urgent pull; harmonic-minor "exotic" drama | trap/drill V chord, cinematic cadences |
| b6 → 5 in minor | sorrowful, the trap staple | trap bells, drill motifs |
| b2 → 1 (Phrygian) | menacing | drill, phonk, dubstep, trailer threat |
| maj7 over IV (E over F in C) | dreamy | lo-fi, R&B, pluggnb |
| Dorian 6 (B over Dm in D Dorian) | bittersweet-hopeful minor | lo-fi, house, synthwave |
| #4 / b5 | unstable; resolve fast | passing only, or Lydian float (film, ambient) |
| b3 or b7 over a major chord (blue notes) | grit, soul | R&B runs, boom bap, gospel licks |
| 13th over a dominant | sweet tension | R&B, neo-soul |

## 8. Rhythm of melody

**Findings.**
- Earworms have **faster tempi** than matched non-earworms **(sourced: Jakubowski et al.)**.
- Some earworm riffs carry **more repeated notes** than typical pop melodies; the examples cited are "My Sharona", "In the Mood" and "Smoke on the Water" **(sourced: Neuroscience News summary)**.
- Producer guidance holds that rhythm is as central as pitch: the same notes with different timing feel unfamiliar **(sourced, practitioner: Lost Stories Academy)**. No study directly measures "rhythm more memorable than pitch".

**Write the rhythm first** **(convention)**:
- Use 4–8 onsets per bar for a hook, **at least one syncopation** and **at least one rest ≥ 0.5 beat**.
- Syncopation means an onset on a weak position (an off-beat 8th or a 16th e/a) that is held across the next stronger position. Example: onset at 1.5, held to 2.5, crosses beat 3.
- Reuse the same rhythm for the answer phrase. Pitch variation over a fixed rhythm reads as development; rhythm change reads as new material.

**Pushes (anticipations).** Move a phrase's arrival note an 8th early (−0.5 beat) or a 16th early (−0.25) onto the previous off-beat, tied over the bar line. They are everywhere in pop, R&B and afrobeats toplines **(convention)**.

**Repeated-note hooks.** Use 3–6 repetitions of one pitch with rhythmic variety, then one move away, a leap for preference. The leap is surprise against stasis **(convention, supported by the repeated-note finding above)**.

**Rests.** Rests frame the hook and leave room for drums, 808 and vocal. In beat-making, leave at least one rest per bar. In trap and drill, leave whole empty bars for the rapper **(convention)**.

**Rhythm cells** (beats within the bar; steps 1–16) **(convention)**:

| Cell | Onsets (beats) | Steps | Use |
|---|---|---|---|
| Half-bar tresillo (3+3+2 sixteenths) | 0, 0.75, 1.5 and 2, 2.75, 3.5 | 1 4 7, 9 12 15 | afrobeats, dancehall, reggaeton, trap bells |
| Full-bar 3+3+2 (eighths) | 0, 1.5, 3 | 1 7 13 | dembow and house stabs, pop pre-choruses |
| Charleston | 0, 1.5 | 1 7 | swing, house, pop push feel |
| Off-beat stabs | 0.5, 1.5, 2.5, 3.5 | 3 7 11 15 | house, UKG, reggae skank |
| Long-short-short | 0 (1.0), 1 (0.5), 1.5 (0.5) | 1 5 7 | ballads, cinematic, hymn-like |
| Short-short-long ("da-da-DAA") | 0 (0.5), 0.5 (0.5), 1 (1.0) | 1 3 5 | pop hooks (Ex 2) |
| Son clave 3-2 (2 bars) | bar 1: 0, 1.5, 3; bar 2: 1, 2 | 1 7 13 / 5 9 | afrobeats, afro house, salsa-derived toplines |
| Quarter-note triplets | 0, 0.667, 1.333 (64 ticks apart) | — | drill "cold" motifs, half-time drags (Ex 8) |
| 16th-note-triplet run | 6 notes per beat (16 ticks apart) | — | R&B runs, trap fills (Ex 5) |

**Note density by role** **(convention)**:

| Role | Onsets per bar | Notes |
|---|---|---|
| Verse topline | 4–10 | follows speech rhythm, narrow range, many repeats |
| Chorus hook | 3–8 | longer notes, more held tones |
| EDM lead / drop riff | 4–12 | 16ths at 120–128 BPM; one lead at a time in a drop |
| Trap/drill bells | 4–8 at 130–160 BPM (half-time) | lots of space |
| Lo-fi keys melody | 3–6 | lazy 8ths, rests |
| Counter-melody | ≈ ½ of the lead's | fills the lead's rests |
| Cinematic theme | 1–4 | long notes, slow harmonic rhythm |

## 9. Articulation, velocity, humanizing

These defaults are **(convention)**:
- **Length:** bells, plucks and marimbas take short notes (0.25–0.75 beat, envelope does the rest). Keys and Rhodes run near legato (90–100% of the slot). Pads and strings take full value. Mono synth leads with portamento: overlapping notes glide, but only on FL native instruments (see `music-bass-808` for slide setup).
- **Velocity:** strong-beat chord tones run 95–110, weak passing tones 70–85, and the climax 110–120. Alternate repeated notes (e.g. 92/80) so they do not machine-gun. Lo-fi and R&B sit at 60–90 overall.
- **Humanize by genre:**
  - EDM, trap and drill: tight grid, velocity ±5.
  - Afro: ±5–10 ms, velocity ±10.
  - Lo-fi and R&B: ±10–20 ms, velocity ±10–15, plus 8th swing 55–62% (MPC scale) applied with `swing8()` from `worked-examples.md`.
  - Never randomise the climax or the downbeats of the hook.
- **Doubling layers:** an octave copy (±12) sits 10–20% softer. Diatonic 3rds or 6ths harmony sits 15–25% softer.

## 10. Sources

- Contour corpus (Huron 1996, Essen): arXiv 2604.13119 — https://arxiv.org/pdf/2604.13119
- Ableton Making Music, Contour — https://makingmusic.ableton.com/creating-melodies-1-contour
- Patel 2007, *Music, Language, and the Brain* ch. 4.5 — https://acousticslab.org/RECA293/293Files/293Downloads/Patel2007_MelodicStatsAndContour.pdf
- Step inertia summary — https://doaj.org/article/43b320953f444935a677d6cec2cb74f8
- von Hippel & Huron 2000, "Why do skips precede reversals?" — https://labs.sonicfield.org/library/why-do-skips-precede-reversals-the-effect-of-tessitura-on-melodic-structure
- Nonchord tones — https://en.wikipedia.org/wiki/Nonchord_tone
- Hooktheory TheoryTab chord-tone percentages — https://www.hooktheory.com/theorytab/view/harry-styles/pop
- Jakubowski, Finkel, Stewart & Müllensiefen 2017 (earworms) — https://research.gold.ac.uk/19405 ; https://www.apa.org/news/press/releases/2016/11/earworms ; https://neurosciencenews.com/song-stuck-in-head-5423/
- Lost Stories Academy, catchy EDM hooks — https://loststoriesacademy.com/blogs-and-tutorials/the-science-behind-catchy-edm-hooks
- Sloboda 1991, *Psychology of Music* 19:110–120 (appoggiaturas and tears) — summary https://www.npr.org/2012/02/13/146818461/the-ballad-of-the-tearful-why-some-songs-make-you-cry
