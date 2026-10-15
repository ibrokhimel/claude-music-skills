# Worked melody examples (drop-in note lists)

Nine original, fully checked melodies plus a parser and a melody checker, written as `start_beat : MIDI : length_beats : velocity` (C4 = 60; FL labels one octave higher, so MIDI 69 shows as "A5" in FL). Beat 0 = bar 1 beat 1. Every list was run through `check_melody()` below: every pitch fits the stated key, chord tones sit on beats 1 and 3 except for the labelled NCTs, and no note ends past the loop.

## Contents
1. Using these lists with `make_midi_template.py`
2. `check_melody()`: the automatic quality gate
3. Ex 1: trap bells, A harmonic minor, 4 bars
4. Ex 2: pop chorus topline, C major, 8-bar period
5. Ex 3: counter-melody under Ex 2
6. Ex 4: lo-fi Dorian keys line, D Dorian, 4 bars
7. Ex 5: R&B phrase with a pentatonic run, Eb major, 4 bars
8. Ex 6: EDM drop lead, A minor (vi–IV–I–V), 4 bars
9. Ex 7: afrobeats lead, G major pentatonic, 4 bars
10. Ex 8: drill motif, C minor, 8 bars (fits `ny-drill-midi`)
11. Ex 9: cinematic theme, D minor, 8 bars (+ augmentation)

---

## 1. Using these lists with the MIDI template

`music-theory-core/references/make_midi_template.py` takes notes as `(start_beat, midi, length_beats, velocity)`, which is the same order used here. Paste a block as a string and parse it:

```python
def parse(block, shift_beats=0.0, transpose=0):
    """'start : midi : len : vel  # comment' lines -> template tuples."""
    out = []
    for line in block.strip().splitlines():
        line = line.split("#")[0].strip()
        if not line:
            continue
        b, m, l, v = (x.strip() for x in line.split(":"))
        out.append((float(b) + shift_beats, int(m) + transpose, float(l), int(v)))
    return out

# in build_parts():  parts["bells"] = parse(BELLS)
#                    parts["bells_oct"] = [(s, m - 12, l, v - 15) for s, m, l, v in parse(BELLS)]
```

- Set `BPM` and `BARS` to the example's values; the template clamps note ends to the last bar.
- Triplet starts are written as 3-decimal beats (13.167 = 13 + 1/6). `round(beat * 96)` gives the exact tick (1264), so no drift.
- 8th-note swing (lo-fi, R&B): delay every note that starts on an off-beat 8th (x.5) by `(mpc - 50) / 100` beats. At 58% that is +0.08 beat (about 8 ticks). The template's `swing16()` only handles 16ths.

```python
def swing8(notes, mpc_percent):
    d = (mpc_percent - 50) / 100            # 1 beat = one 8th pair
    return [(s + d, m, l, v) if abs((s % 1) - 0.5) < 1e-6 else (s, m, l, v)
            for s, m, l, v in notes]
```

## 2. `check_melody()`: the automatic quality gate

Run this on every melody before writing MIDI. The targets are conventions (see `melodic-grammar.md`), so treat a miss as a prompt to look again, not a hard failure.

```python
def check_melody(notes, chords, scale_pcs, loop_beats):
    """notes: [(start, midi, len, vel)]; chords: [(start, end, {pitch classes})]."""
    notes = sorted(notes)
    p = [m for _, m, _, _ in notes]
    iv = [b - a for a, b in zip(p, p[1:])]
    n = max(1, len(iv))
    hi = max(p)
    def sounding(t):
        return [m for s, m, l, _ in notes if s <= t < s + l]
    def chord_at(t):
        return next((pcs for a, b, pcs in chords if a <= t < b), set())
    strong = [(t, m) for t in range(0, int(loop_beats), 2) for m in sounding(t)]
    return {
        "steps<=2": round(sum(abs(i) <= 2 for i in iv) / n, 2),      # target 0.65-0.80
        "thirds": round(sum(3 <= abs(i) <= 4 for i in iv) / n, 2),   # target 0.15-0.25
        "leaps>=5": round(sum(abs(i) >= 5 for i in iv) / n, 2),      # target <= 0.10
        "range": max(p) - min(p),
        "climax_once": p.count(hi) == 1,
        "climax_pos": round(next(s for s, m, _, _ in notes if m == hi) / loop_beats, 2),  # 0.55-0.75
        "strong_beat_chord_tones": round(sum(m % 12 in chord_at(t) for t, m in strong)
                                         / max(1, len(strong)), 2),   # target 0.75-0.85+
        "out_of_scale": [(s, m) for s, m, _, _ in notes if m % 12 not in scale_pcs],
        "past_loop_end": [(s, m) for s, m, l, _ in notes if s + l > loop_beats + 1e-6],
        "gap_fill_misses": [i for i in range(len(iv) - 1)
                            if abs(iv[i]) >= 5 and iv[i] * iv[i + 1] > 0],
    }
```

