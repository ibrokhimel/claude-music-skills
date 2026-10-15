# Kick, bass and the low end: ownership, strategies, tuning apart, frequency rules, bass sound design

How the bass and kick share 20-250 Hz: who owns the sub, the three timing strategies, tuning them apart, sidechain basics, frequency and mono rules, phone translation and starting-point bass patches in FL's native synths.

## Contents
1. Who owns the sub
2. Kick-bass strategies K1 / K2 / K3
3. Tuning the kick and bass apart
4. Sidechain and ducking (summary)
5. Frequency map and low-end rules
6. Mono, stereo and phone translation
7. Bass sound design basics
8. Sources

## 1. Who owns the sub

Decide this before writing a note. One sub source per step: 808, kick tail or sub bass **(convention)**.

| Situation | Sub owner (~30-60 Hz) | Kick's job | Bass/808's job |
|---|---|---|---|
| Long 808 or sine sub (trap, drill, phonk, R&B, DnB, dubstep) | Bass/808 | Short, punchy: ~60-100 Hz punch plus 2-5 kHz click; high-pass ~40-50 Hz if layered on 808 hits | Owns the fundamental |
| Long boomy 4/4 club kick (house, techno) | Kick | Owns 40-80 Hz on the beat | Avoid downbeat steps (offbeat placement) or sit higher (high-pass the bass ~40-60 Hz, energy at 60-120 Hz) |
| Live/rock/pop band | Shared by time | Pulse (~50-80 Hz plus click) | Root 8ths ducked lightly, or complementary EQ |
| Jazz/neo-soul with upright | Bass | Pulse at 100-150 Hz, little sub **(sourced)** | 40-100 Hz |

Sourced facts behind the table: an acoustic kick's fundamental sits at roughly 40-80 Hz with "thickness" around 70 Hz; electric bass fundamentals reach almost 400 Hz; the kick's click lives at 3-5 kHz; bass gains audibility at 900 Hz-1.5 kHz **(sourced)**. The most contested bands are 40-60 Hz and 70-100 Hz **(sourced)**.

## 2. Kick-bass strategies

Pick ONE per section (verse and drop can differ) **(convention)**.

| Strategy | How | Fits | Needs |
|---|---|---|---|
| **K1 Lock** | Bass/808 notes start on the kick's steps | Trap/drill (808 = low end), pop/rock root 8ths, boom bap, phonk | Short kick, ducking, or layering option A/B/C (`808-guide.md` section 8) |
| **K2 Gaps** | Bass plays where the kick is silent | House offbeat 3/7/11/15, tech-house rolling, UKG, amapiano log drum, reggae | Little or no sidechain |
| **K3 Hybrid** | Shared hits, bass ducked 50-150 ms by sidechain so the kick transient wins, then swells | EDM, pop, future bass, synthwave | Sidechain: ratio 4:1+, attack 0-5 ms, release 80-200 ms, back to full level by the next 8th |

Examples:
```
K1 trap     Kick  X . . . | . . . x | . . x . | . . . .
            808   R - - - | - - - R | - - R - | - - - O
K2 house    Kick  X . . . | X . . . | X . . . | X . . .
            Bass  . . R - | . . R - | . . R - | . . R -
K3 EDM      Kick  X . . . | X . . . | X . . . | X . . .
            Bass  R - - - | R - - - | R - - - | R - - -   (each note ducked under its kick)
```

Rules:
- **Two long sub sources never overlap on the same step without ducking.** Their phase relationship changes on every hit and produces volume flutter **(convention)**.
- **The short element keys the sustained one** **(sourced)**: the kick triggers compression on the bass, never the reverse. The bass is the melodic foundation; the kick is only rhythm.
- **Fewer, well-placed 808 notes sound bigger** than busy patterns **(sourced)**. Start from "a hit under each kick plus 1-2 syncopated notes in the gaps" **(sourced)**.
- In drill the kick is NOT under every 808 note; kicks are pickups and phrase accents **(sourced)**.
- Jersey club and similar fast, kick-dense styles use short bass envelopes so the bass never overlaps the next kick **(sourced)**.

## 3. Tuning the kick and bass apart

Tune the kick so its fundamental does not coincide with the bass roots of the key, then EQ the two in a complementary way **(sourced)**.

