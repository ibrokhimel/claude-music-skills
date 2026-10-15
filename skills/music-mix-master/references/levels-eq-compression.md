# Levels, EQ and compression - deep reference

Gain staging numbers, static-balance method, per-instrument EQ lanes with Fruity Parametric EQ 2 recipes, and compression/sidechain setups with FL stock plugins.

## Contents
1. Gain staging
2. Static balance method
3. EQ regions and alternate maps
4. Per-instrument EQ lanes
5. Kick vs 808/bass carving
6. Fruity Parametric EQ 2 recipe format
7. Compression basics and per-element settings
8. Sidechain in FL: Fruity Limiter method
9. Sidechain in FL: Fruity Peak Controller method
10. Parallel compression
11. Sources

## 1. Gain staging

| Point | Target | Evidence |
|---|---|---|
| Plugin input sweet spot | −18 to −12 dBFS | sourced (Boris FX) |
| Insert average | about −18 dBFS | sourced (Imagineer) |
| Insert peaks | −12 to −6 dBFS | sourced (Imagineer) |
| Kick anchor in kick/bass music | peaks about −6 dBFS, everything mixed around it | forum-derived, treat as convention (Studio 11) |
| Mix print / master before mastering | peaks about −6 dBFS, no master-bus processing | sourced (Studio 11) |
| Mix loudness (one author) | about −20 LUFS | single-author preference (iZotope) |

Rules:
- Make headroom with source levels (channel volume, sampler gain) and insert faders. Keep the master fader at unity (0.8).
- If two anchors both peak at −6 dBFS the master will exceed −6 dBFS. In a dense beat, start the kick at −10 to −8 dBFS so the sum lands near −6 (derived).
- Gain stage before plugins and again after them: a compressor's makeup gain or a saturator can add 3–6 dB.
- FL's mixer is 32-bit float, so internal overs do not clip permanently, but exported fixed-point files and level-dependent plugins do.
- FL's mixer meters show sample peak. LUFS needs a loudness meter (Youlean Loudness Meter is free; verify whether the user's FL build has a native LUFS display before relying on it).
- Monitor at 75–85 dB SPL; check at very low volume - anything too loud jumps out (sourced: Sweetwater; Violet Recording).

## 2. Static balance method

1. Pull every insert fader down (or mute everything).
2. Loop the densest section (hook/drop).
3. Bring up the anchor: kick (hip-hop, trap, drill, EDM) or the lead vocal if a vocal exists.
4. Add the 808/bass to taste against the kick; decide which leads the low end.
5. Snare/clap, then lead/vocal, then music bed (chords, pads, counter-lines), then hats/perc/FX.
6. Pan as you go (pan map in `space-stereo-saturation.md`).
7. Faders, pan and polarity only. Aim to finish in about five minutes (sourced: iZotope). The point is a fast honest picture, not a final mix.
8. Low-volume check, then mono check.

Relative order (convention, no source gives dB offsets): kick ≈ 808 > snare/clap > lead/vocal > music bed > hats > perc/FX. Starting relative offsets that usually work (convention): snare 2–4 dB under kick peak; lead near snare; pads 4–8 dB under lead; hats clearly under snare.

## 3. EQ regions and alternate maps

| Region | iZotope range | Alternate (Mastering.com / Audient) | Character |
|---|---|---|---|
| Sub | 20–60 Hz | 20–60 Hz | foundation |
| Bass | 40–250 Hz | 60–200 Hz | body, warmth |
| Low-mids | 200–500 Hz | 200–600 Hz; mud 250–450 Hz | box, mud; too little = thin |
| Mids | 500 Hz–2 kHz | 600 Hz–3 kHz | presence, nasal, attack |
| Presence / upper mids | 2–8 kHz | 3–8 kHz; presence 4–6 kHz | clarity, harshness, aggression |
| Air | 8–12 kHz+ | 6–20 kHz | sparkle |

Boundaries are conventions, not standards. General rules (sourced, iZotope): cut before boost; high-pass anything that does not need low end; subtractive EQ generally sounds more natural.