Pentatonic lines (Ex 5 run, Ex 7) have 3-semitone gaps that are scale steps. Count their steps in scale degrees, or accept 55–65% semitone steps **(derived)**.

---

## 3. Ex 1: trap bells, A minor with harmonic-minor V, 140 BPM, 4 bars

Chords, one per bar: Am (A C E) | F (F A C) | Dm (D F A) | E (E G# B). The melody uses A natural minor and uses G# only over the E chord, which is how trap "harmonic minor" loops usually work. Bells or a pluck. The 2-bar call is the motif, then its exact inversion. The 2-bar response climbs to one climax and ends on the leading tone, which resolves to A when the loop restarts.

```
# bar 1 - Am: the motif (arpeggio up, step back)
0.0   : 69 : 0.75 : 100   # A4  root
0.75  : 72 : 0.75 : 85    # C5  3rd (tresillo position)
1.5   : 76 : 1.0  : 95    # E5  5th, held across beat 3 = syncopation
2.5   : 74 : 0.5  : 78    # D5  passing tone
3.0   : 72 : 0.5  : 88    # C5  3rd; rest 3.5-4.0
# bar 2 - F: chromatic inversion of bar 1 (intervals +3 +4 -2 -2 -> -3 -4 +2 +2)
4.0   : 72 : 0.75 : 98    # C5  5th
4.75  : 69 : 0.75 : 85    # A4  3rd
5.5   : 65 : 1.0  : 92    # F4  root
6.5   : 67 : 0.5  : 78    # G4  passing tone
7.0   : 69 : 0.5  : 88    # A4  3rd; rest
# bar 3 - Dm: straight-8th climb to the climax
8.0   : 69 : 0.5  : 92    # A4  5th
8.5   : 71 : 0.5  : 78    # B4  passing
9.0   : 72 : 0.5  : 85    # C5  passing (m7 colour)
9.5   : 74 : 0.5  : 90    # D5  root
10.0  : 77 : 1.5  : 115   # F5  CLIMAX: 3rd of Dm = b6 of the key, beat 3, 62.5% of loop
11.5  : 76 : 0.5  : 85    # E5  anticipation: root of the coming E chord
# bar 4 - E: b6 -> 5 sigh, then the leading tone
12.0  : 71 : 0.75 : 95    # B4  5th
12.75 : 72 : 0.75 : 82    # C5  b6 upper neighbour (sorrowful)
13.5  : 71 : 0.5  : 85    # B4  5th
14.0  : 68 : 1.75 : 100   # G#4 3rd = leading tone; ends 15.75
```

Check: range 65–77 (12 semitones); 63% steps (65% counting the loop seam), 32% thirds (arpeggio motifs run thirds-heavy), one leap (−5 into bar 4). Every strong beat is a chord tone. Layers: a −12 copy at velocity −15 (its lowest note, F3 53, stays above the 808 zone), or a +12 copy for shimmer. Phrygian-tinged variant: change the passing B4 at 8.5 to Bb4 70 (the b2 of A, and b6 over Dm). Keep the B naturals in bar 4, because they belong to the E chord.

## 4. Ex 2: pop chorus topline, C major, 100 BPM, 8-bar period

Chords: C | G | Am | G || C | G | F G | C (bar 7 = F on beats 1–2, G on beats 3–4). Cell A ("da-da-DAA": two 8ths and a quarter) is stated, sequenced down a step, then sequenced with its interval expanded. The antecedent ends on 2 over V (question). The consequent ends on 1 over I (answer). The climax is an appoggiatura (Sloboda's tear device).

```
# antecedent
0.0  : 64 : 0.5 : 92    # bar 1 C: E4 3rd
0.5  : 64 : 0.5 : 80    #          E4 repeated note
1.0  : 67 : 1.0 : 100   #          G4 5th; rest 2.0-2.5
2.5  : 65 : 0.5 : 82    #          F4 passing (G-F-E)
3.0  : 64 : 1.0 : 90    #          E4 3rd
4.0  : 62 : 0.5 : 90    # bar 2 G: D4 5th (cell A one step down)
4.5  : 62 : 0.5 : 78
5.0  : 65 : 1.0 : 96    #          F4 7th of G7 (weak beat)
6.5  : 64 : 0.5 : 80    #          E4 neighbour
7.0  : 62 : 1.0 : 88    #          D4 5th
8.0  : 64 : 0.5 : 92    # bar 3 Am: E4 5th
8.5  : 64 : 0.5 : 80
9.0  : 69 : 1.0 : 104   #          A4 root: the cell's 3rd widened to a 4th (interval expansion)
10.5 : 67 : 0.5 : 84    #          G4 passing (gap-fill down)
11.0 : 64 : 1.0 : 90    #          E4 5th
12.0 : 62 : 0.5 : 90    # bar 4 G: D4 5th
12.5 : 64 : 0.5 : 78    #          E4 neighbour
13.0 : 62 : 2.5 : 88    #          D4 = degree 2 over V: half cadence; ends 15.5
# consequent
16.0 : 64 : 0.5 : 95    # bar 5 C: cell A again (identity)
16.5 : 64 : 0.5 : 82
17.0 : 67 : 1.0 : 102   #          G4; rest 18.0-18.5
18.5 : 69 : 0.5 : 86    #          A4 neighbour
19.0 : 67 : 0.5 : 88    #          G4 5th
19.5 : 71 : 0.5 : 96    #          B4 anticipation (3rd of G) = the push
20.0 : 76 : 1.5 : 118   # bar 6 G: E5 CLIMAX, accented appoggiatura (6th over G), leapt to (+5), 62.5%
21.5 : 74 : 1.0 : 100   #          D5 resolves down by step to the 5th
22.5 : 72 : 0.5 : 86    #          C5 passing
23.0 : 71 : 1.0 : 92    #          B4 3rd
24.0 : 69 : 1.0 : 96    # bar 7 F: A4 3rd
25.0 : 67 : 0.5 : 82    #          G4 9th (weak)
25.5 : 69 : 0.5 : 84    #          A4
26.0 : 71 : 1.0 : 94    #       G: B4 3rd
27.0 : 74 : 1.0 : 90    #          D5 5th
28.0 : 72 : 3.5 : 100   # bar 8 C: C5 root = authentic cadence; ends 31.5
```

Check: range D4–E5 (62–76, 14 semitones, female-pop window; transpose −5 to G major for a male voice); 76% steps, 18% thirds, 6% leaps; climax once, at 62.5%; strong beats are chord tones except the intentional appoggiatura on beat 20. Lyric rule: put the title on bar 6 beat 1 (the climax) or on the long C5.

## 5. Ex 3: counter-melody under Ex 2

Strings or a pad-lead in the D3–C4 band (50–60). It sits a register below the topline and at least 3 semitones under it, with about 40% of its density. It moves in the topline's rests (beats 2, 6, 10, 18), holds still (oblique motion) under the topline's long notes, and goes contrary at the climax: down while the topline leaps up. On every strong beat where both parts sound, the interval is a 3rd, 5th or 6th (or a compound of one) and never an octave. The one exception is beat 20, where the topline's appoggiatura makes a deliberate compound 9th.

```
0.0  : 55 : 2.0 : 72    # bar 1 C:  G3 5th, a major 6th under E4
2.0  : 52 : 2.0 : 68    #           E3 3rd, moves in the topline's rest
4.0  : 55 : 2.0 : 70    # bar 2 G:  G3 root, a 5th under D4
6.0  : 53 : 2.0 : 68    #           F3 7th, in the rest; a 6th under D4 at 7.0
8.0  : 57 : 2.0 : 70    # bar 3 Am: A3 root
10.0 : 60 : 2.0 : 68    #           C4 3rd, in the rest; a 3rd under E4 at 11.0
12.0 : 59 : 2.0 : 70    # bar 4 G:  B3 3rd, 3 semitones under D4 (the minimum)
14.0 : 55 : 4.0 : 66    #           G3: root of G, then 5th of C (common tone, oblique)
18.0 : 52 : 2.0 : 68    # bar 5 C:  E3 3rd, in the rest
20.0 : 50 : 2.0 : 74    # bar 6 G:  D3 falls as the topline leaps to E5 (contrary)
22.0 : 53 : 4.0 : 70    #           F3: 7th of G, held as the root of F in bar 7 (pivot)
26.0 : 50 : 2.0 : 70    # bar 7 G:  D3 5th, a compound 6th under B4
28.0 : 52 : 3.5 : 72    # bar 8 C:  E3 3rd, rises while the topline falls D5->C5
```

Check: every note is a root, 3rd, 5th or 7th of its chord. There are no parallel perfect 5ths or octaves with the topline on consecutive strong beats. The two parts never come closer than 3 semitones, and the density is 13 notes against the topline's 34. The lowest note is D3 50, so with an 808 present, high-pass this part around 150–200 Hz or keep it soft.

## 6. Ex 4: lo-fi Dorian keys line, D Dorian, 80 BPM, 4 bars

Chords: Dm9 (D F A C E) | G13 (G B D F A E) | Dm9 | G13, the Dorian i–IV vamp. The line targets 9ths and 7ths, uses B natural (the Dorian colour) over G, and ends unresolved on the 9th of G. Apply `swing8(notes, 58)` and humanize ±10 ms.

```
0.0  : 76 : 1.0 : 78    # bar 1 Dm9: E5 9th on the downbeat (airy)
1.0  : 74 : 0.5 : 64    #            D5
1.5  : 72 : 0.5 : 70    #            C5 7th
2.0  : 69 : 1.5 : 74    #            A4 5th; rest 3.5-4.0
4.0  : 71 : 0.5 : 72    # bar 2 G13: B4 3rd = Dorian major 6th
4.5  : 72 : 0.5 : 62    #            C5 passing
5.0  : 74 : 1.5 : 76    #            D5 5th
6.5  : 76 : 1.0 : 70    #            E5 13th, off-beat held across beat 4; rest 7.5-8.0
8.0  : 76 : 0.5 : 74    # bar 3 Dm9: E5 (motif head returns)
8.5  : 74 : 0.5 : 62
9.0  : 72 : 0.5 : 70    #            C5 7th
9.5  : 74 : 0.5 : 66    #            D5 neighbour return
10.0 : 77 : 1.5 : 84    #            F5 CLIMAX, 3rd of Dm, beat 3, 62.5%
11.5 : 76 : 0.5 : 68    #            E5 9th
12.0 : 74 : 0.5 : 72    # bar 4 G13: D5 5th
12.5 : 71 : 0.5 : 64    #            B4 3rd
13.0 : 69 : 2.5 : 70    #            A4 9th, unresolved ending; ends 15.5
```

Check: range 69–77 (8); 81% steps, no leaps; velocities 62–84 (soft keys). It also works an octave lower (57–65) on a Rhodes.

## 7. Ex 5: R&B phrase with a pentatonic run, Eb major, 72 BPM, 4 bars

Chords: Abmaj7 (Ab C Eb G) | Bb7 (Bb D F Ab) | Gm7 (G Bb D F) | Cm9 (C Eb G Bb D), IV–V–iii–vi. The phrase body is syllabic, the climax lands on the 7th of Gm7, and bar 4 ends in a descending Eb-major-pentatonic run (Eb F G Bb C) of 16th-note triplets with a turn, landing on a chord tone.

```
0.5    : 63 : 0.5   : 72   # bar 1 Abmaj7: Eb4 5th (starts after the downbeat)
1.0    : 65 : 0.5   : 70   #               F4 passing
1.5    : 67 : 1.5   : 88   #               G4 maj7, held across beat 3
3.0    : 70 : 0.5   : 76   #               Bb4 9th
3.5    : 72 : 0.5   : 84   #               C5 3rd
4.0    : 70 : 1.0   : 86   # bar 2 Bb7:    Bb4 root
5.0    : 68 : 0.5   : 74   #               Ab4 7th
5.5    : 65 : 1.0   : 80   #               F4 5th
6.5    : 67 : 0.5   : 70   #               G4 13th (weak)
7.0    : 68 : 0.5   : 74   #               Ab4 7th
7.5    : 70 : 1.5   : 88   #               Bb4 push: 3rd of Gm7 an 8th early, tied over the bar
9.0    : 72 : 0.5   : 78   # bar 3 Gm7:    C5 passing
9.5    : 74 : 0.5   : 84   #               D5 5th
10.0   : 77 : 1.5   : 100  #               F5 CLIMAX = 7th of Gm7 (R&B colour target), 62.5%
11.5   : 74 : 0.5   : 82   #               D5 5th
12.0   : 75 : 1.0   : 90   # bar 4 Cm9:    Eb5 3rd
13.0   : 72 : 0.167 : 80   #               run: C5
13.167 : 70 : 0.167 : 74   #                    Bb4
13.333 : 67 : 0.167 : 78   #                    G4
13.5   : 65 : 0.167 : 72   #                    F4
13.667 : 63 : 0.167 : 76   #                    Eb4
13.833 : 65 : 0.167 : 70   #                    F4 (turn)
14.0   : 67 : 1.75  : 86   #               G4 5th, landing; ends 15.75
```

Check: range 63–77 (14); 73% steps, no leaps; strong beats are all chord tones. Run tick starts: 1248, 1264, 1280, 1296, 1312, 1328. Swing the body with `swing8(..., 56)` but keep the run straight.

## 8. Ex 6: EDM drop lead, A minor, 128 BPM, 4 bars

Chords: Am | F | C | G (vi–IV–I–V in C). Supersaw or pluck lead. The hook identity is the repeated-note head on beats 1 and 1-a, followed by a step down. The pitches adapt to each chord. Bar 3 holds the one surprise (a +5 leap to G5), and bar 4 is the A′ tail that steps up into the loop restart.

```
0.0   : 76 : 0.5  : 110   # bar 1 Am: E5 5th
0.75  : 76 : 0.5  : 95    #           E5 repeat (16th-syncopated)
1.5   : 74 : 0.5  : 100   #           D5 passing
2.0   : 72 : 0.75 : 105   #           C5 3rd
2.75  : 69 : 0.5  : 95    #           A4 root
3.5   : 72 : 0.5  : 100   #           C5
4.0   : 77 : 0.5  : 110   # bar 2 F:  F5 root (head moves up to fit F)
4.75  : 77 : 0.5  : 95
5.5   : 76 : 0.5  : 100   #           E5 maj7 (weak)
6.0   : 72 : 0.75 : 105   #           C5 5th
6.75  : 69 : 0.5  : 95    #           A4 3rd
7.5   : 72 : 0.5  : 100   #           C5
8.0   : 76 : 0.5  : 110   # bar 3 C:  E5 3rd
8.75  : 76 : 0.5  : 95
9.5   : 74 : 0.5  : 100   #           D5 passing
10.0  : 79 : 0.75 : 120   #           G5 CLIMAX: the one leap (+5), 5th of C, 62.5%
10.75 : 77 : 0.5  : 100   #           F5 passing (gap-fill down)
11.5  : 76 : 0.5  : 100   #           E5 3rd
12.0  : 74 : 0.5  : 110   # bar 4 G:  D5 5th
12.75 : 74 : 0.5  : 95
13.5  : 72 : 0.5  : 100   #           C5 passing
14.0  : 71 : 1.0  : 105   #           B4 3rd, longer (the A' change)
15.0  : 72 : 0.5  : 95    #           C5
15.5  : 74 : 0.5  : 100   #           D5 steps up into the loop's E5
```

Check: range 69–79 (10); 65% steps, 26% thirds, 9% leaps; 6 onsets per bar. Stack +12 at velocity −15 for the drop and keep the build version as half-time augmentation (starts and lengths ×2 over 8 bars).

## 9. Ex 7: afrobeats lead, G major pentatonic, 108 BPM, 4 bars

Chords: G | C | Em | D. Pluck, marimba or guitar lead. A 1-bar call built on 3-3-2 tresillo onsets (0, 0.75, 1.5 per half bar) ends on 5. A 1-bar descending pentatonic response ends on 1. The call returns with the climax, then a pickup leads into the loop. Pitches are only G A B D E.

```
0.0   : 71 : 0.5 : 92    # bar 1 G:  B4 3rd     (tresillo 0)
0.75  : 71 : 0.5 : 80    #           B4         (tresillo 0.75)
1.5   : 74 : 0.5 : 95    #           D5 5th     (tresillo 1.5)
2.0   : 74 : 0.5 : 85    #           D5 5th     (second half: 2.0, 2.75, 3.5)
2.75  : 76 : 0.5 : 82    #           E5 6th (weak)
3.5   : 74 : 0.5 : 90    #           D5 = call ends on 5 (unresolved)
4.0   : 76 : 0.5 : 92    # bar 2 C:  E5 3rd     response: pentatonic descent
4.5   : 74 : 0.5 : 80    #           D5 9th
5.0   : 71 : 0.5 : 84    #           B4 maj7 (weak)
5.5   : 69 : 0.5 : 82    #           A4 6th (weak)
6.0   : 67 : 1.5 : 95    #           G4 5th = degree 1: response resolves; rest 7.5-8.0
8.0   : 71 : 0.5 : 92    # bar 3 Em: B4 5th     call returns
8.75  : 71 : 0.5 : 80
9.5   : 74 : 0.5 : 95    #           D5 7th (weak)
10.0  : 79 : 1.0 : 112   #           G5 CLIMAX, 3rd of Em, leap +5, 62.5%
11.0  : 76 : 0.5 : 88    #           E5 root (gap-fill down)
11.5  : 74 : 0.5 : 85    #           D5
12.0  : 74 : 0.5 : 92    # bar 4 D:  D5 root
12.5  : 71 : 0.5 : 80    #           B4 6th (weak)
13.0  : 69 : 2.0 : 90    #           A4 5th; ends 15.0
15.5  : 71 : 0.5 : 85    #           B4 pickup into the loop restart
```

Check: range 67–79 (12); 65% semitone steps (85% in pentatonic scale steps); one leap. Everything sits above C4, leaving the log drum or bass free below. Humanize: velocity ±10, timing ±5–10 ms.

## 10. Ex 8: drill motif, C minor, 142 BPM, 8 bars

Chords, 2 bars each: Cm (C Eb G) | Ab (Ab C Eb) | Fm (F Ab C) | G7 (G B D F). This matches `Documents/flstudio/ny-drill-midi`. A cold 4-note motif in quarter-note triplets (onsets every 2/3 beat = 64 ticks) plays in the first bar of each pair. The second bar is left empty for the vocal. Statement 2 is an exact diatonic sequence down 2 steps. Statement 3 breaks the pattern (rule of three) and leaps to the climax.

```
0.0    : 79 : 0.5 : 100   # bars 1-2 Cm: G5 5th
0.667  : 80 : 0.5 : 85    #              Ab5 b6 neighbour (dark)
1.333  : 79 : 0.5 : 90    #              G5
2.0    : 75 : 1.5 : 100   #              Eb5 3rd; bar 2 empty
8.0    : 75 : 0.5 : 100   # bars 3-4 Ab: Eb5 5th   (sequence: every note 2 scale steps lower)
8.667  : 77 : 0.5 : 85    #              F5 neighbour
9.333  : 75 : 0.5 : 90    #              Eb5
10.0   : 72 : 1.5 : 98    #              C5 3rd
16.0   : 72 : 0.5 : 100   # bars 5-6 Fm: C5 5th    (third statement breaks the pattern)
16.667 : 75 : 0.5 : 88    #              Eb5 7th (weak)
17.333 : 77 : 0.5 : 95    #              F5 root
18.0   : 84 : 1.0 : 118   #              C6 CLIMAX, 5th of Fm, +7 leap, 56%
19.0   : 82 : 0.5 : 90    #              Bb5 passing (gap-fill)
19.5   : 80 : 0.5 : 88    #              Ab5 3rd
24.0   : 79 : 0.5 : 100   # bars 7-8 G7: G5 root
24.667 : 80 : 0.5 : 88    #              Ab5 = b9 over V (menace)
25.333 : 79 : 0.5 : 90    #              G5
26.0   : 77 : 1.0 : 96    #              F5 7th of G7
27.0   : 74 : 1.0 : 92    #              D5 5th: unresolved, so the loop pulls back to Cm
```

Check: range 72–84 (12); 72% steps; one leap; ends at beat 28 of 32. With the project's existing strings motif (bars 1, 3, 5, 7), mute one of them, or shift this list by +4 beats (`parse(..., shift_beats=4)`) so it answers in the empty bars. In that case the last notes end at beat 32, which the template still allows.

## 11. Ex 9: cinematic theme, D minor, 72 BPM, 8 bars

Chords: Dm | Bb | Gm | A7 || Dm | Bb | Gm A7 | Dm (bar 7 = Gm on beats 1–2, A7 on beats 3–4). Strings, horn or piano. The theme opens with a 5th leap filled by step (gap-fill). The antecedent ends on 2 over V. The consequent climbs to one climax on the VI chord, then cadences with a 9–8 suspension. Pitches use D natural minor; C# lives only in the A7 chord.

```
0.0  : 62 : 1.0 : 80    # bar 1 Dm: D4 root
1.0  : 69 : 2.0 : 92    #           A4 5th: opening leap +7, held across beat 3
3.0  : 67 : 1.0 : 78    #           G4 passing (gap-fill begins)
4.0  : 65 : 1.5 : 84    # bar 2 Bb: F4 5th
5.5  : 64 : 0.5 : 70    #           E4 lower neighbour
6.0  : 65 : 2.0 : 82    #           F4 5th
8.0  : 67 : 1.0 : 84    # bar 3 Gm: G4 root
9.0  : 70 : 2.0 : 92    #           Bb4 3rd
11.0 : 69 : 1.0 : 78    #           A4 9th (weak)
12.0 : 69 : 1.0 : 86    # bar 4 A7: A4 root
13.0 : 67 : 1.0 : 78    #           G4 7th
14.0 : 64 : 2.0 : 84    #           E4 5th = degree 2: half cadence
16.0 : 62 : 1.0 : 82    # bar 5 Dm: D4      consequent restates the opening
17.0 : 69 : 2.0 : 94    #           A4
19.0 : 72 : 1.0 : 88    #           C5 7th (weak): tail change, rising instead of falling
20.0 : 74 : 1.5 : 112   # bar 6 Bb: D5 CLIMAX, 3rd of VI, 62.5%
21.5 : 72 : 0.5 : 90    #           C5 9th passing
22.0 : 70 : 2.0 : 96    #           Bb4 root
24.0 : 70 : 1.0 : 88    # bar 7 Gm: Bb4 3rd
25.0 : 69 : 1.0 : 80    #           A4 9th
26.0 : 67 : 1.0 : 84    #       A7: G4 7th
27.0 : 64 : 1.5 : 86    #           E4 5th, tied over the bar line: 9-8 suspension over Dm
28.5 : 62 : 3.0 : 90    # bar 8 Dm: D4 resolution; ends 31.5
```

Check: range 62–74 (12); 73% steps, 18% thirds, 9% leaps (the two motif leaps). There is one deliberate gap-fill exception: bar 5 keeps rising (D4–A4–C5–D5) to reach the climax. The only non-chord tone on a strong beat is the beat-28 suspension. For the Act-3 restatement, **augment**: multiply every start and length ×2 (16 bars, 64 beats), set `BARS = 16`, double at −12 on low brass or cellos, and reharmonize bar 6 as Gm/Bb for a darker climax.
