# Drums, Rhythm and Groove: How Kicks, Snares, Hats, Percussion and Cymbals Make a Beat Groove (FL Studio-oriented reference)

Notation used throughout (for the later skill):
- One bar of 4/4 = 16 steps (16th notes) = one FL Studio Channel Rack bar. Step map: beat 1 = step 1 ("1 e & a" = 1 2 3 4), beat 2 = 5-8, beat 3 = 9-12, beat 4 = 13-16. Offbeat 8ths ("&") = 3, 7, 11, 15. Second/fourth 16ths in each beat ("e"/"a") = even/odd: "e" = 2, 6, 10, 14; "a" = 4, 8, 12, 16.
- Grid symbols: `x` hit, `X` accent, `g` ghost (low velocity), `o` open hat, `r` roll, `.` rest. Bars of 4 steps separated by `|`.
- Velocities are MIDI 0-127. FL shows velocity as a percentage; MIDI ≈ % x 1.27 (conversion is arithmetic, not from a cited source).

---

## 1. Rhythm fundamentals (meter, subdivisions, downbeat/backbeat/offbeat, syncopation, half/double time, polyrhythm, tresillo)

### Takeaway
Nearly all beat genres covered here are 4/4, 16-step grids; feel is created by where accents fall relative to the strong beats (backbeat on 2 and 4, or beat 3 in half-time), by syncopation (emphasis moved to weak positions), and by cross-rhythms like the tresillo 3+3+2 that underpin dembow, drill hats, afrobeats and Jersey club kicks.

