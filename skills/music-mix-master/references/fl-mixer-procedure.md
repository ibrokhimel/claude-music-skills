# FL Studio mixer procedure via fl-studio-mcp

Exact MCP call sequence for laying out, routing, leveling and checking a mix in the user's FL Studio 21.2.3, plus bridge scripts for dB read-back, fader calibration and drum RMS balancing.

## Contents
1. What the API can and cannot do
2. Call sequence
3. Bus and send routing
4. Sidechain routing (manual)
5. Fader values and dB read-back
6. Fader calibration script
7. Checking levels while playing
8. Balancing drums by sample RMS
9. Writing plugin instructions for the user
10. Troubleshooting

## 1. What the API can and cannot do

| Can (Claude applies) | Cannot (user does, Claude writes exact settings) |
|---|---|
| channel → insert assignment (`fl_assign_channel_to_mixer`) | load plugins into slots, set plugin knobs (not reliably settable) |
| track name and color (`fl_set_track_name_color`, hex `#RRGGBB`) | mixer EQ (no API in FL 21) |
| fader 0–1 (`fl_set_track_volume`), pan −1..1 (`fl_set_track_pan`) | send-knob levels (see 3) |
| full audio routes on/off (`fl_route_track`) | sidechain-only routes ("Sidechain to this track") |
| mute/solo (`fl_mute_track`, `fl_solo_track`, `fl_mute_channel`) | Fruity Limiter SIDECHAIN selector (not an API param) |
| play/stop/loop, peak scan (`fl_play`, `fl_stop`, `fl_set_loop_mode`, `fl_diagnose_mix`) | LUFS / true-peak measurement |
| channel volume/pan/pitch (`fl_set_channel_pitch_pan_vol`, volume 0–1, default 0.78) | |

Limits: keep batches to about 40 calls or fewer (≈400 timed out). `fl_set_track_volume` read-back lags one change inside a batch - set and read in separate requests. Track indices: 0 = Master, 1–125 = inserts.

## 2. Call sequence

1. `fl_check_bridge_status` - stop and troubleshoot (section 10) if it fails.
2. `fl_get_project_info` - BPM (for reverb/delay/release times).
3. `fl_list_channels` - channel index, name, current mixer track.
4. `fl_get_mixer_summary` (only_named=True) - existing names, volumes, pans. If the project already has a layout, keep it and adapt; tell the user before moving anything.
5. For each channel: `fl_assign_channel_to_mixer(channel_index, insert)` using the track map in SKILL.md.
6. For each insert, bus and send: `fl_set_track_name_color(track_index, name, "#RRGGBB")`.
7. Routing (section 3): `fl_route_track(...)`.
8. Reset levels: `fl_set_track_volume(t, 0.8)` for every used insert, bus and the master (0.8 = 0 dB).
9. Pan: `fl_set_track_pan(t, value)` from the pan map.
10. Static balance: set faders (section 5), anchor first.
11. `fl_set_loop_mode` (pattern mode on the densest pattern, or song mode over the hook), `fl_play`, `fl_diagnose_mix` 2–3 times about a second apart, `fl_stop`.
12. Adjust faders; repeat 11.
13. Write the plugin/send instructions for the user (section 9). After the user confirms they are in, repeat 10–12 (processing changes levels).
14. `fl_get_mixer_summary` - final read-back; report the layout to the user as a table.

Example for a 7-channel trap beat (channels from `fl_list_channels`: 0 808, 1 Clap, 2 Hat, 3 Snare, 4 Kick, 5 Strings, 6 Perc):

```
fl_assign_channel_to_mixer(4, 1)   fl_set_track_name_color(1, "Kick", "#E04040")
fl_assign_channel_to_mixer(0, 2)   fl_set_track_name_color(2, "808", "#E07020")
fl_assign_channel_to_mixer(3, 3)   fl_set_track_name_color(3, "Snare", "#E0B020")
fl_assign_channel_to_mixer(1, 4)   fl_set_track_name_color(4, "Clap", "#E0A040")
fl_assign_channel_to_mixer(2, 5)   fl_set_track_name_color(5, "Hats", "#C0C040")
fl_assign_channel_to_mixer(6, 6)   fl_set_track_name_color(6, "Perc", "#60C060")
fl_assign_channel_to_mixer(5, 7)   fl_set_track_name_color(7, "Strings", "#6060E0")
fl_set_track_name_color(20, "Drums Bus", "#A03030")
fl_set_track_name_color(21, "Music Bus", "#3050A0")
fl_set_track_name_color(23, "Verb Short", "#40A0A0")
fl_set_track_pan(5, -0.15)   fl_set_track_pan(6, 0.30)
```

## 3. Bus and send routing

`fl_route_track(source, target, enable)` calls FL's `mixer.setRouteTo` + `afterRoutingChanged`: a full audio route. A new insert routes to the Master by default, and adding a route does not remove that.