## 4. Per-instrument EQ lanes

Frequencies with "(sourced)" are from the iZotope EQ cheat sheet; HPF points and dB amounts are convention - confirm by ear in context, never only soloed.

| Element | HPF | Cut | Boost | Notes |
|---|---|---|---|---|
| Kick | optional 25–30 Hz | box 200–500 Hz (sourced), 2–4 dB, Q 2–4 | low punch 60–80 Hz, knock 100–200 Hz, click 1–5 kHz (sourced), 1–3 dB wide | let the 808 own the sub in trap |
| 808 | optional 25–30 Hz | mud 300–500 Hz (sourced for bass); 2–4 dB notch at kick fundamental if not sidechaining | articulation 800 Hz–1 kHz (sourced for bass) - or get it from saturation | tune before EQ (`music-bass-808`) |
| Bass guitar / synth bass | 30–40 Hz | 300–500 Hz | 800 Hz–1 kHz | |
| Snare | below 80 Hz (sourced) | ring 400–700 Hz narrow (sourced) | body 150–250 Hz, attack 2–3.5 kHz (sourced) | snare often needs 2–4 kHz help to cut (Violet) |
| Clap | 100–150 Hz | 300–500 Hz if boxy | 1–3 kHz snap | |
| Hi-hats / cymbals | 200–400 Hz | harshness 3–7 kHz, sparingly (sourced) | 10 kHz+ shelf only if dull | |
| Percussion | 150–300 Hz | resonances | 2–5 kHz | |
| Lead / pluck / keys | 100–200 Hz | 200–500 Hz mud | 2–5 kHz presence, small | |
| Pads / chords | 100–200 Hz | dip 2–4 dB at 1–4 kHz for lead/vocal | air shelf if dull | complementary EQ |
| Vocal | 80–150 Hz (iZotope says up to 100–250 Hz) | nasal 500 Hz–1.2 kHz, harsh 5–8 kHz (sourced) | air 10 kHz+ (sourced) | |
| Reverb / delay return | 200–400 Hz | | | LPF 6–10 kHz |

Q guidance (convention): boosts wide (Q 0.7–1.4), 1–3 dB; resonance cuts narrow (Q 4–8); mud cuts moderate (Q 1–2).

Masking heuristic (convention): no more than about three elements should dominate 1–5 kHz at the same moment; if more do, cut or arrange (see `music-arrangement`).

## 5. Kick vs 808/bass carving

The bass is very present at 60–120 Hz and masks the kick (sourced, Mixelite). Options, in order of preference:

1. **Arrangement**: kick and 808 on different steps, or kick short and 808 long (`music-bass-808` covers lock/gap/hybrid strategies).
2. **Lane split** (sourced, Violet Recording): kick punch slightly higher, 808 owns the deep sub. Default (derived): 808 owns 40–60 Hz, kick punch 60–100 Hz, kick click 2–5 kHz.
3. **Notch**: if not sidechaining, cut the 808 2–4 dB, Q 2–3, at the kick's fundamental (find it with the Parametric EQ 2 analyzer while the kick plays solo).
4. **Sidechain**: kick ducks the 808 3–6 dB (sections 8–9).
5. **Tune**: kick and 808 fundamentals a few semitones apart avoid stacking on one frequency.

## 6. Fruity Parametric EQ 2 recipe format

Facts (sourced, Image-Line manual): 7 bands; band types Low Pass, Band Pass, High Pass, Notch, Low Shelf, Peaking, High Shelf; slopes −12 to −48 dB/oct for pass filters; analyzer 20 Hz–20 kHz with mid/side monitoring; Compare for A/B; Linear Phase mode (adds latency). Shift-click solos a band; Alt-click resets it.

Write recipes for the user one band per line:

```
Insert 4 "Hats" -> Fruity Parametric EQ 2
  Band 1: High Pass, 300 Hz, slope 24 dB/oct
  Band 5: Peaking, 5 kHz, -2 dB, Q 3   (only if harsh)
```

