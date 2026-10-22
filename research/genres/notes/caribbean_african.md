# Caribbean and African Genres: Recipe Cards for FL Studio

Scope: ska, rocksteady, roots reggae (one drop / rockers / steppers), dub, lovers rock, dancehall (classic digital + modern), calypso, soca, zouk, kompa, bouyon; 1970s Afrobeat, highlife, juju, Congolese rumba/soukous, mbalax, gqom, kwaito, kuduro, afro-house roots, bongo flava, Ethio-jazz, UK afroswing, alté.
Excluded (covered elsewhere, cross-reference only): afrobeats, amapiano, reggaeton/dembow, house, dubstep (see `research_notes/Music theory and beat making/`).

**Grid notation** (from genre-card-format.md): 16 steps = 1 bar of 4/4; step 1 = beat 1, 5 = beat 2, 9 = beat 3, 13 = beat 4. `X` accent, `x` normal, `g` ghost, `.` rest, `o` open hat.
**Number tags:** (sourced) = from a cited source; (convention) = common producer practice, not tied to one source and to be checked by ear; (derived) = my own inference from sourced facts.
**Confidence warning:** most rhythm grids below are (convention). I found few published note-level transcriptions online. Exceptions: the one drop / rockers / steppers definitions, the highlife clave-guitar relationship, the gqom kick families and the afroswing "snare on three" rule, which are all sourced. Treat every other grid as a starting template to check against the reference tracks.

---

## 1. Genre recipe cards: defining rhythms, bass/harmony and instrumentation per genre

### Takeaway
Most Jamaican styles are told apart by **where the kick lands relative to the offbeat skank**. Ska has a fast walking bass and every-offbeat skank. In rocksteady and reggae the skank sits on beats 2 and 4 and the kick moves to beat 3 (one drop), all four beats (rockers) or every beat at double-time (steppers). Dancehall drops the one drop for a syncopated, programmed kick.
The Eastern Caribbean styles split by tempo and percussion:
- soca: about 115–165 BPM, four-on-the-floor plus an iron (brake drum)
- zouk and kompa: 90–145 BPM, tresillo-flavoured rims and bells, lush keys
- bouyon: fast, keyboard-riff driven

The African styles split by guitar language:
- highlife: clave-shaped arpeggios
- Afrobeat: interlocking muted tenor guitar plus chord-chop guitar
- soukous: high, looping sebene lead guitar
- the electronic SA/Angolan styles: kick placement (gqom broken kick vs kwaito slowed four-on-the-floor vs kuduro at about 140 BPM)

### Cited Findings

