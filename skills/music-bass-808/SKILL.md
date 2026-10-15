---
name: music-bass-808
description: Writes basslines and 808s and makes the low end work with the kick, delivered to FL Studio. Use whenever the user wants an 808, 808 pattern, sliding/gliding 808, bassline, bass line, sub bass, reese, wobble, log drum or walking bass. Also use when they ask to make a trap, drill, plugg, rage or phonk beat (the 808 part), write bass for a chord progression, tune an 808 to the key, pick the 808 octave, fix a kick and 808 clash or muddy low end, set FL Studio Mono/Porta/Slide, or make bass audible on phones. Covers note choice (roots on chord changes, fifths, octaves, approach/walking tones, pedal tones); kick-bass lock/gaps/sidechain and tuning kick vs bass; 808 tuning, register, length, slides and saturation; 15 genre bass grids (pop, house, techno, funk, disco, reggae, Motown, R&B, DnB, dubstep, UKG, afrobeats, amapiano, synthwave, lo-fi); and MIDI-file delivery with overlapping slide notes.
---

# music-bass-808

This skill writes the bass part — an 808, a sub, or a synth or electric bass — so that it names the chords, locks with the kick, and translates from club systems down to phone speakers. It turns a key, a chord progression, a tempo and a kick pattern into exact MIDI notes (pitch, start, length, velocity, slides). It delivers them to the user's FL Studio 21 as a MIDI file, plus channel settings and low-end mix moves. Theory basics (MIDI/Hz math, scales, chord spelling) live in `music-theory-core`; the kick pattern itself comes from `music-drums-groove`.

## Core principles (and why)

1. **The bass decides the chord.** Whatever note sits lowest is heard as the root. Play the chord root on every chord change unless a slash chord is intended. Root and 5th state a chord most strongly, and beats 1 and 3 matter most **(sourced)**.
2. **One part owns the sub.** Two long sub sources on the same step fight in phase and flutter. Decide per section: 808/bass owns ~30-60 Hz, or the kick does **(convention)**.
3. **Place the bass relative to the kick, not in a vacuum.** Genres are mostly defined by where bass notes sit relative to the kick (with it, between it, or ducked under it) and how long they last.
4. **The short element keys the sustained one.** The kick ducks the bass, never the reverse **(sourced)**.
5. **Fewer, well-placed 808 notes sound bigger.** Start with a hit under each kick plus 1-2 syncopated notes in the gaps **(sourced)**.
6. **Register is physics.** Keep 808 notes around MIDI 24-40, with roots in 26-38 **(derived)**. Below ~32 Hz notes vanish and eat headroom; above ~98 Hz the 808 stops feeling like sub and muddies the low-mids.
7. **Tune by the tail.** A raw 808's pitch is its sustained tail, not its attack. An out-of-tune 808 ruins a mix **(sourced)**.
8. **Slides are punctuation.** 1-2 per bar at most, both notes in key **(sourced)**. Only overlapping notes on a Mono/Porta FL-native channel glide.
9. **Phones can't play sub.** The ear rebuilds a missing fundamental from its harmonics **(sourced)**. Pair every clean sub with saturation or a mid layer.
10. **Mono below ~100-150 Hz** **(sourced)**; width only on a high-passed mid layer.

## Procedure

Follow in order whenever composing a bass or 808 part.

