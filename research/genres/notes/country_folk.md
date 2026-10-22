# Country, Folk & Acoustic Genres — Recipe Cards for FL Studio

Scope: traditional country/honky-tonk (incl. Bakersfield), outlaw country, bluegrass (+ old-time), Nashville sound/countrypolitan, modern country pop, bro-country, country trap / country-rap (2019 → 2024–2026 boom), Americana/alt-country, traditional folk (British/Irish/Appalachian), folk revival/singer-songwriter, indie folk, folk-pop/stomp-clap, Celtic, acoustic/fingerstyle.

Labels: (sourced) = backed by the cited URL; (convention) = widely taught practice / producer convention, not tied to a single cited source; (derived) = my own inference/arithmetic from sourced facts. Grid notation follows the shared format: 16 steps per 4/4 bar, step 1 = beat 1, 5 = beat 2, 9 = beat 3, 13 = beat 4; X accent, x normal, g ghost, . rest, o open hat. Non-4/4 grids are labelled.

Cross-reference: trap hats/808 programming, swing-knob math and general drum velocity bands are in `research_notes/Music theory and beat making/drums_rhythm_groove.md` and `bass_and_808.md` — not repeated here.

---

## Key question 1 — Genre-by-genre recipe cards (identity, tempo, harmony, melody, instruments, grid, bass, form, mix, neighbours, FL steps)

### Takeaway
Country and folk styles separate mostly on (a) the rhythm cell (train beat, two-beat boom-chick, shuffle, 3/4 waltz, bluegrass offbeat chop, 6/8 jig, stomp four-on-the-floor, trap half-time), (b) the "signature" lead timbre (fiddle + steel = honky-tonk; strings + choir = Nashville sound; banjo roll + mandolin chop + no drums = bluegrass; banjo/acoustic loop + 808 = country trap), and (c) production gloss (raw room → polished stadium). Getting the rhythm cell and the lead instrument right matters more than chord choice, because most of these genres share I–IV–V harmony.

### Cited Findings

---

#### CARD 1 — Traditional country / honky-tonk (incl. Bakersfield sound, neotraditional)