### Cited Findings
- Half-time feel: the snare moves from beats 2 and 4 to beat 3 of each bar, and quarter notes start to "sound like" eighth notes in one giant bar; the half-time shuffle is a common variant in hip-hop — [Wikipedia: Half-time](https://en.wikipedia.org/wiki/Half-time_(music))
- Drill/trap tempo is counted two ways: a 140 BPM session "feels closer to 70" when you nod to the snare, so guides list drill at 70 or 140 and both are right — [Tracklib: Drill beat](https://www.tracklib.com/blog/drill-beat)
- Half-time trap runs at 130-140 BPM with the snare on beat 3 instead of 2 and 4; 140 BPM lets vocalists switch between double-time and half-time flows — [Audeobox: Trap in FL Studio](https://www.audeobox.com/learn/fl-studio/how-to-make-trap-beats-in-fl-studio/)
- Trap is defined partly by "double-time, triple-time, and similarly divided hi-hats" over deep 808 kicks — [Wikipedia: Trap music](https://en.wikipedia.org/wiki/Trap_music)
- Tresillo can be written divisively (dotted-8th, dotted-8th, 8th in 2/4) or additively (3+3+2 sixteenths); it is found across Africa and from Morocco to Indonesia — [Wikipedia: Tresillo](https://en.wikipedia.org/wiki/Tresillo_(rhythm))
- In a 16-step grid, a hat on 16th steps 1, 4 and 7 "gives us a basic tresillo rhythm" (NI drill tutorial) — [Native Instruments: How to make a drill beat](https://blog.native-instruments.com/drill/)
- Dembow is a looped rhythm with a "bounce", built on a 3+3+2 (tresillo) cross-rhythm with slight syncopation on every other half-beat — [Wikipedia: Dembow](https://en.wikipedia.org/wiki/Dembow)
- Syncopation is "a shift of rhythmic emphasis from metrically strong to metrically weak beats"; Witek et al. measured it with an index modelled on Longuet-Higgins & Lee, adapted for drum kits (e.g., snare on a weak position followed by kick on a strong one counts as a syncopation) — [Witek et al. 2014, PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0094446)
- Swing ratios in jazz lie between 1:1 (straight) and 3:1 (dotted-8th + 16th, more accurately called "shuffle"); ratios tend to be wider at slow tempos and narrower at fast tempos — [Wikipedia: Swing time](https://en.wikipedia.org/wiki/Swing_(jazz_performance_style))
- FL Studio Channel Rack pattern length can be set from 1 to 512 steps (one 16th to 64 bars in 4/4) — [Image-Line FL Studio manual: Channel Rack](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/channelrack.htm)
- Polyrhythm is the simultaneous use of two or more conflicting rhythms (e.g., 3 against 4) — [Wikipedia: Polyrhythm](https://en.wikipedia.org/wiki/Polyrhythm)

### Inferences
- Subdivision cheat sheet for a 16-step bar (arithmetic): quarter notes = steps 1,5,9,13; 8th offbeats = 3,7,11,15; all 8ths = odd steps; 16ths = all steps; 8th-note triplets = 12 per bar and 16th-note triplets = 24 per bar (do NOT fit the 16-step grid; use the piano roll). 32nds = 32 per bar (piano roll).
- In FL piano roll Snap terms (FL convention, not from a fetched source): 1/4 beat = 16th, 1/2 beat = 8th, 1/3 beat = 8th triplet, 1/6 beat = 16th triplet ("1/24" rolls), 1/8 beat = 32nd.
- Tresillo in a 16-step bar: half-bar version on steps 1, 4, 7 (repeat at 9, 12, 15); full-bar 3+3+2 over 8th notes = steps 1, 7, 13. The 3-3-3-3-4 / 3-3-2 groupings generate most "bounce" patterns below.
- 3-over-4 polymeter in a 16-step grid: a 3-step or 6-step repeating figure (e.g., hits on 1, 4, 7, 10, 13, 16) drifts against the 4-step beat; FL lets each channel's pattern be a different length, so a 12-step perc loop against a 16-step kick creates polymeter over 3 bars.
- Half-time vs double-time in FL: the same 140 BPM project with snare on step 9 = half-time feel (perceived 70); snare on 5 and 13 = "normal"; hats on every step = double-time energy layer.

### Gaps
- No primary academic source fetched on meter theory itself; definitions rely on Wikipedia and producer guides.

---

## 2. Role of each drum element

### Takeaway
Kick = pulse and low-end foundation (and in trap/drill, the 808 doubles as kick+bass); snare/clap = the backbeat anchor (2 and 4, or 3 in half-time); hats/shakers = timekeeping and subdivision energy; open hats = offbeat lift; ghost notes and percussion = in-between motion; crashes/rides = section markers.

### Cited Findings
- Boom bap is literally named for its two anchors: the "boom" (deep round kick) and the "bap" (tight snapping snare); everything else serves them — [Audeobox: Boom bap](https://www.audeobox.com/learn/fl-studio/how-to-make-boom-bap-beats-in-fl-studio/)
- Four-on-the-floor = bass drum on every quarter note, the core of disco/house/dance music — [Wikipedia: Four on the floor](https://en.wikipedia.org/wiki/Four_on_the_floor_(music))
- A ghost note has rhythmic value but no discernible pitch/very low volume; in drumming it is a quiet in-between snare stroke — [Wikipedia: Ghost note](https://en.wikipedia.org/wiki/Ghost_note)
- Drill: snare on beat 3 of each bar in half-time feel is "non-negotiable"; an optional ghost snare on the "and" of 4 at 40-50% velocity adds movement; layer snare with a short clap panned slightly for width — [Audeobox: Drill in FL Studio](https://www.audeobox.com/learn/fl-studio/how-to-make-drill-beats-in-fl-studio/)
- Afrobeats builds upward from layered interlocking percussion rather than kick-snare: five core elements are shaker (continuous 16ths, constant motion), open hat (offbeat accents), clave/woodblock (defines the groove), congas/bongos (syncopated accents, "human energy") and log drum (tuned melodic percussion), each in its own frequency and rhythmic space — [Audeobox: Afrobeats in FL Studio](https://www.audeobox.com/learn/fl-studio/how-to-make-afrobeats-in-fl-studio/)
- In amapiano a continuous shaker/hi-hat loop "runs without pause," filling gaps between log drum hits for rolling momentum — [RouteNote: Amapiano beat guide](https://create.routenote.com/blog/beatmakers-guide-how-to-make-an-amapiano-beat/) (via search summary); [Beatstorapon: Amapiano](https://beatstorapon.com/blog/how-to-make-amapiano-beat/)
- Trap mix hierarchy: 808 is the reference level (~-8 dB fader), kick punches through it with sidechain ducking of the 808, snare/clap matched in energy to kick, hats sit lower (high-pass around 500 Hz) as texture — [Audeobox: Trap](https://www.audeobox.com/learn/fl-studio/how-to-make-trap-beats-in-fl-studio/)
- Drill 808s are melodic and rhythmically tied to the kick: 808 notes land on or just after kick hits — [Audeobox: Drill](https://www.audeobox.com/learn/fl-studio/how-to-make-drill-beats-in-fl-studio/)
- Dubstep can propel a sparse half-time kit (implied 71 BPM) with a sub-bass running a four-to-the-floor 142 BPM pattern — i.e., bass can carry the pulse the kick omits — [Wikipedia: Dubstep](https://en.wikipedia.org/wiki/Dubstep)
- Chicago house percussion roles: tambourine on every offbeat (two detuned copies panned L/R), syncopated rimshot "around" tambourine and open-hat hits — [Attack Magazine: Beat Dissected 21st-century Chicago house](https://www.attackmagazine.com/technique/beat-dissected/21st-century-chicago-house/)
- In the Amen break, the drummer closes the 4-bar phrase with an early crash cymbal — crashes mark phrase/section boundaries — [Wikipedia: Amen break](https://en.wikipedia.org/wiki/Amen_break)

### Inferences
- Default velocity bands for programming (synthesised from the sourced numbers above plus common practice): kick 100-120; main snare/clap 105-127; ghost snare 30-60 (drill 40-50% = ~51-64 MIDI); closed hat main 8ths 80-100, in-between 16ths 40-65; open hat 80-100; shaker 50-80 with accent on the offbeat; crash 100-120 on step 1 of a new section.
- Crash on step 1 of bar 1 of each 8/16-bar section; ride on quarters or offbeats for a chorus energy lift; toms mainly in fills.

### Gaps
- No single authoritative source quantifying "standard" velocity ranges per drum; numbers above beyond the cited genre guides are practice-based.

---

## 3. How parts interlock (call-and-response, gap-filling, density, space, kick-bass lock)

### Takeaway
Good beats interlock rather than stack: the kick and snare trade positions (call and response), hats/percussion fill the gaps between them, the bass/808 locks to (or just after) the kick, and space is deliberately left — "build the remaining drums around the kick rather than over it."

### Cited Findings
- Jersey club: build other drums around the kick; delete closed-hat hits that duplicate kick transients; let some kick attacks stand alone without bass; keep bass envelope short so the running kick stays readable — [Beatstorapon: Jersey club beat](https://beatstorapon.com/blog/how-to-make-a-jersey-club-beat/)
- If the kick supplies sub, its tail must finish before the next important hit; if a separate 808 carries the lows, shorten/filter the kick's low tail rather than stacking two subs — [Beatstorapon: Jersey club](https://beatstorapon.com/blog/how-to-make-a-jersey-club-beat/) (via search summary)
- Trap: sidechain the 808 from the kick (e.g., Fruity Limiter on the 808 insert) so the 808 ducks when the kick hits — [Audeobox: Trap](https://www.audeobox.com/learn/fl-studio/how-to-make-trap-beats-in-fl-studio/)
- Afrobeats percussion layers interlock "into a groove greater than the sum of its parts"; each occupies its own frequency range and rhythmic space — [Audeobox: Afrobeats](https://www.audeobox.com/learn/fl-studio/how-to-make-afrobeats-in-fl-studio/)
- Avoid straight four-on-the-floor in afrobeats: kick on 1 plus a syncopated second hit on the "and" of 2 or just before 3 gives the forward lean — [Audeobox: Afrobeats](https://www.audeobox.com/learn/fl-studio/how-to-make-afrobeats-in-fl-studio/) (via search summary)
- Boom bap "demands restraint. Where trap stacks layers, boom bap strips back" — [Audeobox: Boom bap](https://www.audeobox.com/learn/fl-studio/how-to-make-boom-bap-beats-in-fl-studio/)
- Drill: "a top line … with more silence in it than notes" — space is part of the genre — [Tracklib: Drill beat](https://www.tracklib.com/blog/drill-beat)
- House: open 909 hat on the offbeat with length set "to ease into the clap without obscuring it" — [Attack Magazine](https://www.attackmagazine.com/technique/beat-dissected/21st-century-chicago-house/) (via search summary)
- Madison et al. found beat salience and event density (sub-beat variability) correlate positively with "wanting to move" ratings — clear beats plus busy subdivisions drive groove — reported in [Witek et al. 2014](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0094446)
- Mix order for Jersey club: kick, clap, bass, vocal chops, hats, melody — [Beatstorapon: Jersey club](https://beatstorapon.com/blog/how-to-make-a-jersey-club-beat/)

### Inferences
- Interlock rules for the skill: (1) never put kick and snare on the same step except as a deliberate accent; (2) a kick just before a snare (step 4 before 5, step 12 before 13, step 8 before 9) creates push; a kick just after (step 6, 14) creates bounce; (3) hats on steps the kick/snare occupy can drop velocity; (4) one "conversation" element (open hat, rim, perc) answers at the end of each 2-bar phrase; (5) 808/bass notes start on kick steps.
- Density layering: 3-4 rhythmic layers carry the groove; additional layers should differ in register (low/mid/high) and rhythm (quarters vs 8ths vs 16ths).

### Gaps
- No controlled research located on "kick-bass lock" timing specifically; guidance is from producer sources.

---

## 4. Groove and feel: swing, microtiming, velocity/humanization, the pocket, and groove research

### Takeaway
Groove is maximised by medium syncopation (Witek 2014) on a clear, dense beat; swing (delaying even 16ths, 50-70% in MPC terms) loosens the grid; microtiming helps only when subtle — research shows groove ratings stay high from quantized up to natural performance-level deviations but drop when deviations are exaggerated.

### Cited Findings
- Witek et al. 2014: web survey, 66 participants, 50 synthesized funk drum-breaks at 120 BPM in 4/4; medium syncopation elicited the most wanting-to-move and pleasure (inverted U; R² = .347 for wanting to move, .427 for pleasure, p < .001); people who enjoy dancing rated higher; audio entropy was a poor predictor — [Witek et al. 2014, PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0094446)
- Witek's explanation: medium syncopation gives enough predictability for the meter to be felt and enough complexity for expectations to be violated; syncopation is an "invitation" for the body to fill in the meter, the urge to move is the response and pleasure the result — [Witek et al. 2014](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0094446)
- Roger Linn's swing: delay every second 16th within each 8th (even steps 2, 4, 6…); 50% = no swing, 66% = perfect triplet swing; a 90 BPM swing groove feels looser at 62% than at 66%; for straight-16th beats 54% loosens the feel without sounding swung; useful settings lie between 50% and ~70% depending on beat and tempo — [Attack Magazine: Roger Linn on swing](https://www.attackmagazine.com/features/interview/roger-linn-swing-groove-magic-mpc-timing/)
- FL Studio Channel Rack swing: holds odd 16ths (1,3,5…15) and shifts even 16ths (2,4…16); Global Swing (0-100%) plus per-channel Channel Swing (Channel settings > Miscellaneous > Time); both must be >0 for a channel to swing — [Image-Line manual: Channel Rack](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/channelrack.htm)
- FL step graph editor (Ctrl+K) per-step parameters: Velocity, Release, Fine pitch (±100 cents), Pan, Mod X (filter cutoff), Mod Y (resonance), Shift (start offset; 100% ≈ one 16th) — Shift is the per-step microtiming tool — [Image-Line manual: Channel Rack](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/channelrack.htm)
- Chicago house: 120-125 BPM at 55-60% swing; swing on the rimshot "dramatically affects groove" — [Attack Magazine: 21st-century Chicago house](https://www.attackmagazine.com/technique/beat-dissected/21st-century-chicago-house/)
- Genre swing/velocity recipes using FL's Quantize-dialog swing (a different scale from MPC %): lo-fi 8th hats at 40-70% velocity alternating, swing 20-30%; R&B 16th hats with 8ths at 70-80% and in-between 16ths at 30-50%, open hat on "and" of 2 at 65%, swing 15-20% — [Audeobox: Lo-fi](https://www.audeobox.com/learn/fl-studio/how-to-make-lofi-beats-in-fl-studio/); [Audeobox: R&B](https://www.audeobox.com/learn/fl-studio/how-to-make-rnb-beats-in-fl-studio/)
- Boom bap kicks keep consistent velocity (90-100%) — "the pattern creates the groove, not the dynamics"; drum feel is swing-heavy, emulating MPC quantization — [Audeobox: Boom bap](https://www.audeobox.com/learn/fl-studio/how-to-make-boom-bap-beats-in-fl-studio/)
- J Dilla used the MPC with real-time, unquantized rhythms, producing a "drunk", "laid-back" style — [Wikipedia: J Dilla](https://en.wikipedia.org/wiki/J_Dilla)
- Senn et al. 2016: swing and funk rhythm-section recordings with microtiming scaled to several magnitudes; 79 expert and 81 non-expert listeners; a "high groove zone" ran from fully quantized to the original performance timing (and slightly beyond), while exaggerated microtiming lowered ratings; experts were more sensitive — [Senn et al. 2016, Frontiers/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5050221)
- Davies et al. 2013 and Frühauf et al. 2013 found quantized versions rated highest; Davies concluded "microtiming does not increase groove" — reported in [Senn et al. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5050221) and [Kilchenmann & Senn 2015](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.01232/full); also [Witek 2014](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0094446) notes microtiming decreased liking/desire to move in Davies
- Kilchenmann & Senn 2015 (body-movement measure): expert listeners' entrainment dropped for quantized/near-quantized clips versus a "tight" 60%-reduced microtiming level; at 80% reduction the deviation range was about −13/+17 ms (swing) and −9/+12 ms (funk) — i.e., tiny natural deviations may help experts' movement — [Frontiers in Psychology 2015](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.01232/full)
- Madison: microtiming showed no effect on groove ratings while beat salience and event density did — [Witek 2014 citing Madison et al.](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0094446)

### Inferences
- Practical microtiming rule: keep deviations small (roughly within ±10-20 ms, consistent with the near-original ranges above) and systematic (e.g., snare consistently late = laid back; hats slightly early = pushing). Random large offsets reduce groove.
- ms per step math: one 16th = 15000 / BPM ms (e.g., 90 BPM → 166.7 ms; 140 BPM → 107 ms). So 10 ms at 90 BPM ≈ 6% of a 16th; in FL graph-editor Shift (100% ≈ one 16th) that is about +6%.
- Swing defaults (MPC-style %): straight-but-loose 52-54%; house 55-60%; boom bap/lo-fi 58-64%; UK garage/2-step 60-66%; trap/drill hats mostly straight (triplets programmed explicitly) — house value is sourced (Attack), the rest are inferences from Linn's range.
- Humanization: vary hat velocity ±5-15 around an accent pattern (loud on 8ths, soft on in-between 16ths) rather than randomizing everything; keep kicks/snares near-constant.
- Medium syncopation in practice: keep 2-4 anchors on strong positions (kick on step 1, snare on backbeat) and move 1-3 hits off-grid (kick on step 8, 11 or 15; ghost snare on 10 or 16). Fully syncopated (no anchor on 1) or fully on-grid both reduce groove per Witek's inverted U.

### Gaps
- Janata, Tomic & Haberman 2012 (J Exp Psychol Gen; PubMed 21668108) could not be fetched (PubMed blocked by a cookie wall); its groove definition and sensorimotor-coupling findings are therefore not cited here.
- No official Image-Line documentation was found that maps FL's 0-100% Channel Rack swing to MPC-style 50-75% values; tune by ear.
- Tempo-dependence of swing ratio is sourced only for jazz (Wikipedia); no producer-music study found.

---

## 5. Hi-hat techniques (8th vs 16th, rolls, triplets, pitch, open/closed choke, velocity)

### Takeaway
Hats set the energy level: 8ths = relaxed (boom bap, lo-fi, rock), 16ths = driving (R&B, house, trap verses), with velocity accents on 8ths; trap/drill add rolls at 1/32 and triplet subdivisions plus pitch moves; open hats on offbeats give lift and should be choked by the closed hat.

### Cited Findings
- Trap hats are "double-time, triple-time, and similarly divided" — [Wikipedia: Trap music](https://en.wikipedia.org/wiki/Trap_music)
- UK drill hats: triplet rolls, swung/bouncy; Chicago drill straighter/simpler; Brooklyn/NY fast aggressive rolls — [Tracklib](https://www.tracklib.com/blog/drill-beat); [Audeobox: Drill](https://www.audeobox.com/learn/fl-studio/how-to-make-drill-beats-in-fl-studio/)
- NI drill hat recipe (146 BPM): bar 1 hats on 16th steps 1, 4, 7 at velocity 100, second hat lowered to 87, repeated on the next two beats (9, 12, 15), extra hat on step 16 at velocity 52; bar 2 repeats without the step-16 hat — [Native Instruments: Drill](https://blog.native-instruments.com/drill/)
- Drill hats: start from 8ths, then add triplets, rolls and velocity variation to make them organic — [eMastered: How to make a drill beat](https://emastered.com/blog/how-to-make-a-drill-beat)
- Hats should sit low in the mix with a high-pass ~500 Hz in trap — [Audeobox: Trap](https://www.audeobox.com/learn/fl-studio/how-to-make-trap-beats-in-fl-studio/)
- House: 16th closed hats with varying velocity; open hat placement can go beyond offbeats; set open-hat envelope to tempo and optionally use a choke group — [Attack Magazine: Chicago house](https://www.attackmagazine.com/technique/beat-dissected/21st-century-chicago-house/)
- FL graph editor Fine pitch per step (±100 cents) allows pitched hat rolls directly in the step sequencer — [Image-Line manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/channelrack.htm)
- Lo-fi: 8th hats, alternating 40-70% velocity; R&B: 16ths with 70-80% on 8ths and 30-50% between — [Audeobox: Lo-fi](https://www.audeobox.com/learn/fl-studio/how-to-make-lofi-beats-in-fl-studio/); [Audeobox: R&B](https://www.audeobox.com/learn/fl-studio/how-to-make-rnb-beats-in-fl-studio/)

### Inferences
- Trap hat template (140 BPM, half-time): base 8ths (odd steps) or 16ths; every 1-2 bars replace one beat with a roll: 1/32 roll (8 hits in a beat), 16th-triplet roll (6 per beat, FL snap 1/6 beat), or 8th-triplet (3 per beat, snap 1/3 beat). Place rolls on beat 4 leading into the next bar, or on beat 2 leading into the snare on 3.
- Roll velocity shapes: crescendo (60→110), decrescendo, or alternating 110/70. Pitch shapes: ramp +1 to +12 semitones over the roll (piano roll notes or step Fine pitch ±100 cents for subtle tilt).
- Open/closed choke: put open hat and closed hat in the same cut group (FL channel settings "Cut"/"Cut by" — FL feature, not from fetched source) so a closed hat silences the ringing open hat.
- Velocity accent pattern for 16th hats (default): steps on beats 110, "&" 95, "e"/"a" 60-70.

### Gaps
- No source found giving canonical trap hat roll placement statistics; templates above are practice-based.

---

## 6. Fills and transitions (snare rolls, fills every 4/8 bars, drops, build-ups)

### Takeaway
Arrangements move in 4/8/16-bar phrases; mark phrase ends with a short fill (changed last beat, extra snares/toms, early crash) and mark sections by adding/removing elements — e.g., removing the kick for a breakdown or drop tension.

### Cited Findings
- Amen break structure (four bars, ~7 s): two bars of the main beat, bar 3 delays a snare hit, bar 4 leaves beat 1 empty then plays a syncopated pattern and an early crash — a model 4-bar phrase with variation at the end — [Wikipedia: Amen break](https://en.wikipedia.org/wiki/Amen_break)
- DnB producers commonly switch between two breaks after each bar; the "Tramen" combines Amen, a James Brown break and an Alex Reece break — [Wikipedia: Drum and bass](https://en.wikipedia.org/wiki/Drum_and_bass)
- Jersey club arrangement: 8-bar sections with elements added/removed at phrase boundaries; one short fill into a hook or drop; for rap songs, thin the rhythm in verses and restore at hooks — [Beatstorapon: Jersey club](https://beatstorapon.com/blog/how-to-make-a-jersey-club-beat/)
- Chicago house turnaround: an extra reduced-velocity kick on the final offbeat of the phrase — [Attack Magazine](https://www.attackmagazine.com/technique/beat-dissected/21st-century-chicago-house/)
- 909 snares and claps are handy for fills and builds — [Attack Magazine](https://www.attackmagazine.com/technique/beat-dissected/21st-century-chicago-house/) (via search summary)
- Drill: the bar-2 snare is often displaced relative to bar 1 (NI places bar 1 snare on beat 3, bar 2 snare on beat 4); producers judge whether the main snare feels early, centered or delayed across the two-bar phrase — [Native Instruments](https://blog.native-instruments.com/drill/); [Beatstorapon: Drill](https://beatstorapon.com/blog/how-to-make-a-drill-beat-bpm-808s-drums/)
- Afrobeats patterns often develop over 4-bar cycles — [Audeobox: Afrobeats](https://www.audeobox.com/learn/fl-studio/how-to-make-afrobeats-in-fl-studio/)

### Inferences
- Fill schedule: small variation at bar 4, bigger fill at bar 8, crash + full fill at bar 16.
- EDM build (8 bars): snare/clap on quarters (bars 1-4) → 8ths (5-6) → 16ths (7) → 32nds or 16th triplets (8), velocity ramp 60→120, plus high-pass filter sweep on drums; last beat empty before the drop.
- Drops/breakdowns: remove kick (and 808) for 4-8 bars, keep hats/perc; re-enter with crash + kick on step 1.
- Hip-hop fills: mute the kick for the last beat or half-bar before the hook; add a snare/808 stutter or reverse cymbal into step 1.

### Gaps
- No quantitative source on how often fills occur in contemporary productions.

---

## 7. Concrete 16-step genre patterns (with BPM, swing, velocities)

### Takeaway
Each genre is identifiable from its kick/snare skeleton plus one signature layer (offbeat open hat, triplet hats, tresillo perc, 5-kick run, log drum, cowbell). Sourced elements are cited; patterns marked (practice) are standard textbook conventions not verified against a fetched source.

### Cited Findings (genre facts and sourced patterns)
- House/Chicago house: 120-125 BPM, 55-60% swing, four-on-the-floor kick, 16th closed hats with varying velocity, offbeat open hat/tambourine, layered 909+707 clap, syncopated rim — [Attack Magazine](https://www.attackmagazine.com/technique/beat-dissected/21st-century-chicago-house/). Classic house: kick on quarters, open hat on all offbeat 8ths, closed hat on quarters — [MusicRadar: Beat building classic house](https://www.musicradar.com/news/beat-building-how-to-make-classic-house) (via search summary)
- Trap: 130-160 BPM, 140 standard; half-time snare on beat 3 — [Audeobox: Trap](https://www.audeobox.com/learn/fl-studio/how-to-make-trap-beats-in-fl-studio/)
- Drill tempos: UK 140-144, Chicago 130-140, Brooklyn 140-150 (Tracklib); UK 140-143, NY 140-145, Chicago 135-145 (Audeobox); UK = long controlled 808 slides, swing-heavy with off-beat kicks; NY = heavier distortion, harder, less swing — [Tracklib](https://www.tracklib.com/blog/drill-beat); [Audeobox](https://www.audeobox.com/learn/fl-studio/how-to-make-drill-beats-in-fl-studio/)
- NI drill pattern (146 BPM, 2 bars): kick bar 1 steps 1 and 8; bar 2 steps 1, 4, 7, 15 (last at vel 96); snare bar 1 step 9, bar 2 step 13; hats as in section 5 — [Native Instruments](https://blog.native-instruments.com/drill/)
- Drill 808: C minor or G minor common; slides between notes a minor 3rd or perfect 4th apart, usually upward; 2-3 slides per 4-bar phrase; let some notes sustain a full beat; in FL right-click note → Slide — [Audeobox: Drill](https://www.audeobox.com/learn/fl-studio/how-to-make-drill-beats-in-fl-studio/)
- Boom bap: 85-95 BPM; kick on 1, "and" of 2, sometimes 3, and "and"/"e" of 4 (ghost kick); kicks 90-100% velocity; MPC-style swing — [Audeobox: Boom bap](https://www.audeobox.com/learn/fl-studio/how-to-make-boom-bap-beats-in-fl-studio/)
- Lo-fi: 70-90 BPM (78 typical), snap rarely finer than 1/16, 8th hats 40-70% velocity, swing 20-30% (FL quantize) — [Audeobox: Lo-fi](https://www.audeobox.com/learn/fl-studio/how-to-make-lofi-beats-in-fl-studio/)
- R&B hats as in section 4/5 — [Audeobox: R&B](https://www.audeobox.com/learn/fl-studio/how-to-make-rnb-beats-in-fl-studio/)
- Reggaeton/dembow: 3+3+2 cross-rhythm, derived from Jamaican "boom-ch-boom-chick" riddims (Steely & Clevie's 1989 "Fish Market"/Pocoman Jam, used in Shabba Ranks' 1990 "Dem Bow") — [Wikipedia: Dembow](https://en.wikipedia.org/wiki/Dembow)
- Afrobeats: 95-115 BPM (105-110 common, 108 a versatile default); kick on 1 + syncopated second kick ("and" of 2 or just before 3); soft backbeat on 2 and 4 (rim, soft clap, or clap+snare); continuous 16th shaker; offbeat open hat; clave; congas; 4-bar cycles — [Audeobox: Afrobeats](https://www.audeobox.com/learn/fl-studio/how-to-make-afrobeats-in-fl-studio/)
- Amapiano: emerged in Pretoria/Johannesburg townships in the 2010s, broke out ~2019; around 110 BPM (NI tutorial at 114, kick on every beat) — [Native Instruments: Amapiano](https://blog.native-instruments.com/amapiano-music/); 108-115 BPM, 112 a reliable start; restrained four-on-the-floor; constant 16th shaker + offbeat open hat; log drum syncopated with pitch variation for bounce; rims/congas — [Beatstorapon](https://beatstorapon.com/blog/how-to-make-amapiano-beat/); [RouteNote](https://create.routenote.com/blog/beatmakers-guide-how-to-make-an-amapiano-beat/) (via search summary). "Private school" amapiano uses shakers and mellow log drums — [Wikipedia: Amapiano](https://en.wikipedia.org/wiki/Amapiano)
- Drum & bass: 160-180 BPM, mostly 170-180 since ~1996 (mid-170s hallmark); early forms ~130 (1990-91) then 155-165 (1993); syncopated breakbeats are the defining element — [Wikipedia: Drum and bass](https://en.wikipedia.org/wiki/Drum_and_bass)
- Dubstep: sparse kick/snare/hats, half-time implied ~71 BPM over a 142 BPM grid — [Wikipedia: Dubstep](https://en.wikipedia.org/wiki/Dubstep)
- UK garage 2-step: the key change from speed garage was removing the 2nd and 4th kick of each bar; shuffled beats; kick ideas borrowed from dancehall/bashment ("conga rhythm") — [Wikipedia: UK garage](https://en.wikipedia.org/wiki/UK_garage); future garage 130-140 BPM — same source
- Jersey club: 130-140 BPM (start 140), straight 16th grid; 5-kick skeleton on steps 1, 5, 9, 12, 15 (4-4-3-3-2); stable clap backbeat; restrained hats; bed-squeak sample (from Trillville's "Some Cut", 2004) as percussion — [Beatstorapon: Jersey club](https://beatstorapon.com/blog/how-to-make-a-jersey-club-beat/); triplet kick patterns and chopped samples also described — [Wikipedia: Jersey club](https://en.wikipedia.org/wiki/Jersey_club)
- Phonk: draws on Memphis rap (DJ Screw, Three 6 Mafia, Tommy Wright III, DJ Spanish Fly); "drift phonk" (late 2010s, Russia) = faster tempos, prominent TR-808 cowbell patterns, aggressive distorted bass — [Wikipedia: Phonk](https://en.wikipedia.org/wiki/Phonk)
- Breakbeat: nu skool breaks ~130-140 BPM — [Wikipedia: Drum and bass](https://en.wikipedia.org/wiki/Drum_and_bass)
- Amen break: 4-bar break from The Winstons' "Amen, Brother" (drummer Gregory Coleman) — [Wikipedia: Amen break](https://en.wikipedia.org/wiki/Amen_break)
- Funk ghost notes: low-volume in-between snare strokes — [Wikipedia: Ghost note](https://en.wikipedia.org/wiki/Ghost_note); Witek's groove stimuli were funk drum-breaks — [Witek 2014](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0094446)

### Inferences — programmable grids
(Steps: `1 2 3 4 | 5 6 7 8 | 9 10 11 12 | 13 14 15 16`. Velocities in brackets. "(practice)" = convention, not verified from a fetched source.)

**Four-on-the-floor house** — 120-126 BPM, swing 55-60% (Attack)
```
Kick     X . . . | X . . . | X . . . | X . . .   [115-120]
Clap     . . . . | X . . . | . . . . | X . . .   [110]
ClHat    x x x x | x x x x | x x x x | x x x x   [beats 90, & 75, e/a 55]  (or omit on offbeats)
OpHat    . . o . | . . o . | . . o . | . . o .   [95]
Tamb     . . x . | . . x . | . . x . | . . x .   [70, two copies panned L/R]
Rim      . . . x | . . x . | . . . . | . x . .   [80] (syncopated, practice)
```
Turnaround: bar 4 add kick on step 15 at ~80.

**Techno** (practice) — 125-135 BPM, swing 50-54%
```
Kick     X . . . | X . . . | X . . . | X . . .   [127]
ClHat    . . x . | . . x . | . . x . | . . x .   [90]
16thHat  x x x x | x x x x | x x x x | x x x x   [70/45 alternating]
Clap     . . . . | x . . . | . . . . | x . . .   [100, optional]
Rumble   bass/reverb tail on steps 2-4, 6-8... ducked by kick
Ride     . . x . | . . x . | . . x . | . . x .   [85, peak sections]
```

**Trap (half-time, snare on 3)** — 130-160 BPM (140 default), swing 50% (triplets programmed explicitly)
```
Kick/808 X . . . | . . . x | . . x . | . . . .   [120] (practice; 808 notes start on kicks)
Snare+Clp. . . . | . . . . | X . . . | . . . .   [127]
Hat 8ths x . x . | x . x . | x . x . | x . r r   [100/75; step 15-16 = 1/32 or 1/6-beat roll]
OpHat    . . . . | . . . . | . . . . | . . . .   (occasional on step 7 or 15)
```
Bar 2 variation: kick on 1, 4, 11, 15; snare on 9 + ghost snare step 16 [~55].

**UK drill** — 140-144 BPM, 2-bar pattern (NI kick/snare/hat placement; bar-2 snare displacement)
```
Bar 1:
Kick     X . . . | . . . x | . . . . | . . . .   [100]
Snare    . . . . | . . . . | X . . . | . . . .   [100]
Hat      x . . x | . . x . | x . . x | . . x g   [100,87,100 | 100,87,100 | g=52]
Bar 2:
Kick     X . . x | . . x . | . . . . | . . x .   [100, step 15 = 96]
Snare    . . . . | . . . . | . . . . | X . . .   [100]
Hat      x . . x | . . x . | x . . x | . . x .
```
Add 16th-triplet hat rolls (snap 1/6 beat) on beat 2 or 4 every 2 bars; ghost snare on "and" of 4 (step 15) at ~55 (40-50%). 808: follows kick, 2-3 upward slides (minor 3rd / 4th) per 4 bars, C or G minor.

**NY / Brooklyn drill** — 140-150 BPM; same half-time snare skeleton (practice: snare on 9, bar-2 snare often shifted to step 12 or 14), harder distorted 808, faster aggressive hat rolls, less swing; perc/808 often on offbeat 16ths (steps 4, 7, 12, 15).

**Boom bap** — 85-95 BPM, swing ~56-62% (MPC-style; Linn range)
```
Kick     X . . . | . . x . | x . . . | . . x g   [95 all; g (step 16) ghost kick 70]  (Audeobox: 1, &2, sometimes 3, &4/e4)
Snare    . . . . | X . . . | . . . . | X . . .   [120]
Hat 8ths x . x . | x . x . | x . x . | x . x .   [95/70]
```
(Step 7 = "and" of 2; step 15 = "and" of 4; alternative ghost kick on step 14.)

**Lo-fi hip hop** — 70-90 BPM (78), swing ~58-64% MPC or 20-30% FL quantize
```
Kick     X . . . | . . . . | . . x . | . . . .   [100] (practice; sparse)
Snare/Rim. . . . | X . . . | . . . . | X . . .   [90-100, shift +3-8% late for lazy feel]
Hat 8ths x . x . | x . x . | x . x . | x . x .   [alternate ~89 / ~51  (70%/40%)]
```

**R&B** — practice tempo 60-100 BPM (half-time snare at faster tempos)
```
Kick     X . . . | . . . . | . x . . | . . . .   [100] (practice)
Snare    . . . . | X . . . | . . . . | X . . .   [105] + rim ghosts [40]
Hat 16ths x x x x | x x o x | x x x x | x x x x  [8ths 89-102 (70-80%); between 38-64 (30-50%); o step 7 = 83 (65%)]
```

**Pop** (practice) — 95-128 BPM
```
Kick     X . . . | . . . . | X . x . | . . . .   [110]
Clap/Snr . . . . | X . . . | . . . . | X . . .   [120]
Hat 8ths x . x . | x . x . | x . x . | x . x .   [90/70]
```

**Rock basic beat** — 90-140 BPM; backbeat on 2 and 4 ([Wikipedia: Beat/backbeat](https://en.wikipedia.org/wiki/Backbeat))
```
Kick     X . . . | . . . . | X . x . | . . . .   [115]
Snare    . . . . | X . . . | . . . . | X . . .   [120]
Hat 8ths x . x . | x . x . | x . x . | x . x .   [100/80]
Crash    X on step 1 of each section
```

**Funk with ghost notes** (practice) — 95-115 BPM, swing 52-56%
```
Kick     X . x . | . . . . | . . x . | . x . .   [110]
Snare    . . . . | X . . g | . g . . | X . . g   [X 120; g 35-50]
Hat 16ths x x x x | x x x x | x x x x | x x x x  [accents on 8ths]
```

**Reggaeton / dembow** — practice tempo 88-100 BPM
```
Kick     X . . . | X . . . | X . . . | X . . .   [115]
Snare    . . . x | . . x . | . . . x | . . x .   [110]  (steps 4,7,12,15 = 3+3+2 per half bar)
Hat      . . x . | . . x . | . . x . | . . x .   [80, optional]
```

**Afrobeats** — 105-110 BPM (108), slight swing 52-56% (practice)
```
Kick     X . . . | . . x . | . . . . | . . . .   [110]  (second kick &2 = step 7, or step 8 "just before 3")
Rim/Clap . . . . | x . . . | . . . . | x . . .   [85, soft backbeat]
Shaker   x x x x | x x x x | x x x x | x x x x   [accent & 85, others 55]
OpHat    . . o . | . . o . | . . o . | . . o .   [75]
Clave    x . . x | . . x . | . . x . | x . . .   [90]  (3-2 son clave steps 1,4,7,11,13 — practice)
Conga    . . . . | . x . x | . . . . | . x x .   [70-90, syncopated — practice]
```

**Amapiano** — 108-115 BPM (112-114), swing 54-58% (practice)
```
Kick     X . . . | X . . . | X . . . | X . . .   [95, "restrained"]
Shaker   x x x x | x x x x | x x x x | x x x x   [constant; accent offbeats]
OpHat    . . o . | . . o . | . . o . | . . o .   [80]
Clap/Rim . . . . | x . . . | . . . . | x . . x   [85] (practice)
LogDrum  x . . x | . . x . | . . x . | . x . .   [100, pitch moves on later hits — practice; often 1-2 bar melodic bass phrase]
```

**Drum & bass two-step** — 170-176 BPM (practice skeleton)
```
Kick     X . . . | . . . . | . . x . | . . . .   [120]
Snare    . . . . | X . . . | . . . . | X . . .   [127]
Hat      x . x . | x . x . | x . x . | x . x .   [80/60] + ghost snares [40] on 8, 15 (practice)
```
Amen-style break: chop/re-sequence a 4-bar break; vary bar 3 (delayed snare) and bar 4 (empty beat 1, syncopation, early crash).

**Dubstep (half-time)** — 138-142 BPM
```
Kick     X . . . | . . . . | . . . . | . . . .   [127] (+ optional kick step 11 or 15)
Snare    . . . . | . . . . | X . . . | . . . .   [127]
Hat      . . x . | . . x . | . . x . | . . x .   [70, sparse]
```

**UK garage 2-step** — 130-138 BPM, heavy swing ~60-66% (practice)
```
Kick     X . . . | . . . . | . . x . | . . . .   [115]  (2nd/4th quarter kicks removed — Wikipedia)
Snare/Clp. . . . | X . . . | . . . . | X . . .   [110]
Hat      . . x . | . . x x | . . x . | . . x x   [90/60, shuffled]
Rim      . . . x | . . . . | . . . x | . x . .   [70]
```

**Jersey club** — 130-140 BPM (140), straight grid (Beatstorapon)
```
Kick     X . . . | X . . . | X . . X | . . X .   [120]  (1,5,9,12,15 = 4-4-3-3-2)
Clap     . . . . | X . . . | . . . . | X . . .   [110]  (stable backbeat)
BedSqueak/Chop on/between kicks, call-and-response with vocal chops
```

**Phonk / Memphis** (practice) — classic Memphis ~130-145 BPM half-time; drift phonk often faster
```
Kick/808 X . . . | . . . . | . . x . | . . . .   [120]
Snare/Clp. . . . | . . . . | X . . . | . . . .   [120]
Hat      x . x . | x . x . | x . x . | x x x x   [90]
Cowbell  x . . x | . . x . | x . . x | . . x .   [100, 808 cowbell melody, pitched in key — tresillo-based, practice]
```

**Breakbeat** — 130-140 BPM (nu skool breaks)
```
Kick     X . . . | . . . . | . . x . | . . . .   [115] (+ step 8 or 15 variants)
Snare    . . . . | X . . . | . . . . | X . . .   [120] + ghost [45] on 10, 16
Hat      x . x . | x . x . | x . x . | x . x .
```

### Gaps
- No fetched sources gave verified 16-step grids for techno, reggaeton tempo, pop, rock, funk, dubstep extra kicks, UK garage hat patterns, amapiano log drum note-by-note patterns, or phonk tempos; those grids are convention and should be checked by ear.
- MusicRadar, RouteNote and Beatstorapon-amapiano content was seen only via search summaries, not full fetch.
- No source fetched for the Amen break's original tempo.

---

## 8. Drum sound choice, layering and tuning

### Takeaway
Choose sounds by role and frequency space: layer clap+snare for snap and width, use short kicks when a separate 808 carries the sub, sidechain 808 to kick, high-pass hats, and keep 808/log drums in the track's key.

### Cited Findings
- Drill: layer snare with a short clap panned slightly L or R for width without clutter — [Audeobox: Drill](https://www.audeobox.com/learn/fl-studio/how-to-make-drill-beats-in-fl-studio/); drill snares are sharp/snappy, optionally layered with a clap — [eMastered](https://emastered.com/blog/how-to-make-a-drill-beat)
- House: clap layered from 909 + 707 samples, saturated with low end cut; 707 kick tuned down — [Attack Magazine](https://www.attackmagazine.com/technique/beat-dissected/21st-century-chicago-house/)
- Jersey club: short hard kick readable across five attacks; shorten/filter kick tail if an 808 provides sub; mono bass so notes don't overlap — [Beatstorapon](https://beatstorapon.com/blog/how-to-make-a-jersey-club-beat/)
- Trap: 808 sidechained from kick; hats high-passed ~500 Hz — [Audeobox: Trap](https://www.audeobox.com/learn/fl-studio/how-to-make-trap-beats-in-fl-studio/)
- Drill 808s are written in the song's key (C or G minor most common) with slides — [Audeobox: Drill](https://www.audeobox.com/learn/fl-studio/how-to-make-drill-beats-in-fl-studio/)
- Afrobeats: layer percussion so each element has its own frequency range — [Audeobox: Afrobeats](https://www.audeobox.com/learn/fl-studio/how-to-make-afrobeats-in-fl-studio/)
- Boom bap texture: dusty, warm, bit-reduced, saturated, filtered highs — [Audeobox: Boom bap](https://www.audeobox.com/learn/fl-studio/how-to-make-boom-bap-beats-in-fl-studio/)
- FL step graph editor Fine pitch (±100 cents) per step and Mod X/Y (filter cutoff/resonance) allow tuning and tonal variation per hit — [Image-Line manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/channelrack.htm)

### Inferences
- Kick layering: sub/body layer (40-100 Hz) + click/top layer (2-5 kHz); align transients, high-pass the top layer, keep one sub only.
- Tune kick (and 808) fundamental to the song's root or fifth; tune snare body to a chord tone; in FL use channel pitch knob or piano-roll note.
- Converting Channel Rack steps to piano roll for detailed editing: per Image-Line, select all, snap none, discard note lengths (Shift+D) to keep step alignment — [Image-Line manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/channelrack.htm) (cited fact, placed here for workflow)

### Gaps
- No acoustic/psychoacoustic study fetched on drum tuning to key; guidance is practice-based.
- Frequency targets for kick layering not verified from a fetched source.
