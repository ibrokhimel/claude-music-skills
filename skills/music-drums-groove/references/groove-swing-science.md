# Groove, swing and rhythm science

Rhythm fundamentals, the groove research and the rules it implies, swing math (MPC/Linn scale, ticks, ms), FL Studio's swing implementation, sourced genre swing values, humanization and velocity bands.

## Contents
1. Rhythm fundamentals on the 16-step grid
2. The groove research (studies and findings)
3. Rules that follow from the research
4. Measuring syncopation: a quick budget
5. Timing math (ms per step, ticks per ms)
6. Swing: Linn scale, formula, tables
7. Swing in FL Studio
8. Sourced and default genre swing values
9. Humanization: systematic, not random
10. Velocity bands
11. Sources

---

## 1. Rhythm fundamentals on the 16-step grid

**Subdivisions in a 4/4 bar (PPQ 96; derived):**

| Subdivision | Hits/bar | Steps | Ticks apart | FL snap |
|---|---|---|---|---|
| Quarter | 4 | 1, 5, 9, 13 | 96 | 1 beat |
| 8th | 8 | odd steps | 48 | 1/2 beat |
| 8th offbeats ("&") | 4 | 3, 7, 11, 15 | — | — |
| 16th | 16 | all | 24 | 1/4 beat |
| "e" / "a" 16ths | 8 | e = 2, 6, 10, 14; a = 4, 8, 12, 16 | — | — |
| 8th triplet | 12 | off-grid | 32 | 1/3 beat |
| 16th triplet ("1/24") | 24 | off-grid | 16 | 1/6 beat |
| 32nd | 32 | off-grid | 12 | 1/8 beat |
| 64th | 64 | off-grid | 6 | 1/16 beat |

Triplets and 32nds do not fit the 16-step sequencer: deliver them as MIDI.

**Downbeat / backbeat / offbeat.** Downbeats = beats 1 and 3 (steps 1, 9). Backbeat = beats 2 and 4 (steps 5, 13), the snare/clap anchor in most styles (sourced, Wikipedia: Backbeat). Offbeats = the "&" 8ths (3, 7, 11, 15) — house open hats, reggaeton hats, trance open hats.

**Half-time / double-time.** Half-time moves the snare to beat 3 only (step 9) so quarter notes feel like 8ths in one giant bar (sourced, Wikipedia: Half-time). A 140 BPM trap/drill beat is felt at 70; both numbers are "right" (sourced, Tracklib). 140 lets vocalists switch between half- and double-time flows (sourced, Audeobox). Double-time energy = hats on every 16th (or 32nd rolls) over the same skeleton.

**Syncopation** = "a shift of rhythmic emphasis from metrically strong to metrically weak beats" (sourced, Witek 2014). Witek's index (after Longuet-Higgins & Lee, adapted to drum kits) counts e.g. a snare on a weak position followed by a kick on a strong one as a syncopation.

**Tresillo (3+3+2).** Dotted-8th, dotted-8th, 8th (or 3+3+2 sixteenths), found across Africa and from Morocco to Indonesia (sourced, Wikipedia: Tresillo). Grid forms (derived):
- Half-bar tresillo: steps 1, 4, 7 (repeat 9, 12, 15) — drill hats (NI: hats on 1, 4, 7 "give us a basic tresillo"), phonk cowbell, Brazilian funk kicks.
- Displaced half-bar: steps 4, 7, (9) / 12, 15, (1) — the dembow snare (4, 7, 12, 15).
- Full-bar over 8ths: steps 1, 7, 13.
- Extended 4-4-3-3-2: steps 1, 5, 9, 12, 15 — the Jersey club kick.
- Son clave 3-2: steps 1, 4, 7 | 11, 13.

**Polyrhythm** = two conflicting rhythms at once, e.g. 3 against 4 (sourced, Wikipedia). On the grid (derived): 8th-note triplets against 8th hats = 3:2 per beat; a figure every 3 steps (1, 4, 7, 10, 13, 16) against the quarter-note kick = 3:4 that resolves each bar. **Polymeter**: give one channel a 12-step pattern against a 16-step kick and it realigns every 3 bars (FL channel pattern length is settable 1–512 steps — sourced, Image-Line manual; set in the UI, the MCP tool writes up to 64 steps). Use polymeter on one percussion layer at most.

