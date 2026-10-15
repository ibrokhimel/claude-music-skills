---
name: music-melody-hooks
description: Writes beautiful, memorable melodies, hooks, leads, toplines, riffs, motifs and counter-melodies, and delivers them to FL Studio as MIDI files. Use whenever the user wants a melody, hook, earworm, catchy lead, topline, vocal melody, bell/pluck/piano melody, trap or drill melody, EDM drop lead, synth riff, lo-fi keys line, R&B run, afrobeats or amapiano lead, cinematic theme, counter-melody or harmony line. Also use when they say "make it catchier", "the melody is boring/random/robotic", "write a hook over these chords", "add a melody to my beat", or make any beat that needs a melodic part. Covers contour and the single climax, step/leap rules and gap-fill, range, chord tones vs non-chord tones (appoggiatura, suspension, passing, neighbor), melodic rhythm and syncopation, motif development (sequence, inversion, augmentation, displacement), period/sentence/call-and-response templates, an earworm checklist, genre melody styles and an 11-step piano-roll algorithm.
---

# Melody and hooks

This skill turns a key, a chord progression and a genre into a melody that is simple, singable and memorable, with exactly one surprise. It covers hooks, leads, toplines, bells and riffs, plus counter-lines that support them. The method is a pipeline: set the context, write the rhythm first, put chord tones on strong beats, fill mostly by step, build one arch with one climax, answer the call, check the numbers, subtract, layer, humanize. Delivery is a `.mid` file per part via the `music-theory-core` MIDI template. Pitches are MIDI with **C4 = 60**; FL labels MIDI 60 as "C5", so always write e.g. "MIDI 69 (A4, FL: A5)".

## Core principles (and why)

1. **Mostly steps, few leaps.** 65–80% of intervals are 0–2 semitones and at most 10% are leaps of 5 or more. Real melodies are dominated by small steps (Patel 2007), so listeners expect them. **(sourced direction, convention numbers)**
2. **After a leap, turn back by step (gap-fill).** Leaps land near the edge of the range, and the line must retreat (von Hippel & Huron 2000). Unfilled leaps sound random. **(sourced)**
3. **One arch, one climax.** The arch is the most common phrase contour in corpora. Earworms use common contours (Jakubowski 2017). Put the highest note once, 55–75% of the way through, on a strong beat. **(sourced shape, convention placement)**
4. **Chord tones on beats 1 and 3, colour in between.** About 75–85% of strong-beat notes are chord tones. Non-chord tones resolve by step. This makes the melody imply its harmony, so it still works when soloed. **(convention; real songs: 45–69% chord tones overall, Hooktheory)**
5. **Accented dissonance is where emotion lives.** Appoggiaturas and sequences were the devices most reliably tied to tears in Sloboda's 1991 study. Spend the climax on an appoggiatura or suspension when the moment should ache. **(sourced)**
6. **Rhythm first.** The same pitches in a different rhythm feel unfamiliar. Hooks need 4–8 onsets per bar, at least one syncopation and one rest. **(practitioner-sourced, convention numbers)**
7. **Familiar frame + exactly one surprise + lively note rate.** Earworms combine common contours with locally unusual intervals or repeated notes, at faster tempi (Jakubowski). Pleasure peaks when a surprise follows predictability (Cheung 2019). Never stack surprises. **(sourced)**
8. **Repeat the hook, vary its surroundings.** Repetition makes sound musical (Margulis, Deutsch), but identical repetition lowers liking (Gold 2019). Keep the hook fixed and change drums, harmony, register and layers. **(sourced)**
9. **Leave room.** Keep leads ≥ MIDI 52 (E3, FL: E4) when an 808 or log drum is present, leave rests for the vocal or drums, and use only one lead at a time in a drop. **(convention + Bax-shop)**

## Procedure: the 11-step piano-roll melody algorithm

Run these steps in order for every melodic part. Write notes as `(start_beat, midi, length_beats, velocity)`, with beat 0 = bar 1 beat 1.

1. **Set the context.**
   - Key and scale by genre: trap uses natural minor with a harmonic-minor V, or Phrygian; drill uses minor with b2/b6; pop uses major or Aeolian; lo-fi uses Dorian; R&B uses major-7/minor-9 harmony with pentatonic runs; afro uses major pentatonic.
   - Set the BPM and the loop length (2, 4 or 8 bars), and get the chords with their beat ranges. If there are no chords yet, get them from `music-chords-voicing` first.
   - Pick the role (topline, lead, bells, counter) and its register from the range table below.
