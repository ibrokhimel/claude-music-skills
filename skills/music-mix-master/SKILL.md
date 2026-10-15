---
name: music-mix-master
description: Mix and master beats in FL Studio - gain staging, static balance, EQ lanes, compression, sidechaining the 808 to the kick, panning and stereo width, reverb/delay times from BPM, 808 saturation and clipping, master chain and loudness targets (LUFS, true peak) for Spotify, YouTube, Apple and beat leases. Applies fader levels, pans, bus routing and track names directly through the fl-studio-mcp mixer tools, and tells the user the exact Fruity Parametric EQ 2, Fruity Limiter, Reeverb 2, Delay 3, Maximus, Soundgoodizer and Soft Clipper settings to dial in. Use whenever the user says mix, master, mixdown, balance, levels, too quiet, too loud, clipping, muddy, harsh, boomy, 808 too loud or not hitting, kick and 808 clash, sidechain, EQ, compressor, reverb, delay, panning, stereo, mono, headroom, LUFS, make it louder, make it sound professional or radio-ready, or asks to set up the FL Studio mixer, buses or sends - including right after composing a beat.
---

# music-mix-master

Purpose: turn a composed beat into a balanced, translating mix and a platform-appropriate master inside the user's FL Studio 21. Claude applies everything the API can reach (mixer-insert assignment, names, colors, fader levels, pan, bus routing, mute/solo, playback and peak checks) and writes precise plugin settings for the user to dial in (EQ, compression, sidechain, reverb, delay, saturation, limiting), because FL 21 exposes no mixer-EQ API and plugin knobs are not reliably settable. Composition belongs to the other skills; this one starts when sounds and notes exist.

## Core principles (with the why)

1. **Gain stage before anything else.** Plugins modelled on analog gear expect roughly −18 to −12 dBFS input and distort when fed near 0 dBFS **(sourced)**. Target each insert at about −18 dBFS average with peaks −12 to −6 dBFS, and leave the master peaking near −6 dBFS before any master processing **(sourced)**. FL mixes in 32-bit float so overs do not clip permanently inside the mixer, but plugins still react to level.
2. **Balance with faders and pan first, processing second.** A static mix (faders, pan, polarity only) done fast exposes what actually needs EQ or compression **(sourced, iZotope)**. Most "mixing problems" in beats are level problems.
3. **Every element gets a lane.** Masking happens when two parts put energy in the same band at the same time. High-pass everything that does not need low end, decide whether the kick or the 808 owns the sub, and cut before boosting **(sourced)**.
4. **The sub is mono and centered.** Kick, 808/bass, snare and the lead/vocal sit in the center; width lives above ~100–150 Hz **(sourced)**. Mono-incompatible lows vanish on club systems and phones.
5. **Space comes from sends, timed to the tempo.** Reverb and delay go on send tracks at 100% wet, timed from 60000/BPM **(sourced)**. Inserted reverbs and a reverb on the master turn the mix to mud.
6. **Loudness is a delivery setting, not a quality.** Platforms normalize (Spotify/YouTube −14 LUFS, Apple −16) **(sourced)**; loudness has little effect on listener preference and hypercompression side effects are disliked (Vickers 2010) **(sourced)**. Keep section contrast: a drop only hits if the verse is quieter. Master louder (−8 to −10 LUFS) only when the user wants a competitive beat-lease master.
7. **Measure, then trust ears.** FL's meters are sample-peak, polled peaks miss short drum hits, and the API cannot read LUFS. Use numbers to catch errors and the user's ears (75–85 dB SPL, plus a very-low-volume check) for decisions.

## Procedure

Follow in order. Steps marked API are done by Claude with MCP tools; steps marked USER are written as exact instructions for the user.

