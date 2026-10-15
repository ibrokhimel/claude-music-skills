---
name: music-arrangement
description: Arranges music so parts fit together and loops become full songs. Use whenever the user wants to arrange a beat or song, turn a loop into a song, "make this 8-bar loop a full track", plan intro/verse/hook/chorus/drop/breakdown/outro, pick song structure or bar counts, fix instruments that clash or sound muddy/cluttered, decide which instruments play where, layer or double parts, build tension into a drop, add risers/builds/transitions, plan an energy curve, or stop a beat getting boring. Covers instrument roles (foundation, pad, rhythm, lead, fills), the 3-4 focal-element limit, frequency/register slotting, orchestration (octave doubling, layering, voicing across instruments), song-form templates (trap, drill, hip hop, pop, R&B, EDM, house, techno, DnB, lo-fi, afrobeats, amapiano, cinematic), bars-to-seconds math and the FL Studio playlist workflow. Trigger on "arrangement", "song structure", "how many bars", "build-up", "drop", "too busy".
---

# Music arrangement

Purpose: decide WHAT plays WHERE and WHEN. Inside one section, arrangement means every part has a role, a register and a prominence plane, so parts fit instead of masking each other. Across the song, it means a sequence of 4/8/16-bar sections whose element count and energy rise and fall on purpose, with builds and clearings placed so the peaks land. The usual production path is subtractive: build the fullest 8-bar section first, then derive every other section by muting, and add variation every 4/8 bars. In FL Studio the MCP bridge cannot place playlist clips, so Claude plans the arrangement, auditions it with mute/solo, and delivers either per-section patterns with a placement table or full-length MIDI per role.

## Core principles (with the why)