Procedure:
1. Measure the kick's fundamental (the body tone after the click; tuner or spectrum), e.g. 52 Hz.
2. List the bass roots in Hz from `808-guide.md` section 2, e.g. G minor 808: G1 49.0, D#1 38.9, F1 43.7.
3. If the kick lands within about a semitone of a frequent root, retune it to an **in-key, non-root** pitch: the 3rd or the 5th of the key, or the 2nd **(derived)**. G minor example: Bb = A#1, 58.3 Hz (b3), or A1 55.0 Hz (2nd), or D2 73.4 Hz (5th; punchier).
4. Retune with `fl_set_channel_pitch_pan_vol(kick_channel, volume, pan, pitch_cents)`. Cents = 1200 x log2(f_target / f_now). 52 Hz to 58.3 Hz is +197 cents (about +2 semitones). Pass the channel's current volume and pan (default 0.78, 0). If the pitch hits a limit, the channel's pitch range is smaller than the request; ask the user to retune in the Sampler instead.
5. Complementary EQ for the user to set (Fruity Parametric EQ 2) **(sourced example)**:
   - Kick-owns-sub template: kick +tight boost ~50 Hz, gentle cut 100-250 Hz; bass the opposite (cut ~50 Hz, keep 100-250 Hz).
   - 808-owns-sub template (trap): kick high-pass ~40-50 Hz, punch ~60-100 Hz, click 2-5 kHz; 808 small 2-4 dB notch at the kick's fundamental if not sidechaining **(convention)**.
6. Re-listen solo kick+bass at the drop. If the low end "flutters", it is a phase or overlap problem: shorten one, duck, or choose a different strategy.

## 4. Sidechain and ducking (summary; detail in `music-mix-master`)

- Classic: a compressor on the bass keyed from the kick, fast attack, fast-to-moderate release; depth sets how audible the pump is **(sourced)**.
- Surgical alternative: a sidechained dynamic EQ ducking only 40-80 Hz on the bass. It only helps if the kick has energy there **(sourced)**.
- FL stock starting point **(convention, from the mixing notes)**: Fruity Limiter in COMP mode on the 808/bass mixer track, SIDECHAIN = kick track. Ratio 2.5:1-4:1, attack 0-1 ms, release 50-150 ms, threshold for ~3-6 dB gain reduction on kick hits. Release must recover before the next 808 note: one 8th = 30000/BPM ms, so 214 ms at 140 BPM.
- For the EDM pump (K3): deeper reduction, 6-10 dB, release ~1/8 note.
- Routing is done by the user: select the kick's mixer track, right-click the bass track's send arrow, choose "Sidechain to this track", then pick it in Fruity Limiter's SIDECHAIN menu **(sourced, Image-Line)**. Do NOT use `fl_route_track` for this: it creates an audio route, which would sum the kick into the bass bus.
- Fruity Peak Controller on the kick linked to the bass volume is volume-automation ducking: a precise pump shape, no ratio **(sourced)**.

## 5. Frequency map and low-end rules

| Band | Hz | What lives there |
|---|---|---|
| Sub | ~20-60 | Felt more than heard; 808 and sub fundamentals. Keep controlled and mono **(sourced)**. |
| Contested 1 | 40-60 | Kick vs 808 fundamentals **(sourced)** |
| Contested 2 | 70-100 | "Round bass", kick thickness **(sourced)** |
| Low end overall | 20-250, main energy 20-160 | Kick, bass **(sourced)** |
| Mud zone | 200-400 | Bass harmonics + low pads/piano/guitar pile up **(convention)** |
| Low-mids | 250-500 | Body of everything else **(sourced)** |
| Bass presence | 900 Hz-1.5 kHz | Where the bass line is "heard" in a dense mix **(sourced)** |
| Kick click | 3-5 kHz | Attack **(sourced)** |

Rules:
- High-pass ~20-30 Hz and below on bass-heavy elements to save headroom **(sourced)**. The 808's lowest notes (MIDI 24 = 32.7 Hz) set how low that filter can go. Keep it below the lowest note's fundamental.
- Cutting around 300 Hz on the bass lets mid instruments come forward **(sourced)**.
- Chord instruments' lowest notes at or above ~C3 (MIDI 48, 130.8 Hz) when the bass is active, or high-pass them ~150-250 Hz **(convention)**. Voicing rules are in `music-chords-voicing`; register slotting is in `music-arrangement`.
- Register guardrails: 808 notes MIDI 24-40, root zone 26-38 **(derived)**; synth/electric bass MIDI 28-52 **(derived)**.

## 6. Mono, stereo and phone translation

- Keep the bass mono below roughly **100-150 Hz**. Phones and clubs are effectively mono, stereo lows cancel, and directionality is not perceived there **(sourced)**. Width (chorus, unison, Haas) only goes on a high-passed mid layer above ~120-150 Hz **(sourced)**.
- Bass, 808 and kick are panned centre **(convention)**.
- **Missing fundamental:** the ear infers a pitch from its harmonic series even when the fundamental is absent, so small speakers can imply low notes they cannot play **(sourced)**.
- Small speakers roll off hard below ~150-200 Hz **(sourced)**. A pure sine at 41 Hz (E1) is near-silent on a phone. The same line with harmonics at 82 and 124 Hz plus some 300-1000 Hz content is clearly audible **(derived)**.
- So: **always pair a sine sub with either saturation or a mid-bass layer** **(derived)**. Recipes are in `808-guide.md` section 9 (808) and section 7 below (synth bass).
- Phone check before delivery: if the bass line disappears on a phone or laptop speaker, add drive or the mid layer; don't just turn the sub up.

