# Space, stereo and saturation - deep reference

Reverb/delay timing (full 70–160 BPM table), Reeverb 2 and Delay 3 send setups, pan map and width tools with mono-compatibility rules, 808 saturation layering and drum clipping.

## Contents
1. Tempo-synced times (70–160 BPM)
2. Reverb by role and Fruity Reeverb 2 setup
3. Delay and Fruity Delay 3 setup
4. Send levels and ducking the returns
5. Pan map
6. Width, mono compatibility and Haas
7. Saturation for 808s
8. Clipping and transient shaping
9. Sources

## 1. Tempo-synced times (70–160 BPM)

Formulas (sourced: Omni Calculator): quarter note ms = 60000/BPM. 1/8 = ÷2; dotted 1/8 = quarter × 0.75; 1/8 triplet = quarter ÷ 3; 1/16 = ÷4; 1/32 = ÷8; 1/64 = ÷16; bar = 240000/BPM. Dotted = ×1.5 of the plain value; triplet = ×2/3. Values below are derived and rounded to the nearest ms.

| BPM | 1/4 | 1/8 | dotted 1/8 | 1/8T | 1/16 | 1/32 | 1/64 | 1 bar |
|---|---|---|---|---|---|---|---|---|
| 70 | 857 | 429 | 643 | 286 | 214 | 107 | 54 | 3429 |
| 75 | 800 | 400 | 600 | 267 | 200 | 100 | 50 | 3200 |
| 80 | 750 | 375 | 563 | 250 | 188 | 94 | 47 | 3000 |
| 85 | 706 | 353 | 529 | 235 | 176 | 88 | 44 | 2824 |
| 90 | 667 | 333 | 500 | 222 | 167 | 83 | 42 | 2667 |
| 95 | 632 | 316 | 474 | 211 | 158 | 79 | 39 | 2526 |
| 100 | 600 | 300 | 450 | 200 | 150 | 75 | 38 | 2400 |
| 105 | 571 | 286 | 429 | 190 | 143 | 71 | 36 | 2286 |
| 110 | 545 | 273 | 409 | 182 | 136 | 68 | 34 | 2182 |
| 115 | 522 | 261 | 391 | 174 | 130 | 65 | 33 | 2087 |
| 120 | 500 | 250 | 375 | 167 | 125 | 63 | 31 | 2000 |
| 125 | 480 | 240 | 360 | 160 | 120 | 60 | 30 | 1920 |
| 128 | 469 | 234 | 352 | 156 | 117 | 59 | 29 | 1875 |
| 130 | 462 | 231 | 346 | 154 | 115 | 58 | 29 | 1846 |
| 135 | 444 | 222 | 333 | 148 | 111 | 56 | 28 | 1778 |
| 140 | 429 | 214 | 321 | 143 | 107 | 54 | 27 | 1714 |
| 145 | 414 | 207 | 310 | 138 | 103 | 52 | 26 | 1655 |
| 150 | 400 | 200 | 300 | 133 | 100 | 50 | 25 | 1600 |
| 155 | 387 | 194 | 290 | 129 | 97 | 48 | 24 | 1548 |
| 160 | 375 | 188 | 281 | 125 | 94 | 47 | 23 | 1500 |

Half-time feel: trap/drill at 140–160 BPM often feels like 70–80; a 1/4-note delay at 140 equals a 1/8 at 70. Pick delay values that match the felt pulse.

Pre-delay: 1/64 to 1/16 note keeps transients clear (sourced: Violet Recording reverb calculator). At 140 BPM that is 27–107 ms; small rooms want the low end of that range.

Decay: end by the next beat (tight) or the next bar (lush) (sourced). Total reverb time = pre-delay + decay (sourced: AnotherProducer). Example at 140 BPM, tight: pre-delay 27 ms, decay ≈ 429 − 27 ≈ 400 ms. Lush: decay ≈ 1714 − pre-delay.

## 2. Reverb by role and Fruity Reeverb 2 setup

Reverb types (convention; no primary source gave ranges):

| Type | Decay | Pre-delay | Use |
|---|---|---|---|
| Room | 0.3–0.8 s | 0–1/64 note | drums, percussion, glue |
| Plate | 1–2 s | 20–40 ms | snare, vocals, leads |
| Hall | 2–4 s+ | 1/32–1/16 note | pads, pluck tails, transitions, FX |

