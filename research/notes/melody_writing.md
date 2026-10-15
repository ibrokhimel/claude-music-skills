# Melody Writing Craft: Hooks, Leads, Toplines, Counter-Melodies (for an FL Studio piano-roll composer skill)

Conventions used throughout: MIDI numbers use the C4 = 60 convention (scientific pitch). FL Studio's piano roll labels MIDI 60 as "C5", so add 1 to the octave number when reading the FL Studio display (MIDI 69 = A4 here = "A5" in FL). Positions are written as `beat offset (0-based, 4/4) : note MIDI : duration in beats`. 1 beat = a quarter note; at FL's default 96 PPQ, 1 beat = 96 ticks.

Sourcing note: items under "Cited Findings" carry a source link. Items under "Inferences" are my synthesis plus standard tonal-theory practice (interval names, chord spellings, MIDI arithmetic). They are rules of thumb, not empirical claims. Every worked example is original. None is transcribed from a copyrighted song.

---

## 1. Contour: shapes, the single climax, and range

### Takeaway
Across large folk corpora the arch (convex) shape is the most common phrase contour, followed by ascending and then descending. Phrases tend to hold steady at the start and fall at the end. Practical teaching agrees on a few points: balance rises with falls, use one highest note that appears only once (ideally on a strong beat), and put it around the middle-to-late part of the phrase.

