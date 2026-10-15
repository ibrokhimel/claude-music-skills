# Motifs, development operations, phrase templates, song-level development, counter-melodies

How a 2–7-note idea becomes an 8-bar hook and then a whole song's melodic plan, written as operations on note lists `(start_beat, midi, length_beats, velocity)` that Claude can run directly.

## Contents
1. Motif: definition and size
2. Development operations (table and Python)
3. Worked demo: one motif through every operation
4. Rule of three and hook-loop shapes
5. Phrase templates: call and response, period, sentence, 4- and 8-bar loops, odd lengths
6. Song-level development (verse, pre, chorus, drop, bridge)
7. Counter-melodies and layering
8. Sources

---

## 1. Motif: definition and size

A motif is "the smallest structural unit possessing thematic identity". It can be melodic, harmonic or rhythmic. A rhythmic motif is a rhythm abstracted from a melody, as in Beethoven's Fifth, whose short-short-short-long cell returns in many permutations **(sourced: Wikipedia, Motif)**.

Sizes **(convention)**:
- Motif: 2–7 notes over 2–4 beats (hook motif: 3–7 distinct notes, span ≤ 9 semitones).
- Phrase: 2–4 bars. Period or sentence: 8 bars. Beat loops: 2, 4 or 8 bars.
- The motif's identity lives mostly in its **rhythm + contour**. Keep those two constant when developing it, and let pitches adapt to the chords.

## 2. Development operations

The operations are standard theory; their effects are convention.

| Technique | Operation on the note list | Effect |
|---|---|---|
| Exact repetition | `start += N` beats | identity, memorability |
| Real transposition | `midi += k` | same shape, new colour; may leave the key |
| Diatonic sequence | shift each note by k scale steps | stays in key; the pop/EDM default; Sloboda links sequences with tears |
| Inversion (chromatic) | `midi' = 2*axis - midi` | mirrored "answer"; may leave the key |
| Inversion (diatonic) | mirror in scale steps around an axis degree | mirrored answer that stays in key |
| Retrograde | reverse pitch order (keep rhythm), or reverse pitches and rhythm | subtle variation, less recognisable |
| Augmentation | starts and lengths ×2 | broadening; half-time drops, cinematic restatements |
| Diminution | starts and lengths ×0.5 | urgency; build-ups |
| Rhythmic displacement | `start += 0.25` or `0.5` | syncopated renewal (trap, afro); same notes, new accent |
| Fragmentation | repeat the head (or tail) 2–3 notes | continuations, builds, the sentence's middle |
| Tail change | keep the first ~70%, change the last 1–2 notes | question → answer (the main hook variation) |
| Interval expansion | widen one interval (e.g. 3 → 5 semitones) | the climax surprise |
| Chord adaptation | keep rhythm and contour, snap pitches to the new chord's tones | the EDM/afro riff-over-changes method (Ex 6) |

```python
MAJOR = [0, 2, 4, 5, 7, 9, 11]          # use any scale list from make_midi_template.SCALES

def to_deg(m, tonic, scale):            # MIDI -> absolute scale-degree index (m must be in scale)
    pc, octv = (m - tonic) % 12, (m - tonic) // 12
    return octv * len(scale) + scale.index(pc)

def from_deg(d, tonic, scale):
    octv, i = divmod(d, len(scale))
    return tonic + 12 * octv + scale[i]

def repeat(n, beats):   return [(s + beats, m, l, v) for s, m, l, v in n]
def transpose(n, k):    return [(s, m + k, l, v) for s, m, l, v in n]
def displace(n, d):     return [(s + d, m, l, v) for s, m, l, v in n]
def invert(n, axis):    return [(s, 2 * axis - m, l, v) for s, m, l, v in n]

def diatonic_shift(n, k, tonic=60, scale=MAJOR):
    return [(s, from_deg(to_deg(m, tonic, scale) + k, tonic, scale), l, v) for s, m, l, v in n]

def diatonic_invert(n, axis, tonic=60, scale=MAJOR):
    a = to_deg(axis, tonic, scale)
    return [(s, from_deg(2 * a - to_deg(m, tonic, scale), tonic, scale), l, v) for s, m, l, v in n]

def retrograde_pitch(n):                # reverse pitches, keep the rhythm
    ps = [m for _, m, _, _ in n][::-1]
    return [(s, p, l, v) for (s, _, l, v), p in zip(n, ps)]

def retrograde(n):                      # reverse pitches and rhythm
    t0, end = min(s for s, *_ in n), max(s + l for s, _, l, _ in n)
    return sorted((t0 + end - (s + l), m, l, v) for s, m, l, v in n)

def scale_time(n, f, origin=0.0):       # f=2 augmentation, f=0.5 diminution
    return [(origin + (s - origin) * f, m, l * f, v) for s, m, l, v in n]
```

