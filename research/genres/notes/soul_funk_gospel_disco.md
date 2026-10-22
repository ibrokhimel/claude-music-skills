# Soul, Funk, Gospel & Disco (and descendants): genre recipe cards for FL Studio

Scope: traditional and contemporary gospel/CCM, doo-wop, Motown, Southern/Memphis soul (Stax), Philly soul, funk (James Brown, P-Funk), disco, boogie/post-disco, new jack swing, 90s R&B/hip-hop soul (brief), neo-soul, nu-disco/French touch, modern funk/city-pop revival. Modern R&B, house, boom bap and lo-fi are covered in the earlier notes (`research_notes/Music theory and beat making/genres_hiphop_urban_global.md`, `genres_electronic_pop_cinematic.md`). This file only cross-references them.

Grid notation (from the card format): 16 steps per bar in 4 groups. Step 1 = beat 1, 5 = beat 2, 9 = beat 3, 13 = beat 4. X = accent, x = normal, g = ghost, o = open hat, . = rest. 12/8 grids use 12 steps (4 groups of 3). Number tags: (sourced) = cited, (convention) = standard producer practice that I did not find in a source this session, (derived) = my own working from a cited description. FL timing: the default piano-roll PPQ is 96, so one 16th note = 24 ticks (convention).

## Genre recipe cards (objective: one card per style, so a composer-AI can write each style and tell them apart)

### Takeaway
The family splits along four axes you can hear. (1) **Where the weight sits in the bar:** funk leans on beat 1, Motown/Stax/boogie on the 2-and-4 backbeat, disco/Philly/French touch on four-on-the-floor plus an open hat on the "&". (2) **Swing amount:** near-straight for disco, Motown and French touch. Light swing for funk and boogie. Heavy swung 16ths/triplets for new jack swing. Unquantized and "drunk" for neo-soul. (3) **Harmonic density:** one-chord dominant/minor vamps in funk. Lush maj7/m9 with strings in Philly. Passing-chord-heavy in gospel. Looped m9/m11/maj13 cycles in neo-soul. (4) **Live band vs machine:** live band for Motown/Stax/Philly/funk/disco. Drum machine/synth bass for boogie, NJS and modern funk. Sample loop plus filter for French touch.

### Cited Findings

