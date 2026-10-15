# Bass Lines and 808s in Modern Production (for an FL Studio bass/808-writing skill)

Conventions used throughout: MIDI note 60 = C4 (scientific pitch). FL Studio labels MIDI 60 as "C5", so an FL label is always one octave number HIGHER than the scientific name (MIDI 36 = C2 scientific = "C3" in FL). 16-step grid = one 4/4 bar of 16th notes; steps 1, 5, 9, 13 are beats 1-4; steps 3, 7, 11, 15 are the 8th-note offbeats ("and"); even steps are the 16th "e"/"a" positions. At 96 PPQ (FL default) one step = 24 ticks, one beat = 96 ticks.

Note on sources: some genre how-tos found (Audeobox, Violet Recording, Beatstorapon) are producer blogs rather than primary pedagogy; they are useful for concrete FL workflow but their numbers are rules of thumb, not standards. Several fetches (MusicRadar kick/bass article, Attack Magazine pages 2-8) returned truncated content, so only the parts actually read are cited.

## 1. Role of bass: harmonic foundation and rhythmic link; note choice relative to chords

### Takeaway
The bass defines which chord the listener hears (its root) and glues drums to harmony; the safe default is root on every chord change and on strong beats, with 5ths/octaves as stable alternates and chromatic or scale approach tones used on weak beats to lead into the next root.

