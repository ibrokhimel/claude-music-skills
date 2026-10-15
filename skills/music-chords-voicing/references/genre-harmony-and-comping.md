# Genre harmony, harmonic rhythm and comping rhythms on the 16-step grid

This file covers what chords each genre uses, how fast the chords change, and where the chord attacks fall in the bar. It ends with a Python helper that turns a comping grid into MIDI notes. Pitches use C4 = 60 (FL Studio shows "C5"). Steps are numbered 1–16 per 4/4 bar: step 1 = beat 1, 5 = beat 2, 9 = beat 3, 13 = beat 4. Start beat = (step − 1) / 4. Most values here are **(convention)**: practitioner defaults, not measurements. Tune them by ear.

## Contents
1. Genre harmony tendencies
2. Harmonic rhythm by genre
3. Comping grid notation
4. Comping grids per genre
5. Humanising, rolls and velocity
6. Python: grid → MIDI notes
7. Sources

---

## 1. Genre harmony tendencies

Library numbers (#) refer to `progression-library.md`.

| Genre | Key / scale | Chord vocabulary | Signature moves | Voicing and instrument notes |
|---|---|---|---|---|
| Trap | natural or harmonic minor, Phrygian. Keys whose tonic suits the 808 (F, F#, G, A minor) | minor triads, m(add9), sus2, the occasional dim or harmonic-minor V | i–VI–v, i–v–iv (#21), i–VI–III–VII (#18), Andalusian (#19), b2/b6 semitone motifs | 2–4 chord loops over 8 bars. The melody (bells, plucks, dark piano, strings) carries the harmony. Chords stay above about MIDI 48 so the 808 owns the low end **(sourced: eMastered; PML)** |
| UK / NY drill | minor, Phrygian b2 colour, harmonic minor, Hungarian minor | sparse triads, sus, dim; orchestral strings, choir | i–v–VI, i–VII–VI, i–iv–VII–III (#22); descending semitone lines | very sparse; tension over resolution; leave a gap every bar. In NY drill the sliding 808 carries the harmony **(sourced: Orphiq summary)** |
| Boom bap | whatever key the sample is in, often minor or Dorian | sampled jazz and soul chords: m7, 9, 7#9 | 1–2 chord loops, ii–V fragments, blues (#24) | chop 1–2 bar sample loops; dusty 7ths and 9ths; filtered |
| Lo-fi hip hop | major or Dorian | maj7, m7, 9, 11, 13, 6/9 | ii–V–I (#7), I–vi (#13), IV–iii–vi (#12), I–VI7–ii–V (#9), Am7–F–E7 | few chords, no hard cadences, loose timing, rolled chords, Rhodes or e-piano **(sourced: Native Instruments; eMastered; Audeobox)** |
| R&B (modern) | major-7 and minor-9 colours | m9, m11, maj9, 13, slash chords | IVmaj7–iii7–vi9, ii9–V13, "Just the Two of Us" (#10), secondary dominants | the 808 or bass is tuned to the chord roots; anticipations; Rhodes and pads; space for the vocal **(sourced: violetrecording)** |
| Neo-soul / gospel | Dorian, major, melodic minor | m9, m11, maj9, 13, 7#9, quartal, slash chords | tritone subs, backdoor (#15), walk-ups (#16), Dorian vamp (#14) | voice-lead every chord; rootless voicings over a separate bass; chromatic bass walks |
| Plugg / pluggnb | plugg: minor or dreamy major; pluggnb: maj7 and m9 | maj9, m9, add9, close inversions with tensions beside the root | 2–3 chord loops, e.g. `Fmaj9 41 | 55 57 60 64` → `Cmaj9/B 47 | 55 59 62 64` → `Dm9 38 | 53 60 62 64` → `Cmaj9/E 40 | 55 59 62 64` (the example comes from a search snippet, unverified) | electric-piano block chords, sine leads, glassy bells **(sourced: Splice; NI summary)** |
| Pop | major (or Aeolian) | triads, add9, sus, occasional borrowed iv or bVI | I–V–vi–IV family (#1–2), I–vi–IV–V (#3), i–VI–III–VII (#18); key change on the last chorus | big, simple, clear; 1 chord per bar; IV and V are more common than I **(sourced: Hooktheory)** |
| House / deep house | Dorian or Aeolian minor | m7, m9, m11, 7sus4, organ and piano stabs | parallel m9 stabs (#17), Dorian i–IV vamp (#14), 2-chord loops, tonic pedal | chord memory (the same shape transposed); offbeat stabs. Deep house has "advanced chord structures" and avoids big builds **(sourced: Wikipedia; MusicRadar summary)** |
| Tech house / techno | minor, 1–2 chords or none | one- or two-note stabs, minor 7th or sus stabs (Detroit) | drone or pedal | rhythm and timbre lead; harmony is optional **(sourced: Wikipedia, Techno)** |
| Trance / EDM | natural minor; major for big-room and pop EDM | triads, sus2 and sus4, supersaw stacks | i–VI–III–VII (Am–F–C–G), vi–IV–I–V, a sus chord held one bar long, +1/+2 key lift for the last drop | write the breakdown first; offbeat bass; arps **(sourced: Orphiq summary)** |
| Future bass | major-leaning, Lydian | maj7, m7, maj9, add9; triads too thin unless the 2nd note is doubled up an octave | royal road (#11), vi–IV–I–V (#2), I–V–vi–IV | detuned supersaw chords with pitch swells; long sub notes under short rhythmic chords; 4-bar parts **(sourced: FeelYourSound; Violet Recording)** |
| Synthwave | Aeolian | triads, add9, sus | i–VI–III–VII, i–VII–VI–VII (#18), i–bVI–bVII (#25) | 16th arpeggiated poly chords, a pedal bass, 80s brightness over minor |
| Cinematic / epic | Aeolian, harmonic minor, Lydian (wonder), Phrygian (threat) | triads, power chords, sus, add9, maj7#11 | i–bVI–bIII–bVII, chromatic mediants, pedal points, Picardy endings (`color-devices.md`) | slow harmonic rhythm; ostinato over a pedal; orchestral spacing that follows the harmonic series |
| Liquid DnB / UK garage | minor 7/9; R&B harmony | maj7, m9, dominant 9 | ii–V–I, R&B loops | Rhodes, strings, soul vocals; UKG chord stabs get heavy swing (MPC 62–69%) **(sourced: genre notes)** |
| Afrobeats | major or minor, diatonic | simple triad loops | I–IV–V, vi–IV–I–V | guitar and pluck patterns; 3-2 clave feel; the bass follows the roots |
| Amapiano | no fixed key; Dorian or minor | m9, maj7, 6/9, ii–V–I | `Em9 40 | 55 59 62 66` → `Cmaj7 36 | 55 59 60 64` → `Gmaj7 43 | 55 59 62 66` → `D6/9 38 | 54 59 62 64` | long jazzy piano or pad chords; the log drum is the bass hook **(chord example: Roland/genre notes)** |

Scale note: modal colour is only audible when the tonic is established (a pedal or a returning vamp) and the characteristic note actually sounds. Scale tables are in `music-theory-core`.

## 2. Harmonic rhythm by genre (convention; no measured data was found)

| Genre | Typical BPM | Chord changes | Loop length |
|---|---|---|---|
| Trap | 130–160 (half-time feel) | 1 per 1–2 bars (per 2 bars at fast tempos) | 2–4 chords over 4–8 bars |
| Drill | 138–145 | 1 per 1–2 bars; sometimes 2 per bar in fills | 4–8 bars |
| Boom bap | 85–95 | the sample's rate, 1–2 per bar | 1–4 bars |
| Lo-fi | 70–90 | 1 per bar (sometimes 2) | 2–4 bars |
| R&B / neo-soul | 60–100 | 1–2 per bar plus passing chords | 4–8 bars |
| Pop | 90–130 | 1 per bar; doubles in the pre-chorus | 4 bars |
| House / deep house | 118–126 | 1 per 1–2 bars | 2–8 bars |
| Future bass / EDM | 128–160 | 1 per bar in the drop; slower in the breakdown | 4–8 bars |
| Cinematic | free | 1 per 2–8 bars, or a pedal | phrase-based |

Design rules **(convention)**:
1. Change chords on the bar downbeat, where the drums are strongest. R&B and pop anticipations (step 15 or 16) are the exception.
2. Speed up harmonic rhythm going into a section change, e.g. 2 chords per bar in the last pre-chorus bar.
3. Hold one chord or a pedal during builds, so the tension comes from rhythm and filtering.
4. The melody moves faster than the chords. Melody notes on strong beats are usually chord tones (`music-melody-hooks`).
5. Harmonic rhythm that is too fast in a rap beat fights the vocal. In verses, 1 chord per 2 bars is safer.

## 3. Comping grid notation

One row per bar, 16 symbols in 4 groups of 4. A pattern may span several bars (32 steps = 2 bars per chord).
- `X` accented chord attack (velocity 95–115);
- `x` normal attack (75–95);
- `-` hold the previous attack;
- `.` silence;
- `N` the next bar's chord, played early (anticipation) and tied over the barline.

Chord velocities are lower than drum velocities on purpose. Attacks at steps 1, 7, 13 mean start beats 0, 1.5 and 3.

Rules for writing the MIDI:
- Every chord note in a loop must end at or before the last bar's end, or FL Studio adds an empty bar.
- An `N` on the last bar gets clamped, so the loop re-strikes chord 1 on step 1. That is correct.

## 4. Comping grids per genre (convention unless marked)

**Pad / trap / cinematic sustain**: one chord held 1–2 bars, legato into the next (overlap 0–1 steps).
```
Pad   X - - - | - - - - | - - - - | - - - -     (attacks: 1; length 16 or 32 steps)
```

**Trap keys as an arpeggio** (chord tones, 3+3+2 placement, 1–2 step notes). Pitch order: root, 5th, octave, b3 above, then repeat. The 808 marks each chord change.
```
Arp   X . . x | . . x . | X . . x | . . x .     (steps 1,4,7,9,12,15)
```

**Drill** (sparse: a chord or strings on 1, then silence before the bar ends; the motif lives in the melody):
```
Str   X - - - | - - - - | - - . . | . . . .     (attack 1, length 10)
```

**Boom bap sample-chop style** (re-trigger the chord chop off the beat):
```
Chop  X - - - | - - x - | - - - - | . . x -     (1 len 6, 7 len 6, 15 len 2)
```

**Lo-fi** (whole or half notes, rolled, behind the beat):
```
Keys  X - - - | - - - - | - - - - | - - - -     (1 chord per bar)
Keys  X - - - | - - - - | x - - - | - - - -     (2 chords per bar: steps 1 and 9)
```
Settings: roll 10–30 ms, humanise ±10–30 ms with a slight late bias, velocity 60–90, swing 55–60% MPC (optional).

**R&B / neo-soul anticipation** (the next chord arrives on step 15 and ties over the barline):
```
Keys  - - - - | - - - - | - - - - | - - N -     (bar 1 starts struck; then each chord enters on 15)
```
Settings: roll 10–30 ms bottom-to-top; add ghost re-strikes on step 7 or 11 at low velocity for movement.

**Pop pulse and pop push**:
```
8ths  X . x . | x . x . | X . x . | x . x .     (steps 1,3,5,...,15; length 1-2 steps)
Push  X - - - | - - x - | - - - - | x - - -     ("1, 2&, 4": steps 1, 7, 13)
```
In choruses, play the chord change a 16th or an 8th early (step 16 or 15 of the previous bar).

**House offbeat stabs** (short, 1 step long; the classic deep-house organ or piano stab):
```
Stab  . . x . | . . x . | . . x . | . . x .     (steps 3,7,11,15 = the "&"s)
Stab2 x . . x | . . x . | . . x . | . . . .     (8th / dotted-8th mix: steps 1,4,7,11)
```

**Trance / EDM** (offbeat supersaw plucks, or a 16th gate with sidechain):
```
Pluck . . x . | . . x . | . . x . | . . x .
Gate  x x x x | x x x x | x x x x | x x x x     (1-step notes; sidechain pumps it)
```

**Future bass** (rhythmic supersaw chord chops with heavy sidechain; pitch-bend swells into changes):
```
Chop  x . . x | . . x . | x . . x | . . x .     (steps 1,4,7,9,12,15) (sourced grid: genre notes)
```

**Synthwave** (16th arpeggio through the chord tones, e.g. 1-5-8-10 up, or up-down):
```
Arp   x x x x | x x x x | x x x x | x x x x
```

**Afrobeats keys / guitar** (3-2 clave placement, short notes):
```
Clave x . . x | . . x . | . . x . | x . . .     (steps 1,4,7,11,13)
```

**Ballad / cinematic piano**: the left hand arpeggiates root–5th–octave in 8ths (e.g. MIDI 36 43 48), and the right hand plays a close voicing on top. Strings sustain spread voicings that follow the harmonic series.

## 5. Humanising, rolls and velocity

- Converting ms to ticks: `ticks = ms × PPQ × BPM / 60000`. At PPQ 96 and 90 BPM, 20 ms ≈ 2.9 ticks. At 140 BPM, 20 ms ≈ 4.5 ticks.
- Rolls (strums): offset each note upward by 10–30 ms, from the lowest note up. Use them for R&B, lo-fi and gospel; not for EDM stabs.
- Humanise: ±10–30 ms of random timing for lo-fi and R&B, 0 for EDM and house, and ±5 ms at most for pop.
- Velocity:
  - chord pads 70–95;
  - lo-fi 60–90;
  - house stabs 90–110;
  - ghost re-strikes 40–60.
  - Keep the top voice level with the rest or a little louder, because it is the melody.
- Length: pads legato (end exactly at the next attack); stabs 1 step; plucks 1–2 steps. Gate length is a big part of the genre sound.
- Swing: give MPC/Linn values (50% straight, 66% triplet). FL's Channel Rack swing is a different 0–100 knob with no verified mapping: start at about 15–30% FL and match by ear. It only acts if both the global swing and the channel swing are above 0.

## 6. Python: grid → MIDI notes

Returns the `(start_beat, midi, length_beats, velocity)` tuples used by `music-theory-core/references/make_midi_template.py` (`write()` clamps notes to the last bar).

```python
import random

def comp(chords, pattern, bpm, vel=(100, 84), roll_ms=0, human_ms=0, seed=7):
    """chords: one (bass or None, [upper MIDI]) per pattern cycle. pattern: 16*k
    symbols (spaces/| ignored) = one chord's span: X accent, x normal, - hold,
    . rest, N next chord early (tied over). Returns (start_beat, midi, len, vel)."""
    p = [c for c in pattern if c in 'Xx-.N']
    L = len(p)
    assert L % 16 == 0, 'pattern needs 16 steps per bar'
    lead_hold = next((i for i, c in enumerate(p) if c != '-'), L)
    rnd, ms = random.Random(seed), bpm / 60000.0          # beats per ms
    out = []
    for idx in range(len(chords)):
        for step, sym in enumerate(p):
            first_tie = idx == 0 and step == 0 and sym == '-'
            if sym not in 'XxN' and not first_tie:
                continue
            bass, upper = chords[(idx + 1) % len(chords)] if sym == 'N' else chords[idx]
            n = 1
            while step + n < L and p[step + n] == '-':
                n += 1
            if sym == 'N':
                n += lead_hold                              # tie into next chord
            if first_tie:
                n = lead_hold
            v = vel[0] if sym in 'XN' or first_tie else vel[1]
            t0 = (idx * L + step) * 0.25
            notes = ([bass] if bass is not None else []) + sorted(upper)
            for k, m in enumerate(notes):
                jitter = rnd.uniform(-human_ms, human_ms) * ms if human_ms else 0
                start = max(0.0, t0 + k * roll_ms * ms + jitter)
                out.append((round(start, 4), m, round(n * 0.25 - (start - t0), 4), v))
    return out

# Lo-fi I-vi, R&B anticipation, 80 BPM, 20 ms roll (tested):
# comp([(48, [52, 55, 59, 62]), (45, [52, 55, 59, 60])], '---- ---- ---- --N-', 80, roll_ms=20)
# -> Cmaj9 at beat 0 for 3.5 beats; Am9 at 3.5 for 4 beats; Cmaj9 at 7.5 (write() clamps at 8)
# Trap pads, 2 bars per chord, no bass (808 owns roots):
# comp([(None, [56, 60, 65]), (None, [56, 61, 65])], 'X--- ---- ---- ---- ---- ---- ---- ----', 140)
# House stabs: comp([(None, [56, 60, 65])], '..x. ..x. ..x. ..x.', 124)
```

Under an 808, pass `None` as the bass and write the 808 roots as a separate .mid (`music-bass-808`). For 2 bars per chord, give a 32-step pattern. For mixed harmonic rhythm (e.g. 2 chords in the last bar), call `comp` per section and shift the start beats.

## 7. Sources
- Native Instruments, lo-fi chord progressions: https://blog.native-instruments.com/lo-fi-chord-progressions/
- eMastered, trap and lofi progressions: https://emastered.com/blog/trap-chord-progressions
- Production Music Live, trap melody scales: https://productionmusiclive.com/blogs/news/trap-beat-guide-melodies-3-essential-scales-for-making-melodies
- Orphiq, drill chords; trance (via search summaries): https://orphiq.com/resources/drill-chords
- violetrecording, R&B beats and future bass: https://violetrecording.com/how-to-make-future-bass/
- FeelYourSound, future bass chords; Splice, What is pluggnb; Roland, amapiano; MusicRadar, deep house minor 9ths (via search summaries).
- Wikipedia: Harmonic rhythm; Deep house; Techno; Neo soul.
- Hooktheory, 1,300-song analysis (IV and V more common than I).
