---
name: music-theory-core
description: Hub and router for making music with Claude, especially in FL Studio. Use FIRST whenever the user asks to make, write, compose or produce a beat, song, track, loop, instrumental, type beat, melody or idea in any genre ("make me a trap beat", "drill beat in FL", "write a song", "lo-fi loop", "afrobeats", "house track", "DnB", "cinematic"), or asks music theory: notes, MIDI numbers, FL Studio octave names, Hz, intervals, scales, modes, keys, circle of fifths, chord spellings, diatonic chords, BPM, bars to seconds, grid, ticks, swing. Holds ~40 genre parameter cards, the default beat-from-scratch workflow that routes to music-drums-groove, music-bass-808, music-chords-voicing, music-melody-hooks, music-arrangement and music-mix-master, the attention/surprise/complexity budgets, the science of why music sounds good, and the FL Studio delivery workflow (fl-studio-mcp tools, mido MIDI-file template, bridge fixes).
---

# Music theory core (hub)

This skill is the entry point of a 7-skill family that composes and produces music in the user's FL Studio 21. It owns the deterministic layer (pitch, interval, scale, chord, key and tempo math), the genre parameter cards, the "budgets" that keep a track musical, the science behind those budgets, and the FL Studio delivery workflow. For each production step it routes to the sibling skill that holds the detail. Load it first for any music request, pick a genre card, then follow the workflow below and open sibling skills as each step comes up.

## Core principles (and why)

1. **MIDI numbers are the only unambiguous pitch reference.** C4 = 60; FL Studio labels MIDI 60 "C5" (FL octave = scientific + 1). Always write "MIDI 48 (C3, FL: C4)". Why: every DAW names octaves differently, and one-octave errors ruin 808s and voicings.
2. **Genres are parameter vectors over the same theory.** Tempo band, snare placement (2&4 vs half-time 3), swing, the one sub owner, chord vocabulary and section lengths separate genres more than scales do. Why: it makes genre choice a lookup, not guesswork.
3. **Budgets beat rules.** Spend attention (3–4 focal elements, one sub owner), surprise (one per predictable context) and complexity (medium syncopation × medium harmony) deliberately. Why: pleasure peaks at intermediate predictability (Cheung 2019, Gold 2019, Witek 2014).
4. **Familiar template + one twist.** Start from the genre-standard groove and form, then add one distinctive element. Why: familiarity raises groove ratings (Senn 2018), and earworms pair common contours with one unusual interval (Jakubowski 2017).
5. **Deterministic core, tunable genre layer.** Theory tables are **(derived)** and safe to hard-code; genre numbers are mostly **(convention)** and get checked by ear. Say which is which.
6. **On FL 21, notes travel as MIDI files.** MCP tools set tempo, simple step rows and the mixer; anything with pitch, per-note velocity, rolls, slides or exact timing is written with the mido template and dragged in by the user.

## Routing table

| Request or sub-task | Skill |
|---|---|
| "Make a beat/track/song", genre choice, tempo/key, theory lookups, FL delivery, why-it-works questions | `music-theory-core` (this) |
| Drum patterns, 16-step grids, hi-hat rolls, swing, ghost notes, fills, groove, "make the drums bounce" | `music-drums-groove` |
| 808s, basslines, kick–bass relationship, 808 tuning/glides/slides, sub, "808 not hitting" | `music-bass-808` |
| Chord progressions, voicings, voice leading, "make the chords sound expensive", cadences, borrowed chords, harmonic rhythm | `music-chords-voicing` |
| Melody, topline, hook, motif, counter-melody, bells/lead lines, "make it catchy", earworm | `music-melody-hooks` |
| Song structure, intro/verse/hook/drop/breakdown, loop-to-song, builds, energy curve, instrument roles, "too busy/muddy" (arrangement cause) | `music-arrangement` |
| Mixing, mastering, levels, EQ, compression, sidechain, reverb/delay, loudness, LUFS, FL mixer setup | `music-mix-master` |

