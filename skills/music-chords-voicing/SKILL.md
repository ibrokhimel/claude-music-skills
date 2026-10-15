---
name: music-chords-voicing
description: Chooses and voices chord progressions that sound expensive rather than muddy, and delivers them to FL Studio as MIDI files. Use whenever the user wants chords, a chord progression, a chord loop, keys, pads, piano chords, Rhodes, stabs or harmony for a beat or song; asks what chords fit a mood (sad, dark, hopeful, epic, nostalgic, romantic, menacing); wants chords to sound lush, jazzy, neo-soul, "expensive" or less muddy; or asks about voicings, inversions, voice leading, 7th/9th/13th chords, rootless or drop-2 voicings, borrowed chords, secondary dominants, tritone subs, key changes, cadences, harmonic rhythm or comping. Also use for the chord part of any trap, drill, boom bap, lo-fi, R&B, pop, house, EDM, future bass, synthwave or cinematic track. Includes a 25-progression library with MIDI voicings, an emotion-to-progression cheat sheet, register floors under 808s, and a nearest-voicing algorithm.
---

# Music chords and voicing

This skill picks chord progressions and turns them into MIDI voicings that sound clear and "expensive": spaced like the harmonic series, connected by smooth voice leading, kept out of the 808's way, and changing at the genre's harmonic rhythm with the genre's comping pattern. It owns:
- the progression library;
- function and cadences;
- voicing types and the low-interval limits;
- the nearest-voicing algorithm;
- chromatic colour devices and the surprise budget;
- harmonic rhythm and comping by genre.

Scale, chord-formula and diatonic tables live in `music-theory-core` (`references/theory-tables.md` §6, §7 and §10). Use them; don't re-derive them. Pitches use C4 = 60, and FL Studio labels MIDI 60 as "C5", so write registers as "MIDI 48 (C3, FL: C4)".

## Core principles (and why)

1. **Voicing matters more than the chord name.** The same Cmaj7 is mud at MIDI 36 40 43 47 and lush as `36 | 43 52 59`. Low partials crowd one critical band (Plomp & Levelt 1965), so wide intervals go low and close intervals go high, the way the harmonic series is laid out.
2. **Keep chords off the sub.** When an 808 or bass owns the low end, chord upper voices stay at or above about MIDI 48 (prefer 52–76), and nothing below 48 except root, 5th or octave. Two parts in the sub register mask each other and smear the mix **(convention)**.
3. **Connect chords by the smallest moves.** Hold common tones and move the other voices 1–2 semitones. Smooth lines let the ear hear continuous voices instead of jumping blocks, which is the polish people call "expensive".
4. **The top voice is a melody, and the bass names the chord.** Choose the top note on purpose. Remember that the same upper shape becomes a different chord over a different bass (C E G B over A = Am9).
5. **Function drives tension.** Tonic means rest (I, vi, iii), predominant means departure (IV, ii), and dominant means pull (V, vii°). V7→I resolves because its tritone collapses inward by semitones.
6. **Loops shouldn't end.** Trap, drill, lo-fi and house avoid a full V7→I inside the loop: they leave out I or finish on V or IV so the loop keeps cycling. Save the authentic cadence for endings and pre-chorus → chorus lifts.
7. **One surprise per predictable context.** Pleasure peaks for a surprising chord in a predictable context (Cheung et al. 2019, about 80k Billboard chords). After 4–8 bars, spend one borrowed or chromatic chord. Never stack surprises.
8. **Genre is mostly harmonic rhythm, colour and comping,** more than progression choice. The same i–VI–III–VII is a trap loop, a trance breakdown or a synthwave arp depending on those three.

## Procedure: writing the chord part

1. **Read the brief.** Note the genre, mood, BPM, key (if given), whether an 808 or bass owns the sub, and the section (verse, hook, drop). Use the genre card in `music-theory-core` if one exists.
2. **Pick the key and mode.**
   - In 808 genres, choose a key whose tonic lands on a good 808 note: F, F#, G or A minor put the 808 root around MIDI 29–33 **(convention)**.
   - Modal colour comes from one characteristic note: Dorian is minor with a major 6th, Phrygian adds a b2, Lydian adds a #4, Mixolydian adds a b7. That note must actually sound in a chord or the melody.