#### CARD 1: Funk (James Brown "on the one", 1965–1975)
1. **Identity:** Developed by James Brown in the mid-1960s. It rests on interlocking contrapuntal parts: syncopated bass, 16th-beat drum patterns and syncopated guitar riffs — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). Reference tracks: "Cold Sweat" (1967), "Mother Popcorn" (1969), "Get Up (I Feel Like Being a) Sex Machine" (1970) — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk), and "Funky Drummer" (1969) — [Wikipedia: Funky Drummer](https://en.wikipedia.org/wiki/Funky_Drummer). Neighbours: The Meters "Cissy Strut", Earth Wind & Fire "September" — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). **By ear:** one chord for minutes, a huge downbeat on 1, trebly scratchy guitar, the bass as the hook, horns as percussion.
2. **Tempo & feel:** Mixgraph's measured median is 118 BPM, with an interquartile range of 105–124 across only 21 tracks. Its editorial range is 90–110 BPM — [Mixgraph: Funk BPM](https://www.mixgraph.io/bpm-for/funk) (sourced, small sample). Working default: 100–112 BPM for JB funk, 95–108 for P-Funk (convention). The feel uses swung or syncopated 16ths with a heavy beat 1 — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). Swing: MPC 54–58% or FL swing knob ~15–30 (convention).
3. **Harmony:** Funk uses bebop-style extended chords. Examples are minor 11th (Fm11), 7#9sus4 (C7(#9)sus4), dominant 9 (F9), minor 6 (Cm6) and 6/9 (F6/9). Minor 7ths are preferred over minor triads — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). "Cold Sweat" has only one definite chord change, a move to the subtonic at the bridge — [Wikipedia: Cold Sweat](https://en.wikipedia.org/wiki/Cold_Sweat). Spelled (derived): verse vamp D9 (I9 = D F# A C E) for 8–16+ bars, bridge C9 (bVII9 = C E G Bb D), then back. "Funky Drummer" is in D minor, with the first verse in C major — [Wikipedia: Funky Drummer](https://en.wikipedia.org/wiki/Funky_Drummer). Second vamp archetype (derived): Dm7 to G7/G9 (i7–IV7 Dorian). Harmonic rhythm: one chord per 4–16+ bars (derived from the "one change" description).
4. **Melody & vocals:** Brown sang anthemic lines over long vamps and used his voice as a percussion instrument, with rhythmic grunts and patterns resembling West African polyrhythm — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). Melodies come from the blues/minor pentatonic with the major 3rd above the root, which the basslines also use — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk).
5. **Instrumentation:** Electric bass, clean trebly guitar(s), drums, a horn section (tenor sax, trumpet, trombone, plus bari sax in bigger sections), and organ/clavinet — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). Jimmy Nolen's tone: hollow-body jazz guitar with P-90 single coils into a Fender Twin Reverb, mids low and treble high, no distortion — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). DAW: a funk drum kit (FPC with a dry 70s kit, or sampled breaks), a bass-guitar library (Scarbee/MODO Bass, or FL BooBass as a fallback), a clean single-coil guitar library or loops, a horn-section library (brass stabs), and FL Keys or a clavinet emulation (convention).
6. **Rhythm (derived from "Cold Sweat": two-bar pattern, snare on 2 and 4, but bar 1's beat-4 snare is delayed by one eighth — [Wikipedia: Cold Sweat](https://en.wikipedia.org/wiki/Cold_Sweat)):**
   ```
   Bar 1  Kick  X . . . | . . . . | x . x . | . . . .
          Snare . . . . | X . . g | . g . . | . . X .   <- beat-4 snare pushed to step 15
          Hat   X x x x | X x x x | X x x x | X x x x
   Bar 2  Kick  X . . . | . . . . | x . x . | . . . .
          Snare . . . . | X . . g | . g . . | X . . g
          Hat   X x x x | X x x x | X x x x | X x x x
   ```
   Funky-Drummer-*inspired* ghost-note groove (derived, not a transcription). The break is an 8-bar unaccompanied version of Stubblefield's main riff and among the most-sampled recordings ever — [Wikipedia: Funky Drummer](https://en.wikipedia.org/wiki/Funky_Drummer):
   ```
   Kick  X . x . | . . . . | . . x . | . x . .
   Snare . . . . | X . . g | . g . g | X . . g
   Hat   x x x x | x x x o | x x x x | x o x x
   ```
   Chicken-scratch guitar on one chord (X = chord stab, g = muted scratch, every 16th strummed down-up) (derived from [Premier Guitar](https://www.premierguitar.com/lessons/rhythm/how-to-play-funk-guitar)):
   ```
   Gtr   X g g g | g g X g | g g X g | X g g g
   ```
7. **Bass:** Funk is "the style in which the bassline is most prominent", with the bass playing the hook. Early lines used syncopated 8ths, blues-scale notes plus the major 3rd. Later lines use 16th syncopation and octave or wider leaps — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). Larry Graham (Sly and the Family Stone) introduced slap on electric bass in the late 1960s, and it spread to funk and disco — [Wikipedia: Slapping](https://en.wikipedia.org/wiki/Slapping_(music)). Example in E (derived): `E1 . . G1 | . . A1 . | E1 . . E2 | D2 . B1 .`, with a heavy root on step 1 every bar.
8. **Form:** Long vamps instead of 12-bar blues ("extensive vamps") — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). Horn arrangements are especially important in intros — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). There is a bridge on the subtonic, and the bandleader calls a drum break late in the track ("give the drummer some") — [Wikipedia: Funky Drummer](https://en.wikipedia.org/wiki/Funky_Drummer). Typical shape (convention): intro hits (4) → vamp A (16–32) → bridge on bVII (8) → vamp A → breakdown/drum break (8) → vamp out. Length 3–7 min.
9. **Mix:** Dry, close-miked, mid-forward. Guitar trebly and clean. Horns short and punchy. Little reverb (convention).
10. **Neighbours:** New Orleans funk (The Meters: looser, second-line syncopation) — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). P-Funk (Card 2). Disco takes the funk bass and puts four-on-the-floor under it — [Wikipedia: Disco](https://en.wikipedia.org/wiki/Disco).
11. **FL Studio:** (a) 105 BPM, swing ~20. (b) Program kick and snare per the grid, with ghost snares at velocity 25–40 and accented 8th hats (vel 100 on 8ths, 60–70 on the off-16ths) (convention). (c) Pick a single dom9 or m7 chord. Write the guitar as 16th scratches with 2–4 accented stabs per bar, gated short (convention). (d) Bass: root on 1, then 16th syncopation with octaves and the b7. Leave space where the guitar stabs (convention). (e) Horns: 2–4 short unison/octave stabs on off-16ths in the intro and between vocal lines — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). **Fake-sounding mistakes:** quantizing everything 100% to straight 16ths, too many chord changes, distorted guitar, bass and kick both hitting every downbeat with nothing in between, sustained horns.

#### CARD 2: P-Funk (Parliament-Funkadelic, 1970s)
- **Identity:** George Clinton's collective. Bernie Worrell's keyboard range covers Hammond organ, RMI electric piano, acoustic piano, clavinet ("Up for the Down Stroke"), Minimoog ("Flash Light", "Aqua Boogie", "Knee Deep") and ARP string ensemble ("Chocolate City", "Give Up the Funk (Tear the Roof off the Sucker)") — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk); see also [Wikipedia: Parliament-Funkadelic](https://en.wikipedia.org/wiki/P-Funk). **By ear:** slower, heavier and spacier than JB funk. Minimoog bass melodies, big gang vocals and chants, psychedelic guitar.
- **Tempo:** 95–108 BPM, more swing than JB (MPC 56–60%) (convention).
- **Harmony:** Mostly minor/Dorian one- or two-chord vamps with blues inflections, e.g. Em7 to A9 (convention).
- **Rhythm (derived, convention):**
  ```
  Kick  X . . . | . . x . | . . X . | . . . .
  Snare . . . . | X . . . | . . . . | X . . .
  Hat   x . x . | x . x . | x . x . | x . x .   (swing 56-60%)
  MoogB X . x . | . x . . | x . . X | . x . .   (portamento slides between notes)
  ```
- **Bass:** Bootsy Collins' electric bass, with envelope filter and octave effects (convention), sitting alongside Minimoog synth bass — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). In FL: Sytrus/3x Osc saw+square, low-pass filter with envelope, glide on overlapping notes, plus a mono subtle overdrive (convention).
- **Form:** Long jams of 5–10 min with chant hooks and call-and-response gang vocals (convention).
- **FL:** Minimoog-style lead/bass from a mono synth with glide, ARP string-machine pad (any string-ensemble preset with chorus), clavinet comping (convention). **Mistakes:** too fast, synth bass with no glide or filter movement, too clean and quantized.

#### CARD 3: Disco (c. 1974–1980)
1. **Identity:** A dance-centric evolution of soul, funk and R&B — [Native Instruments blog](https://blog.native-instruments.com/disco/). Philly soul is a direct parent — [Wikipedia: Philadelphia soul](https://en.wikipedia.org/wiki/Philadelphia_soul). Earl Young (MFSB, Sigma Sound) is credited with the beat: "put some fours on the floor and twos on the snare, and ride the 16th on the sock cymbal" — [Wikipedia: Earl Young](https://en.wikipedia.org/wiki/Earl_Young_(drummer)), [The Second Disc](https://theseconddisc.com/2024/04/15/im-doin-fine-now-groove-machine-the-earl-young-drum-sessions-spotlights-philly-legend/). Loud hats in disco are said to come from a recording error on Harold Melvin & the Blue Notes' "Bad Luck" (1975), where Young's hi-hat was mixed too loud — [Wikipedia: Disco](https://en.wikipedia.org/wiki/Disco). Chic (Nile Rodgers): "Le Freak", "Good Times" — [London Guitar Academy](https://www.londonguitaracademy.com/mastering-funk-guitar). **By ear:** a relentless four-on-the-floor kick, a hissing open hat on every "&", an octave-jumping bass and strings.
2. **Tempo:** Editorial range 110–130 BPM. Measured median 122 (IQR 119–124, 7,359 tracks) — [Mixgraph: Disco](https://www.mixgraph.io/bpm-for/disco) (sourced; that catalog is likely skewed toward DJ-friendly 12"s). NI's worked example is 115 BPM — [Native Instruments](https://blog.native-instruments.com/disco/). Straight 16ths, at most a tiny swing (MPC 50–54%) (convention).
3. **Harmony:** NI's example (sourced, [Native Instruments](https://blog.native-instruments.com/disco/)):
   - Verse: Em → D/B (= Bm7) → C/A (= Am7) → D then D# octaves pushing back to E. Roman: i – v7 – iv7 – bVII → VII (chromatic push).
   - Chorus: Em – G – A, two bars, repeated. That is i – III – IV, a Dorian-flavoured vamp (derived).
   - Bridge: E for three bars → D → D#.
   - "Chords without the fifth" for a strong, simplified sound.

   Convention: two-chord minor-7 Dorian vamps (i7–IV7, e.g. Em7–A7, the "Good Times" type) and maj7/m9 Philly colours. Harmonic rhythm: 1–2 bars per chord.
4. **Melody & vocals:** Soulful, gospel-trained lead vocals over lush orchestration, with catchy, repetitive hooks — [Native Instruments](https://blog.native-instruments.com/disco/). Diva belting, unison or octave female backing chants, falsetto male harmonies (convention).
5. **Instrumentation:** Strings, horns, electric keyboards — [Native Instruments](https://blog.native-instruments.com/disco/). Also drum kit, African/Latin percussion, and later electronic drums (Simmons, Roland modules). Rhythm guitar supports the 8th pattern — [Wikipedia: Disco](https://en.wikipedia.org/wiki/Disco). NI's DAW build: string loop, Studio Drummer "Session Funk", Scarbee Rickenbacker bass, "Soul Sessions" brass stabs and plucked guitar — [Native Instruments](https://blog.native-instruments.com/disco/). FL stock: FPC kit, BooBass, FL Keys, FLEX strings and brass presets. Better: Kontakt string and brass libraries (convention).
6. **Rhythm:** The cited pattern is a four-on-the-floor kick, an 8th or 16th hat with an open hissing hat on the off-beat, and a heavy syncopated bass — [Wikipedia: Disco](https://en.wikipedia.org/wiki/Disco). NI's version: kick on every beat, snare on 2 and 4, closed hats on beats, open hats between beats — [Native Instruments](https://blog.native-instruments.com/disco/). Latin layers (rhumba, samba, cha-cha-cha) are common — [Wikipedia: Disco](https://en.wikipedia.org/wiki/Disco).
   ```
   Kick  X . . . | X . . . | X . . . | X . . .
   Snare . . . . | X . . . | . . . . | X . . .
   CHat  x x . x | x x . x | x x . x | x x . x
   OHat  . . o . | . . o . | . . o . | . . o .
   Shkr  x x x x | x x x x | x x x x | x x x x   (accent the 2nd and 4th 16ths)
   Conga . . . x | . . x . | . . . x | . x x .
   ```
7. **Bass:** Prominent and syncopated, with heavy use of broken octaves (low then high octave) — [Wikipedia: Disco](https://en.wikipedia.org/wiki/Disco). NI: low notes on the beat, the octave above between beats, velocity 127 — [Native Instruments](https://blog.native-instruments.com/disco/).
   ```
   Bass  X . x . | X . x . | X . x x | X . x .   (X = E1 on the beat, x = E2 on the "&"; step 12 is a 16th pickup)
   ```
8. **Form:** NI's 8-bar-block layout — [Native Instruments](https://blog.native-instruments.com/disco/):
   - Intro: strings only (4 bars), then add guitar (4).
   - Verse (8), pre-chorus (8).
   - Chorus (8): brass enters.
   - Bridge (8): drums and bass only.
   - Final chorus (16).

   12" disco mixes stretch to 6–10 min with percussion breakdowns (convention).
9. **Mix:** Hats loud and bright (the "Bad Luck" legacy) — [Wikipedia: Disco](https://en.wikipedia.org/wiki/Disco). NI uses reverb on brass (hall, 30% mix) and plucked guitar (25% mix) and masters with an "RnB/Soul" profile — [Native Instruments](https://blog.native-instruments.com/disco/). Wide strings, mono kick and bass, and a moderate-loudness 70s mix (convention).
10. **Neighbours:**
    - Philly soul (Card 6) is the slower, more song-like parent.
    - Boogie/post-disco (Card 10) drops four-on-the-floor.
    - Nu-disco/French touch (Card 13) loops and filters it.
    - Euro/Italo disco (convention): sequenced synth bass, less funk.
11. **FL:**
    - (a) 118–122 BPM with swing off.
    - (b) Build the grid above in the Channel Rack. Open hat on steps 3/7/11/15 with the closed hat choked by the open one (cut group in FPC) (convention).
    - (c) Write an octave bass, root on the beat and octave on the "&".
    - (d) Strings: sustained pads for the verse, 16th-note "runs" or sweeps into the chorus, octave-doubled stabs (convention).
    - (e) Rodgers-style guitar: 16th chanks on maj7/m7/9 voicings — [London Guitar Academy](https://www.londonguitaracademy.com/mastering-funk-guitar).
    - (f) Brass stabs in the chorus only.

    **Mistakes:** a 909 house kick and a sidechain pump (that is French house, not disco), quiet hats, the bass playing roots only, a dry mix with no strings.

#### CARD 4: Motown (Detroit, 1959–early 70s)
1. **Identity:** Berry Gordy's Hitsville U.S.A. from 1959: Marvin Gaye, the Supremes, the Temptations, early Stevie Wonder — [Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/). House band: the Funk Brothers, including Benny Benjamin, Uriel Jones, James Jamerson, Joe Messina, and Jack Ashford on tambourine — [Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/), [Reverb: What Makes Motown Sound Like Motown](https://reverb.com/news/video-what-makes-motown-sound-like-motown). Reference tracks: "Get Ready" (Temptations 1966), "Ain't No Mountain High Enough", "My Guy", "Heat Wave" — [Wikipedia: James Jamerson](https://en.wikipedia.org/wiki/James_Jamerson). **By ear:** a bright pop-soul backbeat reinforced by tambourine, a busy melodic bass, and polished harmony vocals.
2. **Tempo:** Uptempo hits ~120–140 BPM, ballads 70–90 (convention, unsourced). Straight 8ths with "gentle swing" in the drums — [Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/). Some songs use a shuffle (the "Motown shuffle" is a recognized drum groove — [Bonedo](https://www.bonedo.de/artikel/10-basis-drum-grooves-2-motown-shuffle)).
3. **Harmony:** Major-key pop progressions: I–vi–IV–V, I–IV–V, ii–V turnarounds (convention). A key change up a half or whole step for the last chorus (convention). In C (convention): C – Am – F – G | C – C7 – F – Fm (minor iv borrowed for a gospel-ish lift).
4. **Melody & vocals:** Doubled lead vocals and dramatic harmonies — [Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/). Call-and-response between lead and group, gospel-derived (convention).
5. **Instrumentation:** Drums, tambourine, handclaps, finger snaps, congas — [Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/). Jamerson played P-Bass ("Black Beauty", from 1960–61) and earlier upright. He sometimes cut acoustic bass then overdubbed the same line on electric — [Wikipedia: James Jamerson](https://en.wikipedia.org/wiki/James_Jamerson), [Reverb](https://reverb.com/news/video-what-makes-motown-sound-like-motown). Guitars play fragmented rhythm parts around downbeats and vocal lines — [Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/). Also vibraphone, bari sax and strings (convention).
6. **Rhythm:** Beats 2 and 4 are heavily emphasized, reinforced by rhythm guitar and Ashford's tambourine — [Reverb](https://reverb.com/news/video-what-makes-motown-sound-like-motown). Drums are "pulsating four-on-the-floor... with ghost notes and gentle swing" — [Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/).
   ```
   Kick  X . . . | X . . . | X . . . | X . . .
   Snare . . . . | X . . g | . . . . | X . . .
   Tamb  . . x . | X . x . | . . x . | X . x .   (accent the backbeat; 8ths elsewhere)
   Clap  . . . . | X . . . | . . . . | X . . .
   Hat   x . x . | x . x . | x . x . | x . x .
   Gtr   . . . . | X . . . | . . . . | X . . .   (short chop on 2 and 4)
   ```
   Variant (convention): snare or footstomp on all four beats for the "stomp" feel on some early-60s hits.
7. **Bass:** Jamerson replaced root-fifth playing with chromatic runs, syncopation and ghost notes. He often played with one index finger — [Wikipedia: James Jamerson](https://en.wikipedia.org/wiki/James_Jamerson), [Reverb](https://reverb.com/news/video-what-makes-motown-sound-like-motown). Lines "weave around the kick and snare" — [Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/). Pattern in C (derived): `C2 . . G1 | . . A1 . | C2 . E2 . | . F2 F#2 .` → G (a chromatic approach into the next root).
8. **Form:** Verse–chorus pop, 2:30–3:00. Intro hook riff (bass, guitar or bari sax), modulation into the last chorus, fade-out (convention).
9. **Mix:** A tiled attic echo chamber with a bright character on vocals and drums. Tape hit hard for compression and warmth. Neumann U47 on vocals, Shure 545 on drums and amps, RCA ribbons on brass. 3-track, later 8-track — [Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/). Mid-forward and mono-compatible; the tambourine is very audible (convention).
10. **Neighbours:**
    - Stax (Card 5) is rawer, horn-led and behind the beat.
    - Northern soul (UK DJ scene for uptempo Motown-like records) (convention).
    - Doo-wop (Card 8) is the vocal-group parent.
11. **FL:**
    - (a) 124 BPM, FL swing ~10.
    - (b) Kick on four, snare+clap+tambourine on 2 and 4. The tambourine needs its own channel at near-snare level (convention).
    - (c) Bass: write melodic 8th/16th lines with chromatic approach notes. Avoid sustained roots.
    - (d) Short reverb-chamber send (Fruity Reeverb 2, bright, ~1.2 s) on snare and vocals. Saturate the buses with Fruity Blood Overdrive/Soft Clipper (convention).
    - (e) Stack vocals: doubled lead plus 3-part backing "oohs".

    **Mistakes:** an 808/trap kick, a sub-bass instead of a P-Bass, no tambourine, a modern wide stereo image.

#### CARD 5: Southern / Memphis soul (Stax, Muscle Shoals, Hi, 1960s–70s)
1. **Identity:** Late-1950s Southern US. Origins in soul, blues, country, R&B and gospel — [Wikipedia: Southern soul](https://en.wikipedia.org/wiki/Southern_soul). Stax house band Booker T. & the M.G.'s (Booker T. Jones, Steve Cropper, Donald "Duck" Dunn, Al Jackson Jr.) backed Otis Redding, Sam & Dave, Rufus and Carla Thomas and others, and cut the instrumental "Green Onions" — [Wikipedia: Memphis soul](https://en.wikipedia.org/wiki/Memphis_soul). Other refs: Eddie Floyd "Knock on Wood" — [Wikipedia: Stax Records](https://en.wikipedia.org/wiki/Stax_Records). **By ear:** grittier and more gospel/blues than Motown. Organ and horns, a raw room sound, a sermon-like lead.
2. **Tempo:** Uptempo 100–125 BPM. Ballads often 12/8 at 50–70 dotted-quarter BPM (convention). Feel: laid back, "mellow, not sweet" — [Wikipedia: Stax Records](https://en.wikipedia.org/wiki/Stax_Records).
3. **Harmony:** Gospel, blues and country roots — [Wikipedia: Stax Records](https://en.wikipedia.org/wiki/Stax_Records). Convention: I–IV vamps with dominant 7ths, 12-bar blues (e.g. an F blues: F7–Bb7–C7), and gospel plagal IV–I "amen" cadences in ballads (in C: F → C, or F → Fm → C).
4. **Melody & vocals:** Call and response between lead and chorus, handclaps — [Wikipedia: Memphis soul](https://en.wikipedia.org/wiki/Memphis_soul). Raw, emotionally intense leads (Otis Redding) and gritty vocal duos (Sam & Dave) — [Wikipedia: Stax Records](https://en.wikipedia.org/wiki/Stax_Records). Shouted climaxes and repeated pleading tags (convention).
5. **Instrumentation:** Brass and saxophones are common — [Wikipedia: Memphis soul](https://en.wikipedia.org/wiki/Memphis_soul). Hammond organ (Booker T.), Telecaster rhythm (Cropper), bass, drums. Horns in unison or octaves, often baritone and tenor sax with trumpet (the Mar-Keys/Memphis Horns approach) (convention).
6. **Rhythm:** Head arrangements without sheet music, cut live as a band — [Wikipedia: Stax Records](https://en.wikipedia.org/wiki/Stax_Records). Grid (convention, unsourced):
   ```
   Kick  X . . . | . . . . | X . x . | . . . .
   Snare . . . . | X . . . | . . . . | X . . .   (place 5-15 ms late)
   Hat   x . x . | x . x . | x . x . | x . x .
   Horns . . . . | . . X . | . . . . | . . X .   (short stabs on the "&" of 2 and 4)
   ```
   12/8 ballad (12 steps = 4 beats x 3 triplets):
   ```
   Kick  X . . | . . . | X . x | . . .
   Snare . . . | X . . | . . . | X . .
   Piano x x x | x x x | x x x | x x x   (triplet chords)
   ```
7. **Bass:** Dunn-style: simple, supportive root-fifth-octave lines locked to the kick, fewer notes than Jamerson (convention).
8. **Form:** Verse–chorus with a vamp-out. The vocalist "testifies" over a repeating tag (convention).
9. **Mix:** Stax was a converted movie theater with a sloped floor, which gave a big, deep, raw sound. Early recordings were mono on an Ampex — [Wikipedia: Stax Records](https://en.wikipedia.org/wiki/Stax_Records). Use more room and less polish than Motown.
10. **Neighbours:** Muscle Shoals (Aretha's Atlantic sessions), Hi Records (Al Green: softer, more hi-hat-led), New Orleans soul — [Wikipedia: Southern soul](https://en.wikipedia.org/wiki/Southern_soul). Memphis soul is Southern soul's "uptown" urban variant — [Wikipedia: Memphis soul](https://en.wikipedia.org/wiki/Memphis_soul).
11. **FL:** (a) 108 BPM, or 12/8 for ballads (set the time signature to 12/8, or use triplet snap in the piano roll). (b) A Hammond-style organ with drawbar/Leslie presets (FLEX or any B3 plug-in) holding chords with swells (convention). (c) Horn stabs in unison/octaves, short, on off-beats, with a fall-off on the last note (convention). (d) Drag the snare late by 6–12 ticks. (e) Room reverb, mono-ish drums. **Mistakes:** Motown-style tambourine pop polish, strings, quantized-ahead drums.

#### CARD 6: Philly soul (Philadelphia International, c. 1968–1979)
1. **Identity:** Gamble & Huff, Thom Bell, Bobby Martin, Linda Creed and others. Often considered "a producers' genre" for its emphasis on sound and arrangement — [Wikipedia: Philadelphia soul](https://en.wikipedia.org/wiki/Philadelphia_soul). House band MFSB at Sigma Sound; Baker–Harris–Young rhythm section (Ronnie Baker bass, Norman Harris guitar, Earl Young drums) — [Wikipedia: Earl Young](https://en.wikipedia.org/wiki/Earl_Young_(drummer)). Roots in soul, funk, R&B, big band and baroque pop. It led to disco and smooth jazz — [Wikipedia: Philadelphia soul](https://en.wikipedia.org/wiki/Philadelphia_soul). Refs: O'Jays "For the Love of Money" (Earl Young), Harold Melvin & the Blue Notes "Bad Luck" — [Wikipedia: Earl Young](https://en.wikipedia.org/wiki/Earl_Young_(drummer)), [Wikipedia: Disco](https://en.wikipedia.org/wiki/Disco). **By ear:** a soul song in an orchestral dress. Sweeping strings and horns, hi-hat-driven drums, sophisticated chords.
2. **Tempo:** 95–120 BPM for dance cuts, 60–80 for ballads (convention). Straight 16ths on the hats.
3. **Harmony:** maj7, m9 and 11 chords with lush ii–V motion (convention, unsourced). Example in F (convention): Bbmaj7 – Am7 – Gm9 – C9sus | Fmaj9.
4. **Vocals:** Group harmony (O'Jays, Blue Notes, Stylistics falsetto) with gospel-trained leads (convention).
5. **Instrumentation:** Full rhythm section plus strings, horns, vibes and percussion (MFSB's large lineup) — [Wikipedia: Earl Young](https://en.wikipedia.org/wiki/Earl_Young_(drummer)). DAW: an orchestral string library (legato violins in octaves, divisi), a brass section, FL Keys electric piano, vibraphone (convention).
6. **Rhythm:** Young's "fast, rhythmic and crisp" open and closed hi-hats, which DJs could hear in their cue headphones — [Wikipedia: Earl Young](https://en.wikipedia.org/wiki/Earl_Young_(drummer)), [The Second Disc](https://theseconddisc.com/2024/04/15/im-doin-fine-now-groove-machine-the-earl-young-drum-sessions-spotlights-philly-legend/).
   ```
   Kick  X . . . | X . . . | X . . . | X . . .   (four on the floor, sometimes lighter on 2/4)
   Snare . . . . | X . . . | . . . . | X . . .
   Hat   x x o x | x x o x | x x o x | x x o x   ("ride the 16th on the sock cymbal")
   ```
7. **Bass:** Syncopated, melodic, octave-leaning lines that disco inherited (derived from the Philly → disco lineage).
8. **Form:** Verse–chorus with long instrumental intros and string interludes. Album versions often run 5–7 min with an extended vamp (convention).
9. **Mix:** Wide, reverberant strings and horns. A bright hat clearly audible. Polished 70s studio sound (convention).
10. **Neighbours:** Disco is faster, simpler and more repetitive. Quiet storm (70s–90s radio format) is a softer, jazz-tinged slow-jam R&B — [Wikipedia: Quiet storm](https://en.wikipedia.org/wiki/Quiet_storm). The Salsoul label continued the band into disco — [Wikipedia: Earl Young](https://en.wikipedia.org/wiki/Earl_Young_(drummer)).
11. **FL:**
    - (a) 108 BPM.
    - (b) Program the Young hat pattern, opening the hat on every "&", with velocity humanized ±10 (convention).
    - (c) Write strings in three layers (convention):
      - sustained pad voicings (3rd/7th/9th on top);
      - an octave-doubled counter-melody answering the vocal;
      - 16th rising runs or a glissando into choruses.
    - (d) Horns: pads under the chorus plus short stabs.
    - (e) Panning: strings wide, horns mid-sides, rhythm section center.

    **Mistakes:** triad-only harmony, unison strings in one octave, strings that play the vocal melody literally.

#### CARD 7: Gospel: traditional black gospel, urban contemporary gospel, CCM, shout/praise break
1. **Identity:** Urban contemporary gospel fuses traditional black gospel with 70s/80s secular black music. It is the most common form of recorded gospel today and often uses electronic beats — [Wikipedia: Gospel music](https://en.wikipedia.org/wiki/Gospel_music). Early forms date to the 1970s and the style was established by the end of the 1980s. Typical instruments are guitar, bass, drums and piano. Christian hip-hop is a subtype — [Wikipedia: Urban contemporary gospel](https://en.wikipedia.org/wiki/Urban_contemporary_gospel). CCM draws on folk, gospel, pop and rock, and since the 2000s has moved into contemporary worship music and Christian EDM — [Wikipedia: CCM](https://en.wikipedia.org/wiki/Contemporary_Christian_music). Twinkie Clark (The Clark Sisters) is widely credited with the classic contemporary shout sound — [Wikipedia: Shout](https://en.wikipedia.org/wiki/Shout_(Black_gospel_music)). **By ear:** choir and lead call-and-response, piano and Hammond with constant passing chords, big dynamic builds and vamps.
2. **Tempo & feel:**
   - Ballads and hymns often 12/8 or 6/8 at slow tempos (convention).
   - Contemporary gospel uses R&B/hip-hop tempos, 70–100 (convention).
   - Shout/praise break: "very fast tempo" — [Wikipedia: Shout](https://en.wikipedia.org/wiki/Shout_(Black_gospel_music)). No BPM is published. Treat ~140–180 BPM as convention (unsourced).
3. **Harmony:** Gospel progressions use walk-ups, walk-downs, sus chords, passing chords and turnarounds. Bass walk-ups commonly run from the II chord to the IV, or II to V — [PianoGroove: Gospel Chord Progressions](https://pianogroove.com/?p=5342). PianoGroove's concrete examples in F major, a 1–4–5 skeleton with passing chords as "stepping stones" — [PianoGroove: Gospel Passing Chords](https://pianogroove.com/blues-piano-lessons/gospel-passing-chords-substitutions/):
   - **Chromatic walk-up to IV:** Ab7(9, Bb on top) → A7 → Bb9sus → Bbmaj7, i.e. bIII7 → III7 → IV9sus → IV.
   - **1–6–2–5:** F → D7(b9,#9,#5) → Gm7 → C7. The vi becomes an altered secondary dominant. Variation: insert E7 (chromatic) → D7sus before resolving.
   - **Diminished passing:** Bb7 → Bdim7 → F/C (IV7 → #IVdim7 → I/5).
   - **Turnaround:** F7 – F7/A – Bb – Bbdim7 – C7 (I7 – I7/3 – IV – ivdim7 – V7).
   - Tritone substitution (e.g. Gb7 for C7 in F) also appears — [PianoGroove search summary](https://pianogroove.com/?p=5342) (exact example not verified).
   - Shout harmony: organists hold dominant 7 chords over riffs, with chromatic basslines — [Wikipedia: Shout](https://en.wikipedia.org/wiki/Shout_(Black_gospel_music)).
4. **Melody & vocals:** Melisma, runs on pentatonic/blues scales, choir stacked in 3 parts (SAT). The lead ad-libs over a repeating vamp that modulates up by half-steps (convention). Shout: exclamations such as "Hallelujah!" — [Wikipedia: Shout](https://en.wikipedia.org/wiki/Shout_(Black_gospel_music)).
5. **Instrumentation:** Piano, Hammond B3 with Leslie, bass (often 5/6-string), drums (heavy chops), choir — (convention). The shout has a brass variant (UHOP trombone shout bands) — [Wikipedia: Shout](https://en.wikipedia.org/wiki/Shout_(Black_gospel_music)). FL: FL Keys or a grand piano library, any B3 emulation, a choir "aah/ooh" library or FLEX choir presets, FPC kit (convention).
6. **Rhythm:** Shout: snare hits and handclaps on the upbeat of each beat, chromatic bass — [Wikipedia: Shout](https://en.wikipedia.org/wiki/Shout_(Black_gospel_music)).
   ```
   Kick  X . . . | X . . . | X . . . | X . . .
   Snare . . X . | . . X . | . . X . | . . X .   (upbeat "&" of every beat)
   Clap  . . X . | . . X . | . . X . | . . X .
   Hat   x x x x | x x x x | x x x x | x x x x
   Organ X . x . | X . x . | X . x . | X . x .   (stabbed dom7, counter to the snare)
   ```
   12/8 traditional ballad (12 steps):
   ```
   Kick  X . . | . . . | X . . | . . .
   Snare . . . | X . . | . . . | X . .
   Hat   x x x | x x x | x x x | x x x
   ```
7. **Bass:** Chromatic walk-ups into chord changes (II→IV, II→V) — [PianoGroove](https://pianogroove.com/?p=5342). Shout bass runs chromatic 8ths — [Wikipedia: Shout](https://en.wikipedia.org/wiki/Shout_(Black_gospel_music)).
8. **Form:** Intro → verse → chorus → bridge → **vamp** (repeated 2–4 bar phrase, modulating) → optional shout/praise break → tag ending (convention). Studio and live albums often include shout segments — [Wikipedia: Shout](https://en.wikipedia.org/wiki/Shout_(Black_gospel_music)).
9. **Mix:** Live-church ambience (room/hall), a choir as wide as possible, a forward lead vocal, prominent organ (convention).
10. **Subgenres:**
    - Traditional (quartet, choir, hymn-based, piano+organ).
    - Urban contemporary (R&B/hip-hop production, e.g. Kirk Franklin) — the [Wikipedia](https://en.wikipedia.org/wiki/Urban_contemporary_gospel) definition.
    - CCM/worship (pop-rock, guitars and pads, fewer passing chords; I–V–vi–IV-type pop progressions (convention)).
    - Christian hip-hop.
11. **FL:**
    - (a) Write the skeleton (I–IV–V or I–vi–ii–V) first.
    - (b) Insert one passing chord before each strong-beat change: a chromatic dom7 a half-step below the target, a #IVdim7, or a V/x with b9/#9.
    - (c) Bass walk-ups of 3–4 chromatic 8ths on beats 3–4 into each change.
    - (d) Vamp section: loop 2 bars and modulate up a half-step every 4–8 bars.
    - (e) Shout: 150+ BPM, snare+clap on every "&".

    **Mistakes:** static triads, no walk-ups, a choir in unison, quantized organ with no Leslie movement.

#### CARD 8: Doo-wop (1940s–early 60s)
- **Identity:** An R&B subgenre from African-American communities (New York, Philadelphia, Chicago, Baltimore, Detroit, DC, LA). Group vocal harmony carries an engaging melody over a simple beat with little or no instrumentation. Simple love lyrics, often with a heartfelt spoken recitative in the bridge. Harmonized nonsense syllables. Commercially viable until the early 1960s — [Wikipedia: Doo-wop](https://en.wikipedia.org/wiki/Doo-wop). Gribin & Schiff's five features: vocal group music, a range from bass to falsetto, nonsense syllables, a simple beat with low-key instrumentals, simple words and music. Bill Kenny (Ink Spots) introduced the "top and bottom" arrangement: high tenor lead plus spoken bass — [Wikipedia: Doo-wop](https://en.wikipedia.org/wiki/Doo-wop). **By ear:** a bass singer's "bom-bom" line, falsetto on top, the I–vi–IV–V loop, 12/8 piano triplets.
- **Tempo:** Ballads with a slow 12/8 feel, roughly 55–75 dotted-quarter BPM. Uptempo jump numbers 130–160 (convention).
- **Harmony:** The typical doo-wop progression is the "50s progression", shown in C as C – Am – F – G (I–vi–IV–V). Its precedent, I–vi–ii–V (C – Am – Dm – G), appears in "Blue Moon" (1934) and "Heart and Soul" (1938) — [Wikipedia: Doo-wop](https://en.wikipedia.org/wiki/Doo-wop). One chord per bar, or two per bar in 12/8 (convention).
- **Rhythm:** 12/8 piano triplet chords, light snare backbeat on 2 and 4, brushes (convention). Use the 12/8 grid from Card 5.
- **Arrangement:** Lead vocal; 2–3 background voices on syllables ("doo-wop", "sh-boom", "ooh"); a bass voice on the root as a rhythmic ostinato; falsetto descant (sourced as features above; voicings are convention).
- **FL:** Vocal samples or a choir library on "doo/ooh" for the BGVs, FL Keys piano triplets, upright bass (convention). **Mistakes:** dense drums, synth pads, modern chord extensions.

#### CARD 9: New jack swing (1985–1993)
1. **Identity:** Teddy Riley's sound (Guy). Term coined in Barry Michael Cooper's 1987 Village Voice profile — [Wikipedia: New jack swing](https://en.wikipedia.org/wiki/New_jack_swing). Origins: contemporary R&B, funk, hip-hop, jazz and dance-pop, 1985–87, US. Instruments: vocals, keyboards, synthesizers, drum machine, sampler — [Wikipedia: New jack swing](https://en.wikipedia.org/wiki/New_jack_swing). Precursor: Jimmy Jam & Terry Lewis' work on Janet Jackson's *Control* (1986) — [Mixdown Magazine](https://mixdownmag.com.au/features/columns/producer-focus-teddy-riley), [Wikipedia: Contemporary R&B](https://en.wikipedia.org/wiki/Contemporary_R%26B). Artists: Keith Sweat, Bobby Brown, Johnny Kemp, Bell Biv DeVoe — [Wikipedia: Contemporary R&B](https://en.wikipedia.org/wiki/Contemporary_R%26B). Riley later produced for Michael Jackson and Blackstreet — [Mixdown Magazine](https://mixdownmag.com.au/features/columns/producer-focus-teddy-riley). **By ear:** a hard, swung drum machine with a giant snare, hip-hop drums under gospel-trained R&B vocals, synth stabs and orchestra hits.
2. **Tempo:** ~95–110 BPM — [DJ TechTools forum / Subgenropedia search snippets](https://forum.djtechtools.com/t/new-jack-swing-train/23097) (weak source; example tracks at 98, 107, 108 and 110 BPM per [SongBPM](https://songbpm.com/@wreckx-n-effect/new-jack-swing)). Default 104 (derived). **Swing is the identity:** "swingbeats" use off-beat, accented 16th-note triplets — [Wikipedia: New jack swing](https://en.wikipedia.org/wiki/New_jack_swing). Hi-hats are often in 16th-note triplets, a Riley trademark — [Mixdown Magazine](https://mixdownmag.com.au/features/columns/producer-focus-teddy-riley). Practical: MPC swing 62–66% on 16ths, or FL swing knob ~55–75 (convention).
3. **Harmony:** Gospel- and funk-derived minor 7/9 vamps with dominant stabs (convention). Example in C minor (convention): Cm9 – Fm9 – Ab maj7 – G7#9.
4. **Vocals:** Clearly enunciated vocals and light melody lines over an insistent beat — [Wikipedia: New jack swing](https://en.wikipedia.org/wiki/New_jack_swing) (via search summary). Group harmony (Guy, BBD), rap verses or features, call-and-response hooks (convention).
5. **Instrumentation:** E-mu SP-1200 sampler and Roland TR-808 with a dominant snare — [Mixdown Magazine](https://mixdownmag.com.au/features/columns/producer-focus-teddy-riley). Riley says he never used a sequencer to program beats — [Mixdown Magazine](https://mixdownmag.com.au/features/columns/producer-focus-teddy-riley) (via search summary). FM/digital synths (DX7-type bass and bells), orchestra hits, synth brass (convention). FL: FPC with 808 kick + a sampled SP-1200-style snare (bit-reduce to 12-bit/26 kHz with Fruity Squeeze or a bitcrusher), FM bass from Sytrus, synth brass from FLEX/Sytrus (convention).
6. **Rhythm (derived from "accented off-beat 16th triplets"):**
   ```
   Kick  X . . x | . . x . | . x X . | . . x .
   Snare . . . . | X . . . | . . . . | X . . x   (big snare + clap layer; pickup on step 16)
   Hat   x x x x | x x x x | x x x x | x x x x   (16ths at heavy swing, accent the swung "e" and "a")
   ```
   Triplet-hat version, 24 steps per bar (6 per beat, positions 1-6; accent position 4 = the "&"):
   ```
   Hat   x . x X . x | x . x X . x | x . x X . x | x . x X . x
   ```
7. **Bass:** Synth bass (FM or Minimoog-style), short and punchy, locked to the syncopated kick (convention).
8. **Form:** Pop verse–pre–chorus, 4–5 min, dance breakdown with a rap verse, ad-lib outro (convention).
9. **Mix:** Very loud, bright snare with gated/plate reverb. Dry, punchy kick. Crisp digital-era top end (convention, with the "dominant snare" sourced above).
10. **Neighbours:** Hip-hop soul (early/mid-90s) evolved from NJS. It fuses R&B singing with hip-hop production: boom-bap loops instead of swingbeat drum machines — [Wikipedia: Hip-hop soul](https://en.wikipedia.org/wiki/Hip_hop_soul). It later led into neo-soul — [Wikipedia: Hip-hop soul](https://en.wikipedia.org/wiki/Hip_hop_soul). Hip house and G-funk are related — [Wikipedia: New jack swing](https://en.wikipedia.org/wiki/New_jack_swing).
11. **FL:** (a) 104 BPM, Channel Rack swing ~65 (or write hats on a triplet grid in the piano roll). (b) Layer snare + clap + noise, add plate reverb with a gate. (c) Program a syncopated kick that dodges the snare. (d) FM bass and synth-brass stabs on the "&"s. (e) Orchestra-hit accents at section changes. **Mistakes:** straight hats (then it is 80s pop), a soft snare, live-band drums, trap 808 glides.

#### CARD 10: Boogie / post-disco (late 1970s–mid 80s)
- **Identity:** Late-1970s US. Rooted in post-disco, funk, soul and R&B. Typical instruments are synthesizers, keyboards, bass guitar, bass synthesizer, sampler, sequencer and drum machine. It led to electro and house — [Wikipedia: Boogie](https://en.wikipedia.org/wiki/Boogie_(genre)). In post-disco, drum machines, synths and sequencers increasingly dominated. By the mid-80s they dominated completely, with a "minimal" approach: more sounds, fewer instruments ("Forget Me Nots", "Don't Make Me Wait") — [Wikipedia: Post-disco](https://en.wikipedia.org/wiki/Post-disco). **By ear:** a mid-tempo synth-funk strut with the clap on 2 and 4, slap or synth bass, and no four-on-the-floor.
- **Tempo:** 110–116 BPM, with a strong accent on beats 2 and 4. It generally lacks the four-on-the-floor kick — [Wikipedia: Boogie](https://en.wikipedia.org/wiki/Boogie_(genre)). (sourced)
- **Harmony:** Jazz-influenced — [Wikipedia: Boogie](https://en.wikipedia.org/wiki/Boogie_(genre)). m9/maj7 synth-pad progressions, e.g. Am9 – Dm9 – Gm9 – C9sus (ii–V cycles in minor) (convention).
- **Rhythm (derived from the sourced 2/4 accent and the absence of four-on-the-floor):**
  ```
  Kick  X . . . | . . x . | X . . . | . . . x
  Clap  . . . . | X . . . | . . . . | X . . .   (LinnDrum/808 clap, big)
  Hat   x . x . | x . x . | x . x . | x . x .   (swing 54-56%)
  SynB  X . . x | . . x . | X . x . | . x . .
  ```
- **Bass:** Prominent slap bass (electric), or synth bass in later years — [Wikipedia: Boogie](https://en.wikipedia.org/wiki/Boogie_(genre)). FL: Sytrus/3x Osc square+saw with a short decay, or BooBass slap-ish settings (convention).
- **FL:** A LinnDrum/808-style kit in FPC, an analog-style poly pad (Juno-like) with Vintage Chorus, a vocoder/talkbox hook (Vocodex) (convention). **Mistakes:** a four-on-the-floor kick (becomes disco/house), a modern sub-bass, no chorus effect on the synths.

#### CARD 11: 90s R&B / hip-hop soul (brief; full modern R&B card is in earlier notes)
- Hip-hop soul is R&B or soul singing over hip-hop production, most popular in the early-to-mid 90s. It evolved from NJS and led to neo-soul — [Wikipedia: Hip-hop soul](https://en.wikipedia.org/wiki/Hip_hop_soul). The quiet storm format (mid-70s–early 90s) defined the slow-jam side: sensuous, jazz-flourished, "smooth grooves" — [Wikipedia: Quiet storm](https://en.wikipedia.org/wiki/Quiet_storm).
- Build: 85–100 BPM boom-bap or swung drum loop (see the boom bap card in `genres_hiphop_urban_global.md`), a sampled soul/R&B loop or Rhodes chords (m9, maj7), stacked harmonies with melismatic ad-libs (convention). Slow jams: 60–75 BPM, 6/8 or half-time feel, quiet-storm maj7 chords (convention).
- Telling it apart: NJS has heavy-swung, bright drum-machine drums and is uptempo. Hip-hop soul uses dusty sampled boom-bap breaks. Neo-soul has live, drunk-feel drums and jazzier chords (derived from the definitions above).

#### CARD 12: Neo-soul (mid-1990s–present)
1. **Identity:** Album-oriented and musicianship-driven, with organic live instrumentation in contrast to producer-driven, sample-based contemporary R&B. It incorporates jazz fusion, funk, hip-hop and electronic elements — [Wikipedia: Neo soul](https://en.wikipedia.org/wiki/Neo_soul). D'Angelo's *Voodoo* (recorded 1998–99 at Electric Lady with engineer Russ Elevado and the Soulquarians) — [Wikipedia: Voodoo](https://en.wikipedia.org/wiki/Voodoo_(D%27Angelo_album)). Refs: "Devil's Pie", "Left & Right" (*Voodoo*) — [Wikipedia: Voodoo](https://en.wikipedia.org/wiki/Voodoo_(D%27Angelo_album)). Players to study: Robert Glasper, D'Angelo, Erykah Badu — [PianoGroove: Neo Soul Harmony](https://www.pianogroove.com/?p=21017). **By ear:** a lazy, behind-the-beat groove, Rhodes playing m9/m11/maj13 loops, a warm saturated mono drum sound, intimate stacked vocals.
2. **Tempo:** ~70–95 BPM — [Orphiq BPM guide](https://orphiq.com/resources/bpm-tempo-guide) (sourced, low-authority). Default 84 (derived). Grooves are built to "hang on the back of the beat for a loose feel" — [Wikipedia: Voodoo](https://en.wikipedia.org/wiki/Voodoo_(D%27Angelo_album)). Questlove's drumming was modeled on J Dilla's "almost drunken" programming. D'Angelo asked him to play "as drunk and as slow and as dusted" as possible — [Wikipedia: Devil's Pie](https://en.wikipedia.org/wiki/Devil%27s_Pie), [Wikipedia: Voodoo](https://en.wikipedia.org/wiki/Voodoo_(D%27Angelo_album)).
3. **Harmony:** Built on minor 9 and minor 11 plus maj7 and maj13. 13sus chords often replace plain dominants. Neo-soul avoids 2-5-1s in favour of 3–4-chord loops and moves in small steps (e.g. a minor third down) — [PianoGroove](https://www.pianogroove.com/?p=21017), [Fundamental Changes](https://www.fundamental-changes.com/neo-soul-chords/). Signature loop: **Bbm11 → Gm9 → Gbmaj13 → Ebm11**. Roman (derived, Bb Dorian-ish): i11 – vi9 – bVImaj13 – iv11. Voicings — [PianoGroove](https://www.pianogroove.com/?p=21017):
   - Bbm11 = Bb F Ab C Eb
   - Fmaj7 = F A C E (extend to maj13)
   - G13sus = G C F A E

   Cluster voicings (9-3-11 close together) and quartal (stacked 4ths) voicings — [Fundamental Changes](https://www.fundamental-changes.com/neo-soul-chords/). Harmonic rhythm: 1 chord per bar, or 2 per bar with anticipations (convention).
4. **Melody & vocals:** Grace notes and slides into chord tones from a half-step below, especially into the 3rd or 7th — [PianoGroove](https://www.pianogroove.com/?p=21017). Breathy, layered falsetto stacks. Laid-back phrasing behind the beat (convention).
5. **Instrumentation:** Fender Rhodes; vintage gear and console for a classic sound — [search summary of Voodoo sources](https://en.wikipedia.org/wiki/Voodoo_(D%27Angelo_album)). *Voodoo* drums: mono, a lot of snare saturation, a Yamaha piccolo snare rimshot, a Ludwig Vistalite kick with the front head removed and muffled, Zildjian 14" K Dark hats — [Reverb: D'Angelo's Voodoo-era drums](https://reverb.com/news/video-dangelos-vibey-the-line-drums-whats-that-sound). FL: FL Keys (Rhodes-type) with Vintage Chorus or phaser, a muted P-bass, a dusty kit (convention).
6. **Rhythm (derived; the offsets matter more than the grid):**
   ```
   Kick  X . . x | . . . . | . . X . | . x . .   (kick 2 slightly early or late, unquantized)
   Snare . . . . | X . . . | . . . . | X . . .   (rimshot/snare 10-30 ms LATE)
   Hat   x . x x | x . x . | x . x x | x . x .   (velocity 40-90, timing jitter +/-5-10 ms)
   ```
   In FL ticks at 96 PPQ (convention): snare +6 to +12 ticks, hats randomized ±3–6 ticks, kick ±0–4. Do not apply global swing: use per-hit nudges instead (Dilla-style "unquantized" feel).
7. **Bass:** Behind the beat, sparse, slides; often follows the kick and leaves the snare open (convention).
8. **Form:** Loop-based. One 4–8-bar cycle carries most of the song, with long vamps and ad-libs; album tracks run 4–7 min — [PianoGroove](https://www.pianogroove.com/?p=21017) for the loop basis; lengths are convention.
9. **Mix:** Mono, saturated drums, warm tape-like mids, little high-frequency sheen — [Reverb](https://reverb.com/news/video-dangelos-vibey-the-line-drums-whats-that-sound). Not loud (convention).
10. **Neighbours:**
    - Hip-hop soul: sampled boom-bap, less jazz.
    - Modern alt-R&B: see earlier notes.
    - Jazz-hop/lo-fi: similar chords but no vocal focus, more vinyl noise (see the earlier lo-fi card).
11. **FL:**
    - (a) 84 BPM.
    - (b) Write the Bbm11–Gm9–Gbmaj13–Ebm11 loop in FL Keys. Put the top voice on the 9th or 11th, and roll chords slightly using the piano-roll strum tool (convention).
    - (c) Program drums, then nudge each hit off-grid by hand.
    - (d) Saturate the drum bus (Fruity Blood Overdrive, low), sum it to mono with Fruity Stereo Shaper.
    - (e) Bass enters a 16th late on some downbeats.

    **Mistakes:** perfectly quantized drums, ii–V–I jazz cadences, bright modern hats, triads.

#### CARD 13: Nu-disco and French touch/filter house (1990s–present)
1. **Identity:** French house, also called French touch, filter house or tekfunk, came from French musicians in the 1990s. It is a form of Eurodisco defined by filter and phaser effects on samples of late-70s/early-80s European disco. Acts include Daft Punk, Pépé Bradock, Bob Sinclar and David Guetta — [Wikipedia: French house](https://en.wikipedia.org/wiki/French_house). Filter house started mid-90s in France on labels such as Roulé and Crydamoure — [Splice](https://splice.com/blog/filter-house-history-ingredients-techniques). Nu-disco is guitar- and bass-lick-driven in the disco tradition. Examples: Nile Rodgers with Daft Punk (2013), Breakbot "Baby I'm Yours", Classixx "Holding On", Luxxury "Be Good 2 Me" — [Wikipedia: Nu-disco](https://en.wikipedia.org/wiki/Nu-disco). "One More Time" is among the most influential filter-disco examples — [Wikipedia: Nu-disco](https://en.wikipedia.org/wiki/Nu-disco). Other artists: Fred Falke, Alan Braxe, Modjo — [NI: French house](https://blog.native-instruments.com/french-house-music/). **By ear:** a disco loop "breathing" open and closed under a filter, and the whole track pumping against the kick. "The loop is the song; the filter is the arrangement" — [Futureproof Genre Explorer](https://genreexplorer.futureproofmusicschool.com/genre/french-house).
2. **Tempo:** French house 110–130 BPM in 4/4 — [Wikipedia: French house](https://en.wikipedia.org/wiki/French_house). Nu-disco editorial range 110–125, measured median 122 — [Mixgraph: Nu-disco](https://www.mixgraph.io/bpm-for/nu-disco). Default 122–124 for French touch, 115–120 for nu-disco (convention). Hats are dragged slightly forward of the grid for swing — [NI: French house](https://blog.native-instruments.com/french-house-music/).
3. **Harmony:** Whatever the sampled loop contains, usually a 1–2-chord disco/funk phrase. Original hooks are often written to match the sample — [Wikipedia: French house](https://en.wikipedia.org/wiki/French_house). Convention: m7/9 Dorian two-chord loops (e.g. Am9 → D9), or a 4-chord maj7 loop.
4. **Vocals:** Vocoder or talkbox is common (Daft Punk) — [Splice](https://splice.com/blog/filter-house-history-ingredients-techniques). Chopped disco diva phrases (convention).
5. **Instrumentation:** A 2–4-bar sampled loop from a disco/funk record, repeated for the whole track with filter, phaser and flanger variations. A heavy, tight kick (usually a 909) sidechained to almost everything. Hats, snares, claps, short funky synth lines, an optional bassline, lots of filter automation — [Splice](https://splice.com/blog/filter-house-history-ingredients-techniques).
6. **Rhythm:** NI layout: kick on every beat, snare/clap on 2 and 4, hats on the "&" of each beat (bar.beat.step positions x.x.3) — [NI: French house](https://blog.native-instruments.com/french-house-music/).
   ```
   Kick  X . . . | X . . . | X . . . | X . . .
   Clap  . . . . | X . . . | . . . . | X . . .
   OHat  . . o . | . . o . | . . o . | . . o .   (nudge 2-5 ticks early)
   Loop  [2-4 bar disco sample, sidechained to kick]
   ```
7. **Bass:** Sample-based, or MIDI in the sample's key — [NI: French house](https://blog.native-instruments.com/french-house-music/). Nu-disco favours a live-style octave or slap bass riff — [Wikipedia: Nu-disco](https://en.wikipedia.org/wiki/Nu-disco).
8. **Form:** Nu-disco avoids pop verse–chorus. It uses drawn-out, repetitive sections that ramp up and down, brought to life with filters and subtle changes — [Wikipedia: Nu-disco](https://en.wikipedia.org/wiki/Nu-disco). NI uses 8- and 16-bar blocks: intro (kick, top loop, bass) → build (add drums) → drop (everything) — [NI: French house](https://blog.native-instruments.com/french-house-music/).
9. **Mix:** Sidechain pump. Filter automation: low-pass from ~75 Hz at the start, ~5–6 kHz in the breakdown, fully open (19.9 kHz) at the drop. High-pass at 90–100 Hz initially, removed at the drop. Phaser on the loop, delay on the snare/clap — [NI: French house](https://blog.native-instruments.com/french-house-music/).
10. **Neighbours:**
    - Disco house (house with disco samples; earlier house notes).
    - Nu-disco: more live riffs, less pumping, often slower — [Wikipedia: Nu-disco](https://en.wikipedia.org/wiki/Nu-disco).
    - Future funk: a sample-based microgenre built on city pop — [Wikipedia: City pop](https://en.wikipedia.org/wiki/City_pop).
11. **FL:**
    - (a) 123 BPM.
    - (b) Chop a 2- or 4-bar loop in Edison/Slicex and stretch it to tempo.
    - (c) Fruity Love Philter or Fruity Filter low-pass on the loop. Automate the cutoff 75 Hz → 20 kHz across 16–32 bars.
    - (d) Sidechain the loop/bass to the kick with Fruity Limiter (comp mode, sidechain input from the kick mixer track). Fast attack, release ~100–200 ms, 4–8 dB of gain reduction (convention).
    - (e) Fruity Phaser on breakdowns, Vocodex vocoder hook.

    **Mistakes:** a static unfiltered loop, too much modern sub, EDM risers, missing pump.

#### CARD 14: Modern funk, boogie revival and city-pop/"city funk" revival (2000s–2026)
- **Identity:** Dâm-Funk (Stones Throw) has been the leading ambassador of the boogie/modern-funk revival since the mid-to-late 2000s. He describes "modern funk" as a meld of P-Funk and Prince with drum machines and post-house groove, from vintage synths and drum machines. The LA DJ night Funkmosphere connected the LA, SF, Chicago and Montreal modern-funk scenes — [First Avenue](https://first-avenue.com/performer/dam-funk-dj-set/), [PopMatters](https://www.popmatters.com/dam-funk-endless-quest-interview), [Stones Throw](https://www.stonesthrow.com/?p=14587) (search-snippet attributions; exact page for each quote not verified). Vulfpeck (formed 2011 by University of Michigan music students) revives a Motown/old-school sound — [UCSB Bottom Line](https://thebottomline.as.ucsb.edu/?p=44826). Cory Wong is a funk-guitar figure in that orbit — [Guitar Player](https://guitarplayer.com/lessons/cory-wong-guitar-lesson). City pop: Japanese 1970s–80s pop rooted in AOR, jazz fusion and funk (Tatsuro Yamashita, Haruomi Hosono, Happy End). Since the 2010s it has resurged online, led by Mariya Takeuchi (1984 "Plastic Love"), and it is a touchstone for vaporwave and future funk — [Wikipedia: City pop](https://en.wikipedia.org/wiki/City_pop). **By ear:** modern funk is boogie (Card 10) made today: synth bass, talkbox, 80s drum machines. Vulfpeck-style is dry, minimal, live Motown/funk with heavy compression. City pop has a glossy AOR band, maj7 chords, slap bass, brass, and Japanese vocals.
- **Tempo:** Modern funk 100–118. Vulfpeck-style 95–115. City pop 100–125. Future funk 110–130 (all convention, unsourced).
- **Harmony (convention):** City pop leans on maj7/9 and the "royal road" IVmaj7–V7–iii7–vi (in C: Fmaj7–G7–Em7–Am). Modern funk uses m9 Dorian vamps and ii–V synth chords.
- **Rhythm:** Use the boogie grid (Card 10) for modern funk. For city pop, a live 16th-hat pop-funk groove with snare on 2 and 4 and swing 52–55% (convention).
- **FL:** Modern funk: LinnDrum/808 FPC kit, Sytrus square/saw bass with glide, Vocodex or a talkbox-style vocoder on the lead, Juno-style chorus pads. City pop: FL Keys or a DX7-style FM EP from Sytrus, slap bass library, brass section, bright plate reverb. Future funk: chop city-pop samples and apply the French-touch workflow (Card 13) (convention). **Mistakes:** trap hats, an overly loud modern master, triad harmony.

### Inferences
- The most reliable single cue separating disco from French touch is drums plus processing. Disco has live-feel drums, loud open hats, strings and dynamic level. French touch has a 909 kick, a sidechain pump and filter automation on one loop (derived from Cards 3 and 13).
- Funk vs boogie vs disco is decided by the kick: funk is syncopated and anchored on 1, boogie leaves out four-on-the-floor and accents 2 and 4 with claps, disco has four-on-the-floor (derived from Wikipedia: Funk, Boogie, Disco).
- Swing amount is the cleanest numeric separator: disco/Motown/French ≈ 50–54%, funk/boogie ≈ 54–58%, NJS ≈ 62–66%, neo-soul uses per-note offsets instead of global swing (derived, conventions marked above).
- Gospel's harmonic fingerprint (chromatic dom7 approach chords, #IVdim7, altered VI7, bass walk-ups) carries into neo-soul and 90s R&B keyboard playing. Neo-soul then strips out the dominant function (2-5-1s) and loops colour chords instead (derived from the PianoGroove sources).

### Gaps
- No authoritative published BPM ranges were found for Motown, Stax, Philly soul, doo-wop, gospel/shout, P-Funk, modern funk or city pop. Those numbers are marked (convention).
- I could not fetch transcriptions of specific drum parts (e.g. "Funky Drummer", Al Jackson Jr.'s grooves, Benny Benjamin). Grids here are derived from verbal descriptions or are convention, not transcriptions.
- The NJS tempo range comes only from weak sources (a forum and a podcast snippet). The Riley "16th-note triplet hats" claim comes from a magazine column, not an interview transcript.
- 2025–2026 current state: no sourced material was gathered this session on the 2020s disco-pop wave or recent gospel/worship trends. Unverified pointers to check: Dua Lipa *Future Nostalgia* (2020), Silk Sonic (Bruno Mars/Anderson .Paak, 2021) as a Philly-soul revival, Maverick City Music / Kirk Franklin collaborations, and the continued TikTok-era city-pop and future-funk revival.
- Reverb's "The Low-End Legacy of D'Angelo's Voodoo" (Pino Palladino bass) returned HTTP 403, so neo-soul bass specifics are convention.

## Key question: What grooves define each style (as 16-step grids)?

### Takeaway
Each style's groove reduces to where the kick and backbeat sit and how much the 16ths swing. The cards above give full grids. The table below is the quick lookup and grid summary.

### Cited Findings
| Style | Kick | Backbeat / accent | Hats | Swing | Source basis |
|---|---|---|---|---|---|
| JB funk | Syncopated, heavy on 1 | Snare 2 and 4, with displaced hits (bar-1 beat-4 delayed an 8th in "Cold Sweat") | 16ths, accented 8ths | light | [Wikipedia: Cold Sweat](https://en.wikipedia.org/wiki/Cold_Sweat), [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk) |
| Disco | Four on the floor | Snare 2 and 4 | 16th "sock cymbal", open on "&" | ~none | [Wikipedia: Earl Young](https://en.wikipedia.org/wiki/Earl_Young_(drummer)), [Wikipedia: Disco](https://en.wikipedia.org/wiki/Disco) |
| Motown | Four on the floor ("pulsating") | 2 and 4 + tambourine + guitar chop | 8ths | gentle | [Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/), [Reverb](https://reverb.com/news/video-what-makes-motown-sound-like-motown) |
| Boogie | No four-on-the-floor | Strong 2 and 4 (clap) | 8ths/16ths | light | [Wikipedia: Boogie](https://en.wikipedia.org/wiki/Boogie_(genre)) |
| NJS | Syncopated hip-hop kick | Dominant snare 2 and 4 | Off-beat accented 16th triplets | heavy | [Wikipedia: NJS](https://en.wikipedia.org/wiki/New_jack_swing), [Mixdown](https://mixdownmag.com.au/features/columns/producer-focus-teddy-riley) |
| Neo-soul | Loose | Snare late, behind the beat | Drunk, uneven | per-note offsets | [Wikipedia: Voodoo](https://en.wikipedia.org/wiki/Voodoo_(D%27Angelo_album)) |
| Shout | Four (convention) | Snare + clap on every upbeat | 16ths | none | [Wikipedia: Shout](https://en.wikipedia.org/wiki/Shout_(Black_gospel_music)) |
| French touch | 909 four on the floor | Clap 2 and 4 | Off-beat, slightly early | slight push | [NI](https://blog.native-instruments.com/french-house-music/), [Splice](https://splice.com/blog/filter-house-history-ingredients-techniques) |

- The disco quaver pattern is often doubled by rhythm guitar. Latin layers (rhumba over merengue) are common — [Wikipedia: Disco](https://en.wikipedia.org/wiki/Disco).
- Funk horns and guitar act as percussion. All of the band's instruments are used percussively — [Wikipedia: Cold Sweat](https://en.wikipedia.org/wiki/Cold_Sweat).

### Inferences
- The interlock rule for this family: the bass and the guitar/clav should rarely attack on the same 16th, apart from beat 1 in funk. Disco bass alternates octaves against the steady kick, and Motown bass "weaves around" the kick and snare (derived from [Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/) and [Wikipedia: Disco](https://en.wikipedia.org/wiki/Disco)).

### Gaps
- No sourced numeric swing percentages were found for any of these styles. All swing values are convention.

## Key question: What harmony defines each style?

### Takeaway
Funk: extended chords on 1–2-chord vamps. Gospel: a 1–4–5 skeleton decorated with chromatic and diminished passing chords and bass walk-ups. Neo-soul: looped m9/m11/maj13/13sus colours without ii–V–I. Disco: minor-7 Dorian vamps and simple triads without 5ths. Doo-wop/Motown: the I–vi–IV–V family.

### Cited Findings
- **Funk:** Fm11, C7(#9)sus4, F9, Cm6, F6/9. Minor 7ths preferred over minor triads — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). One change to the subtonic at the bridge in "Cold Sweat" — [Wikipedia: Cold Sweat](https://en.wikipedia.org/wiki/Cold_Sweat).
- **Gospel, in F** — [PianoGroove](https://pianogroove.com/blues-piano-lessons/gospel-passing-chords-substitutions/):
  - Ab7 → A7 → Bb9sus → Bbmaj7
  - F → D7(b9#9#5) → Gm7 → C7, with E7 → D7sus inserted
  - Bb7 → Bdim7 → F/C
  - F7 – F7/A – Bb – Bbdim7 – C7
  - Walk-ups II→IV and II→V — [PianoGroove](https://pianogroove.com/?p=5342).
  - Shout organ holds dom7 chords over chromatic bass — [Wikipedia: Shout](https://en.wikipedia.org/wiki/Shout_(Black_gospel_music)).
- **Neo-soul:**
  - Bbm11 → Gm9 → Gbmaj13 → Eb m11.
  - Voicings Bb-F-Ab-C-Eb and G-C-F-A-E (G13sus).
  - Half-step slides into the 3rd or 7th.
  - Loops instead of 2-5-1s — [PianoGroove](https://www.pianogroove.com/?p=21017).
  - Cluster and quartal voicings — [Fundamental Changes](https://www.fundamental-changes.com/neo-soul-chords/).
- **Disco:**
  - Verse Em – Bm7(D/B) – Am7(C/A) – D, D# push.
  - Chorus Em – G – A.
  - Fifthless voicings — [NI](https://blog.native-instruments.com/disco/).
- **Doo-wop:** C – Am – F – G (50s progression). Its precedent is C – Am – Dm – G (I–vi–ii–V) — [Wikipedia: Doo-wop](https://en.wikipedia.org/wiki/Doo-wop).
- **Quiet storm:** jazz flourishes, "smooth grooves" — [Wikipedia: Quiet storm](https://en.wikipedia.org/wiki/Quiet_storm).

### Inferences
- A practical "soulify" ladder for a composer-AI (derived from the sources above):
  1. Triads → 7ths.
  2. Add 9ths on minor and dominant chords.
  3. Make V a 13sus or 7#9.
  4. Add a chromatic approach chord (dom7 a half-step above or below) before strong-beat targets.
  5. Use a #IVdim7 between IV and I/5.
  6. Add bass walk-ups.

  Gospel stops at step 6. Neo-soul instead removes the cadences (step 4 and the V7) and loops colour chords. Funk collapses everything to one dom9 or m7.

### Gaps
- No sourced Philly-soul or Motown harmonic analyses were retrieved, so the progressions given for them are convention.

## Key question: How are horns, strings, rhythm guitar, clavinet, Rhodes and slap bass arranged?

### Takeaway
In funk every instrument is percussion. Horns and guitar play short syncopated stabs. Philly/disco strings provide sustained harmony, octave counter-lines and sweeps. Rhodes and organ comp chords; clav plays a percussive 16th riff; slap bass drives the hook.

### Cited Findings
- **Horns:** Funk sections run from tenor sax, trumpet and trombone up to quintets/sextets with bari sax. Parts are rhythmic and syncopated, with off-beat phrases and rhythmic displacement. They punctuate lyrics and are especially important in intros. They mimic the percussive style of funk rhythm guitar — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). Memphis soul uses brass and saxophone prominently — [Wikipedia: Memphis soul](https://en.wikipedia.org/wiki/Memphis_soul). NI's disco brass stab line: A3 G3 F#3 D3 E3 (bars 1–4), A3 G3 F#3 (bars 5–8), with hall reverb — [NI](https://blog.native-instruments.com/disco/).
- **Rhythm guitar:**
  - Chicken scratch (Jimmy Nolen): staccato, muted 16th strums. The hand keeps a constant down-up motion; the chord sounds only where fretting pressure is applied — [Premier Guitar](https://www.premierguitar.com/lessons/rhythm/how-to-play-funk-guitar), [London Guitar Academy](https://www.londonguitaracademy.com/mastering-funk-guitar).
  - The pattern of attack points matters more than pitch, so the guitar is used like an African drum or idiophone — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk).
  - Nile Rodgers: polished jazz-inflected "chanks" (maj7/9 voicings), alternately strumming bass-side and treble-side string sets for texture — [London Guitar Academy](https://www.londonguitaracademy.com/mastering-funk-guitar), [Your Guitar Academy](https://yourguitaracademy.com/courses/nile-rogers/lessons/good-times-guitar-lesson).
  - Motown guitar: fragmented parts around downbeats and vocals — [Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/).
- **Keys:** Funk uses acoustic piano ("September"), Hammond B3 ("Cissy Strut"), clavinet, RMI, Minimoog and ARP string ensemble (P-Funk) — [Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk). Neo-soul's core is the Fender Rhodes — [Wikipedia: Voodoo](https://en.wikipedia.org/wiki/Voodoo_(D%27Angelo_album)).
- **Bass:** Slap (Larry Graham, late 60s) spread to funk and disco — [Wikipedia: Slapping](https://en.wikipedia.org/wiki/Slapping_(music)). Boogie uses prominent slap or synth bass — [Wikipedia: Boogie](https://en.wikipedia.org/wiki/Boogie_(genre)). Disco uses broken octaves — [Wikipedia: Disco](https://en.wikipedia.org/wiki/Disco).
- **Strings:** NI's disco intro is strings only for 4 bars — [NI](https://blog.native-instruments.com/disco/). Philly soul's sound is arrangement-led, a "producers' genre" — [Wikipedia: Philadelphia soul](https://en.wikipedia.org/wiki/Philadelphia_soul).

### Inferences
- Register map for a dense soul/funk arrangement (derived, convention). If a part has nothing to answer, mute it.

  | Part | Register | What it plays |
  |---|---|---|
  | Bass | E1–G2 | |
  | Guitar scratch | ~E3–E5 | Thin upper voicings (3-7-9 on the top strings) |
  | Clav | C3–C5 | 16th riff interlocking with the guitar on different 16ths |
  | Rhodes/organ | C3–C5 | Sustained or comping |
  | Horns | Trumpet ~C4–C6, sax/trombone an octave below | Stabs |
  | Strings | Violins C5–C7 doubled an octave down | |

- Arrangement roles: guitar and clav are the rhythm; horns are punctuation in the gaps between vocal lines; strings are glue and lift (derived).

### Gaps
- No sourced horn-voicing specifics (e.g. close-position triads vs unison) were retrieved. Treat horn voicings as convention: unison/octave for funk riffs, 3-part close voicing for soul pads.

## Key question: How do producers recreate these in a DAW (FL Studio), and what makes them sound fake?

### Takeaway
Authenticity comes from (1) the genre's swing/offset profile, (2) velocity-dynamic ghost notes, (3) era-correct sound sources and processing (tape and echo chamber for 60s soul, mono saturation for neo-soul, filter plus sidechain for French touch), and (4) interlocking parts instead of stacked unison rhythms.

### Cited Findings
- NI's disco build in a DAW: a string loop held for 8 bars, a Studio Drummer funk kit (kick C1, snare D#1, closed hat G#1, open hat F#1), a Rickenbacker-sampled octave bass at velocity 127, brass stabs, an Ozone "RnB/Soul" master — [NI](https://blog.native-instruments.com/disco/).
- NI's French house build: one 2–4-bar sample, a filter automation map (75 Hz → 5–6 kHz → 19.9 kHz), HPF at 90–100 Hz removed at the drop, phaser, delay on the clap, hats dragged slightly forward — [NI](https://blog.native-instruments.com/french-house-music/). A 909 kick sidechained to everything — [Splice](https://splice.com/blog/filter-house-history-ingredients-techniques).
- Motown processing: a bright tiled echo chamber on vocals and drums, tape driven hard — [Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/). Stax: a raw mono room — [Wikipedia: Stax](https://en.wikipedia.org/wiki/Stax_Records).
- Neo-soul: mono, saturated drums; behind-the-beat Dilla feel — [Reverb](https://reverb.com/news/video-dangelos-vibey-the-line-drums-whats-that-sound), [Wikipedia: Voodoo](https://en.wikipedia.org/wiki/Voodoo_(D%27Angelo_album)).
- NJS: SP-1200 + TR-808 with a dominant snare — [Mixdown](https://mixdownmag.com.au/features/columns/producer-focus-teddy-riley).

### Inferences
- FL Studio stock mapping (convention; check availability in FL 21):

  | Need | FL stock tool |
  |---|---|
  | Drums | FPC (choke open/closed hats via a cut group) |
  | Rhodes, Wurli, piano | FL Keys |
  | Strings, brass, choirs, organ presets | FLEX |
  | Synth bass and FM EPs | Sytrus / 3x Osc |
  | Bass guitar (fallback) | BooBass |
  | Filter sweeps | Fruity Love Philter / Fruity Filter |
  | Sidechain | Fruity Limiter |
  | Vocoder/talkbox | Vocodex |
  | Echo chamber / plate | Fruity Reeverb 2 / Fruity Convolver |
  | Swing | Channel-rack swing knob |
  | Offsets and humanizing | Piano-roll quantize strength, randomize |
  | SP-1200 grit | Fruity Squeeze / bitcrush |
  | Era-correct glue | Fruity Blood Overdrive |

- Universal "fake" tells for this family (derived):
  - all velocities equal;
  - ghost notes missing;
  - bass doubling the kick rhythm exactly;
  - full-range sampled chords stacked on every instrument (mud);
  - modern 808 sub or trap hats in retro styles;
  - over-wide stereo on 60s material;
  - horns or strings playing long sustained notes where stabs belong;
  - heavily quantized neo-soul or funk.

### Gaps
- FL-specific workflows for these genres were not found in Image-Line sources this session. The FL mapping above is convention, based on FL's stock plugin set.