A single-part request ("give me a drill hi-hat pattern") goes straight to that skill, but still take tempo, key and swing from this skill's genre card.

## Default workflow: make a beat or track from scratch

Follow these steps in order. Don't ask questions the card can answer; ask only if the genre or vibe is genuinely unclear (one short question, with a default offered).

1. **Parse the brief.** Extract genre, mood words, reference artists/tracks, BPM or key if given, vocal or instrumental, length. Map reference artists to a genre card.
2. **Pick the genre card** (quick cards below; full set in `references/genre-cards.md`). If a mood is given, apply the emotion override (genre-cards §5).
3. **Set tempo and key.** BPM = card default unless specified. Key: minor-key 808 genres → choose a tonic that puts the 808 root in MIDI 28–33 (F, F#, G, A minor are practical) or match the 808 sample's pitch; otherwise use the card's mode. Write the scale's MIDI pitch classes down once (theory quick reference below).
4. **Fill the budget sheet** (next section): focal elements, sub owner, where the one surprise goes, complexity split between drums and harmony.
5. **Drums → `music-drums-groove`.** Kick/snare skeleton from the genre grid, then hats/shakers, then ghosts, rolls, velocity bands, fills on the 4/8/16-bar schedule. Apply swing as an MPC value.
6. **Bass / 808 → `music-bass-808`.** Choose the kick–bass strategy (lock, gaps or hybrid), roots on chord changes, glides sparingly, register MIDI 24–40 for 808s.
7. **Chords → `music-chords-voicing`.** Progression from the card's vocabulary, nearest-voicing with chords mostly ≥ MIDI 48 when an 808 owns the sub, genre harmonic rhythm and comping.
8. **Melody → `music-melody-hooks`.** Motif from chord tones on strong beats, mostly steps, one climax, one distinctive interval or rhythm; leave space for a vocalist in rap beats.
9. **Arrangement → `music-arrangement`.** Turn the loop into the card's section lengths by subtraction; plan builds, drops and the energy curve; vary each hook return.
10. **Mix → `music-mix-master`.** Gain staging, sub-owner sidechain, EQ lanes, levels/pans via MCP, loudness target.
11. **Deliver** (FL Studio delivery below) and report to the user what was applied and what to drag where.

Variants:
- **"Write a song" (vocal/topline-led):** card → tempo/key → chords → melody/hook → drums → bass → arrangement → mix. The hook leads, so write it before the beat gets busy.
- **"Make a loop":** steps 1–8 only, 4 or 8 bars, plus delivery.
- **Existing project:** `fl_get_project_info` + `fl_list_channels` first; keep the user's tempo, key and sounds.

## The budgets

### Attention budget
- At most **3–4 focal (foreground) elements** at once; three often works best (Owsinski; "rule of three"). Several drum tracks playing one groove count as one element.
- **Exactly one sub owner** below ~100 Hz: the 808 OR the bass OR the kick (hard techno). Other parts are high-passed or kept above MIDI ~48.
- Every new part gets a **role** (foundation, pad, rhythm, lead, fill) and a **plane** (fore/middle/background) before notes are written. A would-be fifth focal element replaces one or gets pushed back (lower, filtered, wider, less active).
- In rap beats the vocal is a focal element: leave the melody sparse in verses.

### Surprise budget
- **One surprise per predictable context**: after 4–8 bars (or 3 loops) of established pattern, spend one twist — a borrowed chord (iv, bVI, bVII), a dropped beat, a fill, a new sound, a leap.
- After an ambiguous or wandering passage, **land on the expected** (tonic, kick on 1).
- **Never stack surprise on surprise.** Save the biggest twist for the last hook or the second drop.
- Surprise is genre-relative: measure it against the card's normal vocabulary.

### Complexity budget
- **Medium syncopation** groove best: anchors stay (kick on 1, backbeat on 2&4 or 3); syncopation lives in hats, ghosts, bass and secondary kicks.
- **Medium harmony** with busy drums: 7th-chord level, not dense altered chords. Sparse drums can carry richer harmony.
- Raise one dimension, lower another. Dense subdivisions (16th hats/shakers) plus clear anchors.
- Repeat 2- or 4-bar units 2–4 times, then vary the surroundings, not the hook.

Budget sheet (fill before writing notes):
```
Genre/BPM/key/swing: ...
Sub owner: 808 | bass | kick      Focal elements (≤4): drums, 808, lead, [vocal]
Surprise plan: bar __ (what)       Complexity: drums = med-high, harmony = med
Section plan: intro _, hook _, verse _ ...
```

## Theory quick reference

Full tables (Hz grid, all keys, compound intervals, modal chords, swing math): `references/theory-tables.md`.

**Pitch.** `MIDI = 12 × (sci_octave + 1) + pc` = `12 × FL_octave + pc`. pc: C0 C#1 D2 D#3 E4 F5 F#6 G7 G#8 A9 A#10 B11. `f = 440 × 2^((m − 69)/12)`.

| MIDI | Sci (FL) | Hz | Typical occupant |
|---|---|---|---|
| 24 | C1 (C2) | 32.7 | 808 floor |
| 28 | E1 (E2) | 41.2 | deep 808, bass open E |
| 33 | A1 (A2) | 55.0 | 808 sweet spot |
| 36 | C2 (C3) | 65.4 | bass, upper 808 |
| 48 | C3 (C4) | 130.8 | floor for chord 3rds over an 808 |
| 60 | C4 (C5) | 261.6 | harmony core; drum samples' own pitch in FL Sampler |
| 69 | A4 (A5) | 440.0 | lead / topline |
| 72–84 | C5–C6 (C6–C7) | 523–1047 | bells, arps, upper leads |

**Intervals (semitones).** 1 m2 harsh/b2 menace · 2 M2 air · 3 m3 minor · 4 M3 major · 5 P4 open · 6 TT unstable · 7 P5 stable · 8 m6 bittersweet (b6) · 9 M6 warm (Dorian) · 10 m7 bluesy · 11 M7 lush/harsh · 12 octave · 14 9th · 17 11th · 21 13th.

**Scales.**

| Scale | Formula | Colour note | Use |
|---|---|---|---|
| Major (Ionian) | 0 2 4 5 7 9 11 | 4, 7 | pop, house, afrobeats |
| Natural minor (Aeolian) | 0 2 3 5 7 8 10 | b6 | trap, trance, synthwave |
| Harmonic minor | 0 2 3 5 7 8 11 | natural 7 | trap/drill bells, V–i |
| Dorian | 0 2 3 5 7 9 10 | M6 | lo-fi, neo-soul, deep house |
| Phrygian | 0 1 3 5 7 8 10 | b2 | trap, drill, phonk |
| Mixolydian | 0 2 4 5 7 9 10 | b7 | funk, gospel |
| Lydian | 0 2 4 6 7 9 11 | #4 | cinematic, future bass |
| Phrygian dominant | 0 1 4 5 7 8 10 | b2 + M3 | "eastern" leads |
| Minor / major pentatonic | 0 3 5 7 10 / 0 2 4 7 9 | no half steps | safe hooks |

Brightness ladder: Lydian → Ionian → Mixolydian → Dorian → Aeolian → Phrygian → Locrian (each flattens one note).

**Chords.** maj 0 4 7 · m 0 3 7 · dim 0 3 6 · aug 0 4 8 · sus2 0 2 7 · sus4 0 5 7 · 7 0 4 7 10 · maj7 0 4 7 11 · m7 0 3 7 10 · m7b5 0 3 6 10 · dim7 0 3 6 9 · add9 0 4 7 14 · m(add9) 0 3 7 14 · maj9 0 4 7 11 14 · m9 0 3 7 10 14 · 9 0 4 7 10 14 · 7b9 0 4 7 10 13.

**Diatonic chords.** Major: I ii iii IV V vi vii° (C Dm Em F G Am B°). Natural minor: i ii° III iv v VI VII (Cm D° Eb Fm Gm Ab Bb). Harmonic minor changes v → **V (G 67 71 74)** and VII → **vii° (B°)**. Semitone offsets from tonic: I 0, ii 2, iii 4, IV 5, V 7, vi 9, bIII 3, bVI 8, bVII 10, bII 1. Relative minor = major tonic − 3.

**Time.** 16 steps per bar; beats 1–4 = steps 1, 5, 9, 13; `beat = (bar − 1) × 4 + (step − 1)/4`. Quarter ms = 60000/BPM; 16th ms = 15000/BPM; bar s = 240/BPM (16 bars at 140 = 27.4 s). PPQ 96: beat 96, 1/16 24, 1/16T 16, 1/8T 32, 1/32 12 ticks. MPC swing S% delays even 16ths by `(S − 50) × 0.48` ticks (66% ≈ 8 = triplet).

## Genre quick cards (most requested)

Full ~40-genre table with signature sounds and section lengths: `references/genre-cards.md`. Swing on the MPC scale (50 straight).

| Genre | BPM (range) | Feel / snare | Swing | Key / mode | Chords | Sub owner | Signature |
|---|---|---|---|---|---|---|---|
| Trap | 140 (130–160) | half-time, snare step 9 | 50, explicit triplets | minor, harmonic minor, Phrygian | 2–4 minor triads; i–VI–v | long 808, saturated | 8th hats + 1/32 & triplet rolls, bells |
| UK drill | 142 (138–151) | HT; bar 2 snare on step 13 | 50–54 | dark minor, b2 | i–v–VI, i–VII–VI | sliding 808 carries melody | 3+3+2 hats with gaps |
| NY drill | 144 (140–150) | as UK, punchier | ~50 | minor triads | harm. minor V | heavy long-glide 808 | hook-forward, hard drums |
| Boom bap | 90 (85–95) | 2&4 | 57 kick/snare, 74 hats | sample key, minor/Dorian | sampled m7/9 | bass doubling kick | chopped vinyl, layered kicks |
| Lo-fi | 78 (60–90) | 2&4, late soft snare | ~58–64 (FL 20–30%) | Dorian/minor | maj7/m7/9, ii–V–I | soft LP bass | LP ~3 kHz, vinyl, loose |
| R&B | 75 (60–90) | 2&4 or 3, rim ghosts | ~55–58 (FL 15–20%) | minor/Dorian | 7ths–13ths, passing | 808 tuned to roots | Rhodes, vocal chops |
| Afrobeats | 108 (95–115) | soft 2&4, syncopated kick | 54–58 | major | simple triads | round bass | 16th shaker, 3-2 clave |
| Amapiano | 112 (108–115) | light four-floor, rim 2&4 | 55–60 | minor/modal | m9/maj7/6-9 | log drum | log drum, offbeat open hat |
| Reggaeton | 94 (85–100) | dembow steps 4, 7, 12, 15 | 50 | minor | i–VI–III–VII | sidechained sub | dembow |
| House | 124 (120–126) | four-floor, clap 2&4 | 55–60 | minor/Dorian | m7/m9 vamps | offbeat bass | 909, offbeat open hat |
| Pop | 110 (95–125); ballad 75 | 2&4 or four-floor | 50–54 | major/minor | I–V–vi–IV family | sub/808 locked to kick | hook by 30–45 s |
| DnB | 174 (170–180) | two-step, snare 2&4 | ~50 | minor; liquid 7/9 | ii–V–I (liquid) | sub (+ reese mid) | chopped breaks, silence pre-drop |
| Future bass | 150 HT (140–160) | snare step 9 | 50 | major-leaning | maj7/m7/add9, royal road | long sub/808 | pitch-bent supersaw chords |

## FL Studio delivery (family-wide)

Details, tool table and troubleshooting: `references/fl-delivery.md`. Template: `references/make_midi_template.py`.

- **Start:** load the `fl_*` tools with one `ToolSearch("select:...")`, then `fl_check_bridge_status` → `fl_get_project_info` → `fl_set_tempo` → `fl_list_channels`.
- **Works on FL 21:** tempo, transport, channel list, `fl_set_step_sequencer` (on/off, ≤ 64 chars, selected pattern), channel volume/pan/pitch-cents, all mixer level/pan/routing/name tools, `fl_diagnose_mix` (while playing).
- **Does NOT apply on FL 21:** `fl_add_notes`, `fl_add_chord_progression`, `fl_quantize_piano_roll`, `fl_clear_piano_roll` (they only queue notes). Plugin knobs and mixer EQ are not settable — describe them.
- **Notes = MIDI files:** copy the template to `C:\Users\User\Documents\flstudio\<beat-name>\make_midi.py`, fill `build_parts()` with `(start_beat, midi, length_beats, velocity)` tuples, run `uv run --with mido --no-project python make_midi.py`. One `.mid` per channel; PPQ 96; ends clamped to the last bar.
- **Pitch rules:** drums at MIDI 60; a sampled 808 sounds at `sample_root + (note − 60)`; synth parts at real pitch. 808 glides need Mono + Porta on a native FL instrument (not VST/AU) and overlapping notes.
- **Swing:** no MCP tool. Bake exact MPC swing with `swing16()`, or tell the user to set both global and channel swing (> 0), starting ~15–30% FL, by ear.
- **Hand-off:** list key/BPM/swing/progression, what was applied, a file → channel → settings table, and what the user must dial in by hand.

## Quality checklist / common mistakes

- [ ] Every register named as MIDI plus FL label; no off-by-one octave (FL "C5" = MIDI 60).
- [ ] Every chord re-spelled from its formula; harmonic-minor V is major (B natural in C minor).
- [ ] Tempo, swing, snare placement and sub owner match the genre card; half-time genres put the snare on step 9.
- [ ] One sub owner; chord 3rds not below MIDI 48 under an 808; nothing else doubles the 808's octave.
- [ ] ≤ 4 focal elements per section; vocal space left in rap beats.
- [ ] One surprise per 4–8 bar context, none stacked; biggest twist saved for the last hook/drop.
- [ ] Busy drums ↔ medium harmony (or the reverse).
- [ ] No note ends past the last bar; drum MIDI at 60; slides only on native instruments with overlapping notes.
- [ ] Did not use piano-roll MCP tools as if they write notes on FL 21.
- [ ] Convention numbers (swing, grids, bar counts, 808 floor) flagged as "tune by ear".
- Common mistakes: writing the 808 an octave off because of FL's labels; MPC swing typed into FL's knob as the same number; a full authentic V–I cadence inside a loop that should cycle; stacking four new sounds into one hook; maxing loudness so the drop has no contrast.

## References

- `references/theory-tables.md` — open for any exact lookup: Hz for a note, all 12 keys and their diatonic chords, minor keys with 808 roots, compound intervals, full scale/mode list, chord formula table, Roman-numeral offsets, tempo/tick/swing tables.
- `references/genre-cards.md` — open when choosing or justifying a genre, for genres not in the quick table, section lengths, close-relative tie-breakers, or mood overrides.
- `references/science-of-beauty.md` — open when the user asks why something sounds good, when deciding where to spend surprise/complexity, or designing climaxes, hooks and builds; each finding has a "Do:".
- `references/fl-delivery.md` — open before the first FL tool call in a session, when writing MIDI, when a tool fails, or when composing the hand-off message.
- `references/make_midi_template.py` — copy it for every MIDI delivery; read its header for the helper API.

## Related skills

`music-drums-groove` (grids, swing, rolls, fills) · `music-bass-808` (808/bass notes, tuning, glides) · `music-chords-voicing` (progressions, voicing, cadences) · `music-melody-hooks` (melody, hooks, motifs) · `music-arrangement` (roles, register, song forms, builds) · `music-mix-master` (mixing, mastering, MCP mixer).