2. **Write the rhythm first.**
   - Use 4–8 onsets per bar for a hook (see the density table for other roles), with at least one syncopation (an off-beat onset held across a stronger beat) and at least one rest of 0.5 beat or more.
   - Start from a cell: tresillo `0, 0.75, 1.5` per half bar; short-short-long `0, 0.5, 1(long)`; off-beat stabs `0.5 1.5 2.5 3.5`; quarter triplets `0, 0.667, 1.333`.
   - Write a 1–2-bar rhythm and reuse it for the answer phrase.
3. **Place the pitch skeleton.**
   - On each strong-beat onset (beats 1 and 3, plus any note sounding there), put a chord tone of the current chord.
   - Priority: the **3rd** (emotion), then the **5th** (open), then the **7th or 9th** (R&B, lo-fi colour). Keep the **root** for cadences.
   - At chord changes, move by step or hold to the nearest 3rd or 7th of the new chord (guide tones).
4. **Fill.**
   - Connect skeleton notes with passing and neighbor tones on weak positions.
   - Hit 65–80% steps. After any leap of 5 or more semitones, move the next 2–4 notes stepwise in the opposite direction.
   - If the line drifts more than 7 semitones from its running mean, steer back.
5. **Call and response.**
   - Bars 1–2 end on an unstable degree (2, 5 or 7).
   - Bars 3–4 repeat bars 1–2 with a tail change that ends on 1 or 3.
   - For 8 bars, use the period (4+4) or the sentence (2+2+4, with continuation fragments climbing). For loops, make the last note lead into the first one by step or by the leading tone.
6. **Climax.**
   - Make exactly one note the highest, at 55–75% of the phrase, on a strong beat. For 4 bars that is bar 3 beat 3 (beat 10). For 8 bars it is bar 6 beat 1 (beat 20).
   - Spend the **one surprise** there: a 5th–octave leap with gap-fill after it, an appoggiatura, a borrowed note, or a long hold after repeated notes.
   - Give it velocity 110–120 and put the title lyric there.
7. **Check range and register.**
   - Toplines span ≤ 14 semitones inside the voice window. A hook motif spans ≤ 9. Bells and leads can reach about 24 with doubling.
   - Keep the lead ≥ 52 when an 808 is present, and keep the counter-line ≥ 3 semitones from the lead.
8. **Develop across the song.**
   - Verse: lower and narrow. Pre-chorus: an ascending sequence. Chorus: 3–5 semitones higher with longer notes. Drop: the hook as a riff (A A A A′).
   - Use augmentation for half-time drops or cinematic restatements, diminution and fragmentation for builds, and displacement for a variation every 4th or 8th bar.
9. **Layer.**
   - Add an octave copy (±12, velocity −10–20%) or a diatonic 3rds/6ths harmony (`diatonic_shift(n, 2)` / `(n, -5)`).
   - Add a counter-melody: about half the density, in the lead's rests, contrary at the lead's leaps, in its own register band, and with no parallel 5ths or octaves on consecutive strong beats.
10. **Subtract and check.**
    - Remove 10–20% of the notes.
    - Run `check_melody()` from `references/worked-examples.md`: steps 0.65–0.80, leaps ≤ 0.10, climax once at 0.55–0.75, strong-beat chord tones ≥ 0.75, no out-of-scale notes, nothing past the loop end.
    - Score the hook with the 12-point checklist and keep it at 9 or more.
    - Confirm the motif is still recognisable after 4 repeats and that the chord changes are audible when it is soloed.
11. **Humanize by genre.**
    - EDM, trap and drill: tight grid, velocity ±5.
    - Afro: ±5–10 ms, velocity ±10.
    - Lo-fi and R&B: ±10–20 ms, velocity ±10–15, 8th swing 55–62% (MPC scale) via `swing8()`.
    - Never move the climax or the hook's downbeats.

When the user gives no chords, either write chords first via `music-chords-voicing`, or (for a bare hook) choose a 4-chord loop from the genre card and state it.

## Defaults tables

**Contour by section** **(convention)**

| Section / style | Contour |
|---|---|
| Hook, chorus, theme, EDM lead | arch, climax at 55–75% |
| Dark loop (trap, drill, lo-fi) | descending or inverted arch, falling to the tonic at the loop end |
| Pre-chorus, build | ascending sequence; save the peak for the downbeat after |
| Verse topline | narrow, near-stationary, speech rhythm |
| R&B phrase end | descending pentatonic run onto a chord tone |

**Interval mix** **(convention)**: steps (0–2) 65–80% · thirds (3–4) 15–25% · leaps (≥5) ≤ 10%, one signature leap per hook. Pentatonic lines: count steps in scale degrees.

**Range and register** (MIDI, scientific; FL name = octave + 1) **(convention)**