1. **Check the bridge.** `fl_check_bridge_status`. If it fails: loopMIDI running, FL Script output window, port 10 for FL MCP in and out.
2. **Inventory (API).** `fl_list_channels` (names, mixer routing) and `fl_get_mixer_summary` (named tracks, volume, pan). Note BPM from `fl_get_project_info`. Ask which section is densest (the drop/hook) - mix there first.
3. **Lay out the mixer (API).** Give every channel its own insert with `fl_assign_channel_to_mixer` using the track map below, then `fl_set_track_name_color`. Create buses (Drums, Music, Vocal) and sends (Verb Short, Verb Long, Delay) on empty inserts and name them.
4. **Route buses (API).** `fl_route_track(source, bus)` then remove the source's direct master route with `fl_route_track(source, 0, enable=False)` - otherwise the part reaches the master twice. Buses keep their master route. Route each insert to the send tracks the same way but keep its master route (the send is in addition). Send levels cannot be set by API: tell the user the send-knob amounts.
5. **Sidechain routing (USER).** `fl_route_track` creates a full audio route, so it would feed the kick's audio into the 808 chain. Ask the user to do it by hand: select the kick insert, right-click the 808 insert's send arrow, choose "Sidechain to this track". Then set Fruity Limiter's SIDECHAIN box on the 808 insert. Details in `references/fl-mixer-procedure.md`.
6. **Gain stage (API + USER).** Leave channel-rack volumes at default (0.78) unless a sample is extreme. Set all inserts to unity (0.8) as the start, pull the master to unity, and make headroom with insert faders, never with the master fader.
7. **Static balance (API).** Set faders in the balance order below, starting from the anchor (kick), with `fl_set_track_volume`. The fader curve is not linear: set, read back in a separate request, adjust (see "Fader values"). Pan with `fl_set_track_pan` using the pan map.
8. **Check while playing (API).** `fl_set_loop_mode` on the densest pattern, `fl_play`, then `fl_diagnose_mix` 2-3 times; `fl_stop`. Trust it for clipping on sustained parts (808, pads, master). Do not trust it for short drum one-shots - balance drums by sample RMS plus fader dB (`references/fl-mixer-procedure.md`).
9. **EQ lanes (USER).** Write Fruity Parametric EQ 2 settings per insert from the EQ table below: high-passes first, then the kick/808 carve, then one or two corrective cuts, then small wide boosts only if needed.
10. **Dynamics (USER).** Kick/snare compression, drum-bus glue, optional parallel drum bus, 808 sidechain (~2.5:1 start). Settings in the compression table.
11. **Space (USER).** Reeverb 2 / Delay 3 on the send tracks with times from the tempo table; tell the user send-knob levels.
12. **Saturation and clipping (USER).** 808 harmonics for small speakers (clean sub + saturated high-passed layer), optional Soft Clipper on the drum bus (1–3 dB of peak shaving).
13. **Re-balance (API).** Processing changes levels: repeat steps 7-8.
14. **Checks.** Run the checklist at the end of this file; have the user listen in mono, at very low volume, on a phone or laptop, against a reference track at matched loudness.
15. **Master (USER).** Print or route the mix with the master peaking near −6 dBFS, then build the master chain: optional gentle EQ → glue 1.5–2:1 for 1–2 dB GR → limiter with ceiling −1.0 to −1.5 dB → loudness meter. Pick the target from the loudness table and confirm the user's goal (streaming vs beat lease).

## Default track map (convention)

Use these inserts unless the project already has a layout; adapt numbers to the channel list.

| Insert | Name | Color | Pan | Routes to |
|---|---|---|---|---|
| 1 | Kick | #E04040 | 0 | Drums bus (or Master) |
| 2 | 808 | #E07020 | 0 | Master (keep the 808 off the drum bus so drum glue does not pump it) |
| 3 | Snare/Clap | #E0B020 | 0 | Drums bus |
| 4 | Hats | #C0C040 | −0.15 | Drums bus |
| 5 | Open hat / Ride | #A0C040 | +0.25 | Drums bus |
| 6 | Perc | #60C060 | ±0.30 alternate | Drums bus |
| 7 | Lead / Melody | #4080E0 | 0 | Music bus |
| 8 | Chords / Pad | #6060E0 | 0 (stereo source) | Music bus |
| 9 | Counter / Arp | #8060E0 | ±0.30 | Music bus |
| 10 | Vocal | #E060C0 | 0 | Vocal bus |
| 20 | Drums bus | #A03030 | 0 | Master |
| 21 | Music bus | #3050A0 | 0 | Master |
| 22 | Vocal bus | #A03080 | 0 | Master |
| 23 | Verb Short | #40A0A0 | 0 | Master |
| 24 | Verb Long | #308080 | 0 | Master |
| 25 | Delay | #50B0B0 | 0 | Master |