Bus (exclusive path):
```
fl_route_track(3, 20)              # Snare -> Drums Bus
fl_route_track(3, 0, enable=False) # remove Snare -> Master, else it reaches the master twice
```
Leave the bus → Master route on. Do the same for every member of a bus.

Send (parallel path - reverb, delay, parallel compression):
```
fl_route_track(3, 23)              # Snare -> Verb Short, keep Snare -> Master
```
Send level: the new route's level is not settable through the MCP tools. Tell the user to set it with the send knob on the source strip (the small knob by the route arrow) - typical starting amounts: drums to Verb Short low, snare/clap moderate, lead/vocal to plate or delay moderate, pads to Verb Long moderate (convention; judge by ear). Until the user sets it, consider muting the send track (`fl_mute_track(23, True)`) so a full-level send does not swamp the mix. If needed, check whether the build exposes a route-level function via `api_call` (e.g. `mixer.getRouteToLevel` / `setRouteToLevel`) - unverified on FL 21, so read first, then set.

Do not route the 808 into the Drums bus if the bus has glue compression that the 808 would pump (convention); 808 → Master directly.

Verify a route: `api_call mixer.getRouteSendActive(src, dst)` (section 5 script pattern). Remove a wrong one: `fl_route_track(src, dst, enable=False)`.

## 4. Sidechain routing (manual)

`fl_route_track` cannot make a sidechain-only route. Ask the user:

1. Click the Kick insert (selected = source).
2. Right-click the arrow at the bottom of the 808 insert (destination) → "Sidechain to this track".
3. Load Fruity Limiter on the 808 insert → COMP → right-click SIDECHAIN → pick the kick input by name (box shows the list position, e.g. 1).
4. RATIO 2.5:1 start, ATT 0–1 ms, REL 50–150 ms, THRES down to 3–6 dB GR on kick hits.

Then verify direction with `mixer.getRouteSendActive(kick, 808)` → True. `mixer.getTrackPeaks` does not show GR; the user confirms ducking on the Limiter display. `mixer.focusEditor(track, slot)` + `ui.showWindow(0)` via `api_call` can open the plugin window for the user.

## 5. Fader values and dB read-back

- `fl_set_track_volume`: 0–1, 0.8 = 0 dB (sourced: MCP docs). 1.0 ≈ +5.6 dB (FL maximum; unverified here). The curve is not linear; no verified dB↔fader table exists - do not compute values by formula. Use read-back or the calibration table (section 6).
- `fl_get_mixer_summary` returns the 0–1 value only.
- FL's `mixer.getTrackVolume(track, 1)` returns the fader in dB (tested on FL 21). Reach it through the bridge's `api_call` handler from a Python script (no MCP tool wraps it):

```python
# read_db.py  -- run: uv run --project C:\Users\User\Documents\flstudio\fl-studio-mcp python read_db.py 1 2 3
import sys
sys.path.insert(0, r"C:\Users\User\Documents\flstudio\fl-studio-mcp")
from src.bridge import FLBridge
b = FLBridge()
for t in map(int, sys.argv[1:]):
    db = b.call("api_call", {"module": "mixer", "function": "getTrackVolume", "args": [t, 1]})
    v = b.call("api_call", {"module": "mixer", "function": "getTrackVolume", "args": [t]})
    print(t, "fader", round(v, 4), "dB", db)
```

Put scripts in the scratchpad or a project `scripts/` folder, not the user's root. Each `b.call` is a separate request, so the lag-inside-batch issue does not apply.

Loop to hit a dB target: set with `fl_set_track_volume`, read with the script, nudge (≈0.01–0.03 per step near unity, larger steps lower down), repeat. Report final values to the user as dB, not as 0–1.

## 6. Fader calibration script

Run once on an unused insert (default 50, check it is unnamed and silent first), save the output table, then convert dB targets by lookup/interpolation. Restores the original value at the end.

```python
# calibrate_fader.py -- uv run --project C:\Users\User\Documents\flstudio\fl-studio-mcp python calibrate_fader.py 50
import sys
sys.path.insert(0, r"C:\Users\User\Documents\flstudio\fl-studio-mcp")
from src.bridge import FLBridge
b, t = FLBridge(), int(sys.argv[1] if len(sys.argv) > 1 else 50)
call = lambda f, *a: b.call("api_call", {"module": "mixer", "function": f, "args": list(a)})
orig = call("getTrackVolume", t)
print("| fader | dB |\n|---|---|")
for i in range(0, 101, 5):
    call("setTrackVolume", t, i / 100)      # one request
    print(f"| {i/100:.2f} | {call('getTrackVolume', t, 1)} |")  # separate request
call("setTrackVolume", t, orig)
```

If the output is useful, offer to add the table to this file so later sessions can convert dB directly.

## 7. Checking levels while playing