#### 1.1 Ska (Jamaica, late 1950s–mid 1960s)
- **Identity:** Jamaican genre of the late 1950s. Its roots are mento, jazz and New Orleans R&B, and it led to rocksteady, reggae and dancehall ([Wikipedia: Ska](https://en.wikipedia.org/wiki/Ska)).
  - Key artists: the Skatalites, Prince Buster, Desmond Dekker, Toots & the Maytals (unsourced, well known). 2 Tone (UK, around 1979: the Specials, Madness) and third wave (US 1990s) are fusion descendants ([Wikipedia: Ska](https://en.wikipedia.org/wiki/Ska) lists two-tone among fusion genres).
  - Reference tracks: Skatalites "Guns of Navarone"; Millie Small "My Boy Lollipop"; Prince Buster "Al Capone".
  - **By ear:** fast, upbeat, choppy guitar or piano on **every** offbeat 8th, a walking bass and big unison horn lines.
- **Tempo & feel:** about 110–135 BPM for 1960s ska, 140–170 for 2 Tone/third wave (convention). Straight to lightly shuffled 8ths, swing about 55–60% (convention).
- **Harmony:** major keys. I–IV–V and I–vi–IV–V (doo-wop/R&B heritage), e.g. in Bb: Bb–Gm–Eb–F. Harmonic rhythm 1 chord per bar or per half-bar (convention).
- **Melody/vocals:** jazz-influenced horn heads (trombone, tenor sax, trumpet), with solos between vocal sections (convention).
- **Instrumentation:** drum kit, upright or electric bass, guitar, piano/organ, horn section (convention). DAW: FL Keys or electric piano for the "chop", a clean Strat-type guitar sample, a brass ensemble library, upright-bass samples.
- **Rhythm (convention):**
  ```
  Kick   X . . . | . . . . | X . . . | . . . .
  Snare  . . . . | X . . . | . . . . | X . . .   (rimshot/cross-stick)
  Hat    x . x . | x . x . | x . x . | x . x .   (light shuffle)
  Skank  . . X . | . . X . | . . X . | . . X .   (guitar+piano on every "and")
  Bass   X . . . | x . . . | x . . . | x . . .   (walking quarters)
  ```
- **Form:** about 2:30–3:00. Intro (horns), verse/chorus, then a horn or sax solo chorus (convention).
- **FL Studio:** set swing 55–60% on the hats only. Keep the skank note length very short (about a 1/16 gate), and avoid long sustained pads (convention).

#### 1.2 Rocksteady (Jamaica, about 1966–1968)
- **Identity:** originated around 1966. It was dominant in Jamaica for about two years and sits between ska and reggae ([Wikipedia: Rocksteady](https://en.wikipedia.org/wiki/Rocksteady)).
  - Harmony groups: the Techniques, the Paragons. Musicians: Jackie Mittoo, Lynn Taitt, Tommy McCook. The name comes from a slower dance named in the Alton Ellis song "Rocksteady" ([Wikipedia: Rocksteady](https://en.wikipedia.org/wiki/Rocksteady)).
  - Rocksteady is "slower than ska", with more romantic lyrics and less prominent horns. One theory: Hopeton Lewis couldn't sing "Take It Easy" at ska tempo ([Wikipedia: Reggae](https://en.wikipedia.org/wiki/Reggae)).
  - Influences: American R&B (Fats Domino, Louis Jordan), mento, African drumming and soul ([Wikipedia: Rocksteady](https://en.wikipedia.org/wiki/Rocksteady)).
  - Reference tracks: Alton Ellis "Rock Steady"; the Paragons "The Tide Is High"; Phyllis Dillon "Perfidia".
  - **By ear:** ska slowed down, a soulful vocal harmony group, and the bass breaks free into short melodic phrases with gaps.
- **Tempo:** about 80–105 BPM (convention). Straight to mildly swung.
- **Harmony:** soul-style progressions in major keys, e.g. I–IV–V–IV, and I–vi–ii–V (in F: F–Dm–Gm–C) (convention).
- **Rhythm:** the guitar skank moves to beats 2 and 4. In reggae the slower tempos then allowed "double skank" offbeat strokes ([Wikipedia: Reggae](https://en.wikipedia.org/wiki/Reggae)). Template (convention):
  ```
  Kick   . . . . | . . . . | X . . . | . . . .   (proto one drop) or X on 1 and 9
  Rim    . . . . | X . . . | . . . . | X . . .
  Hat    x . x . | x . x . | x . x . | x . x .
  Skank  . . . . | X . . . | . . . . | X . . .
  Bass   . . X . | . . x . | X . . . | x . x .   (melodic, leaves holes)
  ```

#### 1.3 Roots reggae: one drop, rockers, steppers (Jamaica, late 1960s–1980s)
- **Identity:** reggae developed from ska and rocksteady in the late 1960s ([Wikipedia: Reggae](https://en.wikipedia.org/wiki/Reggae)). Roots reggae draws on Nyabinghi and riddim traditions and is linked to Rastafari ([Wikipedia: Roots reggae](https://en.wikipedia.org/wiki/Roots_reggae)).
  - Carlton Barrett (the Wailers' drummer) is credited with taking the one drop mainstream ([MusicRadar one-drop tutorial, via search summary](https://www.musicradar.com/how-to/how-to-program-a-typical-one-drop-reggae-beat-and-add-fills)).
  - Reference tracks: Bob Marley & the Wailers "Stir It Up" / "One Drop"; Burning Spear "Marcus Garvey"; Culture "Two Sevens Clash"; Israel Vibration "Same Song". Rockers: Sly & Robbie-era Black Uhuru "Shine Eye Gal". Steppers: Revolutionaries / Mighty Diamonds sessions; UK steppers by Jah Shaka and Iration Steppas.
  - **By ear:** half-time, floaty, beat 1 left empty, a big melodic bass, a guitar chop on 2 and 4, and an organ "bubble".
- **Tempo & feel:** roots reggae is quoted at **70–90 BPM** ([Orphiq: What is dancehall, comparison table](https://orphiq.com/resources/what-is-dancehall)). Hats are usually swung or shuffled to sit with the bass ([wayneandwax roots riddim tutorial](https://www.wayneandwax.com/org/lessons/roots-riddim-tutorial.html)). 4/4 only: the repeating strong/weak pattern doesn't suit 3/4 ([Wikipedia: Reggae](https://en.wikipedia.org/wiki/Reggae)).
- **Counting conflict:** Wikipedia and Orphiq put the one-drop kick (+ snare) on **beat 3** with beat 1 empty ([Wikipedia: One drop rhythm](https://en.wikipedia.org/wiki/One_drop_rhythm); [Orphiq](https://orphiq.com/resources/what-is-dancehall)). The wayneandwax FruityLoops tutorial says the drop is on **beats 2 and 4** ([wayneandwax](https://www.wayneandwax.com/org/lessons/roots-riddim-tutorial.html)). These are the same groove counted at double tempo (about 150 BPM vs about 75 BPM) (derived). **Recommendation:** program at 70–80 BPM with the drop on step 9.
- **Variations (sourced definitions):** "rockers" is the one drop plus a steady kick on every quarter note. "Steppers" is the one drop plus a kick on every eighth note. One drop is slower than ska, and rockers is often slower than one drop ([Wikipedia: One drop rhythm](https://en.wikipedia.org/wiki/One_drop_rhythm)).
- **Rhythm grids at about 75 BPM** (one drop and rockers placement sourced as above; the hat and keys detail is convention):
  ```
  ONE DROP
  Hat    x . x . | x . x . | x . x . | x . x .   (swing 60-66%, or 12/8 triplet hats)
  Rim    . . . . | . . . . | X . . . | . . . .   (cross-stick; fills on bar 4/8 only)
  Kick   . . . . | . . . . | X . . . | . . . .
  Skank  . . . . | X . . . | . . . . | X . . .   (guitar+piano chop on 2 and 4)
  Organ  . . x g | . . x g | . . x g | . . x g   ("bubble": offbeat 16th pairs)
  Bass   . . . . | . . X . | X . . x | . . x .   (often silent on beat 1, lands with the drop)

  ROCKERS (kick on every beat; Sly Dunbar-style busier 16th hats)
  Kick   X . . . | X . . . | X . . . | X . . .
  Rim    . . . . | . . . . | X . . . | . . . .
  Hat    x x x x | x x x x | x x x x | x x x x   (accent offbeats, open hat on some "and"s)

  STEPPERS (kick on every 8th at a 75 count = four-on-the-floor at a 150 count)
  Kick   X . X . | X . X . | X . X . | X . X .
  Rim    . . . . | . . . . | X . . . | . . . .
  ```
- **Fills:** use rimshot syncopated turnarounds sparingly, about every 4 or 8 bars. A little delay on the hat makes it feel more active ([wayneandwax](https://www.wayneandwax.com/org/lessons/roots-riddim-tutorial.html)).
- **Ensemble:** two guitars (rhythm + lead), drums, congas, keyboards and a couple of vocalists ([Wikipedia: Reggae](https://en.wikipedia.org/wiki/Reggae)).
  - Reggae is "made" from an offbeat skank on guitar and keys, a relaxed one drop, a deep melodic bass and roughly 60–90 BPM ([violetrecording, via search summary](https://violetrecording.com/how-to-make-reggae-music/)).
- **Harmony (convention):** often 1–2 chord minor vamps, e.g. i–iv (Am–Dm) or i–VII (Am–G). Also major I–IV–V. Common progressions:
  - I–V–vi–IV (in G: G–D–Em–C)
  - i–VII–VI–VII (Am–G–F–G)
  Harmonic rhythm is 1 chord per 1–2 bars. Orphiq has a dedicated "Reggae chords: 6 progressions" page (not fetched).
- **Melody/vocals:** call-and-response harmony trios, Rasta/conscious lyric themes, relaxed behind-the-beat phrasing (convention).
- **Form:** about 3:30–4:30 with intro, verse, chorus, verse, chorus, then often a dub-style instrumental outro. Vinyl B-side = "version" (see 1.4).

#### 1.4 Dub (Jamaica, late 1960s–1970s → global)
- **Identity:** pioneered by engineer-producers King Tubby, Scientist, Lee "Scratch" Perry and Errol Thompson. Augustus Pablo brought the melodica. Producers treated the **mixing console as an instrument** ([Wikipedia: Dub music](https://en.wikipedia.org/wiki/Dub_music)).
  - By 1973 instrumental "versions" had evolved into dub as a subgenre ([Wikipedia: Dub music](https://en.wikipedia.org/wiki/Dub_music)).
  - A dub is a "version" of an existing song, usually instrumental with some or all of the vocal removed. It was originally a 45 B-side emphasising drums and bass for sound systems, and a bed for DJs to toast over ([Wikipedia: Dub music](https://en.wikipedia.org/wiki/Dub_music)).
  - Reference tracks: King Tubby Meets Rockers Uptown (Augustus Pablo); Scientist "Rids the World of the Evil Curse of the Vampires"; Lee Perry/Upsetters "Super Ape"; modern: Mad Professor, Adrian Sherwood/On-U Sound.
  - **By ear:** a reggae riddim that keeps dropping instruments in and out, with long echo tails, spring-reverb splashes and huge bass.
- **Tempo:** same as roots (70–90) ([Orphiq](https://orphiq.com/resources/what-is-dancehall)). Rhythm grids: as 1.3.
- **Production:** see Section 3.

#### 1.5 Lovers rock (London, mid-1970s–1980s)
- **Identity:** romantic reggae that originated in 1970s London. Origins: rocksteady, reggae, soul and R&B ([Wikipedia: Lovers rock](https://en.wikipedia.org/wiki/Lovers_rock)).
  - Brown Sugar (with Caron Wheeler, later of Soul II Soul) pioneered "conscious lovers". Staple of London sound systems such as Chicken Hi-Fi and Soferno B ([Wikipedia: Lovers rock](https://en.wikipedia.org/wiki/Lovers_rock)).
  - Reference tracks: Janet Kay "Silly Games" (1979); Louisa Mark "Caught You in a Lie"; Carroll Thompson "Hopelessly in Love"; Dennis Brown also crossed into the style (unsourced, well known).
  - **By ear:** reggae one-drop/rockers bed with sweet, often female or falsetto, Philly-soul-style vocals, lush keys and backing harmonies.
- **Tempo:** about 68–85 BPM (convention).
- **Harmony (convention):** soul vocabulary of maj7, m7, m9 and ii–V movement, e.g. ii7–V7–Imaj7–vi7 in Eb: Fm7–Bb7–Ebmaj7–Cm7.
- **Rhythm:** one drop or rockers (1.3), softer rim, more shaker/tambourine (convention).
- **Production:** cleaner and warmer than dub, with chorus on guitar, Rhodes and string pads (convention).

#### 1.6 Dancehall: classic digital (1985–late 1990s) and modern (2000s–2026)
- **Identity:** genre of late-1970s Jamaica. Origins: reggae, dub, toasting, electronic music, ska and rocksteady ([Wikipedia: Dancehall](https://en.wikipedia.org/wiki/Dancehall)).
  - Wayne Smith's "Under Mi Sleng Teng" (1985, Jammy's label, co-written by King Jammy) is the landmark digital riddim ([Wikipedia: Under Mi Sleng Teng](https://en.wikipedia.org/wiki/Under_Mi_Sleng_Teng)).
  - Riddim categories: classic (e.g. Sly & Robbie's Bam Bam), ragga (e.g. Juice riddim, Richard "Shams" Browne) and digital (Sleng Teng, Punaany, Duck — King Jammy) ([Wikipedia: Riddim](https://en.wikipedia.org/wiki/Riddim)).
  - The dembow pattern is traced to Steely & Clevie's late-1980s work, named after Shabba Ranks' "Dem Bow" ([Orphiq: dancehall](https://orphiq.com/resources/what-is-dancehall)). See the earlier reggaeton notes for the grid.
  - Reference tracks:
    - classic: Wayne Smith "Under Mi Sleng Teng"; Shabba Ranks "Dem Bow"; Chaka Demus & Pliers "Murder She Wrote"
    - 2000s: Sean Paul "Get Busy" (Diwali riddim); Elephant Man "Pon de River"
    - modern: Vybz Kartel "Fever"; Spice "Go Down Deh"; Skillibeng "Whap Whap"; Valiant, Masicka (unsourced, well known)
  - **By ear:** sparse, programmed, kick + rim hook, a short repeating synth-bass figure, a deejay (toaster) or singjay voice up front, one drop absent.
- **Tempo:** about **85–110 BPM** ([Orphiq](https://orphiq.com/resources/what-is-dancehall)). Default about 95–100 (convention). Modern trap-influenced dancehall often has 1/32 hat rolls (convention).
- **Defining traits (sourced from [Orphiq](https://orphiq.com/resources/what-is-dancehall)):**
  - programmed syncopated kick, with rim or snare answering off the beat; the one drop is mostly gone
  - bass is a short repeated synth figure, often the main melodic hook
  - harmony is minimal: a stab, a two-note riff, or nothing
  - the middle is left empty for the voice
- **Rhythm grids (convention):**
  ```
  DEMBOW-FAMILY (late 80s/90s ragga; see reggaeton notes)
  Kick   X . . . | X . . . | X . . . | X . . .
  Snare  . . . x | . . X . | . . . x | . . X .

  DIWALI-STYLE CLAP RIDDIM (2002; 3+3+2 claps)
  Kick   X . . . | . . X . | X . . . | . . X .
  Clap   X . . X | . . X . | X . . X | . . X .   (3+3+2 / tresillo pairs)
  Hat    . . x . | . . x . | . . x . | . . x .

  MODERN (2015-26)
  Kick   X . . x | . . X . | X . . . | . . X .
  Rim    . . . . | X . . x | . . . . | X . . .
  Hat    x x x x | x x x x | x x x x | x x x x   (+ 1/32 rolls; trap influence)
  808    follows the kick, short glides
  ```
- **Harmony:** minor keys dominate. One-chord vamps or i–VI–VII (Cm–Ab–Bb). Use stabs, not pads (convention, consistent with [Orphiq](https://orphiq.com/resources/what-is-dancehall)).
- **Vocals:** deejay toasting/chatting in patois, rapid internal rhyme, "singjay" melodic hooks (convention).
- **Form:** a riddim is often 8-bar sections looped, with verse/hook alternation, about 3:00. One riddim is voiced by many artists (a "juggling" album) (convention; see Section 3).

#### 1.7 Calypso (Trinidad & Tobago, early 19th c. → 1950s peak)
- **Identity:** originated in early-19th-century Trinidad & Tobago from kaiso and Canboulay ([Wikipedia: Calypso music](https://en.wikipedia.org/wiki/Calypso_music)). Typical instruments are trumpet, trombone, saxophone, guitar and double bass. Descendants include soca, chutney soca, rapso, cadence-lypso and spouge ([Wikipedia: Calypso music](https://en.wikipedia.org/wiki/Calypso_music)).
  - Key artists: Lord Kitchener, the Mighty Sparrow, Lord Invader, Calypso Rose (unsourced, well known).
  - Reference tracks: Lord Kitchener "London Is the Place for Me"; Mighty Sparrow "Jean and Dinah"; Harry Belafonte "Banana Boat Song (Day-O)" (US pop-calypso).
  - **By ear:** bright major-key 2-beat strum, witty narrative storytelling vocal, horn riffs between lines.
- **Tempo:** about 100–130 BPM with a 2/4 "two-beat" feel (convention).
- **Harmony (convention):** major. I–IV–V7–I and I–V7 alternating every bar or half-bar, e.g. in C: C–F–G7–C. Verse-chorus with a horn "kaiso" break.
- **Rhythm (convention):**
  ```
  Kick   X . . . | . . . . | X . . . | . . . .
  Snare  . . . . | X . . x | . . . . | X . . x
  Gtr    X . x X | . x X . | X . x X | . x X .   (boom-chick-a strum)
  Bass   X . . . | . . X . | X . . . | . . X .   (root, then 5th on the "and" of 2 = anticipation)
  ```

#### 1.8 Soca (Trinidad, 1970s → modern power/groovy soca)
- **Identity:** created by Lord Shorty (Garfield Blackman, later Ras Shorty I) as the "Soul of Calypso".
  - He fused calypso with Indo-Caribbean music after 1965 and debuted it in the early 1970s.
  - "Endless Vibrations" (1975) spread it. The original spelling "sokah" referenced the Indo-Caribbean influence ([Wikipedia: Soca music](https://en.wikipedia.org/wiki/Soca_music)).
  - Related instrument families: tassa, steelpan, brass band ([Wikipedia: Soca music](https://en.wikipedia.org/wiki/Soca_music)).
  - Reference tracks: Lord Shorty "Endless Vibrations"; Arrow "Hot Hot Hot"; Machel Montano "Like Ah Boss" (power); Bunji Garlin "Differentology" (power); Kes "Savannah Grass" (groovy); Destra, Patrice Roberts (unsourced, well known).
  - **By ear:** relentless four-on-the-floor with an iron or cowbell clank, horn stabs, "jump and wave" crowd-call vocals. Fast (power) or mid-tempo and sensual (groovy).
- **Subgenres by tempo:**
  - "Groovy soca" was coined by International Soca Monarch organisers around 2005 as a rebrand of slower styles. "Frenchman" (Robin Imamshah, 1990) is named as a trend-setter ([Wikipedia: Soca music](https://en.wikipedia.org/wiki/Soca_music)).
  - Power soca is about **160 BPM** and groovy soca about **115 BPM** ([NYS Music, via search summary](https://nysmusic.com/2023/08/30/the-birth-and-evolution-of-soca-music/)).
  - St Lucia's competition rules cap groovy soca at **130 BPM** and require power soca to be faster than 130 ([RCI St Lucia](https://rcistlucia.com/?p=11784)).
  - Other production references cite 120–132 for groovy and mid-130s to 140s for road/power ([jackrighteous soca lab, via search summary](https://jackrighteous.com/blogs/build-your-sound-with-ai-music-instrumentals/soca-genre-control-lab-ai-music)).
  - Defaults: power 155–160, groovy 118–124 (derived).
- **Bouyon soca / jump-up:** blends 1990s bouyon rhythms with soca. Mostly St Lucian producers, popular in Antigua, St Lucia and the French Antilles ([Wikipedia: Soca music](https://en.wikipedia.org/wiki/Soca_music)).
- **Rhythm (convention; no note-level source found):**
  ```
  POWER SOCA (~158 BPM)
  Kick   X . . . | X . . . | X . . . | X . . .
  Snare  . . . . | X . . x | . . . . | X . x .   (with offbeat ghost pickups)
  Iron   X . x x | X . x x | X . x x | X . x x   (brake-drum/cowbell gallop)
  OpHat  . . o . | . . o . | . . o . | . . o .
  Bass   . . X . | . . X . | . . X . | . . X .   (offbeat-pumping, or root on beats with octave jumps)

  GROOVY SOCA (~120 BPM)
  Kick   X . . x | . . X . | X . . x | . . X .   (syncopated; dancehall/R&B influence)
  Clap   . . . . | X . . . | . . . . | X . . .
  Perc   tassa/dholak-style 16ths, shaker
  ```
- **Harmony:** major and bright. I–V–vi–IV or I–IV loops, synth-brass stabs; minor for "dark" road tunes (convention).
- **Form:** about 3:00–3:30. Intro with crowd chant → verse → pre (build) → hook/"drop" with instructions (wave, jump) → breakdown → final hook (convention).

#### 1.9 Zouk and zouk-love (Guadeloupe/Martinique, early 1980s)
- **Identity:** pioneered by Kassav' in the early 1980s. **Originally 120–145 BPM**, percussion-driven, with a loud horn section ([Wikipedia: Zouk](https://en.wikipedia.org/wiki/Zouk)).
  - Origins: cadence rampa, compas, cadence-lypso, bèlè, biguine and gwo ka ([Wikipedia: Zouk](https://en.wikipedia.org/wiki/Zouk)).
  - Zouk-love added MIDI instrumentation to compas and "gradually became indistinguishable from compas" ([Wikipedia: Zouk](https://en.wikipedia.org/wiki/Zouk)).
  - Reference tracks: Kassav' "Zouk-la sé sèl médikaman nou ni"; Kassav' "Syé bwa"; zouk-love: Edith Lefel, Jocelyne Béroard, Kaysha, modern Kizomba-adjacent productions (unsourced, well known).
  - **By ear:** fast, horn-led party (classic), or slow, glossy, sensual synth ballad with a rolling tom/rim tresillo (zouk-love).
- **Tempo:** classic 120–145 (sourced); zouk-love about 75–95 (convention).
- **Harmony (convention):** major and minor. Zouk-love loves i–VI–III–VII (Am–F–C–G) and maj7/add9 voicings with long pads.
- **Rhythm (convention; low confidence, check by ear):**
  ```
  ZOUK-LOVE (~85 BPM)
  Kick   X . . . | . . . . | X . . . | . . . .
  Snare  . . . . | X . . . | . . . . | X . . .
  Rim/tom X . . X | . . X . | X . . X | . . X .  (tresillo 3+3+2, the "zouk roll")
  Shaker 16ths
  ```

#### 1.10 Kompa / compas (Haiti, 1955 →)
- **Identity:** a modern méringue dance music of Haiti created by **Nemours Jean-Baptiste** (Ensemble Aux Callebasses 1955, then Ensemble Nemours Jean-Baptiste 1957) ([Wikipedia: Compas](https://en.wikipedia.org/wiki/Compas)).
  - "Compas" means measure/rhythm. Its most distinctive feature is a **consistent pulsating tanbou beat** ([Wikipedia: Compas](https://en.wikipedia.org/wiki/Compas)).
  - It is the main music of Dominica and the French Antilles, partly via zouk ([Wikipedia: Compas](https://en.wikipedia.org/wiki/Compas)).
  - Reference artists: Tabou Combo ("New York City"), Coupé Cloué, Sweet Micky, Carimi, T-Vice, Harmonik, Kai ([Wikipedia: Compas](https://en.wikipedia.org/wiki/Compas) names Tabou Combo and Coupé Cloué; the others are unsourced).
  - **By ear:** steady mid-tempo, almost hypnotic pulse, a clean chorus-guitar arpeggio riff, a cowbell/cymbal-bell cadence, synth pads and horn/keys stabs.
- **Tempo/feel:** "moderate tempo", "remarkably steady". The interlocking guitar, percussion and bass create motion inside a reliable cadence ([jackrighteous kompa lab](https://jackrighteous.com/blogs/build-your-sound-with-ai-music-instrumentals/kompa-compas-genre-control-lab-ai-music)). That source is an AI-music brief site, so this is a weak source. About 95–120 BPM, default 105 (convention).
- **Rhythm (convention; low confidence):**
  ```
  Kick   X . . . | . . . . | X . . . | . . . .
  Tom/tanbou . . . . | . . X . | . . . . | . . X x   (low-tom answer = "pulsating tanbou")
  Bell   X . X X | . X X . | X . X X | . X X .   (cymbal bell/cowbell cadence)
  Hat    . . x . | . . x . | . . x . | . . x .
  Gtr    16th arpeggio riff, palm-light, chorus FX
  Bass   X . . X | . . X . | X . . X | . . X .   (anticipates the next chord)
  ```
- **Harmony (convention):** major and minor two- to four-chord loops, e.g. I–vi–ii–V (C–Am–Dm–G) or i–iv–VII–III (Am–Dm–G–C). Extended jazz-pop voicings.
- **Form:** long dance versions (5–7 min). Verse/chorus, then an extended instrumental "kompa" groove section with guitar/keys solos (convention).

#### 1.11 Bouyon (Dominica, 1988 →)
- **Identity:** Windward Caribbean Kulture (WCK) originated it in 1988 by fusing cadence-lypso with jing ping.
  - Ingredients: native drum rhythms (lapo kabwit), jing-ping band elements and ragga-style vocals ([Wikipedia: Soca music](https://en.wikipedia.org/wiki/Soca_music)).
  - Instruments: tambour bélé, tambou lélé, lapo kabwit, chakchak (maracas), syak/gwaj scraper, tambal, accordion, drums, rhythm guitar, keyboards ([Wikipedia: Bouyon music](https://en.wikipedia.org/wiki/Bouyon_music)).
  - Late 1980s, Roseau ([Wikipedia: Bouyon music](https://en.wikipedia.org/wiki/Bouyon_music)).
  - Fusions: bouyon soca, bouyon-muffin, alternative bouyon, bouyon hybrid ([Wikipedia: Bouyon music](https://en.wikipedia.org/wiki/Bouyon_music)).
  - Reference artists: WCK, Triple Kay International, Asa Bantan, Reo, Signal Band (unsourced, well known).
  - **By ear:** very fast, a frenetic looping keyboard riff (an accordion-like 16th line), four-on-the-floor plus scraper, chanted ragga vocals.
- **Tempo:** about 150–170 BPM (convention).
- **Rhythm (convention):**
  ```
  Kick   X . . . | X . . . | X . . . | X . . .
  Snare  . . x . | X . x . | . . x . | X . x .
  Scraper x x x x | x x x x | x x x x | x x x x
  Keys   16th ostinato riff, 1-2 bars, major-key, 2-3 notes
  ```
- **FL:** use a bright saw/square lead or accordion patch (FL Keys/Sytrus), mono, and repeat it hard (convention).

#### 1.12 Afrobeat, Fela style (Lagos, late 1960s–1970s)
- **Identity:** evolved in late-1960s Nigeria under Fela Kuti with drummer **Tony Allen**. Influences: highlife, fuji, jùjú, Yoruba vocal traditions, jazz and soul ([Wikipedia: Afrobeat](https://en.wikipedia.org/wiki/Afrobeat)).
  - Allen became musical director of Africa '70 in 1969. The band mixed the heavy groove of soul with jazz, highlife and Yoruba polyrhythm ([Wikipedia: Tony Allen](https://en.wikipedia.org/wiki/Tony_Allen_(musician))).
  - Fela wrote out every musician's part except Allen's, who originated his own patterns and played different things with all four limbs ([Wikipedia: Tony Allen](https://en.wikipedia.org/wiki/Tony_Allen_(musician))).
  - Allen took his hi-hat approach from a Max Roach lesson in *DownBeat*; African drummers had rarely used the hi-hat ([search summary of Modern Drummer/Paste obituaries](https://www.moderndrummer.com/2020/04/tony-allen-passes/)).
  - He broke Afrobeat into **five major patterns, all in 4/4**, differing in how the parts are grouped ([Rolling Stone, 2020](https://www.rollingstone.com/music/music-news/tony-allen-afrobeat-drum-patterns-unseen-doc-clip-993318)).
  - Reference tracks: Fela Kuti & Africa '70 "Zombie" (1976), "Water No Get Enemy" (1975), "Lady", "Expensive Shit"; modern: Antibalas, Seun Kuti & Egypt 80, Femi Kuti.
  - **By ear:** a long, hypnotic one-chord jam, a muted high single-note guitar ostinato against a chord-chop guitar, unison sax/trumpet riffs, a loose but locked kit with busy open/closed hat, and a long instrumental intro before the vocal.
- **Tempo:** about 95–130 BPM, straight 16ths with a slight push (convention).
- **Harmony (convention):** a modal vamp on one or two chords, minor or Dorian, e.g. Dm7 (i7) or Dm7–G7 (i7–IV7 Dorian). Horns harmonise in 4ths/octaves. Harmonic rhythm is extremely slow: 1 chord for minutes.
- **Rhythm (convention; derived from the sourced "four independent limbs" description — not a transcription):**
  ```
  Hat    x x o x | x x o x | x x o x | x x o x   (open hat on the "and"s, sizzle)
  Kick   X . . . | . . X . | . . X . | . . . x
  Snare  g . g . | X . g g | . g . g | X . g .   (ghost-note conversation)
  Shekere/conga 16ths; Clave X . . X | . . X . | . . X . X . . .   (3-2)
  TenorGtr  x x . x | . x x . | x . x x | . x . x   (muted single notes, high register, 2-bar loop)
  RhythmGtr . . X . | . . . X | . . X . | . . . X   (short chord chops)
  Bass   X . . x | . . X . | . X . . | X . . .   (2-bar riff, repeated for minutes)
  ```
- **Form:** 10–20+ minutes. A long instrumental intro builds part by part (drums → bass → guitars → keys → horns), then horn head, organ/sax solos, then Fela's vocal with call-and-response chorus. Breakdowns drop to drums + bass (convention).

#### 1.13 Highlife (Ghana, 1920s →; Nigeria)
- **Identity:** in the 1920s Ghanaian musicians mixed foxtrot and calypso with Ghanaian rhythms like osibisaba. The name comes from elite club audiences ([Wikipedia: Highlife](https://en.wikipedia.org/wiki/Highlife)).
  - In the 1940s it split into dance-band highlife (urban; E.T. Mensah & the Tempos, "King of Highlife") and guitar-band highlife (rural; E.K. Nyame's Akan Trio) ([Wikipedia: Highlife](https://en.wikipedia.org/wiki/Highlife)).
  - Highlife's **two-finger picking style** came from the dagomba style of Liberian Kru sailors ([Wikipedia: Highlife](https://en.wikipedia.org/wiki/Highlife)).
  - Congolese music via Radio Brazzaville spawned guitar-based Igbo highlife (Oliver De Coque, Oriental Brothers) ([Wikipedia: Soukous](https://en.wikipedia.org/wiki/Soukous)).
  - Reference tracks: E.T. Mensah "All for You"; Prince Nico Mbarga "Sweet Mother"; Oriental Brothers; burger highlife of 1980s Germany: George Darko "Akoo Te Brofo" (unsourced).
  - **By ear:** bright major-key, sweetly arpeggiated interlocking guitars that dance around a bell/clave, a relaxed mid-tempo lilt, often horns.
- **Rhythm (sourced):**
  - The arpeggiated highlife guitar part is modelled on the Afro-Cuban guajeo.
  - Its attack points are nearly identical to the **3-2 clave** guajeo.
  - The clave bell pattern is **indigenous to Ghana** and used in highlife ([Wikipedia: Highlife](https://en.wikipedia.org/wiki/Highlife)).
- **Grid (clave placement derived from the sourced 3-2 relationship; the other lines are convention):**
  ```
  Bell   X . . X | . . X . | . . X . X . . .   (3-2 son clave)
  Gtr1   X . x X | . x X . | x . X . X x . x   (arpeggio; accents land on clave hits)
  Gtr2   . x . . | x . . x | . x . x . . x .   (fills the gaps; thirds/sixths)
  Kick   X . . . | . . X . | X . . . | . . X .
  Snare  . . . . | X . . . | . . . . | X . . .
  Bass   X . . X | . . X . | X . . . | X . . .   (follows clave; root-5th)
  ```
- **Tempo:** about 100–135 BPM (convention).
- **Harmony (convention):** major. I–IV–V–I, I–V–I and I–IV–I–V in 1–2 bar cycles (in G: G–C–D–G). Guitar lines in parallel 3rds/6ths. Harmonic rhythm 1 chord per bar.

#### 1.14 Jùjú (Lagos, Yoruba; 1920s → 1970s–80s peak)
- **Identity:** early ensembles were trios: a singer on banjo, tambourine and sèkèrè.
  - **Talking drums** entered in 1948.
  - After WWII came electric guitars, synthesizers, **pedal steel guitar**, sometimes saxophones, plus thumb piano, conga-type drums and Hawaiian guitar.
  - It is played at àríyá celebrations (weddings, naming ceremonies, etc.) ([Wikipedia: Jùjú music](https://en.wikipedia.org/wiki/J%C3%B9j%C3%BA_music)).
  - Key artists: King Sunny Adé, Ebenezer Obey, I.K. Dairo; Tunde King (early) ([Wikipedia: Jùjú](https://en.wikipedia.org/wiki/J%C3%B9j%C3%BA_music) for KSA and Tunde King).
  - Reference: King Sunny Adé *Juju Music* (1982), "Ja Funmi".
  - **By ear:** a gentle mid-tempo groove. A talking drum "speaks" phrases, pedal steel slides and swoops, several clean guitars interlock, praise-song vocal leader with chorus, long medleys.
- **Tempo:** about 95–120 BPM (convention). Harmony: major, I–IV–V, mostly 1–2 chords (convention).
- **FL:** pitch-bend a talking-drum sample with a short pitch envelope per hit (Fruity Slicer / Sampler pitch envelope), and slide a pedal steel or lap steel (convention).

#### 1.15 Congolese rumba and soukous (Kinshasa/Brazzaville, 1940s → 1960s–90s)
- **Identity:** Franco (TPOK Jazz) turned the **sebene** from a short instrumental bridge into the **central element** of Congolese popular music. His fast *rumba odemba* style is called rougher, more repetitive and hip-moving ([Wikipedia: Soukous](https://en.wikipedia.org/wiki/Soukous); [Wikipedia: Congolese rumba](https://en.wikipedia.org/wiki/Congolese_rumba)).
  - Origins of soukous are disputed. Some credit Brazzaville's Jacques Kimbembe and the Super Band (1964, later Orchestre Sinza Kotoko) ([Wikipedia: Soukous](https://en.wikipedia.org/wiki/Soukous)).
  - **Mi-solo guitar** (pioneered by Faugus Izeidi) sits between lead and rhythm. Franco's mi-solo used arpeggios and fingerpicking. Docteur Nico's "fiesta" style drew on Baluba melodies ([Wikipedia: Congolese rumba](https://en.wikipedia.org/wiki/Congolese_rumba)).
  - Nigerian listeners favoured the faster, improvisational second-half sebene over the slower "A" sides. The Verckys stable and the **cavacha** rhythm are named ([Wikipedia: Soukous](https://en.wikipedia.org/wiki/Soukous)).
  - Reference tracks: Franco & TPOK Jazz "Mario"; Tabu Ley Rochereau; Kanda Bongo Man "Isambe"; Diblo Dibala/Loketo; Papa Wemba; Koffi Olomide; Fally Ipupa (unsourced except Franco and Loketo).
  - **By ear:** two-part songs. A sweet, slower vocal rumba section is followed by a fast, euphoric sebene of looping high-register guitar lines, a driving snare/hi-hat "cavacha" and animateur shouts.
- **Tempo:** rumba section about 100–120, sebene about 125–160 BPM (convention).
- **Harmony (convention):** major. I–IV–V and I–V–IV–V vamps (in E: E–A–B). Guitar lines in 3rds, high on the neck.
- **Rhythm (convention):**
  ```
  SEBENE / CAVACHA
  Kick   X . . . | X . . . | X . . . | X . . .
  Snare  x x X x | x x X x | x x X x | x x X x   (cavacha: driving 16ths on snare/closed hat)
  LeadGtr high looping 16th arpeggio (2-bar cell), clean + light chorus
  MiSolo  offbeat arpeggios in middle register
  Bass   X . . X | . . X . | X . . X | . . X .
  ```
- **Form:** about 6–10 min. Vocal rumba (A) → break → sebene (B), with dance-command shouts. Modern ndombolo is a later dance form (convention).

#### 1.16 Mbalax (Senegal/Gambia, 1970s →)
- **Identity:** urban dance music of Senegal, Mauritania and the Gambia, rooted in **polyrhythmic Wolof sabar drumming**.
  - From the 1970s it fused with US soul, Latin, jazz and rock. Instruments: sabar, **tama** (talking drum), balafon, riti, plus guitar, keys, horns and synth ([Wikipedia: Mbalax](https://en.wikipedia.org/wiki/Mbalax)).
  - Youssou N'Dour is the emblematic artist (the page pictures his talking-drum player) ([Wikipedia: Mbalax](https://en.wikipedia.org/wiki/Mbalax)).
  - Reference tracks: Youssou N'Dour "Immigrés", "Set"; Étoile de Dakar; Thione Seck (unsourced).
  - **By ear:** cracking, high, rapid sabar and tama phrases cut across a pop-soul band. Strong accents fall "against" the 4/4 and the vocals are high and melismatic.
- **Tempo:** about 110–140 BPM; the sabar phrases imply 12/8 against 4/4 (convention).
- **FL:** layer sabar one-shots (slap, open, rim) in 16th and triplet phrases with heavy velocity variation. Program tama with pitch slides (convention).

#### 1.17 Gqom (Durban, early 2010s →)
- **Identity (all sourced from [Orphiq: What is gqom](https://orphiq.com/resources/what-is-gqom)):**
  - minimal, raw, bass-heavy Durban dance music of the early 2010s
  - **broken kick patterns, not four-on-the-floor**, with tom rolls, chanted vocal fragments and long repetition
  - the name is Zulu onomatopoeia for a hitting drum
  - landmarks: Rudeboyz EP (Goon Club Allstars, 2015); *Gqom Oh! The Sound of Durban Vol. 1* (2016); Babes Wodumo ft. Mampintsha "Wololo" (2016, prod. Distruction Boyz); DJ Lag "Ice Drop" (2016; DJ Lag is billed "King of Gqom"); Distruction Boyz *Gqom Is the Future* (2017, gold)
  - afro-house is listed as gqom's parent style ([Wikipedia: Afro house](https://en.wikipedia.org/wiki/Afro_house))
- **Tempo:** commonly **120–130 BPM**, but tempo won't identify it. The kick pattern is the tell ([Orphiq](https://orphiq.com/resources/what-is-gqom)).
- **Named kick families (sourced, [Orphiq](https://orphiq.com/resources/what-is-gqom)):**
  - broken/two-step: irregular kicks, the raw traditional style
  - three-step: a broken groove organised around three kick hits (not triple meter); distinct from the newer "3-Step" genre
  - sgubhu/four-step: a steady four, closer to house
  - taxi kick: heavily distorted kick plus crashes and triplets (TLC Fam, Newlands West, late 2010s–early 2020s)
  - uThayela: a bass-heavy broken beat for clubs (Unticipated Soundz; DJ Lag's *Uhuru* EP)
- **vs amapiano (sourced):** gqom has no log drum. Its low end is kick + sub and the interest is in placement. It is darker, harder and more hypnotic ([Orphiq](https://orphiq.com/resources/what-is-gqom)).
- **Grids (placement families sourced; exact steps are convention):**
  ```
  BROKEN (two-step)
  Kick   X . . . | . . X . | . . . . | . . X .
  Tom    . . . . | . . . . | . x x x | x . . .   (rolls, pitched low)
  Clap   . . . . | X . . . | . . . . | . . . .   (sparse)
  Hat    . . x . | . . x . | . . x . | . . x .

  THREE-STEP
  Kick   X . . X | . . X . | . . . . | . . . .
  Perc   . . . . | . . . . | X . x . | X . x .

  TAXI KICK: kick distorted, crash on beat 1 of each 2 bars, triplet tom fills at phrase ends
  ```
- **Harmony:** minimal minor stabs or a single dark chord, a vocal chant sample, no log drum (sourced mood; voicing is convention).

#### 1.18 Kwaito (Soweto/Johannesburg, early 1990s)
- **Identity:** "house music with the tempo pulled down" from early-1990s Soweto. It sits around **100–110 BPM** vs 120–130 for house, and ranges disagree at the edges ([Orphiq: What is kwaito, via search summary](https://orphiq.com/resources/what-is-kwaito)). Kwaito is a listed stylistic origin of afro-house ([Wikipedia: Afro house](https://en.wikipedia.org/wiki/Afro_house)).
  - Key artists: Arthur Mafokate, Boom Shaka, TKZee, Mandoza ("Nkalakatha", 2000), Trompies (unsourced, well known).
  - **By ear:** slow, bouncy four-on-the-floor with a fat synth bassline. Chanted or half-rapped township-slang vocals, a party/call-response vibe, simple keys.
- **Rhythm (convention):**
  ```
  Kick   X . . . | X . . . | X . . . | X . . .
  Clap   . . . . | X . . . | . . . . | X . . .
  Hat    . . o . | . . o . | . . o . | . . o .
  Shaker x x x x ... (16ths)
  Bass   X . . X | . . X . | . X . . | X . X .   (fat, syncopated, synth)
  ```
- **Harmony:** minor or major 2–4 chord loops, organ/piano stabs, deep-house influence (convention).

#### 1.19 Kuduro (Luanda, late 1980s–1990s →)
- **Identity:** Tony Amado, the self-proclaimed creator, says the dance came first. It was inspired by Jean-Claude Van Damme's drunk dance in *Kickboxer* (1989) ([Wikipedia: Kuduro](https://en.wikipedia.org/wiki/Kuduro)).
  - Vivian Host notes elements in common with punk, tribal house and Daft Punk. DJ Riot (Buraka Som Sistema) stresses that it is kids making electronic dance music, not folk ([Wikipedia: Kuduro](https://en.wikipedia.org/wiki/Kuduro)).
  - Kuduro also helped popularise house in Angola ([Wikipedia: Afro house](https://en.wikipedia.org/wiki/Afro_house)).
  - Reference: Buraka Som Sistema "Kalemba (Wegue Wegue)"; Os Lambas; Sebem; Titica (unsourced except Buraka).
  - **By ear:** fast, frantic and percussive, with a pounding syncopated kick, sirens/whistles, shouted vocals and a cheap, aggressive synth palette.
- **Tempo:** about **140–150 BPM** with pounding syncopated kicks, off-beat claps, chopped shouts, sirens and whistle FX (search-engine summary; the originating page was unclear, so treat as **weakly sourced**).
- **Rhythm (convention):**
  ```
  Kick   X . . X | . . X . | X . . X | . . X .   (tresillo-driven, pounding)
  Clap   . . . . | X . . . | . . . . | X . . .
  Hat    . . x . | . . x . | . . x . | . . x .
  Perc   16th congas/toms; siren/whistle stabs at 4-bar ends
  ```

#### 1.20 Afro-house: roots only (SA, 1980s–2000s)
- **Origins:** a house subgenre developed mainly in South Africa from kwaito, house, mbaqanga, deep, tribal and soulful house. Typical instruments: vocals, sax, piano, drum kit, synth, flute, sequencer. Derivatives: gqom; subgenre afro tech ([Wikipedia: Afro house](https://en.wikipedia.org/wiki/Afro_house)).
- The House Afrika label was founded in 1994 by Vinny Da Vinci, Tim White and DJ Strat3gy ([Wikipedia: Afro house](https://en.wikipedia.org/wiki/Afro_house)).
- Card details: see the earlier house notes. Roots-era differentiator: live-sounding percussion (congas, shakers), Zulu/Sotho vocal chants and mbaqanga-tinged guitar/keys at about 118–124 BPM (convention).

#### 1.21 Bongo flava (Dar es Salaam, 1990s →)
- **Identity:** the nickname for Tanzanian pop. It developed in the 1990s from US hip hop plus taarab and dansi. Origins also include dancehall. Subgenre: **singeli**; related: zenji flava ([Wikipedia: Bongo Flava](https://en.wikipedia.org/wiki/Bongo_Flava)).
  - In the 2020s "bongopiano" fused bongo flava with amapiano (Diamond Platnumz, Marioo, Harmonize, Nandy, Jux, Mbosso, Zuchu) ([Wikipedia: Amapiano](https://en.wikipedia.org/wiki/Amapiano)).
  - Reference tracks: Diamond Platnumz "Number One", "Waah!" (with Koffi Olomide), Zuchu "Sukari" (unsourced titles).
  - **By ear:** Swahili-language R&B/afro-pop with melismatic, taarab-inflected vocal runs. Rhythms borrow from dancehall, afrobeats, Congolese sebene guitars and, recently, log drums.
- **Tempo:** about 95–115 BPM. Singeli is extremely fast, about 200–300 BPM (convention; no source found).
- **FL:** start from an afrobeats or dancehall template (earlier notes). Add taarab-style melisma (Arabic-tinged, harmonic-minor/Phrygian-dominant turns in the vocal or a qanun/violin-like synth) and sebene-style guitar licks (convention).

#### 1.22 Ethio-jazz / Ethio-groove (Addis Ababa, 1950s–1970s "Swinging Addis" → revival)
- **Identity:** blends traditional Ethiopian music with jazz. Its **pentatonic Amharic melodies** sit on 12-tone Western harmony and instrumentation: saxophone, **vibraphone**, drums, bass. Origins: traditional Ethiopian music, Armenian jazz and afrofunk, from 1950s Addis Ababa ([Wikipedia: Ethio-jazz](https://en.wikipedia.org/wiki/Ethio-jazz)).
  - Key artists: Mulatu Astatke ("father of Ethio-jazz"), Mahmoud Ahmed ("King of Tizita"), Bezawork Asfaw ("Queen of Tizita"), Hailu Mergia, Aster Aweke, Teddy Afro ([Chromatone](https://chromatone.center/theory/scales/ethiopian/) for the tizita artists). The Walias Band and the *Éthiopiques* reissue series (Francis Falceto) are unsourced here.
  - Reference tracks: Mulatu Astatke "Yègellé Tezeta", "Tezeta", "Yekermo Sew"; Mahmoud Ahmed "Ere Mela Mela"; Hailu Mergia "Tche Belew".
  - **By ear:** minor-ish pentatonic melodies with wide gaps, a hypnotic 6/8 or 4/4 groove, vibraphone/organ/wah guitar, brooding horn unisons and vocals full of trills and melisma.
- **Modes:** see Section 2 (qenet).
- **Tempo & meter (convention):** many grooves are 6/8 or 12/8 ("chik-chika" style) at about 100–130 dotted-quarter-feel. Others are slow 4/4 ballads (tizita) at 60–80.
- **Rhythm, 12/8 (convention; steps are 8th notes, 1 = beat 1, 4 = beat 2, 7 = beat 3, 10 = beat 4):**
  ```
  Kick   X . . | . . x | X . . | . . x
  Snare  . . . | X . . | . . . | X . .
  Hat    x x x | x x x | x x x | x x x   (accent 1st of each triplet)
  Bass   X . x | . X . | X . x | . X .   (pentatonic riff in the qenet)
  ```
- **Harmony:** one or two chord minor vamps (i–iv or i–bVI) under a pentatonic melody. Chords are often implied rather than stated (convention).

#### 1.23 Afroswing (UK, mid-2010s →)
- **Identity:** a British genre derived from afrobeats, dancehall and hip-hop ([Wikipedia: Afroswing](https://en.wikipedia.org/wiki/Afroswing)).
  - Foundations: UK funky (Donae'o); Sneakbo "Touch Ah Button" (2010); Timbo & Mover "Ringtone" (2014) ([Wikipedia: Afroswing](https://en.wikipedia.org/wiki/Afroswing)).
  - Key producers: Jae5, Blairy Hendrix, Joshua Beatz; key rapper: J Hus ([Wikipedia: Afroswing](https://en.wikipedia.org/wiki/Afroswing)).
  - Reference tracks: J Hus "Did You See" (2017), "Friendly"; Not3s "Aladdin"; Kojo Funds "Dun Talkin'"; Yxng Bane "Rihanna" (unsourced titles).
  - **By ear:** a London-accented rap/sing hybrid over a bouncy afro-dancehall groove with the snare on beat 3, warm major-7 or dark minor chords, and a melodic, catchy flow.
- **Defining rules (sourced):**
  - Afroswing is "largely defined by its melody rather than a specific tempo" ([Wikipedia: Afroswing](https://en.wikipedia.org/wiki/Afroswing)).
  - Steel Banglez named happy or dark chords plus the drum pattern as the key elements: the **snare lands on the third beat** (from afrobeats) rather than the fourth as in hip-hop ([Wikipedia: Afroswing](https://en.wikipedia.org/wiki/Afroswing)).
  - Martin Connor describes a recurring **three-note grouping inside 4/4** with Jamaican-derived rhythm plus hip-hop kick/snare ([Wikipedia: Afroswing](https://en.wikipedia.org/wiki/Afroswing)).
- **Tempo:** about 95–110 BPM (convention).
- **Rhythm (snare-on-3 sourced; the 3+3+2 placement is derived from the three-note description; the rest is convention):**
  ```
  Kick   X . . X | . . X . | . . . . | X . . .
  Snare  . . . . | . . . . | X . . . | . . . .   (beat 3)
  Rim    . . . X | . . X . | . . . X | . . X .   (3+3+2 feel)
  Hat    x . x x | x . x . | x . x x | x . x .
  Shaker 16ths; Bass/808 short, follows kick
  ```

#### 1.24 Alté (Lagos, about 2014 →)
- **Identity:** a left-field Nigerian movement. It fuses afrobeats, rap, R&B, soul, dancehall and alternative styles ([Wikipedia: Alté](https://en.wikipedia.org/wiki/Alt%C3%A9)).
  - The term was coined by DRB LasGidi and first heard on BOJ's "Paper" (2014). TeeZee describes it as Nigerian lingo for "alternative", meaning freedom of expression; it broke into the mainstream around 2016 ([Wikipedia: Alté](https://en.wikipedia.org/wiki/Alt%C3%A9)).
  - Artists: Cruel Santino, Odunsi (The Engine), Zamir, Tems, Lady Donli, Nonso Amadi, Tay Iwar, Amaarae ([Wikipedia: Alté](https://en.wikipedia.org/wiki/Alt%C3%A9)).
  - Visual culture: early-2000s fashion, music videos inspired by 1990s Nollywood horror ([Wikipedia: Alté](https://en.wikipedia.org/wiki/Alt%C3%A9)).
  - Reference tracks: Cruel Santino "Rapid Fire"; Odunsi "Alté Cruise"; Tems "Try Me"; Amaarae "SAD GIRLZ LUV MONEY" (unsourced titles).
  - **By ear:** afrobeats-adjacent rhythms but hazy, lo-fi, R&B/psychedelic textures, unusual chords, understated or whispery vocals, genre-hopping.
- **Tempo:** about 80–110 BPM (convention).
- **Production (convention):** detuned or chorused keys, tape saturation, sparse afro percussion, filtered drums, maj9/min11 voicings. Deliberately "imperfect" mixes.

### Inferences
- **Fastest ear tests (derived from the sourced definitions above):**
  - kick on 3 only → one drop
  - kick on every beat + rim on 3 → rockers
  - kick doubled → steppers
  - kick syncopated + synth bass hook + no skank → dancehall
  - four-on-the-floor + iron + over 130 BPM → power soca
  - irregular kick at 120–130 with no log drum → gqom
  - log drum present → amapiano (not covered here)
  - snare on beat 3 at about 100 BPM with UK rap → afroswing
  - two-part song with a fast high-guitar second half → soukous
- Many Caribbean/African grooves here share the **tresillo / 3+3+2 cell**: dembow, Diwali-style claps, zouk-love rims, kuduro kicks, afroswing rims and the highlife 3-2 clave. The genre identity comes from tempo, timbre and what plays the cell (derived from sourced clave/bell and afroswing findings).
- For FL Studio, the most common "fake" giveaways across these styles are:
  1. quantised, velocity-flat percussion
  2. long-sustained chord pads where the style uses short chops
  3. a busy kick where the genre is defined by kick absence (one drop) or kick irregularity (gqom)
  4. wrong swing: reggae hats need shuffle; soca/kuduro are straight

  (derived from the wayneandwax humanisation caveat and the Orphiq/Wikipedia rhythm definitions)

### Gaps
- No note-level published transcriptions were found for soca, zouk, kompa, bouyon, mbalax, kuduro or the Tony Allen patterns (the Rolling Stone clip is video only). Those grids are conventions and should be checked against the reference tracks.
- BPM figures for ska, rocksteady, lovers rock, calypso, kompa, bouyon, highlife, juju, soukous, mbalax, bongo flava, singeli, afroswing, alté and Ethio-jazz are conventions; I found no authoritative source.
- The kuduro 140–150 BPM figure came from a search-engine summary with an unclear originating page.
- 2025–2026 current state: sources fetched date from 2020–Sept 2026 (Orphiq articles dated Sep 2026), but I found no specific 2025–26 trend reporting for dancehall, soca or gqom beyond these. Trend status (e.g. the gqom → 3-step evolution, modern dancehall's trap influence) is only partly sourced.
- The full Ska Wikipedia page failed to render; only its infobox (origins/derivatives) was captured.

---

## 2. Bass, harmony and melodic conventions (reggae bass as lead, highlife lines, Ethiopian qenet)

### Takeaway
- **Reggae bass:** a melodic lead instrument that often rests on beat 1. It plays the hook in one drop/dub, and dancehall replaces it with a short synth-bass hook.
- **Highlife and soukous:** major-key I–IV–V guitar lines built in 3rds/6ths. The highlife arpeggio follows the 3-2 clave.
- **Ethio-jazz:** built on the four qenet pentatonic modes (tizita, bati, ambassel, anchihoye). They are untempered on traditional instruments, and sources disagree on exact spellings for anchihoye and the "minor" variants.

### Cited Findings
- Dancehall bass is a short, repeated synth figure, often the track's most memorable melodic idea, with minimal harmony ([Orphiq: dancehall](https://orphiq.com/resources/what-is-dancehall)).
- Reggae typically uses two guitars (rhythm + lead), drums, congas and keyboards. The skank is the staccato offbeat chord on guitar/piano ([Wikipedia: Reggae](https://en.wikipedia.org/wiki/Reggae)).
- Reggae is described as a groove around the offbeat skank, a relaxed one drop and a **deep and melodic bass line** ([violetrecording, via search summary](https://violetrecording.com/how-to-make-reggae-music/)).
- The highlife guitar arpeggio follows a 3-2 clave guajeo, and highlife guitar uses the two-finger dagomba picking style ([Wikipedia: Highlife](https://en.wikipedia.org/wiki/Highlife)).
- Congolese guitar roles split into lead, mi-solo (arpeggios/fingerpicking) and rhythm ([Wikipedia: Congolese rumba](https://en.wikipedia.org/wiki/Congolese_rumba)).
- **Ethiopian qenet (modes):**
  - The four main modes are **tizita (tezeta), bati, ambassel and anchihoye**, plus variants: tizita minor, bati major and bati minor.
  - The modes are pentatonic with "characteristically long intervals" between some notes.
  - They are untempered on traditional instruments but played tempered on Western instruments ([Wikipedia: Music of Ethiopia](https://en.wikipedia.org/wiki/Music_of_Ethiopia); [Wikipedia: Qenet](https://en.wikipedia.org/wiki/Qenet)).
  - A qenet is a set of intervals defining both the mode of a piece and the tuning of the instrument ([Wikipedia: Qenet](https://en.wikipedia.org/wiki/Qenet), citing Weisser & Falceto 2013).
- **Note spellings from C (sources disagree):**

  | Qenet | Chromatone | Other source |
  |---|---|---|
  | Tizita major | C D E G A (= major pentatonic; intervals M2-M2-m3-M2-m3) | — |
  | Tizita minor | C D Eb G A | — |
  | Bati major | C D F G A | — |
  | Bati minor | C Db F G A | — |
  | Ambassel | C D E G Ab ("major"), C D Eb G Ab ("minor") | **C Db F G Ab** = Phrygian subset 1-b2-4-5-b6, a mode of Hirajoshi, used in Gondar/Wollo ([Wikipedia: Ambassel scale](https://en.wikipedia.org/wiki/Ambassel_scale)) |
  | Anchihoye | C D Eb G Ab ("traditional") | **C Db F F# A** (diminished fifth from the root; Orthodox church and devotional use) ([guitarcomposerstoolbox](https://guitarcomposerstoolbox.com/guitar-scales/c-anchihoye/)) |

  - Chromatone source: [Chromatone: Ethiopian kinits](https://chromatone.center/theory/scales/ethiopian/).
  - **Conflict:** Chromatone's ambassel/anchihoye spellings disagree with Wikipedia and guitarcomposerstoolbox. Chromatone also lists a fifth kinit, "Yematibela".
  - Chromatone notes that qenet are defined as much by contour, motifs, ornamentation and emotion as by intervals ([Chromatone](https://chromatone.center/theory/scales/ethiopian/)).
- Tizita means memory/nostalgia (compared to *saudade*) and is used for slow, emotive songs ([Chromatone](https://chromatone.center/theory/scales/ethiopian/)).

### Inferences
- **Recommended qenet set for a composer-AI** (derived; prefers the Wikipedia/independent spellings where they conflict):

  | Mode | Notes from C | Character / use |
  |---|---|---|
  | Tizita major | C D E G A | nostalgic ballads |
  | Tizita minor | C D Eb G Ab | widely circulated; Chromatone gives C D Eb G A, so flag it |
  | Bati major | C E F G B | widely circulated; Chromatone gives C D F G A, so flag it |
  | Ambassel | C Db F G Ab | brooding Mulatu-style minor grooves |
  | Anchihoye | C Db F F# A | eerie and tense |

  Prefer ambassel or tizita minor for the "Yègellé Tezeta / Ethiopiques" sound. Keep harmony to one chord (e.g. Cm or C5) so the pentatonic gaps carry the colour (derived).
- **Reggae bass recipe (derived from sourced "melodic bass" + one-drop placement):**
  - 1–2 bar riffs mostly on chord tones plus passing tones
  - rest on step 1, land with the drop on step 9
  - register around E1–E2 with round, filtered tone (low-pass about 800 Hz–1.2 kHz, convention)
  - bass is the loudest musical element in dub
- **Highlife/soukous lines (derived):** harmonise in parallel diatonic 3rds/6ths over I–IV–V, place accents on clave hits (highlife) or loop 2-bar arpeggio cells high on the neck (sebene).

### Gaps
- No authoritative musicological table of all qenet note spellings was fetched. Weisser & Falceto (2013) is the cited acoustic study but was not read. The tizita minor and bati major spellings in the Inferences table are partly from general knowledge and disagree with Chromatone.
- No sourced chord-progression statistics for these genres. All Roman-numeral progressions in the cards are conventions.

---

## 3. Instruments and production techniques (dub delays/spring reverb, riddim versioning, DAW emulation)

### Takeaway
Dub is mixing-as-performance: mute instruments in and out, send snare/skank/vocal hits to tempo-synced tape delay and spring reverb, high-pass the effect returns, and let the bass carry the track. Riddim culture means one instrumental is reused under many vocals and versions. The African band styles are emulated by layering role-specific parts (talking drum with pitch envelopes, pedal steel slides, clean chorused guitars, unison horns) rather than by heavy processing.

### Cited Findings
- **Console as instrument:** King Tubby and Lee Perry treated the mixing console as an instrument. The Roland Space Echo is named among the core tools ([Wikipedia: Dub music](https://en.wikipedia.org/wiki/Dub_music)). Attack Magazine names spring reverb, tape delay and analogue effects as the core of the King Tubby / Prince Jammy / Lee Perry techniques ([Attack Magazine: Dub-style drum processing](https://www.attackmagazine.com/technique/tutorials/dub-style-drum-processing-for-character-and-groove/)).
- **Attack's dub-drum chain:** spring reverb on the snare via Surreal Machines Modnetic.
  - Echo section off, "501 Spring" reverb.
  - Phaser modulation at about 30% rate and 10% amount, stereo spread.
  - Bass down and treble up on the return, noise added for dirt, input driven for saturation, mix about 50/50 ([Attack Magazine](https://www.attackmagazine.com/technique/tutorials/dub-style-drum-processing-for-character-and-groove/)).
- **Delay throws and spring sends (Attack practical tips, via search summary):**
  - Hit the delay aux on snares at the end of a drum phrase while muting the drum group, which drops the mix to bass and guitars ("the essence of doing dub").
  - Put a spring aux on the drums with the bottom end high-passed out.
  - Automate a filter on the spring return.
  - Subtraction matters as much as effects ([Attack Magazine, via search summary](https://attackmagazine.com/?p=95750)).
- Lee Perry ran percussive sounds through an early Grampian spring reverb ([zZounds blog, via search summary](https://blog.zzounds.com/2018/06/22/beat-techniques-dub-production/)).
- **Version culture:** producers made multiple versions of one session for economic reasons. The B-side "version" was for experimentation and for DJs to toast over. 1970s dub LPs collected riddims or dubbed whole vocal LPs ([Wikipedia: Dub music](https://en.wikipedia.org/wiki/Dub_music)). Rising dub and toasting demand led producers to sell rhythm tracks to one another ([Wikipedia: Dub music](https://en.wikipedia.org/wiki/Dub_music)).
- Riddim types are classic, ragga and digital (see 1.6). Kumina and Burru riddims draw on African-Jamaican religious drumming ([Wikipedia: Riddim](https://en.wikipedia.org/wiki/Riddim)).
- Programmed reggae will lack live dynamics unless humanised. Producers have programmed roots riddims since the 1980s ([wayneandwax](https://www.wayneandwax.com/org/lessons/roots-riddim-tutorial.html)).
- Augustus Pablo's melodica is a signature dub lead timbre ([Wikipedia: Dub music](https://en.wikipedia.org/wiki/Dub_music)).
- Jùjú instrumentation includes talking drum (from 1948), pedal steel and Hawaiian guitar ([Wikipedia: Jùjú music](https://en.wikipedia.org/wiki/J%C3%B9j%C3%BA_music)). Mbalax uses sabar and tama ([Wikipedia: Mbalax](https://en.wikipedia.org/wiki/Mbalax)). Bouyon uses lapo kabwit, scraper, accordion and keyboards ([Wikipedia: Bouyon music](https://en.wikipedia.org/wiki/Bouyon_music)).
- Gqom's taxi kick is heavily distorted, with crashes and triplets, designed to be heard from a moving minibus taxi ([Orphiq: gqom](https://orphiq.com/resources/what-is-gqom)).

### Inferences
- **FL Studio dub rig** (derived from the sourced techniques; plugin choices are convention):
  1. **Mixer layout.** Route drums, bass, skank, organ, horns/melodica and vocal to separate inserts.
  2. **Send A: tape delay.** Fruity Delay 3 at 3/16 or 1/4 tempo-synced, feedback 50–70%. Put a low-cut of about 300 Hz and a high-cut of 3–5 kHz in the feedback path, and add Fruity Blood Overdrive or Fruity Fast Dist lightly after it for tape grit.
  3. **Send B: spring.** Fruity Convolver with a spring impulse response (or a spring-reverb plugin), high-passed about 400 Hz, slightly overdriven.
  4. **Performance.** Automate send levels as one-shot "throws" on the last snare/skank of a phrase. Automate insert mutes (record live with a controller) so instruments drop out for 2–8 bars. Sweep a Fruity Filter high-pass on the full mix into a drop.
  5. **Feedback swell.** Briefly push delay feedback above 90% for runaway echo, then cut it.
  6. **Bass.** Keep it dry and mono, low-passed and loud. It is the one element never effected.
- **Riddim workflow** (derived): build one 8- or 16-bar riddim pattern, then make multiple arrangement versions: vocal mix, "version" (instrumental), dub (effected), and a deejay cut with the bass up and the skank down. This mirrors the sourced version culture.
- **Emulation shortcuts** (convention):
  - Space Echo → Fruity Delay 3 with modulation and saturation, or a third-party RE-201 emulation.
  - Melodica → FL Keys/Sytrus reed patch with breath vibrato.
  - Organ bubble → FL Keys organ or a B3 emulation, staccato.
  - Talking drum → Sampler pitch envelope per note, or Fruity Slicer with pitch bend.
  - Pedal steel → slide-enabled guitar library, or Sytrus with portamento.
  - Steelpan → FL Keys/FPC steelpan samples or a Sytrus FM bell.
  - Iron → cowbell or brake-drum one-shots with a 16th gallop.
  - Sabar → Wolof sabar sample packs.
- **Mix character by era** (convention):
  - 1960s ska/rocksteady: mono-ish, mid-forward, room reverb.
  - Roots/dub: heavy low end, spring/tape effects, bass loudest.
  - Digital dancehall: dry, punchy, sparse.
  - Modern soca/dancehall/afroswing: loud (about −8 to −6 LUFS integrated club/streaming masters), polished.
  - 1970s Afrobeat/highlife/juju: live-band bleed, warm tape, moderate dynamics. Keep it less loud (about −12 to −10 LUFS) to stay authentic.
  - Gqom/kuduro: raw, distorted kicks, minimal processing.

### Gaps
- No sourced loudness (LUFS) measurements for any of these genres; the LUFS targets above are convention.
- The MusicRadar one-drop tutorial and the Attack "creating dub delays with standard plugins" article were found but not fully read. Their exact settings (delay times, feedback values) are not captured here beyond the search summaries.
- I found no source on how modern (2025–26) dancehall/soca producers build riddims in DAWs (e.g. FL Studio prevalence). Treat workflow claims as derived.