1. **Collect inputs.** Key and mode, BPM, chord progression with chord-change positions (bar/step), genre, and the kick pattern. Get the kick from `music-drums-groove` or the existing beat; if none exists, use the reference kick row in the genre grid. Also: the instrument (808 sample? synth? which FL plugin?) and, for a sample, its measured pitch. If the pitch is unknown, ask the user or plan the tuning step (808 guide section 4).
2. **Pick the sound family and sub owner.** 808 (trap, drill, plugg, rage, phonk, R&B), sine sub plus mid layer (DnB, dubstep, EDM), or plucked/played bass (house, funk, disco, reggae, pop, lo-fi). Then decide who owns the sub (table below).
3. **Pick the kick-bass strategy per section:** K1 lock, K2 gaps or K3 hybrid (table below). Verse and drop may differ.
4. **Fix the register.** 808: put the tonic in the octave inside MIDI 26-37 (key-root picker below). Synth/electric bass: MIDI 28-52. Place each next chord root in the octave nearest the previous note, staying inside the window.
5. **Choose the rhythm template** from the genre grid (`references/bassline-styles.md` or `references/808-guide.md` section 10). Map its steps onto the actual kick: K1 starts on kick steps, K2 fills the kick's silences.
6. **Assign pitches.** Root on each chord's first step. Fill other notes by priority: root > octave > 5th > 4th/b7 > 3rd > scale tones > chromatic. Put an approach tone on step 15 or 16 before a change (half step above or below the next root, its 5th, or the adjacent scale step). Use a pedal tone for intros and builds.
7. **Set lengths.** Long/legato 808s fill to the next note (melodic trap, drill, phonk, rage). Short (≤ 1/8, ~150-300 ms) for bouncy, kick-dense styles. Synth basses follow the style card. In mono, trim every note so it ends at or before the next start unless it is a slide.
8. **Add slides (808/glide styles only).** Choose 0-2 per bar: octave up-slides into turnarounds (trap), m3/P4 up-slides then a sustained low note (drill, 2-3 per 4 bars), 1-2 semitone glides into chord changes (plugg, R&B). Write each as an overlap with a pitch change.
9. **Set velocity.** 808s steady at 100-120 (accent the downbeat). Played basses 90-110 with accents 110-127. Funk ghosts 20-40.
10. **Phrase it.** Build a 2- or 4-bar phrase: state, repeat, vary the end. Put the variation (an approach run, an octave slide, a dropout) in bar 4 or 8. Leave the 808 out for one bar or beat before hooks when the arrangement calls for it (`music-arrangement`).
11. **Validate** with the quality checklist below, then write the MIDI file with the template in `references/bass-midi-delivery.md` and run it.
12. **Tell the user the FL setup:** which file goes to which channel, Mono/Porta/Slide, tuning applied, and any mixer moves (sidechain, sub/drive split) they must do by hand.

## Defaults tables

### Note choice (convention unless marked)
| Position | Default | Alternatives |
|---|---|---|
| First step of a chord | Chord root | Slash-chord bass note only if the chord symbol says so (C/E) |
| Other strong steps (1, 5, 9, 13) | Root or 5th **(sourced)** | Octave |
| Weak steps | Octave, 5th, b7, 4th | 3rd and scale tones as passing notes |
| Step 15/16 before a change | Approach: next root ±1 semitone, its 5th, or the adjacent scale step | Double chromatic from above (+2, +1) |
| Intro/build | Pedal on the tonic (or 5th) | Repeated 8ths, then 16ths into the drop |
| Loop-based minor beats | Chord roots | Minor-pentatonic riff (1, b3, 4, 5, b7) implying the chords |

### Register (MIDI, C4 = 60; FL label = octave + 1)
| Part | Window | Notes |
|---|---|---|
| 808 floor | 24 = C1 (FL C2), 32.7 Hz | Nothing lower **(derived)** |
| 808 root zone | 26-38 = D1-D2 (FL D2-D3), 36.7-73.4 Hz | Sweet spot 28-35 (41-62 Hz) **(derived)** |
| 808 notes | 24-40; brief slide peaks to 43-48 | 48 = C3 (FL C4), 130.8 Hz |
| Synth/electric bass | 28-52 = E1-E3 | Open E = 28 (41.2 Hz) |
| Pads/chords above a busy bass | lowest note ≥ 48 | See `music-chords-voicing` |

**808 key-root picker (26-37 rule, derived):** C 36, C# 37, D 26, D# 27, E 28, F 29, F# 30, G 31, G# 32, A 33, A# 34, B 35. Use C 24 only for a deep, saturated 808. When the root is high (A#, B, C, C#), put riff notes below it rather than above. The full Hz table (MIDI 24-48 with FL labels and harmonics) is in `references/808-guide.md` section 2.