- `fl_diagnose_mix` reads `mixer.getTrackPeaks` for named tracks + Master while playing. Flags: peak ≥ 1.0 linear (≥ 0 dBFS, clipping), peak ≥ 0.707 (above −3 dBFS, low headroom), L/R difference ≥ 3 dB. All zeros = transport not running.
- It polls (~30 ms), so it reads sustained parts (808, pads, master) reasonably and misses short one-shot drums. Never conclude "the kick is quiet" from it.
- Take 2–3 readings across the loop and use the maximum.
- Raw master level without master plugins: via `api_call`, `mixer.enableTrackSlots(0, 0)`, measure, then `mixer.enableTrackSlots(0, 1)` - always turn the slots back on.
- Targets: inserts ≤ −6 dBFS peaks (flag anything above −3), master ≈ −6 dBFS before master processing.

## 8. Balancing drums by sample RMS

Because polled peaks miss drum hits, balance drums from the sample files:

1. Get sample paths: ask the user, or scan the .flp (paths are UTF-16LE strings inside it).
2. Measure peak and RMS of each sample:

```python
# drum_levels.py -- uv run --with soundfile --with numpy --no-project python drum_levels.py project.flp
import re, sys, numpy as np, soundfile as sf
raw = open(sys.argv[1], "rb").read()
paths = sorted({m.decode("utf-16-le") for m in re.findall(rb"(?:[\x20-\x7e]\x00){4,}?\.\x00(?:w\x00a\x00v\x00|W\x00A\x00V\x00)", raw)})
for p in paths:
    try:
        x, sr = sf.read(p, always_2d=True)
    except Exception as e:
        print("skip", p, e); continue
    peak = 20 * np.log10(np.max(np.abs(x)) + 1e-12)
    n = max(1, int(0.05 * sr))                        # RMS over the first 50 ms = the hit
    rms = 20 * np.log10(np.sqrt(np.mean(x[:n] ** 2)) + 1e-12)
    print(f"{peak:6.1f} dBFS peak  {rms:6.1f} dB RMS(50ms)  {p}")
```

If the regex finds nothing (path encoding differs), ask the user for the sample folder and measure those files instead.

3. Estimated level on the insert ≈ sample level + fader dB (+ channel volume and velocity, which cancel if every drum channel keeps the same channel volume, 0.78, and similar velocities). Example: kick sample peak −1 dBFS, snare −3 dBFS; for the snare to sit 3 dB under the kick, set the snare fader 1 dB below the kick fader.
4. Set faders with `fl_set_track_volume`, read back dB (section 5), then confirm by ear and with the user's meters during playback.

## 9. Writing plugin instructions for the user

One line per plugin, in signal order, with the insert number and name. Give values the user can type; give threshold as a GR target. Example block for a trap beat at 140 BPM:

```
Insert 1 "Kick"   -> slot 1 Fruity Parametric EQ 2: B1 HP 30 Hz 24 dB/oct; B3 Peak 300 Hz -3 dB Q 3; B6 Peak 3 kHz +2 dB Q 1
                  -> slot 2 Fruity Limiter COMP: RATIO 4:1, ATT 15 ms, REL 80 ms, THRES to 3 dB GR
Insert 2 "808"    -> slot 1 Fruity Limiter COMP: SIDECHAIN = Kick, RATIO 2.5:1, ATT 1 ms, REL 107 ms (1/16 @140), THRES to 4 dB GR on kick hits
                  -> slot 2 Fruity WaveShaper: soft clip preset, drive until it growls on a phone
Insert 5 "Hats"   -> slot 1 Fruity Parametric EQ 2: B1 HP 300 Hz 24 dB/oct; B5 Peak 5 kHz -2 dB Q 3 if harsh
Insert 20 "Drums Bus" -> Fruity Limiter COMP: RATIO 2:1, ATT 20 ms, REL 150 ms, THRES to 2-3 dB GR
Insert 23 "Verb Short" -> Fruity Reeverb 2: Dry 0%, Wet 100%, Decay 0.6 s, Pre-delay 27 ms (1/64 @140), Low cut 300 Hz, High cut 8 kHz
Sends: Snare -> Verb Short about a quarter of the knob; Strings -> Verb Long about a third (adjust by ear)
```

Remind the user that `mixer.focusEditor(track, slot)` can open each plugin window if they want Claude to bring it up.

## 10. Troubleshooting

- Tool errors/timeouts: `fl_check_bridge_status`; loopMIDI running; FL Options → MIDI Settings: "FL MCP" input and output on port 10 with the MCP device script; FL View → Script output for errors. Reinstall scripts with `install.copy_fl_script` if needed.
- Volume read-back shows the previous value: lag inside a batch - read again in a new request.
- `fl_diagnose_mix` all zeros: not playing, or the tracks are unnamed (only named tracks + Master are scanned) - name them first.
- Part plays twice as loud after bus routing: the source still routes to the Master - `fl_route_track(src, 0, enable=False)`.
- Kick audible in the 808 chain: an audio route kick → 808 exists - remove with `fl_route_track(kick, 808, enable=False)` and redo the sidechain by hand.
- Never call unknown no-argument API functions as probes (e.g. `general.undoUp` performs an undo).
