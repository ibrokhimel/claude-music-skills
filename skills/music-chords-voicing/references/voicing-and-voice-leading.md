# Voicing and voice leading: function, cadences, voicing shapes, register floors, and the nearest-voicing algorithm

This file covers how to turn chord symbols into MIDI notes that sound clear ("expensive") rather than muddy, and how to connect chords smoothly. Pitches use C4 = 60; FL Studio labels MIDI 60 as "C5". Chord formulas and diatonic tables are in `music-theory-core` (`references/theory-tables.md` §7 and §10). Every voicing in backticks was checked by script for chord tones, the low-interval limits, and parallel 5ths and octaves.

## Contents
1. Function and cadences
2. Voicing types with MIDI examples
3. Low-interval limits and register floors
4. Rules for an expensive sound: extensions, omissions, avoid-notes
5. The nearest-voicing algorithm (manual procedure plus Python)
6. Guide tones, common tones and the top-voice line
7. Sources

---

## 1. Function and cadences

| Family | Major-key chords | Minor-key chords | Job |
|---|---|---|---|
| Tonic | I, vi, (iii) | i, III, (VI) | rest, home |
| Predominant | IV, ii | iv, ii°, VI | departure |
| Dominant | V, vii° | V (harmonic minor), vii°, (v, VII are weak) | tension that wants home |

- Default motion is T → PD → D → T.
- Root motion strength **(convention)**:
  - Down a 5th (up a 4th) is the strongest "forward" move.
  - Down a 3rd is smooth, because the chords share two notes.
  - Up a step is the rock lift (IV–V, bVI–bVII).
  - Up a 5th (down a 4th) is softer and plagal.
- V7→I resolves through its tritone. In G7 (67 71 74 77), B rises to C (71→72) and F falls to E (77→76), so the tritone collapses onto C–E **(derived)**.

Cadences, spelled in C (bass | upper):

| Cadence | Spelling | Effect |
|---|---|---|
| Perfect authentic | `G7 43 | 53 55 59` → `C 48 | 52 55 60` | full stop: F→E, B→C, tonic on top |
| Imperfect authentic | `G7 43 | 55 59 65` → `C 48 | 55 60 64` | softer stop: E on top, not C |
| Half | `Dm 50 | 62 65 69` → `G 43 | 62 67 71` | comma: ends a verse or pre-chorus open |
| Plagal | `F 41 | 60 65 69` → `C 48 | 60 64 67` | "amen"; also the pop IV–I |
| Minor plagal | `Fm 41 | 60 65 68` → `C 48 | 60 64 67` | tears: the A→Ab→G line |
| Deceptive | `G7 43 | 53 55 59` → `Am 45 | 52 57 60` | surprise: the voices resolve, but the bass steps G→A |
| Phrygian half (A minor) | `Dm/F 41 | 57 62` → `E 40 | 56 59 64` | flamenco pull: bass semitone F→E |
| Backdoor | `Fm7 41 | 56 60 63` → `Bb7 46 | 56 62 65` → `Cmaj7 48 | 55 59 64` | soulful soft landing |

Loop rule **(sourced, Native Instruments; convention)**: loop genres such as trap, drill, lo-fi and house avoid a full V7→I inside the loop, so the loop never "ends". They either leave out I or end on V so the loop restarts. Save the strong authentic cadence for:
- song endings;
- the pre-chorus → chorus lift;
- R&B and gospel turnarounds.

---

## 2. Voicing types with MIDI examples