```
Insert 8 "Chords" -> Fruity Parametric EQ 2
  Band 1: High Pass, 150 Hz, 24 dB/oct
  Band 3: Peaking, 350 Hz, -2 dB, Q 1.5   (mud)
  Band 5: Peaking, 2.5 kHz, -3 dB, Q 1     (room for lead)
```

```
Insert 2 "808" -> Fruity Parametric EQ 2
  Band 1: High Pass, 28 Hz, 24 dB/oct      (rumble only)
  Band 3: Peaking, <kick fundamental>, -3 dB, Q 2.5   (if no sidechain)
```

Tell the user to sweep a narrow boost to find resonances, then cut at the found frequency; finish by A/B with Compare at matched level.

## 7. Compression basics and per-element settings

Attack sets how much transient passes before gain reduction (slower = punchier); release sets recovery and should breathe with the tempo. Fruity Limiter manual (sourced): first ~10 ms of a sound mostly forms the timbre impression; modes LIMIT, COMP, NOISE GATE; 0 ms attack recommended to avoid latency issues unless Plugin Delay Compensation is on; too-short release distorts; SUSTAIN is an RMS window 0–1000 ms; CEIL at +12 dB effectively bypasses the limiter stage; THRESH at 0 dB disables the compressor.

| Element | Ratio | Attack | Release | GR | Evidence |
|---|---|---|---|---|---|
| Kick | 4:1 (6–8:1 aggressive) | 10–20 ms | fast-medium, 50–100 ms | 2–4 dB | ratio/attack sourced (Music Guy Mixing) |
| Snare | 3–4:1 | 20–30 ms | fast | 2–4 dB | attack sourced |
| 808 | 2–4:1 | slow-ish, 10–30 ms | 100–200 ms | 2–4 dB | slow attack sourced (Violet); too fast = distortion |
| Lead / vocal | 3–4:1 | 5–15 ms | 50–150 ms | 3–6 dB | convention |
| Drum bus glue | 2:1 | 10–30 ms (slow) | 100–200 ms or tempo | 2–3 dB (max 5) | 2:1 and 2–5 dB sourced (Mastering.com) |
| Music bus glue | 1.5–2:1 | 20–30 ms | 100–200 ms | 1–2 dB | convention |

Fruity Limiter COMP line format for the user:

```
Insert 1 "Kick" -> Fruity Limiter, COMP tab: THRES -14 dB (until 2-4 dB GR on hits), RATIO 4:1, KNEE 0, ATT 15 ms, REL 80 ms, GAIN +2 dB
```

Threshold is always "lower until the GR meter shows X dB on the loud hits" - absolute threshold values depend on input level.

Release in ms tied to tempo (derived): 1/16 = 15000/BPM, 1/8 = 30000/BPM. At 140 BPM: 107 ms and 214 ms.

## 8. Sidechain in FL: Fruity Limiter method