3. **Pick the progression** from the emotion cheat sheet below, which points into `references/progression-library.md`. Respect the genre vocabulary (genre table below). Keep it to 2–4 chords for loop genres.
4. **Set the harmonic rhythm:** how many bars per chord, and the loop length (genre table). The default is a chord change on the bar downbeat.
5. **Choose the chord colour per genre:**
   - trap and drill: triads, m(add9), sus;
   - lo-fi, R&B and neo-soul: 7ths to 13ths;
   - house: m7, m9, 7sus4;
   - future bass: maj7, add9;
   - cinematic: triads, power chords, add9, maj7#11.
   On 5-plus-note chords, drop the 5th first, then the root (the bass has it). Keep the 3rd, the 7th and the named colour tone.
6. **Voice the first chord.**
   - Pick the top note deliberately (64–72, or at least a 3rd below the lead melody).
   - Fill down with the required tones inside the window: 52–76 for keys, 55–79 for pads, floor about 48 under an 808.
   - Check every adjacent interval against the low-interval limits (table below).
7. **Voice-lead the rest** with the nearest-voicing algorithm (`references/voicing-and-voice-leading.md` §5, procedure or Python):
   - hold common tones, move the others to the nearest chord tone;
   - score total motion, plus a penalty for parallel 5ths and octaves between bass and top voice, plus a penalty for top-voice leaps beyond a 4th;
   - also try the inversion above and the one below, and keep the cheapest;
   - for loops, also score the last chord → first chord.
8. **Place the bass.** Use roots or slash notes in 36–52, leaping 4ths and 5ths, ideally moving against the top voice. Under an 808, leave the low register out of the chord MIDI and pass the roots (pitch class plus bar positions) to `music-bass-808`. Pedal points are a deliberate choice, not an accident.
9. **Spend at most one colour device per 4–8 bar context**, usually in the turnaround bar (`references/color-devices.md`). Check the genre baseline for what counts as surprising there. If the melody spends its surprise in that bar, stay diatonic.
10. **Apply the genre comping rhythm** on the 16-step grid: pads, stabs, anticipations, arps, rolls (`references/genre-harmony-and-comping.md` §4). Set velocity, roll and humanise.
11. **Run the checklist** at the end of this file. Read every voicing back as MIDI numbers with FL labels.
12. **Deliver it as a MIDI file** (see FL Studio delivery), and report the key, the progression and a voicing table.

## Function and cadences (compact)

| Cadence | Motion | Effect | Example (C) |
|---|---|---|---|
| Authentic | V(7) → I | full stop | `G7 43 | 53 55 59` → `C 48 | 52 55 60` |
| Half | … → V | comma: end of a verse or pre-chorus | `Dm 50 | 62 65 69` → `G 43 | 62 67 71` |
| Plagal | IV → I (or iv → I) | "amen"; minor plagal = tears | `Fm 41 | 60 65 68` → `C 48 | 60 64 67` |
| Deceptive | V → vi | surprise; extends the phrase | `G7 43 | 53 55 59` → `Am 45 | 52 57 60` |
| Phrygian half | iv6 → V in minor | flamenco pull | `Dm/F 41 | 57 62` → `E 40 | 56 59 64` |
| Backdoor | iv7 → bVII7 → I | soulful soft landing | `Fm7 41 | 56 60 63` → `Bb7 46 | 56 62 65` → `Cmaj7 48 | 55 59 64` |

## Emotion → progression cheat sheet (convention)