### Kick-bass strategy (convention)
| Strategy | Bass placement | Genres | Needs |
|---|---|---|---|
| K1 Lock | Starts on the kick's steps | Trap, drill, phonk, rage, boom bap, pop/rock 8ths | Short kick, kick layered on 808 (HPF ~40-50 Hz), or sidechain |
| K2 Gaps | Where the kick is silent | House offbeat, tech house, UKG, amapiano, reggae | Little or no sidechain |
| K3 Hybrid | Shared hits, bass ducked 50-150 ms | EDM, pop, future bass, synthwave | Sidechain ratio 4:1+, attack 0-5 ms, release 80-200 ms |

Tune the kick so its fundamental does not coincide with the bass roots **(sourced)**. Move it to an in-key non-root pitch, e.g. the b3 or 5th **(derived)**, using `fl_set_channel_pitch_pan_vol` (cents = 1200 x log2(f_new/f_old)).

### Genre quick picks
| Genre | BPM | Bass/808 | Pattern core (steps) | Length | Slides | Strategy |
|---|---|---|---|---|---|---|
| Trap | 130-150 | 808 | 1, 8, 11 with kick; octave up-slide on 16 | long | 0-1/bar | K1 |
| Drill UK/NY | 138-151 | 808 | 1, 4/5, 8, 11; with or 1/16 after kick | long + whoops | 2-3 per 4 bars, m3/P4 up | K1-ish |
| Plugg/pluggnb | 130-150 | clean 808 | 1, 11, 15 + glide into change | medium | 1-2 st into changes | K1 |
| Rage | 140-170 | distorted 808 | 1, 11 doubled with kick | long | rare | K1 |
| Phonk | 120-160 | distorted 808 | every kick (1, 7, 9, 15 drift) | long/short | rare | K1 / 808 = kick |
| Boom bap | 85-95 | bass/808 | 1, 8, 11, roots and 5ths | short | none | K1 |
| Pop/rock | 90-130 | bass | odd steps, root 8ths | 1.5 steps | none | K1 |
| House | 120-128 | pluck bass | 3, 7, 11, 15 | 1-2 | none | K2 |
| Tech house | 124-128 | pluck | all non-kick 16ths | 1 | none | K2 |
| Techno | 130-160 | rumble | kick tail ducked | n/a | none | kick owns |
| Funk | 95-115 | electric/slap | R on 1, ghosts, b7, approach | 0.5-2 | none | interlock |
| Disco | 115-125 | electric | R / O O per beat | 1-2 | none | K1 + offbeats |
| Reggae | 65-80 | round bass | rest on 1, land on 9 | 2-4 | none | K2 |
| Motown/walking | 100-130 | electric | one per beat | 4 | none | K1 |
| R&B/neo-soul | 65-95 | synth/808 | 1, 8, 11, 15, 16 | mixed | optional | K1 loose |
| DnB | 170-176 | sub + reese | sub whole bar; reese 1, 8, 11 | long | none | own sub |
| Dubstep | 140 | sub + wobble | sub 1, 11; LFO rates | long | none | own sub |
| UKG/2-step | 128-134 | sub/reese | 1, 4, 7, 11, 15 | 2-3 | short porta | K1/K2 |
| Afrobeats | 95-115 | round bass | 1, 7, 13 (+15) | 2-4 | none | K1 loose |
| Amapiano | 108-115 | log drum | 4, 7, 11, 14, 16 / 3, 6, 9, 11, 16 | 1-2 | pitch drop | K2 |
| Synthwave | 80-118 | saw bass | R/O 16ths or R 8ths | 1 | none | K3 light |
| Lo-fi | 70-90 | upright | 1, 8, 11, 15 | 1-4 | none | K1 |

Full grids, worked MIDI and sound notes are in `references/bassline-styles.md` (15 styles) and `references/808-guide.md` section 10 (808 genres).