| Type | How to build it | Example | Use |
|---|---|---|---|
| Closed | all upper voices within an octave | `Cmaj7 48 | 60 64 67 71` | dense; stabs, pop keys |
| Open / spread | spread over more than an octave, wide at the bottom | `Cmaj7 48 | 55 64 71` | big, clear, piano and strings |
| Drop-2 | take a closed 4-note chord and drop the 2nd-highest note an octave | closed 60 64 67 71 → `Cmaj7 48 | 55 60 64 71` | the smooth 4-voice keys and guitar standard |
| Drop-3 | drop the 3rd-highest note an octave | `Cmaj7 48 | 52 60 67 71` | wider; good left-hand shape |
| Shell | root + 3rd + 7th only | `Cmaj7 48 | 59 64`, `G7 43 | 53 59` | minimum clear function; leaves room |
| Rootless A form (3-7-9-5 / 7-9-3-13) | the bass or 808 has the root; the keys play 3, 5, 7, 9 or 7, 9, 3, 13 | `Dm9 38 | 53 57 60 64`, `G13 43 | 53 57 59 64`, `Cmaj9 36 | 52 55 59 62` | jazz, R&B, neo-soul, lo-fi |
| Rootless B form (7-9-3-5 / 3-13-7-9) | the A form inverted | `Dm9 38 | 60 64 65 69`, `G13 43 | 59 64 65 69`, `Cmaj9 36 | 59 62 64 67` | the same, one register up |
| Quartal ("So What") | stacked 4ths with a major 3rd on top | `Dm11 38 | 50 55 60 65 69` (D G C F A) | modal, ambient, neo-soul |
| Spread 10th | left hand plays root + 10th, right hand plays a close cluster above | `Cmaj9 36 | 48 64 67 71 74` | ballad piano, cinematic |
| sus2 / sus4 | 2 or 4 replaces the 3rd | `Csus2 48 | 60 62 67`; `G9sus4 43 | 53 57 60 62` (F/G) | open, ambiguous; gospel and house dominants |
| add9 (open) | triad plus 9, with the 9 placed high | `Cadd9 48 | 55 64 74` | pop shimmer, future bass |
| m(add9) | minor triad plus 9, no 7 | `Am(add9) 45 | 57 60 64 71` | sad-beautiful trap and emo piano |
| 6/9 | 1 3 5 6 9, often voiced in 4ths | `C6/9 48 | 52 57 62 67` | open final chord, neo-soul |
| Power (5) | root + 5th (+ octave) | `C5 36 | 43` or `C5 48 | 55 60` | neutral; the only shape safe very low |
| Slash (upper triad over bass) | foreign triad over the bass | `Bb/C 48 | 58 62 65` (= C9sus4/C11 sound); `F/G 43 | 53 57 60` | gospel, house, pop pre-chorus |

The bass names the chord:
- A rootless Am9 (C E G B) is literally a Cmaj7 shape: `Am9 45 | 60 64 67 71`.
- The upper notes of Ebmaj7 (G Bb D) are a Gm triad.
- So chords can change while the hands stay still, which is the cheapest "expensive" voice leading there is (see library entries 2 and 22).

Inversions: C/E = `C/E 52 | 55 60 64` puts the 3rd in the bass, for smooth stepwise bass lines.

---

## 3. Low-interval limits and register floors

A low-interval limit is the lowest register where an interval still sounds clear before it turns to mud. Consonant intervals can sit lower than dissonant ones **(sourced: Robin Hoffmann; Sleepfreaks)**. The values below are commonly reproduced Berklee-style arranging figures. They are **approximate (convention)**: the source chart is an image, sources differ by a semitone or two, and soft or dark timbres forgive more than bright, loud ones. Read each value as "the lower note of the interval should be at or above this MIDI note".

| Interval (semitones) | Lowest lower note | FL label |
|---|---|---|
| minor 2nd (1) | E3 = 52 | E4 |
| major 2nd (2) | Eb3 = 51 | D#4 |
| minor 3rd (3) | C3 = 48 | C4 |
| major 3rd (4) | Bb2 = 46 | A#3 |
| perfect 4th (5) | Bb2 = 46 | A#3 |
| tritone (6) | B2 = 47 | B3 |
| perfect 5th (7) | Bb1 = 34 | A#2 |
| minor 6th (8) | G2 = 43 | G3 |
| major 6th, minor 7th, major 7th (9–11) | F2 = 41 | F3 |
| minor 9th (13) | E2 = 40 | E3 |
| major 9th (14) | Eb2 = 39 | D#3 |
| major 10th (16) | Bb1 = 34 | A#2 |