| Part | Span | Register |
|---|---|---|
| Pop topline | 9–14 | male 45–69 (A2–A4); female 53–77 (F3–F5) |
| Verse topline | 5–9 | chorus sits 3–5 higher |
| Hook motif | ≤ 9 | doubling adds width |
| Trap/drill bells | 12–14 | 64–84 (E4–C6) |
| EDM lead | 10–15 | 64–84, stacked ±12 |
| Lo-fi/R&B keys or vocal | 8–14 | 57–79 |
| Counter-melody | ≤ 10 | its own band, ≥ 3 semitones from the lead |

**Onsets per bar by role** **(convention)**: verse topline 4–10 · chorus 3–8 (longer notes) · EDM riff 4–12 · trap bells 4–8 · lo-fi keys 3–6 · counter ≈ ½ the lead · cinematic theme 1–4.

**Non-chord tones (quick)** **(mechanics sourced; effects convention)**

| NCT | Motion | Accent | Effect |
|---|---|---|---|
| Passing | step–step, same direction | weak | smooth flow |
| Neighbor | step out, step back | weak | decoration, hooky wobble |
| Appoggiatura | leap in, step out (usually down) | strong | ache, the "tear" device (Sloboda) |
| Suspension | tied over the change, resolves down (4–3, 9–8) | strong | longing, delayed release |
| Anticipation | next chord's tone, early | weak | push, forward motion |
| Escape | step out, leap back the other way | weak | sigh, cadence ornament |

**Tension colours:** 9th = airy · sus4→3 = longing · 7→1 = urgent · b6→5 (minor) = sorrow, trap · b2→1 = menace, drill/phonk · maj7 over IV = dreamy, lo-fi · Dorian 6 = bittersweet · b3/b7 over major = blues/R&B grit.

**Motif operations** (all one-liners on note lists; code in `motifs-and-phrases.md`): repetition (`start += N`) · real transposition (`midi += k`) · diatonic sequence (shift scale steps) · inversion (`2*axis - midi`, or diatonic) · retrograde · augmentation/diminution (×2/×0.5 starts and lengths) · rhythmic displacement (±0.25/0.5) · fragmentation (repeat the head) · tail change (last 1–2 notes) · interval expansion (the climax surprise) · chord adaptation (keep rhythm and contour, snap to the new chord). Rule of three: state, repeat, break.

**Genre quick picks** (full cards in `hooks-and-genre-styles.md`) **(convention unless sourced there)**

| Genre | Scale | Register | Rhythm / density | Signature device |
|---|---|---|---|---|
| Trap | minor + harmonic V, Phrygian | 64–84 | 4–8/bar, tresillo, space | b6→5, leading tone, octave layer |
| UK/NY drill | minor, b2/b6 | 72–88 | 2–4-note cold motif, quarter triplets, empty bars | b2/b6 neighbors, sequence then break |
| Plugg/pluggnb | major-ish, m7/add9 | 67–88 | sparse sine/bell phrases | end on 9ths/maj7s |
| Lo-fi | Dorian, minor pentatonic | 57–79 | 3–6/bar, swung 8ths, rests | target 7ths/9ths, unresolved ending |
| R&B | major-7/minor-9, pentatonic runs | 57–79 | syllabic body + 16th-triplet runs | descending run onto a chord tone, pushes |
| Pop topline | major, Aeolian | voice window | verse speech-like, chorus longer notes | title on the climax, period/sentence |
| EDM drop | minor/major, vi–IV–I–V | 64–84 ±12 | 1–2-bar riff ×4, A A A A′ | repeated-note head + one leap |
| House | minor/Dorian stabs | 60–79 | off-beat stabs (3 7 11 15) | top voice of the stab moves by step |
| Amapiano | m9/maj7 jazz | 60–84 | smooth piano, arps | common tones; log drum answers below C4 |
| Afrobeats | major pentatonic | 64–84 | tresillo/clave, repeated notes, pushes | 1-bar call + 1-bar response |
| Cinematic | Aeolian, Phrygian | 50–74 | long notes, 1–4/bar | 5th/6th opening leap filled by step; augment later |

## FL Studio delivery