`tonic` is any MIDI note of the key's tonic (60 for C, 57 for A minor). For minor keys, pass the minor scale list. Diatonic 3rds above = `diatonic_shift(n, 2)`; diatonic 6ths below = `diatonic_shift(n, -5)` **(derived)**.

## 3. Worked demo: one motif through every operation

Motif M in C major, a 3-beat "short-short-long-long": `0:64:0.5  0.5:67:0.5  1:69:1  2:67:1` (E4 G4 A4 G4). These outputs were computed with the code above (format `start:midi:len`).

| Operation | Result | Notes |
|---|---|---|
| repeat +4 beats | 4:64:0.5  4.5:67:0.5  5:69:1  6:67:1 | |
| real transpose +2 | 0:66  0.5:69  1:71  2:69 | F#4 leaves C major |
| diatonic +1 step | 0:65  0.5:69  1:71  2:69 | F A B A, in key |
| diatonic −1 step | 0:62  0.5:65  1:67  2:65 | D F G F |
| diatonic 3rds above (+2 steps) | 0:67  0.5:71  1:72  2:71 | G B C B; intervals 3, 4, 3, 4 |
| chromatic inversion, axis E4 | 0:64  0.5:61  1:59  2:61 | C#4 leaves the key |
| diatonic inversion, axis E4 | 0:64  0.5:60  1:59  2:60 | E C B C, in key |
| retrograde (pitch only) | 0:67  0.5:69  1:67  2:64 | G A G E |
| retrograde (pitch + rhythm) | 0:67:1  1:69:1  2:67:0.5  2.5:64:0.5 | long-long-short-short |
| augmentation ×2 | 0:64:1  1:67:1  2:69:2  4:67:2 | 6 beats |
| diminution ×0.5 | 0:64:0.25  0.25:67:0.25  0.5:69:0.5  1:67:0.5 | 1.5 beats |
| displacement +0.5 | 0.5:64  1:67  1.5:69  2.5:67 | the A now syncopates across beat 2 |
| fragmentation + sequence | 0:64 0.5:67 / 1:65 1.5:69 / 2:67 2.5:71 (all 0.5) | head E–G climbing by step: builds |
| tail change (answer) | 0:64 0.5:67 1:69 **2:72:1** | ends on C5 = 1 (resolved) instead of G |
| interval expansion | 0:64 0.5:67 **1:74:1** 2:72:1 | the G–A step becomes a G–D 5th; gap-fill to C |

## 4. Rule of three and hook-loop shapes

Rule of three **(convention)**: state, repeat (exact or sequenced), then **break the pattern on the third statement** (extend it, leap to the climax, or cadence). The common forms are A A A′ B, A A′ A B′, and the sentence (idea, repetition, continuation). Ex 8 (drill) uses it at pair level: statement, sequence, break-to-climax, cadence.