Fruity Reeverb 2 facts (sourced, Image-Line manual): pre-delay can be tempo-synced; small rooms want shorter decay; decay is measured to −60 dB; shorter decays for drums; low cut reduces rumble; on a send set **Dry 0%, Wet 100%**; reverb belongs on individual sources/sends, not the master.

Send setup lines for the user:

```
Insert 23 "Verb Short" -> Fruity Reeverb 2: Dry 0%, Wet (ER and reverb) 100%, Size small, Decay 0.6 s, Pre-delay 1/64 (sync), Low cut 300 Hz, High cut 8 kHz
Insert 24 "Verb Long"  -> Fruity Reeverb 2: Dry 0%, Wet 100%, Size large, Decay 2.5 s, Pre-delay 1/32 (sync), Low cut 400 Hz, High cut 7 kHz
```

Return EQ (convention): high-pass 200–400 Hz, low-pass 6–10 kHz, either inside Reeverb 2's cut controls or with Parametric EQ 2 after it.

Depth = lower level + less top end + more reverb. Front elements (lead vocal, snare, kick) get less send; background (pads, perc) more.

## 3. Delay and Fruity Delay 3 setup

Fruity Delay 3 facts (sourced, Image-Line manual): time 1–1000 ms or tempo-synced; Mono / Stereo / Ping Pong modes; feedback can exceed 100% (self-oscillation - avoid unless intended); per-echo LP/HP/BP filter; sine modulation 0–20 Hz for wow/flutter; diffusion smears echoes toward reverb; Tone helps prevent muddy repeats.

Defaults (convention):

| Use | Time | Feedback | Filter | Mode |
|---|---|---|---|---|
| Vocal/lead throw | 1/4 or dotted 1/8 | 20–35% | HP 300 Hz, LP 5–6 kHz | Ping Pong |
| Rhythmic pluck | dotted 1/8 | 25–40% | HP 250 Hz, LP 7 kHz | Stereo |
| Slap/thickener | 60–120 ms | 0–10% | HP 200 Hz | Mono |
| Snare/clap throw (end of phrase) | 1/8 or 1/4 | 30–50% | HP 400 Hz | Ping Pong |

```
Insert 25 "Delay" -> Fruity Delay 3: Dry 0 (send), Wet 100%, Time 3/16 synced (dotted 1/8), Feedback 30%, Mode Ping Pong, Filter LP 6 kHz + HP 300 Hz, Modulation off
```

## 4. Send levels and ducking the returns

- Start sends low and raise until the space is just audible in context, then back off 2–3 dB (convention).
- If a long reverb or delay clouds the lead/vocal, sidechain-duck the return from the vocal/lead track (Fruity Limiter COMP on the return, sidechain = lead, 3–6 dB GR, release about 1/8 note) (convention).
- Automate throws (one delayed word or snare hit at a phrase end) instead of constant heavy sends.

## 5. Pan map

`fl_set_track_pan` takes −1 (hard left) to +1 (hard right): 20% right = 0.20.

| Element | Pan | Evidence |
|---|---|---|
| Kick, 808/bass, snare/clap, lead vocal, main lead | 0 | sourced for sub; convention for the rest |
| Closed hats | ±0.10 to ±0.30 | convention |
| Open hat / ride | opposite side to closed hat, ±0.20 to ±0.35 | convention |
| Percussion, shakers | ±0.20 to ±0.50, alternate sides | convention |
| Doubled parts, layered chords | ±0.50 to ±1.00 | convention |
| Backing vocals | wide, symmetric pairs | convention |
| Pads/chords | stereo source at 0, lows mono | convention |
| Counter-melody vs lead | counter offset ±0.20 to ±0.40 | convention |

Balance the field: if hats go left, put a shaker or open hat right. Check that the stereo image is not lopsided with `fl_diagnose_mix` (flags L/R peak differences ≥ 3 dB).

## 6. Width, mono compatibility and Haas