Steps (sourced: Image-Line Fruity Limiter manual; Mixelite; confirmed on the user's FL 21):

1. Click the **kick** insert to select it (the selected track is the SOURCE).
2. On the **808** insert (the DESTINATION), right-click its send arrow at the bottom of the strip -> "Sidechain to this track". This makes a sidechain-only route (no audio is mixed in).
3. Load Fruity Limiter on the 808 insert, open the COMP tab.
4. Right-click the SIDECHAIN box -> choose the kick input by name. The box then shows the input's position in the list (e.g. 1), not the track number.
5. Settings: RATIO 2.5:1 to start (sourced, Slooply), ATT 0–1 ms, REL 50–150 ms (808 must recover before its next note; shorter at higher BPM), lower THRES until kick hits show 3–6 dB GR (convention).
6. Confirm ducking on the Limiter's display during playback. `mixer.getTrackPeaks` does not show compressor GR (tested).
7. Check the route direction with `mixer.getRouteSendActive(kick, 808)` via api_call (fl-mixer-procedure.md). Remove a wrong route with `mixer.setRouteTo(src, dst, 0)` or `fl_route_track(src, dst, enable=False)`.

Do not create this route with `fl_route_track`: it makes a full audio send and the kick's audio would play through the 808 chain.

Pumping music bus: same steps with the Music bus as destination; 6–10 dB GR, release about 1/8 note (30000/BPM ms) (convention).

Reference values from the user's own project (worked, 2026-10-16): Fruity Limiter on the 808 insert, comp threshold −24.3 dB, 4:1, attack 1 ms, release 111 ms, kick as sidechain.

## 9. Sidechain in FL: Fruity Peak Controller method

Volume automation driven by the kick's envelope (sourced, Image-Line Peak Controller manual). No lookahead, independent of ratio; gives a precise pump shape.

1. Load Fruity Peak Controller on the kick insert.
2. Raise Base; set Volume negative (range −200% to +200%) so kick peaks pull the target down.
3. Decay = return time to Base (start about 1/8 note); Tension = curve shape.
4. On the 808 insert fader (or a Fruity Balance on the 808 insert), right-click -> Link to controller -> Internal controller: Peak ctrl (Peak).
5. Optional "ghost kick": a duplicate kick channel on its own insert whose master route is removed (`fl_route_track(ghost, 0, enable=False)`), carrying the Peak Controller. It is silent but still drives the duck, so the duck pattern can differ from the audible kick (convention).

## 10. Parallel compression

Parallel compression blends a heavily compressed copy under the dry signal: impact without audible cymbal pumping (sourced, Scraps Audio).

1. Create insert "Drums Smash"; route the Drums bus to it (`fl_route_track(drums_bus, smash)`) in addition to its master route; Smash routes to Master.
2. Fruity Limiter COMP on Smash: 6–10:1, fast attack (0–5 ms), fast release (30–60 ms), 8–12 dB GR (convention).
3. Smash fader starts low (inaudible) and comes up until the drums feel denser, then back off slightly. Optionally high-pass Smash at 80–100 Hz to keep the kick sub clean.
4. Watch the master headroom: parallel paths add level.

## 11. Sources

- Boris FX gain staging cheat sheet: https://borisfx.com/blog/gain-staging-cheat-sheet/
- Imagineer gain staging: https://blog.imagineersystems.com/blog/gain-staging-cheat-sheet/
- Studio 11 Chicago, −6 dB headroom: https://mastering.studio11chicago.com/mastering-6db/
- iZotope static mix: https://www.izotope.com/en/learn/7-tips-for-a-balanced-static-mix.html
- iZotope EQ cheat sheet: https://www.izotope.com/en/learn/eq-cheat-sheet.html
- Mastering.com EQ: https://mastering.com/how-to-use-eq ; compression cheat sheet PDF: https://mastering.com/wp-content/uploads/2017/07/COMPRESSION-CHEAT-SHEET.pdf
- Audient frequency ranges: https://audient.com/tutorial/frequency-ranges-explained/
- Violet Recording (levels, 808s, low volume): https://violetrecording.com/how-to-balance-levels-in-a-mix/ ; https://violetrecording.com/how-to-mix-808s/ ; https://violetrecording.com/how-to-mix-at-low-volume/
- Sweetwater monitor volume: https://www.sweetwater.com/insync/monitor-volume-2/
- Music Guy Mixing drum compression: https://www.musicguymixing.com/?p=3896
- Scraps Audio drum compression: https://scrapsaudio.com/blogs/scraps-blog/mastering-drum-compression-your-complete-guide
- Mixelite sidechain in FL: https://mixelite.com/blog/top-3-ways-to-sidechain-in-fl-studio/
- Slooply Fruity Limiter sidechain: https://slooply.com/blog/how-to-sidechain-kick-and-bass-in-fl-studio-fruity-limiter-method/
- Image-Line manuals: Fruity Limiter, Fruity Peak Controller, Fruity Parametric EQ 2 (https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/)