The repetition science behind this **(sourced)**:
- Over 90% of music people hear is music they have heard before (Huron, cited by Margulis).
- A phrase repeated exactly about ten times starts to sound sung (Deutsch's speech-to-song illusion), but not if the repeats are transposed or jumbled. Exact-pitch repetition makes a chop or riff melodic.
- Identical repetition lowers liking (Gold et al. 2019). Keep the hook constant and vary its surroundings (drums, harmony, register, layer) on each return.

Loop shapes for beats **(convention)**:

| Length | Shape | Use |
|---|---|---|
| 1 bar | motif + rest | drill/trap cold motif with an empty answer bar |
| 2 bars | call (ends on 2/5/7) + response (ends on 1/3) | most beat loops, afro, EDM |
| 4 bars | A A′ (2+2) or A A A′ B (1 bar each) | trap bells, lo-fi, EDM drop |
| 8 bars | period (4+4) or sentence (2+2+4) | toplines, themes, full hooks |

**Loop seam:** the last note should lead into the first one by step, by the leading tone, or by a pickup on the last off-beat. Then the loop sounds composed, not cut (Ex 1: G#4 → A4; Ex 6: D5 → E5) **(derived)**.

## 5. Phrase templates

**Call and response** **(convention)**:
- The call is 1–2 bars and ends unresolved (degree 2, 5 or 7, or an ascending contour).
- The response is 1–2 bars and ends resolved (1 or 3). It is often answered in another register, by another instrument, or with the call's contour inverted.
- In EDM and afro, the response can be a vocal chop or a second synth. In afro and amapiano vocals, a group answers a sparse lead line to widen the refrain **(sourced: Beats To Rap On)**.

**Period, 8 bars (4 + 4)** **(sourced definition: Wikipedia, Sentence; proportions convention)**:
- Antecedent (bars 1–4): ends on an unstable degree (2, 5 or 7), usually over V. This is the half cadence (the question).
- Consequent (bars 5–8): starts like the antecedent, then changes its tail to end on 1 (or 3) over I. This is the authentic cadence (the answer).
- Worked: Ex 2.

**Sentence, 8 bars (2 + 2 + 4)** **(sourced: Schoenberg via Wikipedia; 2+2+4 is standard Caplin teaching)**:
- Bars 1–2: basic idea (BI).
- Bars 3–4: BI repeated or sequenced (e.g. tonic version → dominant version).
- Bars 5–6: fragments of the BI in 1-bar or half-bar units, rising in energy (fragmentation + sequence).
- Bars 7–8: cadence.
- Schoenberg considered it the higher form because development starts immediately.
- Worked sentence in A minor, checked with `check_melody`: 71% steps, 3% leaps, range 60–69, climax once at 69%, every strong beat a chord tone. Harmonic rhythm doubles in the continuation, as is typical. Chords: Am | F | Dm | G7 | C Dm | C F | G E7 | Am.

```
# BI, bars 1-2 (Am | F): long-short head, step fill
0.0   : 64 : 0.75 : 96    # E4 5th
0.75  : 64 : 0.25 : 80
1.0   : 60 : 0.5  : 86    # C4 3rd
1.5   : 62 : 0.5  : 80    # D4 passing
2.0   : 64 : 2.0  : 92    # E4
4.0   : 65 : 1.0  : 94    # F4 root of F
5.0   : 64 : 1.0  : 80    # E4 maj7 (weak)
6.0   : 60 : 2.0  : 88    # C4 5th
# repetition, bars 3-4 (Dm | G7): diatonic sequence +1 step
8.0   : 65 : 0.75 : 96
8.75  : 65 : 0.25 : 80
9.0   : 62 : 0.5  : 86
9.5   : 64 : 0.5  : 80
10.0  : 65 : 2.0  : 92
12.0  : 67 : 1.0  : 94
13.0  : 65 : 1.0  : 80    # F4 7th of G7
14.0  : 62 : 2.0  : 88
# continuation, bars 5-6 (C Dm | C F): head fragment (X X, step down) climbing by step
16.0  : 64 : 0.75 : 96
16.75 : 64 : 0.25 : 80
17.0  : 62 : 1.0  : 84
18.0  : 65 : 0.75 : 98
18.75 : 65 : 0.25 : 82
19.0  : 64 : 1.0  : 86
20.0  : 67 : 0.75 : 102
20.75 : 67 : 0.25 : 84
21.0  : 65 : 1.0  : 88
22.0  : 69 : 1.0  : 115   # A4 CLIMAX over F, 69%; the repeated note is dropped (liquidation)
23.0  : 67 : 0.5  : 86
23.5  : 65 : 0.5  : 84
# cadence, bars 7-8 (G E7 | Am): motif rhythm gone, 5-3-2 down to 3
24.0  : 67 : 2.0  : 94
26.0  : 64 : 1.0  : 88    # E4 root of E7
27.0  : 62 : 1.0  : 86    # D4 7th of E7
28.0  : 60 : 3.5  : 92    # C4 3rd of Am (use A3 57 for a final 1); ends 31.5
```

**4-bar loop template** **(convention)**:
- Bar 1: motif (rhythm R, ends on a chord tone).
- Bar 2: same rhythm R, sequenced or inverted to fit chord 2.
- Bar 3: varied rhythm, climbs to the climax at 62.5%.
- Bar 4: tail toward the loop seam, ending on 2, 5 or 7 so the loop pulls back.
- Worked: Ex 1, Ex 6, Ex 7.

**Odd lengths.** Pattison's prosody teaching treats even phrase counts with matched lengths as stable, and odd counts or mismatched lengths as unstable **(sourced: Pattison/Berklee)**. Use a 3- or 5-bar pre-chorus, or a 3-bar phrase plus a 1-bar fill, when you want to destabilise on purpose.

## 6. Song-level development

**(convention)**

| Section | Range and register | Density | Operations |
|---|---|---|---|
| Intro | hook fragment or full hook, filtered | low | fragmentation; tease the hook in the first 5–15 s |
| Verse | low, narrow (5–9 semitones) | speech-like 4–10 onsets | repeated notes, small steps, inverted arch |
| Pre-chorus | rising | increasing | ascending diatonic sequence, diminution, odd length allowed |
| Chorus / hook | 3–5 semitones higher than the verse, peak +2–5 | 3–8 onsets, longer notes | arch, title on the climax or the longest note, call + response |
| Post-chorus / drop | hook as instrument or chop | riff density 4–12 | exact repetition, A A A A′, octave stacking |
| Half-time drop | same hook | halved | augmentation ×2 |
| Build-up | hook head | doubling every 2–4 bars | fragmentation + diminution (1 bar → ½ → ¼) |
| Bridge | new contour, new register | contrast | inversion or retrograde of the hook, borrowed chord |
| Final chorus | +12 layer, optional +1/+2 key lift (trance, pop) | full | same hook, new surroundings |

Placement **(convention)**: tease the hook early, give it in full at the chorus or drop, and restate it in the post-chorus or outro. In beat-making, the main melody loop usually is the hook and plays from bar 1, with drums entering after 4–8 bars. Arrangement bar counts and energy curves: `music-arrangement`.

## 7. Counter-melodies and layering

**Why.** Parallel 5ths and octaves are avoided in classical writing because they erase the independence of the voices. Contrary and oblique motion preserve it. Parallel 5ths remain idiomatic in rock power chords and folk **(sourced: Wikipedia, Consecutive fifths)**. Hidden 5ths and octaves (approached by similar motion) are avoided in outer voices unless the upper voice moves by step **(sourced)**.

**Mode 1: thicken one line (parallel)** **(convention)**:

| Recipe | How | Effect |
|---|---|---|
| Octave doubling | copy at ±12, velocity −10–20% | width and weight; trap bells, EDM leads, supersaw stacks |
| Diatonic 3rds above | `diatonic_shift(n, 2)` | sweet; pop and R&B harmonies |
| Diatonic 6ths below | `diatonic_shift(n, -5)` | warmer and wider than 3rds |
| Mixed 3rds and 6ths | choose per note | keep each harmony note inside the current chord; fix clashes by hand |

**Mode 2: true counter-melody (independent)** **(convention)**:
1. **Fill the lead's rests**: put counter onsets where the lead holds or rests.
2. **Contrary motion** at phrase boundaries and against the lead's leaps. Use **oblique** motion (hold) under the lead's busy passages.
3. **Register separation**: stay at least 3 semitones from the lead and never cross it. Give it its own band, about an octave below or above, or the mid range under a high lead.
4. **Complementary density**: about half the lead's onsets, or the opposite texture (long notes under a busy lead, a busy arpeggio under a sustained lead).
5. **Strong-beat intervals**: favour 3rds, 6ths and 10ths. Avoid consecutive perfect 5ths or octaves on successive strong beats.
6. **Material**: guide tones (3rds and 7ths moving by step) are the safest counter-line. A rhythmic answer echoing the motif's head is the most "hooky" one.
- Trap counter-melodies often use only the root, octave, 5th and m7 **(sourced: NI trap guide)**. Drill counter-lines often use triplet-feel 8ths and b2/b6 neighbours **(convention)**.
- Worked: Ex 3 (under Ex 2).

**Outer voices.** Melody against bass or 808 should move mostly contrary or oblique. Do not let the 808 double the melody's note at the octave on downbeats if both should read as separate parts. Bass note choice: `music-bass-808`.

**Call and response between instruments.** Lead plays bars 1 and 3, the counter or chop answers in bars 2 and 4, so each fills the other's rests. This is the drill "empty bar" idea (Ex 8, shifted +4 beats) and the afro/EDM vocal-chop answer.

Quick independence check (run alongside `check_melody`):

```python
def parallel_perfects(lead, ctr, loop_beats):
    def at(n, t):
        return next((m for s, m, l, _ in n if s <= t < s + l), None)
    hits, prev = [], None
    for t in range(0, int(loop_beats), 2):               # beats 1 and 3
        a, b = at(lead, t), at(ctr, t)
        cur = None if a is None or b is None else ((a - b) % 12, a)
        if cur and prev and cur[0] in (0, 7) and cur[0] == prev[0] and cur[1] != prev[1]:
            hits.append(t)
        prev = cur
    return hits                                            # [] = no parallel 5ths/8ves
```

## 8. Sources

- Motif — https://en.wikipedia.org/wiki/Motif_(music)
- Sentence and period (Schoenberg; Beethoven Op. 2 No. 1) — https://en.wikipedia.org/wiki/Sentence_(music)
- Pattison prosody, stable and unstable phrase groupings — https://www.coursera.org/learn/songwriting-lyrics
- Consecutive and hidden fifths, types of motion — https://en.wikipedia.org/wiki/Consecutive_fifths
- Lost Stories Academy (repeat with small changes; subtraction) — https://loststoriesacademy.com/blogs-and-tutorials/the-science-behind-catchy-edm-hooks
- Margulis on repetition — https://blog.oup.com/2014/01/music-repetition-neuroscience/ ; Deutsch speech-to-song — https://deutsch.ucsd.edu/psychology/pages.php?i=212 ; Gold et al. 2019 — https://pmc.ncbi.nlm.nih.gov/articles/PMC6867811
- Sloboda 1991 (sequences and appoggiaturas linked to tears) — https://www.npr.org/2012/02/13/146818461/the-ballad-of-the-tearful-why-some-songs-make-you-cry
- NI trap guide (counter-melody from root, octave, 5th, m7) — https://blog.native-instruments.com/how-to-make-a-trap-beat/
- Beats To Rap On, amapiano call and response — https://beatstorapon.com/blog/how-to-make-amapiano-beat/
