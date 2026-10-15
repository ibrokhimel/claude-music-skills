# FL Studio delivery workflow (whole music family)

One-line summary: how every music skill gets its result into the user's FL Studio 21.2.3 — which `fl-studio-mcp` tools work, when to write MIDI files instead, the run/import procedure, the hand-off message to the user, and bridge troubleshooting.

Contents
1. Environment facts
2. Loading the tools
3. Tool status on FL 21
4. Delivery decision table
5. MIDI-file route (mido script)
6. Step-sequencer route
7. Order of operations for a full beat
8. Hand-off message to the user
9. Bridge troubleshooting
10. Known limits and gotchas

---

## 1. Environment facts

- FL Studio **21.2.3** (MIDI scripting API v30). MCP server `fl-studio-mcp` at `C:\Users\User\Documents\flstudio\fl-studio-mcp`, locally patched to talk over **MIDI SysEx** through the loopMIDI port **"FL MCP"** (FL MIDI settings: input and output both on **port 10**). FL 21's embedded Python has no `open`, `json`, `os` or `time`, which is why the upstream file-mailbox design fails and why piano-roll note writing does not work.
- Project PPQ: assume **96** (1/16 = 24 ticks). Check Options > Project general settings if timing looks off.
- Working folder for generated parts: `C:\Users\User\Documents\flstudio\<beat-name>\` (existing example: `ny-drill-midi\make_midi.py`).

## 2. Loading the tools

The `fl_*` tools are usually **deferred**. Load all you need in ONE call before use, e.g.:

`ToolSearch("select:mcp__fl-studio-mcp__fl_check_bridge_status,mcp__fl-studio-mcp__fl_set_tempo,mcp__fl-studio-mcp__fl_list_channels,mcp__fl-studio-mcp__fl_set_step_sequencer,mcp__fl-studio-mcp__fl_set_channel_pitch_pan_vol,mcp__fl-studio-mcp__fl_get_project_info")`

Mixer tools (`fl_assign_channel_to_mixer`, `fl_set_track_volume`, `fl_set_track_pan`, `fl_route_track`, `fl_set_track_name_color`, `fl_get_mixer_summary`, `fl_diagnose_mix`) are loaded by `music-mix-master` when mixing.

## 3. Tool status on FL 21

| Tool | Status | Use / notes |
|---|---|---|
| `fl_check_bridge_status` | works | first call of every session; if it fails see §9 |
| `fl_get_project_info`, `fl_get_transport_state` | works | read tempo, pattern, play state |
| `fl_set_tempo(bpm)` | works | set from the genre card before anything else |
| `fl_list_channels` | works | get channel indices and names; never assume indices |
| `fl_set_step_sequencer(channel_index, step_pattern)` | works | on/off steps only, `"1000100010001000"`, up to 64 chars (4 bars), writes into the **selected pattern**; no per-step velocity or pitch |
| `fl_set_channel_pitch_pan_vol(channel_index, volume, pan, pitch)` | works | volume 0–1 (0.78 default), pan −1..1, pitch in cents ±1200 — use to tune a drum or 808 sample to the key |
| `fl_mute_channel` | works | A/B parts |
| `fl_play`, `fl_stop`, `fl_pause`, `fl_set_loop_mode`, `fl_toggle_record` | works | audition |
| Mixer: `fl_assign_channel_to_mixer`, `fl_set_track_volume` (0–1; 0.8 = 0 dB), `fl_set_track_pan`, `fl_route_track`, `fl_set_track_name_color`, `fl_mute_track`, `fl_solo_track`, `fl_get_mixer_summary` | works | see `music-mix-master`; read-back of volume lags one change inside a batch; keep batches ≤ ~40 calls |
| `fl_diagnose_mix` | partial | only while playing; polled peaks miss short one-shot drums |
| `fl_add_notes`, `fl_add_chord_progression`, `fl_quantize_piano_roll`, `fl_clear_piano_roll` | **do not apply on FL 21** | they only queue notes for the "MCP PianoRoll" script, which needs file access FL 21 lacks — use MIDI files instead |
| Plugin knobs, mixer EQ | not available | describe settings for the user to dial in |
| Channel swing / global swing | no tool | tell the user, or bake swing into MIDI with `swing16()` |

## 4. Delivery decision table

| Content | Route |
|---|---|
| Tempo | `fl_set_tempo` |
| Simple on/off drum rows (kick, clap, hats without rolls), one velocity | `fl_set_step_sequencer` on the right channel |
| Drums with velocity accents, ghosts, rolls, triplets, flams, swing | MIDI file (one per drum channel, notes at MIDI 60) |
| 808 / bass (pitch, length, slides) | MIDI file; channel set to Mono + Porta for glides |
| Chords, pads, keys, melody, counter-melody, arps | MIDI file per part |
| Sample tuning | `fl_set_channel_pitch_pan_vol(pitch=cents)` or describe |
| Levels, pans, routing, track names/colours | mixer tools (`music-mix-master`) |
| EQ, compression, sidechain, reverb, saturation settings | describe for the user (`music-mix-master`) |
| Song arrangement in the Playlist | describe the bar layout (`music-arrangement`); patterns are placed by the user |

## 5. MIDI-file route (mido script)

1. Copy `references/make_midi_template.py` to `C:\Users\User\Documents\flstudio\<beat-name>\make_midi.py`.
2. Set `BPM`, `BARS` (the loop length; every note is clamped to end by the last bar line, because a note past it makes FL add a bar).
3. Write `build_parts()` returning `{part_name: [(start_beat, midi, length_beats, velocity), ...]}`. Helpers:
   - `pos(bar, step, ticks=0)` → beats (1-based bar and 16-step).
   - `grid("X... ..x. X... ....", bars)` → drum notes from family grid notation (`X` 118, `x` 95, `g` 48, `o` 90; `.`/`r` rest).
   - `scale_note(root, "minor", degree, octave)`, `chord(root, "m7", start, length, vel)`.
   - `swing16(notes, mpc_percent)` → exact MPC/Linn swing on even 16ths (66 ≈ triplet).
   - `TRIP16 = 1/6`, `TRIP8 = 1/3`, `STEP = 1/4`, `HIT = 1/8` beat one-shot length.
4. Run: `uv run --with mido --no-project python make_midi.py` (optional arg: output folder). Each part prints `name.mid: N notes`; a "dropped" count means notes started outside the loop or had invalid pitch — fix them.
5. The writer trims same-pitch overlaps (MIDI cannot hold two identical notes) and keeps different-pitch overlaps (these glide when the channel is Mono + Porta).

Pitch rules for the parts:
- **Drums**: MIDI 60 (FL "C5") = the sample's own pitch in FL's Sampler.
- **Sampled 808**: heard pitch = sample root + (note − 60). Measure or ask the 808's root (e.g. "BULLY 808 = C1"); then the key's tonic is `60 + (tonic_pc − sample_pc)`, wrapped so roots stay within about ±7 of 60. Alternative: retune the sample with channel pitch cents so that 60 = the key's tonic.
- **Synth 808/bass** (3x Osc, FLEX, Sytrus): write real pitches, roots in MIDI 24–40 — see `music-bass-808`.
- **Chords/melody**: real pitches (chords mostly ≥ MIDI 48 when an 808 owns the sub).
- **Slides**: only on FL native instruments/Sampler/FLEX/3x Osc (not VST/AU); channel settings > Misc: Mono + Porta; only overlapping notes glide.

User import (tell them): open the channel's Piano roll and drag the `.mid` from Explorer into it, or Piano roll menu > File > Import MIDI file; repeat per channel. Dropping a MIDI file elsewhere (empty Channel Rack, Playlist) can create new channels instead **(convention; verify on the user's FL)**.

## 6. Step-sequencer route

1. `fl_list_channels` → map part names to indices (ask the user to load samples first if channels are empty or default).
2. Make sure the intended pattern is selected (the tool writes into the selected pattern).
3. Convert each grid row to binary: any hit symbol (`X x g o`) → `1`, `.` → `0`; 16 chars per bar, up to 64 chars. Example trap kick `X... .... ..x. ....` → `1000000000100000`.
4. Velocity accents are lost on this route — use it for sketches, simple house/techno rows, or when the user wants editable steps; otherwise write MIDI.

## 7. Order of operations for a full beat

1. `fl_check_bridge_status` → `fl_get_project_info`.
2. `fl_set_tempo(card BPM)`.
3. `fl_list_channels`; agree channel names with the user (kick, snare/clap, hats, open hat, perc, 808, keys, lead...).
4. Simple drum rows → `fl_set_step_sequencer`; everything else → one script run producing all `.mid` files.
5. Tune samples (`fl_set_channel_pitch_pan_vol` pitch cents) if the 808/kick is off-key.
6. Mixer pass via `music-mix-master` (assign channels to tracks, levels, pans, names/colours) — only after notes are in.
7. `fl_play` + loop mode for audition; `fl_diagnose_mix` while playing.

## 8. Hand-off message to the user

Always end a composing turn with:
- Key, scale, BPM, swing (MPC value and FL starting point), bar count, progression in Roman numerals and chord names.
- What was applied directly (tempo, step rows, mixer moves).
- A table: `.mid` file → which channel → instrument/sample suggestion → special settings (e.g. "808: Mono + Porta, slide time ~ by ear").
- Settings the user must dial by hand (swing knobs, EQ, sidechain, plugin settings).
- One or two suggested next moves (variation bar, arrangement, mix).

## 9. Bridge troubleshooting

1. `fl_check_bridge_status` fails or times out → is **loopMIDI** running with port "FL MCP"?
2. FL: Options > MIDI settings — "FL MCP" input and output enabled, both on **port 10**, controller script assigned.
3. View > Script output — look for errors in the device script.
4. Port numbers mismatch → fix in MIDI settings, then restart the script (or FL).
5. Scripts missing or stale → reinstall with the server's `install.copy_fl_script` (bakes in the home-dir fallback), restart FL.
6. Calls hang inside big batches → keep batches to ≤ ~40 calls; ~400-call batches time out.
7. Notes "added" but nothing appears in the piano roll → expected on FL 21; deliver MIDI files.

## 10. Known limits and gotchas

- No note may end past the last bar (FL adds an extra bar). The template clamps this.
- `fl_set_track_volume` read-back lags by one change inside a batch: set, then read in a separate request.
- `fl_diagnose_mix` polled peaks miss short drums; judge drum balance by ear or from sample RMS.
- Channel swing works only if BOTH global and channel swing are > 0; FL swing % ≠ MPC swing %.
- Slides do not work on VST/AU instruments.
- Velocity in FL is shown in %: MIDI ≈ % × 1.27.
- Never call unknown no-argument FL API functions as probes (some, e.g. undo, act immediately).