Why this works **(sourced: Plomp & Levelt 1965)**: two tones sound rough when they fall inside one critical band, and in semitone terms that band is wider at low frequencies. The harmonic series of C2 (36) shows nature's spacing: 36, 48, 55, 60, 64, 67, ~70, 72, 74, 76. The octave and 5th sit at the bottom and the 3rds and 2nds appear only higher up. Copy that layout.

Register floors **(convention; tune by ear)**:

| Part | MIDI range | Scientific (FL) | Rule |
|---|---|---|---|
| 808 / sub | about 24–40 | C1–E2 (FL C2–E3) | owns everything below about 100 Hz (`music-bass-808`) |
| Bass note of the keys, no 808 | 36–52 | C2–E3 (FL C3–E4) | root, 5th or octave only below 48 |
| Chord upper voices with an 808 present | ≥ 48, prefer 52–76 | C3–E5 (FL C4–E6) | never double the 808's octave; 3rds at 48 or above; 7ths and 9ths at about 55 or above; clusters (2nds) at about 60 or above |
| Pads | 52–79 | E3–G5 | spread voicings; high-pass in the mix |
| Bells, plucks, arps | 60–96 | C4–C7 | outline chord tones; thin is fine |
| Lead melody | above the chord top voice | — | `music-melody-hooks`; keep the chord top voice at least a 3rd below the lead, or in another octave |

Muddy versus clear, with Cmaj7 over C2:
- **Muddy:** MIDI 36 40 43 47. The major 3rd at 36 is below its limit of 46, and the 5th and 7th crowd the bass.
- **Clear:** `Cmaj7 36 | 43 52 59`. It has a 5th at the bottom, the 3rd at E3 and the 7th at B3. The spread `Cmaj9 36 | 48 64 67 71 74` is clear too.

---

## 4. Rules for an expensive sound: extensions, omissions, avoid-notes