### 808 essentials
| Topic | Default |
|---|---|
| Tuning | Measure the sustained tail (skip the first 50-100 ms); fix cents with `fl_set_channel_pitch_pan_vol`; keep transposition within ~±7 semitones of the sample pitch **(convention)** |
| Length | Long = to the next note; short = ≤ 1/8 (~150-300 ms) **(convention)** |
| Slides | Mono + Porta, Slide ~40 at 140-150 BPM **(sourced, blog)**; overlap = glide; 1/16 overlap tight, 1 beat slow bend **(sourced)** |
| Slide sound | 1-2 semitones vocal, octave dramatic; up = tension, down = resolution **(sourced)** |
| Velocity | Steady 100-120; ~6 dB swings make the master limiter pump **(sourced)** |
| Translation | Clean sub track (LP ~100 Hz) + driven track (HP 100-150 Hz, saturate, LP 2-5 kHz) **(derived)** |

### Low-end frequency rules
- Sub ~20-60 Hz is felt more than heard; contested bands are 40-60 and 70-100 Hz **(sourced)**.
- Mono below ~100-150 Hz **(sourced)**; bass, 808 and kick centred.
- High-pass ~20-30 Hz on bass-heavy parts **(sourced)**, but keep it below the lowest note's fundamental.
- Mud lives at 200-400 Hz: keep chords ≥ MIDI 48 or high-passed when the bass is busy **(convention)**.
- Bass presence at 900 Hz-1.5 kHz; kick click at 3-5 kHz **(sourced)**.

## FL Studio delivery

- **MIDI files, not piano-roll tools.** On FL 21 `fl_add_notes` and the other piano-roll tools only queue notes; they do not apply them. Write `808.mid` / `bass.mid` with the tested template in `references/bass-midi-delivery.md`. PPQ 96, 1/16 = 24 ticks. Run with `uv run --with mido --no-project python make_bass.py`. One file per channel; the user drags it onto the channel or piano roll.
- **No note may end past the last bar**, or FL adds a bar. The template clamps and reports any overrun. A slide cannot wrap from the last bar into bar 1.
- **Pitch mode, stated in every script docstring:**
  - **Sample-relative (drum-style)**: an 808 one-shot in FL's Sampler with the default root (FL "C5" = MIDI 60). MIDI 60 plays the sample at its own pitch, so write `60 + (target - sample_pitch)`. With a C1 (24) sample, G1 is written 67. This is the user's usual setup (`ny-drill-midi/make_midi.py`).
  - **Pitched**: synth basses (3x Osc, FLEX, Sytrus, GMS, VSTs), or a Sampler whose root note the user set to the measured pitch. Write the true MIDI pitch.
  - Always check the REAL pitch against the register window.
- **One-pitch shortcut:** a root-only 808 on a sample already tuned to the key can go through `fl_set_step_sequencer` (binary string). It rings its natural decay; Mono cuts it at the next hit.
- **Slides:** the user sets Channel settings > Miscellaneous functions (FUNC) > Polyphony: Mono on, Porta on, Slide ~40. Only overlapping notes are guaranteed to glide. If separated notes glide too, the user turns Porta off and keeps Mono **(verify by ear)**. Slides work on FL native generators and the Sampler only, NOT on VST/AU plugins **(sourced)**. Piano-roll "slide notes" do not survive a MIDI file; overlaps do.
- **Tools that do apply on FL 21:**
  - `fl_set_channel_pitch_pan_vol(ch, volume, pan, pitch_cents)`: cent-tune the 808 or the kick (pass the current volume 0.78 and pan 0).
  - `fl_assign_channel_to_mixer`, `fl_set_track_name_color`: put the 808/bass on its own mixer track.
  - `fl_route_track(source, target)`: the 808 SUB / 808 DRIVE split.
  - `fl_set_track_volume` (0.8 = 0 dB).