### Cited Findings
- In walking bass lines the root and 5th are the most important notes because they most strongly state each chord's tonality; the 5th is a stable stepping stone to the next root — [The Jazz Piano Site: Walking Bass-lines](https://www.thejazzpianosite.com/?p=483)
- Beats 1 and 3 (in 4/4) are harmonically most important because chords usually change there, so target the root or 5th on those beats — [The Jazz Piano Site](https://www.thejazzpianosite.com/?p=483)
- A basic walking-bass recipe: play the chord's triad (root-3rd-5th) on beats 1-3, then a chromatic approach note on beat 4 leading into the next chord's root from a half step above or below — [TalkingBass: Walking bass lines made easy](https://www.talkingbass.net/walking-bass-lines-made-easy/)
- Chord tones can be targeted with a double chromatic approach from above or a single chromatic approach from below — [Bass Musician Magazine](https://bassmusicianmagazine.com/?p=110823)
- The bass provides some rhythm but is also the melodic foundation, while the kick is essentially rhythmic only (this is iZotope's rationale for letting the kick trigger compression on the bass, not the reverse) — [iZotope: 7 tips for mixing the low end](https://www.izotope.com/en/learn/7-tips-for-mixing-the-low-end)
- In an off-beat house bass example, the bass supports chord changes while moving between only two notes — [Attack Magazine: Low-End Theory, eight bassline styles](https://www.attackmagazine.com/technique/tutorials/low-end-theory-exploring-eight-common-bassline-styles/)
- 808 lines should be built around the root of the progression and stay in the song's key; pitch movement is best kept mostly within an octave so the 808 stays in bass territory — [Violet Recording: How to make 808 patterns](https://violetrecording.com/how-to-make-808-patterns/)

### Inferences
Programmable note-choice rules (derived from the above plus standard practice; treat as defaults, not laws):
- R1 Root-on-change: on the first step of every new chord (usually step 1 of the bar, or step 9 for two chords per bar) play the chord ROOT in the bass register. This is what "defines" the chord: e.g. pads playing C-E-G-B over a bass A make the listener hear Am9, not Cmaj7. Never put a non-root under a chord change unless you intend a slash/inversion chord (e.g. C/E for a smooth descending line).
- R2 Interval priority for non-change notes (most to least stable): root > octave (+12) > 5th (+7) > 4th/b7 (+5 / +10, genre-dependent) > 3rd (+3 minor / +4 major) > other scale tones > chromatic tones. 3rds in the bass sound "melodic"/inverted; use them as passing notes or for deliberate first-inversion colour, not as a held note under a chord change.
- R3 Octave bounce: root + root+12 alternating is the safest way to add motion without adding harmonic information (disco, house, trap 808 slides).
- R4 Approach tone: on the last 8th or 16th before a chord change (step 15 or 16 of the bar), play a note a half step above or below the NEXT root (chromatic approach), or the next root's 5th (dominant approach), or a scale step adjacent to it (diatonic approach). Chromatic approach tones belong on weak steps only and should be short.
- R5 Pedal tone: hold or repeat one note (usually the tonic, sometimes the 5th) while chords change above it; creates tension/drone (common in techno, drill, trap intros, EDM builds). Works best when the chords above contain that note or resolve back to it.
- R6 Avoid doubling the 3rd low: a 3rd in the bass under a chord whose 3rd is also voiced low in the pads muddies the 100-300 Hz region; keep pads' lowest note at or above roughly C3 (MIDI 48) when bass is busy.
- R7 Walking pattern (4 quarter notes per chord, one chord per bar): steps 1/5/9/13 = root, 3rd or scale step, 5th, chromatic approach to next root.
- R8 For loop-based minor-key beats (trap/drill/lo-fi), the 808/bass usually follows chord roots, but an equally valid choice is a riff built from root, b3, 4, 5, b7 of the key (minor pentatonic) that implies the chords loosely.

### Gaps
- Could not access StudyBass or Scott's Bass Lessons pages directly in the tool budget; walking/approach-tone rules above come from TalkingBass, The Jazz Piano Site, Bass Musician Magazine.
- No quantitative source on how often professional pop bass lines play roots vs non-roots on chord changes.

## 2. Kick-bass relationship: locking vs gaps, sidechain, frequency ownership

### Takeaway
Decide per track which element owns the sub (the long 808/sub bass, or the kick), then separate them in time (bass in the kick's gaps, or sidechain ducking on shared hits) and/or in frequency (complementary EQ, tuning the kick so its fundamental differs from the bass roots).

### Cited Findings
- Acoustic kick fundamental sits roughly 40-80 Hz, with "thickness" peaking around 70 Hz; electric bass fundamentals reach up to almost 400 Hz — [Sonarworks: Eliminate competition between kick and bass](https://www.sonarworks.com/blog/learn/eliminate-competition-between-the-kick-and-bass)
- Where possible, tune the kick so its fundamental does not coincide with the bass roots of the song's key, then EQ each to make room — [Sonarworks](https://www.sonarworks.com/blog/learn/eliminate-competition-between-the-kick-and-bass)
- Complementary EQ example: kick boosted in a tight band around 50 Hz with a gentle cut at 100-250 Hz; do the opposite on the bass. In a jazz context the bass may own 40-100 Hz while the kick sits higher at 100-150 Hz (kick gives pulse, not low end) — [Sonarworks](https://www.sonarworks.com/blog/learn/eliminate-competition-between-the-kick-and-bass)
- Kick click lives around 3-5 kHz; bass benefits from a push near 900 Hz-1.5 kHz to cut through dense mixes — [Sonarworks](https://www.sonarworks.com/blog/learn/eliminate-competition-between-the-kick-and-bass)
- Classic sidechain: compressor on the bass keyed from the kick; bass ducks only when the kick plays; fast attack and fast-to-moderate release let the bass react and recover quickly; depth sets how audible the "pumping" is — [Sonarworks](https://www.sonarworks.com/blog/learn/eliminate-competition-between-the-kick-and-bass)
- More surgical alternative: sidechained dynamic/multiband EQ ducking only the band where the kick's fundamental lives (e.g. 40-80 Hz) — only useful if the kick actually has energy there — [McDSP: Sidechain kick and bass](https://mcdsp.com/2021/12/08/011-sidechain-kick-and-bass/)
- The short, punchy element (kick) should trigger compression on the sustained element (bass) — [iZotope](https://www.izotope.com/en/learn/7-tips-for-mixing-the-low-end)
- The most contested low-end real estate is roughly 40-60 Hz ("sub") and 70-100 Hz ("round bass") — [iZotope (via search summary)](https://www.izotope.com/en/learn/7-tips-for-mixing-the-low-end)
- For 808s: sidechain so the 808 ducks a few dB on each kick, or pick a kick and 808 occupying slightly different frequencies; foundational 808 move is a hit under each kick plus 1-2 syncopated notes in the gaps; fewer, well-placed notes sound bigger than busy patterns — [Violet Recording: 808 patterns](https://violetrecording.com/how-to-make-808-patterns/)
- Off-beat bass placed between four-on-the-floor kicks creates a call-and-response with the kick; Attack also shows LFO Tool (volume shaping) as a sidechain-style alternative — [Attack Magazine](https://www.attackmagazine.com/technique/tutorials/low-end-theory-exploring-eight-common-bassline-styles/); [The Producer School: hard house/trance bass](https://theproducerschool.com/blogs/featured-blogs/5-essential-bass-patterns-that-define-hard-house-and-trance-music)

### Inferences
Programmable kick/bass strategies (choose ONE per section):
- K1 LOCK (unison): bass/808 notes start on the same steps as the kick. Use when the 808 IS the kick's low end (trap, drill) or in rock/pop root 8ths. Requires either a short/clicky kick with little sub, or sidechain/ducking, or layering (see section 3).
- K2 GAPS (call-and-response): bass occupies steps where the kick is silent (house offbeat 3/7/11/15; garage; amapiano log drum between kicks). Minimal masking, maximum bounce; no heavy sidechain needed.
- K3 HYBRID: bass starts on the kick's step but its envelope is ducked for ~50-150 ms by sidechain so the kick transient wins, then swells (EDM/pop). Typical starting point (my inference, not from a cited source): ratio 4:1+, attack 0-5 ms, release 80-200 ms tuned so the bass is back at full level by the next 8th note.
- Sub ownership rule: if bass notes are long and sub-heavy (808, sine sub), the bass owns ~30-60 Hz and the kick should be shorter/higher (punch ~60-100 Hz plus click); if the kick is a long boomy 4/4 club kick, the bass should avoid the downbeat steps or be high-passed so its energy sits higher.
- Never let two long sub sources overlap on the same step without ducking; their phase relationship changes per hit and causes volume flutter.

### Gaps
- MusicRadar's kick/bass programming article could not be extracted (page truncated); no attack/release numbers for sidechain were found in a cited source — the ms figures above are my own defaults.

## 3. 808s specifically: tuning, safe range, glides, length, distortion, patterns, layering

### Takeaway
An 808 is a long-decay, near-sine tuned kick used as the bass instrument; tune the sample's root so every MIDI note lands in key, keep notes roughly in the ~30-80 Hz fundamental zone (about MIDI 24-40), play it monophonic with portamento for slides, and add saturation so harmonics carry it on small speakers.

### Cited Findings
- Trap's bass drums are tuned with a long decay so they emit a bass frequency, a technique originating with the Roland TR-808 — [Wikipedia: Trap music](https://en.wikipedia.org/wiki/Trap_music)
- An 808 is mostly sine-wave sub energy with a fundamental usually somewhere around 30-80 Hz depending on the note — [Amped Studio: 808 bass (search summary)](https://www.ampedstudio.com/blog/secrets-of-808-bass/)
- Raw 808 one-shots often are not tuned to a clean pitch; check the sample with a tuner or against a reference sine and correct it until the root reads true; then every note played from it is in tune and slides resolve cleanly — [Violet Recording: 808 slides](https://violetrecording.com/how-to-make-808-slides/)
- Most 808 samples default to C, so verify against the melody; set the 808 to the root of the progression — [Violet Recording: 808 patterns](https://violetrecording.com/how-to-make-808-patterns/)
- To tune, find the key's root frequency in Hz and pitch the 808 until its fundamental matches — [Music Production Wiki: 808 sub-bass tuner (search summary)](https://musicproductionwiki.com/tools/808-sub-bass-tuner)
- Slides: the instrument must be monophonic (one voice) with legato; overlapping note ends/starts make the pitch glide, separated notes retrigger. Start with a short glide time, lengthen until the travel is audible, then trim so the slide arrives on time; faster tempos want snappier glides. 1-2 semitone slides sound subtle/vocal, octave slides dramatic. Upward slides on accents build tension, downward slides give heavy resolution. Use slides as punctuation (turnarounds, lead-ins), roughly one or two per bar at most. Both start and target notes must be in key. The 808 sample needs enough sustain to carry the glide — [Violet Recording: 808 slides](https://violetrecording.com/how-to-make-808-slides/); [Violet Recording: 808 patterns](https://violetrecording.com/how-to-make-808-patterns/)
- Apply the same swing (about 8-15%) to drums and 808 so they move together — [Violet Recording: 808 patterns](https://violetrecording.com/how-to-make-808-patterns/)
- FL Studio Channel settings > Misc > Polyphony: "Mono" allows one voice and makes overlapping notes transition smoothly; "Porta" makes every new note slide from the previous one; the "Slide" knob sets glide time (further right = longer). Portamento/sliding of overlapping notes is NOT supported for VST/AU instruments (it works for FL native generators/samplers) — [Image-Line FL Studio manual: Channel settings Misc](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/chansettings_misc.htm)
- FL piano roll "slide notes": a slide note makes the note below/above it glide to the slide note's pitch; slide time is set by the slide note's length — [Image-Line FL Studio manual: Piano roll](https://flstudio.image-line.com/help/html/pianoroll.htm)
- FL trap workflow: Channel settings > Misc, enable Porta with slide around 40 (lower = faster), set Mono; draw a note, draw a second overlapping note, right-click it and choose Slide (triangle shape). A 1/16 overlap gives a tight slide, a full-beat overlap a slow bend; an octave slide is the signature trap sweep — [Audeobox: Trap beats in FL Studio](https://www.audeobox.com/learn/fl-studio/how-to-make-trap-beats-in-fl-studio/)
- Drill 808s: written in C minor or G minor most often; notes land on or just after kick hits; slides of a minor 3rd or perfect 4th; about 2-3 slides per 4-bar phrase; some notes sustain a full beat; slides mostly upward, a quick upward slide followed by a sustained low note is a signature move — [Audeobox: Drill beats in FL Studio](https://www.audeobox.com/learn/fl-studio/how-to-make-drill-beats-in-fl-studio/)
- A clean sub fundamental can vanish on a phone; gentle saturation/controlled distortion adds upper harmonics so the 808 line is perceptible on small speakers; keep the deepest bass centred — [Beatstorapon: How to make a drill beat](https://beatstorapon.com/blog/how-to-make-a-drill-beat-bpm-808s-drums/)
- Missing fundamental: the ear infers a pitch from its harmonic series even when the fundamental is absent, which lets small speakers imply low notes they cannot reproduce — [Wikipedia: Missing fundamental](https://en.wikipedia.org/wiki/Missing_fundamental)

### Inferences
Note-to-Hz table (equal temperament, A4 = 440 Hz, f = 440 x 2^((n-69)/12); computed, not sourced). Format: MIDI = scientific name (FL label) = Hz.
- 24 = C1 (FL C2) = 32.7 | 25 C#1 34.6 | 26 D1 36.7 | 27 D#1 38.9 | 28 E1 (FL E2) 41.2 | 29 F1 43.7 | 30 F#1 46.2 | 31 G1 49.0 | 32 G#1 51.9 | 33 A1 55.0 | 34 A#1 58.3 | 35 B1 61.7
- 36 = C2 (FL C3) = 65.4 | 37 C#2 69.3 | 38 D2 73.4 | 39 D#2 77.8 | 40 E2 (FL E3) 82.4 | 41 F2 87.3 | 42 F#2 92.5 | 43 G2 98.0 | 44 G#2 103.8 | 45 A2 110.0 | 46 A#2 116.5 | 47 B2 123.5 | 48 C3 (FL C4) 130.8
- Electric bass open E = MIDI 28 (41.2 Hz); 5-string low B = MIDI 23 (30.9 Hz).
808/bass register rules:
- 808 root zone: MIDI 26-38 (D1-D2, ~37-73 Hz). Pick the octave of the key's root that falls in this window (e.g. F minor: F1 = MIDI 29, 43.7 Hz; G minor: G1 = MIDI 31, 49 Hz; C minor: C2 = 36 or C1 = 24 depending on sample).
- Hard floor ~MIDI 24 (32.7 Hz): below this most playback systems (and many club subs) lose output and the note becomes inaudible rumble eating headroom. Hard ceiling for the 808 "body" ~MIDI 43-48 (98-131 Hz): above this the 808 stops feeling like sub and starts competing with the low-mids; use upward octave slides that briefly visit this zone, then return.
- If the key root lands awkwardly (e.g. root at A#1 58 Hz feels thin, B0 31 Hz too low), keep the root and move riff notes BELOW the root (b7, 5th under the root) rather than leaving the zone.
- Synth/mid bass (non-808) lines: MIDI 28-52 (E1-E3), with sub layer one octave below the mid-bass if needed.
Tuning procedure for a sample-based 808 in FL:
- Detect the sample's fundamental (tuner, or Edison/FL pitch detection). If the sample is e.g. 10 cents flat of F, set channel fine pitch +10 cents; if its root is not C5 (FL label), set the sampler's root note (Channel settings > Misc "Root note") to the detected note so the piano roll key = actual pitch. Ignore the initial click/pitch-drop transient; measure the sustained tail.
- Many 808 samples have a downward pitch envelope in the first ~50-100 ms; read the stable pitch after it.
808 length/shape:
- Long 808 (sustain into next note, legato): melodic trap, drill, Atlanta-style; note length runs until the next 808 note (fill the gaps), giving continuous sub.
- Short/punchy 808 (1/8 or less, ~150-300 ms decay): bouncier hip-hop, Memphis, jersey, rage, when the kick is busy; leaves space for kick and vocals.
- Rule: if two 808 notes are closer than ~1 step, cut the first (mono cut / choke) to avoid phase clicks; FL "Mono" or "Cut itself" handles this.
Slide recipes (FL native sampler or FLEX/3x Osc/FL instruments; NOT third-party VST):
- S1 Octave up-slide: note A = root, 1 step long, ends overlapping note B = root+12 by 1 step; B marked Slide or Porta on. Place B on step 15/16 leading into the next bar or on the "and".
- S2 Drop slide: hold root+12, slide down to root on beat 1 of next bar (heavy resolve).
- S3 Drill "whoop": quick upward slide (b3 or 4th, 1/16 long) then a sustained low note.
- S4 Glide time defaults: FL Porta/Slide knob near ~40 (Audeobox) for tight slides at 140-150 BPM; lengthen for slow tempos.
- Limit: 1-2 slides per bar, 2-3 per 4 bars in drill.
808 patterns on the 16-step grid (x = 808 note start, numbers = steps):
- Trap basic (follows kick): kick 1, 8 (or 9), 11; 808 on 1 (long, root), 8/9, 11 with the last note sliding up an octave into the next bar.
- Trap sparse: 808 on 1 (sustain ~1.5 beats), 11 (b7 or 5th), 15 (octave up-slide).
- Drill (UK/NY, ~140-145 BPM, half-time feel): 808 on 1, 4 (or 5), 8, 11; frequently syncopated off the grid via slides; 808 notes start with the kick or a 16th after; slides by b3 or 4th.
- Hip-hop boom-bap: bass/808 on 1 and 8 (or 1, 7, 11), short notes, root/5th only.
808 + kick layering:
- Option A: kick on top of every 808 start (same step), kick high-passed ~40-50 Hz so the 808 owns the sub; kick supplies attack/click. Align transients (nudge the 808 sample start to remove its own click, or phase-align so first cycles reinforce).
- Option B: no separate kick on 808 hits; the 808's own transient is the kick (classic 808 style).
- Option C: sidechain the 808 to the kick by a few dB (Violet) for long sustained 808s under a busy kick.
Saturation for translation:
- Add harmonics (soft clip, tape, Fruity Blood Overdrive, Distructor, Fruity Waveshaper) so the 2nd-4th harmonics (e.g. 49 Hz root -> 98, 147, 196 Hz) carry the pitch on phones; band-split so the sub below ~100 Hz stays clean and mono. Check the line on a phone/laptop speaker.

### Gaps
- No authoritative published number for the "lowest safe 808 note"; the MIDI 24-40 window is my synthesis of the cited 30-80 Hz range plus playback-system reasoning.
- No source gave a millisecond value for 808 glide time; FL's Slide knob is unitless in the manual; "around 40" comes from one producer blog.
- FLEX 808 presets and 3x Osc bass specifics were not researched in the tool budget.

## 4. Bass line styles with example patterns

### Takeaway
Genres are largely defined by where the bass sits relative to the kick and how long its notes are: offbeat (house/trance), locked root 8ths (pop/rock), syncopated 16ths with octaves and ghost notes (funk/disco), space and avoidance of beat 1 (reggae), tied-to-kick sliding sub (trap/drill), detuned or LFO-modulated mid bass over a clean sub (DnB/dubstep).

### Cited Findings
- Off-beat bass: notes between every kick in four-on-the-floor; roots in disco/synth-pop/hi-NRG; medium-length notes with sharp attack and moderately filtered decay; release raised slightly to avoid clicks; start from a saw wave with an ADSR sweeping a low-pass downward; tempo-synced delay (e.g. dotted 8th) optional; sidechain or LFO Tool volume shaping; often only two alternating notes — [Attack Magazine](https://www.attackmagazine.com/technique/tutorials/low-end-theory-exploring-eight-common-bassline-styles/)
- Offbeat bass is one of the most-used patterns in modern tech house; in hard house/trance the offbeat "donk" places a single note on every offbeat for clean call-and-response with the kick — [The Producer School: tech house bass](https://theproducerschool.com/blogs/featured-blogs/master-modern-tech-house-bass-lines-complete-tutorial-guide); [The Producer School: hard house/trance](https://theproducerschool.com/blogs/featured-blogs/5-essential-bass-patterns-that-define-hard-house-and-trance-music)
- Disco bass: heavy use of octaves, often doubling the second (upper) octave note to give an 8th followed by a 16th; offbeat 8ths and syncopated 16th phrases — [TalkingBass: Disco bass octaves](https://www.talkingbass.net/disco-bass-octaves/); [Bass Musician Magazine: disco patterns](https://bassmusicianmagazine.com/2019/08/bass-lines-disco-basic-bass-patterns/amp/)
- Funk: ghost notes are muted, percussive plucks often placed before a real note; they act like a second drum part; funk relies on syncopated 16th subdivisions interlocking with drums — [TalkingBass: ghost-note basslines](https://www.talkingbass.net/bass-technique-ghost-notes/)
- Reggae one drop: emphasis on beat 3 with a light/empty beat 1; reggae bass lines get their character from avoiding beat 1 and using rests; dub foregrounds the bass and uses echo/dropouts — [Soundfingers: reggae/dub bass](https://soundfingers.com/techniques/authentic-reggae-dub-bass-tutorial/); [Violet Recording: reggae](https://violetrecording.com/how-to-make-reggae-music/)
- UK garage: ~130 BPM, 2-step kick on beats 1 and 3 only (often skipping), snares on 2 and 4, swung; heavy, liquid sub bass locked tight to the drums — [SampleFocus: UK garage](https://samplefocus.com/blog/how-to-produce-uk-garage-music); [Orphiq: UK garage](https://orphiq.com/resources/what-is-uk-garage)
- Reese bass: originated with Kevin Saunderson's "Reese" project (late 1980s), adopted by jungle/DnB; two detuned oscillators whose beating creates movement; saws (or squares) detuned about +/-25 cents is a common DnB/dubstep starting point — [Wikipedia: Drum and bass](https://en.wikipedia.org/wiki/Drum_and_bass); [Emastered: Reese bass](https://emastered.com/blog/reese-bass); [Avid: How to make a Reese bass](https://www.avid.com/resource-center/how-to-make-a-reese-bass)
- Dubstep wobble: harmonically rich bass with its filter cutoff modulated by a tempo-synced LFO (e.g. square LFO at 1/4 for on/off wobble) — [Emastered / Dubspot via search summary](https://blog.dubspot.com/video-tutorial-making-a-dubstep-bass-in-ableton-live)
- Amapiano log drum: hybrid of kick, 808, synth bass and percussion; usually ~110-115 BPM; syncopated pattern that bounces between kicks rather than on them, with pitch variation for bounce; any separate bass is a warm sine/low-passed sub, EQ'd or sidechained against the log drum — [Beatstorapon: Amapiano](https://beatstorapon.com/blog/how-to-make-amapiano-beat/); [RouteNote: Amapiano beat](https://create.routenote.com/blog/beatmakers-guide-how-to-make-an-amapiano-beat/)
- Drill 808 rules (see section 3) — [Audeobox: Drill](https://www.audeobox.com/learn/fl-studio/how-to-make-drill-beats-in-fl-studio/)

### Inferences
16-step patterns (steps 1-16 per bar; R = chord root, O = root+12, 5 = fifth, A = approach tone; length in steps). Defaults to be adapted to the chord progression with R1 (root on chord change).
- Pop/rock root 8ths: R on 1,3,5,7,9,11,13,15, length 2 (slightly detached, ~1.5 steps); move to new root exactly on the chord change; optional A on 15 before a change.
- House offbeat: R on 3,7,11,15, length 1-2; kick 1,5,9,13. Variation: R on 3,7,11 and O on 15; or two-note alternation (R on 3/11, 5 or O on 7/15).
- Tech house rolling: notes on 2,3,4 / 6,7,8 / 10,11,12 / 14,15,16 (everything except kick steps), short (length 1), with filter-envelope pluck; sidechain heavy.
- Techno rumble: not a note pattern; long sub/kick-reverb tail on R, sidechained/gated so it pumps on 3,7,11,15 offbeats. Typically one pedal note for 8-16 bars.
- Disco octave: R on 1, O on 3, O on 4 (8th + 16th doubling), R on 5, O on 7, O on 8 ... repeating per beat pair; i.e. per beat "R(1 step), O(1 step) on the and, O on the a". Change root with chord.
- Funk/slap: R on 1 (long-ish, 2), ghost (very low velocity ~20-40, length 0.5, same pitch or muted) on 2/4, O on 7 or 8, b7 on 11, 5 on 14, A on 16; leave beat 3 partly empty for the snare-adjacent space. Velocity contrast is essential (accents 110-127, ghosts 20-40).
- Motown/walking: one note per beat (steps 1,5,9,13) with R7 recipe; add 8th pickups (step 15) and chromatic A tones; long, legato.
- R&B/neo-soul: sparse, behind-the-beat feel (shift notes +5-15 ms or apply swing 55-60%), R on 1, A via chromatic step from a half step below on 16 or 8, 9th/7th colour tones as passing notes, slides between notes; follow extended chords but keep the root on the change.
- Reggae one drop: rest on step 1 (or very short), R long on 3 or on 5-ish, phrase lands on 9 (beat 3, with the one-drop kick+snare/rim), 5/b7/O movement in 11-16; leave whole beats empty; round, low-passed tone (cutoff ~600-1000 Hz), little attack.
- Dub: same, more space, bass dropouts for 1-2 bars, echo on other parts not the sub.
- UK garage / 2-step: kick on 1 and 11 (or 1, 8, 11), bass on 1 (long), 4 or 7 (syncopated), 11, octave/5th jumps, often with portamento; swing 55-62%.
- DnB (170-175 BPM, half-time drums): sub sine plays R long on 1 (sustain through bar), reese (detuned saws, mid band) on top with the same notes; rhythmic variety comes from the reese's filter/automation not the note grid. Notes change every 1-2 bars.
- Dubstep (140 BPM half-time, snare on 9): sub on 1 (long); mid-bass wobble/growl with LFO rate tempo-synced (1/4, 1/8, 1/8T, 1/16) automated per bar; sub stays a separate clean sine.
- Amapiano log drum (~112 BPM): hits on 4, 7, 11, 14, 16 (between kicks), pitched to chord roots and their octaves/5ths with pitch jumps for bounce; separate sub bass sparse or absent.
- Afrobeats: bass/808 on 1, 4 (or 7), 11 (tresillo-like 3+3+2 feel: steps 1, 7, 13 is the pure tresillo), roots and 5ths, short to medium notes.
- Synthwave: straight 8th or 16th arpeggiated bass (R on every 8th, or R-O 16ths) with saw + low-pass filter, little swing; follows chord roots exactly.
- Lo-fi / upright-style: walking-ish or sparse root-5th line with heavy swing (55-65%), slow attack, short release, low-passed (cutoff ~800 Hz), slight pitch drift; velocity variation 70-110.
- Trap / drill: see section 3 pattern list.

### Gaps
- Attack Magazine's eight-style article only yielded style 1 (off-beat) in fetch; styles 2-8 not read. Specific step placements for amapiano, afrobeats, synthwave, lo-fi, reggae and garage above are my synthesis of genre descriptions, not verbatim from a cited pattern chart.
- No source checked for dubstep growl synthesis (FM/resampling) or techno rumble processing in this budget.

## 5. Register, frequency bands, mono, translation (harmonics, missing fundamental)

### Takeaway
Low end is ~20-250 Hz: sub (~20-60 Hz) is felt more than heard and should be controlled and mono; most bass "presence" and definition lives in its harmonics (100 Hz-1.5 kHz), which is what phones and laptops actually reproduce.

### Cited Findings
- Low end spans 20-250 Hz with primary energy 20-160 Hz; low-mids 250-500 Hz — [iZotope](https://www.izotope.com/en/learn/7-tips-for-mixing-the-low-end)
- Sub-bass (about 20-60 Hz) is felt more than heard; low-end mixing = give kick and bass separate space, keep sub controlled and mostly mono, keep headroom — [Violet Recording: How to mix low end](https://violetrecording.com/how-to-mix-low-end/)
- Filter out roughly 20-30 Hz and below on bass-heavy instruments to preserve headroom; cutting around 300 Hz on bass lets mid instruments (guitar, piano) come forward; high-passing higher instruments clears room for kick and bass — [iZotope](https://www.izotope.com/en/learn/7-tips-for-mixing-the-low-end)
- Keep bass below roughly 100-120 Hz mono (phones/clubs are effectively mono, stereo lows cause phase cancellation); a common split point is 100-150 Hz with width only above it; vinyl mastering sums lows to mono below ~120-150 Hz because directionality is not perceived there and cartridges track it badly — [Future Proof Music School](https://futureproofmusicschool.com/blog/how-do-i-preserve-mono-low-end-while-adding-stereo-width-to-highs); [Mastering The Mix](https://www.masteringthemix.com/blogs/learn/how-to-add-width-to-bass-without-losing-mono-compatibility)
- Bass benefits from presence around 900 Hz-1.5 kHz to cut through — [Sonarworks](https://www.sonarworks.com/blog/learn/eliminate-competition-between-the-kick-and-bass)
- The auditory system infers a missing fundamental from its overtones, which can be used to simulate low notes on speakers that cannot play them — [Wikipedia: Missing fundamental](https://en.wikipedia.org/wiki/Missing_fundamental)
- Saturation reveals sub lines on phones; keep deepest bass centred — [Beatstorapon](https://beatstorapon.com/blog/how-to-make-a-drill-beat-bpm-808s-drums/)

### Inferences
- Mud zone: 200-400 Hz build-up from bass harmonics + low pad/piano notes + guitars; keep chord instruments' lowest notes above ~C3 (MIDI 48, 131 Hz) when bass is active, or high-pass them ~150-250 Hz.
- One sub source at a time per step (808 OR kick tail OR sub bass).
- Translation check: a pure sine at 41 Hz (E1) is near-silent on a phone; the same line with 2nd/3rd harmonics (82, 123 Hz) and some 300-1000 Hz content is clearly audible. For a skill: always pair a sine sub with either saturation or a mid-bass layer.
- Stereo: bass/808 channels centred; any chorus/unison/stereo widening only on a high-passed mid layer (>120-150 Hz).

### Gaps
- No primary standard defines exact band boundaries; numbers vary across iZotope, Violet, Sonarworks (e.g. sub top edge 60 Hz vs 80 Hz).

## 6. Bass sound design basics (sine/triangle sub, saw/square, filter pluck, layering)

### Takeaway
Use a sine (or triangle) for clean sub weight, saw/square for harmonic mid-bass, a low-pass filter with a fast decaying envelope for "pluck", and split sub vs mid layers so the sub stays mono and clean while the top layer carries character.

### Cited Findings
- A sine wave contains only the fundamental (no harmonics), which is why sine-based 808s sit cleanly in the sub range — [Amped Studio (search summary)](https://www.ampedstudio.com/blog/secrets-of-808-bass/)
- Off-beat house bass: saw wave, ADSR sweeping a low-pass downward ("moderately filtered decay"), sharp attack, slight release — [Attack Magazine](https://www.attackmagazine.com/technique/tutorials/low-end-theory-exploring-eight-common-bassline-styles/)
- Reese: two saws/squares detuned ~+/-25 cents — [Emastered](https://emastered.com/blog/reese-bass)
- Wobble: filter cutoff modulated by tempo-synced LFO — [Dubspot](https://blog.dubspot.com/video-tutorial-making-a-dubstep-bass-in-ableton-live)
- Amapiano: sine or low-passed sub to complement the log drum — [Beatstorapon: Amapiano](https://beatstorapon.com/blog/how-to-make-amapiano-beat/)
- FL native generators support Mono/Porta/Slide; VST/AU instruments do not support FL's overlap portamento/slide notes — [Image-Line manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/chansettings_misc.htm)

### Inferences
Starting presets (my defaults for FL 3x Osc / FLEX / Sytrus; tune by ear):
- Sub: sine, amp attack 0-5 ms, sustain 100%, release 30-80 ms (no clicks), mono, low-pass ~100-150 Hz to stay pure; optionally triangle for slightly more audibility (adds odd harmonics).
- Pluck bass: saw (or saw+square), LP cutoff ~200-400 Hz, resonance low-moderate, filter env amount high with decay 100-300 ms and sustain 0-20%, amp decay similar; velocity -> cutoff for dynamics.
- Layered bass: Layer 1 sine sub (one octave below or unison), low-passed ~100 Hz, mono; Layer 2 saw/square/reese mid-bass high-passed ~100-150 Hz, can be stereo/distorted. Same MIDI, same note lengths, both mono-voiced with identical portamento.
- 3x Osc quick bass: Osc1 sine at 0 (sub), Osc2 saw at 0 coarse with slight fine detune, Osc3 square -12 semitones low volume; enable Channel Misc Mono + Porta for glides.
- 808 from a synth: sine with pitch envelope +12 to +24 semitones dropping over 20-60 ms (the "knock"), amp decay 0.5-3 s, then saturation.
- Distortion order: saturate the mid layer (or band above ~100 Hz) rather than the whole sub, then low-pass the distortion around 2-5 kHz to avoid fizz.

### Gaps
- Did not retrieve Ableton Learning Synths, Sound On Sound, or Image-Line pages on 3x Osc/FLEX/Sytrus bass presets within the call budget; preset numbers above are uncited defaults.
