---
name: music-drums-groove
description: Programs drums that groove in FL Studio - kick, snare, clap, hi-hat, open hat, percussion and cymbal patterns as 16-step grids plus FL step-sequencer binary strings, with BPM and swing for trap, UK/NY drill, boom bap, lo-fi, R&B, pop, rock, funk, reggaeton/dembow, afrobeats, amapiano, house, deep/tech house, techno, trance, DnB, dubstep, UK garage/2-step, jersey club, phonk, plugg, rage, breakbeat, future bass, synthwave and hyperpop. Covers drum roles, interlock rules, velocity bands, ghost notes, swing (MPC/Linn vs FL swing knob), groove science, hi-hat rolls and triplets, fills, build-ups, drum layering/tuning, and delivery via fl_set_step_sequencer or drum MIDI files. Use whenever the user wants to make a beat, program or write drums, a drum pattern or loop, add hi-hat rolls, bounce or swing, fix a stiff, robotic or boring groove, add a fill or build-up, or says "make a trap/drill/house beat" - even if only one drum is mentioned.
---

# Drums and groove

Write drum parts that make people move: a clear low-end pulse, a backbeat anchor, medium syncopation, a dense but quiet subdivision layer, and space. This skill turns a genre or vibe into per-channel 16-step grids, velocities, swing and fills, then delivers them to FL Studio — on/off rows straight into the Channel Rack with `fl_set_step_sequencer`, and anything with velocity shape, rolls, triplets or microtiming as one MIDI file per drum channel (notes at MIDI 60). Notation and conventions follow the family spec: steps 1–16, beats on 1/5/9/13, `X` accent 110–127, `x` normal 85–105, `g` ghost 35–60, `o` open hat, `r` roll start, `.` rest.

## Core principles (and why)

1. **Anchor, then syncopate.** Groove peaks at *medium* syncopation (inverted U; Witek 2014; Senn 2018). Keep 2–4 anchors (kick on 1, snare on the backbeat or beat 3) and move 1–3 hits per bar off the strong positions. All-on-grid is stiff; no anchors loses the meter.
2. **Low end carries the beat.** Low tones drive beat tracking in the brain and timing perception (Lenc 2018; Hove 2014). Keep kick and bass uncluttered and exactly on time; put complexity in the hats, ghosts and percussion.
3. **Density lives in the top.** Event density raises groove (Senn 2018; Madison). 16th hats/shakers at low velocity add drive without mud.
4. **Quantize by default; swing is a ratio, not jitter.** Quantized beats are never penalized; exaggerated microtiming lowers groove (Davies 2013; Senn 2016). Humanize only systematically, within ±10–20 ms (snare late = laid back, hats early = push). Vary velocity more than timing.
5. **Interlock, don't stack.** Each drum owns a job and a slot; parts trade positions (call and response) and leave space. Drill wants "more silence than notes"; boom bap "strips back".
6. **Familiar template first.** Familiar patterns earn a groove bonus (Senn 2018): start from the genre grid, then personalize one layer.

## Rhythm fundamentals (compact)