**Tempo preference.** DJ BPM lists (>70,000 pieces) and tapping data cluster at 115–127 BPM, peaking near 125; preferred range ~67–150 (sourced, Moelants 2002 via Frontiers 2022). Half-time and double-time feels keep a ~2 Hz pulse available in slower and faster genres.

---

## 2. The groove research

| Study | Design | Finding |
|---|---|---|
| Janata, Tomic & Haberman 2012 (J Exp Psych: General) | Groove ratings + movement | Groove = urge to move + positive affect; listeners agree on what grooves; better sensorimotor coupling predicts felt groove. |
| **Witek et al. 2014** (PLOS ONE) | 66 web participants, 50 synthesized funk breaks, 120 BPM | **Medium syncopation** gives the most wanting-to-move and pleasure: inverted U (R² = .347 move, .427 pleasure, p < .001). Dance-lovers rated higher. Audio entropy was a poor predictor. Medium syncopation keeps the meter predictable while violating expectations; the body "fills in" the missing beat. |
| Madison et al. (as reported by Witek 2014) | Groove ratings | Beat salience and event density correlate positively with groove; microtiming had no effect. |
| **Senn et al. 2018** (PLOS ONE) | 248 reconstructed drum patterns, 665 participants, 8,329 ratings | **Syncopation and event density predict groove positively**; beat salience, residual microtiming and rhythmic variability had no effect. Familiarity with the pattern raised ratings. |
| Matthews et al. 2019 (PLOS ONE) | Rhythm × harmony complexity | Rhythm complexity follows an inverted U; strongest with **medium-complexity chords**; harmony mainly drives pleasure. |
| **Davies et al. 2013** (Music Perception) | Jazz/funk/samba, microtiming 0 to ~2× natural | **Quantized versions rated highest**; systematic microtiming lowered groove, liking and naturalness — except the simple short-long jazz shuffle. Frühauf et al. 2013 agree. |
| **Senn et al. 2016** (Frontiers) | Swing and funk recordings, microtiming scaled; 79 experts, 81 non-experts | A "high groove zone" runs from fully quantized to the original performance timing (slightly beyond); exaggerated microtiming lowers ratings; experts are more sensitive. |
| Kilchenmann & Senn 2015 (Frontiers) | Body-movement measure | Experts moved less to quantized/near-quantized clips than to a "tight" 60%-reduced microtiming level. At 80% reduction, deviations spanned about −13/+17 ms (swing) and −9/+12 ms (funk). |
| Lenc et al. 2018 (PNAS) | EEG | Rhythms in low tones (130 Hz) produce stronger neural tracking at the beat frequency than the same rhythms in high tones (1236.8 Hz), especially when syncopated. |
| Hove et al. 2014 (PNAS) | Two simultaneous tone streams | Timing deviations are detected better in the lower stream and tapping follows the lower stream (cochlear origin); across cultures rhythm tends to be low, melody high. |
| Huron, ITPRA (Sweet Anticipation) | Theory | Accurate predictions are rewarded; surprises get a fast negative reaction that slower appraisal can turn pleasant. Syncopation and skipped beats before drops exploit this. |

Contested: beat salience (Madison positive vs Senn 2018 null); microtiming (Davies/Senn ratings vs Kilchenmann movement). The defensible synthesis is below.

---

## 3. Rules that follow from the research

1. **Anchor, then syncopate (Witek; Senn 2018).** Keep 2–4 anchors on strong positions (kick on 1, snare on the backbeat or beat 3) and move 1–3 hits off the grid's strong positions per bar (kick on 8, 11, 15 or "and" of 2; ghost snare on 10, 16). No anchor on 1 = too much; nothing off-grid = too little. (derived)
2. **Density in the top, clarity in the bottom (Senn 2018; Madison; Lenc; Hove).** Event density raises groove: run 16th hats/shakers or 8ths with ghosts. Low frequencies carry the beat: the kick and bass must be clear, uncluttered and tightly timed.
3. **Quantize by default (Davies; Senn 2016).** Fully quantized is inside the high-groove zone and never penalized. Swing is a structured, consistent ratio, not jitter.
4. **Humanize systematically, within ±10–20 ms (Senn 2016; Kilchenmann).** Consistent offsets per element (snare late = laid back, hats early = pushing). Never random large offsets. Kick stays on the grid (Hove: timing errors are most audible low).
5. **Vary velocity more than timing (inference).** Accent patterns on hats and ghost notes on snares give life without breaking the beat.
6. **Familiar first (Senn 2018).** Genre-standard templates earn a familiarity bonus: start from the genre grid, then innovate on one layer.
7. **Balance complexity across dimensions (Matthews).** Busy syncopated drums want 7th-chord-level harmony, not dense jazz alterations; simple drums can carry richer harmony.
8. **Silence before impact (Huron).** A skipped beat or gap before a drop is a "safe surprise".