| Mood | Progression (library #) | Colour and voicing |
|---|---|---|
| Optimistic, anthemic | I–V–vi–IV (#1); IV–I–V–vi | add9, triads; top voice on the root or 5th |
| Melancholic but hopeful | vi–IV–I–V (#2) | m9/maj9 with a held top note |
| Nostalgic, bittersweet | royal road IV–V–iii–vi (#11); I–III–IV–iv (#6); borrowed iv | maj7, m7; the iv's b6 line |
| Warm, late-night, jazzy | ii–V–I (#7); I–vi (#13); "Just the Two of Us" (#10) | rootless 9ths and 13ths, rolled |
| Floating, unresolved | IV–iii–vi (#12); end the loop on IV | no tonic chord |
| Restless, forward | end the loop on V or V7 (#3, #20) | dominant at the loop end |
| Sad, serious | i–VI–III–VII (#18); i–iv–V7 (#20) | m(add9), sparse |
| Dark with a lift | trap i–VI–v (#21) | major VI as the light |
| Cold, tense | drill i–v–VI / i–VII–VI (#22); tonic pedal | sparse triads, sus, dim stabs |
| Menace, villain | Phrygian i–bII over a pedal (#23); b6→5 semitone | b2 grinding on the root |
| Fateful, dramatic | Andalusian i–bVII–bVI–V (#19) | harmonic-minor V |
| Heroic, triumphant | i–bVI–bVII–i (#25); bVI–bVII–I | power chords, brass planing |
| Wonder, awe | chromatic mediant (I→III, I→bVI); Lydian maj7#11 | wide, bright, slow |
| Cool, groovy | Dorian vamp i9–IV9 (#14); deep-house m9 (#17) | stabs; the Dorian major 6th |
| Soulful, church | gospel walk-up (#16); backdoor (#15) | chromatic bass, 13ths |
| Retro, sweet | I–vi–IV–V (#3); Canon (#4) | inversions, a walking bass |
| Swagger | I–bVII–IV (#5); 12-bar blues (#24) | dominant 7ths, shells |
| Noir, spy | minor ii–V–i (#8); line cliché | m(maj7), m6 |
| Hope after sadness | Picardy third ending | major tonic as the last chord |

## Quick-pick voicings (verified; bass | upper; full list in the library)

| Use | Voicing |
|---|---|
| Pop axis, expensive (C) | `Cadd9 48 | 55 60 62 64` → `G6 43 | 55 59 62 64` → `Am7 45 | 55 57 60 64` → `Fmaj9 41 | 55 57 60 64` |
| Emotional vi–IV–I–V (C) | `Am9 45 | 55 59 60 64` → `Fmaj9 41 | 55 57 60 64` → `Cmaj9 48 | 55 59 62 64` → `G6 43 | 55 59 62 64` |
| Neo-soul ii–V–I (C) | `Dm9 38 | 53 57 60 64` → `G13 43 | 53 57 59 64` → `Cmaj9 36 | 52 55 59 62` |
| Lo-fi I–vi (C) | `Cmaj9 48 | 52 55 59 62` → `Am9 45 | 52 55 59 60` |
| Royal road (C) | `Fmaj9 41 | 55 57 60 64` → `G13 43 | 53 57 59 64` → `Em11 40 | 55 57 59 62` → `Am9 45 | 55 59 60 64` |
| Trap i–VI–v (F minor) | `Fm 41 | 56 60 65` → `Db 37 | 56 61 65` → `Cm 36 | 55 60 63` |
| Drill i–v–VI (G minor) | `Gm 43 | 55 58 62` → `Dm 38 | 53 57 62` → `Ebmaj7 39 | 55 58 62` |
| Epic minor (A minor) | `Am 45 | 64 69 72` → `F 41 | 65 69 72` → `C 48 | 64 67 72` → `G 43 | 62 67 71` |
| Dorian vamp (A) | `Am9 45 | 55 59 60 64` → `D9 38 | 54 57 60 64` |

Under an 808, drop the bass numbers. The 808 plays the same roots (`music-bass-808`).

## Voicing types (examples in C; details in voicing-and-voice-leading §2)

| Type | Shape | Example |
|---|---|---|
| Closed | all within an octave | `Cmaj7 48 | 60 64 67 71` |
| Open / spread | wide at the bottom | `Cmaj7 48 | 55 64 71` |
| Drop-2 | 2nd-highest note dropped an octave | `Cmaj7 48 | 55 60 64 71` |
| Shell | root + 3rd + 7th | `Cmaj7 48 | 59 64`; `G7 43 | 53 59` |
| Rootless (bass or 808 has the root) | 3-5-7-9 / 7-9-3-13 | `Dm9 38 | 53 57 60 64`; `G13 43 | 53 57 59 64` |
| Quartal ("So What") | 4ths plus a top major 3rd | `Dm11 38 | 50 55 60 65 69` |
| Spread 10th (ballad) | root + 10th low, cluster high | `Cmaj9 36 | 48 64 67 71 74` |
| sus / add9 / m(add9) | open, airy, sad-pretty | `Csus2 48 | 60 62 67`; `Cadd9 48 | 55 64 74`; `Am(add9) 45 | 57 60 64 71` |

## Low-interval limits and register floors

Approximate Berklee-style arranging values. Treat them as **convention**: sources differ and timbre shifts them. Read each as "the lower note of the interval at or above this MIDI note".

| Interval | m2 | M2 | m3 | M3 / P4 | TT | P5 | m6 | M6 / m7 / M7 | m9 | M9 | M10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Lowest note | 52 (E3) | 51 (Eb3) | 48 (C3) | 46 (Bb2) | 47 (B2) | 34 (Bb1) | 43 (G2) | 41 (F2) | 40 (E2) | 39 (Eb2) | 34 (Bb1) |

| Part | MIDI range **(convention)** |
|---|---|
| 808 / sub | about 24–40 (C1–E2, FL: C2–E3) |
| Keys left-hand bass (no 808) | 36–52; root, 5th or octave only below 48 |
| Chord upper voices with an 808 | at or above about 48, prefer 52–76 (E3–E5, FL: E4–E6); 3rds at 48 or above; 7ths and 9ths at about 55 or above; clusters at about 60 or above |
| Pads | 52–79 |
| Bells, plucks, arps | 60–96 |
| Chord top voice | at least a 3rd below the lead melody, or in another octave |

## Genre defaults (convention; full detail in genre-harmony-and-comping)

| Genre | Chords per bar | Vocabulary | Comping | Library # |
|---|---|---|---|---|
| Trap (130–160 HT) | 1 per 1–2 bars | minor triads, m(add9), sus | sustained pad, or bell arp at steps 1,4,7,9,12,15 | 18, 19, 21, 23 |
| Drill (138–145) | 1 per 1–2 bars | sparse triads, sus, dim | strings on step 1, gap before the bar ends | 22, 23 |
| Boom bap (85–95) | 1–2 per bar (sample) | m7, 9, 7#9 | chops at steps 1, 7, 15 | 7, 14, 24 |
| Lo-fi (70–90) | 1 per bar | maj7, m7, 9, 11, 6/9 | whole or half notes, roll 10–30 ms, velocity 60–90, humanised | 7, 9, 12, 13 |
| R&B / neo-soul (60–100) | 1–2 per bar + passing | m9, maj9, 13, slash | next chord on step 15, rolled | 10, 14, 15, 16 |
| Pop (90–130) | 1 per bar; 2 in the pre-chorus | triads, add9, sus | 8th pulses or 1, 2&, 4; push changes a 16th or 8th early | 1, 2, 3, 18 |
| House (118–126) | 1 per 1–2 bars | m7, m9, 7sus4 | offbeat stabs at steps 3, 7, 11, 15, 1 step long | 14, 17 |
| EDM / trance (128–140) | 1 per bar | triads, sus | offbeat plucks or a 16th gate with sidechain | 1, 18, 25 |
| Future bass (140–160 HT) | 1 per bar | maj7, m7, add9 | chops at steps 1, 4, 7, 9, 12, 15 with pitch swells | 2, 11 |
| Synthwave (85–118) | 1 per bar | triads, add9, sus | 16th arpeggio | 18, 25 |
| Cinematic | 1 per 2–8 bars, or a pedal | triads, power, add9, maj7#11 | whole-note pads, ostinato over a pedal | 19, 20, 25, mediants |

## Colour devices (one per predictable context; details and spellings in color-devices)

| Device | Example in C | Use it for |
|---|---|---|
| Borrowed iv / bVI / bVII | Fm, Ab, Bb in C major | bittersweet (iv), epic (bVI, bVII); turnaround bar |
| Secondary dominant | E7→Am (V/vi), D7→G (V/V), A7→Dm (V/ii) | forward pull; R&B, gospel, pre-chorus |
| Tritone sub | Db9(#11) for G7 → Cmaj9 | slinky chromatic bass; R&B, neo-soul, lo-fi |
| Chromatic mediant | C→E, C→Ab, C→A, C→Eb | wonder or reveal; cinematic, last chorus |
| Pedal point | Bb/C, Ab/C over a held C | builds; trap and drill (808 holds the root), house |
| Picardy third | A minor piece ends on A major | hope at the end |
| Line cliché | Am → Am(maj7) → Am7 → Am6 | noir intro or turnaround |
| Modulation | pivot chord; V7 of the new key; +1/+2 semitone lift | last chorus or last drop; verse → chorus |

## FL Studio delivery

- **Do not use `fl_add_chord_progression` or `fl_add_notes` for chords.** On FL 21 they only *queue* notes for the "MCP PianoRoll" script, which cannot run under FL 21's embedded Python, so nothing reaches the piano roll. Deliver chords as **MIDI files** instead, using the family workflow in `music-theory-core` (`references/fl-delivery.md` and `references/make_midi_template.py`; PPQ 96; run with `uv run --with mido --no-project python make_midi.py`).
- Build note tuples with `lead()` (voicings) from `references/voicing-and-voice-leading.md` §5 and `comp()` (rhythm) from `references/genre-harmony-and-comping.md` §6. Write one file per part: `chords.mid` (keys or pad), plus optional `arp.mid` or `stabs.mid`.
- **Under an 808,** `chords.mid` holds upper voices only. The 808 or bass is its own .mid from `music-bass-808`, with the same roots on the same bars. Without a bass part, include the left-hand bass (36–52) in `chords.mid`.
- **Clamp the loop end:** no note may end past the last bar, or FL adds an empty bar. An anticipation (`N`) on the last bar is clipped, and chord 1 re-strikes on step 1.
- Chords are written at sounding pitch: MIDI 60 shows as "C5" in FL's piano roll.
- **Don't put chords on a channel set to Mono** (the 808 glide setting). Mono cuts chords down to one note.
- `fl_set_step_sequencer` is for on/off drum rows only, not chords. Mixer volume, pan and routing for the chord bus can be set directly. EQ and reverb can only be described (`music-mix-master`).
- **Hand-off to the user:**
  - key, mode and BPM;
  - the progression in Roman numerals and chord names;
  - a voicing table (chord, MIDI numbers, FL names);
  - the comping pattern;
  - which .mid goes onto which channel;
  - instrument suggestions (e.g. FL Keys/FLEX Rhodes, a pad, a supersaw).

## Quality checklist

- [ ] Every chord is re-spelled from its formula: no foreign notes; the 3rd, the 7th and the named colour tone are present. Harmonic-minor V is major (B natural in C minor).
- [ ] Every adjacent interval, bass included, sits above its low-interval limit. Nothing below MIDI 48 except root, 5th or octave.
- [ ] Under an 808, upper voices are at or above about 48 (prefer 52 or above), and nothing doubles the 808 an octave up in the 40–55 zone.
- [ ] Upper-voice motion is 6 semitones or less per change (the loop restart and deliberate planing excepted). Common tones are held.
- [ ] No parallel 5ths or octaves between bass and top voice, unless it is intentional planing (power chords, deep-house chord memory, fanfare).
- [ ] The top voice reads as a stepwise line and sits under the lead.
- [ ] Harmonic rhythm and comping match the genre; changes land on downbeats (or deliberate anticipations).
- [ ] Loop genres have no full V7→I inside the loop unless resolution is the point.
- [ ] At most one colour device per 4–8 bar context, not stacked with a melodic or drum surprise.
- [ ] Every register is named as MIDI plus FL label; the .mid ends inside the last bar.

Common mistakes:
- Block root-position triads jumping around: voice-lead them instead.
- Close 3rds or 2nds around MIDI 36–47 under an 808.
- Writing the chords an octave off because of FL's "C5" = 60 labelling.
- Stuffing every extension into busy trap drums: medium harmony suits busy drums.
- Changing chords every beat under a rapper.
- Trying to make the piano-roll MCP tools write chords on FL 21.
- Forgetting that after transposing, the voicing and the low-interval limits must be re-checked.

## References

- `references/progression-library.md` — open when choosing or spelling a progression: 25 loops with Roman numerals, a concrete key, a voice-led MIDI voicing, character, genres and songs; plus the Hooktheory and Cheung statistics and transposition rules.
- `references/voicing-and-voice-leading.md` — open when voicing chords by hand or in code: function and cadence spellings, every voicing type with MIDI examples, the full low-interval and register tables, the step-by-step nearest-voicing procedure and its Python implementation, and guide-tone lines.
- `references/color-devices.md` — open when a progression needs a twist, a key change or an emotional peak: the surprise budget, genre surprise baselines, every chromatic device spelled with when-to-use notes, modulation routes and placement recipes.
- `references/genre-harmony-and-comping.md` — open when matching a genre or writing the rhythm of the chords: genre harmony table (trap to amapiano), harmonic rhythm, 16-step comping grids per genre, humanise and roll values, and the `comp()` grid-to-MIDI helper.

## Related skills

- `music-theory-core` — hub: scale and chord formula tables, keys, tick math, genre cards, the budgets, FL delivery and the MIDI template.
- `music-bass-808` — 808 and bass roots, register, slides and kick lock under these chords.
- `music-melody-hooks` — the lead over the chords: chord tones on strong beats, and the melody's own surprise.
- `music-arrangement` — when chords enter or drop out, register slotting against other parts, builds over pedals.
- `music-drums-groove` — the drum grid the comping must lock to.
- `music-mix-master` — EQ and space for keys and pads, sidechain for stabs and supersaws.