### Cited Findings
- Huron (1996) analysed melodic arches in 6,251 melodies from the European subset of the Essen folksong corpus and proposed nine contour classes. These are now computable in the FANTASTIC toolbox. — [arXiv: Melodic contour does not cluster (2026)](https://arxiv.org/pdf/2604.13119)
- Contour studies find four broad shapes across datasets: convex (arch), concave (inverted arch), descending, and ascending. Pitch tends to stay stable at phrase beginnings and to descend at phrase endings. In the Essen collection convex contours predominate, followed by ascending and then descending. — [arXiv 2604.13119](https://arxiv.org/pdf/2604.13119)
- Five basic contour types are commonly taught: ascending, descending, arch, inverse arch, and stationary. — [arXiv 2604.13119](https://arxiv.org/pdf/2604.13119); see also [Dummies: shaping the melody](https://www.dummies.com/article/academics-the-arts/music/music-theory/how-to-use-music-theory-to-shape-the-melody-144456/)
- Ableton's "Making Music" melody chapter gives these guidelines:
  - Balance rise and fall: after rising for a while, fall back by roughly the same amount.
  - Most effective melodies have one highest note that occurs only once, often on a strong beat.
  - Its example arc starts from the lowest note, climbs to the peak around the midpoint, then descends.
  - Good melodies do not follow these rules 100% of the time. — [Ableton: Creating Melodies 1 – Contour](https://makingmusic.ableton.com/creating-melodies-1-contour)
- Earworms (involuntarily recalled tunes) tend to have *more common* global contours. The researchers' example is the rise-and-fall shape of "Twinkle Twinkle Little Star", which they say "Moves Like Jagger" also follows. — [Neuroscience News summary of Jakubowski et al.](https://neurosciencenews.com/song-stuck-in-head-5423/)

### Inferences
- **Default contour for a 4- or 8-bar hook:** an arch, with the climax at 55–75% of the way through the phrase. In an 8-bar phrase, that is the downbeat of bar 5 or 6.
- **Low-energy or dark loops** (trap, drill, lo-fi): use an inverted arch or descending shape, falling to the tonic at the loop end, which matches the descending phrase endings found in corpora.
- **Build-ups and pre-choruses:** use an ascending contour; save the climax for the drop or chorus.
- **One climax rule:** in any 4- or 8-bar section, let the highest MIDI number occur once. The section that follows (for example, the chorus after the verse) can take a new, higher peak, typically 2–5 semitones above the previous section's peak.
- **Range guidelines (practical, uncited):**
  - Singable pop topline: total range about 9–14 semitones (a 6th to a 9th). Verses usually sit in a narrower 5–9 semitone band, and the chorus sits higher.
  - Typical comfortable windows: male voice about A2–A4 (45–69); female voice about F3–F5 (53–77).
  - Instrumental leads and bells can span 12–24 semitones, but a hook *motif* itself usually sits within 5–9 semitones (a 4th to a 6th). Octave doubling adds the width.
  - Bass-register melodies (808 or log drum): roughly E1–E3 (28–52).
- **Worked contour skeleton.** A major, 8 bars, arch. The peak is at bar 5 and occurs once.
  - Bars 1–4: A3 57, B3 59, C#4 61, E4 64, F#4 66
  - Peak at bar 5 beat 1: A4 69
  - Fall back: F#4 66, E4 64, C#4 61, B3 59
  - End on A3 57
  - Range = 12 semitones.

### Gaps
- I did not retrieve the exact percentages from Huron (1996), such as what share of phrases are convex. The arXiv source gives only the ordering.
- I found no empirical source for exact singable ranges. The ranges above are standard vocal-pedagogy approximations.

---

## 2. Motion: steps, leaps, gap-fill, regression to the mean, interval character

### Takeaway
Real melodies are dominated by small intervals. Most motion is by steps of 2 semitones or less, and the whole step is the most common interval in music. Steps tend to continue in the same direction ("step inertia"). After a large leap, melodies usually change direction. von Hippel & Huron argue this "post-skip reversal" is mostly regression toward the middle of the range rather than a separate psychological rule. For a composer either explanation leads to the same rule: leap, then step back the other way.

### Cited Findings
- "Musical melodies are dominated by small intervals… most melodic motion is by small steps (of 2 semitones or less)." In musical melodies 2-semitone intervals are more common than 1- or 0-semitone ones, likely because whole steps are more common in scales. Listeners' expectations reflect this. — [Patel, *Music, Language, and the Brain* (2007), ch. 4.5](https://acousticslab.org/RECA293/293Files/293Downloads/Patel2007_MelodicStatsAndContour.pdf)
- Step inertia: a step tends to be followed by another step in the same direction. There is strong evidence for it in European folk songs, classical instrumental themes, and English hymn tunes. — [summary via search results, Sonicfield library / Music & Science](https://doaj.org/article/43b320953f444935a677d6cec2cb74f8)
- von Hippel & Huron, "Why do skips precede reversals? The effect of tessitura on melodic structure":
  - In melodies from many cultures, a large interval tends to be followed by a change of direction.
  - Skips tend to land near the extremes of a melody's range, from which the melody "has little choice but to retreat".
  - Analyses of vocal melodies from four continents fit this explanation, implying that gap-fill, registral direction, and registral return are largely side effects of range constraints.
  — [Sonicfield library entry (search summary)](https://labs.sonicfield.org/library/why-do-skips-precede-reversals-the-effect-of-tessitura-on-melodic-structure)
- Ableton's guidance agrees in practice: after a stretch of steps, a leap in the opposite direction is a good choice, and after a leap, stepwise motion in the opposite direction usually follows. — [Ableton: Contour](https://makingmusic.ableton.com/creating-melodies-1-contour)
- Earworms show "less common average gradients between melodic turning points" and "unusual intervals" (unexpected leaps) or more repeated notes than typical pop songs. — [APA press release](https://www.apa.org/news/press/releases/2016/11/earworms); [Neuroscience News](https://neurosciencenews.com/song-stuck-in-head-5423/)

### Inferences
- **Step/leap ratio rule of thumb:** about 65–80% of intervals should be steps (0–2 semitones, counting repeated notes), about 15–25% small skips (3–4 semitones, i.e. 3rds), and at most 10% leaps of 5 semitones or more. Allow one "signature leap" per hook; that is the "one surprise" (see section 5).
- **Gap-fill algorithm:**
  1. After any leap of 5 semitones or more, move the next 2–4 notes stepwise in the *opposite* direction.
  2. Fill at least half the gap before the phrase ends.
  - Example: C4 60 → A4 69 (major-6th leap up, 9 semitones), then G4 67, F4 65, E4 64 stepwise down. This is the same opening gesture as the traditional song "My Bonnie Lies Over the Ocean".
- **Regression to the mean:** track the running mean pitch of the phrase. When the melody is more than 7 semitones above or below it, bias the next motion back toward it. End phrases within about 5 semitones of where they started, unless the phrase is a deliberate build.
- **Interval character** (conventional Western associations; subjective, not research-backed):

| Interval | Semitones | Typical effect |
|---|---|---|
| Unison / repeated note | 0 | rhythmic emphasis, chant-like, hooky in rap or afro toplines |
| Minor 2nd | 1 | tension, dark, "horror" (trap Phrygian b2 → 1) |
| Major 2nd | 2 | neutral flow, the default step |
| Minor 3rd | 3 | sad or soulful, the core of minor pentatonic and blues |
| Major 3rd | 4 | bright, open |
| Perfect 4th | 5 | strong, heroic, "announcing" (pickup 5 → 1) |
| Tritone | 6 | unstable, wants resolution |
| Perfect 5th | 7 | open, stable, powerful, fanfare |
| Minor 6th | 8 | yearning, bittersweet (5 → b3 up in minor) |
| Major 6th | 9 | warm, expansive, nostalgic |
| Minor 7th | 10 | bluesy, unresolved, dramatic |
| Major 7th | 11 | rarely leapt; striking, dreamy |
| Octave | 12 | big lift, the "drop" leap; also octave doubling |

- **Ascending vs descending:** ascending leaps read as effortful or energetic; descending steps read as relaxing or resolving. A cadence is most often approached by descending step (2 → 1 or 4 → 3), and less often by ascending leading tone (7 → 1).

### Gaps
- I did not retrieve exact post-skip reversal percentages or the journal citation details for von Hippel & Huron. It is known to be in *Music Perception* (2000), but this was not verified in-session, and the source page domain failed to load. Narmour's implication–realization model was not fetched.

---

## 3. Motifs and development; phrase and period structures

### Takeaway
A motif is the smallest unit with thematic identity, often just 2–5 notes or a rhythmic cell. Melodies are built by stating it and then repeating it with controlled variation. Two standard 8-bar templates do most of the work:
- **Period:** a question phrase (antecedent) and an answer phrase (consequent).
- **Sentence:** a basic idea, its repetition, then a developmental continuation to a cadence.

### Cited Findings
- A motif is "a short musical idea, salient recurring figure… the smallest structural unit possessing thematic identity". Motifs can be melodic, harmonic, or rhythmic. A rhythmic motif is a rhythm abstracted from a melody. Beethoven's Fifth uses a four-note motif (three short notes and one long) that reappears in many permutations. — [Wikipedia: Motif (music)](https://en.wikipedia.org/wiki/Motif_(music))
- The Schoenberg-tradition sentence:
  - First part: a basic motive plus its complementary repetition, for example the tonic version answered by the dominant version.
  - Second part: "reduction/condensation" leading to a "liquidated" cadence.
  - Schoenberg called it a higher form than the period because it begins development immediately. The period, by contrast, is an antecedent–consequent pair. Beethoven's Piano Sonata in F minor (Op. 2 No. 1) is the classic example.
  — [Wikipedia: Sentence (music)](https://en.wikipedia.org/wiki/Sentence_(music))
- Hooks benefit from repeating the core idea with small changes (rhythm shifts, an altered final note, added harmony), which balances familiarity and surprise. — [Lost Stories Academy: The Science Behind Catchy EDM Hooks](https://loststoriesacademy.com/blogs-and-tutorials/the-science-behind-catchy-edm-hooks)
- Pattison's prosody teaching treats even numbers of lines or phrases (and matching phrase lengths) as *stable*, and odd numbers or mismatched lengths as *unstable*. Songwriters use stable versus unstable groupings to match the emotion of the lyric. — [Coursera: Songwriting – Writing the Lyrics (Pattison, Berklee)](https://www.coursera.org/learn/songwriting-lyrics)

### Inferences
- **Development toolbox** (standard theory). Each technique is listed with an operation a piano-roll AI can apply to a motif, a list of (offset, MIDI, duration) notes:

| Technique | Operation | Effect |
|---|---|---|
| Exact repetition | copy, offset +N bars | identity, memorability |
| Real transposition | all MIDI ± k | same shape, new color (may leave the key) |
| Diatonic sequence | shift each note by k scale steps | most common in pop and EDM; stays in key |
| Inversion | MIDI' = 2·axis − MIDI (or invert by scale steps) | mirror contour, an "answer" feel |
| Retrograde | reverse note order, keep the rhythm grid | subtle variation, usually less recognizable |
| Augmentation | durations ×2, offsets ×2 | broadening, ideal for half-time drops or cinematic themes |
| Diminution | durations ×0.5 | urgency, a build-up device |
| Rhythmic displacement | offsets ± 0.5 or ± 0.25 beat | syncopation, renewed interest (very common in trap and afro) |
| Fragmentation | use only the head or tail 2–3 notes, repeat | drives continuations and build-ups |
| Tail change | keep the first 70%, alter the last 1–2 notes | the classic question → answer move |
| Interval expansion | widen one interval (for example 3 → 5 semitones) | the "one surprise" at the climax |

- **Rule of three:** state the motif, repeat it (exact or sequenced), then on the third statement break the pattern (extend it, leap to the climax, or cadence). In 4-bar terms: A A A' B, or the sentence's basic idea → repetition → continuation.
- **Phrase lengths:** the motif is 1–2 bars, the phrase 2–4 bars, and the period or sentence 8 bars. Loops in beat music are typically 2, 4, or 8 bars. Avoid odd lengths unless you deliberately want instability, such as a 3- or 5-bar pre-chorus (Pattison's unstable grouping).
- **Period (8 bars):**
  - Antecedent, bars 1–4: ends on an unstable degree (2, 5, or 7), often over V. This is the half cadence.
  - Consequent, bars 5–8: starts like the antecedent and ends on 1 (or 3) over I. This is the authentic cadence.
- **Sentence (8 bars):**
  - Bars 1–2: basic idea (BI).
  - Bars 3–4: BI repeated or sequenced.
  - Bars 5–6: fragments of the BI, usually 1-bar or half-bar units, rising in energy.
  - Bars 7–8: cadence.
  - Proportion 2 + 2 + 4.
- **Call and response:** the call is 1–2 bars ending unresolved; the response is 1–2 bars (often a different instrument, register, or inverted contour) ending resolved. In EDM and afro styles the response may be a vocal chop or a different synth.
- **Worked example: period, C major, chords C | G | Am | F**, one bar each, repeated as C | G | F | C for the consequent.
  - Antecedent bar 1 (C):
    - `0.0:E4 64:1.0` (3rd of C on the downbeat)
    - `1.0:D4 62:0.5` (passing tone)
    - `1.5:C4 60:0.5`
    - `2.0:E4 64:0.5`
    - `2.5:G4 67:1.5` (chord tone, held)
  - Antecedent bar 2 (G):
    - `4.5:G4 67:0.5`
    - `5.0:F4 65:1.0` (7th of G7, tension)
    - `6.0:D4 62:2.0` (5th of G, ends on scale degree 2: the "question")
  - Antecedent bars 3–4 (Am, F): repeat bars 1–2 but change the peak to `10.5:A4 69:1.5` (root of Am). That is the one-step-higher variation, and it is the climax.
  - Consequent bars 5–8 (C | G | F | C):
    - Repeat bar 1, then `20.0:F4 65:0.5`, `20.5:E4 64:0.5`, `21.0:D4 62:1.0` over F.
    - End `24.0:C4 60:4.0` on the tonic. This is the "answer".
  - Range is C4–A4 (60–69), 9 semitones: singable. The climax A4 occurs once.
- **Worked example: sentence, A natural minor, chords Am | F | C | G**
  - BI (bars 1–2): `0.0:E4 64:0.75`, `0.75:E4 64:0.25`, `1.0:C4 60:0.5`, `1.5:D4 62:0.5`, `2.0:E4 64:2.0`, then over F: `4.0:F4 65:1.0`, `5.0:E4 64:1.0`, `6.0:C4 60:2.0`.
  - Repetition (bars 3–4): the same rhythm, diatonic sequence +1 step over C | G, giving F4 65, F4 65, D4 62, E4 64, F4 65 / G4 67, F4 65, D4 62.
  - Continuation (bars 5–6): fragment the first 3 notes (a long, a short, a lower note) and repeat each 1-beat cell a step higher: E–E–C, F–F–D, G–G–E, A–A–F. That peaks at A4 69.
  - Cadence (bars 7–8): G4 67 → E4 64 → D4 62 → long A3 57 or C4 60.

### Gaps
- Open Music Theory's sentence and period chapters returned HTTP 403, so the detailed Caplin-style definitions (basic idea, contrasting idea, cadence types) were not pulled from a primary source in-session. The 2+2+4 proportion is standard Caplin teaching but uncited here.

---

## 4. Melody vs harmony: chord tones, non-chord tones, tension and resolution

### Takeaway
Stable melodies place chord tones on strong beats and use non-chord tones (NCTs) on weak beats as connective tissue. Expressive "ache" comes from *accented* NCTs (appoggiaturas, suspensions) that resolve by step. A strong melody also implies its own harmony, so it still makes harmonic sense when played alone.

### Cited Findings
Non-chord-tone mechanics, from [Wikipedia: Nonchord tone](https://en.wikipedia.org/wiki/Nonchord_tone):

| Type | Approached by | Left by | Accent |
|---|---|---|---|
| Passing tone | step | step, same direction | unaccented (accented variant exists) |
| Neighbor tone | step | step back to the same note | unaccented (accented variant exists) |
| Escape tone (échappée) | step | leap in the opposite direction | unaccented |
| Anticipation | step | same pitch (it is the next chord's tone, arriving early) | unaccented |
| Appoggiatura | leap | step to a chord tone | accented ("overshoot") |
| Suspension | tied preparation | step *down* (4–3, 7–6, 9–8, 2–3) | accented |
| Retardation | tied preparation | step *up* | accented |
| Pedal point | held | held through chord changes | — |
| Changing tones (double neighbor) | step to an NCT | leap to the other NCT, then resolve | — |

- Hooktheory's TheoryTab analyses show per-song chord-tone percentages; individual songs range from about 45% to 69% of melody notes being chord tones. I found no aggregate statistic. — [Hooktheory TheoryTab, via search summary](https://www.hooktheory.com/theorytab/view/harry-styles/pop)
- Hooktheory's approach uses scale degrees 1–7 and shows which melody notes are stable (chord tones) or dissonant against the current chord. — [Musical U on Hooktheory](https://musical-u.com/learn/learn-music-theory-the-fun-way-with-hooktheory)

### Inferences
- **Placement rule:** on beat 1 of each chord, and on beat 3 in 4/4, use a chord tone about 75–85% of the time. On off-beats and 16ths, NCTs are free if they resolve by step.
- **Which chord tone to target:**
  - The **3rd** defines major or minor and is the most "emotional" target.
  - The **root** is the most final; save it for cadences.
  - The **5th** is open and neutral.
  - The **7th** gives smooth, jazzy, or R&B color.
  - Voice-leading trick: when the chord changes, move the melody by step to the nearest 3rd or 7th of the new chord. In ii–V–I, the 7th of one chord falls by a half step to the 3rd of the next.
- **Tension notes and emotional effect:**
  - The 9th (scale degree 2 over I) sounds airy and modern pop.
  - The sus4 (4 over I, resolving to 3) gives longing that then relaxes.
  - The leading tone (7, resolving up to 1) is urgent; harmonic minor's raised 7th gives a dramatic, "exotic" pull.
  - The b6 resolving to 5 in minor is sorrowful (the trap staple).
  - The b2 resolving to 1 (Phrygian) is menacing.
  - The maj7 over IV (E over F in C) sounds dreamy and lo-fi.
  - The #4/b5 is unstable and needs fast resolution.
- **Melody that implies harmony:** arpeggiate the chord tones on strong beats (for example C–E–G across beats 1 and 3) and fill with passing tones. A listener can then infer the progression from the melody alone. Test by soloing the melody: if the chord changes are audible, it implies harmony.
- **Worked NCT examples** in C major over a C chord (C–E–G):
  - Passing: E4 64 → F4 65 (off-beat) → G4 67.
  - Neighbor: E4 64 → F4 65 → E4 64.
  - Appoggiatura: leap from G4 67 up to an accented D5 74 on the downbeat, then resolve down a step to C5 72.
  - Suspension 4–3: hold F4 65 from a preceding F chord into the C chord's downbeat, then fall to E4 64 on beat 2.
  - Anticipation: over G, play C4 60 on the "and" of 4 just before the C chord arrives. This is the "push" (see section 5).

### Gaps
- No aggregate corpus statistic on the percentage of chord tones on downbeats in pop melodies was found. The Hooktheory Trends data was not accessible through search.

---

## 5. Rhythm of melody: syncopation, pushes, space, repeated notes, density

### Takeaway
Rhythm carries as much hook identity as pitch: the same notes in a different rhythm feel unfamiliar. Faster tempi and repeated-note figures are associated with earworms. Space (rests) frames the hook and leaves room for the drums and the 808.

### Cited Findings
- Earworm tunes had faster average tempi than matched non-earworm tunes. — [APA press release](https://www.apa.org/news/press/releases/2016/11/earworms); [Goldsmiths research repository](https://research.gold.ac.uk/19405)
- Some earworms contain more repeated notes than typical pop melodies. The examples given are the riffs of "My Sharona", "In the Mood", and "Smoke on the Water". — [Neuroscience News](https://neurosciencenews.com/song-stuck-in-head-5423/)
- Rhythm is as important as melody for hooks: the same notes with different timing feel unfamiliar, and rhythm should feel natural and unforced. — [Lost Stories Academy](https://loststoriesacademy.com/blogs-and-tutorials/the-science-behind-catchy-edm-hooks)
- For drops, consider a half-time groove, triplet rhythm, or an off-kilter groove instead of a straight 4/4. — [Bax-shop: EDM drop tips](https://www.bax-shop.co.uk/blog/dj-gear/edm-tips-tricks-how-to-make-the-ultimate-drop/)
- Rhythmic motifs are a recognized type of motif, abstracted from a melody's note values. — [Wikipedia: Motif](https://en.wikipedia.org/wiki/Motif_(music))

### Inferences
- **Write the rhythm first.** Tap a 1- or 2-bar rhythm. A good hook rhythm has 4–8 onsets per bar, at least one syncopation (an onset on an off-beat 8th or 16th that is held across the next beat), and at least one rest of half a beat or more.
- **Anticipation or "push":** move a phrase's arrival note an 8th earlier (offset −0.5) or a 16th earlier (−0.25) onto the previous "and", tied over the barline. This is ubiquitous in pop, R&B, and afrobeats toplines.
- **Note density by role:**

| Role | Onsets per bar | Notes |
|---|---|---|
| Topline verse | 4–10 | follows speech rhythm |
| Chorus hook | 3–8 | longer notes, more held tones |
| Lead or drop riff | 4–12 | 16ths at 120–128 BPM |
| Trap bells | 4–8 at 140–160 BPM | half-time feel, lots of space |
| Counter-melody | about half the lead's density | fills the lead's rests |

- **Repeated-note hooks:** 3–6 repetitions of one pitch with rhythmic variety, then one move away. That creates surprise against stasis (Kylie's "Can't Get You Out of My Head" chorus is often cited as a repeated-note-heavy hook, an uncited observation).
- **Common rhythm cells** for 16th-grid placement, in beats (positions within one beat or bar):
  - Tresillo / 3-3-2: onsets at 0, 0.75, 1.5 (repeat each half bar). This is the core of afrobeats, dancehall, reggaeton, and trap bells.
  - Charleston: 0, 0.75 (dotted quarter then 8th).
  - Off-beat stab: 0.5, 1.5, 2.5, 3.5 (house).
  - Long-short-short: 0 (1.0), 1.0 (0.5), 1.5 (0.5).

### Gaps
- I found no study that quantifies "rhythm more memorable than pitch" directly. That claim rests on producer and educator sources, not research, in my notes.

---

## 6. What makes a hook catchy (earworm research, simplicity plus one surprise, repetition)

### Takeaway
The best evidence (Jakubowski et al.) says sticky tunes combine a *familiar* overall shape (a common contour) with *locally unusual* interval patterns (unexpected leaps or repeated notes), and they tend to be faster and more popular. Producer wisdom converges on the same formula: simple, repetitive material with one distinctive twist.

### Cited Findings
- **Study details.** Jakubowski, Finkel, Stewart & Müllensiefen, "Dissecting an Earworm: Melodic Features and Song Popularity Predict Involuntary Musical Imagery", *Psychology of Aesthetics, Creativity, and the Arts*. It was published online 3 Nov 2016, in the 2017 volume. — [Goldsmiths repository](https://research.gold.ac.uk/19405); [APA](https://www.apa.org/news/press/releases/2016/11/earworms)
- **Method.** About 3,000 participants named frequent earworms. Those tunes were compared with tunes never named as earworms but matched on popularity and recency in the UK charts. Genres were pop, rock, rap, and R&B; data were collected 2010–2013. — [Neuroscience News](https://neurosciencenews.com/song-stuck-in-head-5423/); [APA](https://www.apa.org/news/press/releases/2016/11/earworms)
- **Results.** Compared with a large pop corpus, earworms had more common global melodic contours, less common average gradients between turning points, and faster tempi. Chart success and recency also predicted earworm status. — [Durham repository (paper)](https://durham-repository.worktribe.com/OutputFile/1371487); [Goldsmiths](https://research.gold.ac.uk/19405)
- **Most-named earworms:** "Bad Romance" (Lady Gaga), "Can't Get You Out of My Head" (Kylie Minogue), "Don't Stop Believin'" (Journey), "Somebody That I Used to Know" (Gotye), "Moves Like Jagger" (Maroon 5). — [Neuroscience News](https://neurosciencenews.com/song-stuck-in-head-5423/)
- Jakubowski summarized sticky songs as having a fairly fast tempo, a common melodic shape, and unusual intervals or repetitions. — [Neuroscience News](https://neurosciencenews.com/song-stuck-in-head-5423/)
- **Producer guidance:**
  - Simple ideas are easier to process, recall, and sing.
  - Many iconic EDM melodies use surprisingly few notes.
  - Great hooks are rewritten (one note changed, a rhythm shifted, a phrase removed), and removing notes often helps more than adding them.
  - Every memorable drop has one element that becomes the section's identity.
  — [Lost Stories Academy: Science of EDM hooks](https://loststoriesacademy.com/blogs-and-tutorials/the-science-behind-catchy-edm-hooks); [Lost Stories: drops people remember](https://loststoriesacademy.com/blogs-and-tutorials/the-secret-to-writing-drops-that-people-actually-remember)
- Use only one lead sound at a time in a drop so listeners have one thing to latch onto. — [Bax-shop](https://www.bax-shop.co.uk/blog/dj-gear/edm-tips-tricks-how-to-make-the-ultimate-drop/)

### Inferences
- **Catchy-hook checklist** for an AI to score candidate motifs:
  1. Overall contour is a common shape (arch, or descending ending on 1, 3, or 5).
  2. The motif is 2–4 beats long, with 3–7 distinct notes and a range of 9 semitones or less.
  3. It is repeated at least twice within the hook, and the hook recurs at least 3 times per song section, so the listener hears it 4–8+ times per song.
  4. There is exactly one "surprise": an unexpected leap (6th, 7th, or octave), a chromatic or borrowed note, a rhythmic displacement, or a repeated-note run broken by a leap.
  5. The tempo or note rate is lively: for slow BPMs, use 8th or 16th subdivisions.
  6. It is singable or hummable: mostly steps, no awkward augmented intervals unless genre-appropriate.
  7. The hook title or main lyric lands on the climax or on the longest note.
- **Placement:** hooks belong in the first 5–15 seconds (intro tease), in the chorus or drop, and in the post-chorus or outro. In beat-making, the main melody loop usually *is* the hook and plays from bar 1, with the drums dropping in after 4–8 bars.

### Gaps
- The exact number of earworm vs control tunes (I believe 100 each) and the specific contour classes were not verified in-session, so they are not stated as fact.
- No research-backed "optimal number of repetitions" was found.

---

## 7. Genre melody styles

### Takeaway
Each genre has stock scale choices, rhythmic feels, and densities:
- **Trap/drill:** dark minor, harmonic minor, or Phrygian; simple repetitive bells or piano with octave doubling and space for the 808.
- **R&B:** pentatonic runs and melisma, usually descending at phrase ends.
- **EDM:** a simple, singable lead over a 4-chord loop, rhythm-led.
- **Amapiano and afrobeats:** jazzy 7th/9th harmony, piano leads, syncopated call and response with the log drum or groove.

### Cited Findings
- **Trap:**
  - Most trap melodies use natural minor, harmonic minor (raised 7th), or Phrygian (lowered 2nd). — [Production Music Live: 3 essential scales](https://productionmusiclive.com/blogs/news/trap-beat-guide-melodies-3-essential-scales-for-making-melodies)
  - Trap melodies are typically dark, sparse, minor-key, and simple or repetitive, because the 808 patterns underneath are complex. Plucks, arpeggios, bells, stabs, and synths are typical. Doubling the lowest chord note an octave below strengthens chords. A semitone interval sounds dark or dissonant. — [RouteNote: How to make trap melodies](https://create.routenote.com/blog/how-to-make-trap-melodies/)
- **R&B:**
  - R&B singers often improvise elaborate, usually *descending* melismas at phrase ends.
  - Runs are built from the pentatonic scale of the song's key (C major pentatonic: C D E G A).
  - Riffs are short complementary phrases; runs are longer, featured phrases.
  — [DeviantNoise: How to sing runs and riffs](https://deviantnoise.net/education/singing/how-to-sing-runs-riffs/); [MusicGurus: The pentatonic scale](https://www.musicgurus.com/courses/learn-to-sing-licks-riffs-runs-for-pop-singers/lessons/the-pentatonic-scale)
- **EDM:**
  - Most EDM sits on a simple emotional 4-chord loop (for example vi–IV–I–V).
  - The drop lead should be strong, singable, and not too busy. — [Bax-shop](https://www.bax-shop.co.uk/blog/dj-gear/edm-tips-tricks-how-to-make-the-ultimate-drop/)
- **Amapiano:**
  - Typical tempo is about 108–115 BPM.
  - Leads are smooth piano over minor-7th and 9th chords for a jazzy, melancholic feel; arpeggiators add flow.
  - The tuned log drum serves as bass and momentum and interacts with the drums.
  - Common tones between chords give a hypnotic synth melody.
  - Elements are introduced gradually.
  — [Beats To Rap On: Amapiano](https://beatstorapon.com/blog/how-to-make-amapiano-beat/); [SampleFocus: Amapiano](https://samplefocus.com/blog/start-making-amapiano-jazz-fusion-deep-house-music-2); [RouteNote amapiano guide](https://create.routenote.com/blog/beatmakers-guide-how-to-make-an-amapiano-beat/)
- **Afro and amapiano vocals:** call and response, with a group answering a sparse lead line to widen a refrain. Log-drum syncopation opens up off-grid pockets. — [Beats To Rap On](https://beatstorapon.com/blog/how-to-make-amapiano-beat/)

### Inferences (style recipes; uncited unless noted above)
- **Trap/drill bell or piano loop.** 2 bars, 130–160 BPM (half-time feel; drill about 140–145). Key A minor, using harmonic minor for the G# (or Phrygian Bb). Chords Am | F | Dm | E.
  - Bar 1:
    - `0.0:A4 69:0.5`
    - `0.5:C5 72:0.5`
    - `1.0:E5 76:0.75`
    - `1.75:C5 72:0.25`
    - `2.0:B4 71:0.5`
    - `2.5:A4 69:0.5`
    - `3.0:E4 64:1.0`
  - Bar 2:
    - `4.0:F5 77:0.75` (b6, dark)
    - `4.75:E5 76:0.25`
    - `5.0:C5 72:0.5`
    - `5.5:B4 71:0.5`
    - `6.0:G#4 68:1.5` (harmonic-minor leading tone over E)
    - rest at 7.5
  - Phrygian flavor: replace B4 71 with Bb4 70 (b2).
  - Range is E4–F5 (64–77), 13 semitones.
  - Double the whole loop an octave below (−12) at lower velocity for weight, or an octave above for the bell shimmer.
  - Keep pitches 52 and below free for the 808. Use velocities 80–110 with slight variation.
- **Drill:** similar dark minor, with more sliding, triplet-feel 8ths in the counter-melody and frequent b2 or b6 neighbor tones. Melodies often sit in a high register with a contrasting low piano or strings.
- **Lo-fi or jazzy:**
  - Melody targets the 7ths and 9ths of maj7, m7, and m9 chords.
  - Use slow 8th-note lines with lazy swing (16th swing about 55–62%) and rests.
  - Bias toward pentatonic or Dorian.
  - Humanize: timing ±10–20 ms, velocity 60–95.
  - End phrases on the 9th or maj7 rather than the root, to stay unresolved and dreamy.
- **R&B run** (descending C major pentatonic run ending on a chord tone, 16th-note triplets):
  - A4 69, G4 67, E4 64, D4 62, C4 60, then a long E4 64 or C4 60.
  - Put the run at phrase ends; keep the phrase body mostly syllabic.
  - Minor-pentatonic or blues runs add b3 and b7 (A minor pentatonic: A C D E G).
- **Pop topline:**
  - Verses are rhythmically speech-like in a narrow range (5–9 semitones) with many repeated notes.
  - Pre-chorus rises (an ascending sequence).
  - The chorus is about 3–5 semitones higher, with longer notes and the title on the climax or the downbeat. It is often a 2-bar call plus 2-bar response.
- **EDM lead or drop:**
  - A 1- or 2-bar riff of 4–8 notes, repeated 4× with a changed ending on the 4th repetition (A A A A').
  - Mostly chord tones over a vi–IV–I–V loop, played as a 16th or syncopated 8th rhythm.
  - Call-and-response between the lead and a vocal chop, or between high and low octaves.
  - Super-saw leads are often stacked in octaves.
- **House stabs:** 1–3-note chord stabs (m7 or m9 voicings) on off-beats ("and" positions), or tresillo-style 3-3-2 patterns. The melodic content is in the top voice of the stab, which moves by step.
- **Cinematic theme:**
  - Slow tempo, long notes, arch contour.
  - An opening leap of a 5th or 6th that is then filled by step (gap-fill).
  - The motif is augmented in later statements and reharmonized.
  - Peak once near the end of the theme.
- **Afrobeats or amapiano:**
  - Pentatonic or major-mode toplines with lots of repeated notes and 3-3-2 syncopation.
  - Short call-and-response phrases (1 bar call, 1 bar response).
  - Piano leads on m7 or m9 chords using common tones.
  - The log drum is a melodic bass voice (slides between chord roots), so keep the lead above about C4.

### Gaps
- No primary sources were retrieved for lo-fi, house-stab, drill, cinematic, or afrobeats (as distinct from amapiano) melodic conventions. Those recipes are inference and practitioner knowledge, not cited.
- Attack Magazine, Splice, and Native Instruments articles were not fetched because of tool-call limits.

---

## 8. Counter-melodies and layering

### Takeaway
Use *parallel* motion (octaves, 3rds, 6ths) when you want a thicker single line. Use *contrary* or *oblique* motion and complementary rhythm when you want an independent counter-melody. Parallel 5ths and octaves erase independence. They are fine (even idiomatic) for doubling or power-chord color in popular music.

### Cited Findings
- **Why parallel 5ths and octaves are avoided:** they reduce the independence of the voices. Octaves function as doublings, and successive 5ths create ambiguity. — [Wikipedia: Consecutive fifths](https://en.wikipedia.org/wiki/Consecutive_fifths)
- **Four types of motion:**
  - Parallel: same direction, same interval.
  - Similar: same direction, different interval.
  - Contrary: opposite directions.
  - Oblique: one voice holds while the other moves.
  - Contrary and oblique motion keep voices independent. — [Wikipedia: Consecutive fifths](https://en.wikipedia.org/wiki/Consecutive_fifths)
- **Hidden (direct) 5ths/octaves:** a 5th or octave approached by similar motion. These are generally avoided in the outer voices unless the upper voice moves by step. — [Wikipedia: Consecutive fifths](https://en.wikipedia.org/wiki/Consecutive_fifths)
- Parallel 5ths are common and acceptable in popular and folk music, such as rock power chords; the prohibition is a classical convention. — [Wikipedia: Consecutive fifths](https://en.wikipedia.org/wiki/Consecutive_fifths)

### Inferences
- **Layering recipes:**

| Recipe | How | Use / effect |
|---|---|---|
| Octave doubling (±12) | copy and transpose | thickness, trap bells, EDM leads; lower the doubled layer's velocity 10–20% |
| Diatonic 3rds above or below | shift each note ±2 scale steps; in major this is ±3 or ±4 semitones depending on the degree | sweet, pop or R&B harmonies |
| Diatonic 6ths below | invert the 3rd: −8 or −9 semitones | warmer, wider than 3rds |
| Mixed 3rds and 6ths | — | keeps the harmony inside the chord; check that each harmony note fits the current chord |

- **Independent counter-melody rules:**
  1. Fill the lead's rests: place counter-melody onsets where the lead holds or rests.
  2. Use contrary motion at phrase boundaries and when the lead leaps.
  3. Keep at least 3 semitones apart and avoid crossing the lead's register.
  4. Use about half the lead's note density, or the opposite density (long notes under a busy lead, busy arpeggio under a sustained lead).
  5. Avoid consecutive perfect 5ths or octaves between lead and counter-line on successive strong beats.
  6. Favor 3rds, 6ths, and 10ths on strong beats.
  7. Give the counter-line its own register band: about an octave below or above, or the mid range under a high lead.
- **Worked counter-line** under the period example in section 3 (C | G | Am | F):
  - Sustained guide tones, one per half-bar: E3 52, G3 55 | D3 50, F3 53 | C3 48, E3 52 | A2 45, C3 48.
  - These are 3rds and 5ths of each chord, moving by step or small skip, often contrary to the lead's arch.
- **Bass vs melody:** outer voices (melody and bass or 808) should mostly move contrary or oblique. Avoid the 808 doubling the melody's note at the octave on downbeats if both should be heard as separate parts.

### Gaps
- No producer-oriented source on counter-melody density ratios was retrieved. The density guidance is inference.

---

## 9. Practical step-by-step methods producers use

### Takeaway
Producer methods are reliable because they constrain choices: start from chords (or a loop), fix the rhythm first, limit pitches to a pentatonic or a few chord tones, write a 1–2-bar motif, then answer it, then refine by subtraction.

### Cited Findings
- Start from a simple 4-chord loop and write a singable, not-too-busy lead over it. — [Bax-shop](https://www.bax-shop.co.uk/blog/dj-gear/edm-tips-tricks-how-to-make-the-ultimate-drop/)
- Refine hooks iteratively: change one note, shift a rhythm, remove a phrase. — [Lost Stories Academy](https://loststoriesacademy.com/blogs-and-tutorials/the-secret-to-writing-drops-that-people-actually-remember)
- Choose run and melisma notes from the key's pentatonic scale. — [MusicGurus](https://www.musicgurus.com/courses/learn-to-sing-licks-riffs-runs-for-pop-singers/lessons/the-pentatonic-scale)
- Keep trap melodies simple and repetitive to leave room for the 808. — [RouteNote](https://create.routenote.com/blog/how-to-make-trap-melodies/)
- Balance rise and fall, and use a single peak note. — [Ableton](https://makingmusic.ableton.com/creating-melodies-1-contour)

### Inferences: algorithm for an FL Studio piano-roll AI

1. **Set the context.**
   - Key and scale, by genre: trap uses natural, harmonic minor, or Phrygian; pop and EDM use major or Aeolian; lo-fi uses Dorian with maj7 color; afro uses major pentatonic.
   - BPM.
   - Loop length: 2, 4, or 8 bars.
   - Chord progression, one chord per bar or two per bar.
2. **Rhythm first.** Generate a 1- or 2-bar rhythm with 4–8 onsets per bar, at least one syncopation or push, and at least one rest. Reuse it for the answer phrase.
3. **Pitch skeleton.** On each strong-beat onset, place a chord tone, preferring the 3rd, then the 5th, then the 7th or 9th by genre. Keep the root for the final cadence.
4. **Fill.** Connect skeleton notes with passing or neighbor tones on weak onsets. Keep 65–80% steps. If a leap of 5 semitones or more occurs, follow it with stepwise motion in the opposite direction.
5. **Call and response.**
   - Bars 1–2 end on an unstable degree (2, 5, or 7).
   - Bars 3–4 repeat bars 1–2 with a tail change ending on 1 or 3.
   - For 8 bars, use the period or the sentence 2+2+4.
6. **Climax.** Make exactly one note the highest in the phrase. Place it on a strong beat at 55–75% of the phrase. Make it the "one surprise" (a bigger leap, a borrowed note, or a long hold).
7. **Range check.** Vocal toplines span 14 semitones or less, within the voice window. Bells and leads can span about 24 semitones including doubling. Keep the lead above the 808 and bass register (about 52+).
8. **Develop across the song.**
   - Verse: lower and narrower.
   - Pre-chorus: ascending sequence.
   - Chorus or drop: higher, with longer notes.
   - Use augmentation for a half-time drop, diminution for build-ups, displacement for variation every 4th or 8th bar.
9. **Layer.** Add octave doubling (±12) and/or a 3rds/6ths harmony. Add a sparse counter-melody that fills the rests with contrary motion.
10. **Refine by subtraction.** Remove 10–20% of notes. Check that the motif is still recognizable after 4 repeats and that the melody implies the harmony when soloed.
11. **Humanize** by genre: velocity variation ±10–15; slight timing offsets for lo-fi and R&B; tight quantization for EDM and trap.

### Gaps
- Splice, Attack Magazine, Point Blank, and Native Instruments melody articles were not fetched (tool-call budget), so method steps are not attributed to those outlets specifically.
- "Sing or hum first" is common practitioner advice, but I did not retrieve a source for it in-session.