- **Melodies are delivered as MIDI files.** On FL 21, `fl_add_notes` / `fl_add_chord_progression` only queue notes and do not apply them. Write one `.mid` per melodic part (lead, lead_oct, harmony, counter) with the template at `music-theory-core/references/make_midi_template.py`. Its notes are `(start_beat, midi, length_beats, velocity)`, the exact format of this skill. Paste lists with `parse()` from `references/worked-examples.md`. Set `BPM` and `BARS`. Run `uv run --with mido --no-project python make_midi.py` in `Documents/flstudio/<beat-name>/`.
- **Pitch is real pitch** (not the sampler-at-60 drum convention). MIDI 72 is C5 scientific and shows as "C6" in FL's piano roll. Tell the user the register in both namings.
- **No note may end past the last bar**, or FL adds a bar. The template clamps ends. Still, plan loop tails to end by the bar line, including pickups and shifted (`shift_beats`) copies.
- **Triplets and swing:** quarter triplet = 64 ticks, 8th triplet = 32, 16th triplet = 16 (PPQ 96). For exact 8th swing use `swing8()`; for 16ths use the template's `swing16()`. FL's channel swing knob is a different scale: start around 15–30% and match by ear, noting it only acts when both global and channel swing are above 0.
- **Glides for leads** (rage, future bass, synthwave portamento): only overlapping notes glide, only with Mono + Porta, and only on FL native instruments, Sampler, FLEX or 3x Osc. They do not work on VST/AU plugins.
- **Apply directly** with MCP: `fl_set_tempo`. `fl_list_channels` maps names. Then hand off. The user drags each `.mid` into the matching channel's piano roll.
- **Hand-off line for melodic parts:** key/scale, chords, register (MIDI + FL names), file → channel → suggested sound (bells, pluck, Rhodes, supersaw...), layering (octave copy volume −3 to −6 dB), and the one surprise you placed, so the user knows where the hook's identity is.
- Mixer moves for leads (presence, delay/reverb timing, ducking under vocals) belong to `music-mix-master`.

## Quality checklist and common mistakes

Before writing MIDI, confirm:
- [ ] Every pitch is in the stated key, or is a deliberately labelled chromatic/borrowed note. Check MIDI numbers against each chord's spelling.
- [ ] Strong beats sound chord tones except labelled appoggiaturas or suspensions.
- [ ] Steps 65–80%, leaps ≤ 10%, every leap ≥ 5 followed by reversal.
- [ ] One highest note, once, at 55–75%, on beat 1 or 3.
- [ ] One surprise only, and it sits at or near the climax.
- [ ] At least one syncopation and one rest per bar of hook; density fits the role.
- [ ] Range fits the role; the lead is ≥ 52 with an 808; the counter is ≥ 3 semitones away and never crosses.
- [ ] Call ends open (2/5/7), response ends closed (1/3); the loop seam connects by step.
- [ ] Nothing ends past the last bar; triplet starts round to exact ticks.

Common mistakes:
- **Random-walk melodies:** equal steps and leaps, no gap-fill, several peaks. Fix with steps 3–4 of the procedure.
- **Climax on the first note or repeated at the top:** move it to 55–75% and make it unique.
- **Root on every downbeat:** sounds like a bassline. Target 3rds, 5ths and 7ths, and keep the root for the cadence.
- **Pitch-first writing:** the result has no rhythmic identity. Write and clap the rhythm first.
- **Too many surprises** (chromatic note + leap + syncopation all at once): keep one.
- **Melody in the 808 register,** or counter-line doubling the lead at the octave on downbeats.
- **Harmonic minor everywhere:** use the raised 7th only over V. Elsewhere, natural minor avoids the augmented 2nd.
- **Endless identical loop:** vary the surroundings or the tail every 4th or 8th bar (A A A A′).
- **Writing notes into FL with `fl_add_notes` on FL 21:** nothing appears. Always deliver MIDI.

## References

- `references/melodic-grammar.md`: open when shaping contour, checking interval stats, choosing a register, placing chord tones vs non-chord tones (full NCT table with examples), choosing tension notes, or writing melodic rhythm (cells, syncopation, pushes, density, humanize values).
- `references/motifs-and-phrases.md`: open when developing a motif (operation table + tested Python helpers + demo outputs), building a period, sentence (worked 8-bar sentence), call-and-response or 4/8-bar loop, planning melody across verse/pre/chorus/drop, or writing a counter-melody or harmony layer (rules + parallel-5ths check).
- `references/hooks-and-genre-styles.md`: open when the goal is catchiness or emotion (earworm study, surprise budget, chill devices, 12-point hook scoring) or when writing in a specific genre (style cards for 26 genres).
- `references/worked-examples.md`: open for drop-in note lists and the code to use them (`parse()`, `swing8()`, `check_melody()`). It holds 9 validated examples: trap bells, pop period topline, counter-melody, lo-fi Dorian, R&B run, EDM drop, afrobeats, drill (fits `ny-drill-midi`), cinematic theme.

## Related skills

- `music-theory-core`: hub; MIDI/FL octave mapping, scales, genre cards, the MIDI template and delivery workflow, budgets and the science of beauty.
- `music-chords-voicing`: progressions and voicings the melody sits on; harmonic rhythm.
- `music-bass-808`: bass and 808 note choice, slides and register (the melody stays above it).
- `music-drums-groove`: the groove the melody's rhythm should lock to or answer.
- `music-arrangement`: where hooks enter and return, focal-element limits, register slotting, builds and drops.
- `music-mix-master`: making the lead sit (EQ presence, delay/reverb timing, ducking).