1. **Identity**
   - Origin: Texas/Oklahoma/Southern bars ("honky-tonks"), 1940s; golden age 1950s with Webb Pierce, Lefty Frizzell, Faron Young, George Jones, Hank Williams; Ernest Tubb's "Walking the Floor Over You" (1941) helped establish it — [Wikipedia: Honky-tonk](https://en.wikipedia.org/wiki/Honky-tonk) (sourced)
   - Bakersfield sound (late 1950s–60s, California): pioneered by Wynn Stewart, popularised by Buck Owens and Merle Haggard; first country style to lean heavily on electric instruments and a defined backbeat, i.e. the first strongly rock-influenced country — [Wikipedia: Bakersfield sound](https://en.wikipedia.org/wiki/Bakersfield_sound); [AllMusic: Bakersfield Sound](https://www.allmusic.com/style/bakersfield-sound-ma0000002443) (sourced)
   - Reference tracks: Hank Williams "Hey, Good Lookin'", Ernest Tubb "Walking the Floor Over You", Buck Owens "Under Your Spell Again" (cited as a shuffle example by PAS), Loretta Lynn "Coal Miner's Daughter" — [PAS](https://pas.org/pas-blog/country-music-grooves-variations-on-the-classics/) (sourced for the last two as shuffle examples). Neotraditional heirs: George Strait, Randy Travis, Dwight Yoakam (convention); current revival figure Zach Top was a 2025 CMA talking point — [AOL/CMA 2025](https://www.aol.com/2025-cma-awards-snubs-surprises-144930528.html) (sourced that he was discussed; that he is "neotraditional" is convention)
   - Recognise by ear: crying steel guitar + fiddle trading fills over a bouncing two-beat bass and crisp backbeat, nasal twangy vocal singing about drinking/cheating/loneliness.
2. **Tempo & feel**: two-beat "with a crisp backbeat", built for two-stepping and jitterbug — [Wikipedia: Honky-tonk](https://en.wikipedia.org/wiki/Honky-tonk) (sourced). BPM: shuffles/two-steps ~ 100–170 (quarter), default 120; ballads 60–80; waltzes 90–140 in 3/4 (convention). Swing: straight two-beat OR full shuffle (MPC ~66%); rarely in between (convention).
3. **Harmony**: I–IV–V triads with dominant-7 on V (and often on I before going to IV) (convention). Common: I–I–IV–IV–I–I–V–V (or I–V7–I ballads), secondary dominant II7 → V7 ("ragtime" turnaround inherited from western swing) (convention). Keys: guitar/fiddle keys G, A, C, D, E (convention). Harmonic rhythm: 1–2 bars per chord; changes on the bar line (convention).
   - Ex. (key of G): I–IV–I–V7–I → G | C | G | D7 | G ; with II7: G | G | A7 | D7 | G (convention)
4. **Melody & vocals**: early vocals "rough and nasal" (Hank Williams, Floyd Tillman); later "clear and sharp" (George Jones, Faron Young) — [Wikipedia: Honky-tonk](https://en.wikipedia.org/wiki/Honky-tonk) (sourced). Major pentatonic melodies with the "cry"/yodel break (flip into falsetto on long vowels), scooped attacks from a semitone/tone below, blue 3rd (b3→3) slides (convention). Lyrics: lost love, adultery, loneliness, alcoholism, self-pity — [Wikipedia](https://en.wikipedia.org/wiki/Honky-tonk) (sourced).
5. **Instrumentation**: "steel guitar and fiddle are the dominant instruments", plus guitar and string bass — [Wikipedia: Honky-tonk](https://en.wikipedia.org/wiki/Honky-tonk) (sourced). Honky-tonk piano (rhythmic, out-of-tune-ish upright; fed boogie-woogie) (sourced, same page). Bakersfield: twin Fender Telecasters picked (not strummed), big drum beat, fiddle, occasional pedal-steel solo — [Wikipedia: Bakersfield sound](https://en.wikipedia.org/wiki/Bakersfield_sound) (sourced); Buck Owens' bright, loud, twangy Tele tone contrasted with Nashville's strings — [Fender](https://www.fender.com/articles/instruments/10-chart-topping-country-telecaster-players) (sourced).
   - DAW: pedal steel library (e.g. Impact Soundworks Pedal Steel, which offers sustain/harmonic/legato/vibrato/bend articulations — [ISW](https://impactsoundworks.com/product/pedal-steel/?isw=4), sourced); fiddle library with legato + slides; Tele = clean electric guitar library or amp sim with bridge-pickup "spanky" EQ + slapback delay; upright bass sample; honky-tonk piano = FL Keys / any upright with slight detune (convention).
6. **Rhythm** (two-beat "boom-chick", 4/4, ~120 BPM):
   ```
   Kick     X . . . | . . . . | x . . . | . . . .
   Snare    . . . . | X . . . | . . . . | X . . .   (brush or cross-stick; crisp backbeat)
   HatFoot  . . . . | x . . . | . . . . | x . . .
   Bass     X . . . | . . . . | x . . . | . . . .   (root on 1, fifth on 3)
   GtrBass  X . . . | . . . . | x . . . | . . . .   (thumb bass note)
   GtrStrum . . . . | x . x . | . . . . | x . x .   (boom-chicka: strum 2, &2, 4, &4)
   ```
   Guitar "boom-chicka" = root bass note on beat 1, strum on 2 and "&" of 2, bass on 3, strum on 4 and "&" of 4 — [AcousticLife](https://acousticlife.tv/guitar-strumming-patterns-the-boom-chicka/) (sourced). Shuffle and waltz variants: see Key question 2 grids. Drum figure as written = convention.
7. **Bass**: upright/electric alternating root–fifth on 1 and 3 ("two-beat"), walking quarter notes (root–2–3–5 or chromatic approach) into chord changes and in shuffles (convention).
8. **Form**: verse–chorus or AABA, ~2:30–3:00, 2–4 bar intro played by steel or fiddle, instrumental break = half a verse/whole verse by steel then fiddle, final chorus, tag ending (repeat last line) (convention).
9. **Production**: mono/narrow-stereo room, little compression feel, slapback on vocal and Tele (Bakersfield), plate reverb on vocal; dynamic (convention).
10. **Subgenres/neighbours**: Bakersfield = louder, electric, backbeat-forward, Tele lead vs. Nashville's strings — [Wikipedia](https://en.wikipedia.org/wiki/Bakersfield_sound), [Fender](https://www.fender.com/articles/instruments/10-chart-topping-country-telecaster-players) (sourced). Western swing = adds horns/jazz chords and swing 4/4 (convention). Neotraditional (1980s–) = honky-tonk with modern hi-fi production (convention).
11. **FL Studio**
   - 120 BPM, swing off for two-beat (or 12/8 triplet grid / swing ~66% for shuffle).
   - Program bass root–fifth on 1 & 3; boom-chick guitar (bass note + muted strum chords).
   - Brush snare/cross-stick on 2 & 4 at moderate velocity; no big room kick.
   - Steel = fills only in gaps between vocal lines; fiddle takes intro/turnarounds; steel and fiddle trade the solo.
   - Fake-sounding mistakes: drums too loud/compressed, 808-style low end, steel played as a static pad (needs bends/volume swells), piano chords that sustain instead of "chunking".

---

#### CARD 2 — Outlaw country (and today's "outlaw/red-dirt" revival)

1. **Identity**: 1970s movement against the Nashville polish; Waylon Jennings (an original member), Willie Nelson, Kris Kristofferson, David Allan Coe, Billy Joe Shaver (convention, Waylon membership sourced — [Fender](https://www.fender.com/articles/instruments/10-chart-topping-country-telecaster-players)). Bakersfield set the stage for country-rock and outlaw — [AllMusic](https://www.allmusic.com/style/bakersfield-sound-ma0000002443) (sourced). Reference tracks: Waylon Jennings "Are You Sure Hank Done It This Way", Willie Nelson "Whiskey River", Waylon & Willie "Mammas Don't Let Your Babies Grow Up to Be Cowboys" (convention). Modern descendants: Chris Stapleton, Sturgill Simpson, Tyler Childers, Zach Bryan (convention; Childers/Bryan named as the country-derived camp of the current folk resurgence — [Penn State Collegian](https://www.psucollegian.com/opinion/columnists/why-noah-kahan-style-folk-music-has-returned-to-mainstream-column/article_28113a22-16e6-11ee-aed6-ffa1185dc0da.html), sourced).
   - Recognise by ear: lazy, swaggering mid-tempo groove with a heavy, simple bass line, phasered/tremolo Telecaster, gruff baritone, live-band looseness, no strings or choirs.
2. **Tempo & feel**: 80–130 BPM, default ~100; straight 8ths with a laid-back "behind the beat" pocket; some shuffles (convention).
3. **Harmony**: I–IV–V plus Mixolydian bVII (rock influence), blues dominant 7s; minor ballads (convention). Ex. in E: I–bVII–IV–I = E | D | A | E; I–IV–V7 = E | A | B7 (convention).
4. **Melody & vocals**: low-register spoken-sung baritone, conversational phrasing, pentatonic/blues melodies, little ornamentation, occasional talking verses (convention).
5. **Instrumentation**: Waylon's leather-covered 1953 Telecasters — [Fender](https://www.fender.com/articles/instruments/10-chart-topping-country-telecaster-players) (sourced); drums with full kit, electric bass, steel guitar used grittily, harmonica, Willie's nylon-string guitar (convention). DAW: electric guitar library + amp sim with phaser and tremolo; picked bass; acoustic kit with roomy snare (FPC acoustic kits) (convention).
6. **Rhythm** ("Waylon" chug, 4/4):
   ```
   Kick   X . . . | . . . . | X . . x | . . . .
   Snare  . . . . | X . . . | . . . . | X . . .
   Hat    x . x . | x . x . | x . x . | x . x .
   Bass   X . . x | . . x . | X . . x | . . x .   (repetitive root/octave/5th riff with 8th pick-ups)
   Gtr    x . x . | x . x . | x . x . | x . x .   (palm-muted 8th chug, phaser)
   ```
   (convention)
7. **Bass**: prominent, riff-based, locked with kick; often a two-note root/fifth figure with a pickup 8th (convention).
8. **Form**: verse–chorus, 3–4 min, guitar/harmonica solos, live-sounding endings (convention).
9. **Production**: dry, mid-forward, live-off-the-floor feel; less reverb than Nashville; modern revivalists (Stapleton) use vintage gear, analog tape warmth (convention).
10. **Neighbours**: vs honky-tonk = rock backbeat and heavier bass, fewer fiddles; vs Americana = more radio-country swagger, less indie/folk; red-dirt (Texas/Oklahoma) = outlaw + jam-band rock (convention).
11. **FL Studio**: 96–104 BPM, slight late-pocket (shift snare +5–10 ms); bass riff first; phaser on Tele; one steel or harmonica answer per line. Mistake: too polished/quantized, too many layers.

---

#### CARD 3 — Bluegrass (and old-time string band)

1. **Identity**: Bill Monroe & the Blue Grass Boys, 1940s Kentucky/Tennessee; Monroe's high mournful tenor set the "high lonesome" vocal convention and his breakneck mandolin set the instrumental standard — [Britannica: Bill Monroe](https://www.britannica.com/biography/Bill-Monroe) (sourced). Earl Scruggs' forward roll was the breakthrough enabling clear 3-finger banjo — [Deering/Wikipedia: Banjo roll](https://en.wikipedia.org/wiki/Banjo_roll) (sourced). Reference tracks: Bill Monroe "Blue Moon of Kentucky", Flatt & Scruggs "Foggy Mountain Breakdown", Monroe "Blue Grass Breakdown" (reported 175 BPM — [tunee.ai](https://www.tunee.ai/music-generator/bluegrass), weak source), modern: Billy Strings, Alison Krauss & Union Station, Molly Tuttle (convention).
   - Recognise by ear: no drums; banjo rolling continuous 8ths, mandolin "chop" on 2 and 4, upright bass on 1 and 3, very fast tempos, high-pitched close harmony, instruments taking turns soloing.
2. **Tempo & feel**: 120–200 BPM (sourced, [tunee.ai](https://www.tunee.ai/music-generator/bluegrass) — treat as approximate); breakdowns/instrumentals 160–240+, ballads/waltzes slower (convention). Straight 8ths, driving and slightly ahead of the beat ("drive") (convention). Felt in cut time (2) at fast tempos (convention).
3. **Harmony**: I–IV–V triads, almost no 7ths except V7; occasional bVII (e.g. G–F) and II major (A in key of G, "Salty Dog" type I–VI7–II7–V7–I) (convention). Keys: G, A, B, C, D, E (capo-friendly; banjo tuned open G) (convention).
   - Ex. in G: G | G | C | G | G | D | G | G ; "ragtime" cycle: G | E7 | A7 | D7 | G (convention)
4. **Melody & vocals**: "high lonesome" tenor — [Britannica](https://www.britannica.com/biography/Bill-Monroe) (sourced); trio harmony stacked lead/tenor (above)/baritone, often parallel 3rds/5ths, full-throated, nasal, little vibrato; major pentatonic melodies with blue 3rd hammer-ons; G-run guitar lick at phrase ends (convention).
5. **Instrumentation**: banjo (Scruggs 3-finger rolls), mandolin, fiddle, acoustic flat-top guitar (flatpicking), upright bass, dobro (resophonic slide) (convention + sourced roles: bass on-beats, banjo steady 8ths — [Wikipedia: Chop chord](https://en.wikipedia.org/wiki/Chop_chord)). Mandolin chop = chord muted by lifting fretting fingers right after the strum — a Monroe innovation that gave the music a harder groove than old-time — [Wikipedia: Chop chord](https://en.wikipedia.org/wiki/Chop_chord) (sourced).
   - DAW: sampled banjo and mandolin libraries with roll/chop articulations; for chop use a very short (50–80 ms) muted chord sample with a bright mid transient; dobro = slide guitar library or pitch-bent resonator samples (convention).
6. **Rhythm** (4/4 at ~170 BPM; written in 16ths but at bluegrass tempo the banjo plays 8ths = odd steps):
   ```
   Bass     X . . . | . . . . | x . . . | . . . .   (root on 1, fifth on 3 — the "two-beat")
   MandChop . . . . | X . . . | . . . . | X . . .   (offbeat chop on 2 & 4 = the snare)
   GtrBass  X . . . | . . . . | x . . . | . . . .   (bass note, alternates root/5th)
   GtrStrum . . . . | x . . . | . . . . | x . . .   (boom-chick)
   Banjo    X . x . | x X . x | . x X . | x . x .   (8ths continuous; accents 3+3+2 from forward roll)
   ```
   Banjo roll = repeating 8th-note broken-chord arpeggio that keeps time — [Wikipedia: Banjo roll](https://en.wikipedia.org/wiki/Banjo_roll) (sourced). Forward roll string order given by Deering: 2-1-5-2-1-5-2-(1) (thumb on 5th string, index on 2nd, middle on 1st) — [Deering](https://blog.deeringbanjos.com/the-four-essential-5-string-banjo-rolls) (sourced; final note derived). Repeating a 3-note T-I-M cell across 8 eighths produces the 3+3+2 accent grouping (derived). Accent placement in grid = derived.
   - Old-time variant: clawhammer banjo (down-stroke "bum-ditty": quarter + two 8ths = steps 1, 5, 7 per beat-pair) and fiddle with double stops — [Emory American Routes](https://scholarblogs.emory.edu/americanroutes/?p=399) (fiddle-banjo interlock/double stops sourced; bum-ditty grid convention).
7. **Bass**: upright, root–fifth on 1 and 3, walks between chords with 3-note runs (e.g. G–A–B–C) (convention; on-beat role sourced above).
8. **Form**: kick-off (instrumental intro, often fiddle or banjo, 4–8 bars) → verse → chorus (trio harmony) → instrumental break (one full verse/chorus cycle per soloist: banjo, fiddle, mandolin, dobro, guitar) → verse → chorus → tag (repeat last line, "shave and a haircut" ending lick). 2:30–3:30 (convention). Instrumentals ("breakdowns") are AABB fiddle-tune form (convention).
9. **Production**: acoustic, natural room, minimal compression, players around one or two mics in classic style; modern bluegrass = close-mic'd, very clean, wide stereo placement of instruments (convention).
10. **Neighbours**: old-time = older, fiddle-banjo duet, clawhammer, dance-oriented, less soloing — [Emory](https://scholarblogs.emory.edu/americanroutes/?p=399) (sourced); newgrass/progressive bluegrass = jazz/rock harmony, extended jams (Sam Bush, Béla Fleck, Billy Strings) (convention); "bluegrass covers" pop songs (convention).
11. **FL Studio**
   - 160–180 BPM, swing 0 (maybe a hair of push: shift chop -5 ms).
   - Program bass 1 & 3, chop 2 & 4 (that IS the backbeat — no drums).
   - Banjo: continuous 8th rolls through chord tones (open G: G-B-D strings plus drone 5th string high G).
   - G-run on guitar at phrase end: in G, a chromatic bass walk A–Bb–B then D, resolving to low G (convention; exact fingering varies).
   - Mistakes: adding a drum kit; banjo rolls quantized at identical velocity (vary 70–110); banjo playing chords not arpeggios; vibrato-heavy singing.

---

#### CARD 4 — Nashville sound / countrypolitan

1. **Identity**: late 1950s–1960s Nashville; Chet Atkins (head of RCA country division) and Owen Bradley replaced honky-tonk elements (fiddles, steel guitar, nasal lead vocals) with pop elements (string sections, background vocals, crooning lead vocals), slick production and pop structures — [Wikipedia: Nashville sound](https://en.wikipedia.org/wiki/Nashville_sound); [UT Austin DWRL](https://sites.dwrl.utexas.edu/countrymusic/the-history/the-nashville-sound/) (sourced). Bradley's productions with Patsy Cline are the archetype — [AllMusic](https://www.allmusic.com/subgenre/nashville-sound-countrypolitan-ma0000002739/artists) (sourced). Morphed into "countrypolitan" (more pop-structured, highly commercial) in the 1960s–70s — [Wikipedia](https://en.wikipedia.org/wiki/Nashville_sound) (sourced). Reference tracks: Patsy Cline "Crazy", Jim Reeves "He'll Have to Go", Glen Campbell "Wichita Lineman", Tammy Wynette "Stand By Your Man" (convention).
   - Recognise by ear: smooth crooner vocal, lush strings and "oohs" from a backing choir, soft brushes, slip-note piano, no fiddle sawing, no twang.
2. **Tempo & feel**: ballads 60–90 BPM, often 12/8 or 6/8 triplet feel; mid-tempo 4/4 shuffles 100–120 (convention).
3. **Harmony**: pop/jazz-tinged — maj7/6 chords, ii–V, secondary dominants, diminished passing chords, key-change up a semitone/tone for last chorus (countrypolitan) (convention; "jazz-tinged productions" sourced [AllMusic](https://www.allmusic.com/subgenre/nashville-sound-countrypolitan-ma0000002739/artists)).
   - Ex. in C: I–vi–ii–V = C | Am | Dm7 | G7 ; I–I7–IV–iv–I = C | C7 | F | Fm | C (convention)
4. **Melody & vocals**: crooning, legato, wider range, vibrato on held notes, minimal yodel; backing choir pads "oohs"/answer lines (Anita Kerr Singers / Jordanaires-type) (convention; crooning/backing vocals sourced above).
5. **Instrumentation**: string section, backing vocal group, piano (Floyd Cramer slip-note style: grace-note whole-tone slides into chord tones), tic-tac bass (electric bass doubled with muted gut-string guitar), brushes, vibes, light electric guitar (convention). DAW: FL Keys/any grand piano; string ensemble library; choir "ooh" library; electric bass + short muted baritone guitar doubled (convention).
6. **Rhythm** (12/8 ballad; 12 steps = 4 beats × 3 triplet 8ths):
   ```
   Ride/BrushSwirl x x x | x x x | x x x | x x x
   Kick            X . . | . . . | x . . | . . .
   Snare(brush)    . . . | X . . | . . . | X . .
   Piano triplets  x x x | x x x | x x x | x x x   (repeated chord triplets, doo-wop style)
   Bass            X . . | x . . | X . . | x . .   (root–5th on beats)
   ```
   (convention)
7. **Bass**: "tic-tac" doubled bass, root–fifth, smooth walk-ups (convention).
8. **Form**: AABA or verse–chorus, 2:30–3:00, string intro, half-step key change late (convention).
9. **Production**: lush plate/chamber reverb, vocal front and centre, polished, soft dynamics (convention; "slick" sourced above).
10. **Neighbours**: countrypolitan = bigger orchestra, more pop structure — [Wikipedia](https://en.wikipedia.org/wiki/Nashville_sound) (sourced); vs honky-tonk = no fiddle/steel twang; ancestor of modern country pop gloss (convention).
11. **FL Studio**: 72 BPM 12/8 (use triplet grid — set piano roll snap to 1/6 beat); strings as long legato pads under, choir "oohs" in chorus; piano grace-notes; plate reverb send 20–30% on vocal. Mistake: putting steel/fiddle in front (that's honky-tonk), quantizing triplets to straight 16ths.

---

#### CARD 5 — Modern country pop (2010s–2020s mainstream Nashville)

1. **Identity**: Nashville radio country absorbing pop, rock and hip-hop production; producers like Joey Moi (Florida Georgia Line, Jake Owen, Morgan Wallen; sole producer of "7 Summers") — [Wikipedia: Joey Moi](https://en.wikipedia.org/wiki/Joey_Moi) (sourced). Wallen's 2018 debut leaned on bro-country, pop, and rap/trap elements "in the form of snap tracks and 808 beats" — [Whiskey Riff](https://www.whiskeyriff.com/?p=642128) (sourced, secondary). Moi's mixes layered 808s behind Telecaster licks and stadium refrains — source is a low-quality aggregator page, treat as unverified ([latahcountyid mirror](https://phdns.latahcountyid.gov/article/morgan-wallen-mix-latest-songs-deep-cuts)). Country regularly occupies a large share of the Hot 100 in 2025 — same AOL piece ([AOL](https://www.aol.com/2025-cma-awards-snubs-surprises-144930528.html)) (sourced, though "half the spots" is an article claim). Reference tracks: Morgan Wallen "Last Night", Luke Combs "Fast Car" (cover), Kane Brown "Thank God", Lainey Wilson "Watermelon Moonshine" (convention).
   - Recognise by ear: big pop-structured chorus, acoustic guitar strumming 16ths + electric Tele licks, programmed/hybrid drums (snaps, claps, sometimes 808), slight twang in a pop vocal, very loud polished mix.
2. **Tempo & feel**: 70–110 BPM ballads/mid-tempo (default ~90), uptempo 110–150; mostly straight 16ths, some half-time trap feel (convention).
3. **Harmony**: pop loops: I–V–vi–IV, vi–IV–I–V, IV–I–V–vi; add9/sus2 colour; Mixolydian bVII for rock lift; mostly major keys (convention). Ex. in G: G | D | Em | C ; Em | C | G | D (convention).
4. **Melody & vocals**: verse in low register, talk-sung, chorus jumps up a 4th–6th; pentatonic hooks; vocal twang via vowel bends and "cry" flips; heavy doubling/harmony stacks in chorus; some rap-cadence verses (convention).
5. **Instrumentation**: acoustic guitars (often Nashville high-strung tuning layered with standard), Telecaster, pedal steel or B-bender as pad/fills, banjo as texture loop, piano/organ, programmed drums with live overdubs (convention; high-strung + layering example sourced in Shaboozey SOS piece — [SOS](https://www.soundonsound.com/techniques/inside-track-shaboozey-bar-song-tipsy)).
6. **Rhythm** (4/4, ~92 BPM pop-country groove):
   ```
   Kick     X . . . | . . x . | X . . . | . . . .
   Snap/Clap. . . . | X . . . | . . . . | X . . .
   Hat      x . x . | x . x . | x . x . | x . x .
   AcGtr    X . x x | . x x . | X . x x | . x x .   (16th strum D . D U . U D U ...)
   Bass/808 X . . . | . . x . | X . . . | . . . .
   ```
   (convention)
7. **Bass**: electric bass or 808 sub layered; root-based, follows kick (convention).
8. **Form**: Intro (4–8) – V1 (8–16) – Pre (4–8) – Chorus (8) – Post/turn (4) – V2 – Pre – Chorus – Bridge (8) – Chorus ×2 – Outro; ~3:00 (convention).
9. **Production**: polished, wide, loud (radio pop loudness), vocal tuned/compressed upfront, guitar layers L/R (convention).
10. **Neighbours**: bro-country (party lyrics, harder rock/hip-hop elements), country trap (808/trap hats dominate), Americana (live, raw) (convention).
11. **FL Studio**: start with an acoustic 16th strum loop (2 layers panned L/R + mono bus low — [SOS](https://www.soundonsound.com/techniques/inside-track-shaboozey-bar-song-tipsy), sourced technique); snaps on 2 & 4; electric Tele answers after each vocal line; steel swells under chorus. Mistake: using EDM/pop drums with no acoustic instruments; no twang vowel in topline.

---

#### CARD 6 — Bro-country (c. 2012–2016)

1. **Identity**: term coined by Jody Rosen (New York magazine, 11 Aug 2013) about Florida Georgia Line's "Cruise"; also named Luke Bryan, Jason Aldean, Jake Owen — [Wikipedia: Bro-country](https://en.wikipedia.org/wiki/Bro-country) (sourced). A 2010s form of country pop influenced by hip hop, hard rock and electronica; upbeat songs about women, alcohol, partying, jeans, boots, trucks — [Wikipedia](https://en.wikipedia.org/wiki/Bro-country) (sourced). "Cruise (Remix)" with Nelly was the first country single certified RIAA diamond — [Wikipedia: Country rap](https://en.wikipedia.org/wiki/Country_rap) (sourced). Reference tracks: FGL "Cruise", Luke Bryan "That's My Kind of Night", Jason Aldean "Dirt Road Anthem" (convention).
   - Recognise by ear: arena-rock electric guitars + banjo loop + drum-machine claps/loops, party-chant chorus, half-rapped verses.
2. **Tempo**: 90–120 BPM (convention); straight 8ths/16ths.
3. **Harmony**: 3–4 chord loops (I–V–vi–IV, I–IV–vi–V), power chords on choruses (convention).
4. **Vocals**: talk-sung/rap-lite verses, shouted gang choruses, heavy Auto-Tune polish (convention).
5. **Instrumentation**: distorted electric guitars (rock), banjo loop, programmed loops/claps + live drums, synth subs (convention).
6. **Rhythm** (4/4, ~104 BPM):
   ```
   Kick  X . . . | . . x . | X . x . | . . . .
   Clap  . . . . | X . . . | . . . . | X . . .
   Hat   x x x x | x x x x | x x x x | x x x x   (16th loop)
   Gtr   X . . . | X . . . | X . . . | X . . .   (big chord stabs on beats in chorus)
   ```
   (convention)
7–9. Bass follows kick; V–C–V–C–B–C ~3:15; loud rock-pop master (convention).
10. **Neighbours**: modern country pop (broader lyrical palette, less rock), country trap (trap hats/808s), Southern rock (no loops) (convention).
11. **FL**: banjo loop + clap loop first, add crunchy guitars in chorus. Mistake: too traditional (fiddle/steel prominent) or too EDM.

---

#### CARD 7 — Country trap / country-rap crossover (2019 → 2024–2026 boom)

1. **Identity**
   - Country rap blends country elements with hip-hop beats and rapping; late-1990s South; milestones: Kid Rock "Cowboy" (1999), Bubba Sparxxx (2001), Big & Rich/Cowboy Troy (2005), Colt Ford (first #1 on both Billboard Country Albums and Rap Albums), FGL "Cruise" remix with Nelly (RIAA diamond) — [Wikipedia: Country rap](https://en.wikipedia.org/wiki/Country_rap) (sourced).
   - "Country trap" breakthrough: Lil Nas X "Old Town Road" — 19 weeks at #1 on the Hot 100; Blanco Brown "The Git Up" (2019) — [Wikipedia: Country rap](https://en.wikipedia.org/wiki/Country_rap) (sourced). The OTR beat: Dutch producer YoungKio sampled banjo from Nine Inch Nails "34 Ghosts IV", sped it up (changing key), used a tuned 808 kick as bassline, layered pitched hi-hat patterns over a plain clap backbeat; sold on BeatStars for $30 — [Songfacts](https://www.songfacts.com/facts/lil-nas-x/old-town-road); [Highsnobiety](https://highsnobiety.com/p/lil-nas-x-old-town-road-history); [SOS](https://www.soundonsound.com/node/4920422?page=1) (sourced).
   - 2024–2026: Shaboozey "A Bar Song (Tipsy)" (released 12 Apr 2024; interpolates J-Kwon's "Tipsy"; #1 Hot 100; first song simultaneously top 10 on Country Airplay, Pop Airplay, Adult Pop Airplay and Rhythmic Airplay) — [Hit Songs Deconstructed](https://www.hitsongsdeconstructed.com/a-bar-song-tipsy-2/) and search summary (sourced). BigXthaPlug's country-rap album "I Hope You're Happy" (Aug 2025) featured Darius Rucker, Bailey Zimmerman, Ella Langley, Tucker Wetmore, Jelly Roll, Shaboozey, Luke Combs, Thomas Rhett — [AOL](https://www.aol.com/2025-cma-awards-snubs-surprises-144930528.html); [Billboard](https://www.billboard.com/music/music-news/bigxthaplug-teases-upcoming-country-ep-shaboozey-jelly-roll-morgan-wallen-1235867036/) (sourced). Billboard (2026) frames a "rap revival" led by Jelly Roll, BigXthaPlug and Post Malone; Shaboozey & Jelly Roll's "Amen" topped Billboard charts in March 2026; Billboard says trap drums and 808s "blurred lines" between the genres; Stagecoach 2025 booked Nelly and T-Pain, Wallen's Sand in My Boots fest had Wiz Khalifa, 2 Chainz, Three 6 Mafia — [Billboard: Country's Rap Revival](https://www.billboard.com/music/country/country-rap-crossover-hits-trend-1235983104/) (via search snippet; full article paywalled, see Gaps). Beyoncé's "Cowboy Carter" (2024) mixed country with hip-hop/R&B — [Wikipedia: Country rap](https://en.wikipedia.org/wiki/Country_rap) (sourced). Breland "My Truck" framed as country-trap — [OnesToWatch](https://onestowatch.com/blog/breland-my-truck) (sourced).
   - Recognise by ear: banjo/acoustic guitar loop or twangy guitar riff over trap drums (half-time clap, 16th/triplet hi-hat rolls, 808 bass), rap or melodic-rap verse with a sing-along country chorus.
2. **Tempo & feel**: trap convention 130–160 BPM with half-time feel (felt 65–80) — (convention, see earlier trap notes). "A Bar Song" listed at 162 BPM in A major — [Hit Songs Deconstructed snippet](https://reports.hitsongsdeconstructed.com/?p=53620) (sourced; it is commonly felt at ~81 half-time, derived). Straight 16ths with triplet hat rolls.
3. **Harmony**: two camps — (a) major-key sing-along loops (I–V–vi–IV, I–IV–I–V; "A Bar Song" in A major, sourced above); (b) minor-key trap loops (i–VI–VII, i–iv) with a banjo/guitar arpeggio (convention).
   - Ex. A major: A | E | F#m | D ; A minor: Am | F | G | Am (convention)
4. **Vocals**: rap verse (triplet "Migos" flow or Southern drawl) + belted country hook; gang vocals; Auto-Tune (convention). Shaboozey's take was largely the first-day vocal; gang vocals increase through the song for "everyone singing" — [SOS](https://www.soundonsound.com/techniques/inside-track-shaboozey-bar-song-tipsy) (sourced).
5. **Instrumentation & sounds**: banjo loop, acoustic guitar layers (30+ in "A Bar Song", incl. Nashville high-strung), fiddle (Splice loop blended with live fiddle), upright bass in chorus, piano, Farfisa/B3, programmed drums from self-recorded samples, guitar-case kick stomp, brushes, gang claps recorded in a hallway, an 808 added late — [SOS](https://www.soundonsound.com/techniques/inside-track-shaboozey-bar-song-tipsy) (sourced). "Old Town Road": sped-up banjo sample + tuned 808 + pitched hats + clap — [SOS/Songfacts](https://www.songfacts.com/facts/lil-nas-x/old-town-road) (sourced).
6. **Rhythm** (two templates)
   - (a) Trap template (OTR-style), 4/4 at ~136–140, half-time:
   ```
   Kick/808 X . . . | . . . x | . . x . | . . . .
   Clap     . . . . | . . . . | X . . . | . . . .   (half-time backbeat on beat 3)
   Hat      x x x x | x x x x | x x x x | x x x x   (16ths; add 1/32 and triplet rolls, pitch some up/down)
   BanjoLoop x . x . | x . x . | x . x . | x . x .  (8th-note arpeggio sample)
   ```
   (convention; clap backbeat + pitched hats sourced for OTR)
   - (b) Stomp-clap hybrid (Shaboozey-style), A major, felt ~81 half-time:
   ```
   Stomp/Kick X . . . | . . . . | X . . . | . . . .   (guitar-case stomp)
   GangClap   . . . . | X . . . | . . . . | X . . .   (felt backbeat)
   AcGtr      X . x x | . x x . | X . x x | . x x .   (16th strum)
   808        X . . . | . . . . | X . . . | . . . .   (sustained roots, added late)
   ```
   (convention; elements sourced from SOS)
7. **Bass**: 808 following chord roots with glides (trap camp) or upright/808 hybrid holding roots (sing-along camp) (convention; upright+808 sourced in SOS).
8. **Form**: Intro (banjo loop alone 4–8 bars) → hook (8) → verse (16, rap) → hook (8) → verse 2 (16) → hook → bridge/outro; 2:30–3:00 (trap norm) (convention).
9. **Production**: trap-loud low end; "A Bar Song" went roomy — mics 10–15 ft from acoustics, Valhalla Room on guitars, drum bus slightly clipped (Event Horizon), claps through tape — [SOS](https://www.soundonsound.com/techniques/inside-track-shaboozey-bar-song-tipsy) (sourced).
10. **Neighbours**: bro-country (rock guitars, less trap), hick-hop/country rap (rapping on country-rock beats, Colt Ford) — [Wikipedia](https://en.wikipedia.org/wiki/Country_rap) (sourced); Southern trap (no country instruments).
11. **FL Studio**
   - Chop or play a banjo/acoustic loop (Slicex/Fruity Slicer), pitch to key; 140 BPM half-time or 162/81 for sing-along.
   - Add clap on beat 3 (half-time), 16th hats with rolls (see trap notes), 808 tuned to roots.
   - Add country identity markers: fiddle answer phrases, steel swell, twangy hook vocal, gang claps/stomps recorded or sampled with room reverb.
   - The SOS producers avoided "lazy" trap-on-country — they built guitars/claps/roominess first and added the 808 last — [SOS](https://www.soundonsound.com/techniques/inside-track-shaboozey-bar-song-tipsy) (sourced). Mistakes: banjo loop with no other organic layer; 808 clashing with acoustic low end (HPF acoustics ~120 Hz).

---

#### CARD 8 — Americana / alt-country

1. **Identity**: Americana Music Association (2020) defines it as threads of country, folk, blues, soul, bluegrass, gospel and rock; earlier (2016) definition stressed a roots-oriented sound apart from the pure parent genres — [Wikipedia: Americana](https://en.wikipedia.org/wiki/Americana_(music)) (sourced). Alt-country solidified in the 1990s as artists rejected Nashville polish for lo-fi with punk/rock influence; Uncle Tupelo's "No Depression" (1990) credited as the first alt-country album; Wilco, Lucinda Williams, Gillian Welch; 2010s popularisers Mumford & Sons, The Lumineers, The Avett Brothers — [Wikipedia](https://en.wikipedia.org/wiki/Americana_(music)) (sourced). Current: Jason Isbell, Chris Stapleton, Sturgill Simpson, Tyler Childers, Zach Bryan (convention; Childers/Bryan sourced as country-derived folk-resurgence camp — [PSU Collegian](https://www.psucollegian.com/opinion/columnists/why-noah-kahan-style-folk-music-has-returned-to-mainstream-column/article_28113a22-16e6-11ee-aed6-ffa1185dc0da.html)). Reference tracks: Uncle Tupelo "No Depression", Lucinda Williams "Car Wheels on a Gravel Road", Jason Isbell "Cover Me Up", Zach Bryan "Something in the Orange" (convention).
   - Recognise by ear: band-in-a-room, acoustic + electric guitars, imperfect raw voice, literary lyrics, less compression and no programmed drums.
2. **Tempo**: 60–130 BPM, wide; ballads 60–80 common (convention).
3. **Harmony**: I–IV–V, vi minor colours, Mixolydian bVII, folk modal touches; open-chord voicings with drones (convention).
4. **Vocals**: unpolished, conversational, some grit/strain; storytelling detail (convention).
5. **Instrumentation**: acoustic guitar, banjo, fiddle, upright bass, often full electric band — [Wikipedia](https://en.wikipedia.org/wiki/Americana_(music)) (sourced); plus Hammond organ, pedal steel, harmonica (convention). DAW: real or sampled acoustic guitar; acoustic kit with brushes/rods; avoid snaps/808s (convention).
6. **Rhythm** (mid-tempo 4/4 ~96, rods/brushes):
   ```
   Kick   X . . . | . . . . | X . x . | . . . .
   Snare  . . . . | X . . g | . . . . | X . . .
   Hat    x . x . | x . x . | x . x . | x . x .
   AcGtr  X . x . | x . x x | X . x . | x . x x   (D . D . D . D U pattern, convention)
   ```
   (convention)
7–8. Bass: root/5th, few fills. Form: V–C–V–C–solo–C or strophic story songs 3–5 min; long instrumental outros (convention).
9. **Production**: live tracking, natural room, tape/analog warmth, moderate loudness (dynamic) (convention; "rejected polished production" sourced).
10. **Neighbours**: outlaw (more swagger/radio), indie folk (more reverb/indie textures), modern country pop (polished/programmed) (convention).
11. **FL**: record/sequence in one take feel — humanize timing ±10–20 ms, velocity variation; one room reverb for everything. Mistake: grid-perfect quantization, glossy vocal tuning.

---

#### CARD 9 — Traditional folk (British, Irish, Appalachian ballad tradition)

1. **Identity**: oral ballad and dance-tune traditions; Child Ballads = 305 English/Scottish ballads anthologised by Francis James Child in the late 19th century; Appalachian music blends Scots-Irish, English and African American traditions from 18th-century settlement — [Emory American Routes](https://scholarblogs.emory.edu/americanroutes/?p=399) / search summary (sourced). Ancient ballads often sung unaccompanied or with minimal accompaniment (sourced, same). Reference recordings: Jean Ritchie (Appalachian dulcimer), Shirley Collins, The Watersons, Frank Proffitt "Tom Dooley", Smithsonian Folkways field recordings ([Folkways FW02477](https://folkways-media.si.edu/docs/folkways/artwork/FW02477.pdf)) (convention).
   - Recognise by ear: solo voice telling a long story in many identical verses, modal melody (flat 7th), drone or no accompaniment, free/rubato rhythm.
2. **Tempo & feel**: ballads rubato/free or 3/4 / 6/8 lilt 60–100 BPM; dance tunes 100–130+ (convention).
3. **Harmony/modes**: Mixolydian and Dorian dominate, flattened 7th gives the ancient unresolved feel; pentatonic scales underpin many tunes — [Emory/search summary](https://scholarblogs.emory.edu/americanroutes/?p=399) (sourced; the summary may derive from tunee.ai, moderate confidence). Accompaniment minimal: drone on 1 and 5 (dulcimer/bagpipe), or I–bVII–I modal shifts (convention).
   - Ex. D Mixolydian drone: D5 drone with melody on D E F# G A B C; chord shifts D | C | D (convention). A Dorian: Am | G | Am | D (Dorian IV major) (convention).
4. **Melody & vocals**: strophic, many verses; ornaments are small grace notes/slides, unaccompanied "sean-nós" (Irish) melismatic decoration; plain unvibrato tone; Appalachian nasal "lonesome" tone (convention).
5. **Instrumentation**: voice; Appalachian: fiddle melody + clawhammer banjo rhythmic drone, interlocked fiddle with double stops — [Emory/search summary](https://scholarblogs.emory.edu/americanroutes/?p=399) (sourced); mountain (Appalachian) dulcimer, autoharp; British/Irish: concertina, melodeon, fiddle, pipes (convention).
6. **Rhythm**: ballads have no fixed grid (free); dance tunes see Celtic card. Drone accompaniment (12-step 3/4 example):
   ```
   Drone  X . . . | . . . . | . . . .   (sustained D+A, re-articulated each bar)
   Dulc   x . . . | x . . . | x . . .   (strum on each beat, melody on top string)
   ```
   (convention)
7. **Bass**: none or drone (convention).
8. **Form**: strophic (AAAA…), 8–20+ verses, sometimes refrain lines; no intro or one-line intro (convention).
9. **Production**: field-recording intimacy, mono or close-mic'd, no compression (convention).
10. **Neighbours**: folk revival (adds guitar accompaniment, topical songs); Celtic dance music (instrumental); old-time (fiddle-banjo string band) (convention).
11. **FL**: if no vocals, write a modal melody over a drone (Sytrus/any sine-saw pad set to a soft reed/bagpipe-like timbre or a fiddle sample held), slight tempo drift via automation. Mistake: functional pop chords under a modal tune (forces the major 7th).

---

#### CARD 10 — Folk revival / singer-songwriter (1940s–70s and contemporary)

1. **Identity**: 1940s–60s folk revival → folk rock (feeds Americana) — [Wikipedia: Americana](https://en.wikipedia.org/wiki/Americana_(music)) (sourced). Woody Guthrie is cited as a root of talking/country-rap delivery — [Wikipedia: Country rap](https://en.wikipedia.org/wiki/Country_rap) (sourced). Key artists: Woody Guthrie, Pete Seeger, Bob Dylan, Joan Baez, Joni Mitchell, James Taylor, Simon & Garfunkel (convention). Reference tracks: Dylan "Blowin' in the Wind", Joni Mitchell "A Case of You", James Taylor "Fire and Rain" (convention).
   - Recognise by ear: one voice + one acoustic guitar (maybe harmonica), lyric is the centre, simple chords strummed or Travis-picked.
2. **Tempo**: 70–130 BPM, rubato ballads; straight or lightly swung 8ths (convention).
3. **Harmony**: I–IV–V, I–vi–IV–V, descending bass lines (I–I/7–vi–IV), open tunings (Joni Mitchell) with drones (convention).
4. **Vocals**: speech-like, clear diction, little ornament; harmonica breaks between verses (convention).
5. **Instrumentation**: steel-string acoustic (Travis picking or flatpicked strum), harmonica, upright bass, light percussion (convention). Travis picking used by Dylan, Johnny Cash, Fleetwood Mac etc. — [MusicianWave](https://www.musicianwave.com/what-is-the-travis-picking-pattern-how-to-learn-it/) (sourced).
6. **Rhythm** (Travis pattern, see Card 14 grid). Strum: D . D U . U D U (classic "folk strum") (convention):
   ```
   Strum  X . . . | x . x . | . . x . | x . x .   (D, D U, U, D U  — "old faithful")
   ```
   (convention)
7–8. Bass usually from guitar thumb. Form: strophic or verse–chorus, 3–6 min, harmonica interludes (convention).
9. **Production**: close-mic'd acoustic + vocal, natural room, almost no processing (convention).
10. **Neighbours**: indie folk (more atmosphere/reverb/layers), traditional folk (older material, unaccompanied), Americana (band) (convention).
11. **FL**: acoustic guitar library with strum engine (or record), human timing; pan guitar slightly off-centre, vocal centre. Mistake: perfectly identical strum velocity, chorus/pad layers.

---

#### CARD 11 — Indie folk (and the 2020s folk-pop resurgence)

1. **Identity**: arose in the 1990s among indie-rock musicians influenced by folk; also called alternative folk, stomp and holler, or "stomp clap hey" — [Wikipedia: Indie folk](https://en.wikipedia.org/wiki/Indie_folk) (sourced). Key artists: Iron & Wine, Sufjan Stevens, Bon Iver, Fleet Foxes, Phoebe Bridgers, Big Thief, boygenius (convention; Bridgers/boygenius sourced as indie-pop-derived camp of the resurgence — [PSU Collegian](https://www.psucollegian.com/opinion/columnists/why-noah-kahan-style-folk-music-has-returned-to-mainstream-column/article_28113a22-16e6-11ee-aed6-ffa1185dc0da.html)). Noah Kahan's "Stick Season" went viral on TikTok in 2022 and was the UK's first #1 of 2024 (5 Jan 2024) — [Wikipedia: Noah Kahan](https://en.wikipedia.org/wiki/Noah_Kahan) (sourced). Resurgence has two camps: country-derived (Tyler Childers, Zach Bryan) and indie-pop-derived (Kahan, Bridgers, boygenius); folk "often doesn't have a heavily produced sound" — [PSU Collegian](https://www.psucollegian.com/opinion/columnists/why-noah-kahan-style-folk-music-has-returned-to-mainstream-column/article_28113a22-16e6-11ee-aed6-ffa1185dc0da.html) (sourced, opinion column). Reference tracks: Bon Iver "Skinny Love", Fleet Foxes "White Winter Hymnal", Noah Kahan "Stick Season" (convention).
   - Recognise by ear: intimate fingerpicked/strummed acoustic, breathy or falsetto vocal, stacked choral harmonies, lots of reverb/room, quiet → swelling dynamics.
2. **Tempo**: 60–120 BPM, default ~90; often 6/8 or 3/4 (convention).
3. **Harmony**: diatonic but with sus2/add9, open tunings, IV–I plagal, vi–IV–I–V; occasional modal mixture (iv minor) (convention).
4. **Vocals**: breathy, falsetto (Bon Iver), close harmonies in 3rds and unison doubles, rounds/canons (Fleet Foxes); confessional lyrics (convention).
5. **Instrumentation**: acoustic guitar, banjo, piano/upright, strings, horns (Sufjan), ambient textures, sparse percussion, sometimes vocoder/Prismizer (Bon Iver) (convention). DAW: acoustic library + reverb-heavy piano (FL Keys with soft felt-like EQ), Vocodex for harmonised vocal effects (convention).
6. **Rhythm** (6/8 indie-folk lilt; 12 steps = 2 bars of 6/8 at 8th level):
   ```
   FloorTom X . . x . . | X . . x . . |
   Shaker   x x x x x x | x x x x x x |
   Guitar   X . x x . x | X . x x . x |   (fingerpicked 6/8 arpeggio)
   ```
   (convention)
7–8. Bass sparse/ sustained; form: verse–chorus or through-composed builds; 3–5 min, long fades (convention).
9. **Production**: lo-fi to cinematic; heavy plate/hall reverb, tape saturation, room mics; moderate loudness (convention).
10. **Neighbours**: stomp-clap folk-pop (more anthemic, four-on-floor), singer-songwriter (drier, single instrument), Americana (band/country leanings) (convention).
11. **FL**: build from one acoustic pattern, add vocal stacks, swell strings via volume automation; room reverb + tape (Fruity Waveshaper light / any tape sat). Mistake: dense drum programming, bright hyped EQ.

---

#### CARD 12 — Folk-pop / stomp-clap ("stomp and holler", c. 2009–2014 and revivals)

1. **Identity**: strain of indie folk from the early 2010s; terms "stomp and holler", "stomp clap hey", "hoedown pop" coined retrospectively — [Wikipedia: Indie folk](https://en.wikipedia.org/wiki/Indie_folk) (sourced). The Lumineers, Mumford & Sons, The Head and the Heart led via foot-stomp percussion, driving guitar and banjo, and builds from soft verses to howled choruses — [Rolling Stone AU](https://au.rollingstone.com/music/music-features/mumford-and-sons-lumineers-folk-stomp-74308) (sourced). Known for catchy simple melodies, stomping rhythms, and shouted "hey/oh/woah" — [Substack: Stomp and Holler](https://reidht.substack.com/p/every-genre-project-july-31-stomp) (sourced, low-authority). Reference tracks: The Lumineers "Ho Hey", Mumford & Sons "Little Lion Man", Of Monsters and Men "Little Talks", Edward Sharpe "Home" (convention).
   - Recognise by ear: kick-drum/stomp on every beat, hand claps, "hey!" shouts, frantically strummed acoustic + banjo, gang chorus.
2. **Tempo**: 80–150 BPM (convention); often fast strumming with half-time vocal; straight 8ths.
3. **Harmony**: 3–4 major chords (I–IV–I–V, I–V–vi–IV), drone-y open chords, suspended chords (Mumford DADGAD/open tunings) (convention).
4. **Vocals**: shouted, raw, gang unison "hey"/"ho" call-and-response (convention; sourced shouts above).
5. **Instrumentation**: acoustic guitar, banjo, upright bass, kick drum played by foot (Mumford), tambourine, claps, glockenspiel, piano, trumpet (convention). DAW: real stomp samples (wood floor), layered claps with room reverb, tambourine loop (convention).
6. **Rhythm** (4/4 ~ 130, chorus):
   ```
   Kick/Stomp X . . . | X . . . | X . . . | X . . .   (four-on-the-floor stomp)
   Clap       . . . . | X . . . | . . . . | X . . .
   Tamb       x . x . | x . x . | x . x . | x . x .
   Shout      . . . . | . . . . | . . . . | X . . .   ("hey!" on beat 4 / end of phrase)
   AcGtr      X x x x | X x x x | X x x x | X x x x   (driving 16th strum, accent each beat)
   Banjo      x . x . | x . x . | x . x . | x . x .   (rolls/8ths)
   ```
   (convention)
7. **Bass**: upright, root on each beat or 1 & 3 (convention).
8. **Form**: quiet intro (voice+guitar) → verse → build (kick enters) → big gang chorus → breakdown → final chorus double-time; 3–4 min (convention, builds sourced above).
9. **Production**: roomy, gang vocals with distance, mid-forward acoustic, moderate compression; parallel compression on stomps (convention).
10. **Neighbours**: indie folk (softer, more reverb, less stomp), country trap stomp-clap hybrid (Shaboozey adds 808) (derived).
11. **FL**: stomp sample on all quarters, claps 2 & 4 with hall send, "hey" vocal chops at phrase ends; 16th acoustic strums with accents on beats; use automation to drop the kick for verses. Mistake: electronic claps/808 kick (sounds EDM), too clean.

---

#### CARD 13 — Celtic music (Irish/Scottish traditional dance music)

1. **Identity**: Irish/Scottish traditional dance and air repertoire; instruments: fiddle, tin whistle, uilleann pipes, bodhrán, harp, bouzouki, concertina, flute, accordion, guitar — [Wikipedia: Gaelic folk music](https://en.wikipedia.org/wiki/Gaelic_folk_music) / search summary (sourced). Reference: The Chieftains, The Bothy Band, Planxty, Altan, Lúnasa; Scottish: Capercaillie; tunes "The Kesh" (jig), "The Silver Spear" (reel) (convention).
   - Recognise by ear: fast fiddle/whistle unison melody in running 8ths with rolls and cuts, bodhrán pulse, DADGAD guitar/bouzouki drones, Dorian/Mixolydian colour.
2. **Tempo & feel**: jigs 6/8, reels 4/4 (cut time), airs free — (sourced, [Gaelic folk music](https://en.wikipedia.org/wiki/Gaelic_folk_music)/search summary); reels "around 130 BPM" ([tunee.ai](https://www.tunee.ai/music-generator/celtic), weak source; beat unit ambiguous — see Gaps). Other dance types: slip jig 9/8, hornpipe (swung/dotted 4/4, slower), polka 2/4, slide 12/8, strathspey (Scottish, "Scotch snap" short-long) (convention).
3. **Harmony/modes**: Ionian, Dorian, Mixolydian, Aeolian dominate; session keys D, G (Ionian), A and E Dorian — [search summary/greylarsen](https://greylarsen.com/revisions/minorchanges/p.26.pdf) (sourced). Accompaniment: modal drones, power-chord (no 3rd) voicings in DADGAD so they fit both major and minor; double-tonic shifts (I–bVII in Mixolydian, i–bVII in Dorian) (convention).
   - Ex. E Dorian reel: Em | D | Em | D | Em | D | G | Bm/D... ; A Mixolydian: A | G | A | G | D | A (convention)
4. **Melody & ornaments**: cut = very quick grace note from above; rolls built from main note–cut–main–tap–main; cuts/taps are articulations "built in" to tunes rather than extras — [irishtune.info / chiffandfipple](https://www.irishtune.info/rhythm/reel-structure.html) and search summary (sourced). Ornamentation is a decisive stylistic marker — [Springer article](https://link.springer.com/article/10.1007/s00799-019-00267-2) (sourced). Also bowed triplets, crans (pipes), slides (convention). Melodies: stepwise running 8ths, arpeggio outlines, range ~2 octaves on fiddle (convention).
5. **Instrumentation**: as above. DAW: tin whistle / uilleann pipe / fiddle sample libraries (ethnic/Celtic packs), bodhrán samples (low "boom" + high tipped rim); DADGAD guitar library or pluck synth; drones = held pipe drones or sustained fifth pad (convention).
6. **Rhythm**
   - Jig (6/8, 12 steps = 2 bars, each bar 2 beats × 3 8ths):
   ```
   Bodhrán  X . x x . x | X . x x . x |   (DOWN-up-down per beat; accent each dotted quarter)
   Guitar   X . x X . x | X . x X . x |   (strum D . U D . U)
   Melody   x x x x x x | x x x x x x |   (running 8ths, rolls on long notes)
   ```
   - Reel (4/4, 16 steps; melody in continuous 8ths = odd steps):
   ```
   Bodhrán  X . x . x . x . | (repeat)  → X on 1 and 9, light x on other 8ths
   Guitar   X . . x . . x . | X . . x . . x .   (3+3+2 push accompaniment common in DADGAD backing)
   Melody   x . x . x . x . | x . x . x . x .   (continuous 8ths, slight long-short lilt)
   ```
   - Slip jig 9/8 (9 steps): `X . x X . x X . x`
   (all convention)
7. **Bass**: often none; bouzouki/guitar root drones; modern bands add bass on root/5th (convention).
8. **Form**: reels have two 8-bar parts A and B; "doubled" = each part repeated (AABB) — [irishtune.info](https://www.irishtune.info/rhythm/reel-structure.html) (sourced). Each tune typically played 3 times, then changed into the next tune in a set of 2–3 (convention). Airs: free-time, slow.
9. **Production**: acoustic, natural; modern "Celtic fusion" adds drum kit, pads (convention).
10. **Neighbours**: Appalachian old-time (descended, banjo-centred, more syncopated), Celtic punk (Pogues/Dropkick Murphys: punk drums + whistle/accordion), Celtic new age (Enya: pads, choirs) (convention).
11. **FL**: write AABB 8-bar strains in D major/E Dorian; add cuts as 1/32 grace notes above the main note (vel lower), rolls as 5-note figures; bodhrán in 6/8 triplet grid; drone pad on tonic+5th. Mistakes: functional ii–V harmony, quantizing jigs to straight 16ths (needs 6/8 triplet grid), adding vibrato everywhere (trad players use little).

---

#### CARD 14 — Acoustic / fingerstyle guitar

1. **Identity**: Travis picking (named after Merle Travis) — the most widely used fingerpicking technique; thumb alternates between two bass notes in steady 8ths (palm-muted) while fingers pick melody on top strings, on or between the bass notes; used by Dylan, Johnny Cash, Fleetwood Mac, Led Zeppelin — [Guitar World](https://www.guitarworld.com/lessons/how-fingerpick-merle-travis); [MusicianWave](https://www.musicianwave.com/what-is-the-travis-picking-pattern-how-to-learn-it/) (sourced). Chet Atkins extended the style (convention). Modern percussive fingerstyle: Tommy Emmanuel, Andy McKee (tapping/body hits), open tunings (DADGAD, open D/G) (convention).
   - Recognise by ear: steady alternating bass "boom-boom" with syncopated treble melody from one guitar.
2. **Tempo**: 70–140 BPM; straight or lightly swung 8ths (convention).
3. **Harmony**: open-position chords, moving bass under static shapes, harmonics, open-string drones (convention).
4. **Melody**: melody on top strings, often pinched with bass; hammer-ons, pull-offs, slides; harmonics at 12th/7th/5th frets (convention).
5. **Instrumentation**: one steel-string or nylon guitar. DAW: multi-sample acoustic guitar libraries with separate bass/treble note articulations; or FL "FLEX"/DirectWave acoustic presets (convention).
6. **Rhythm** (Travis pattern in C, 16 steps):
   ```
   ThumbLow  X . . . | x . . . | X . . . | x . . .   (root bass, e.g. C on 5th string, on every beat)
   ThumbHigh . . x . | . . x . | . . x . | . . x .   (alternate bass, e.g. E/G on 4th/3rd string, on the "&"s)
   Finger    . . . x | . x . . | . . . x | . x . .   (melody/treble notes in between, syncopated 16ths)
   ```
   i.e. the thumb plays every 8th (steps 1,3,5,…,15) alternating low/high bass, and fingers add treble notes on in-between 16ths (here steps 4, 6, 12, 14) (convention, consistent with sourced description of 8th-note thumb + in-between 16ths).
7. **Bass**: the thumb is the bass: root on beats 1 & 3, alternate (5th/3rd string) on 2 & 4 (convention).
8. **Form**: instrumental AABA or verse–chorus; percussive fingerstyle has intro riffs, tapped sections (convention).
9. **Production**: stereo pair (SDC at 12th fret + LDC/ribbon body or pickup blend), light compression, plate/hall reverb (convention).
10. **Neighbours**: classical guitar (nylon, no alternating bass), flatpicking (bluegrass lead with pick), percussive fingerstyle (body slaps on 2 & 4) (convention).
11. **FL**: separate bass notes (thumb) and treble notes on different channels/velocity layers; thumb vel 80–95 palm-muted (short), treble 90–110; humanize ±10 ms. Mistake: all notes same velocity/length, letting palm-muted bass ring.

### Inferences
- The fastest way to "flip" genre with the same chord progression is to swap the rhythm cell and the lead timbre: e.g. G–C–D in two-beat + steel/fiddle = honky-tonk; same with chop/banjo rolls/no drums at 170 BPM = bluegrass; same with stomp four-on-floor + claps + "hey" = stomp-clap; same with banjo loop + half-time clap + 808 = country trap (derived from cards above).
- The 2024–26 country-rap boom has two distinct production models: the "OTR model" (sample loop + stock trap drums) and the "Bar Song model" (organic, roomy, acoustic-first with an 808 added at the end) (derived from SOS and Songfacts/Billboard).

### Gaps
- No sourced BPMs/keys for most classic reference tracks (only "A Bar Song" 162 BPM/A major and "Blue Grass Breakdown" 175 BPM from weak aggregators). Tempo ranges marked (convention) should be checked against a tempo database (e.g., SongBPM/Tunebat) before being hard-coded.
- Billboard's 2026 "Country's Rap Revival" article was paywalled (HTTP 402); details come from the search snippet only.
- A "67% increase in country-rap tracks on streaming 2025 vs 2023" stat appeared only on spammy "web log free" pages — excluded as unreliable.
- Reel tempo: "~130 BPM" source does not specify quarter vs half-note beat; session tempos vary greatly.

---

## Key question 2 — Groove library: train beat, two-step/boom-chicka, shuffle, waltz, bluegrass chop, stomp-clap (grids)

### Takeaway
Six cells cover nearly all of the family: train beat (snare 16ths, accents 2 & 4), two-beat boom-chick (bass 1 & 3, strum/snare 2 & 4), shuffle (triplet long-short), waltz (3/4 oom-pah-pah), bluegrass (bass 1 & 3 + mandolin chop 2 & 4 + banjo 8ths, no drums), and stomp-clap (four-on-floor stomp + claps 2 & 4).

### Cited Findings
- **Train beat**: steady 8th (or 16th) notes with no pulse inconsistency; snare carries accents, kick follows the bass; most famous on Johnny Cash's "Folsom Prison Blues"; also Brad Paisley and Jason Aldean; often played with brushes — [PAS](https://pas.org/pas-blog/country-music-grooves-variations-on-the-classics/); [Andy Guitar](https://andyguitar.co.uk/videos/lesson-7-acoustic-rhythm) (sourced). Guitar train-beat strum: D, D, U, D, U, D, U with accents on 2 and 4 — [Andy Guitar](https://andyguitar.co.uk/videos/lesson-7-acoustic-rhythm) (sourced).
  ```
  4/4, 100–140 BPM (convention)
  Snare(brush) g g g g | X g g g | g g g g | X g g g   (16ths, accents 2 & 4)
  Kick         X . . . | . . . . | x . . . | . . . .   (with bass, 1 & 3)
  Bass         X . . . | . . . . | x . . . | . . . .
  Gtr strum    D . . . | D . U . | D . U . | D . U .   (sourced stroke order; X accents on steps 5 & 13)
  ```
  Variant (cut-time "chugga-chugga"): accent the offbeat 8ths (steps 3, 7, 11, 15) instead (convention). Grid placement = derived from sourced description.
- **Boom-chicka / two-beat**: bass note beat 1, strum beat 2 and &2, bass beat 3, strum 4 and &4 — [AcousticLife](https://acousticlife.tv/guitar-strumming-patterns-the-boom-chicka/) (sourced). Honky-tonk rhythm section plays "a two-beat rhythm with a crisp backbeat" — [Wikipedia](https://en.wikipedia.org/wiki/Honky-tonk) (sourced). Grid in Card 1.
- **Shuffle**: Buck Owens "Under Your Spell Again" and Loretta Lynn "Coal Miner's Daughter" as examples; lighter variation for fast tempos, heavier for slow — [PAS](https://pas.org/pas-blog/country-music-grooves-variations-on-the-classics/) (sourced).
  ```
  12/8 grid (4 beats × 3 triplet steps), 100–150 BPM (convention)
  Ride/Hat  X . x | X . x | X . x | X . x   (long-short)
  Snare     . . . | X . . | . . . | X . .
  Kick      X . . | . . . | X . . | . . .
  Bass      X . . | x . . | X . . | x . .   (walking quarters: 1–3–5–6 or root–5)
  ```
  In FL 16-step grid: equivalent to swing ~66% on 8ths (convention; see earlier drums notes).
- **Country waltz**: Patti Page "Tennessee Waltz", Hank Williams "The Alabama Waltz"; basic quarter-note pattern on snare or hi-hat, embellish later with left-foot hats, extra kicks and snare ghosts, or brushes — [PAS](https://pas.org/pas-blog/country-music-grooves-variations-on-the-classics/) (sourced).
  ```
  3/4, 12 steps (3 beats × 4 sixteenths); 90–150 BPM (convention)
  Kick         X . . . | . . . . | . . . .
  Snare(brush) . . . . | x . . . | x . . .
  Hat(foot)    . . . . | x . . . | x . . .
  Bass         X . . . | . . . . | . . . .   (root bar 1, fifth bar 2)
  GtrBass/Strum X . . . | x . . . | x . . .  ("boom–chick–chick")
  ```
- **Bluegrass offbeat chop**: mandolin chop (muted chord) gives the backbeat, bass on on-beats, banjo steady 8ths — [Wikipedia: Chop chord](https://en.wikipedia.org/wiki/Chop_chord) (sourced). Grid in Card 3.
- **Stomp-clap**: foot-stomp percussion, driving guitar/banjo — [Rolling Stone AU](https://au.rollingstone.com/music/music-features/mumford-and-sons-lumineers-folk-stomp-74308) (sourced). Grid in Card 12.
- **Celtic jig/reel/slip-jig grids**: Card 13. **Travis picking grid**: Card 14. **Country-trap half-time grid**: Card 7.

### Inferences
- In acoustic country/bluegrass the "drum kit" job is distributed: bass = kick (1 & 3), chop/strum = snare (2 & 4), banjo/guitar = hats (8ths). When programming without drums, keep those three layers' velocities distinct (derived).
- Train beat and bluegrass both depend on unbroken, even subdivisions; humanize timing only slightly (±5 ms) but vary velocity more (derived from PAS "no inconsistencies in the pulse").

### Gaps
- PAS article's notation figures were images; exact kick variations not extractable as text. Grids above are reconstructions consistent with the text.

---

## Key question 3 — Harmony & melody habits: I–IV–V, Mixolydian, Nashville numbers, pentatonics, pedal-steel bends, Celtic modes & ornaments

### Takeaway
Most country/folk harmony is diatonic triads (I–IV–V, plus vi and II7) with Mixolydian bVII as the "rock/outlaw/Celtic" colour; melodies are major-pentatonic with blue-3rd slides; the instrument idioms (pedal-steel pedal moves, banjo rolls, Celtic cuts/rolls) carry the genre more than chord choice.

### Cited Findings
- **Nashville Number System**: chords as scale-degree numbers (C=1, D=2 … B=7 in C); minor shown as 2- or 6-; a diamond = strike and hold (whole note/"football"); ">" above a number = "push" (played on the "and" before the beat); an underline groups numbers sharing one bar — [MusicianWave](https://www.musicianwave.com/nashville-number-system/); [Premier Guitar](https://www.premierguitar.com/pro-advice/the-nashville-number-system-demystified) (sourced). Use it as the composer-AI's internal chord representation so the same chart transposes to any key (derived).
  - Example chart (convention): `1 1 4 1 | 1 1 5 5 | 1 1 4 4 | 1 5 1 1` (honky-tonk verse); modern pop-country `1 5 6- 4`; bluegrass "salty dog" `1 6 2 5 1` (6 and 2 as major/dominant).
- **Modes**: Mixolydian and Dorian dominate Appalachian and Celtic music; pentatonic scales underpin many tunes — [Emory/search summary](https://scholarblogs.emory.edu/americanroutes/?p=399) (sourced); Celtic: Ionian, Dorian, Mixolydian, Aeolian; session keys D & G Ionian, A & E Dorian — [Grey Larsen PDF](https://greylarsen.com/revisions/minorchanges/p.26.pdf)/search summary (sourced).
- **Pedal steel**: pedals/knee levers raise or lower specific strings by precisely a half or whole step; some strings in a chord move while others stay — the signature sound; perfectly in-tune bends, smooth portamentos and chord vibrato — [Guitar Player](https://www.guitarplayer.com/lessons/how-to-mimic-the-sound-of-pedal-steel-on-electric-guitar); [NIME 2023](https://nime.org/proceedings/2023/nime2023_57.pdf) (sourced). MIDI emulation trick: use 3 MIDI channels with the same patch, each set to bend a different interval, so only some voices bend — [Yamaha Synth forum](https://yamahasynth.com/community/modx-series-synthesizers/pedal-steel-guitar-emulation) (sourced).
  - Classic E9 "A+B pedal" move (convention): pressing both raises the 5th of the I chord a whole step and the 3rd a half step while the root holds → I becomes IV (in C: C-E-G → C-F-A). Program: hold C; slide E→F and G→A over ~150–300 ms; swell volume in (steel attack is usually faded in with the volume pedal) (convention; consistent with sourced "some strings move while others stay").
- **Banjo roll** = repeating 8th-note arpeggio that keeps time — [Wikipedia](https://en.wikipedia.org/wiki/Banjo_roll) (sourced); forward roll from Earl Scruggs — [Deering](https://blog.deeringbanjos.com/the-four-essential-5-string-banjo-rolls) (sourced).
- **Celtic ornaments**: cut = quick grace from above; rolls built of cuts and taps; considered articulations built into the tune — [irishtune.info](https://www.irishtune.info/rhythm/reel-structure.html); [Chiff & Fipple](https://www.chiffandfipple.com/t/adding-ornamentation/53198) (sourced).
- **Vocal conventions**: high lonesome tenor (bluegrass, sourced Britannica); nasal (early honky-tonk) vs crooning (Nashville sound) (sourced Wikipedia pages).

### Inferences
- Melody rule for "country-sounding" toplines: major pentatonic (1-2-3-5-6) + slide b3→3 on accented syllables + end phrases on 1 or 5 approached from 6 or 2 (derived from pentatonic + blue-note conventions).
- For Celtic tunes, prefer double-tonic harmony (I–bVII or i–bVII alternating every bar) to avoid the leading tone clash with modal melodies (derived).

### Gaps
- No primary-source (e.g., academic) quantification of chord-progression frequencies in country; progressions given are convention.
- No verified technical spec for pedal-steel bend timing; 150–300 ms is a producer convention.

---

## Key question 4 — Instrumentation & DAW emulation; song forms & storytelling; how modern country production changed (808s, trap hats)

### Takeaway
Acoustic instruments must be emulated via articulation-rich sample libraries plus idiomatic programming (rolls, chops, slides, swells). Country song forms are short verse–chorus story songs with instrumental breaks; modern Nashville since ~2012 added loops, snaps, 808s and trap hats, peaking in the 2024–26 country-rap wave, while a parallel folk/Americana camp went the opposite way (raw, live).

### Cited Findings
- **Instrument roles**: honky-tonk = steel + fiddle dominant ([Wikipedia](https://en.wikipedia.org/wiki/Honky-tonk)); Bakersfield = twin picked Telecasters, big drum beat, fiddle, occasional steel solo ([Wikipedia](https://en.wikipedia.org/wiki/Bakersfield_sound)); Nashville sound = strings, background vocals, crooning ([Wikipedia](https://en.wikipedia.org/wiki/Nashville_sound)); bluegrass = banjo rolls, mandolin chop, on-beat bass ([Wikipedia: Chop chord](https://en.wikipedia.org/wiki/Chop_chord)); Appalachian = fiddle melody + clawhammer banjo drone ([Emory](https://scholarblogs.emory.edu/americanroutes/?p=399)); Celtic = fiddle, whistle, uilleann pipes, bodhrán, harp, bouzouki, concertina, flute, accordion ([Wikipedia: Gaelic folk music](https://en.wikipedia.org/wiki/Gaelic_folk_music)) (all sourced).
- **Emulation tools**: sampled pedal steel libraries with sustain/harmonic/legato/vibrato/bend articulations and auto slide/vibrato — [Impact Soundworks](https://impactsoundworks.com/product/pedal-steel/?isw=4) (sourced); multi-channel pitch-bend trick (sourced above); faux-steel on guitar via bends/volume swells — [Guitar Player](https://guitarplayer.com/lessons/learn-the-faux-pedal-steel-technique) (sourced).
- **Real-world hybrid recipe ("A Bar Song (Tipsy)")**: 30+ acoustic guitar tracks (incl. Nashville high-strung), banjo, Splice fiddle loop + live fiddle, no drum kit — programmed drums from own samples, guitar-case kick stomps, brushes, hallway gang claps; upright bass in chorus, piano, Farfisa/B3 on final hook; 808 added in the last month; a mono acoustic bus tucked under panned guitars; Valhalla Room/Flamingo Verb for a saloon feel; Ableton + Pro Tools; Event Horizon clipping on drum bus — [Sound On Sound](https://www.soundonsound.com/techniques/inside-track-shaboozey-bar-song-tipsy) (sourced).
- **"Old Town Road" recipe**: sped-up banjo sample, tuned 808 as bass, pitched hi-hat layers, simple clap backbeat — [Songfacts](https://www.songfacts.com/facts/lil-nas-x/old-town-road) (sourced).
- **Production shift timeline**: Nashville sound (1950s–60s) added pop polish ([Wikipedia](https://en.wikipedia.org/wiki/Nashville_sound)); Bakersfield (late '50s–60s) electric/backbeat ([Wikipedia](https://en.wikipedia.org/wiki/Bakersfield_sound)); 1990s alt-country rejected polish for lo-fi ([Wikipedia: Americana](https://en.wikipedia.org/wiki/Americana_(music))); 2012–13 bro-country added hip-hop/rock/electronica ([Wikipedia: Bro-country](https://en.wikipedia.org/wiki/Bro-country)); 2018 Wallen's debut used snap tracks and 808 beats ([Whiskey Riff](https://www.whiskeyriff.com/?p=642128)); 2019 country trap via OTR ([Wikipedia: Country rap](https://en.wikipedia.org/wiki/Country_rap)); 2024–26 country-rap revival, trap drums/808s as a "shared language" ([Billboard](https://www.billboard.com/music/country/country-rap-crossover-hits-trend-1235983104/), snippet) (sourced).
- **Counter-trend**: folk/Americana resurgence with raw, minimally produced sound — two camps (Childers/Bryan; Kahan/Bridgers/boygenius) — [PSU Collegian](https://www.psucollegian.com/opinion/columnists/why-noah-kahan-style-folk-music-has-returned-to-mainstream-column/article_28113a22-16e6-11ee-aed6-ffa1185dc0da.html) (sourced, opinion).
- **Forms**: reels/jigs AABB 8-bar strains ([irishtune.info](https://www.irishtune.info/rhythm/reel-structure.html), sourced); Child ballads strophic, often unaccompanied (sourced, Emory summary). Country/bluegrass forms in cards = convention.
- **Storytelling**: honky-tonk lyrics on lost love, adultery, loneliness, alcoholism ([Wikipedia](https://en.wikipedia.org/wiki/Honky-tonk)); bro-country on trucks, drinking, partying ([Wikipedia](https://en.wikipedia.org/wiki/Bro-country)); country and rap share heartbreak, life stories and struggle themes ([Billboard snippet](https://www.billboard.com/music/country/country-rap-crossover-hits-trend-1235983104/)) (sourced). Common country storytelling devices (convention): title hook repeated as the chorus's last line; each verse advances time (youth → adulthood → death); final-chorus "twist" where the same hook line takes a new meaning; concrete nouns (brand names, place names) over abstractions.

### Inferences
- For a composer-AI, a generic "country production stack" in FL: (1) acoustic 16th strum ×2 panned L/R + quiet mono copy, (2) bass on 1 & 3 (or 808 for trap), (3) snare/snap/clap on 2 & 4 (or 3 for half-time trap), (4) one signature lead (steel/fiddle/banjo/Tele) answering vocal phrases, (5) genre-specific room/reverb amount (dry outlaw → plate Nashville → roomy stomp-clap/indie) (derived).
- Era tells: strings/choir = 1960s; Tele+slapback = Bakersfield; snaps + loops = 2012–18 bro/pop; 808 + trap hats + banjo loop = 2019–26 country trap (derived).

### Gaps
- No verified loudness (LUFS) figures for country masters found; mix-loudness statements are convention.
- No primary interview with Joey Moi/Charlie Handsome on exact drum programming; the 808/Telecaster layering claim came from a low-quality aggregator page.
- Did not find authoritative tempo surveys for modern country radio singles.