## 7. Bass sound design basics

Waveforms **(sourced)**: sine = fundamental only (clean sub); triangle = fundamental plus weak odd harmonics (slightly more audible sub); square = odd harmonics only (hollow, retro); saw = all harmonics (bright, filterable, the base of most mid basses).

Starting patches **(convention; tune by ear)**:

| Patch | Recipe | Use |
|---|---|---|
| Sub | Sine (or triangle), amp attack 0-5 ms, sustain 100%, release 30-80 ms (no clicks), mono, low-pass ~100-150 Hz | Under any mid bass; DnB, dubstep, R&B |
| Pluck bass | Saw (or saw+square), low-pass ~200-400 Hz, low-moderate resonance, high filter-envelope amount, decay 100-300 ms, sustain 0-20%, velocity to cutoff | House offbeat, tech house, synthwave, UKG |
| Layered bass | Layer 1: sine sub, low-passed ~100 Hz, mono. Layer 2: saw/square/reese, high-passed ~100-150 Hz, may be wide or distorted. Same MIDI and lengths, identical mono/porta settings. | Pop, EDM, trap with melodic bass |
| Reese | 2 saws detuned about +/-25 cents, low-pass with slow movement, over a separate sine sub **(sourced detune)** | DnB, future garage |
| Wobble | Saw/square mid bass, filter cutoff on a tempo-synced LFO (1/4, 1/8, 1/8T, 1/16) **(sourced)**, separate sine sub | Dubstep |
| Synth 808 | Sine with a +12 to +24 semitone pitch envelope dropping over 20-60 ms (the knock), amp decay 0.5-3 s, then saturation | When no good 808 sample is available |
| Log drum | Fruity DX10 log-drum preset **(sourced)**, or synth kick + sine + marimba layer with a fast pitch drop; soft clip | Amapiano |
| Upright | Sine+triangle or a sampled bass, low-pass ~800 Hz, soft attack, short release, slight pitch drift | Lo-fi, jazz |

FL quick bass in 3x Osc **(convention)**: Osc 1 sine at 0 (sub), Osc 2 saw at 0 coarse with slight fine detune, Osc 3 square at -12 semitones, low volume. Then Channel settings > Miscellaneous functions > Mono (+ Porta for glides). 3x Osc, FLEX, Sytrus, GMS and the Sampler are FL-native, so FL's Mono/Porta/Slide work on them; VST/AU synths need their own glide settings **(sourced)**.

Distortion order **(convention)**: saturate the mid layer, or the band above ~100 Hz, rather than the whole sub. Then low-pass the distortion ~2-5 kHz to avoid fizz. FL stock options: Fruity Blood Overdrive, Fruity Fast Dist, Fruity WaveShaper, Fruity Soft Clipper, Distructor (verify names in FL 21). Plugin settings are for the user to dial in; see `music-mix-master`.

## 8. Sources

- Sonarworks, kick vs bass competition (kick 40-80 Hz, bass to ~400 Hz, tuning apart, complementary EQ, click 3-5 kHz, presence 900 Hz-1.5 kHz, sidechain basics): https://www.sonarworks.com/blog/learn/eliminate-competition-between-the-kick-and-bass
- iZotope, 7 tips for mixing the low end (short element keys sustained, contested 40-60 / 70-100 Hz, 20-250 Hz, HPF 20-30 Hz, cut ~300 Hz): https://www.izotope.com/en/learn/7-tips-for-mixing-the-low-end
- McDSP, sidechain kick and bass (dynamic EQ 40-80 Hz): https://mcdsp.com/2021/12/08/011-sidechain-kick-and-bass/
- Violet Recording, 808 patterns (hit under each kick + gaps; fewer notes bigger), mix low end (sub 20-60 Hz felt, mono): https://violetrecording.com/how-to-make-808-patterns/ ; https://violetrecording.com/how-to-mix-low-end/
- Future Proof Music School and Mastering The Mix (mono below ~100-150 Hz): https://futureproofmusicschool.com/blog/how-do-i-preserve-mono-low-end-while-adding-stereo-width-to-highs ; https://www.masteringthemix.com/blogs/learn/how-to-add-width-to-bass-without-losing-mono-compatibility
- Wikipedia, Missing fundamental: https://en.wikipedia.org/wiki/Missing_fundamental
- Beat Kitchen, oscillators (waveform harmonics): https://beatkitchen.io/guides/synthesist/02-oscillators/
- Image-Line manual: Fruity Limiter sidechain, Fruity Peak Controller, Channel settings Misc (via `mixing_sound_design.md` and `bass_and_808.md`).
- Beatstorapon, drill (kicks not under every 808) and Jersey club (short bass envelopes): https://beatstorapon.com/blog/how-to-make-a-drill-beat/ ; https://beatstorapon.com/blog/how-to-make-a-jersey-club-beat/
- Sidechain ms values and patch numbers are inferences; no cited source gave them.