1. **Spacing follows the harmonic series:** wide at the bottom, close at the top **(derived)**.
2. **The top voice is a melody.** Choose it on purpose, move it by step, and give it one high point per phrase.
3. **Drop notes in this order when a chord has 5 or more notes:** the 5th first, then the root (the bass has it), then doubled notes. Always keep the guide tones (3rd and 7th) and the named colour tone (9, 11, 13, #11, b9) **(convention)**.
4. **Avoid-notes (convention):**
   - A natural 11 over a major or dominant chord forms a minor 9th above the 3rd, so use #11 instead.
   - Use b9 only on dominant chords.
   - The 11 is fine on minor chords (m11).
5. **Colour by genre:**
   - trap and drill: triads, m(add9), sus;
   - lo-fi, R&B and neo-soul: 7ths, 9ths and 13ths;
   - house: m7, m9 and 7sus4;
   - future bass: maj7, add9 and wide stacks;
   - cinematic: triads, power chords, add9 and maj7#11.
6. **Don't double the 3rd low,** and never double the 808's pitch an octave above it in the 40–55 region.
7. **Density follows the drums:** busy drums want 7th-chord harmony at most; sparse drums can carry 9ths, 11ths and 13ths (`music-theory-core` complexity budget).
8. **Same-shape parallel motion** (planing) is a deliberate effect: deep-house chord memory, power chords, fanfares, the Phrygian bII. Use it on purpose, and voice-lead everything else.

---

## 5. The nearest-voicing algorithm

Inputs:
- chord symbols, each with a bass note (root or slash bass);
- number of upper voices `n`: 3 for triads, 4 for 7th and 9th chords;
- a window `[lo, hi]`: 52–76 for keys by default, 55–79 for pads, with a floor of about 48 when an 808 is present;
- a maximum span of 14 semitones (one hand).

### Manual procedure (follow these steps when writing voicings by hand)

1. **Spell the pitch classes** of each chord from its formula. Mark the **required** tones: the 3rd, the 7th if present, and the named colour tone (9, 11, 13, #11, b9, sus 2 or 4). Mark the **optional** tones: the 5th, and the root when the bass already plays it.
2. **Voice the first chord top-down:**
   - Pick its top note on purpose: a chord tone in 64–72, or the melody's note minus a 3rd or more.
   - Fill downward with the required tones.
   - Keep every adjacent pair, bass included, above its low-interval limit (§3).
   - Centre the shape around MIDI 60–64.
3. **For each next chord, move the previous voicing into the new chord:**
   - a. Keep every **common tone** in the same voice.
   - b. Move every other voice to the **nearest** tone of the new chord, ideally 1–2 semitones.
   - c. If a required tone is missing, the voice whose old note is closest to it takes it.
   - d. If two voices land on the same pitch, or there are more tones than voices, drop the 5th first, then the root.
4. **Score the result**, then also score the next inversion up and the next one down, and keep the cheapest. The score adds:
   - the total semitone motion of the upper voices;
   - 6 points if the bass and the top voice move in the same direction into a perfect 5th or octave, measured as a pitch-class interval (the parallel P5/P8 test);
   - 2 points per semitone of top-voice leap beyond 5 semitones (a perfect 4th).
   Reject outright any voicing that breaks a low-interval limit or leaves the window.
5. **Place the bass separately.** Use the root, or the slash note, at the octave nearest the previous bass inside 36–52. The bass is exempt from the motion score: leaps of a 4th or 5th are its normal motion, and **contrary motion against the top voice** is what makes a progression feel strong. Under an 808, skip this step and hand the roots to `music-bass-808`.
6. **For loops, close the cycle.** Score last chord → first chord. If that wrap costs more than about 7, re-voice chord 1 (try each candidate first voicing and keep the lowest total). Otherwise the loop jumps at every restart.
7. **Read the top-voice line as a melody.** It should be mostly steps, with no repeated awkward leap, and it must not collide with the lead. If it does, shift the whole upper structure by an inversion.
8. **Output** a list of `bass | upper` MIDI numbers per chord, with FL labels on request (FL octave = scientific + 1).

Common-tone shortcuts **(derived)**:
- Roots a 3rd apart share 2 notes (C↔Am, C↔Em, F↔Dm): two voices hold and one moves.
- Roots a 5th apart share 1 note (C↔G, C↔F): one voice holds and two move by step.
- Roots a step apart share none (F↔G, Ab↔Bb): move all the upper voices **against** the bass direction.

Worked example, I–vi–IV–V in C, three voices:
`C 48 | 60 64 67` → `Am 45 | 60 64 69` → `F 41 | 60 65 69` → `G 43 | 59 62 67`
- C→Am: C and E are common tones, so only G→A moves (2).
- Am→F: A and C are common, so only E→F moves (1).
- F→G: no common tones, so all voices move down against the rising bass: C→B, F→D, A→G (1+3+2 = 6).
- G→C (the wrap): B→C, D→E, G holds (1+2+0 = 3).
- The top-voice line is G–A–A–G. No parallel perfect intervals.

Worked example, ii–V–I with rootless voicings:
`Dm9 38 | 53 57 60 64` → `G13 43 | 53 57 59 64` → `Cmaj9 36 | 52 55 59 62`
- Dm9→G13: F, A and E are common tones, and C→B moves (1).
- G13→Cmaj9: F→E, A→G, B holds, E→D (1+2+0+2 = 5).

### Python (paste into a `make_midi.py`)

Tested: it reproduces the F minor example below exactly. For other inputs it may return a different voicing that is just as smooth. Hand-edit the top voice if the melody needs it.

```python
from itertools import combinations

# approx. lowest lower-note per interval (semitones -> MIDI); convention, tune by ear
LIL = {1: 52, 2: 51, 3: 48, 4: 46, 5: 46, 6: 47, 7: 34, 8: 43, 9: 41, 10: 41, 11: 41}

def chord(root_pc, ivs, req, bass):
    """root_pc 0-11, ivs = all allowed intervals, req = required intervals, bass = MIDI."""
    return ({(root_pc + i) % 12 for i in ivs}, {(root_pc + i) % 12 for i in req}, bass)

def voicings(pcs, req, n, bass, lo=52, hi=76, span=14):
    notes = [m for m in range(lo, hi + 1) if m % 12 in pcs]
    for v in combinations(notes, n):
        if v[-1] - v[0] > span or not req <= ({x % 12 for x in v} | {bass % 12}):
            continue
        s = sorted([bass, *v])
        if any(b - a in LIL and a < LIL[b - a] for a, b in zip(s, s[1:])):
            continue
        yield v

def cost(pv, pb, v, b):
    c = sum(abs(x - y) for x, y in zip(pv, v))           # voice motion
    i1, i2 = (pv[-1] - pb) % 12, (v[-1] - b) % 12
    if i1 == i2 and i1 in (0, 7) and (b - pb) * (v[-1] - pv[-1]) > 0:
        c += 6                                             # parallel P5/P8 bass-top
    return c + 2 * max(0, abs(v[-1] - pv[-1]) - 5)         # top leap > P4

def lead(chords, n=4, loop=True, **kw):
    """chords: [chord(...)]; tries every first voicing, greedy after, scores the wrap."""
    cands = [list(voicings(p, r, n, b, **kw)) for p, r, b in chords]
    best = None
    for first in cands[0]:
        path, total = [first], 0
        for i in range(1, len(chords)):
            pb, b = chords[i - 1][2], chords[i][2]
            v = min(cands[i], key=lambda v: cost(path[-1], pb, v, b))
            total += cost(path[-1], pb, v, b); path.append(v)
        if loop:
            total += cost(path[-1], chords[-1][2], first, chords[0][2])
        if best is None or total < best[0]:
            best = (total, path)
    return [(v, c[2]) for v, c in zip(best[1], chords)]

# Fm - Db - Cm, triads, F minor trap:
# lead([chord(5,[0,3,7],[0,3,7],41), chord(1,[0,4,7],[0,4,7],37),
#       chord(0,[0,3,7],[0,3,7],36)], n=3)
# -> [((56,60,65),41), ((56,61,65),37), ((55,60,63),36)]
```

Notes on the code:
- For extended chords, put the colour tone in `req`. Example for m9: `ivs=[0,3,7,10,14]`, `req=[3,10,14]`. Leaving the root out of `req` allows rootless voicings.
- If the result contains a minor-2nd cluster at the bottom (for example 52–53), raise `lo` to 55.
- If the result doubles a note or drops a colour tone you wanted, add that tone to `req`.
- `n` must not exceed the number of distinct pitch classes unless you want doublings.

---

## 6. Guide tones, common tones and the top-voice line

- **Guide tones** are the 3rd and 7th. In a ii–V–I they move by semitone or hold:
  - the 7th of ii (C) drops to the 3rd of V (B);
  - the 3rd of ii (F) holds as the 7th of V;
  - then F drops to E (the 3rd of I), and B holds as the maj7 or rises to C.
- The tritone sub keeps the same guide tones: Db7's F and Cb (= B) are G7's B and F swapped **(sourced: Wikipedia, Tritone substitution)**.
- A held top note over moving chords is cheap and lush, because the same note takes a new role each time. E over Fmaj9 → G6 → Am7 → Cadd9 is the 7th, then the 6th, then the 5th, then the 3rd.
- Contrary motion between the bass and the top voice is the strongest-sounding connection, oblique motion (one voice holds) is next, and similar motion into a perfect interval is the weakest.
- In pads and supersaws, smooth voice leading also stops audible jumps in brightness. With glide or portamento enabled it produces the legato "chord morph" of future bass and synthwave.

## 7. Sources
- Plomp & Levelt (1965), tonal consonance and critical bandwidth: https://www.math.miami.edu/~armstrong/592sp15/Plomp_Levelt_1965.pdf
- Robin Hoffmann, Low Interval Limits: https://www.robin-hoffmann.com/dfsb/low-interval-limits
- Sleepfreaks, voicing and low interval limit: https://sleepfreaks-dtm.com/en/music-theory-beginner/voicing-arpeggio/
- Open Music Theory, core principles of orchestration (close versus open voicing).
- Wikipedia: Voice leading; Cadence; Tritone substitution; Consonance and dissonance.
- Native Instruments, lo-fi chord progressions (loops that avoid I or end on V7).