- **Backbeat:** snare/clap on beats 2 and 4 = steps 5, 13. **Half-time:** snare on beat 3 only = step 9; 140 BPM feels like 70 (trap, drill, dubstep, future bass, plugg, rage, phonk).
- **Four-on-the-floor:** kick on 1, 5, 9, 13 (house, techno, trance, amapiano, reggaeton, dance-pop).
- **Tresillo 3+3+2:** half-bar steps 1, 4, 7 (drill hats, phonk cowbell); displaced 4, 7, 12, 15 (dembow snare); full bar 1, 7, 13; extended 1, 5, 9, 12, 15 (Jersey club kick).
- **Syncopation:** emphasis on weak positions — "e"/"a" steps (2, 4, 6, 8…) and "&" steps (3, 7, 11, 15) — especially when the next strong beat is left empty.
- **Polyrhythm:** 3 against 4 — 8th triplets over 8th hats, or a 3-step figure (1, 4, 7, 10, 13, 16) over a quarter kick. **Polymeter:** a 12-step perc loop against 16 steps realigns every 3 bars (set channel length in FL's UI; one layer max).
- Triplets, 32nds and 64ths do not fit the 16-step grid: MIDI only. Ticks at PPQ 96: 1/16 = 24, 1/16-triplet = 16, 1/32 = 12, 1/8-triplet = 32.

## Drum roles

| Element | Job | Default slot |
|---|---|---|
| Kick | Pulse and low-end foundation; in trap/drill the 808 doubles it | Step 1 + genre placements; 808/bass starts on kick steps |
| Snare / clap | Backbeat anchor | 5 and 13, or 9 (half-time) |
| Ghost snare / rim | In-between motion | e/a steps around the backbeat (8, 10, 16) at 35–60 |
| Closed hat / shaker | Timekeeping, subdivision energy | 8ths, 16ths or 3+3+2 groups |
| Open hat | Offbeat lift | "&" steps (3, 7, 11, 15); choked by the closed hat |
| Percussion (clave, conga, rim, cowbell, log drum) | Conversation, answers, genre signature | Syncopated slots between kick and snare |
| Crash / ride | Section markers / chorus energy | Crash on step 1 of new 8/16-bar sections; ride on 8ths/offbeats in peaks |

## Interlock rules

1. **No kick and snare on the same step** unless it is a deliberate accent (Jersey club stacks on 9 and 12 on purpose).
2. **Kick just before the snare pushes; just after bounces.** Snare on 5: kick on 4 pushes, 6 bounces. Snare on 9: kick on 8 pushes, 10/11 bounces. Snare on 13: 12 pushes, 14 bounces.
3. **Hats that coincide with kick/snare drop 10–20 in velocity**; in kick-heavy styles delete hats that duplicate kick transients.
4. **An answer element closes each 2-bar phrase:** open hat, rim, perc hit or vocal chop near the end of bar 2 (e.g. bar-2 step 11 or 15).
5. **3–4 rhythmic layers carry the groove.** Extra layers must differ in register (low/mid/high) and subdivision (quarters vs 8ths vs 16ths) and sit lower in velocity (afrobeats/amapiano percussion is the model).
6. **Bass/808 locks to the kick:** 808 notes start on or just after kick steps; sidechain the 808 from the kick (see `music-bass-808`, `music-mix-master`).

## Procedure: programming a beat

1. **Pick genre, BPM, swing** from the genre index below (open the genre grid file for the full pattern). Set tempo with `fl_set_tempo(bpm)`.
2. **List channels** with `fl_list_channels`; map kick, snare/clap, closed hat, open hat, perc, crash to channel indexes. If a needed sound is missing, ask the user to load one (and suggest the kit from the "Kit choice" table in `hats-fills-builds.md`).
3. **Kick + snare skeleton (2 bars).** Start from the genre grid. Check the syncopation budget: 2–4 anchors, 1–3 off-grid hits per bar. Make bar 2 differ from bar 1 slightly (kick displacement, drill snare shift, pickup).
4. **Hats/shakers.** Choose density by energy (8ths relaxed, 16ths driving, 3+3+2 bouncy). Apply an accent pattern (on-beat 110, "&" 95, e/a 60–70). Remove closed hats under open hats.
5. **Ghosts, rolls, percussion.** Add 1–3 ghost snares, one roll per 1–2 bars (trap/drill), one answer element per 2 bars. Count layers (≤4 carrying).
6. **Swing and feel.** Straight for trap/drill/EDM; genre swing for house, garage, boom bap, lo-fi, R&B. Bake swing into MIDI ticks; for step-sequencer rows use FL's swing knob (both levels > 0).
7. **Phrase variation.** Bar 4 small variation, bar 8 bigger fill, bar 16 full fill + crash. Mark hooks with a kick/808 dropout or build (see `hats-fills-builds.md`).
8. **Deliver** (see FL Studio delivery): step-sequencer rows first, MIDI files for the rest. Set channel volume/pan/pitch for balance and tuning.
9. **Verify:** play (`fl_play`), check the checklist below, adjust one layer at a time.

## Genre index

BPM default in brackets. Swing on the MPC/Linn scale (50 = straight, 66 = triplet). s = sourced, c = convention, la = low-authority source. Full grids, velocities and binary strings: **HG** = `references/genre-grids-hiphop-global.md`, **EP** = `references/genre-grids-electronic-pop.md`.

| Genre | BPM | Swing | Kick steps | Snare/clap steps | Signature | File |
|---|---|---|---|---|---|---|
| Trap | 130–160 (140) s | 50 c | 1, 8, 11 / 1, 4, 11, 15 | 9 | 8th hats + 1/32 and 1/24 rolls | HG |
| UK drill | 138–151 (142) s | 50–55 c | b1 1, 8 / b2 1, 4, 7, 15 s | b1 9 / b2 13 s | 3+3+2 hats 1, 4, 7, 9, 12, 15 s | HG |
| NY drill | 140–150 (142) s | 50 s | b1 1, 7, 13 / b2 3, 9 | b1 9 / b2 13 | triplet hat bars, hard 808 glides | HG |
| Boom bap | 85–95 (90) s | 57 K/S 8ths, 74 hats 16ths s | 1, 7, 9 / 1, 7, 11, (15) s | 5, 13 | swung 16th hats, constant kick vel | HG |
| Lo-fi | 70–90 (78) s | ~58–64 (FL 20–30) s | 1, 7, 11 | 5, 13 late | 8th hats 89/51 s | HG |
| R&B | 60–90 (75) s | ~55–58 (FL 15–20) s | 1, 11, (16) | 5, 13 + rim ghosts | 16th hats, open hat step 7 s | HG |
| Plugg / pluggnb | 130–150 (140) s | 50 c | 1, 11, 15 | 9 | simple 8ths, soft clap | HG |
| Rage | 140–170 (155) la | 50 c | 1, 11 | 9 | simple drums, distorted 808 | HG |
| Phonk (drift) | 130–160 (145) la | 50 c | 1, 7, 9, 15 | 5, 13 | 808 cowbell tresillo | HG |
| Reggaeton | 85–100 (94) s | 50–54 c | 1, 5, 9, 13 | 4, 7, 12, 15 s | dembow 3+3+2 | HG |
| Afrobeats | 95–115 (108) s | 52–56 c | 1, 7, 9 (+15 alt bars) s | rim 5, 13 s | 16th shaker, clave, open hat 7 | HG |
| Amapiano | 108–115 (112) s | 54–58 c | 1, 5, 9, 13 s | rim 5, 13 | log drum, conga 5, 8, 11, 13 s | HG |
| Jersey club | 130–140 (140) s | 50 s | 1, 5, 9, 12, 15 s | 9, 12 / 9, 11, 12 s | 5-kick run, bed squeak | HG |
| House | 120–125 (124) s | 55–60 s | 1, 5, 9, 13 | 5, 13 | offbeat open hat, tamb, rim | EP |
| Deep house | 110–125 (121) s | 55–62 c | 1, 5, 9, 13 | 5, 13 soft | shaker, no big builds | EP |
| Tech house | 123–130 (126) s | 55–65 s | 1, 5, 9, 13 | 5, 13 (+16 g) | hats 1st/2nd/4th 16th + offbeat open | EP |
| Techno | 120–150 (130); hard 145–160 s | 50–54 c; rolling 20% DAW s | 1, 5, 9, 13 | 5, 13 opt | 16th hats, rumble kick | EP |
| Trance | 125–150 (138) s | 50 c | 1, 5, 9, 13 | 5, 13 | open hat every offbeat s, snare-roll builds | EP |
| DnB | 160–180 (174) s | 52–55 hats c | 1, 11 s | 5, 13 s | ghost snares, chopped breaks | EP |
| Dubstep | 138–142 (140) s | 50 c | 1 | 9 | sparse half-time, sub carries pulse | EP |
| UK garage / 2-step | 122–134 (130) s | 60–69 s | 1, 11 / bar 2 skips beat 1 s | 5, 13 | swung rims, offbeat hats | EP |
| Future bass | 130–175 (150) s | 50 c | 1, 11 | 9 s | chord stabs, pumping, rolls | EP |
| Synthwave | 80–118 (100) s | 50 c | 1, 5, 9, 13 | 5, 13 gated | 16th hats, tom fills | EP |
| Pop | dance 118–124; mid 95–110 c | 50–54 c | 4-floor or 1, 9, 11 | 5, 13 | density changes by section | EP |
| Rock | 90–140 (120) c | 50 c | 1, 9, 11 | 5, 13 s | 8th hats, crash on sections | EP |
| Funk | 95–115 (105) c | 52–56 c | 1, 3, 11, 14 | 5, 13 + g 8, 10, 16 | 16th hats, ghost snares | EP |
| Breakbeat | 130–140 (135) s | 50–54 c | 1, 11 | 5, 13 + g 10, 16 | breaks layered | EP |
| Hyperpop | 140–170+; NI 205 s | 50 c | b1 1, 13 / b2 13, 15 s | 9 s | all vel 100, glitch rolls | EP |

## Velocity bands

| Element | MIDI velocity |
|---|---|
| Kick | 100–120 (boom bap: constant 115–125) |
| Kick ghost / pickup | 65–90 |
| Snare / clap | 105–127 |
| Ghost snare | 30–60 (drill 40–50% ≈ 51–64) |
| 16th hats: on-beat / "&" / "e","a" | ≈110 / ≈95 / 60–70 |
| Open hat | 80–100 |
| Shaker | 50–80, accent on the offbeat |
| Crash | 100–120, step 1 of a new section |
| Rolls | ramp 60 → 110, or alternate 110/70 |

FL shows velocity in %: MIDI ≈ % × 1.27. Keep kicks and main snares near-constant; vary hats ±5–15 around the accent pattern.

## Swing quick rules

- MPC/Linn: 50% straight, 54% loosens without sounding swung, 57–62% hip-hop/house bounce, 66% triplet, up to ~70% useful (Linn). Delay of each even 16th = 48 × (S − 50)/100 ticks at PPQ 96 (S = 57 → 3 ticks, 62 → 6, 66 → 8).
- Swing hats/percussion most, kick least; boom bap per Attack: 57% (8ths) on kick/snare, 74% (16ths) on hats. Give drums and 808 the same swing.
- **FL Studio:** Channel Rack swing holds odd 16ths and delays even 16ths. Global Swing knob + per-channel swing (Channel settings > Misc > Time); **a channel swings only when BOTH are > 0.** The FL knob is not the MPC scale and has no verified mapping: start low (~15–30% FL) and match by ear. For MIDI deliveries bake swing into ticks instead.
- Details, sourced genre table and the full delay table: `references/groove-swing-science.md`.

## Hats, rolls and fills (summary)

- Energy ladder: none → 8ths → 3+3+2 → 16ths → 16ths + rolls. Change density at section boundaries.
- Rolls every 1–2 bars on beat 4 (into the next bar) or beat 2 (into a beat-3 snare): 1/32 = 8 per beat (12 ticks), 1/24 = 16th triplets, 6 per beat (16 ticks), 8th triplets 3 per beat (32 ticks). Pitched roll = rising MIDI note numbers (+1 to +12 semitones).
- Open hat on offbeats, closed hat removed on that step, both in one cut group (FL Channel settings > Misc "Cut"/"Cut by").
- Fill schedule: bar 4 small variation, bar 8 bigger fill, bar 16 full fill + crash on the next step 1; never the same fill at every boundary.
- EDM build: snare quarters (bars 1–4) → 8ths (5–6) → 16ths (7) → 32nd/triplet rolls with beat 4 empty (8); velocity 60 → 120. Hip hop: drop kick+808 for the last half bar before the hook.
- Grids, roll tables and build stages: `references/hats-fills-builds.md`.

## FL Studio delivery

| Content | Route |
|---|---|
| On/off rows at one velocity (kick, main snare, plain hats, open hat, crash) | `fl_set_step_sequencer(channel_index, "1000000100100000")` — 16 chars per bar, concatenate up to 64 chars (4 bars); writes into the selected pattern |
| Ghost notes, accent patterns, velocity ramps | MIDI file (step sequencer cannot set per-step velocity) |
| Rolls (1/32, 1/24), triplets, flams | MIDI file |
| Swing baked per element, late snare, early hats | MIDI file (ticks); or FL swing knob/graph-editor Shift by hand for step rows |
| Pitched rolls, cowbell/log-drum melodies | MIDI file with note numbers in key |
| Element balance, pan, kit tuning | `fl_set_channel_pitch_pan_vol(channel, volume 0–1, pan −1..1, pitch cents ±1200)` |

- **Binary strings:** each reference grid row ends with its exact FL string (non-`.` = `1`). A `g` or `r` cell becomes a full-velocity step if sent via the step sequencer — strip ghosts (set those chars to `0`) or deliver that row as MIDI.
- **MIDI files:** one .mid per drum channel, every drum note at **MIDI 60** (FL "C5", the sample's own pitch), PPQ 96, written with `mido` and run with `uv run --with mido --no-project python make_drums.py`. **No note may end past the last bar** or FL adds an extra bar. The user drags each .mid onto its channel. Tested template: `references/hats-fills-builds.md` §10 (pattern from `ny-drill-midi/make_midi.py`).
- **Piano-roll MCP tools** (`fl_add_notes` etc.) only queue notes and do not apply on FL 21 — never rely on them for drums.
- **Velocity workaround without MIDI:** clone a channel (user does it in FL), give the clone a lower volume (e.g. 0.4 vs 0.78) and put ghosts on the clone's step row.
- **Tuning:** pitch a kick/snare sample with the channel pitch (cents) to the root or fifth; 808 tuning is in `music-bass-808`.
- **If tools fail:** `fl_check_bridge_status`, loopMIDI port "FL MCP" running, FL Script output window, port 10.
- `fl_diagnose_mix` polls peaks and misses short one-shot drums — judge drum balance by ear or with the mixer meters.

Example (trap bar 1, from HG): kick `1000000100100000`, snare `0000000010000000`, open hat `0000001000000000` via step sequencer; hats (with the 1/32 roll) as `hihat.mid`.

## Quality checklist

- [ ] Kick on step 1 of most bars (drill bar 2 may skip it on purpose); snare on the genre's backbeat every bar.
- [ ] Syncopation budget: 2–4 anchors, 1–3 off-grid kick/snare hits per bar.
- [ ] No kick+snare on the same step unless intended; hats lowered or removed under kicks/snares/open hats.
- [ ] Bar 2 differs from bar 1; an answer element closes the 2-bar phrase; fills at bars 4/8/16 vary.
- [ ] ≤4 carrying layers; extras differ in register and subdivision.
- [ ] Velocities in band: ghosts 35–60, hats accented, kick/snare steady.
- [ ] Swing consistent per element and shared with the 808; no random timing beyond ±20 ms; kick on the grid.
- [ ] Every binary string is 16 chars per bar and matches its grid; MIDI notes at 60, nothing past the last bar.
- [ ] 808/bass starts on kick steps; kick and 808 tuned to the key.

**Common mistakes:** copying the same roll into every bar; 16th hats at one flat velocity; ghost notes sent through the step sequencer at full velocity; snare on 5/13 in a half-time genre (or on 9 in boom bap); open hat ringing over the next clap; crash every 4 bars; random humanize on the kick; stacking a long kick sub under a long 808; forgetting FL's channel swing needs the global knob > 0 too; four-on-the-floor kick in afrobeats (use 1 + "and" of 2).

## References

- `references/genre-grids-hiphop-global.md` — open when programming trap, UK/NY/Chicago drill, boom bap, lo-fi, R&B, plugg, rage, phonk, reggaeton/dembow, afrobeats, amapiano or Jersey club: full 2-bar grids, binary strings, velocities, rolls, sources.
- `references/genre-grids-electronic-pop.md` — open for house, deep/tech/afro house, techno (peak, rolling, hard), trance, DnB/Amen/jungle, dubstep/riddim, UK garage and 2-step, future bass, synthwave, pop, rock, funk, breakbeat, hyperpop.
- `references/groove-swing-science.md` — open when the groove feels stiff or wrong, when choosing swing or humanization numbers, or when the user asks why: rhythm fundamentals, study-by-study research, syncopation budget, ms/tick tables, swing formula and FL swing details, full velocity table.
- `references/hats-fills-builds.md` — open when writing hi-hats, rolls, fills, transitions, build-ups or drops, choosing/layering/tuning drum sounds, or writing the drum MIDI script (tested template in §10).

## Related skills

- `music-theory-core` — hub: tempo/grid math, genre parameter cards, overall FL delivery workflow and MIDI template.
- `music-bass-808` — kick–bass strategy, 808 notes, slides and tuning that lock to these drum grids.
- `music-arrangement` — section lengths, where fills/builds/drops go in the song, energy curves.
- `music-mix-master` — drum levels, EQ, sidechain 808 to kick, drum bus compression, saturation.
- `music-chords-voicing`, `music-melody-hooks` — harmony and melody over the beat (pair medium-syncopation drums with 7th-chord-level harmony).
