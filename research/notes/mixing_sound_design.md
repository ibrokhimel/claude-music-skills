# Mixing Fundamentals and Basic Sound Design / Sound Selection for Beat Producers (FL Studio)

Scope: practical reference intended to become a Claude skill for balancing and mixing beats in FL Studio (mixer volume, pan, routing, sidechain, stock plugins). Research date: 2026-10. Numbers are starting points, not rules; sources often stress "dial in by ear".

## 1. Gain staging and level balance

### Takeaway
Keep individual tracks well below 0 dBFS (averages near -18 dBFS, peaks roughly -12 to -6 dBFS), leave about 6 dB of peak headroom on the master before mastering, build a static mix with faders and pan only (anchor on kick/snare or lead), and monitor at moderate level (75-85 dB SPL) while also checking at very low volume and against references.

### Cited Findings
- Analog-modeled plugins (EQ, compressors, saturators) are generally designed for input around -18 to -12 dBFS; feeding them near -1 dBFS makes many distort unpleasantly — [Boris FX / Imagineer gain staging cheat sheet](https://borisfx.com/blog/gain-staging-cheat-sheet/)
- Common gain-staging practice: average level around -18 dBFS with peaks between -12 and -6 dBFS, leaving room for processing — [Imagineer Systems gain staging cheat sheet](https://blog.imagineersystems.com/blog/gain-staging-cheat-sheet/)
- More headroom in the mix gives the mastering stage more room to work — [Boris FX](https://borisfx.com/blog/gain-staging-cheat-sheet/)
- Many mastering services ask for roughly -6 dB of peak headroom on the mix print (print peaking around -6 dBFS, no master-bus FX) — [Studio 11 Chicago mastering](https://mastering.studio11chicago.com/mastering-6db/)
- In kick/bass-driven music, a common approach is to set the kick peaking around -6 dBFS and mix everything around it, then maximize in mastering — [Studio 11 Chicago mastering](https://mastering.studio11chicago.com/mastering-6db/) (forum-derived practice; treat as convention, not standard)
- iZotope's static-mix method: start from the densest/loudest section, bring up the primary group first (lead vocal, drums, bass), then harmonic instruments and backing parts; use only faders, pan pots and polarity; aim to finish in about 5 minutes; author targets roughly -20 LUFS (or -18 to -14 LU) for the mix to keep mastering headroom — [iZotope: 7 steps to a balanced static mix](https://www.izotope.com/en/learn/7-tips-for-a-balanced-static-mix.html)
- A static mix is a preliminary balance achieved with level and panning only — [Avid: volume balancing / static mix](https://www.avid.com/resource-center/volume-balancing-setting-levels-static-mix)
- Pull all faders down, bring up the most important element first (lead vocal or kick and snare), then set everything else around it; in hip-hop/electronic the kick and snare are usually the anchor; snare may need help at 2-4 kHz to cut through — [Violet Recording: how to balance levels](https://violetrecording.com/how-to-balance-levels-in-a-mix/)
- Most engineers find 75-85 dB SPL monitoring gives the truest picture and limits ear fatigue — [Sweetwater: monitor volume](https://www.sweetwater.com/insync/monitor-volume-2/)
- Low-volume check: at very low volume anything too loud jumps out and anything too quiet vanishes; if the vocal stays clear and snare still cuts, the balance is solid — [Violet Recording: mixing at low volume](https://violetrecording.com/how-to-mix-at-low-volume/)

### Inferences
- Practical FL Studio default for a beat (synthesized from the above): insert-track peaks for kick and 808 around -6 to -10 dBFS, snare/clap a few dB under kick, lead/vocal comparable to snare, chords/pads/music bed and hats/percussion lower; master peaking around -6 dBFS before any master-chain processing. Use the channel/insert volume, not the master fader, to create headroom.
- Typical relative loudness order in trap/hip-hop: kick and 808 (loudest, trading off), then snare/clap, then vocal or lead melody, then harmonic music bed, then hats/percs/FX. This ordering is consistent with the "anchor on kick and snare" guidance but no source gave dB offsets between elements.
- FL Studio mixer meters are sample-peak; use a loudness meter (e.g., Youlean, or FL's Wave Candy) for LUFS. Since FL works in 32-bit float, internal overs won't clip permanently, but plugins still respond to level, so gain-stage anyway.

### Gaps
- No authoritative source gave fixed dB offsets per element (e.g., "hats 10 dB below snare"); these remain genre/ear decisions.
- iZotope's -20 LUFS figure is one author's preference, not a standard.

## 2. EQ: spectrum regions, subtractive vs additive, carving

### Takeaway
Think in regions — sub (20-60 Hz), bass (60-250 Hz), low-mids/mud (200-500 Hz), mids (500 Hz-2 kHz), presence (2-8 kHz), air (8 kHz+). Cut before boosting, high-pass anything that doesn't need low end, and give kick and 808 (and lead vs pads) their own frequency lanes.

### Cited Findings
- iZotope region map: Sub 20-60 Hz (foundation); Bass 40-250 Hz (body/warmth); Low-mids 200-500 Hz (boxiness, mud, body); Mids 500 Hz-2 kHz (presence, nasal, attack); Presence 2-8 kHz (clarity, harshness, aggression); Air/brilliance 8-12 kHz+ (sparkle, shimmer) — [iZotope EQ cheat sheet](https://www.izotope.com/en/learn/eq-cheat-sheet.html)
- Kick: 60-80 Hz low punch; 100-200 Hz knock; 200-500 Hz boxiness (cut); 1-5 kHz attack/click — [iZotope EQ cheat sheet](https://www.izotope.com/en/learn/eq-cheat-sheet.html)
- Snare: cut rumble below 80 Hz; body 150-250 Hz; ring 400-700 Hz (narrow cut); attack 2-3.5 kHz — [iZotope EQ cheat sheet](https://www.izotope.com/en/learn/eq-cheat-sheet.html)
- Bass: mud 300-500 Hz (cut); articulation 800 Hz-1 kHz (boost) — [iZotope EQ cheat sheet](https://www.izotope.com/en/learn/eq-cheat-sheet.html)
- Vocals: high-pass below ~100-250 Hz; nasal 500 Hz-1.2 kHz (cut); harshness 5-8 kHz (cut if needed); air 10 kHz+ (boost) — [iZotope EQ cheat sheet](https://www.izotope.com/en/learn/eq-cheat-sheet.html)
- Hi-hats: harshness 3-7 kHz (cut sparingly) — [iZotope EQ cheat sheet](https://www.izotope.com/en/learn/eq-cheat-sheet.html)
- "Less is more": subtractive EQ generally sounds more natural than additive; high-pass filters remove unneeded lows on non-bass sources — [iZotope EQ cheat sheet](https://www.izotope.com/en/learn/eq-cheat-sheet.html)
- Alternate map: 20-60 Hz sub, 60-200 Hz bass, 200-600 Hz low mids, 600 Hz-3 kHz mids, 3-8 kHz upper mids, 8-20 kHz highs; mud/fullness 250-450 Hz; too much 250-500 Hz = muddy/boomy, too little = thin; presence 4-6 kHz; air 6-20 kHz — [Mastering.com: how to use EQ](https://mastering.com/how-to-use-eq); [Audient: frequency ranges explained](https://audient.com/tutorial/frequency-ranges-explained/)
- Kick vs bass: bass is very present at 60-120 Hz and masks the kick; sidechain lets the kick take the initial impact and the 808 the tail — [Mixelite: sidechain in FL Studio](https://mixelite.com/blog/top-3-ways-to-sidechain-in-fl-studio/)
- Kick/808 carving: let the kick own a slightly higher punch frequency and the 808 own the deep sub, or notch the 808 where the kick lives — [Violet Recording: how to mix 808s](https://violetrecording.com/how-to-mix-808s/)

### Inferences
- Kick/808 lane split: decide which owns ~40-60 Hz (usually the 808 in trap) and let the kick's punch sit ~60-100 Hz with click at 2-5 kHz; small notch (2-4 dB) on the 808 at the kick's fundamental if not sidechaining.
- High-pass starting points (inference from region map): hats/cymbals 200-400 Hz+, pads/chords/keys 100-200 Hz, leads/melodies 100-200 Hz, snare/clap ~80-100 Hz, vocals 80-150 Hz. Always confirm by soloing and A/B in context.
- Lead/vocal vs pads: dip pads/chords 2-4 dB around 1-4 kHz where the lead/vocal's presence sits (complementary EQ).
- Boosts: wide Q, small amounts (1-3 dB); cuts: narrow Q for resonances, wider for mud (200-500 Hz).

### Gaps
- Sources disagree slightly on region boundaries (e.g., presence 2-8 kHz vs 4-6 kHz); these are conventions, not standards.

## 3. Compression (including bus, parallel, sidechain)

### Takeaway
Attack sets how much transient passes before gain reduction (slower = more punch), release sets recovery (should breathe with the tempo). Moderate ratios (2:1-4:1) for most tracks, gentle 2:1 with 2-5 dB GR for bus "glue", parallel compression for drum weight; sidechain kick-to-808/pads with a fast attack and release that recovers before the next hit.

### Cited Findings
- Kick: 10-20 ms medium-fast attack lets the transient through; 4:1 starting ratio, up to 6:1-8:1 for aggressive control; slow attack + fast release adds punch — [Music Guy Mixing: drum compression cheat sheet](https://www.musicguymixing.com/?p=3896)
- Snare: slower attack (20-30 ms) emphasizes the stick crack; slow attack + fast release + moderate ratio for punch — [Music Guy Mixing](https://www.musicguymixing.com/?p=3896)
- Drum bus glue: slow attack, fast-to-medium release; group buses ~2:1 with 2-5 dB gain reduction — [Mastering.com compression cheat sheet (PDF)](https://mastering.com/wp-content/uploads/2017/07/COMPRESSION-CHEAT-SHEET.pdf); [Scraps Audio: drum compression](https://scrapsaudio.com/blogs/scraps-blog/mastering-drum-compression-your-complete-guide)
- Parallel compression blends a heavily compressed copy with the dry signal, adding impact without losing dynamics; use it on the drum bus to avoid audible cymbal pumping — [Scraps Audio](https://scrapsaudio.com/blogs/scraps-blog/mastering-drum-compression-your-complete-guide)
- 808 compression: slower attack lets the transient through while taming sustain; very fast settings can react to individual waveform cycles (distortion) — [Violet Recording: how to mix 808s](https://violetrecording.com/how-to-mix-808s/)
- Sidechain for 808: fast attack, quick release; set release so the 808 recovers before the next note — [Violet Recording: how to mix 808s](https://violetrecording.com/how-to-mix-808s/)
- Fruity Limiter sidechain ratio starting point ~2.5:1, threshold lowered by ear — [Slooply: sidechain kick and bass, Fruity Limiter](https://slooply.com/blog/how-to-sidechain-kick-and-bass-in-fl-studio-fruity-limiter-method/)
- Fruity Limiter manual: the first ~10 ms of a sound mostly forms the impression of timbre; COMP/LIMIT/NOISE GATE modes; attack 0 ms recommended to avoid latency issues (or enable Plugin Delay Compensation if using longer attack); too-short release causes distortion; SUSTAIN is an RMS averaging window 0-1000 ms; CEIL at +12 dB effectively bypasses the limiter stage; THRESH at 0 dB disables the compressor — [Image-Line: Fruity Limiter](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Limiter.htm)
- Fruity Limiter sidechain routing: select the source (kick) mixer track, right-click the destination track's send/sidechain arrow → "Sidechain to this track", then on Fruity Limiter COMP tab right-click SIDECHAIN and pick the source; lower threshold below peaks and raise ratio — [Image-Line: Fruity Limiter](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Limiter.htm); [Mixelite](https://mixelite.com/blog/top-3-ways-to-sidechain-in-fl-studio/)
- Fruity Peak Controller: load on the source (kick) track; raise Base, set Volume negative (range -200% to +200%) so peaks pull the target down; Decay sets return time to Base; Tension shapes the curve; link to the target (e.g., synth or mixer track volume) via Link to controller; can be combined with its LFO — [Image-Line: Fruity Peak Controller](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Peak%20Controller.htm)

### Inferences
- FL starting presets (synthesized, adjust by ear):
  - Kick → 808 ducking (Fruity Limiter COMP, sidechain = kick): ratio 2.5:1-4:1, attack 0-1 ms, release 50-150 ms (shorter at higher BPM; must recover before next 808 note), threshold set for ~3-6 dB GR on kick hits. For pumping pads/chords: deeper GR (6-10 dB) and release ~1/8 note (60000/BPM/2 ms).
  - Glue on drum bus: 2:1, attack 10-30 ms, release 100-200 ms or tempo-related, 2-3 dB GR.
  - Parallel drums: send drum bus to a second bus with heavy compression (6:1-10:1, fast attack/release, 8-12 dB GR) and blend in under the dry.
- Fruity Peak Controller ducking is volume automation (no lookahead, independent of ratio) — useful for a precise "pump" shape; Fruity Limiter sidechain behaves like a true compressor.
- Since FL 20.x, many producers use the Fruity Limiter sidechain or third-party tools (e.g., Kickstart/LFO Tool) — third-party tools fall outside "stock plugins" scope.

### Gaps
- No source provided authoritative ms values for kick→808 sidechain release; values above are inferences.
- Did not fetch Fruity Compressor / Fruity Multiband Compressor manual pages.

## 4. Stereo and panning

### Takeaway
Keep kick, snare/clap, 808/bass, lead vocal/main lead in the center and the sub region mono (below ~100-150 Hz); spread hats, percussion, doubles, pads and FX off-center; use Haas (short delay) widening cautiously because it hurts mono compatibility.

### Cited Findings
- Sub frequencies should be centered and mono; collapse the lowest frequencies to mono while leaving higher harmonics free — [Violet Recording: how to mix 808s](https://violetrecording.com/how-to-mix-808s/)
- When widening with M/S or short delays, high-pass the Side signal at about 100-150 Hz so bass stays centered; low frequencies with short Haas delays sum in phase on one side and out of phase on the other — [Sound On Sound: fake M/S, mono compatible](https://www.soundonsound.com/sound-advice/q-how-can-create-fake-ms-setup-mono-compatible)
- Haas widening uses a delayed copy roughly 1-30 ms (some sources say 5-40 ms); it sounds very wide but is usually not very mono compatible — [eMastered: Haas effect](https://emastered.com/blog/haas-effect); [Sound On Sound](https://www.soundonsound.com/sound-advice/q-how-can-create-fake-ms-setup-mono-compatible)
- Static mix uses pan pots as one of only three tools (with faders and polarity) — [iZotope static mix](https://www.izotope.com/en/learn/7-tips-for-a-balanced-static-mix.html)
- Maximus offers per-band stereo separation controls (can narrow the low band) — [Image-Line: Maximus](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Maximus.htm)

### Inferences
- Pan starting positions (convention): kick, snare/clap, 808/bass, lead vocal, main lead = C. Hats 10-30% L or R; open hat/ride opposite side; percussion/shakers 20-50% alternating sides; double-tracked parts or layered chords hard-ish L/R (50-100%); backing vocals spread wide; pads/chords stereo but low end mono.
- FL tools: mixer track pan knob and Stereo Separation knob (narrowing toward mono), Fruity Stereo Shaper (includes delay for Haas), Fruity Stereo Enhancer (phase offset and pre-delay), Maximus low-band stereo separation to mono the lows. Check in mono (e.g., Stereo Separation fully mono on the master temporarily) for disappearing elements.

### Gaps
- Did not fetch Image-Line pages for Fruity Stereo Shaper/Enhancer or mixer stereo separation knob; tool descriptions above are from general FL knowledge and should be verified.

## 5. Space and depth: reverb and delay

### Takeaway
Put reverbs/delays on send (aux) tracks at 100% wet, time pre-delay and decay to the tempo (quarter note = 60000/BPM ms), use short rooms/plates for drums and vocals and longer halls for pads/FX, and filter returns so they don't muddy the low end. Depth = lower level + less top end + more reverb.

### Cited Findings
- Quarter-note length in ms = 60000 / BPM; all other note values derive from it — [Omni Calculator: delay & reverb times](https://www.omnicalculator.com/other/delay-reverb-times); [AnotherProducer delay/reverb calculator](https://anotherproducer.com/online-tools-for-musicians/delay-reverb-time-calculator)
- Pre-delay of about 1/64-1/16 note keeps transients clear; set decay to end by the next beat (tight) or bar (lush) — [Violet Recording reverb calculator](https://violetrecording.com/tools/reverb-calculator/)
- Total reverb time = pre-delay + decay — [AnotherProducer](https://anotherproducer.com/online-tools-for-musicians/delay-reverb-time-calculator)
- Fruity Reeverb 2: pre-delay can be tempo-synced; modest pre-delay for small rooms; small rooms want shorter decay, large rooms longer; decay measured to -60 dB; shorter decays for drums; low cut reduces rumble in drum reverb; on a send track set Dry to 0% and Wet to 100%; reverb works best on individual instruments and should not go on the master — [Image-Line: Fruity Reeverb 2](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Reeverb%202.htm)
- Fruity Delay 3: time 1-1000 ms or tempo-synced; Mono/Stereo/Ping Pong modes; feedback can exceed 100% (self-oscillation); per-echo LP/HP/BP filter; sine modulation 0-20 Hz for wow/flutter; diffusion smears echoes toward reverb; Tone control helps prevent muddy delays — [Image-Line: Fruity Delay 3](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Delay%203.htm)

### Inferences
- Tempo math (computed from 60000/BPM):

| BPM | 1/4 | 1/8 | dotted 1/8 | 1/8 triplet | 1/16 | 1/32 |
|-----|-----|-----|-----------|-------------|------|------|
| 70  | 857 ms | 429 | 643 | 286 | 214 | 107 |
| 90  | 667 | 333 | 500 | 222 | 167 | 83 |
| 120 | 500 | 250 | 375 | 167 | 125 | 63 |
| 140 | 429 | 214 | 321 | 143 | 107 | 54 |
| 160 | 375 | 188 | 281 | 125 | 94 | 47 |

  (dotted = x1.5; triplet = x2/3.) Trap at 140-160 BPM often feels like half-time (70-80), so 1/4-note delays at 140 match the 70 BPM 1/8.
- Reverb type defaults: room (0.3-0.8 s) for drums/percs; plate (1-2 s, pre-delay 20-40 ms) for snare/vocals/leads; hall (2-4 s+) for pads, pluck tails, transitions. High-pass the return at 200-400 Hz and low-pass around 6-10 kHz to keep it out of the way.
- FL routing: create 2-3 FX send tracks (e.g., "Verb Short", "Verb Long", "Delay 1/8 dotted"), route sources via the send knob/right-click "Route to this track only" or sends, and sidechain-duck long reverbs/delays from the vocal/lead if they cloud it.

### Gaps
- No primary source gave reverb-type decay ranges; the defaults above are conventional practice.

## 6. Saturation, distortion, transient shaping, clipping

### Takeaway
Saturate the 808 (or a parallel copy) so its upper harmonics translate on phones/laptops; tune it to key first; keep the sub layer clean. Clipping/limiting drums can raise loudness with fewer artifacts than heavy compression, but no strong primary source was found here.

### Cited Findings
- Small speakers roll off hard below ~150-200 Hz, so a pure 808 sub disappears; saturation adds higher harmonics the ear uses to reconstruct the missing fundamental — [Violet Recording: make 808s hit harder](https://violetrecording.com/how-to-make-808s-hit-harder/)
- Start with light drive and push until the 808 "growls" without fizzing; split into a clean sub layer and a saturated layer; high-pass the saturated layer so its harmonics sit above the fundamental — [Violet Recording: make 808s hit harder](https://violetrecording.com/how-to-make-808s-hit-harder/); [Violet Recording: how to mix 808s](https://violetrecording.com/how-to-mix-808s/)
- Fruity Limiter has a SAT (saturation) control; Maximus bands include saturation controls — [Image-Line: Fruity Limiter](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Limiter.htm); [Image-Line: Maximus](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Maximus.htm)
- An 808 whose notes vary by ~6 dB will repeatedly hit the limiter and duck the whole track — control sub energy before mastering — [Violet Recording: how to master hip hop](https://violetrecording.com/how-to-master-hip-hop/)

### Inferences
- FL stock options: Fruity Fast Dist / Fruity Blood Overdrive / Fruity WaveShaper for grit, Fruity Soft Clipper on drum bus or 808 for peak taming, Fruity Squeeze, Distructor, and Transient Processor for transient shaping (attack up for punch, release down to tighten tails). Verify plugin names/behavior against the FL manual before encoding into the skill.
- Drum clipping practice: soft clip the drum bus or individual kick/snare 1-3 dB to shave peaks and gain loudness; listen for added harshness.

### Gaps
- Did not find a primary-source article with numeric guidance for drum clipping or transient shaper settings; Fruity Soft Clipper and Transient Processor manual pages were not fetched.

## 7. Master chain and loudness

### Takeaway
Streaming services normalize playback (Spotify/YouTube ~-14 LUFS integrated, Apple ~-16 LUFS); keep true peak at or below -1 dBTP (Spotify suggests -2 dBTP if louder than -14 LUFS). Hip-hop masters are commonly louder (~-8 to -10 LUFS) for perceived impact; normalization will turn them down.

### Cited Findings
- Spotify normalizes to -14 LUFS integrated (turning loud masters down, quieter ones up within headroom limits); recommends masters at -14 LUFS with true peak below -1 dBTP; if louder than -14 LUFS, keep true peak below -2 dBTP to avoid transcoding distortion; leaves 1 dB headroom for lossy encodes (example: -20 LUFS track with -5 dBFS TP is only raised to -16 LUFS) — [Spotify for Artists: loudness normalization](https://support.spotify.com/artists/article/loudness-normalization/)
- AES TD1008 (2021) recommends music distribution loudness of -16 LUFS, speech -18 LUFS, mixed content -17 LUFS, peaks no higher than -1 dBTP — [Production Advice: TD1008](https://productionadvice.co.uk/td1008/); [Production Expert: AES update](https://www.production-expert.com/production-expert-1/aes-update-loudness-recommendations-for-audio-only-streaming)
- Spotify moved from -11 to -14 LUFS reference; YouTube uses -14 LUFS LUFS-based normalization; TIDAL uses album normalization (loudest track at -14 LUFS) — [Production Advice: TD1008](https://productionadvice.co.uk/td1008/)
- Apple Music Sound Check normalizes to -16 LUFS (per AES TD1008); YouTube reference -14 LUFS, true peak below -1 dBTP recommended, loud tracks turned down but quiet not raised — [Production Expert: Apple chooses -16 LUFS](https://www.production-expert.com/production-expert-1/apple-choose-16lufs-loudness-level-for-apple-music-heres-why?format=amp); [Meterplugs: Apple switch to LUFS](https://www.meterplugs.com/blog/2022/03/23/apple-switch-to-lufs.html); [Mastering The Mix: mastering for streaming](https://masteringthemix.com/blogs/learn/76296773-mastering-audio-for-soundcloud-itunes-spotify-and-youtube)
- Competitive hip-hop masters often land around -8 to -10 LUFS integrated; keep true-peak ceiling at -1 dBTP — [Violet Recording: how to master hip hop](https://violetrecording.com/how-to-master-hip-hop/)
- Maximus: multiband (Low/Mid/High + master) maximizer, compressor, limiter, gate, expander, ducker, de-esser; intended especially as the last effect on the Master track; manual warns against loudness-war over-compression — [Image-Line: Maximus](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Maximus.htm)
- Soundgoodizer is built on the Maximus engine: four presets (A-D) plus one amount knob (0-100%) that works like Maximus's LMH mix — [Image-Line: Soundgoodizer](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Soundgoodizer.htm)
- Fruity Limiter LIMIT mode = very high ratio (>10:1) capping output, used primarily for mastering — [Image-Line: Fruity Limiter](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Limiter.htm)

### Inferences
- Simple FL master chain for a beat: (optional) Fruity Parametric EQ 2 gentle tonal shaping → glue compressor (Fruity Limiter COMP or Maximus, 1.5-2:1, 1-2 dB GR) → limiter (Fruity Limiter LIMIT or Maximus) with ceiling at -1.0 dB (true-peak safe margin; FL's Fruity Limiter is not a true-peak limiter, so leave extra margin, e.g., -1 to -1.5 dB) → loudness meter. Target: -14 LUFS for streaming-safe, -10 to -8 LUFS for competitive rap/trap beat leases.
- Soundgoodizer on the master is a quick "make it louder/brighter" preset — easy to overdo; prefer explicit Maximus/Limiter settings for a controllable skill.

### Gaps
- Amazon Music and SoundCloud normalization levels were not confirmed from primary sources.

## 8. Sound selection and basic synthesis

### Takeaway
Pick samples that already fit the genre and key, tune 808s and tonal drums to the song's key first, layer only for complementary frequency roles, and know waveforms: sine for subs/808s, saw for leads/pads/basses, square for hollow/reedy/retro tones; detune/unison for width.

### Cited Findings
- Tune the 808 to the song's key before anything else; long low notes make pitch clashes read as mud/"wobble" — [Violet Recording: make 808s hit harder](https://violetrecording.com/how-to-make-808s-hit-harder/)
- Layer a clean sub with a saturated layer for weight on big systems plus presence on small ones — [Violet Recording](https://violetrecording.com/how-to-make-808s-hit-harder/)
- Sine = fundamental only, pure/round; sawtooth = all harmonics, bright/buzzy, workhorse for basses, leads, pads, brass; square = odd harmonics only, hollow/reedy (clarinet, 8-bit) — [Beat Kitchen: oscillators](https://beatkitchen.io/guides/synthesist/02-oscillators/)
- Detuning two same-wave oscillators slightly creates slow periodic swelling/thickening — the basis of lush analog pads — [Beat Kitchen: oscillators](https://beatkitchen.io/guides/synthesist/02-oscillators/)

### Inferences
- ADSR roles: Attack (fade-in; 0-5 ms for plucks/drums, 100 ms+ for pads), Decay (drop to sustain level), Sustain (held level while key down), Release (tail after key up; short for tight basses, long for pads). Filter envelope on a low-pass (cutoff sweep) defines plucks vs pads.
- Practical selection rules: one kick and one 808 that agree on pitch/tail; choose snares/claps that sit 150-250 Hz body + 2-4 kHz crack; avoid stacking multiple wide pads in the same octave; leave space for vocals (1-5 kHz) in beats meant for artists.
- FL tuning: use the channel Pitch knob/Fine tune or the sampler's root note; Edison/Pitcher or the piano roll to check pitch of 808 samples.

### Gaps
- No primary source fetched for ADSR specifics or layering of drums (phase alignment); values above are conventional knowledge.

## 9. FL Studio specifics: mixer, routing, stock plugins

### Takeaway
Route each channel to its own insert, group into buses (drums, music, vocals), add sends for reverb/delay, use Fruity Parametric EQ 2 for EQ, Fruity Limiter (COMP) or Peak Controller for compression/sidechain, Reeverb 2/Delay 3 on sends, Maximus/Limiter on master; use Soundgoodizer sparingly.

### Cited Findings
- Fruity Parametric EQ 2: 7 bands; types Low Pass, Band Pass, High Pass, Notch, Low Shelf, Peaking, High Shelf; slopes -12 to -48 dB/oct; spectrum analyzer 20 Hz-20 kHz with heatmap, mid/side monitoring; Compare for A/B; Linear Phase mode avoids phase artifacts at the cost of latency; shortcuts: Shift-click solo band, Alt-click reset — [Image-Line: Fruity Parametric EQ 2](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Parametric%20EQ%202.htm)
- Fruity Limiter: LIMIT/COMP/NOISE GATE; sidechain via mixer "Sidechain to this track" plus SIDECHAIN selector — [Image-Line: Fruity Limiter](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Limiter.htm)
- Fruity Peak Controller: envelope follower/LFO that automates parameters; negative Volume for ducking — [Image-Line: Fruity Peak Controller](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Peak%20Controller.htm)
- Fruity Reeverb 2 and Fruity Delay 3 details — see section 5 — [Reeverb 2](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Reeverb%202.htm); [Delay 3](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Delay%203.htm)
- Maximus and Soundgoodizer — see section 7 — [Maximus](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Maximus.htm); [Soundgoodizer](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Soundgoodizer.htm)

### Inferences
- Suggested routing template for the skill: inserts 1-N per channel (kick, 808, snare/clap, hats, percs, melody/lead, chords/pads, vocal) → bus tracks (Drums bus, Music bus, Vocal bus) → Master. Sends: Reverb short, Reverb long, Delay. Kick insert set as sidechain source to 808 and to pads/music bus (sidechain-only routing so audio doesn't double).
- The FL Studio MCP bridge in this workspace exposes fl_set_track_volume / fl_set_track_pan / fl_route_track / fl_diagnose_mix — a skill can apply the pan and level conventions above directly; plugin parameter control likely is not available (FL 21 limitations noted in user memory).

### Gaps
- FL mixer routing manual page (send switches, "route to this track only", stereo separation) was not fetched; routing description relies on the Fruity Limiter manual's sidechain steps and general FL knowledge.

## 10. Practical mix checklist and common beginner mistakes

### Takeaway
Order: tune and select sounds → gain stage → static balance (faders/pan) → subtractive EQ/high-passes → kick/808 relationship and sidechain → compression/saturation → sends for space → automation → check mono, low volume, references, small speakers → master with headroom and true-peak margin.

### Cited Findings
- Do the static mix first with faders/pan/polarity only, quickly — [iZotope](https://www.izotope.com/en/learn/7-tips-for-a-balanced-static-mix.html)
- Monitor at 75-85 dB SPL; check at very low volume — [Sweetwater](https://www.sweetwater.com/insync/monitor-volume-2/); [Violet Recording](https://violetrecording.com/how-to-mix-at-low-volume/)
- Out-of-tune 808 and uncontrolled sub energy are top reasons hip-hop mixes/masters fall apart — [Violet Recording: 808s](https://violetrecording.com/how-to-make-808s-hit-harder/); [Violet Recording: master hip hop](https://violetrecording.com/how-to-master-hip-hop/)
- Pure sub 808s vanish on small speakers without harmonics — [Violet Recording](https://violetrecording.com/how-to-make-808s-hit-harder/)
- Feeding plugins too hot (near 0 dBFS) causes unpleasant distortion — [Boris FX](https://borisfx.com/blog/gain-staging-cheat-sheet/)
- Reverb on the master muddies the mix; use sends — [Image-Line: Fruity Reeverb 2](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Reeverb%202.htm)
- Haas widening can break mono compatibility; keep lows mono — [Sound On Sound](https://www.soundonsound.com/sound-advice/q-how-can-create-fake-ms-setup-mono-compatible)
- Over-compression in pursuit of loudness is warned against by Image-Line — [Image-Line: Maximus](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Maximus.htm)

### Inferences
- Common beginner mistakes to encode as skill checks: master clipping / no headroom; everything panned center; kick and 808 fighting (no sidechain/EQ lane, 808 out of key); no high-passes (low-mid mud build-up at 200-500 Hz); hats too loud/harsh (3-7 kHz); reverb inserted at 100% wet on instruments instead of sends; stereo wideners on bass; Soundgoodizer/limiter slammed on master during mixing; judging only on headphones at high volume; mixing soloed tracks instead of in context.
- Skill heuristics: flag any track peaking above -3 dBFS, master peaking above -3 dBFS pre-limiter, bass/808/kick panned off-center, hats louder than snare, more than ~3 elements dominating the same 1-5 kHz region.

### Gaps
- No single authoritative "beginner mistakes" source was fetched; this list is synthesized from the cited guidance above.