---

## 4. Measuring syncopation: a quick budget

A practical proxy (derived, not Witek's exact index). Per bar, on the kick + snare layers only:
- Count **anchors**: hits on 1, 5, 9, 13 that match the genre's skeleton.
- Count **syncopations**: hits on an "e", "&" or "a" step (2–4, 6–8, 10–12, 14–16) that are NOT followed by a hit on the next strong beat in the same layer, plus any strong beat the genre expects but leaves empty (e.g. drill bar 2 with no kick on 1).
- Target: 2–4 anchors and 1–3 syncopations per bar (medium). 0 syncopations = stiff; 4+ with fewer than 2 anchors = the meter collapses.

Examples: boom bap bar 1 (kick 1, 7, 9; snare 5, 13) = 4 anchors, 1 syncopation (7). Funk grid (kick 1, 3, 11, 14; snare 5, 13) = 3 anchors, 3 syncopations — top of the medium band. Four-on-the-floor house = 6 anchors, 0 syncopations in kick/snare: the syncopation lives in the rim, open hats and bass instead.

---

## 5. Timing math (derived)

One 16th = 15000 / BPM ms. One tick at PPQ 96 = 60000 / (BPM × 96) ms.

| BPM | 16th (ms) | 1 tick (ms) | 10 ms in ticks | 20 ms in ticks |
|---|---|---|---|---|
| 70 | 214.3 | 8.93 | 1.1 | 2.2 |
| 78 | 192.3 | 8.01 | 1.2 | 2.5 |
| 90 | 166.7 | 6.94 | 1.4 | 2.9 |
| 100 | 150.0 | 6.25 | 1.6 | 3.2 |
| 110 | 136.4 | 5.68 | 1.8 | 3.5 |
| 124 | 121.0 | 5.04 | 2.0 | 4.0 |
| 130 | 115.4 | 4.81 | 2.1 | 4.2 |
| 140 | 107.1 | 4.46 | 2.2 | 4.5 |
| 150 | 100.0 | 4.17 | 2.4 | 4.8 |
| 174 | 86.2 | 3.59 | 2.8 | 5.6 |

PPQ 96 is coarse: at 140 BPM one tick is ~4.5 ms, so ±10–20 ms = ±2–4 ticks. FL graph-editor Shift (100% ≈ one 16th): 10 ms at 90 BPM ≈ 6% Shift.

---

## 6. Swing: Linn scale, formula, tables

**Reference points (sourced, Roger Linn via Attack):** swing delays every second 16th inside each 8th (steps 2, 4, 6 … 16). 50% = straight; 66% = perfect triplet swing; 54% loosens straight-16th beats without sounding swung; at 90 BPM a groove can feel looser at 62% than at 66%; useful settings 50% to ~70%. In jazz, swing ratios run 1:1 to 3:1 and are wider at slow tempos, narrower at fast ones (sourced, Wikipedia: Swing).

**Formula (derived).** With swing S% at resolution R (R = 24 ticks for 16th swing, 48 for 8th swing), the second note of each pair moves from R to 2R × S/100:

`delay_ticks = 2R × (S − 50) / 100`

- 16th swing (R = 24): delay = 48 × (S − 50)/100.
- 8th swing (R = 48, delays the "&" 8ths 3, 7, 11, 15): delay = 96 × (S − 50)/100.

| MPC % | 16th-swing delay (ticks) | % of a 16th | ms @ 90 BPM | ms @ 140 BPM | 8th-swing delay (ticks) |
|---|---|---|---|---|---|
| 52 | 1.0 | 4 | 6.7 | 4.3 | 1.9 |
| 54 | 1.9 | 8 | 13.3 | 8.6 | 3.8 |
| 56 | 2.9 | 12 | 20.0 | 12.9 | 5.8 |
| 57 | 3.4 | 14 | 23.3 | 15.0 | 6.7 |
| 58 | 3.8 | 16 | 26.7 | 17.1 | 7.7 |
| 60 | 4.8 | 20 | 33.3 | 21.4 | 9.6 |
| 62 | 5.8 | 24 | 40.0 | 25.7 | 11.5 |
| 64 | 6.7 | 28 | 46.7 | 30.0 | 13.4 |
| 66 | 7.7 | 32 | 53.3 | 34.3 | 15.4 |
| 68 | 8.6 | 36 | 60.0 | 38.6 | 17.3 |
| 70 | 9.6 | 40 | 66.7 | 42.9 | 19.2 |
| 74 | 11.5 | 48 | 80.0 | 51.4 | 23.0 |

Round to whole ticks at PPQ 96; 66.7% = exactly 8 ticks (the 16th-triplet position 32 in each 48-tick 8th).

**Swing per element (sourced, Attack 90s boom bap).** Different elements can take different swing: MPC 3000 8th swing 57% on kick/snare, 16th swing 74% on hats. Swing the hats/percussion most, the kick least or not at all.

**Drums and bass together (sourced, Violet Recording).** Apply the same swing (about 8–15%, DAW scale) to drums and 808 so they move together. If MIDI is baked, apply the identical tick delay to bass notes on even 16ths.

**Tempo dependence.** Wider swing at slow tempos, narrower at fast (jazz, sourced); producer evidence is Linn's 90 BPM remark only.

---

## 7. Swing in FL Studio

- **Implementation (sourced, Image-Line manual):** Channel Rack swing holds odd 16ths (1, 3 … 15) and shifts even 16ths (2, 4 … 16). There is a **Global Swing** knob (0–100%) and a per-channel **Channel Swing** (Channel settings > Miscellaneous > Time). **A channel swings only if BOTH are > 0.**
- **Scale:** 0–100 knob, not MPC %. No verified mapping exists (gap in the research). Start low (~15–30% FL) and match by ear. Rough working guess (convention, unverified): MPC 57% ≈ FL 20–30%; MPC 62%+ ≈ FL 40–50%.
- **Scope:** the swing knob shapes step-sequencer steps. Notes delivered as MIDI files should carry their swing baked into the tick positions (use the formula above) — do not rely on the knob to swing piano-roll notes (convention; not verified for FL 21).
- **Per-step microtiming:** Channel Rack graph editor (Ctrl+K) has per-step Velocity, Release, Fine pitch (±100 cents), Pan, Mod X (cutoff), Mod Y (resonance) and **Shift** (start offset, 100% ≈ one 16th) (sourced). Shift is the step-sequencer way to make a late snare; it must be set by hand (no MCP API).
- **FL quantize-dialog swing** (used in Audeobox's lo-fi 20–30% and R&B 15–20%) is another FL-scale value; treat it like the knob: tune by ear.

---

## 8. Sourced and default genre swing values

Sourced (do not mix scales):

| Genre | Swing | Scale | Source |
|---|---|---|---|
| Chicago house, 120–125 BPM | 55–60% | MPC-style | Attack |
| Deep tech house, 125–130 BPM | 60–65% | MPC-style | Attack |
| Tech house, 123–126 BPM | 55–65% | MPC-style | Loopmasters/Attack (snippet) |
| UK garage, 124–132 BPM | 68/69 | MPC16 | Attack |
| Rolling 2-step, 122–128 BPM | 60–65% | MPC-style | Attack |
| Rolling techno, 131 BPM | 20% | DAW scale | Attack |
| 90s boom bap | 57% (8ths, kick/snare); 74% (16ths, hats) | MPC 3000 | Attack |
| Boom bap typical | 54–62% | MPC | violetrecording (summary) |
| Boom bap feel | 58–70% on 1/8 or 1/16 | SP-1200/MPC | The Drum Broker (summary) |
| Lo-fi | 20–30% | FL quantize | Audeobox |
| R&B | 15–20% | FL quantize | Audeobox |
| Drums + 808 together | 8–15% | shared DAW value | Violet Recording |

Defaults where no source exists (convention, MPC scale): trap, drill, rage, plugg, phonk, dubstep, future bass, hyperpop, trance, synthwave 50% (triplets programmed explicitly); techno 50–54%; DnB 52–55% on hats; funk 52–56%; afrobeats 52–56% (sourced: shakers swung, no number); amapiano 54–58%; deep house 55–62%; lo-fi ≈ 58–64%; R&B ≈ 55–58%.

---

## 9. Humanization: systematic, not random

Per-element offsets (convention, kept inside the ±10–20 ms research window):

| Element | Offset | Effect |
|---|---|---|
| Kick | 0 (on grid) | Keeps the low-end beat tight (Hove, Lenc) |
| Snare/clap | +5 to +15 ms late (lo-fi, R&B, boom bap, neo-soul up to +20) | Laid back, "behind the beat" |
| Clap layered on snare | +3 to +8 ms after the snare | Thickens without a flam (Attack: clap "a few ms late") |
| Closed hats | 0, or −3 to −8 ms early in driving styles | Push / urgency |
| Ghost notes | +0 to +10 ms | Relaxed |
| Percussion (shaker/conga) | swing instead of offsets | Bounce |

Velocity humanization: keep kicks and main snares near-constant (boom bap: "the pattern creates the groove, not the dynamics"); vary hats ±5–15 around an accent pattern; random jitter only on hats/shakers and never more than ±10. Ghost notes stay in 35–60.

---

## 10. Velocity bands

Convention, partly anchored to sourced genre figures. FL shows % (MIDI ≈ % × 1.27, derived).

| Element | MIDI velocity | FL % |
|---|---|---|
| Kick (main) | 100–120 (boom bap constant 115–125) | 79–94 |
| Kick (ghost/pickup) | 65–90 | 51–71 |
| Snare / clap (backbeat) | 105–127 | 83–100 |
| Ghost snare | 30–60 (drill 40–50% ≈ 51–64) | 24–47 |
| Rim (backbeat sub, afro/amapiano) | 80–90 | 63–71 |
| Closed hat 16ths: on-beat | ≈ 110 | 87 |
| Closed hat 16ths: "&" | ≈ 95 | 75 |
| Closed hat 16ths: "e"/"a" | 60–70 | 47–55 |
| Closed hat 8ths (trap/boom bap) | 95–100 / 70–80 alternating | — |
| Lo-fi 8th hats | ~89 / ~51 (70% / 40%) | sourced |
| R&B 16th hats | 8ths 89–102, between 38–64 | sourced |
| Open hat | 80–100 | 63–79 |
| Shaker | 50–80, accent on the offbeat (afrobeats cycle 60-40-70-40%) | — |
| Conga | accents ~114, ghosts 44–64 | sourced % |
| Crash | 100–120, step 1 of a new section | 79–94 |
| Ride | 80–95 | — |
| Roll notes | ramp 60 → 110, or alternate 110/70 | — |

---

## 11. Sources

- Witek, Clarke, Wallentin, Kringelbach & Vuust 2014, PLOS ONE: journals.plos.org/plosone/article?id=10.1371/journal.pone.0094446
- Senn et al. 2018, PLOS ONE: pmc.ncbi.nlm.nih.gov/articles/PMC6025871
- Senn et al. 2016, Frontiers: pmc.ncbi.nlm.nih.gov/articles/PMC5050221
- Kilchenmann & Senn 2015, Frontiers in Psychology: frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.01232/full
- Davies, Madison, Silva & Gouyon 2013, Music Perception: repositorio.inesctec.pt/handle/123456789/3901
- Matthews et al. 2019, PLOS ONE: pmc.ncbi.nlm.nih.gov/articles/PMC6328141
- Lenc, Keller, Varlet & Nozaradan 2018, PNAS 115(32): doi.org/10.1073/pnas.1801421115
- Hove, Marie, Bruce & Trainor 2014, PNAS: pmc.ncbi.nlm.nih.gov/articles/PMC4104866
- Janata, Tomic & Haberman 2012, J Exp Psych: General 141(1): zenodo.org/record/997607
- Moelants 2002 via Frontiers 2022: frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.952488/pdf
- Roger Linn on swing, Attack Magazine: attackmagazine.com/features/interview/roger-linn-swing-groove-magic-mpc-timing/
- Image-Line FL Studio manual, Channel Rack: image-line.com/fl-studio-learning/fl-studio-online-manual/html/channelrack.htm
- Wikipedia: Half-time, Tresillo, Polyrhythm, Swing (jazz performance style), Backbeat. Tracklib: drill beat. Audeobox: trap, lo-fi, R&B, boom bap. Violet Recording: 808 patterns.