## Static balance order (convention - no source gives fixed dB offsets)

Loudest to quietest in trap/hip-hop/drill: **kick and 808** (trade off; one usually leads) → **snare/clap** → **lead or vocal** → **music bed** (chords, pads, counter-melodies) → **hats, percussion, FX**. Kick and snare are the usual anchors in hip-hop and electronic music **(sourced)**.

Starting insert-peak targets (convention, tune by ear; sustained parts read reliably, drum peaks do not):

| Element | Insert peak (dBFS) | Relative starting point |
|---|---|---|
| Kick (anchor) | −10 to −8 | reference |
| 808 / bass | −10 to −8 | perceived level similar to kick |
| Snare / clap | −12 to −10 | 2–4 dB under kick |
| Lead / vocal | −14 to −10 | about snare level, must stay audible at low volume |
| Chords / pads | −18 to −14 | 4–8 dB under lead |
| Hats | −20 to −14 | clearly under snare (hats louder than snare = mistake) |
| Perc / FX | −22 to −16 | under hats |
| Master (no processing) | about −6 | **(sourced)** headroom for mastering |

## Fader values

`fl_set_track_volume` takes 0–1; **0.8 = 0 dB (unity)** **(sourced: MCP docs)**. 1.0 is about +5.6 dB (FL's maximum fader gain; unverified on this machine). The curve between those points is not linear and no verified table exists, so do not convert dB to fader values by formula. Instead:

1. Set a value with `fl_set_track_volume`.
2. Read it back in a **separate** request (read-back lags one change inside a batch). `fl_get_mixer_summary` confirms the 0–1 value; the dB value comes from FL's `mixer.getTrackVolume(track, 1)` via the bridge's `api_call` (script in `references/fl-mixer-procedure.md`).
3. Adjust and repeat. To get a full dB↔fader table once, run the calibration script in that reference on an unused insert and reuse its output.

Without dB read-back, steer by the meters: move a fader, play, `fl_diagnose_mix`, compare peaks.

## EQ quick map (regions sourced from iZotope; HPF points and moves are convention)

| Region | Range | Character |
|---|---|---|
| Sub | 20–60 Hz | foundation, felt more than heard |
| Bass | 60–250 Hz | body, weight |
| Low-mids | 200–500 Hz | box, mud (most common cut zone) |
| Mids | 500 Hz–2 kHz | presence, nasal, honk |
| Presence | 2–8 kHz | clarity, attack, harshness |
| Air | 8 kHz+ | sparkle, shimmer |

| Element | High-pass | Typical moves |
|---|---|---|
| Kick | none (or 25–30 Hz rumble) | punch 60–100 Hz; cut box 200–500 Hz; click 2–5 kHz |
| 808 | none (or 25–30 Hz) | owns 40–60 Hz; notch 2–4 dB at kick fundamental if not sidechaining |
| Snare/clap | 80–100 Hz | body 150–250 Hz; ring 400–700 Hz narrow cut; crack 2–4 kHz |
| Hats/cymbals | 200–400 Hz | tame 3–7 kHz harshness sparingly |
| Lead/keys/pads | 100–200 Hz | pads dip 2–4 dB at 1–4 kHz for the lead/vocal |
| Vocal | 80–150 Hz | nasal 500 Hz–1.2 kHz cut; harsh 5–8 kHz cut; air 10 kHz+ |
| Reverb/delay returns | 200–400 Hz | low-pass 6–10 kHz |

Boosts: wide Q, 1–3 dB. Cuts: narrow for resonances, wider for mud. Full lanes and the Parametric EQ 2 recipe: `references/levels-eq-compression.md`.

## Compression and sidechain (FL stock)

| Use | Plugin / mode | Starting settings | Evidence |
|---|---|---|---|
| Kick | Fruity Limiter COMP | 4:1 (to 6–8:1), attack 10–20 ms, release 50–100 ms, 2–4 dB GR | sourced ratio/attack |
| Snare | Fruity Limiter COMP | 3–4:1, attack 20–30 ms, fast release | sourced attack |
| Drum bus glue | Fruity Limiter COMP | 2:1, attack 10–30 ms, release 100–200 ms, 2–3 dB GR (max 5) | sourced 2:1, 2–5 dB |
| Parallel drums | send drums to a "Drums Smash" bus | 6–10:1, fast attack/release, 8–12 dB GR, blend under dry | convention |
| Kick → 808 duck | Fruity Limiter COMP, SIDECHAIN = kick | **2.5:1 start** (to 4:1), attack 0–1 ms, release 50–150 ms (recover before the next 808 note), 3–6 dB GR | sourced 2.5:1; rest convention |
| Pumping pads | same, on Music bus | 6–10 dB GR, release about 1/8 note (30000/BPM ms) | convention |
| Alt. duck | Fruity Peak Controller on kick | Volume negative, Decay = return time, Tension = curve; link to 808 insert volume | sourced mechanics |

808 compression: slower attack passes the transient; very fast settings react to individual waveform cycles and distort **(sourced)**. Step-by-step sidechain setups: `references/levels-eq-compression.md`.

## Stereo and pan map (convention unless marked)

- Center: kick, 808/bass, snare/clap, lead, vocal.
- Mono below ~100–150 Hz **(sourced)**; high-pass the side signal of any widener at 100–150 Hz.
- Hats 10–30% off center with the open hat opposite; percussion 20–50% alternating; doubles 50–100%.
- Haas widening (1–30 ms delayed copy) sounds wide but is often not mono-compatible **(sourced)**: never on bass, check in mono.
- Pan values for `fl_set_track_pan`: 15% = ±0.15, etc. (−1 = hard left).

## Space: tempo math (derived from 60000/BPM)

Quarter note ms = 60000/BPM; 1/8 = ÷2; dotted 1/8 = ×0.75 of a quarter; 1/8 triplet = ÷3; 1/16 = ÷4; pre-delay 1/64–1/16 note **(sourced)**. Full 70–160 BPM table: `references/space-stereo-saturation.md`.

| BPM | 1/4 | 1/8 | dotted 1/8 | 1/16 | 1/64 |
|---|---|---|---|---|---|
| 70 | 857 | 429 | 643 | 214 | 54 |
| 90 | 667 | 333 | 500 | 167 | 42 |
| 120 | 500 | 250 | 375 | 125 | 31 |
| 140 | 429 | 214 | 321 | 107 | 27 |
| 160 | 375 | 188 | 281 | 94 | 23 |

Reverb by role (convention): room 0.3–0.8 s for drums; plate 1–2 s with 20–40 ms pre-delay for snare, vocals, leads; hall 2–4 s for pads and FX. Decay ends by the next beat (tight) or the next bar (lush) **(sourced)**. Reeverb 2 on a send: Dry 0%, Wet 100% **(sourced)**.

## Loudness targets (sourced)

| Destination | Integrated | True peak |
|---|---|---|
| Spotify | −14 LUFS | ≤ −1 dBTP (≤ −2 dBTP if louder than −14) |
| YouTube | −14 LUFS (turns loud down, does not raise quiet) | ≤ −1 dBTP |
| Apple Music (Sound Check) | −16 LUFS | ≤ −1 dBTP |
| AES TD1008 (music) | −16 LUFS | ≤ −1 dBTP |
| Competitive hip-hop / beat lease | −8 to −10 LUFS | ≤ −1 dBTP |

Fruity Limiter is not a true-peak limiter: set its ceiling to −1.0 to −1.5 dB. FL meters cannot show LUFS; the user needs a loudness meter (e.g. Youlean Loudness Meter, free). Master chain and plugin settings: `references/mastering-loudness.md`.

## FL Studio delivery notes

- Apply directly: insert assignment, names/colors, fader volume, pan, bus routing, mute/solo, play/stop/loop, peak diagnostics. Keep batches at 40 calls or fewer; do set and read-back in separate requests.
- Describe for the user: every plugin (load into which insert slot, which mode, which knob values), send-knob amounts, sidechain-to-this-track routing, Fruity Limiter SIDECHAIN selection, Peak Controller links.
- Format plugin instructions as: `Insert 2 "808" -> slot 1: Fruity Limiter, COMP tab: THRES -20 dB, RATIO 2.5:1, ATT 1 ms, REL 120 ms, SIDECHAIN = Kick.` One line per plugin, values the user can type or drag to.
- `fl_diagnose_mix` only works while playing. It flags peaks ≥ 0 dBFS (clipping), above −3 dBFS (low headroom) and L/R differences ≥ 3 dB. Polled every ~30 ms, it misses short one-shots.
- Never change a project the user has not asked to be mixed; before re-routing, read `fl_get_mixer_summary` and tell the user what will move.

## Checklist (run before calling a mix done)

- [ ] No insert peaks above −3 dBFS; master peaks near −6 dBFS before master processing.
- [ ] Kick, 808, snare, lead and vocal centered; nothing below ~120 Hz is wide.
- [ ] Kick and 808 have separate lanes (EQ split or sidechain) and the 808 is tuned to the key (see `music-bass-808`).
- [ ] Every non-bass element is high-passed; no build-up at 200–500 Hz.
- [ ] Hats sit under the snare; no more than ~3 elements dominate 1–5 kHz at once.
- [ ] Reverbs and delays are on sends at 100% wet, returns filtered; no reverb on master.
- [ ] Mono check: nothing important disappears. Low-volume check: lead/vocal and snare still read.
- [ ] Phone/laptop check: 808 line still audible (saturation layer working).
- [ ] Sections still contrast (verse quieter than hook); limiter is not flattening the drop.
- [ ] Master ceiling ≤ −1 dBTP equivalent; loudness matches the chosen target.

## Common beginner mistakes

Master clipping or no headroom; making headroom with the master fader; everything panned center (or bass panned off center); kick and 808 fighting (no sidechain, no lane, 808 out of key); no high-passes so low-mids turn to mud; hats too loud or harsh at 3–7 kHz; reverb inserted at 100% wet instead of on a send; stereo wideners on bass; Soundgoodizer or a limiter slammed on the master while still mixing; mixing soloed tracks instead of in context; judging only on loud headphones; comparing against references without matching loudness (louder always sounds better); slamming the master so the drop is no louder than the verse.

## References

- `references/levels-eq-compression.md` - open when setting levels, writing EQ for a specific instrument, or configuring any compressor or sidechain (full per-instrument EQ lanes, Parametric EQ 2 recipes, Fruity Limiter COMP and sidechain steps, Peak Controller method, parallel compression, sources).
- `references/space-stereo-saturation.md` - open for reverb/delay setup and times (full 70–160 BPM table), panning and width tools, Haas caveats, 808 saturation layering, drum clipping with Fruity Soft Clipper.
- `references/mastering-loudness.md` - open when mastering or the user asks about LUFS, loudness, Maximus, Soundgoodizer, limiter ceilings, platform targets, or "make it louder".
- `references/fl-mixer-procedure.md` - open before touching the mixer through MCP: exact tool-call sequence, bus/send routing, sidechain by hand, fader read-back and calibration script, drum RMS balancing script, troubleshooting.

## Related skills

- `music-theory-core` - hub: genre parameter cards, tempo math, FL delivery workflow.
- `music-bass-808` - 808 tuning, range, slides and sound choice (do this before mixing the low end).
- `music-drums-groove` - drum programming and velocities (velocity balance affects drum levels).
- `music-arrangement` - frequency/register slotting and energy curve; arrangement fixes masking better than EQ.
- `music-chords-voicing`, `music-melody-hooks` - voicing register and lead range, which decide how much EQ carving is needed.