- Sub is mono and centered; collapse the lowest band to mono and leave higher harmonics free (sourced: Violet Recording).
- Keep bass below about 100–120 Hz mono; add width only above a 100–150 Hz split (sourced: Future Proof; Mastering The Mix).
- When widening with M/S or short delays, high-pass the side signal at 100–150 Hz; short Haas delays on lows sum in phase on one side and out of phase on the other (sourced: Sound On Sound).
- Haas: a delayed copy of about 1–30 ms (some sources 5–40 ms) sounds very wide but is usually not mono-compatible (sourced: eMastered; Sound On Sound). Use on hats, plucks or backing parts only; never on kick, 808, bass, lead vocal.
- FL tools (from general FL knowledge; manuals not fetched - verify names in the user's build): mixer track Stereo Separation knob (narrows toward mono), Fruity Stereo Shaper (has a delay control for Haas), Fruity Stereo Enhancer (phase offset and pre-delay), Maximus per-band stereo separation (can narrow the low band; sourced).
- Mono check: temporarily set the master's Stereo Separation fully to mono (or use a mono utility) and listen for parts that vanish or thin out.

## 7. Saturation for 808s

Why: small speakers roll off hard below about 150–200 Hz, so a pure sine 808 disappears; saturation adds harmonics the ear uses to reconstruct the missing fundamental (sourced: Violet Recording). For a 49 Hz (G1, MIDI 31, FL: G2) 808 the 2nd–4th harmonics sit at 98, 147 and 196 Hz (derived).

Procedure:
1. Tune first (`music-bass-808`). Out-of-tune 808s read as mud or wobble.
2. Start with light drive and push until the 808 growls without fizzing (sourced).
3. Layer method (sourced: Violet Recording): clean sub layer + saturated layer; high-pass the saturated layer so its harmonics sit above the fundamental. In FL: duplicate the 808 channel to a second insert "808 Dirt", saturate it, Parametric EQ 2 high-pass at about 100–150 Hz (convention), blend under the clean 808.
4. Single-insert method: saturator on the 808 insert, then re-check level (saturation adds 2–6 dB).
5. Control dynamics: an 808 whose notes vary by about 6 dB will repeatedly hit the master limiter and duck the whole track (sourced: Violet Recording). Even out note levels (velocity, compression, clipping) before mastering.

FL stock saturators (names from general FL knowledge; verify behavior before quoting exact knob values):

| Plugin | Starting point (convention) |
|---|---|
| Fruity Limiter SAT knob | small amount on the 808 insert; listen for grit |
| Fruity WaveShaper | soft-clip curve preset (the user's project used "Soft clip 1"); adjust pre-gain for drive |
| Fruity Blood Overdrive | low PreAmp, mix to taste |
| Fruity Fast Dist | low drive, mix 30–50% |
| Fruity Soft Clipper | see section 8 |
| Maximus per-band SAT | saturate only the low band lightly |

## 8. Clipping and transient shaping

No primary source with numbers was found; all values are convention.

- Fruity Soft Clipper on the drum bus or on kick/snare: shave 1–3 dB of peaks to gain loudness with fewer artifacts than heavy compression. Instruction: raise input (or lower Threshold) until peaks are rounded, then match output level with Post gain; A/B at equal loudness; stop if it gets harsh.
- Soft Clipper on the 808 after saturation evens out note levels (helps the "6 dB variation" problem above).
- Transient shaping (Fruity Transient Processor or similar): attack up for punch, release down to tighten tails (e.g. shorten a booming kick tail that masks the 808).
- Never clip the master during mixing; clipping on the master is a mastering decision.

## 9. Sources

- Omni Calculator delay/reverb: https://www.omnicalculator.com/other/delay-reverb-times
- AnotherProducer calculator: https://anotherproducer.com/online-tools-for-musicians/delay-reverb-time-calculator
- Violet Recording reverb calculator: https://violetrecording.com/tools/reverb-calculator/
- Image-Line Fruity Reeverb 2 / Fruity Delay 3 / Maximus manuals: https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/
- Future Proof mono low end: https://futureproofmusicschool.com/blog/how-do-i-preserve-mono-low-end-while-adding-stereo-width-to-highs
- Mastering The Mix bass width: https://www.masteringthemix.com/blogs/learn/how-to-add-width-to-bass-without-losing-mono-compatibility
- Sound On Sound fake M/S: https://www.soundonsound.com/sound-advice/q-how-can-create-fake-ms-setup-mono-compatible
- eMastered Haas effect: https://emastered.com/blog/haas-effect
- Violet Recording 808s / mastering hip hop: https://violetrecording.com/how-to-make-808s-hit-harder/ ; https://violetrecording.com/how-to-mix-808s/ ; https://violetrecording.com/how-to-master-hip-hop/