- **The user does by hand:** sidechain routing ("Sidechain to this track" + Fruity Limiter SIDECHAIN; never `fl_route_track`, which sums audio), EQ, saturation plugins, root-note setting. Give exact settings and see `music-mix-master`.
- **Swing:** bake the drums' swing into tick offsets on even steps: `round(48 x S/100) - 24` ticks at PPQ 96 (S on the MPC/Linn scale). The bass must match the drums exactly.

## Quality checklist / common mistakes

- [ ] Root on every chord change (no accidental inversions under a change).
- [ ] Bass starts match the chosen K1/K2/K3 strategy against the actual kick steps.
- [ ] Only one long sub source sounds per step; anything sharing a step with a long kick is ducked or short.
- [ ] Real pitches inside the window (808 24-40, root 26-38; bass 28-52); no note below MIDI 24.
- [ ] Sample-relative mode used the measured sample pitch. Mistake: a C1 sample with Ab written as 56 sounds at MIDI 20 (26 Hz); write 68 (G#1, 51.9 Hz).
- [ ] Slides: ≤ 2 per bar (drill 2-3 per 4 bars), in key, written as overlaps with a pitch change; never same-pitch overlaps.
- [ ] Mono line: no unintended overlaps (they glide), no stacked notes.
- [ ] Last note ends at or before the final bar line; the file is exactly N bars.
- [ ] 808 velocity steady; ghosts only in funk-type lines.
- [ ] Approach tones are short and on weak steps; chromatic notes never on a chord change.
- [ ] Chords/pads not doubling the bass's 3rd low; their lowest note ≥ MIDI 48 when the bass is busy.
- [ ] Sub mono and centred; the clean sub is paired with saturation or a mid layer; phone check planned.
- [ ] Docstring states key, BPM, mode, sample pitch and the channel settings needed.

Common mistakes:
- Writing the 808 an octave too low because the FL label was read as scientific (FL "C2" = MIDI 24 = C1).
- A busy 808 that copies every hi-hat-driven kick.
- Slides on a VST synth expecting FL Porta to work.
- A long boomy kick under a long 808 with no ducking (flutter).
- Clean sine 808s that vanish on phones.
- Moving every chord root into the same fixed octave, which causes leaps of a 7th or more.

## References

- `references/808-guide.md`: open for any 808 work. Hz table MIDI 24-48 with FL labels and harmonics, key-root picker, tuning by the tail, pitched vs sample-relative mode, long vs short, slide settings/recipes/budgets, kick+808 layering, saturation chain, and 808 grids for trap, drill, plugg, rage, phonk (drift, Brazilian, Memphis) and boom bap.
- `references/bassline-styles.md`: open when writing a non-808 bass, or for detailed note-choice rules (approach types, walking, pedals, 3rds). Has the 15 genre styles with grids, worked MIDI in a key, lengths, velocities and sound.
- `references/kick-bass-low-end.md`: open when deciding sub ownership, K1/K2/K3, kick tuning, sidechain basics, frequency/mono/phone-translation rules, or designing a bass patch (sub, pluck, layered, reese, wobble, synth 808, log drum, upright; 3x Osc quick bass).
- `references/bass-midi-delivery.md`: open every time a bass/808 MIDI file is written. Tested `make_bass.py` template (grid parser, slide overlaps, clamping, validation, sample/pitched modes), swing ticks, pre-delivery checklist, user message template.

## Related skills

- `music-theory-core`: MIDI/FL octave mapping, Hz math, scales, genre parameter cards, overall beat workflow.
- `music-chords-voicing`: the progression the bass follows; slash chords; keeping voicings above the bass.
- `music-drums-groove`: the kick pattern the bass is written against; swing values; hat and fill grids.
- `music-melody-hooks`: leads, counter-melodies, phonk cowbell lines (the 808 must not fight the hook's rhythm).
- `music-arrangement`: when the 808 drops out, builds and drops, register slotting across parts.
- `music-mix-master`: sidechain, EQ, saturation/clipping, loudness, and applying levels through the MCP mixer tools.