1. **Roles before notes.** Every part is one of five roles (Owsinski): foundation (drums + bass), pad (sustained harmony), rhythm (counter-motion: shakers, arps, strums), lead (vocal, hook, riff), fills (answers in the lead's gaps). Add texture/atmosphere as a background sub-role. Why: listeners hear functions, not tracks; two parts with the same role compete. **(sourced: Owsinski)**
2. **Three to four focal elements at once, never five.** The ear follows about three things. Several tracks playing one rhythm count as one element. Why: beyond that, attention fragments and the mix reads as clutter. **(sourced: Owsinski; "rule of three")**
3. **Three planes.** Foreground (louder, characteristic timbre, centred or prominent), middleground, background (quieter, filtered, wider, less active). A part that would be the fifth foreground element must replace one or move back. **(sourced: orchestration teaching; rule is convention)**
4. **Differ on at least one axis, ideally several.** Parts fit when they differ in register, rhythmic density, timbre, stereo position or plane. Masking is an arrangement problem first; EQ only partly fixes two parts in the same band doing the same rhythm. **(sourced: Sonarworks; Plomp & Levelt critical band)**
5. **One low-end owner.** Below about 100 Hz only one part leads at any moment (808/sub or bass), with the kick interlocked or ducked. Why: low fundamentals share critical bands and smear. **(convention, physically grounded)**
6. **Wide intervals low, close intervals high.** No full chords below MIDI 48 (C3, FL: C4); only root, octave or 5th there. **(sourced: Open Music Theory spacing; MIDI cut-off convention)**
7. **Busy needs sustained.** A busy part (16th hats, rolling arp, fast flow) needs sparse or sustained neighbours in the same register. Busy plus busy only works in different registers. **(convention)**
8. **Double for weight, but not constantly.** Octave/unison doubling makes a hook heavier without adding a focal element; constant doubling sounds grey. Double in choruses/drops, undouble in verses. **(sourced: Belkin)**
9. **Energy and tension are separate controls.** Energy = intensity and momentum (element count, low end, density, loudness). Tension = expectation of release (risers, rolls, filter sweeps, dominant harmony, removed kick). A drop needs high tension before it and a clearing before that. **(sourced: EDMProd)**
10. **Contrast makes peaks.** A drop/hook only hits if the section before it cleared space. Adjacent sections differ on at least two of six axes: element count, low-end presence, hat subdivision, register span, stereo width, lead type. **(sourced: Inspired by Beatz; six-axis rule is convention)**
11. **Change something every 8 bars, vary every 4.** Something enters, leaves or changes at each 8-bar boundary; a micro-variation marks each 4-bar end. No identical 8-bar block more than twice in a row. **(sourced: DJ phrasing, Attack Magazine; exact rule convention)**
12. **Repetition is the point; exact repetition is the risk.** Keep the hook identical, vary its context (layers, drums, register). Why: familiarity drives liking, but over-repetition lowers it (Gold 2019; Margulis). **(sourced)**

## Procedure Claude follows

Run these steps in order. Steps 1-4 happen before writing notes; steps 5-9 shape the song.

1. **Get the inputs.** Genre, BPM, key, target length or use (streaming single, DJ/club extended, beat for a rapper, cue). If missing, take defaults from the genre template in `references/song-form-templates.md` and the genre parameter card in `music-theory-core`.
2. **Inventory the parts and assign role + plane + register.** Make a table: part, role, plane, MIDI range, rhythmic density (sustained / medium / busy), stereo (centre / mid / wide). Use the register map below. Check: one low-end owner, at most 3-4 foreground items in the fullest section, every shared register has a density or timbre or stereo contrast.
3. **Fix clashes by arrangement, not EQ.** In order: move a part by an octave, change its rhythm (busy vs sustained), swap its timbre, move it in stereo, push it to background, or cut it. See `references/roles-and-frequency-slotting.md`.
4. **Build the fullest 8-bar section** (hook/chorus/drop) as separate patterns per role: kick, snare/clap, hats, perc, 808/bass, chords, lead, counter, FX. Drum grids come from `music-drums-groove`, chords from `music-chords-voicing`, melody from `music-melody-hooks`, bass from `music-bass-808`.
5. **Pick the form template and compute time.** Choose the section list and bar counts from the template, then compute seconds (bar seconds = 240 / BPM) and check targets: pop first chorus by about 40 s, EDM/streaming drop within 30-60 s, total length per use.
6. **Draw the energy curve (1-9 per section)** and mark where tension builds. Use the genre default curves below; each repeat of a section sits at or slightly above its previous instance.
7. **Derive sections by subtraction** with an element matrix (rows = sections, columns = roles, cells = plays / partial / out / variant). Intro 1-2 elements; verse drops the lead layer and simplifies hats; breakdown removes kick and bass; final hook adds one layer (octave double, extra perc, counter).
8. **Write variation and transitions.** Make B variants (hat rolls, 808 slides, chord inversion, melody tail). Place micro-variations every 4 bars, a change every 8, and a transition at every section boundary, the strongest one reserved for the biggest drop. See `references/energy-builds-transitions.md`.
9. **Deliver in FL Studio** (see delivery notes) and run the quality checklist.

## Defaults tables

### Role map for a modern beat (convention)

| Role | Typical parts | Register | Density | Plane | Stereo |
|---|---|---|---|---|---|
| Foundation | kick, snare/clap, 808/bass | sub to low-mid | medium | fore/middle | centre |
| Rhythm (counter) | hats, shakers, perc loops, arps, muted guitar | high / upper-mid | busy | middle/back | spread |
| Pad / harmony | pads, sustained keys, strings, chord stabs | low-mid to mid | sustained | back/middle | wide |
| Lead | vocal, topline, lead synth, main riff/sample | mid to upper-mid | medium | fore | centre |
| Fills / counter | answers, vocal chops, ear candy | octave away from lead | in lead's rests | middle | off-centre |
| Texture | vinyl, noise bed, field recording, reverb tails | full band, filtered | static | back | wide |

### Register map (derived from f = 440 x 2^((m - 69)/12))

| Zone | Fundamentals | MIDI (scientific) | FL label | Occupants |
|---|---|---|---|---|
| Sub | 30-60 Hz | 23-34 (B0-A#1) | B1-A#2 | 808/sub fundamentals, kick body |
| Bass | 60-125 Hz | 35-47 (B1-B2) | B2-B3 | basslines, upper 808 notes, kick punch |
| Low-mid | 130-250 Hz | 48-59 (C3-B3) | C4-B4 | chord roots and 5ths, piano left hand |
| Mid | 260 Hz-1 kHz | 60-83 (C4-B5) | C5-B6 | pads, chords, vocals, most leads |
| Upper-mid | 1-4 kHz | 84-107 (C6-B7) | C7-B8 | bell tops, plucks, arps, presence harmonics |
| High | 4 kHz+ | harmonics and noise | - | hats, shakers, cymbals, air |

Slot defaults (convention): bass/808 MIDI 28-47 (E1-B2, FL: E2-B3); chords/pads MIDI 48-76 (C3-E5, FL: C4-E6); lead MIDI 60-84 (C4-C6, FL: C5-C7) above the chord bed or contrasting in timbre; counter-melody an octave away from the lead, in its rests.

### Song-form quick picks (bars at project tempo)

| Genre (default BPM) | Form | Total |
|---|---|---|
| Trap / rap beat (140) | Intro 8, Hook 8, Verse 16, Hook 8, Verse 16, Bridge 8, Hook 8, Outro 8 | 80 bars, ~2:17 |
| Drill (142) | Intro 8, Hook 8, Verse 16, Hook 8, Verse 16, Bridge 8, Hook 8, Outro 8 **(sourced: Beatstorapon)** | 80 bars, ~2:15 |
| Boom bap / hip hop (90) | Intro 4-8, V 16, H 8, V 16, H 8, V 16, H 8, Outro 4-8 **(sourced: HipHopMakers)** | ~88 bars, ~3:55 |
| Pop (115) | Intro 4, V 8, Pre 8, Ch 8, Post 4, V 8, Pre 8, Ch 8, Post 4, Bridge 8, Final Ch 16, Outro 4 (first chorus at bar 21 = 41.7 s) | 88 bars, ~3:04 |
| R&B (80) | Intro 4, V 8, Pre 4, H 8, V 8, Pre 4, H 8, Bridge 8, H 8, H 8, Outro 4 (V 16 at faster tempos) | 72 bars, ~3:36 |
| EDM radio (128) | Intro 16, Break 16, Build 8, Drop 16, Breakdown 16, Build 8, Drop 2 16, Outro 16 **(sourced ranges)** | 112 bars, 3:30 |
| House/tech house club (125) | Intro 32, Groove 32, Breakdown 16, Build 8, Drop 32, Groove 16-32, Outro 32 | 168-184 bars, ~5:20-5:55 |
| DnB (174) | Intro 16-32, Build 8, Drop 1 32, Breakdown 16, Build 8, Drop 2 32, Outro 16-32 **(sourced)** | 128-160 bars, ~2:57-3:41 |
| Lo-fi (85) | Intro 4-8, A 16, B 8-16, A 16, Outro 4-8 (sourced range 64-96 bars) | 48-64 bars = 2:15-3:00 |
| Cinematic trailer | Act 1 sparse, Act 2 ostinato build, silence, Act 3 full, button **(sourced)** | 2:00-2:30 |

Full tables, more genres (afrobeats, amapiano, jersey club, trance, techno, dubstep, future bass, UKG, synthwave) and element matrices: `references/song-form-templates.md`.

### Default energy curves, 1-9 (convention)

| Genre | Curve |
|---|---|
| Pop | Intro 3, V1 4, Pre 5, Ch 7, V2 5, Pre 6, Ch 8, Bridge 4-5, Final Ch 9, Outro 3 |
| EDM | Intro 3, Break 4, Build 5->7, Drop 9, Breakdown 3, Build 5->8, Drop 2 9, Outro 3 |
| Trap | Intro 3, Hook 8, Verse 6, Hook 8, Verse 6-7, Bridge 4, Hook 9, Outro 3 |

### Bars to seconds

`seconds = bars x 240 / BPM`; `bars = seconds x BPM / 240`. 8 bars: 21.3 s at 90, 16.0 s at 120, 15.0 s at 128, 13.7 s at 140, 11.0 s at 174. 30 s = 11.2 bars at 90, 15 at 120, 17.5 at 140. Full table in `references/song-form-templates.md`.

**Half-time caution (derived, uncertain):** at 130-160 BPM with a half-time feel (trap, drill), a rapper's "bar" can mean one FL bar or one felt half-time bar (= 2 FL bars). Templates here count FL bars. Check seconds: a 16-FL-bar verse at 140 BPM is 27 s; if the artist wants a ~50 s verse, use 32 FL bars.

### Builds in one line each (details in `references/energy-builds-transitions.md`)

- 8-bar build: snare/clap quarters (bars 1-4), 8ths (5-6), 16ths (7), 32nds or 16th triplets (8), velocity ramp 60->120. Roll programming: `music-drums-groove`.
- Under it: white-noise riser over all 8 bars, pitch riser 5-24 st (12 default), high-pass sweep on the music bus.
- Remove kick and/or bass for the last 1-2 bars (or the whole build); end with half a beat to one bar of silence, or a vocal pickup.
- Land: crash + sub/808 hit + full drums on beat 1. Use a reverse crash ending just before a downbeat for smaller boundaries.

## FL Studio delivery notes

- **The MCP bridge cannot create, move or place playlist clips, markers or automation.** Never claim to have arranged the playlist. Claude can: set tempo, write step rows into the selected pattern (`fl_set_step_sequencer`, up to 64 steps = 4 bars), set channel/mixer volume, pan and routing, mute/solo for auditioning, play/stop, switch pattern/song loop mode.
- **Audition sections with mute/solo before delivering.** Route each role to its own mixer track (`fl_assign_channel_to_mixer`, `fl_set_track_name_color`), loop the fullest pattern (`fl_set_loop_mode`, `fl_play`), then mute roles with `fl_mute_track` / `fl_mute_channel` to preview "verse = no lead, simpler hats" or "breakdown = no kick/808". Use `fl_solo_track` to check one low-end owner. Unmute everything when done.
- **Delivery option A: patterns + placement table (editable, recommended).** Write one MIDI file per role per variant (e.g. `hats_A.mid`, `hats_B_rolls.mid`, `808_A.mid`, `808_B_slides.mid`) with mido, 8 bars each. Give the user a playlist table: one playlist track per role, which pattern goes at which bar, plus time markers per section.
- **Delivery option B: full-length MIDI per role (fastest).** Write one song-length .mid per role with the arrangement already applied (sections where the role is out simply have no notes). The user drags each into its channel and places each pattern once at bar 1. Script: `references/loop-to-song-workflow.md`.
- MIDI rules from the family: PPQ 96, 1/16 = 24 ticks; drums at MIDI 60 (FL "C5"); no note may end past the last bar; run with `uv run --with mido --no-project python make_midi.py`. Pitched-note tools (`fl_add_notes`, etc.) do not apply notes on FL 21.
- **Describe** markers, clip placement, automation clips (filter sweeps, volume swells) and FX one-shots (riser, reverse crash) as numbered user steps with exact bar numbers. Mixer volume/pan can be set directly; plugin knobs cannot.
- Bar numbers in FL's playlist start at 1. Section start bar = 1 + sum of previous section lengths. Always print the bar map: `Intro 1-8 | Hook 9-16 | Verse 17-32 | ...`.

## Output format for an arrangement plan

Always hand the user (and yourself) these four blocks, in this order:

1. **Bar map with times** (from the template and `240 / BPM`):
   ```
   140 BPM, 1 bar = 1.71 s
   Intro   1-8    0:00   energy 3
   Hook 1  9-16   0:13.7 energy 8
   Verse 1 17-32  0:27.4 energy 6
   ...
   End     80     2:17
   ```
2. **Role table**: part, role, plane, MIDI range (with FL label), density, stereo.
3. **Element matrix**: sections x roles, cells `X` plays, `~` partial/filtered, `-` out, or a variant name (`hats_B`).
4. **Transition list** with exact bars: `bar 8: riser ends on 9.1 | bar 32 beat 4: kick+808 drop-out | bar 64: silence beat 4, impact on 65.1`.

Then state what Claude applied through MCP (tempo, routing, mutes) and what the user must do in the playlist.

## Quality checklist / common mistakes

- [ ] Every part has a role, plane, MIDI range and density written down.
- [ ] Fullest section: 3-4 focal elements, one low-end owner, no chord tones below MIDI 48 except root/5th/octave.
- [ ] Every shared register differs in density, timbre or stereo.
- [ ] Section lengths are 4/8/16-bar multiples unless an odd length is a deliberate effect.
- [ ] Time targets met (first chorus / first drop timing, total length) and the bar map printed.
- [ ] Energy curve drawn; adjacent sections differ on 2+ of the six axes; final hook/drop is at least as full as earlier ones and not identical to them.
- [ ] Every 8-bar boundary has an entry, exit or change; every 4-bar end a micro-variation; no 8-bar block repeats more than twice in a row.
- [ ] A clearing (breakdown, drop-out, silence) precedes each drop/hook; the strongest transition is saved for the biggest moment.
- [ ] Intro/outro fit the use: DJ tracks start and end with drums only; beats for rappers start with something recognisable within 4-8 bars.

Common mistakes: everything playing all the time (no headroom to escalate); a second drop identical to the first; the same fill at every boundary; doubling the lead everywhere; two busy parts in one register; pads and 808 both carrying sub; a 4-bar loop repeated for 3 minutes with no B variant; claiming the MCP placed clips.

## References

- `references/roles-and-frequency-slotting.md`: open when assigning roles/planes, diagnosing "muddy", "cluttered", "parts clash" or "the lead gets lost", choosing octaves for parts, layering/doubling, voicing chords across instruments, stereo placement, texture types. Contains the instrument frequency table, full register map, slotting rules, masking fixes and orchestration principles.
- `references/song-form-templates.md`: open when choosing a structure or bar counts for a specific genre, converting bars to seconds, or building an element matrix (which roles play in which section). Contains per-genre templates, trap/EDM/pop/house matrices, the full bars-to-seconds table and the pop timing data.
- `references/energy-builds-transitions.md`: open when planning energy curves, writing a build-up, drop, breakdown, riser, reverse crash, filter sweep or silence gap, or when the song "feels flat" or "the drop doesn't hit". Contains energy/tension theory, per-genre curves, build recipes, transition menu and variation schedule.
- `references/loop-to-song-workflow.md`: open when the user has a loop and wants a full song, or when delivering an arrangement into FL Studio. Contains the subtractive workflow, B-variant list, FL playlist steps for the user, MCP audition procedure and the mido script for per-section / full-length MIDI.

## Related skills

- `music-theory-core`: hub; MIDI/FL octave mapping, tempo math, genre parameter cards, FL delivery basics.
- `music-drums-groove`: drum grids, fills, roll programming, the 4/8/16 fill schedule at drum level.
- `music-bass-808`: low-end owner choice, kick-808 strategy, 808 slides for B variants.
- `music-chords-voicing`: progressions and voicings that the pad/keys roles play; chord inversions for B variants.
- `music-melody-hooks`: hooks, counter-melodies, call and response for the lead and fills roles.
- `music-mix-master`: EQ lanes, sidechain, panning and reverb that finish what arrangement slotting starts.
