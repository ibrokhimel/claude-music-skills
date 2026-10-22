# Turning Every World Genre Into Programmable Recipes

Every genre in this survey can be written as the same short parameter vector, and a composing skill can set those values directly. The survey covers about 150 styles across rock, metal, jazz and blues, soul/funk/gospel/disco, country and folk, Latin, Caribbean, African, East Asian, South Asian, Middle Eastern, classical, film, game and experimental music, plus roughly 40 hip hop, electronic, pop and cinematic styles carded in the earlier research. The vector has nine fields: tempo band and felt tempo; the governing time-line (backbeat, four-on-the-floor, half-time, a clave, the 3+3+2 tresillo, a dum-tek cycle or a tala); subdivision and swing; the bass's job; chord vocabulary; one or two signature timbres; vocal delivery; form in bar counts; and production aesthetic. The time-line cell plus the bass placement decide a genre more than anything else. They are the trait most reliably passed down family trees, and the Latin research states the rule bluntly: get those two right at the correct tempo and the genre reads, get them wrong and correct instruments will not save it. The rest of the vector separates close relatives: swing amount (disco about 50%, funk 54–58%, new jack swing 62–66%, blues shuffle 66%), guitar gain and tuning in rock and metal, scale and microtuning in maqam music, and harmonic density from one-chord funk to gospel passing chords. Evidence quality is uneven. Genre identities, histories and the defining rhythms are well sourced: one drop/rockers/steppers, the d-beat, the blast-beat family, the clave family, Earl Young's disco hi-hat, Arabic iqa'at, Hindustani talas and gqom kick families. Most BPM ranges, velocities, swing percentages and bar counts are practitioner convention and are labelled that way below. Machine-learning research adds that even trained classifiers do not really "hear" genre, so the skill should identify styles from several cues and report a ranked guess. Production has also moved fast. US R&B/hip-hop is still the largest genre but losing share, while rock, Latin, country and Christian music grew in 2025. Brazilian funk was Spotify's fastest-growing genre worldwide and afro house led creator downloads. Fully AI-generated tracks passed half of Deezer's daily uploads in 2026. Fusion is now the default, and it works when one genre carries the drums and bass and the other only adds colour.

## Genre is a nine-part musical fingerprint wearing a social label

### The social half is real, and machines confirm the musical half is slippery

A genre is partly a social institution, not just a sound. Jennifer Lena and Richard Peterson's study of US popular music identified four recurring genre forms (**avant-garde, scene-based, industry-based and traditionalist**), and Lena's later book, which draws on about 60 styles from rap and bluegrass to death metal and South Texas polka, adds a fifth outside the US, the **government-purposed** genre ([Vanderbilt IR](https://ir.vanderbilt.edu/items/e115978c-c9b3-449c-a607-3b8510941b41); [Princeton UP](https://press.princeton.edu/node/14985)). Chart bodies police those borders. In March 2019 Billboard removed Lil Nas X's "Old Town Road" (country imagery over a trap beat) from Hot Country Songs because it supposedly lacked enough elements of today's country music, even though it had debuted at No. 19 there and was the first song to chart on the Hot 100, Hot Country and Hot R&B/Hip-Hop at once ([XXL](https://www.xxlmag.com/lil-nas-x-old-town-road-removed-billboard-country-chart/); [Okayplayer](https://www.okayplayer.com/news/lil-nas-x-old-town-road-billboard-hot-country-songs-chart.html)). A fusion can be a hit and still be shut out of a genre's institutions.

Music-information-retrieval research shows why a skill should not trust any single cue. GTZAN, the standard genre benchmark of 1,000 thirty-second excerpts in 10 genres used in at least 100 published works, contains **50 exact repetitions, about 93 mislabelings and heavy artist repetition** (over a third of its "reggae" is Bob Marley, and its "blues" has only 9 artists across 100 excerpts). Bob Sturm estimated a fault-limited ceiling of about **94.5% accuracy**, so higher reported scores are suspect ([Sturm, arXiv 1306.1461](https://arxiv.org/abs/1306.1461)). He also showed that state-of-the-art recognisers can be fooled by changes a human would not notice, a "Clever Hans" effect, and 81% of surveyed papers judged genre systems only by classification accuracy ([QMUL](https://qmul.ac.uk/media/news/2015/se/how-music-listening-programs-can-be-easily-fooled.html); [Sturm, arXiv 1606.03044](https://arxiv.org/abs/1606.03044v1)). Industry taxonomies are inconsistent too ([Pachet & Cazaly](https://www.francoispachet.fr/?p=4325)). Spotify's Every Noise at Once map showed 1,742 genres in 2018 ([Spotify for Artists](https://artists.spotify.com/blog/how-spotify-discovers-the-genres-of-tomorrow)). By the time its creator Glenn McDonald was laid off on 4 December 2023, it had placed about a million artists into **6,291 named genres**, including 202 kinds of folk and 230 kinds of hip hop. The site is now a frozen snapshot ([Wikipedia: Every Noise at Once](https://en.wikipedia.org/wiki/Every_Noise_at_Once); [TechCrunch](https://techcrunch.com/2024/02/12/every-noise-shut-down-spotify-layoffs)). Most of those microgenres are listener-and-place clusters rather than musical rules, so "Thai hip hop" can sound like any hip hop. The working definition for the skill is therefore genre = musical fingerprint × scene/place/era/industry label. The skill controls the first factor, and the second decides whether listeners accept the label.

### Nine musical dimensions, ordered by how much they decide genre by ear

The ordering below is synthesis (convention), but each dimension is anchored by sourced examples elsewhere in this report.

| # | Dimension | What the skill sets | Examples that flip genre |
|---|---|---|---|
| 1 | Tempo band and felt tempo | BPM plus half-time/double-time relation | 140 drill felt at 70; DnB 174 felt at 87; bossa quoted 120–140 but counted 60–70 in Brazilian 2/4 |
| 2 | Time-line / kick-snare placement | grid of kick, backbeat or governing cell | backbeat 2 & 4; snare on 3 (half-time, afroswing); kick only on 3 (one drop); four-on-the-floor; dembow 3+3+2; clave; dum-tek iqa' |
| 3 | Subdivision and swing | straight 8ths/16ths, shuffle, triplet grid, per-note offsets | blues shuffle 66%; NJS swung 16th triplets; neo-soul late snare; jazz ride ratio by tempo |
| 4 | Bass job | role, rhythm, register | walking quarters; boogie 1-3-5-6-b7; anticipated tumbao; reggae melodic bass resting on 1; disco broken octaves; 808 glides; drone |
| 5 | Harmony vocabulary | scale/mode, chord types, harmonic rhythm | 12-bar dominant 7ths; ii-V with extensions; one-chord vamp; Mixolydian I-bVII-IV; maqam with half-flats; raga over drone |
| 6 | Signature timbre | one or two identity instruments | pedal steel, banjo roll, log drum, tumbi + dhol, bandoneon, güira, requinto, Rhodes, supersaw |
| 7 | Vocal style | delivery and language | high lonesome tenor, growl, toasting, sonero, melisma, rap flow, crooning |
| 8 | Form | sections and bar counts | 12-bar choruses; AABA 32; head-solos-head; AABB reels; mukhda-antara; A-melo/B-melo/sabi; riff chains; DJ 16-bar blocks |
| 9 | Production aesthetic | room, compression, loudness, effects | dub delays, wall-of-sound reverb, lo-fi black metal hiss, filter-house pump, mono 1960s soul |

### One shared coordinate system and one card schema

All rules below use MIDI numbers, with **C4 = 60, which FL Studio's piano roll labels "C5"**, so FL's octave label is always the scientific octave plus one ([Wikipedia: Scientific pitch notation](https://en.wikipedia.org/wiki/Scientific_pitch_notation)). One 4/4 bar is 16 steps (16th notes), which is one FL Channel Rack bar. Beats 1, 2, 3 and 4 sit on steps 1, 5, 9 and 13; the 8th-note "ands" on 3, 7, 11 and 15. Channel Rack patterns can run from 1 to 512 steps ([Image-Line manual: Channel Rack](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/channelrack.htm)), so 12-step, 14-step (7/8) and 20-step (5/4) patterns are native. Grids use `X` for an accent (velocity about 110–127), `x` for a normal hit (75–105), `g` for a ghost (25–50), `o` for an open hat and `.` for a rest; the velocity bands are convention. Four other grid types appear below. **12-step grids** are 4 beats × 3 triplet steps, used for shuffles, swing, 12/8 and 6/8. **CYCLE16** grids (Cuban and Brazilian styles) put one full two-bar clave cycle on 16 steps of 8th notes; program them in FL at **half the quoted BPM** as one bar. **Dum/Tek/Ka lanes** are used for Arabic and Turkish drums. **Matra grids** are used for Indian talas. Claims carry a link when sourced, "(convention)" when they are practitioner practice the researchers could not tie to a source, and "(derived)" for arithmetic or inference. MPC-style swing is 50% straight to 66% full triplet ([Attack Magazine: Roger Linn](https://www.attackmagazine.com/features/interview/roger-linn-swing-groove-magic-mpc-timing/)). FL's Channel Rack swing works only when both global and channel swing are above zero ([Image-Line manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/channelrack.htm)), and **it swings the even 16ths, not 8ths**. Jazz 8th-note swing therefore has to be written on a triplet piano-roll snap or a 12-step pattern (convention). FL piano-roll slides and portamento work only on native instruments, not VST/AU plugins ([Image-Line manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/chansettings_misc.htm)).

Every genre below is described with the same eleven-field card, which maps one-to-one onto a data schema for the skill.

| Field | Content |
|---|---|
| 1 Identity | origin, era, key artists, 2–4 reference tracks, one-line ear test |
| 2 Tempo & feel | BPM range and default, meter, swing/feel |
| 3 Harmony | scale/mode, progressions in Roman numerals and spelled in a key, harmonic rhythm |
| 4 Melody & vocals | contour, ornaments, delivery |
| 5 Instruments | signature sounds and DAW emulation |
| 6 Rhythm | grids |
| 7 Bass | role and pattern |
| 8 Form | sections with bar counts, length |
| 9 Mix | space, compression, loudness |
| 10 Neighbours | how to tell close relatives apart |
| 11 FL Studio | ordered build steps and "sounds fake" mistakes |

## Seven rhythmic genes explain most family trees

### Sourced lineages run through rhythm more than harmony

Most modern popular music descends from a few African-American and Afro-Caribbean roots (blues, gospel, jazz, Jamaican sound systems) and from disco's DJ culture, and the drum pattern is what survives each mutation. R&B formed in 1940s Black communities from jump blues, swing, gospel and boogie. Billboard's Jerry Wexler coined "rhythm and blues" in 1949 to replace "race music"; R&B fed 1950s rock and roll, "soul" replaced the label in the early 1960s, and late-1980s R&B absorbed hip hop as new jack swing ([Wikipedia: Rhythm and blues](https://en.wikipedia.org/wiki/Rhythm_and_blues)). House grew from Frankie Knuckles re-editing disco at Chicago's Warehouse (1977–82), keeping a repetitive 4/4 kick at **115–130 BPM**, and spawned acid, deep, garage and hip house, with Detroit techno alongside ([Wikipedia: House music](https://en.wikipedia.org/wiki/House_music)). Jungle (early-1990s UK) fused chopped breakbeats at **160–180 BPM** with dub/reggae basslines from sound-system culture, and by 1996–97 it had turned into drum and bass ([Wikipedia: Jungle music](https://en.wikipedia.org/wiki/Jungle_music)). Panamanian reggae en español plus hip hop became Puerto Rican reggaeton. Its backbone is the **dembow** riddim by Steely & Clevie, a kick-snare-timbal 3+3+2 cell that Wikipedia says underlies over 80% of reggaeton ([Wikipedia: Reggaeton](https://en.wikipedia.org/wiki/Reggaeton)). Drill moved from Chicago (2010–12, Young Chop's brass and bells) to Brixton (c. 2013, ~140 BPM with sliding 808s) and then to Brooklyn via Pop Smoke ([Wikipedia: Drill music](https://en.wikipedia.org/wiki/Drill_music)). Baltimore club became Jersey club, which K-pop used in NewJeans' "Ditto" ([Wikipedia: Ditto](https://en.wikipedia.org/wiki/Ditto_(song)); [Splice](https://splice.com/blog/?p=34341)). Kwaito plus deep and soulful house became afro house ([Splice](https://splice.com/blog/?p=34341)), phonk's cowbell plus Brazilian funk became Brazilian phonk, and plugg plus 1990s R&B and gospel harmony became pluggnb ([MIDiA](https://www.midiaresearch.com/blog/jersey-club-in-berlin-behind-the-scenes-and-sounds-of-2025)).

The broader map below is general music-history synthesis. Only the R&B, house, jungle, reggaeton and drill branches were checked against sources, so read it as convention.

```
ROOTS: West African polyrhythm, call-response, clave/tresillo + European harmony and instruments
 +-- Spirituals/gospel ------------------------------> soul -> contemporary gospel / CCM / worship
 +-- Blues (Delta 1920s-30s) -> Chicago electric blues -> jump blues / R&B (1940s)
 |     R&B -> rock'n'roll -> British invasion -> hard rock / metal -> punk -> post-punk / alt / grunge / emo
 |     rock + rap -> nu metal; emo + trap -> emo rap; metal + trap -> trap metal; pop-punk revival (2020s)
 |     soul -> funk ("the One") -> disco -> boogie / post-disco -> house, electro
 |     funk/soul breaks + Jamaican DJing -> hip hop -> boom bap -> trap -> drill / plugg / rage / phonk
 +-- Ragtime + brass bands -> New Orleans jazz -> swing -> bebop -> cool / hard bop -> modal -> fusion
 |     -> smooth / acid / nu-jazz; jazz samples -> boom bap and lo-fi; UK jazz (2010s+)
 +-- Anglo-Celtic folk + blues + gospel -> old-time / hillbilly -> country -> honky-tonk, bluegrass,
 |     Nashville sound, outlaw, country pop, bro-country, country trap; folk revival -> Americana / indie folk
 +-- Caribbean: mento -> ska -> rocksteady -> reggae -> dub -> dancehall
 |     dub/sound systems -> jungle -> DnB; dancehall -> reggaeton -> Latin trap; dancehall + highlife -> afrobeats
 +-- Cuba: son -> mambo / cha-cha -> salsa (NYC); Brazil: samba -> bossa nova -> MPB; Miami bass -> baile funk
 +-- Mexico: corrido / norteño / banda -> corridos tumbados (+ trap attitude)
 +-- Southern Africa: mbaqanga, kwaito (1990s) -> afro house, gqom, amapiano
EDM: disco -> house -> techno / trance / UK garage -> grime, dubstep -> riddim, future garage; synth-pop -> synthwave
```

### The seven genes and where they recur

Reading every card in this report against the others gives seven rhythmic "genes". Together they explain most family resemblances, and several occur far from where they started (derived from the cards and sources cited in later sections).

| Gene | Definition on the 16-step grid | Where it recurs |
|---|---|---|
| Backbeat | snare on 5 and 13 | rock'n'roll, all rock, Motown, Stax, boom bap, country two-beat, bluegrass mandolin chop (no drums), J-pop, sertanejo |
| Half-time | snare/clap on 9 only | trap, drill (bar 1), dubstep, future bass, metalcore breakdowns, pop-punk pre-choruses, country trap, afroswing (snare on beat 3) |
| Four-on-the-floor | kick on 1, 5, 9, 13 | disco, Motown "pulsating" kick, house, techno, trance, soca, kwaito, rockers reggae, French touch, stomp-clap folk, gospel shout, industrial metal |
| Tresillo / 3+3+2 | hits on 1, 4, 7 (half bar) or 1, 7, 13 (whole bar) | dembow, Diwali clap riddim, zouk-love rims, kuduro kick, tamborzão, Khaleeji and malfuf, chiftetelli's opening, highlife clave, baião, tango milonga, bluegrass banjo forward-roll accents, Celtic reel accompaniment, trailer taiko, djent groupings |
| Two-bar clave | son 3-2: steps 1, 4, 7, 11, 13 of CYCLE16 | son, salsa, mambo, Latin jazz, bossa (delayed note), Latin house, highlife bell, Afrobeat |
| Triplet shuffle / compound meter | 12-step long-short | blues, rock'n'roll, jump blues, swing jazz, doo-wop and Stax ballads, Nashville 12/8, bhangra chaal, jig 6/8, Ethio-jazz 6/8, Persian 6/8, son jalisciense, huapango |
| Offbeat chop | short chord on every "and" or on 2 and 4 | ska skank, reggae skank, bluegrass chop, norteño/banda "pah", polka oom-pah, punk skank beat, gospel shout snare on every upbeat, tumbado charcheteo |

A skill can store these seven as reusable layers. Most genres are then one or two genes plus a tempo, a bass job and a timbre.

### The full taxonomy, with the earlier ~40 genres placed

| Family | Carded in this report | Carded earlier (summarised below) | Bridging genres |
|---|---|---|---|
| Rock | rock'n'roll, classic, hard, blues rock, psych, punk, pop-punk, post-punk/new wave, alt/indie, grunge, shoegaze/nu-gaze, post-rock, emo/midwest emo, prog, math rock, garage revival, arena/pop-rock | — | emo rap (rock ↔ trap), pop-punk trap hybrids |
| Metal | NWOBHM/trad, speed/thrash, death (OSDM, slam, melodeath), black, doom/stoner/sludge, power, symphonic, nu metal, metalcore, deathcore, djent/prog, industrial, trap metal | rage (adjacent) | nu metal (metal ↔ hip hop), trap metal |
| Jazz & blues | Delta, Chicago, jump blues, ragtime, Dixieland, swing/big band, bebop, cool, hard bop/soul jazz, modal, Latin jazz/bossa, fusion, smooth, acid, nu-jazz, UK jazz | boom bap and lo-fi (jazz-sample hip hop) | acid jazz, jazz-hop |
| Soul/funk/gospel/disco | JB funk, P-Funk, disco, Motown, Stax/Southern soul, Philly, gospel/CCM/shout, doo-wop, new jack swing, boogie, 90s R&B/hip-hop soul, neo-soul, nu-disco/French touch, modern funk/city pop | modern R&B, classic house, deep house | disco (soul ↔ house), funk (soul ↔ hip hop) |
| Country & folk | honky-tonk/Bakersfield, outlaw, bluegrass/old-time, Nashville sound, country pop, bro-country, country trap, Americana, trad folk, folk revival, indie folk, stomp-clap, Celtic, fingerstyle | trap (carrier for country trap) | country rap, stomp-clap ↔ country trap |
| Latin | son, salsa, mambo/cha-cha, bachata, merengue, cumbia (4 kinds), vallenato, bossa, samba, MPB, baile funk, sertanejo, tango/electrotango, norteño/banda/mariachi/tumbados, Latin trap, Latin pop, moombahton/Latin house | reggaeton, Dominican dembow, Brazilian phonk | corridos tumbados (folk ↔ trap), moombahton (house ↔ reggaeton) |
| Caribbean | ska, rocksteady, roots (one drop/rockers/steppers), dub, lovers rock, dancehall, calypso, soca, zouk, kompa, bouyon | reggaeton, dembow | dub (reggae ↔ bass music), dancehall (reggae ↔ reggaeton ↔ afrobeats) |
| African | Afrobeat (Fela), highlife, jùjú, rumba/soukous, mbalax, gqom, kwaito, kuduro, afro-house roots, bongo flava, Ethio-jazz, afroswing, alté | afrobeats, amapiano, afro house | kwaito (house ↔ amapiano/afro house), afroswing |
| Asia / South Asia / Middle East | K-pop, J-pop, city pop, anime/J-rock, Vocaloid, Mandopop, Bollywood, bhangra, Punjabi pop, Indian classical, Arabic pop, Khaleeji, mahraganat, Turkish/arabesk, Persian, Mizrahi, Uzbek | Jersey club and 2-step (inside K-pop) | city pop → future funk; bhangra ↔ dancehall/trap |
| Classical, film, game, experimental | Baroque, Classical, Romantic, Impressionist, serial/sound-mass, minimalism, neoclassical piano, film adventure/horror/tension/drama/hybrid, game RPG/adaptive, chiptune, new age, drone, noise, musique concrète | cinematic trailer, ambient | hybrid orchestral-electronic, orchestral hip hop |
| Electronic & hip hop | — | see table below | UK garage (house ↔ grime/dubstep/drill), Baltimore/Jersey club (house ↔ hip hop) |

The earlier research carded the following styles in full. They are summarised here only for placement and identification. Each row gives the one or two cues that separate it from neighbours. Sources are the ones cited in that research.

| Earlier genre | BPM (default) | Kick/snare signature | Identity cue | Source |
|---|---|---|---|---|
| Trap | 130–160 (140) | snare on 3, half-time | 8th hats with 1/32 and triplet rolls, long 808 | [Wikipedia: Trap](https://en.wikipedia.org/wiki/Trap_music) |
| UK drill | 138–151 (142–144) | bar 1 snare on 3, bar 2 on 4 | 3+3+2 hats with gaps, sliding 808 melody | [Wikipedia: UK drill](https://en.wikipedia.org/wiki/UK_drill) |
| NY/Brooklyn drill, Chicago drill | 140–150; 60–75 felt | drill skeleton; trap-like | NY: heavier glides; Chicago: static 808, brass/bells | [Wikipedia: Drill](https://en.wikipedia.org/wiki/Drill_music) |
| Plugg / pluggnb | 130–150 half-time | soft clap on 3 | sine leads, bells; pluggnb adds m7/add9 EP chords | [Splice](https://splice.com/blog/what-is-pluggnb/) |
| Rage | 140–170 | snare on 3 | distorted 808, looping supersaw leads | [Wikipedia: Rage](https://en.wikipedia.org/wiki/Rage_rap) |
| Boom bap | 85–95 | 2 & 4 | MPC swing ~57%, chopped vinyl | [Attack](https://www.attackmagazine.com/technique/beat-dissected/90s-boom-bap-hip-hop/) |
| Lo-fi hip hop | 60–90 | soft late 2 & 4 | low-pass ~3 kHz, vinyl, maj7/m7 | [NI](https://blog.native-instruments.com/lo-fi-hip-hop/) |
| Modern R&B | 60–90 | 2 & 4 or 3 | 7th–13th chords, tuned 808 glides | [Violet Recording](https://violetrecording.com/how-to-make-rnb-beats/) |
| Afrobeats | 95–115 (108) | syncopated kick, soft 2 & 4 | 16th shaker, 3-2 clave, muted guitar | [Audeobox](https://www.audeobox.com/learn/fl-studio/how-to-make-afrobeats-in-fl-studio/) |
| Amapiano | 108–115 (112) | restrained four, rim 2 & 4 | log drum, offbeat open hat, jazzy m9 | [Splice](https://splice.com/blog/what-is-amapiano-music/) |
| Reggaeton / Dominican dembow | 85–100 / 115–130 | dembow snare 4, 7, 12, 15 | 3+3+2 "boom-ch-boom-chick" | [Wikipedia: Dembow](https://en.wikipedia.org/wiki/Dembow_beat) |
| Phonk (Memphis/drift/Brazilian) | 130–160 | 2 & 4 or 3 | distorted 808 cowbell melody, Memphis chops | [Wikipedia: Phonk](https://en.wikipedia.org/wiki/Phonk) |
| Jersey club | 130–145 (140) | kicks 1, 5, 9, 12, 15 | bed squeak, chopped vocal hooks | [NI](https://blog.native-instruments.com/jersey-club/) |
| West Coast ratchet; Detroit | ~95–105; ~165–190 | 2 & 4 | clap flurries, "hey"; frantic piano loops | [Wikipedia: Mustard](https://en.wikipedia.org/wiki/Mustard_(music_producer)) |
| Classic/Chicago house | 120–126 (124) | four, clap 2 & 4 | 909, tambourine on every offbeat | [Attack](https://www.attackmagazine.com/technique/beat-dissected/21st-century-chicago-house/) |
| Deep / deep tech / tech house | 110–125 / 125–130 / 123–126 | four | m7/m9 hypnotic vs 16th shaker vs rolling offbeat bass | [Wikipedia: Deep house](https://en.wikipedia.org/wiki/Deep_house) |
| Afro house | ~118–124 | four | 3+3+2 congas/toms, chants | [Wikipedia: Afro house](https://en.wikipedia.org/wiki/Afro_house) |
| Techno; hard techno | 120–150; median 146 | four | timbre over harmony; distorted rumble kick | [Mixgraph](https://www.mixgraph.io/bpm-for/hard-techno) |
| Trance | 125–150 (138) | four, open hat every upbeat | supersaw, beatless breakdown, snare-roll build | [Wikipedia: Trance](https://en.wikipedia.org/wiki/Trance_music) |
| DnB, liquid, neurofunk, jungle | 160–180 (174) | two-step | Amen/Think breaks, reese or clean sub | [Wikipedia: DnB](https://en.wikipedia.org/wiki/Drum_and_bass) |
| Dubstep / riddim | 140 half-time | snare on 3 | wobble/growl; riddim triplet stabs with silence | [Wikipedia: Dubstep](https://en.wikipedia.org/wiki/Dubstep) |
| Future bass | 130–175 | half-time | pitch-bent supersaw chords, pumping | [Wikipedia: Future bass](https://en.wikipedia.org/wiki/Future_bass) |
| UK garage / 2-step | 124–132 / 122–128 | broken, no kick on beat 1 of bar 2 | heavy MPC swing 60–69%, rimshots | [Attack](https://www.attackmagazine.com/technique/beat-dissected/uk-garage/) |
| Synthwave | 80–118 | four or rock | gated snare, octave-pulsing saw bass | [Wikipedia: Synthwave](https://en.wikipedia.org/wiki/Synthwave) |
| Modern pop; hyperpop | 95–125; 135–205 | four or trap | hook by 30–45 s; clipping, Auto-Tune | [Hooktheory](https://www.hooktheory.com/blog/i-analyzed-the-chords-of-1300-popular-songs-for-patterns-this-is-what-i-found/); [Wikipedia: Hyperpop](https://en.wikipedia.org/wiki/Hyperpop) |
| Ambient; cinematic trailer | beatless; 120–150 act 3 | none; taiko 3+3+2 | texture over structure; braams, silence before hits | [Wikipedia: Ambient](https://en.wikipedia.org/wiki/Ambient_music); [Violet Recording](https://violetrecording.com/sound-design-for-trailers/) |

## Rock and metal separate on five settings, not on instruments

### Rock: tempo, swing, chord type, guitar gain and form length decide the subgenre

Almost every rock style uses guitars, bass, drums and voice, so the instrument list identifies nothing. What separates the subgenres is five settings: tempo band, straight versus shuffle feel, chord type (open triads, power chords, add9/maj7 shapes or no chords), how distorted and effected the guitar is, and form length (a 2-minute punk song versus a 10-minute post-rock build). The shared building blocks are sourced. Rock and roll's backbeat on 2 and 4 is "almost always provided by a snare drum" ([Wikipedia: Rock and roll](https://en.wikipedia.org/wiki/Rock_and_roll)). The **power chord** (root, fifth, often octave) stays clear under distortion, where thirds turn "messy and indistinct" ([Wikipedia: Power chord](https://en.wikipedia.org/wiki/Power_chord)). Classic rock's signature move is the **Mixolydian I–bVII–IV**, which resolves bVII to I without a dominant V: "Sweet Home Alabama" is D–C–G ([Benny Sutton](https://bennysutton.com/chords/the-1-flat7-4-1-chord-progression)), and the "Hey Jude" coda uses the same move ([Ethan Hein](https://ethanhein.com/wp/2016/musical-simples-hey-jude/)). Hard rock kept "some swing in the back beat" where metal riffs became stand-alone melodies ([Wikipedia: Hard rock](https://en.wikipedia.org/wiki/Hard_rock)). Blues rock usually plays straight 8ths rather than blues triplets ([Wikipedia: Blues rock](https://en.wikipedia.org/wiki/Blues_rock)). Punk songs are short and fast, keep verse-chorus form and 4/4, and use little syncopation ([Wikipedia: Punk rock](https://en.wikipedia.org/wiki/Punk_rock)). Most rock BPM ranges come from one aggregator ([Orphiq](https://orphiq.com/resources/types-of-rock-music)) or from convention, so treat them as starting points.

| Genre | BPM | Feel | Harmony (spelled) | Guitar / tone | Bass job | Form | Sounds fake when |
|---|---|---|---|---|---|---|---|
| Rock'n'roll (1950s) | 140–180 (conv.) | shuffle ~62–66% or 12/8 | 12-bar in A: A A A A / D D A A / E D A E, dom7s ([Wikipedia](https://en.wikipedia.org/wiki/Rock_and_roll)) | clean/edge-of-breakup, sax or piano lead, slapback 80–140 ms | boogie 1-3-5-6-b7-6-5-3 | 4-bar intro, 12-bar choruses, sax/guitar solo chorus; 2–3 min | straight quantized 8ths, modern gain, huge kick |
| Classic rock | 90–140, ~110–125 (conv.) | straight, slight swing | I–bVII–IV (D–C–G), bVI–bVII–I (C–D–E), sus4 moves | Marshall/Fender crunch, B3 organ, piano | root 8ths with fills | V-C-V-C-solo-C, 3–5 min | too much gain, over-quantized drums |
| Hard rock | 90–140 (conv.) | backbeat with swing → 52–56% (derived) | E/A minor pentatonic; i–bVII–bVI–bVII (E5–D5–C5–D5); E5–G5–A5 | Plexi/JCM800 crunch-to-high gain, 4x12 IR | doubles riff an octave down | riff 4–8, V 8–16, pre 4, C 8, solo 8–16, C ×2 | MIDI guitar without slides/vibrato |
| Blues rock | 70–140 (conv.) | mostly straight ([Wikipedia](https://en.wikipedia.org/wiki/Blues_rock)); Texas shuffle 66% | 12/16-bar I–IV–V; E7 A7 B7 quick change | Tube Screamer into Fender/Marshall | boogie/walking or riff | head ×2, solos ×2–4, head; 4–8 min live | quantized solos without bends |
| Psychedelic | 70–130 (conv.) | mid-tempo, odd-meter shifts ([Wikipedia](https://en.wikipedia.org/wiki/Psychedelic_rock)) | modal drones; C Mixolydian C–Bb–F over C pedal; Dorian Am7–D; Am–Am/G#–Am/G–D/F# | fuzz, wah, flanger, backwards tape, sitar, Mellotron | McCartney counter-lines or drone | 3-min pop psych or 6–20-min jam | busy chord changes, clean digital reverb |
| Punk | 160–200; hardcore 180–220+ ([Orphiq](https://orphiq.com/resources/types-of-rock-music)) | straight, no swing | I–IV–V (E5–A5–B5), I–bVII–IV, I–bIII–IV; all downstrokes | one mid-gain amp, dry | relentless root 8ths ([Wikipedia](https://en.wikipedia.org/wiki/Punk_rock)) | V-C-V-C-break-C, < 2:30 | metal gain, perfect quantize, long songs |
| Pop-punk | 150–190 ([Orphiq](https://orphiq.com/resources/types-of-rock-music)) | straight; half-time pre/bridge | I–V–vi–IV (E5–B5–C#5–A5), vi–IV–I–V | palm-muted verses, open choruses, quad-tracked | root 8ths, walk-ups | intro 4–8, V 8–16, pre 4–8, C 8, bridge 8, C ×2; 2.5–3.5 min | no mute/open contrast, no crash on chorus |
| Post-punk / new wave | 110–150 ([Orphiq](https://orphiq.com/resources/types-of-rock-music)) | mechanical, drum-machine-like ([Wikipedia](https://en.wikipedia.org/wiki/Post-punk)) | two-chord minor vamps Dm–Bb; b2/tritone guitar lines; new wave I–V–vi–IV with maj7 | chorus/flanger single notes, analog synths | **melodic lead bass** high on the neck | vamp-based verse-chorus, 3–5 min | big root bass + wide distorted chords |
| Alt / indie | 90–160, typical 110–140 ([Orphiq](https://orphiq.com/resources/types-of-rock-music)) | straight | Cadd9, Dsus2, Em7 ringing shapes; I–iii–IV; Britpop I–V–vi–IV | jangle (clean+comp+chorus) vs fuzz chorus | simple melodic hooks | quiet verse / loud chorus, 3–4 min | pop-punk-tight editing |
| Grunge | 100–140; sludge 80–110 ([Orphiq](https://orphiq.com/resources/types-of-rock-music)) | slightly behind the beat | drop-D, chromatic power chords; F5–Bb5–Ab5–Db5 (conv.) | DS-1/Big Muff into Marshall, "rolled-off treble" ([Wikipedia](https://en.wikipedia.org/wiki/Grunge)) → LPF 6–8 kHz | "ponderous", overdriven roots | stop-start, soft/loud ([Wikipedia](https://en.wikipedia.org/wiki/Grunge)) | bright scooped metal tone, flat dynamics |
| Shoegaze / nu-gaze | 70–130 (conv.) | straight 8ths, washy | E–Emaj7/G#–A(add9) over open drones, slow harmonic rhythm | wall of fuzz + reverb, glide-guitar pitch wobble ±20–50 cents | root anchor | blurred verse-chorus, noise outro, 4–6 min | upfront clean vocal, dry guitar |
| Post-rock | 60–140 (conv.), "irregular tempos" ([Wikipedia](https://en.wikipedia.org/wiki/Post-rock)) | half/double-time switch at climax | 2–4-chord loop over pedal, Bm–G–D–A | dotted-8th delay, e-bow, tremolo picking, glock/strings | drone, moves at section changes | 6–15 min crescendo (map below) | full loudness too early, crushed master |
| Emo / midwest emo | 90–170; midwest 120–160 (conv.) | odd bars (3/4, 7/8) inserted | Fmaj7–Am7–Bbmaj7(#11)–C(add9), open tunings | clean twinkly arpeggios, bursts of distortion ([Wikipedia](https://en.wikipedia.org/wiki/Emo)) | melodic counterpoint, chugs in loud parts | through-composed, cathartic finale | polished vocal, square 8-bar phrases |
| Progressive rock | varies; 7/8, 5/4, 7/4, 9/8 | meter changes | modal, slash chords; Emaj7–F#/E–G#m7–Asus2 | Mellotron, Hammond, Minimoog ([Wikipedia](https://en.wikipedia.org/wiki/Progressive_rock)) | virtuosic, doubles keys | suites, 6–25 min | odd meter with no grouping defined |
| Math rock | 110–180 (conv.); 5/4, 7/8, 11/8, 13/8 ([Wikipedia](https://en.wikipedia.org/wiki/Math_rock)) | 16th pulse | Amaj9–F#m11–Dmaj7(#11)–E6/9 | clean tapped interlocking guitars | syncopated counter-lines | riff-to-riff, 3–6 min | distorted main parts, plain 4/4 drums |
| Garage revival | 120–170 (conv.) | driving 8ths | E5–A5–B5; single-note lines vs chords | cheap amp crunch, bandpassed vocal 300 Hz–3 kHz | root 8ths or none (duos) | V-C-V-C-solo-C, 2–3.5 min | huge reverb, quad-tracked polish |
| Arena / modern pop-rock | 70–90 anthem; 110–150 up (conv.) | half-time choruses | I–V–vi–IV (Am–F–C–G in C), whole-step last-chorus lift | guitars + pads + hybrid drums | 8th pulse, synth-bass double | pop form with post-chorus; 3–4 min | guitars masking the vocal |

The drum library reduces to one template plus edits: change grid length, move the snare, add kicks or change the cymbal. The punk 8th beat and the d-beat are sourced ([drumhelper](https://drumhelper.com/learning-drums/punk-drum-beats-and-rhythms/); [Wikipedia: D-beat](https://en.wikipedia.org/wiki/D-beat)). The d-beat was developed by Discharge's Terry "Tezz" Roberts around 1979 and named in 1988. The other grids are convention.

```
A  ROCK "MONEY BEAT" (classic, hard, alt, indie, garage; punk at 160-200)
HiHat X . x . | X . x . | X . x . | X . x .
Snare . . . . | X . . . | . . . . | X . . .
Kick  X . . . | . . . . | X . x . | . . . .     push: kick step 7; ghost snare 8/15; open hat 15

B  ROCK'N'ROLL / BLUES SHUFFLE (12-step)        rockabilly train beat: Snare x g g g | X g g g | x g g g | X g g g
Ride  x . x | x . x | x . x | x . x
Snare . . . | X . . | . . . | X . .
Kick  X . . | . . . | X . . | . . .

D  SKANK / POLKA PUNK (hardcore, pop-punk chorus)      E  D-BEAT (crust, Motorhead-style)
Ride  X . x . | X . x . | X . x . | X . x .           HiHat x . x . | x . x . | x . x . | x . x .
Snare . . X . | . . X . | . . X . | . . X .           Snare . . . . | X . . . | . . . . | X . . .
Kick  X . . . | X . . . | X . . . | X . . .           Kick  X . . . | . . x . | X . . . | . . x .

F  HALF-TIME (pop-punk pre, emo/grunge breakdown)      G  GRUNGE CHORUS (snare 5-15 ms late, big room)
HiHat X . x . | X . x . | X . x . | X . x .           Crash x . x . | x . x . | x . x . | x . x .
Snare . . . . | . . . . | X . . . | . . . .           Snare . . . . | X . . . | . . . . | X . . g
Kick  X . . . | . . x . | . . . . | . . x .           Kick  X . . . | . . x . | X . x . | . . . .

H  POST-PUNK TOMS / DANCE-PUNK                         J  MATH ROCK 7/8 (14 steps, 2+2+3)
Tom   x . x x | x . x x | x . x x | x . x x           HiHat x . x . | x . x . | x . x . x .
HiHat . . o . | . . o . | . . o . | . . o . (dance)   Snare . . . . | X . . . | . . . . X .
Kick  X . . . | X . . . | X . . . | X . . . (dance)   Kick  X . . . | . . . . | X . x . . .
                                                      5/4 = 20 steps: kick 1 & 13, snare 9 & 17, 8th hats
L  ARENA STOMP-CLAP: Kick X . X . | . . . . | X . X . | . . . .  Clap on 5 and 13; 1980s gated snare
```

Post-rock is a dynamics map rather than a groove (convention, built on the sourced "repetitive build-ups... extremely wide range of dynamics", [Wikipedia: Post-rock](https://en.wikipedia.org/wiki/Post-rock)). Section 1 runs 16–32 bars with no drums or a ride-bell pulse at velocity 40–60. Section 2 adds floor-tom 8ths for 16 bars at 60–80. Section 3 is an 8–16-bar build with snare 8ths, then 16ths, ramping 60 to 127, ending on a cymbal roll and one beat of silence. Section 4 is a 16–32-bar climax with crashes on every quarter at 110–127. Section 5 is a decay into reverb.

Arrangement follows three models (synthesis of the sourced traits, convention in detail). **Riff-based** rock (hard, blues, grunge) doubles the guitar riff an octave down in the bass, with the kick following riff accents. **Chord-based** rock (classic, punk, pop-punk, indie) locks root-8th bass to the kick under two doubled rhythm guitars. **Texture-based** rock (shoegaze, post-rock, emo, math) treats guitars as layers or interlocking arpeggios over a bass that anchors with roots or drones. Shoegaze is a Spector-like wall where "no instrument is distinguishable" ([Wikipedia: Shoegaze](https://en.wikipedia.org/wiki/Shoegaze)). Post-punk's melodic bass freed guitarists from rock convention ([Wikipedia: Post-punk](https://en.wikipedia.org/wiki/Post-punk)). Quiet-loud dynamics (verse = bass, one clean guitar and closed hat; chorus = doubled distortion, crash and backing vocals) are the core alt/grunge/emo move ([Wikipedia: Alternative rock](https://en.wikipedia.org/wiki/Alternative_rock)).

Emulation is where most AI rock fails. Doubled rhythm guitars must be **two different performances panned hard left and right**. Copy-paste fails because it needs "unique waveforms", and real engineers also vary the pickup, amp EQ and gain between takes ([Music Guy Mixing](https://www.musicguymixing.com/double-tracking-rhythm-guitars/)). Keeping the split at 100% opens the centre for kick, snare, bass and vocal ([Violet Recording](https://violetrecording.com/how-to-double-track-rhythm-guitars/)). MIDI drums should be quantized at about **75% strength** rather than 100%, with a parallel-compressed drum bus at about 10 dB of gain reduction ([Mastering.com](https://mastering.com/program-realistic-midi-drums/)). Notes should be pushed or pulled by small offsets (search summaries put it at about ±10 ticks, unconfirmed), with accents, ghosts and flams, because overusing randomisation also sounds unrealistic ([Native Instruments](https://blog.native-instruments.com/midi-drums)). The FL workflow is convention. For guitar, use a MIDI guitar VST with palm-mute, slide and strum keyswitches into an amp sim and cab IR, or FL's "Hardcore" multi-FX with Fruity Convolver as a sketch-quality fallback. High-pass guitars at 80–120 Hz and low-pass at 8–12 kHz (6–8 kHz for grunge). Stagger chord notes 5–30 ms for strums, low to high on downstrokes. Draw pitch bends on solos (a whole step = +2 semitones) with mod-wheel vibrato. Program the left and right parts with different timing and velocity seeds. Velocity bands for drums are: kick 100–120, backbeat 110–127, ghosts 25–45, hats 95–110 on downbeats and 70–85 on offbeats. Limb logic matters: one hand on hats, ride or crash at a time, no hats under tom fills, and fills resolve to crash plus kick. The six universal rock tells are: cloned L/R guitars that collapse in mono; flat-velocity, 100%-quantized drums with impossible limb overlaps; scooped metal gain on non-metal genres; unbent MIDI solos; no verse/chorus dynamic difference; and reverb where the genre wants it dry (punk, garage) or dry where it wants a wash (shoegaze, post-rock).

### Metal: tuning depth, right hand, drum engine and voice

Metal subgenres are told apart by four audible levers. The first is **tuning depth**: E or Eb standard for traditional and power metal; D or C for thrash through death; B, A, 7- and 8-string for nu metal, metalcore, deathcore and djent. The second is **right-hand technique**: gallop, palm-muted chug or un-muted tremolo. The third is the **drum engine**, and the fourth is **vocal type**. Harmony stays modal-minor across the family. Heavy metal rests on modal progressions, tritone and chromatic moves, and pedal points, favouring **Aeolian** (i–bVI–bVII, i–bVI–iv–bVII) and **Phrygian** (i–bII–i, i–bII–III). Its tempos run from ballad quarter = 60 to blast-beat quarter = 350 ([Wikipedia: Heavy metal](https://en.wikipedia.org/wiki/Heavy_metal_music)). Lowest-string MIDI numbers are derived arithmetic: E standard E2 = 40, drop D/D standard = 38, drop C/C standard = 36, B standard or 7-string = 35, drop A/A 7-string = 33, 8-string F#1 = 30. A power chord is root + 7 semitones (+12). Most 8-strings extend standard tuning with low B and F# ([Strandberg](https://strandbergguitars.com/7-and-8-string-guitar-tunings-with-strandberg)), and Korn play 7-strings in A standard ([Killer Guitar Rigs](https://killerguitarrigs.com/?p=1793)). Drop-A claims for Slipknot are disputed, and Drop B is also reported.

Six drum engines cover nearly everything, and the blast-beat definitions are sourced. The traditional blast alternates snare and kick as a single-stroke roll with the ride in unison with the kick. The bomb blast puts 16th kicks under 8th snares. The **skank beat** is a sped-up 2/4 polka called the "Slayer" or "thrash" beat in the US ([Wikipedia: Blast beat](https://en.wikipedia.org/wiki/Blast_beat)). The **gallop** is an 8th plus two 16ths ([freedrumlessons](https://freedrumlessons.com/drum-lessons/heavy-metal-drumming.php)). In djent, the hands keep a straight 4/4 while the feet follow polymetric guitar cycles such as 3/16, 19/16 or 23/16, or groupings like 5-5-5-1, 6-6-4 and 7-7-7-7-4 across two bars, until they realign ([Premier Guitar](https://www.premierguitar.com/articles/26211-obsessive-progressive-how-to-decode-advanced-polymeters)). Nu-metal drummers are hip-hop-influenced, and blasts and double bass are uncommon there ([Wikipedia: Nu metal](https://en.wikipedia.org/wiki/Nu_metal)).

```
GALLOP (NWOBHM, 160)                         SKANK / THRASH (190)
Kick  X . x x | . . . . | X . x x | . . . .  Kick  X . . . | x . . . | X . . . | x . . .
Snare . . . . | X . . . | . . . . | X . . .  Snare . . x . | . . x . | . . x . | . . x .
Hat   x . x . | x . x . | x . x . | x . x .  Cym   x . x . | x . x . | x . x . | x . x .

TRADITIONAL BLAST (16th strokes)             BOMB BLAST                      HAMMER = all three in unison 8ths
Kick  x . x . | x . x . | x . x . | x . x .  Kick  x x x x | x x x x | x x x x | x x x x
Snare . x . x | . x . x | . x . x | . x . x  Snare x . x . | x . x . | x . x . | x . x .
Cym   x . x . | x . x . | x . x . | x . x .  Cym   x . x . | x . x . | x . x . | x . x .

DOUBLE-KICK + BACKBEAT (power, melodeath, metalcore verse)   METALCORE BREAKDOWN (half-time, kick = guitar chugs)
Kick  x x x x | x x x x | x x x x | x x x x  (alt 110/95)   Kick  X . . X | . . X . | . X . . | X . . .
Snare . . . . | X . . . | . . . . | X . . .                Snare . . . . | . . . . | X . . . | . . . .
Cym   x . . . | x . . . | x . . . | x . . .                China X . . . | X . . . | X . . . | X . . .

DJENT (hands 4/4, kick/guitar 3+3+3+3+4)     NU METAL (100, hip-hop)          TRAP METAL (145 half-time)
Kick  X . . X | . . X . | . X . . | X . . .  Kick  X . . x | . . X . | . . x . | . x . .   Kick  X . . . | . . . . | . . x . | . . . .
Snare . . . . | . . . . | X . . . | . . . .  Snare . . . . | X . . g | . . . . | X . . .   Snare . . . . | . . . . | X . . . | . . . .
Cym   x . . . | x . . . | x . . . | x . . .  Hat   x . x . | x . x . | x . x . | x . o .   Hat   x x x x | x x x x | x x x x | x . x x
DOOM (65): Kick X . . . | . . . . | x . x . | . . . . ; snare on 9; crash/ride quarters
INDUSTRIAL (120): four-on-floor, snare 2 & 4, sequenced 16th hats, everything quantized
```

| Subgenre | BPM (conv.) | Tuning / technique | Harmony | Vocals | Drum engine | Form | Fake tell |
|---|---|---|---|---|---|---|---|
| NWOBHM / traditional | 110–180 (160) | E std, gallops, twin leads in 3rds ([Wikipedia](https://en.wikipedia.org/wiki/New_wave_of_British_heavy_metal)) | Em–C–D (i–bVI–bVII), pedal riffs | high clean tenor | gallop | intro 8, V 16, pre 8, C 8, solo 16–32, C | scooped modern gain, 127-velocity drums |
| Speed / thrash | 160–240 (190) | E/Eb/D std, palm-muted 16th chugs ([Wikipedia](https://en.wikipedia.org/wiki/Thrash_metal)) | chromatic, tritone; E5 pedal → F5 (bII) → Bb5 | barked | skank, double-time | riffs, tempo-shifted middle with solos, 4–8 min | legato palm mutes, buried bass |
| Death (OSDM, slam, melodeath) | 100–260 with abrupt changes ([Wikipedia](https://en.wikipedia.org/wiki/Death_metal)) | D/C or lower, tremolo + palm mute | chromatic clusters; C5–Db5–C5–Gb5 | growls | blasts, double kick; slam half-time | riff chains A-B-C-B-D | one tempo throughout, flat tremolo velocity |
| Black | blasts up to ~300 ([Wikipedia](https://en.wikipedia.org/wiki/Black_metal)); mid 90–130 | E/Eb std, **un-muted** tremolo chords, trebly lo-fi | minor, tritone, i–bVI–bVII–i | shrieks | traditional blast, skank | long riff cycles ×4–16, 6–10 min | clicky polished kicks, palm muting |
| Doom / stoner / sludge | funeral 40–60, doom 50–80, stoner 70–120, sludge 60–90 + bursts | low tunings, fuzz, ring-out ([Wikipedia](https://en.wikipedia.org/wiki/Doom_metal)) | minor pentatonic + b5; C5–Gb5–F5 | mournful clean / laid-back / screamed | crawl, stoner shuffle, sludge d-beat bursts | few riffs, 6–15 min | 16th chugs, thin clean bass |
| Power | 140–200 (170) | E/Eb/D std, tight gain | Am–F–G–Am, harmonic minor, whole-step final lift | operatic tenor ([Wikipedia](https://en.wikipedia.org/wiki/Power_metal)) | constant double kick | orchestral intro … key-change final chorus | machine-gun flat 127 kicks |
| Symphonic | 90–170 (120–140) | simpler guitars under orchestra ([Wikipedia](https://en.wikipedia.org/wiki/Symphonic_metal)) | Dm–Bb–F–C, Picardy lifts | soprano, choirs | rock beat + double-kick fills | orchestral intro/bridge, epics 10+ min | guitars masking orchestra |
| Nu metal | 85–140 (100) | 7-string A/B, one-string syncopated chugs | Dorian/Aeolian/Phrygian ([Wikipedia](https://en.wikipedia.org/wiki/Nu_metal)); A chugs + Bb, Eb stabs | rap/sing/scream | hip-hop beat | quiet rapped V 16 / loud sung C 8 | blasts, solos |
| Metalcore | 120–200 (150–160) | Drop D–A, 7/8-strings ([Wikipedia](https://en.wikipedia.org/wiki/Metalcore)) | Cm–Ab–Eb–Bb chorus | harsh verse, clean (tuned) chorus | double kick verse, 8th chorus, half-time breakdown | intro, V, pre, C, V, C, bridge, breakdown 8–16, C; ~3:30 | breakdown not half-time, no silence before it |
| Deathcore | 100–240 | Drop A and lower; open-string staccato chugs ([Wikipedia](https://en.wikipedia.org/wiki/Deathcore)) | Phrygian, b2/tritone hits | growls, squeals | bomb blast + breakdown | riff-blast-breakdown cycles; last breakdown slowed 10–30% | muddy lows, long chugs |
| Djent / prog | 100–150 half-time feel | 7/8/9-string, gated high-attack chugs ([Wikipedia](https://en.wikipedia.org/wiki/Djent)) | low pedal + add9/maj7#11 cleans | clean airy vs harsh | 4/4 hands, polymetric feet | riff blocks + ambient interludes | snare on the odd grouping, sloppy note ends |
| Industrial | 100–140 (120) | looped riffs, drum machines ([Wikipedia](https://en.wikipedia.org/wiki/Industrial_metal)) | one-two-chord Phrygian | processed shouts | machine four-on-floor | intro synth loop, verse-chorus, ~4 min | humanized "live" drums |
| Trap metal | 130–160 half-time | 808 kit, distorted 808s, occasional guitar ([Wikipedia](https://en.wikipedia.org/wiki/Trap_metal); [eMastered](https://emastered.com/es/blog/what-is-dark-trap-music)) | 1–2-note Phrygian loops | screamed rap | trap | rap form, 2–3 min | clean polite 808, double kick |

Breakdowns are slow, palm-muted, low-string sections, sometimes with a **bass drop**, that cue moshing ([Wikipedia: Breakdown](https://en.wikipedia.org/wiki/Breakdown_(music))). The deathcore version is single palm-muted notes repeated on low open strings ([Wikipedia: Deathcore](https://en.wikipedia.org/wiki/Deathcore)). The recipe is convention consistent with those sources. Cut everything for one beat to one bar before the downbeat. Switch to half-time (snare on step 9) or drop the tempo. Chug the open low string with deliberate 16th rests and b2 or tritone stabs (Drop C: C2 = MIDI 36 chugs with Db and Gb hits). Put the kick in unison with every chug and a china on quarters. Land a falling sine or 808 sub drop on the downbeat. Run it 8 or 16 bars, repeated with variation. Modern hybrids now switch genre inside a song. Sleep Token's "The Summoning" moves from a piano intro to an R&B verse and a low-tuned breakdown, and Sleep Token's *Even in Arcadia* and Ghost's *Skeleta* both reached No. 1 on the Billboard 200 in 2025 ([Cherwell](https://cherwell.org/2025/06/01/oxford-sleep-token-metal/); [Chartmetric](https://hmc.chartmetric.com/sleep-token-turnstile-hard-rock-bands-top-charts-2025/)).

Modern metal tone is "built", and its numbers are unusually well sourced from Nail The Mix. Quad-track guitars with pair 1 at 100% L/R and pair 2 at 70–80% with less gain or a different IR ([NTM: quad tracking](https://www.nailthemix.com/quad-tracking-guitars)). High-pass at 100–150 Hz for low tunings and low-pass from 10–12 kHz. Make narrow cuts at 250–500 Hz, use 1–2 dB of bus compression, and put multiband control on 100–250 Hz palm-mute "woof". Use less gain than you think ([NTM: guitar FAQs](https://www.nailthemix.com/guitar-mixing-faqs)). Sample replacement is practically standard, and deathcore often fully replaces kick and snare ([NTM: drum FAQs](https://www.nailthemix.com/drum-mixing-faqs)). The kick is three layers: a click high-passed at 100–300 Hz, a body boosted at 60–100 Hz, and a 40–60 Hz sine sub. EQ it with a 30–40 Hz high-pass and a 200–500 Hz cut, then compress with FET attack 5–10 ms, release 50–150 ms, 4:1–8:1 and 3–6 dB GR, plus parallel crush ([NTM: kick](https://nailthemix.com/kick-drum)). For MIDI guitars (convention), palm mutes are short notes (about 1/32–1/16 at 150 BPM) at velocity 90–110 ±5, never duplicated L/R, with pick scrapes and slides at section changes. Tighten to the grid for djent, deathcore, metalcore and industrial, and leave old-school, doom, stoner and black looser. Bass is split into a clean compressed low band and a distorted upper band (split frequency is convention). The cross-genre fake tells are flat machine-gun kicks, long legato palm mutes, a single centred guitar, unfiltered guitar lows masking the kick, no silence before breakdowns, and the wrong drum engine for the genre (blasts in nu metal, trap hats in thrash).

## Jazz, blues, soul, funk, gospel and disco run on swing ratio and harmonic density

### Blues and jazz share one harmonic toolkit and differ in who keeps time

Blues styles share the 12-bar I7–IV7–V7 form and the blues scale and differ mainly in instruments, amplification and groove. Jazz styles differ by tempo, harmonic rhythm and the drummer's job. Time moves from the two-beat tuba and banjo of New Orleans, to the swing-era 4/4 walking bass and hi-hat, to the bebop ride cymbal, to funk and electronic kick-snare in fusion and nu-jazz. Bebop's language is sourced: rhythm changes, contrafacts (new melodies on old changes), tritone substitutions, altered chords and upper extensions ([Wikipedia: Bebop](https://en.wikipedia.org/wiki/Bebop)). The 3rd and 7th are the **guide tones** that define chord quality and move by step through ii–V–I, so the 5th is usually dropped ([The Jazz Resource](https://www.thejazzresource.com/shell_voicings.html); [Bass Musician Magazine](https://bassmusicianmagazine.com/2012/08/guide-tones-by-joshua-barnhart/)). Shell voicings (1-3-7) were pioneered on guitar by Freddie Green and Django Reinhardt ([Jazz Guitar Lessons](https://learn.jazzguitarlessons.net/blog/shell-voicings-jazz-guitar)). McCoy Tyner's quartal voicings keep motion inside a mode ([Wikipedia: Modal jazz](https://en.wikipedia.org/wiki/Modal_jazz)). The progressions below are standard teaching convention, spelled out so a generator can use them directly.

```
12-BAR BLUES (A):      A7 | D7 | A7 | A7 | D7 | D7 | A7 | A7 | E7 | D7 | A7 | E7     (bar 2 D7 = quick change)
8-BAR BLUES:           I | V | IV | IV | I | V | I | V
JAZZ BLUES (F):        F7 | Bb7 | F7 | Cm7 F7 | Bb7 | Bdim7 | F7 | Am7 D7 | Gm7 | C7 | F7 D7 | Gm7 C7
BIRD BLUES (F):        Fmaj7 | Em7b5 A7 | Dm7 G7 | Cm7 F7 | Bb7 | Bbm7 Eb7 | Am7 D7 | Abm7 Db7 | Gm7 | C7 | F D7 | Gm7 C7
MINOR BLUES (C):       Cm7 | Fm7 | Cm7 | Cm7 | Fm7 | Fm7 | Cm7 | Cm7 | Ab7 | G7alt | Cm7 | Dm7b5 G7
RHYTHM CHANGES (Bb) A: Bbmaj7 G7 | Cm7 F7 | Dm7 G7 | Cm7 F7 | Fm7 Bb7 | Ebmaj7 Ab7 | Dm7 G7 | Cm7 F7
             bridge:   D7 | D7 | G7 | G7 | C7 | C7 | F7 | F7          (AABA, 32 bars)
ii-V-I (C):            Dm7 G7 Cmaj7;  tritone sub Dm7 Db7 Cmaj7
"SO WHAT" (modal):     16 bars Dm7 (D Dorian) | 8 bars Ebm7 | 8 bars Dm7; chord E-A-D-G-B over D
SCALES (C):            blues C Eb F F# G Bb; major blues C D Eb E G A; bebop dominant C D E F G A Bb B;
                       bebop major C D E F G G# A B; altered = melodic minor mode 7 over V7alt
VOICINGS (C):          shells Dm7 D-F-C, G7 G-F-B, Cmaj7 C-E-B; rootless Dm9 F-A-C-E -> G13 F-A-B-E -> Cmaj9 E-G-B-D;
                       G7alt rootless F-Ab-B-Eb; horn sections 4-way close or drop-2
```

Swing is **not** a fixed 2:1 ratio, and the jazz research's key correction for programmers is this. Friberg and Sundström measured the ride cymbals of Tony Williams, Jack DeJohnette, Jeff Watts and Adam Nussbaum on commercial records. Swing ratios ran up to **almost 3.5:1 at slow tempos and fell to about 1:1 at fast tempos**, with the short note held near **100 ms** across medium-to-fast tempos, so true 2:1 "triplet feel" occurs only around one tempo ([Friberg, ASA](https://acoustics.org/pressroom/httpdocs/137th/friberg.html)). Applying the 100 ms rule gives a programming table (derived): ratio r ≈ (60000/BPM − 100)/100, capped near 3.5. The offbeat sits at r/(r+1) of the beat, which equals the MPC swing percentage.

| BPM | Ride ratio | Offbeat position / MPC % | FL tick at 96 PPQ |
|---|---|---|---|
| ≤120 | ~3:1 to 3.5:1 | 75–78% | 72–75 |
| 150 | 3:1 | 75% | 72 |
| 180 | 2.3:1 | 70% | 67 |
| 200 | 2:1 | 66.7% | 64 |
| 240 | 1.5:1 | 60% | 58 |
| 300+ | ~1:1 | 50–55% | 48–53 |

The ratios are for the drummer's ride. Bass and comping should sit slightly straighter, and horns a few milliseconds behind (convention). The core pattern is the ride on all four beats with skip notes, hi-hat foot on 2 and 4 ([Free Drum Lessons](https://freedrumlessons.com/drum-lessons/basic-jazz-pattern.php); [Vic Firth](https://ae.vicfirth.com/wp-content/uploads/FADrumset-swingin-easy.pdf)), and a "feathered" kick on quarters that is felt rather than heard ([Cruise Ship Drummer](https://cruiseshipdrummer.com/?p=796)). In jazz the ride, not the hi-hat, is the dominant timekeeper, and it is best played in real time on a velocity-sensitive controller ([Sound On Sound](https://www.soundonsound.com/techniques/effective-drum-programming-part-2)).

```
SWING (12-step triplet grid)                  BLUES SHUFFLE (12-step)
Ride    x . . | X . x | x . . | X . x          HH/ride x . x | x . x | x . x | x . x   (every beat long-short)
HHfoot  . . . | X . . | . . . | X . .          Snare   . . . | X . . | . . . | X . .
Kick    g . . | g . . | g . . | g . .  (20-35) Kick    X . . | x . . | X . . | x . .
Snare   . . g | . . . | . . x | . . .  (vary)  Guitar  X . x | X . x | X . x | X . x   (root-5 / root-6 / root-b7 boogie)
Bass    X . . | x . . | x . . | x . .  (walk)
Piano   . . . | . . x | . . . | . . .  (Charleston 1 + "&2")

RAGTIME (16 steps = 2 bars of 2/4, no swing)  DIXIELAND (12-step)
LH bass  X . . . | x . . . | X . . . | x . . . Tuba   X . . | . . . | X . . | . . .
LH chord . . x . | . . x . | . . x . | . . x . Banjo  x . . | X . . | x . . | X . .
RH       X x . x | x . x . | X x . x | . x . . Snare  . . . | x . . | . . . | x . g

BOSSA (16-step one bar)                        FUSION / ACID JAZZ (16-step)
Kick  X . . . | . . X . | X . . . | . . X .    Kick  X . . x | . . X . | . . x . | . X . .
Cross-stick: bar 1 steps 1,7,13; bar 2 steps 5,11 (2-bar bossa clave)   Snare . . . . | X . . g | . g . . | X . . g
Shaker x x x x | x x x x | x x x x | x x x x   HH    x x x x | x x x x | x x x x | x x o x
```

Walking bass follows four rules (convention). Beat 1 is the chord root (or 3rd). Beats 2 and 3 are chord or scale tones. Beat 4 is a chromatic approach a half step from the next root. Heads use a two-feel before walking in four for solos. Over Dm7–G7–Cmaj7 that gives D F A Ab | G B D Db | C E G B, in an upright register of about MIDI 28–55 (FL labels E2–G4).

| Card | BPM | Feel | Harmony | Lead sound / ensemble | Form | Sounds fake when |
|---|---|---|---|---|---|---|
| Delta blues | 60–110, drifting | loose triplet; bars added or dropped | I7–IV7–V7 or one-chord drone; open G/D tunings | solo voice + acoustic slide guitar, harmonica ([Wikipedia](https://en.wikipedia.org/wiki/Delta_blues)) | AAB lyric over loose 12-bar, 2.5–3.5 min | quantized strums, fixed b3 with no bends, drum kit |
| Chicago blues | slow 50–75 in 12/8; shuffles 100–150 | heavy triplet shuffle | 12-bar quick change; stop-time riffs; harp in 2nd position | amplified guitar and harmonica, full band ([Wikipedia](https://en.wikipedia.org/wiki/Chicago_blues)) | intro turnaround, 3–6 vocal choruses, solos | straight 8ths, clean DI guitar |
| Jump blues | 140–200, "bright bounce" ([Wikipedia](https://en.wikipedia.org/wiki/Jump_blues)) | hard shuffle, eight-to-the-bar boogie | 12-bar with 6ths | 5–7 piece, honking tenor, horn riffs | riff tunes, 2.5–3 min | horns with no scoops/falls |
| Ragtime | 70–100 in 2/4 ("never fast", [Wikipedia](https://en.wikipedia.org/wiki/Ragtime)) | **straight** | major with secondary dominants; trio to IV | solo piano, oom-pah LH | AABBACCDD 16-bar strains | swinging it, even velocity |
| New Orleans / Dixieland | 100–220 | two-beat, light swing ([Wikipedia](https://en.wikipedia.org/wiki/Dixieland)) | III7–VI7–II7–V7 cycles | trumpet lead, clarinet above, trombone smears, tuba, banjo | ensemble chorus, breaks, collective out-chorus | horns in block chords, walking bass |
| Swing / big band | dance 120–220, ballads 60–80 | 4/4 walking, swung 8ths ([Wikipedia](https://en.wikipedia.org/wiki/Swing_music)) | 6/9 and 13 chords, ii–V, AABA | 5 sax, 4 tpt, 4 tbn, 4 rhythm (conv.); call-response sections | intro, head, solos with backgrounds, shout chorus | sections perfectly aligned (real ones smear 10–20 ms) |
| Bebop | 180–320+, ballads 50–70 | ratio toward 1:1 at speed | rhythm changes, tritone subs, alterations | sax + trumpet unison heads, ride + "bombs" | head, solos, trading fours, head | 2:1 swing at 300 BPM, root-only bass |
| Cool / West Coast | 90–180 | light swing, brushes | lighter ii–V, maj7/9 counterpoint | soft horns, pianoless or arranged | arranged interludes | sticks instead of brushes |
| Hard bop / soul jazz | 120–240; boogaloo straight | punchy swing | blues, minor blues, gospel IV–I "amen" ([Wikipedia](https://en.wikipedia.org/wiki/Hard_bop)) | trumpet + tenor quintet; B3 organ trio | head with send-offs and drum features | polite drums, no blues inflection |
| Modal | ~130–150 to very fast | Elvin-style 3-over-2 | one mode 8–16 bars; quartal ([Wikipedia](https://en.wikipedia.org/wiki/Modal_jazz)) | quartet, bass ostinato | AABA modal head or open vamps | ii–V clichés over the vamp |
| Latin jazz / bossa | bossa 120–140 quarter (60–70 Brazilian 2/4); mambo 180–220 | **straight** | bossa maj7/m7/13 chromatic ii–Vs; montuno 2-chord vamps | nylon guitar + soft voice; congas, timbales, horns | AABA (Ipanema A8 A8 B16 A8) | swinging bossa, clave reversed |
| Fusion | 90–200 | straight 16ths, slight 52–56% | modal vamps, slash and sus chords | Rhodes, Minimoog, fretless, electric guitar ([Wikipedia](https://en.wikipedia.org/wiki/Jazz_fusion)) | extended vamps, 5–20 min | static synth patches, 100% quantize |
| Smooth jazz | 90–105 ([Wikipedia](https://en.wikipedia.org/wiki/Smooth_jazz)) | straight or 52–58% | IVmaj7–III7–vim7 (Dbmaj7–C7–Fm7) | soprano/tenor sax over programmed R&B groove | radio song form | MIDI sax with no breath/vibrato |
| Acid jazz | 95–120 | break-beat 16ths | m7/m9 Dorian vamps | horns, B3, wah guitar, DJs ([Wikipedia](https://en.wikipedia.org/wiki/Acid_jazz)) | long DJ-friendly grooves | quantized stabs, static Leslie |
| Nu-jazz / jazz-hop | house 118–125; broken beat 125–135; jazz-hop 80–95 | steady electronic groove under jazz harmony ([MasterClass](https://www.masterclass.com/articles/nu-jazz-music-guide)) | m9/maj9/11 loops | live sax/keys over electronics ([Wikipedia](https://en.wikipedia.org/wiki/Nu_jazz)) | 16-bar blocks | jazz chords over generic EDM drums |
| Modern UK jazz | afrobeat 100–125; broken beat 120–135; grime 140 | straight with human push | modal vamps, highlife major | Ezra Collective, Nubya Garcia, Shabaka ([Jazzwise](https://jazzwise.com/articles/nominees-announced-for-2025-jazz-fm-awards)) | vamp, solos with club build/drop | classic swing ride, polite dynamics |

The realism stack is: (a) tempo-correct swing on the right subdivision, (b) wide role-specific velocities, (c) small timing offsets and real-time-played cymbals, (d) idiomatic parts, and (e) acoustic samples in a room ([Mastering.com](https://mastering.com/?p=14279); [Sound On Sound](https://www.soundonsound.com/techniques/effective-drum-programming-part-2)). Velocity bands (convention) are: ride 90–105 on 2 and 4, 75–90 on 1 and 3, and 55–75 on skips; hi-hat foot 60–80; feathered kick 20–35 with bombs at 95–115; comping ghosts 25–45; walking bass 70–95; piano comping 50–80. For timing, keep ride and bass within ±5 ms, put horns 5–20 ms behind on downbeats, and never apply the same random offset to every part. In FL, set the piano-roll snap to 1/3 beat and nudge per the swing table, because the Channel Rack swing knob swings 16ths. The most common fake tells are a fixed 2:1 swing at every tempo, root-only bass, full root-position piano chords on every beat, sustained horns without breath automation, blue notes as fixed b3/b5 instead of bends, swung bossa or ragtime, and a huge hall reverb. Acoustic jazz masters sit around −14 to −18 LUFS integrated (convention).

### Soul, funk, gospel and disco sort on beat weight, swing and chord density

This family splits along four audible axes (derived from the cards below). The first is **where the weight sits**: funk leans on beat 1; Motown, Stax and boogie on the 2-and-4 backbeat; disco, Philly and French touch on four-on-the-floor with an open hat on every "and". The second is **swing**: near straight for disco, Motown and French touch; light for funk and boogie; heavy swung 16th triplets for new jack swing; and per-note "drunk" offsets for neo-soul. The third is **harmonic density**: one-chord funk vamps, lush Philly maj7/m9 with strings, gospel passing chords, and looped neo-soul m9/m11/maj13. The fourth is **live band versus machine**.

Several origin facts are sourced. Funk rests on interlocking syncopated bass, 16th drums and syncopated guitar, and the bass is "most prominent" and plays the hook. Funk prefers extended chords such as Fm11, C7(#9)sus4, F9, Cm6 and F6/9, and minor 7ths over minor triads ([Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk)). "Cold Sweat" has only one definite chord change, to the subtonic at the bridge, and its bar-1 beat-4 snare is delayed by an eighth ([Wikipedia: Cold Sweat](https://en.wikipedia.org/wiki/Cold_Sweat)). Disco's beat comes from Earl Young at Sigma Sound: "put some fours on the floor and twos on the snare, and ride the 16th on the sock cymbal" ([Wikipedia: Earl Young](https://en.wikipedia.org/wiki/Earl_Young_(drummer))). Its loud hats reportedly trace to a mix error on "Bad Luck" (1975) ([Wikipedia: Disco](https://en.wikipedia.org/wiki/Disco)). Measured disco tempos have a median of **122 BPM (IQR 119–124, 7,359 tracks)** in a DJ-skewed catalogue, and funk's small sample (21 tracks) has a median of 118 ([Mixgraph: Disco](https://www.mixgraph.io/bpm-for/disco); [Mixgraph: Funk](https://www.mixgraph.io/bpm-for/funk)). Boogie is **110–116 BPM with strong 2 and 4 and no four-on-the-floor** ([Wikipedia: Boogie](https://en.wikipedia.org/wiki/Boogie_(genre))). New jack swing's "swingbeats" use accented off-beat 16th triplets on an SP-1200 and TR-808 with a dominant snare ([Wikipedia: New jack swing](https://en.wikipedia.org/wiki/New_jack_swing); [Mixdown](https://mixdownmag.com.au/features/columns/producer-focus-teddy-riley)). Neo-soul grooves "hang on the back of the beat". D'Angelo asked Questlove to play "as drunk and as slow and as dusted" as possible, modelled on J Dilla ([Wikipedia: Voodoo](https://en.wikipedia.org/wiki/Voodoo_(D%27Angelo_album))).

```
JB FUNK, "COLD SWEAT"-DERIVED (2 bars; bar-1 beat-4 snare pushed to step 15)    CHICKEN-SCRATCH GUITAR (one chord)
Bar1 Kick  X . . . | . . . . | x . x . | . . . .                                Gtr X g g g | g g X g | g g X g | X g g g
     Snare . . . . | X . . g | . g . . | . . X .
Bar2 Snare . . . . | X . . g | . g . . | X . . g     Hat X x x x on every beat (accent 8ths)

DISCO (118-122, swing off)                      MOTOWN (~124, gentle swing)            STAX / MEMPHIS (108, snare 5-15 ms late)
Kick  X . . . | X . . . | X . . . | X . . .     Kick  X . . . | X . . . | X . . . | X . . .   Kick  X . . . | . . . . | X . x . | . . . .
Snare . . . . | X . . . | . . . . | X . . .     Snare . . . . | X . . g | . . . . | X . . .   Snare . . . . | X . . . | . . . . | X . . .
CHat  x x . x | x x . x | x x . x | x x . x     Tamb  . . x . | X . x . | . . x . | X . x .   Horns . . . . | . . X . | . . . . | . . X .
OHat  . . o . | . . o . | . . o . | . . o .     Gtr   . . . . | X . . . | . . . . | X . . .
Bass  X . x . | X . x . | X . x x | X . x .  (E1 on beats, E2 on "and")

GOSPEL SHOUT (~140-180, conv.)                  NEW JACK SWING (104, swing ~62-66%)     BOOGIE (110-116, no four-floor)
Kick  X . . . | X . . . | X . . . | X . . .     Kick  X . . x | . . x . | . x X . | . . x .   Kick X . . . | . . x . | X . . . | . . . x
Snare . . X . | . . X . | . . X . | . . X .     Snare . . . . | X . . . | . . . . | X . . x   Clap . . . . | X . . . | . . . . | X . . .
Clap  . . X . | . . X . | . . X . | . . X .     Hat   16ths, accent the swung "e" and "a"    SynB X . . x | . . x . | X . x . | . x . .
Organ X . x . | X . x . | X . x . | X . x .     (triplet version: 24 steps/bar, accent 4th of each 6)

NEO-SOUL (84; offsets matter more than steps)   FRENCH TOUCH / FILTER HOUSE (123)
Kick  X . . x | . . . . | . . X . | . x . .     Kick X . . . | X . . . | X . . . | X . . .  (909, sidechain everything)
Snare . . . . | X . . . | . . . . | X . . .  +6..+12 ticks late   Clap 5 & 13;  OHat steps 3,7,11,15 nudged 2-5 ticks early
Hat   x . x x | x . x . | x . x x | x . x .  ±3-6 ticks, vel 40-90; no global swing
```

| Card | BPM | Harmony (spelled) | Bass | Signature / instruments | Form | Sounds fake when |
|---|---|---|---|---|---|---|
| JB funk | 100–112 (conv.); swing MPC 54–58% | one chord: D9 vamp 8–16+ bars, bridge C9 (bVII9); Dm7–G9 Dorian | hook; root on 1, 16th syncopation, octaves, b7 | clean trebly guitar (hollow-body, P-90, Twin, no distortion), horn stabs ([Wikipedia](https://en.wikipedia.org/wiki/Funk)) | intro hits 4, vamp 16–32, bridge 8, drum break 8, vamp out | 100% quantize, distorted guitar, sustained horns |
| P-Funk | 95–108, MPC 56–60% | Em7–A9 Dorian vamps | Bootsy envelope-filter bass + Minimoog with glide | Worrell's clavinet, Minimoog, ARP strings ([Wikipedia](https://en.wikipedia.org/wiki/Funk)) | 5–10-min chant jams | synth bass without glide/filter |
| Disco | 118–122 | NI example: verse Em–Bm7–Am7–D→D#; chorus Em–G–A (i–III–IV); fifthless ([NI](https://blog.native-instruments.com/disco/)) | broken octaves, velocity 127 | strings, horns, Rodgers "chanks" on maj7/9 ([London Guitar Academy](https://www.londonguitaracademy.com/mastering-funk-guitar)) | strings intro 4 + guitar 4, V 8, pre 8, C 8 (brass), bridge 8 (drums+bass), final C 16 ([NI](https://blog.native-instruments.com/disco/)) | 909 + sidechain (that is French house), quiet hats |
| Motown | up 120–140, ballads 70–90 (conv.) | C–Am–F–G; C–C7–F–Fm; final-chorus key change | Jamerson chromatic runs and ghost notes ([Wikipedia](https://en.wikipedia.org/wiki/James_Jamerson)) | tambourine, claps, echo chamber, tape hit hard ([Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/)) | 2:30–3:00 verse-chorus, fade | 808 kick, sub bass, no tambourine, wide stereo |
| Stax / Southern soul | up 100–125; 12/8 ballads 50–70 | I–IV dom7 vamps, F7–Bb7–C7, plagal F→Fm→C | Dunn root-5th-octave | Hammond, Telecaster, unison horns; raw theatre room ([Wikipedia](https://en.wikipedia.org/wiki/Stax_Records)) | verse-chorus + testifying vamp-out | strings, Motown polish |
| Philly soul | 95–120; ballads 60–80 | Bbmaj7–Am7–Gm9–C9sus–Fmaj9 (conv.) | syncopated octave lines | MFSB strings, horns, vibes; Young's 16th sock cymbal ([Wikipedia](https://en.wikipedia.org/wiki/Philadelphia_soul)) | long intros, 5–7-min vamps | triads only, strings doubling the vocal |
| Gospel / shout | ballads 12/8; contemporary 70–100; shout "very fast" ([Wikipedia](https://en.wikipedia.org/wiki/Shout_(Black_gospel_music))) | F: Ab7→A7→Bb9sus→Bbmaj7; F–D7(b9#9#5)–Gm7–C7; Bb7–Bdim7–F/C; F7–F7/A–Bb–Bbdim7–C7 ([PianoGroove](https://pianogroove.com/blues-piano-lessons/gospel-passing-chords-substitutions/)) | chromatic walk-ups II→IV, II→V ([PianoGroove](https://pianogroove.com/?p=5342)) | piano, Hammond, choir; shout snare + clap on every upbeat | V-C-bridge-**vamp** modulating up by half steps, shout, tag | static triads, unison choir |
| Doo-wop | 12/8 ballads ~55–75; up 130–160 | C–Am–F–G (50s progression); C–Am–Dm–G ([Wikipedia](https://en.wikipedia.org/wiki/Doo-wop)) | bass singer ostinato | bass-to-falsetto group, nonsense syllables | spoken bridge | dense drums, synth pads |
| New jack swing | ~95–110 (104) | Cm9–Fm9–Abmaj7–G7#9 (conv.) | punchy FM/Minimoog bass on kick syncopations | SP-1200 + 808, giant gated snare, orchestra hits | pop form + rap break | straight hats, soft snare |
| Boogie / post-disco | 110–116 | Am9–Dm9–Gm9–C9sus | slap or synth bass ([Wikipedia](https://en.wikipedia.org/wiki/Boogie_(genre))) | LinnDrum/808 claps, Juno pads, talkbox | — | four-on-the-floor kick |
| 90s R&B / hip-hop soul | 85–100; slow jams 60–75 | m9/maj7 loops | boom-bap roots | sampled breaks under R&B singing ([Wikipedia](https://en.wikipedia.org/wiki/Hip_hop_soul)) | — | NJS swing (wrong era) |
| Neo-soul | ~70–95 (84) ([Orphiq](https://orphiq.com/resources/bpm-tempo-guide)) | **Bbm11–Gm9–Gbmaj13–Ebm11**; Bbm11 = Bb F Ab C Eb; G13sus = G C F A E; no ii–V–I ([PianoGroove](https://www.pianogroove.com/?p=21017)) | late, sparse, slides | Rhodes; mono saturated drums, piccolo-snare rimshot ([Reverb](https://reverb.com/news/video-dangelos-vibey-the-line-drums-whats-that-sound)) | one 4–8-bar loop, 4–7 min | quantized drums, triads, bright hats |
| Nu-disco / French touch | French 110–130 ([Wikipedia](https://en.wikipedia.org/wiki/French_house)); nu-disco median 122 | whatever the 2–4-bar sample holds | sampled or octave/slap riff | filtered disco loop, 909, sidechain, vocoder ([Splice](https://splice.com/blog/filter-house-history-ingredients-techniques)) | 8/16-bar ramps; LPF 75 Hz → 5–6 kHz → 19.9 kHz at drop ([NI](https://blog.native-instruments.com/french-house-music/)) | static unfiltered loop, EDM risers |
| Modern funk / city pop | 100–118; city pop 100–125 | royal road Fmaj7–G7–Em7–Am | synth bass with glide; slap | Dâm-Funk boogie revival; city pop AOR with maj7 ([Wikipedia: City pop](https://en.wikipedia.org/wiki/City_pop)) | — | trap hats, triads |

Two derived rules help a generator move between these styles. The first is a "soulify" ladder: triads → 7ths → 9ths on minor and dominant chords → V as 13sus or 7#9 → a chromatic dom7 approach chord before strong-beat targets → #IVdim7 between IV and I/5 → bass walk-ups. Gospel climbs the whole ladder. Neo-soul removes the cadences and loops colour chords, and funk collapses everything to one dom9 or m7. The second rule is about **interlock**: bass and guitar or clav rarely attack the same 16th except beat 1 in funk. Motown bass "weaves around" kick and snare ([Gearnews](https://www.gearnews.com/secrets-of-the-motown-sound-studio/)), and in funk every instrument, horns included, is used percussively ([Wikipedia: Funk](https://en.wikipedia.org/wiki/Funk)). The register map (convention) is bass E1–G2, scratch guitar E3–E5 on 3-7-9 top-string voicings, clav and Rhodes C3–C5, trumpets C4–C6 with sax and trombone an octave below, and violins C5–C7 doubled down an octave. FL stock mapping (convention): FPC for drums with a hat cut group, FL Keys for Rhodes and piano, FLEX for strings, brass, choir and organ, Sytrus/3x Osc for synth bass and FM EPs, BooBass as a bass fallback, Fruity Love Philter for filter sweeps, Fruity Limiter for sidechain, Vocodex for talkbox and vocoder, Fruity Squeeze for SP-1200 grit, and Fruity Blood Overdrive for glue. The family's fake tells are equal velocities, missing ghosts, bass doubling the kick exactly, modern 808 subs in retro styles, over-wide stereo on 1960s material, and horns or strings sustaining where stabs belong.

## Country and folk swap the rhythm cell and the lead timbre over the same I–IV–V

Country and folk share so much I–IV–V harmony that chords rarely identify the genre. Two things do: the **rhythm cell** (train beat, two-beat boom-chick, shuffle, 3/4 waltz, bluegrass chop, 6/8 jig, stomp four-on-the-floor or trap half-time) and the **signature lead** (steel plus fiddle for honky-tonk, strings plus choir for the Nashville sound, banjo roll plus mandolin chop with no drums for bluegrass, banjo loop plus 808 for country trap). The fastest genre flip is derived from this. G–C–D in two-beat with steel and fiddle is honky-tonk. The same chords with chop, banjo rolls and no drums at 170 BPM is bluegrass. With a four-on-the-floor stomp, claps and "hey!" it is stomp-clap folk, and with a banjo loop, half-time clap and 808 it is country trap.

Several identity and groove facts are sourced. Honky-tonk is "a two-beat rhythm with a crisp backbeat" in which "steel guitar and fiddle are the dominant instruments" ([Wikipedia: Honky-tonk](https://en.wikipedia.org/wiki/Honky-tonk)). The Bakersfield sound was the first country style built on electric instruments and a defined backbeat, with twin picked Telecasters ([Wikipedia: Bakersfield sound](https://en.wikipedia.org/wiki/Bakersfield_sound)). The Nashville sound replaced fiddles, steel and nasal vocals with strings, backing choirs and crooning ([Wikipedia: Nashville sound](https://en.wikipedia.org/wiki/Nashville_sound)). Bill Monroe's high mournful tenor set the "high lonesome" convention ([Britannica](https://www.britannica.com/biography/Bill-Monroe)). His **mandolin chop**, a chord muted right after the strum, gave bluegrass a harder groove than old-time, with bass on the on-beats and banjo in steady 8ths ([Wikipedia: Chop chord](https://en.wikipedia.org/wiki/Chop_chord)). Earl Scruggs' forward roll is a repeating 8th-note arpeggio that keeps time, with string order 2-1-5-2-1-5-2-1 ([Wikipedia: Banjo roll](https://en.wikipedia.org/wiki/Banjo_roll); [Deering](https://blog.deeringbanjos.com/the-four-essential-5-string-banjo-rolls)). Repeating a 3-note cell across 8 eighths produces the 3+3+2 accent grouping (derived). The **train beat** is steady 8ths or 16ths on snare with accents carried by the snare, most famously on Johnny Cash's "Folsom Prison Blues" and often played with brushes ([PAS](https://pas.org/pas-blog/country-music-grooves-variations-on-the-classics/)). Its guitar strum is D, D, U, D, U, D, U with accents on 2 and 4 ([Andy Guitar](https://andyguitar.co.uk/videos/lesson-7-acoustic-rhythm)). Boom-chicka puts the bass note on beat 1, a strum on 2 and "&2", the bass on 3, and a strum on 4 and "&4" ([AcousticLife](https://acousticlife.tv/guitar-strumming-patterns-the-boom-chicka/)). Travis picking alternates two thumb bass notes in steady 8ths while the fingers pick melody on or between them ([Guitar World](https://www.guitarworld.com/lessons/how-fingerpick-merle-travis)).

```
TWO-BEAT / BOOM-CHICK (honky-tonk ~120)         TRAIN BEAT (100-140, brushes)
Kick     X . . . | . . . . | x . . . | . . . .  Snare g g g g | X g g g | g g g g | X g g g
Snare    . . . . | X . . . | . . . . | X . . .  Kick  X . . . | . . . . | x . . . | . . . .
Bass     X . . . | . . . . | x . . . | . . . .  (root 1, fifth 3)   Gtr D . . . | D . U . | D . U . | D . U .
GtrStrum . . . . | x . x . | . . . . | x . x .

SHUFFLE (12-step, 100-150)                       COUNTRY WALTZ (3/4, 12 steps)
Ride  X . x | X . x | X . x | X . x              Kick X . . . | . . . . | . . . .
Snare . . . | X . . | . . . | X . .              Snare/brush . . . . | x . . . | x . . .   ("boom-chick-chick")
Kick  X . . | . . . | X . . | . . .              Bass X . . . | . . . . | . . . .  (root bar 1, fifth bar 2)

BLUEGRASS (~170, no drums)                       STOMP-CLAP FOLK CHORUS (~130)
Bass     X . . . | . . . . | x . . . | . . . .   Stomp X . . . | X . . . | X . . . | X . . .
MandChop . . . . | X . . . | . . . . | X . . .   Clap  . . . . | X . . . | . . . . | X . . .
Banjo    X . x . | x X . x | . x X . | x . x .   Tamb  x . x . | x . x . | x . x . | x . x .
         (continuous 8ths, 3+3+2 accents)        Shout . . . . | . . . . | . . . . | X . . .   ("hey!")
                                                 AcGtr X x x x | X x x x | X x x x | X x x x

COUNTRY TRAP, "OLD TOWN ROAD" MODEL (136-140)    COUNTRY RAP, "BAR SONG" MODEL (162 = felt 81)
Kick/808 X . . . | . . . x | . . x . | . . . .   Stomp X . . . | . . . . | X . . . | . . . .  (guitar-case kick)
Clap     . . . . | . . . . | X . . . | . . . .   Clap  . . . . | X . . . | . . . . | X . . .  (hallway gang claps)
Hat      x x x x | x x x x | x x x x | x x x x   AcGtr X . x x | . x x . | X . x x | . x x .  (16th strum)
Banjo    x . x . | x . x . | x . x . | x . x .   808   X . . . | . . . . | X . . . | . . . .  (added last)

TRAVIS PICKING (C)                               CELTIC JIG (6/8, 12 steps = 2 bars)     SLIP JIG 9/8: X . x X . x X . x
ThumbLow  X . . . | x . . . | X . . . | x . . .  Bodhran X . x x . x | X . x x . x
ThumbHigh . . x . | . . x . | . . x . | . . x .  Guitar  X . x X . x | X . x X . x
Finger    . . . x | . x . . | . . . x | . x . .  REEL (4/4): melody continuous 8ths; guitar X . . x . . x . (3+3+2 push)

INDIE FOLK 6/8 (12 steps = 2 bars)               OUTLAW "WAYLON" CHUG (~100, snare late)
FloorTom X . . x . . | X . . x . .               Kick X . . . | . . . . | X . . x | . . . .
Shaker   x x x x x x | x x x x x x               Bass X . . x | . . x . | X . . x | . . x .
Guitar   X . x x . x | X . x x . x               Gtr  x . x . | x . x . | x . x . | x . x .  (palm-muted, phaser)
```

The train-beat and two-beat stroke placements are sourced as described. The drum figures and the 6/8, outlaw and stomp grids are convention. In acoustic country and bluegrass, the drum kit's job is distributed across the band: the bass is the kick (1 and 3), the chop or strum is the snare (2 and 4), and the banjo or guitar is the hats. When programming without drums, keep those three layers' velocities distinct (derived).

| Card | BPM (conv. unless cited) | Harmony (spelled) | Lead / signature | Form | Sounds fake when |
|---|---|---|---|---|---|
| Honky-tonk / Bakersfield / neotrad | two-steps 100–170 (120); ballads 60–80; waltz 90–140 | G–C–G–D7–G; II7 turnaround G–A7–D7–G; keys G A C D E | steel + fiddle fills between vocal lines; Bakersfield picked Teles + slapback ([Fender](https://www.fender.com/articles/instruments/10-chart-topping-country-telecaster-players)) | 2–4-bar steel/fiddle intro, verse-chorus or AABA, steel-then-fiddle break, tag; ~2:30–3:00 | loud compressed drums, 808 lows, steel as a static pad |
| Outlaw / red dirt | 80–130 (100), laid back | E–D–A–E (I–bVII–IV), E–A–B7 | phaser/tremolo Tele, harmonica, gruff baritone | 3–4 min, live endings | too polished and layered |
| Bluegrass / old-time | 120–200 ([tunee.ai](https://www.tunee.ai/music-generator/bluegrass), weak); breakdowns 160–240 | G–C–G–D–G; "salty dog" G–E7–A7–D7–G; few 7ths | banjo roll, mandolin chop, fiddle, dobro, upright; trio harmony | kick-off 4–8, verse, trio chorus, one break per soloist, tag; AABB instrumentals | adding a drum kit, flat-velocity rolls (vary 70–110) |
| Nashville sound / countrypolitan | ballads 60–90 in 12/8; mid 100–120 | C–Am–Dm7–G7; C–C7–F–Fm–C; half-step key change | strings, choir "oohs", slip-note piano, tic-tac bass | AABA or V-C, 2:30–3:00 | steel/fiddle up front, triplets quantized to straight 16ths |
| Modern country pop | 70–110 (90); up 110–150 | G–D–Em–C; Em–C–G–D; add9 colour | acoustic 16th strum ×2 L/R + quiet mono copy, Tele answers, steel swells; 808s and snaps ([Whiskey Riff](https://www.whiskeyriff.com/?p=642128)) | intro 4–8, V 8–16, pre 4–8, C 8, post 4, V, pre, C, bridge 8, C ×2; ~3:00 | EDM drums with no acoustics, no twang vowels |
| Bro-country (2012–16) | 90–120 | I–V–vi–IV, power-chord choruses | rock guitars + banjo loop + clap loops ([Wikipedia](https://en.wikipedia.org/wiki/Bro-country)) | V-C-V-C-B-C ~3:15 | fiddle-forward (too trad) or fully EDM |
| Country trap / country rap | trap 130–160 half-time; "A Bar Song" 162 in A major ([Hit Songs Deconstructed](https://reports.hitsongsdeconstructed.com/?p=53620)) | A–E–F#m–D sing-along; or Am–F–G–Am trap loop | banjo/acoustic loop + trap drums + rap verse and belted hook ([Wikipedia](https://en.wikipedia.org/wiki/Country_rap)) | banjo intro 4–8, hook 8, verse 16, hook…; 2:30–3:00 | banjo loop with no other organic layer, 808 vs acoustic low end (HPF acoustics ~120 Hz) |
| Americana / alt-country | 60–130 | I–IV–V with vi, bVII, open drones | live band in a room, imperfect voice ([Wikipedia](https://en.wikipedia.org/wiki/Americana_(music))) | story songs, long outros | grid quantize, glossy tuning |
| Traditional folk (British/Irish/Appalachian) | rubato; dance 100–130+ | Mixolydian and Dorian dominate, pentatonic ([Emory](https://scholarblogs.emory.edu/americanroutes/?p=399)); D drone with D–C–D; Am–G–Am–D | solo voice, fiddle + clawhammer drone, dulcimer | strophic, 8–20+ verses | functional pop chords forcing a leading tone |
| Folk revival / singer-songwriter | 70–130 | I–IV–V; I–I/7–vi–IV descending bass | voice + acoustic (Travis or "old faithful" strum), harmonica | strophic or V-C, 3–6 min | identical strum velocity, pad layers |
| Indie folk | 60–120 (90), often 6/8 | sus2/add9, IV–I plagal, iv borrowed | breathy/falsetto stacks, reverb, piano, strings; Noah Kahan "Stick Season" UK No. 1 on 5 Jan 2024 ([Wikipedia](https://en.wikipedia.org/wiki/Noah_Kahan)) | slow builds, long fades | dense drums, hyped EQ |
| Stomp-clap folk-pop | 80–150 | 3–4 major chords, open tunings | foot stomps, claps, "hey/ho", banjo ([Rolling Stone AU](https://au.rollingstone.com/music/music-features/mumford-and-sons-lumineers-folk-stomp-74308)) | quiet intro → kick enters → gang chorus → breakdown → double-time final chorus | electronic claps, 808 kick |
| Celtic (Irish/Scottish) | reels "around 130" (beat unit unclear, [tunee.ai](https://www.tunee.ai/music-generator/celtic)); jigs 6/8 | session keys D and G Ionian, A and E Dorian ([Grey Larsen](https://greylarsen.com/revisions/minorchanges/p.26.pdf)); Em–D–Em–D; A–G–A–G–D–A | fiddle, whistle, pipes, bodhrán, DADGAD bouzouki/guitar ([Wikipedia](https://en.wikipedia.org/wiki/Gaelic_folk_music)) | **AABB 8-bar strains**, each tune ×3 in sets of 2–3 ([irishtune.info](https://www.irishtune.info/rhythm/reel-structure.html)) | ii–V harmony, jigs on a straight grid, vibrato everywhere |
| Acoustic fingerstyle | 70–140 | open chords, moving bass, harmonics | one guitar, Travis thumb bass ([MusicianWave](https://www.musicianwave.com/what-is-the-travis-picking-pattern-how-to-learn-it/)) | AABA or V-C | ringing palm-muted bass, same velocity everywhere |

Three idiom engines make the difference between country and "pop with a banjo sample". The first is the **Nashville Number System**, the right internal chord representation for the skill: chords as scale degrees, minor written 2- or 6-, a diamond meaning strike and hold, ">" meaning a push onto the "and" before the beat, and underlines grouping numbers in one bar ([Premier Guitar](https://www.premierguitar.com/pro-advice/the-nashville-number-system-demystified); [MusicianWave](https://www.musicianwave.com/nashville-number-system/)). A honky-tonk verse becomes `1 1 4 1 | 1 1 5 5 | 1 1 4 4 | 1 5 1 1` in any key (convention). The second is the **pedal steel**. Its pedals and knee levers raise or lower specific strings by exactly a half or whole step while other strings hold, giving in-tune bends, smooth portamento and chord vibrato ([Guitar Player](https://www.guitarplayer.com/lessons/how-to-mimic-the-sound-of-pedal-steel-on-electric-guitar); [NIME 2023](https://nime.org/proceedings/2023/nime2023_57.pdf)). In MIDI, put the moving voices on separate channels with different bend ranges so only some notes bend ([Yamaha Synth forum](https://yamahasynth.com/community/modx-series-synthesizers/pedal-steel-guitar-emulation)). The classic E9 "A+B pedal" move turns I into IV by holding the root while the 3rd rises a half step and the 5th a whole step (C-E-G → C-F-A), slid over about 150–300 ms with a volume-pedal fade-in (convention). Sampled steel libraries with sustain, harmonic, legato, vibrato and bend articulations exist ([Impact Soundworks](https://impactsoundworks.com/product/pedal-steel/?isw=4)). The third is **Celtic ornamentation**: cuts (very quick grace notes from above) and rolls (main note, cut, main, tap, main) are built into the tunes as articulations ([irishtune.info](https://www.irishtune.info/rhythm/reel-structure.html)), and ornamentation is a decisive stylistic marker ([Springer](https://link.springer.com/article/10.1007/s00799-019-00267-2)). Program cuts as 1/32 grace notes above the main note at lower velocity, and harmonise modal tunes with double-tonic I–bVII or i–bVII shifts to avoid a leading-tone clash (derived). A "country-sounding" topline (derived) is major pentatonic 1-2-3-5-6, a b3→3 slide on accented syllables, and phrase ends on 1 or 5 approached from 6 or 2.

Modern country's production has split into two documented models, and the skill should name which one it is using. The **"Old Town Road" model** is a sample loop over stock trap drums. YoungKio sped up a banjo sample from Nine Inch Nails' "34 Ghosts IV", used a tuned 808 as the bassline and layered pitched hi-hats over a plain clap, and the beat was sold on BeatStars for $30. It spent 19 weeks at No. 1 ([Songfacts](https://www.songfacts.com/facts/lil-nas-x/old-town-road); [Wikipedia: Country rap](https://en.wikipedia.org/wiki/Country_rap)). The **"A Bar Song" model** is organic first. Shaboozey's 2024 hit used 30+ acoustic guitar tracks, including Nashville high-strung. It blended a Splice fiddle loop with live fiddle and used no drum kit: programmed drums from the producers' own samples, guitar-case kick stomps, brushes and hallway gang claps. It added upright bass, piano and Farfisa/B3, put a mono acoustic bus under the panned guitars, used Valhalla Room for a saloon feel and lightly clipped the drum bus. **The 808 was added in the last month** ([Sound On Sound](https://www.soundonsound.com/techniques/inside-track-shaboozey-bar-song-tipsy)). It tied the all-time Hot 100 record of 19 weeks at No. 1 ([Billboard Canada](https://ca.billboard.com/music/chart-beat/shaboozey-record-no-1-hot-100)). Billboard frames 2025–26 as a country "rap revival" in which trap drums and 808s became a shared language ([Billboard](https://www.billboard.com/music/country/country-rap-crossover-hits-trend-1235983104/), snippet only, paywalled). A parallel folk and Americana camp went the other way, toward raw, minimally produced records ([PSU Collegian](https://www.psucollegian.com/opinion/columnists/why-noah-kahan-style-folk-music-has-returned-to-mainstream-column/article_28113a22-16e6-11ee-aed6-ffa1185dc0da.html)). The era tells follow (derived): strings and choir mean the 1960s, Tele plus slapback means Bakersfield, snaps and loops mean 2012–18 bro/pop, and an 808 with trap hats and a banjo loop means 2019–26 country trap.

## Latin, Caribbean and African music is carried by time-lines and anticipation

### Latin genres read from the percussion time-line first and the bass placement second

Almost every Latin genre is identified first by its percussion time-line (clave, güira or guacharaca scrape, surdo accent, tamborzão, oom-pah, 3-3-2) and second by where the bass sits. In the Afro-Cuban core the clave cells are sourced. Son clave 3-2 strikes on 1, 2&, 4 | 2, 3 of a two-bar cycle, and 2-3 swaps the bars. Rumba clave delays the third stroke by one pulse. Bossa clave delays the second note of the 2-side. The tresillo is the first three strokes ([Wikipedia: Clave](https://en.wikipedia.org/wiki/Clave_(rhythm))). The tresillo is also the basis of the **tumbao** bass in son, mambo, salsa and Latin jazz, which supplies harmony and pulse while avoiding a plain downbeat ([Wikipedia: Tumbao](https://www.wikipedia.org/wiki/Tumbao)). On piano the matching figure is the **montuno**, which can support or cross the clave with anticipations ([Piano With Jonny](https://pianowithjonny.com/piano-lessons/piano-montunos-the-complete-guide/)). The biggest fake tell across Afro-Latin styles (derived) is a downbeat-heavy kick or bass, because FL's beat-1 and four-on-the-floor defaults work against grooves carried by anticipation.

The grids use CYCLE16: one step is an 8th note, and the 16 steps are one full two-bar clave cycle, so **set FL to half the quoted BPM** (salsa quoted at 190 → FL 95).

```
CUBAN CORE (CYCLE16)
Son clave 3-2    X . . x | . . x . | . . x . | x . . .   (1,4,7 | 11,13)      sourced positions
Son clave 2-3    . . x . | x . . . | x . . x | . . x .   (bars swapped)
Rumba clave 3-2  X . . x | . . . x | . . x . | x . . .   (3rd stroke delayed)  sourced
Bossa clave      X . . x | . . x . | . . x . | . x . .   (2-side note delayed) sourced
Cascara 3-2      X . x x | . x . x | x . x . | x x . x   (convention; a sourced 7-stroke version conflicts)
Conga tumbao     H T S T | H T O O | H T S T | H T O O   (slap on 2, opens on 4 and 4&)
Bass tumbao      . . . x | . . X . | . . . x | . . X .   (2& and 4, note on 4 = NEXT chord root, tied; no beat 1)
Piano montuno    X . x x | . x . x | . x x . | x . x x   (octave-doubled, anticipating steps 15-16)

CHA-CHA (4/4, ~120)                              BACHATA (~125) - DERECHO verse / MAJAO chorus (sourced)
Cowbell X . . . | x . . . | X . . . | x . . .    Guira x . x . | x . x . | x . x . | x . x .    (all 8ths)
Guiro   X . . . | x . x . | X . . . | x . x .    Bongo X . x . | x . x . | X . x . | B . x .    (B = low hit, beat 4)
Conga   H . T . | S . T . | H . T . | O . O .    MAJAO: Guira X . . . | X . . . | X . . . | X . . . (long scrapes)
Bass    X . . . | . . . . | x . . . | . . x .           Bongo x . . . | x . . . | x . . . | B . . .
                                                 Bass  X . . . | . . x . | x . . . | . . x .
MERENGUE (~150)                                  CUMBIA (~95; guacharaca sourced)
Guira   X . x x | X . x x | X . x x | X . x x    Guacharaca X . x x | X . x x | X . x x | X . x x
Tambora x . S . | x . S . | x . S . | x x x x    Llamador   . . x . | . . x . | . . x . | . . x .
Bass    X . . . | . . . . | x . . . | . . x .    Bass       X . . . | . . x . | X . . . | . . x .   (root 1, fifth 3)
                                                 Kick (digital) X . . . | . . . . | X . . . | . . . .
SAMBA (4/4 grid = two 2/4 bars; FL BPM = surdo pulse)
Surdo 1a (low, THE accent) . . . . | X . . . | . . . . | X . . .
Surdo 2a (mark)            x . . . | . . . . | x . . . | . . . .
Pandeiro                   x g g X | x g g X | x g g X | x g g X
Tamborim                   X . x x | . x . x | X . x x | . x . x

BAILE FUNK / TAMBORZAO (130; funk 150 / mandelao 150) - convention
Kick 808  X . . x | . . x . | X . . x | . . x .   (3-3-2, distorted)
Atabaque  . . x . | . x . x | . . x . | . x . .
Clap      . . . . | x . . . | . . . . | x . . x

POLKA 2/4 (norteno, banda, corrido; FL 95-125)    VALS/RANCHERA 3/4 (12 steps)       HUAPANGO / SON JALISCIENSE (12 steps = two 6/8 bars)
Tuba/bass  X . . . | x . . . | X . . . | x . . .  Bass X . . . | . . . . | . . . .  Strum X . . X . . | X . X . X .  (6/8 then 3/4)
Bajo sexto . . x . | . . x . | . . x . | . . x .  Gtr  . . . . | x . . . | x . . .
Snare      . . x . | . . x . | . . x . | . . x x
CORRIDO TUMBADO: tuba/tololoche root-fifth + 12-string offbeat "charcheteo" chop + requinto 16th runs between lines; optional 808 and trap hats

TANGO (~120)                                     MOOMBAHTON (108)
Marcato X . . . | x . . . | X . . . | x . . .    Kick  X . . . | X . . . | X . . . | X . . .
3-3-2   X . . . | . . x . | . . . . | x . . .    Snare . . . x | . . x . | . . . x | . . x .  (dembow over four)
Arrastre (drag into next bar) . . . . | . . . . | . . . . | . . g x
```

Bachata's three section rhythms are sourced. In the **derecho** (verses), bongo and güira play all eight 8ths, the bongo accents 1, 3 and 4 with the lowest hit on 4. In the **majao** (choruses), both drop to the four downbeats with longer güira scrapes. The **mambo** is the instrumental break where the singer stops ([Ubisoft/Rocksmith](https://www.ubisoft.com/en-us/game/rocksmith/plus/news-updates/3DgS3IltlNGQk5RL2CvHgZ/breaking-down-bachata-part-2-percussion)). Cumbia's guacharaca plays a down-stroke on the beat then a quick down-up pair on the "&-a" ([Music Will PDF](https://jamzone.musicwill.org/wp-content/uploads/2021/04/Cumbia-Print-Lessons-2.pdf)). Merengue típico uses accordion, bass, güira, conga and tambora ([Wikipedia: Merengue típico](https://en.wikipedia.org/wiki/Merengue_t%C3%ADpico)). Vallenato's four "airs" are son and paseo in 2/4 and merengue and puya in 6/8, on accordion, guacharaca and caja ([Wikipedia: Vallenato](https://en.wikipedia.org/wiki/Vallenato)). Baile funk's bases are documented: Volt Mix at about 125–128 BPM, **tamborzão at about 130 BPM** (created 1998 by DJ Luciano Oliveira from candomblé, capoeira and maculelê atabaque figures plus 808 kicks), and the **150 BPM** movement from the mid-2010s ([Orphiq](https://orphiq.com/resources/what-is-baile-funk)). Tamborzão's sub is deliberately overdriven and its empty space is part of the beat ([Music Production Wiki](https://musicproductionwiki.com/articles/how-to-make-brazilian-funk)). Moombahton began in late 2009 when Dave Nada slowed a Dutch-house track from 128 to 108 BPM ([Wikipedia: Moombahton](https://en.wikipedia.org/wiki/Moombahton)). Norteño blends Mexican traditions with Central European polka and waltz on button accordion, bajo sexto and bass ([Wikipedia: Norteño](https://en.wikipedia.org/wiki/Norte%C3%B1o_(music))). Corridos tumbados pair sierreño guitars and tololoche or tuba bass with rapper styling, at usually 100–130 BPM in polka- or waltz-derived feels, with occasional 808s ([Beats To Rap On](https://beatstorapon.com/music/latin/corridos-tumbados)).

| Card | Quoted BPM (conv. unless cited) | Harmony (spelled) | Bass | Signature / DAW | Form | Sounds fake when |
|---|---|---|---|---|---|---|
| Son cubano | 85–120 (FL 43–60 CYCLE16) | I–IV–V7 vamps; Dm–F–Gm–A7 ("Chan Chan") | tumbao, tied anticipations | tres (guitar + octave layer), bongó martillo, maracas | largo 16–32 → montuno coro/pregón → trumpet solo | clave reversed against the melody, bass on downbeats |
| Salsa (dura/romántica) | 160–220; dura 180–210 (FL 80–105) | Am–Dm–E7; C–F–G–F; Dm7–G7 | tumbao | piano montuno in octaves, timbales cáscara→bell in montuno, 2–4 trumpets/trombones | canto 32–48 → coro-pregón 32+ → mambo 8–16 → moña → coro → cierre | four-on-floor kick, MIDI brass without breath |
| Mambo / cha-cha-chá | mambo 180–210; cha-cha 112–128 | I–V7, ii–V; dominant 6ths | cha-cha 1, 3, pickup 4& | charanga flute + violins (cha-cha, Jorrín, [Wikipedia](https://en.wikipedia.org/wiki/Cha-cha-cha_(dance))); big-band sax vs trumpet riffs (mambo) | — | any swing |
| Bachata | 120–140; modern 110–130 | C–F–G7; Am–Dm–E7; Am–F–C–G | syncopated 1, 2&, 3, 4& | chorus-drenched requinto arpeggios, güira, bongo | intro riff 4–8, V (derecho), C (majao), mambo break 8–16 | no derecho/majao switch, dry requinto, drum-kit backbeat |
| Merengue | 130–170 | C–G7 vamps; jaleo alternation | roots 1 and 3 + 4& pickup | tambora roll into beat 1, güira, alto saxes in 3rds | paseo → merengue → jaleo | too slow, missing tambora roll |
| Cumbia (Colombian, Mexican, villera, digital) | 80–110 ([Suno](https://suno.com/music-library/genres/cumbia), weak); Mexican 85–100 | C–G7; Am–G–F–E (Andean) | root-fifth bounce | guacharaca, llamador, accordion or Casio keys; digital = 808, dub delays ([Sounds and Colours](https://soundsandcolours.com/articles/argentina/classic-yet-modern-zzk-records-and-digital-cumbia-10942/)) | riff intro, V, C, riff break | kick on all four beats, scraper without the "&-a" flick |
| Vallenato | paseo 90–115; puya 120–170 in 6/8 | I–IV–V7 | root-fifth | button accordion ornaments, caja, guacharaca | — | piano-style accordion voicings |
| Bossa nova | 120–144 quarter = 60–72 in 2/4 | Fmaj7–G7(9)–Gm7–C7(b9); Gm7–Gb7–Fmaj7 | surdo-like root/fifth thumb | nylon guitar on upbeats ([Premier Guitar](https://www.premierguitar.com/rhythm-rules-brazilian-guitar-101)), whispered vocal | AABA/ABAC 32 | triads, loud kit, swing |
| Samba / pagode | pagode 90–110; enredo 130–150 | C–A7–Dm–G7; 7-string baixaria runs | surdo beat-2 accent | pandeiro, tamborim, cuíca, cavaquinho; partido alto ([Wikipedia](https://en.wikipedia.org/wiki/Partido_alto)) | coro + verses | beat 1 loudest, swing knob instead of hand-placed 16th drag |
| MPB | 70–130 | bossa-derived extended chords over regional rhythms (baião 3-3-2 zabumba) | — | nylon guitar, Rhodes | — | treating it as one groove |
| Baile funk / Brazilian funk | 125–128 / 130 / 150 ([Orphiq](https://orphiq.com/resources/what-is-baile-funk)) | often none; one-note "tuin" stabs | distorted 808 is the bass | chopped atabaque, chant hooks, montagem vocal chops | 2–3 min, hook-first, drops to silence | four-on-floor kick, clean mix |
| Sertanejo / agronejo | ballads 70–90; up 110–140 | G–D–Em–C | — | duplas in 3rds, viola caipira, sanfona ([O Povo](https://www.opovo.com.br/vidaearte/2023/07/24/conheca-a-origem-do-sertanejo-universitario.html)) | pop form | single unharmonised vocal |
| Tango / electrotango | tango 110–130; electrotango 95–125 | Am–Dm–E7–Am; G#dim7; Am–Am/G#–Am/G–Am/F# | marcato on beats | bandoneon, violins, piano; marcato, síncopa, arrastre ([Yale Globalist](https://globalist.yale.edu/?p=4172)); Gotan Project ([Equipboard](https://equipboard.com/band/gotan-project)) | — | swing, rock backbeat, static bandoneon |
| Norteño / banda / mariachi / tumbados | polka 95–125; tumbados 100–130 ([Beats To Rap On](https://beatstorapon.com/music/latin/corridos-tumbados)) | C–F–G7 with D7; Am–Dm–E7; Am–G–F–E7 | tuba/tololoche oom | accordion in 3rds; banda brass with charchetas; mariachi violins/trumpets/vihuela/guitarrón; tumbado requinto | corrido = strophic 4-line stanzas with requinto breaks | rock drums, strums on downbeats, rigid requinto |
| Latin trap | 130–150 half-time (conv.) | Am–F–E7, Phrygian | gliding 808 | trap kit + nylon/flamenco guitar, dembow switch in chorus ([Wikipedia](https://en.wikipedia.org/wiki/Latin_trap)) | rap form | — |
| Latin pop | 90–105 | Am–G–F–E or I–V–vi–IV | — | dembow-lite percussion, nylon guitar, bilingual hooks | pop form | — |
| Moombahton / Latin house | 108 ([Wikipedia](https://en.wikipedia.org/wiki/Moombahton)) / 122–126 | — | — | Dutch-house leads over dembow; Latin house = house + conga tumbao, montuno, timbales | DJ form | — |

Three Latin production currents dominate 2025–26. Bad Bunny's *DeBÍ TiRAR MáS FOToS* weaves salsa, bomba and reggaetón. It became the first Spanish-language album to win Grammy Album of the Year (1 February 2026), and its salsa sits inside a wider salsa resurgence across Luis Fonsi, J Balvin, Rauw Alejandro and Karol G ([Guinness World Records](https://www.guinnessworldrecords.com/world-records/782166-first-spanish-language-album-to-win-a-grammy-award-for-album-of-the-year); [Consequence](https://concerts.consequence.net/articles/bad-bunny-wins-2026-grammy-album-of-the-year)). Peso Pluma, the corridos tumbados pioneer, was No. 7 in Spotify Wrapped 2025's global top 10 with 11.6 billion streams ([SDP Noticias](https://www.sdpnoticias.com/espectaculos/musica/orgullo-mexicano-un-artista-aparece-entre-los-mas-escuchados-del-mundo-en-spotify-wrapped-2025/)). Brazilian funk was Spotify's fastest-growing genre to clear $100M in payouts in 2025, with about half of the average artist's streams from abroad ([Bloomberg Línea](https://www.bloomberglinea.com/estilo-de-vida/funk-brasileno-desbanca-al-k-pop-como-el-genero-que-mas-crece-en-spotify/)). #brazilianphonk posts grew 62% in Europe between February and May 2026, as a hybrid of automotivo, montagens, bruxaria and international phonk ([Billboard Brasil](https://billboard.com.br/brazilian-phonk-crescimento-global-tiktok-funk/)). Several stroke-level grids here (cáscara, partido alto, tamborzão, tambora, tango síncopa) are unverified conventions and should be checked against a method book or a reference loop before being treated as canon.

### Jamaican and Eastern Caribbean styles split on where the kick meets the skank

Jamaican styles are told apart by where the kick lands relative to the offbeat skank. Reggae came from ska and rocksteady in the late 1960s, and rocksteady (about 1966–68) was "slower than ska" with less prominent horns ([Wikipedia: Reggae](https://en.wikipedia.org/wiki/Reggae); [Wikipedia: Rocksteady](https://en.wikipedia.org/wiki/Rocksteady)). The one-drop family is sourced. The **one drop** puts kick and snare on beat 3 with beat 1 empty. **Rockers** adds a steady kick on every quarter, and **steppers** a kick on every eighth ([Wikipedia: One drop rhythm](https://en.wikipedia.org/wiki/One_drop_rhythm)). Roots reggae runs at **70–90 BPM** ([Orphiq](https://orphiq.com/resources/what-is-dancehall)) with hats usually swung or shuffled ([wayneandwax](https://www.wayneandwax.com/org/lessons/roots-riddim-tutorial.html)). One counting conflict needs resolving. A FruityLoops tutorial places the drop on beats 2 and 4, which is the same groove counted at double tempo (about 150 versus 75 BPM). The recommendation is to program at 70–80 BPM with the drop on step 9 (derived). Dancehall (85–110 BPM) drops the one drop for a programmed syncopated kick with rim or snare answering off the beat. Its bass is a short repeated synth figure that is often the main hook, harmony is minimal, and the middle is left empty for the voice ([Orphiq](https://orphiq.com/resources/what-is-dancehall)). Wayne Smith's "Under Mi Sleng Teng" (1985) is the landmark digital riddim ([Wikipedia](https://en.wikipedia.org/wiki/Under_Mi_Sleng_Teng)). Soca was created by Lord Shorty as the "Soul of Calypso" ([Wikipedia: Soca](https://en.wikipedia.org/wiki/Soca_music)). Power soca runs about 160 BPM and groovy soca about 115 ([NYS Music](https://nysmusic.com/2023/08/30/the-birth-and-evolution-of-soca-music/)), and St Lucia's competition rules cap groovy at 130 ([RCI St Lucia](https://rcistlucia.com/?p=11784)). Zouk, pioneered by Kassav', was originally **120–145 BPM**, and zouk-love "gradually became indistinguishable from compas" ([Wikipedia: Zouk](https://en.wikipedia.org/wiki/Zouk)). Kompa's defining feature is a consistent pulsating tanbou beat ([Wikipedia: Compas](https://en.wikipedia.org/wiki/Compas)).

```
SKA (110-135; hats 55-60% swing)                 ROCKSTEADY (80-105)
Kick  X . . . | . . . . | X . . . | . . . .      Kick  . . . . | . . . . | X . . . | . . . .
Snare . . . . | X . . . | . . . . | X . . .      Rim   . . . . | X . . . | . . . . | X . . .
Skank . . X . | . . X . | . . X . | . . X .      Skank . . . . | X . . . | . . . . | X . . .
Bass  X . . . | x . . . | x . . . | x . . .      Bass  . . X . | . . x . | X . . . | x . x .   (melodic, leaves holes)

ONE DROP (~75)                                   ROCKERS                          STEPPERS
Hat   x . x . | x . x . | x . x . | x . x .      Kick X . . . | X . . . | X . . . | X . . .   Kick X . X . | X . X . | X . X . | X . X .
Rim   . . . . | . . . . | X . . . | . . . .      Rim  . . . . | . . . . | X . . . | . . . .   Rim  . . . . | . . . . | X . . . | . . . .
Kick  . . . . | . . . . | X . . . | . . . .      Hat  16ths, accent offbeats
Skank . . . . | X . . . | . . . . | X . . .
Organ . . x g | . . x g | . . x g | . . x g      ("bubble")
Bass  . . . . | . . X . | X . . x | . . x .      (rests on 1, lands with the drop)

DANCEHALL: DEMBOW FAMILY                          DIWALI-STYLE CLAP (2002)          MODERN (2015-26)
Kick  X . . . | X . . . | X . . . | X . . .       Kick X . . . | . . X . | X . . . | . . X .   Kick X . . x | . . X . | X . . . | . . X .
Snare . . . x | . . X . | . . . x | . . X .       Clap X . . X | . . X . | X . . X | . . X .   Rim  . . . . | X . . x | . . . . | X . . .
                                                                                     Hat 16ths + 1/32 rolls; 808 follows kick
POWER SOCA (~158)                                GROOVY SOCA (~120)                ZOUK-LOVE (~85)
Kick  X . . . | X . . . | X . . . | X . . .      Kick X . . x | . . X . | X . . x | . . X .   Kick X . . . | . . . . | X . . . | . . . .
Snare . . . . | X . . x | . . . . | X . x .      Clap . . . . | X . . . | . . . . | X . . .   Snare . . . . | X . . . | . . . . | X . . .
Iron  X . x x | X . x x | X . x x | X . x x      Perc tassa/dholak-style 16ths                Rim  X . . X | . . X . | X . . X | . . X .
OpHat . . o . | . . o . | . . o . | . . o .
KOMPA (~105): Kick X . . . | . . . . | X . . . | . . . . ; tanbou . . . . | . . X . | . . . . | . . X x ; bell X . X X | . X X . | X . X X | . X X .
CALYPSO (100-130): boom-chick-a strum X . x X | . x X . | X . x X | . x X . ; bass root then 5th on "&2"
BOUYON (150-170): four-on-floor + 16th scraper + 1-2-bar 16th keyboard ostinato
```

| Card | BPM | Harmony | Bass | Signature | Sounds fake when |
|---|---|---|---|---|---|
| Ska | 110–135 (2 Tone 140–170) | Bb–Gm–Eb–F | walking quarters | every-offbeat skank, unison horns ([Wikipedia](https://en.wikipedia.org/wiki/Ska)) | long sustained pads |
| Rocksteady | 80–105 | F–Dm–Gm–C; I–IV–V–IV | melodic, gaps | soul harmony groups | ska tempo |
| Roots reggae | 70–90 ([Orphiq](https://orphiq.com/resources/what-is-dancehall)) | Am–Dm, Am–G, G–D–Em–C | melodic lead, rests on 1 | skank 2 & 4, organ bubble, 2 guitars, congas ([Wikipedia](https://en.wikipedia.org/wiki/Reggae)) | kick on beat 1, straight hats |
| Dub | 70–90 | as reggae | loudest element, dry | console as instrument, Space Echo, spring ([Wikipedia: Dub](https://en.wikipedia.org/wiki/Dub_music)) | static mix with no mutes or throws |
| Lovers rock | 68–85 | Fm7–Bb7–Ebmaj7–Cm7 | reggae | sweet soul vocals, London 1970s ([Wikipedia](https://en.wikipedia.org/wiki/Lovers_rock)) | — |
| Dancehall | 85–110 ([Orphiq](https://orphiq.com/resources/what-is-dancehall)) | Cm–Ab–Bb, one-chord vamps, stabs | short synth-bass hook | deejay toasting, riddim culture ([Wikipedia: Riddim](https://en.wikipedia.org/wiki/Riddim)) | pads, one drop |
| Calypso | 100–130 | C–F–G7–C | root + "&2" fifth | narrative vocal, horns ([Wikipedia](https://en.wikipedia.org/wiki/Calypso_music)) | — |
| Soca power / groovy | ~160 / ~115 ([NYS Music](https://nysmusic.com/2023/08/30/the-birth-and-evolution-of-soca-music/)) | I–V–vi–IV, synth brass | offbeat pump | iron (brake drum), crowd-instruction hook | swing (soca is straight) |
| Zouk / zouk-love | 120–145 ([Wikipedia](https://en.wikipedia.org/wiki/Zouk)) / 75–95 | Am–F–C–G, maj7/add9 | — | horn party (classic); tresillo rim roll (love) | — |
| Kompa | ~95–120 (105) | C–Am–Dm–G | anticipates next chord | chorus guitar arpeggio, bell cadence | — |
| Bouyon | 150–170 | major 2–3-note riffs | — | jing ping, lapo kabwit, frantic keys ([Wikipedia](https://en.wikipedia.org/wiki/Bouyon_music)) | — |

Dub is mixing as performance, and its methods are sourced. King Tubby and Lee Perry treated the console as an instrument with the Roland Space Echo among the core tools ([Wikipedia: Dub](https://en.wikipedia.org/wiki/Dub_music)). Spring reverb, tape delay and analogue effects are the core of the style ([Attack Magazine](https://www.attackmagazine.com/technique/tutorials/dub-style-drum-processing-for-character-and-groove/)). The essential move is hitting the delay aux on the last snare of a phrase while muting the drum group, so the mix drops to bass and guitar, with the spring return high-passed and filtered ([Attack Magazine](https://attackmagazine.com/?p=95750)). The FL dub rig is derived from those methods. Send A is Fruity Delay 3 at 3/16 or 1/4 with 50–70% feedback, a 300 Hz low cut and 3–5 kHz high cut in the feedback path, and light Blood Overdrive. Send B is Fruity Convolver with a spring IR, high-passed at about 400 Hz. Automate throws on the last snare or skank of each phrase and insert mutes for 2–8 bars, and push feedback above 90% briefly for runaway echoes. Keep the bass dry, mono and loudest. Version culture means one riddim gets a vocal mix, an instrumental version, a dub and a deejay cut.

### African styles separate on guitar language and kick placement

The African band styles split by guitar language and the electronic Southern African styles by kick placement. Fela Kuti's Afrobeat fused highlife, jùjú and Yoruba traditions with jazz and soul ([Wikipedia: Afrobeat](https://en.wikipedia.org/wiki/Afrobeat)). Tony Allen, the only band member Fela did not write parts for, played different things with all four limbs ([Wikipedia: Tony Allen](https://en.wikipedia.org/wiki/Tony_Allen_(musician))) and described **five major Afrobeat patterns, all in 4/4** ([Rolling Stone](https://www.rollingstone.com/music/music-news/tony-allen-afrobeat-drum-patterns-unseen-doc-clip-993318)). Highlife's arpeggiated guitar is modelled on the Afro-Cuban guajeo, with attack points nearly identical to the **3-2 clave**, a bell pattern indigenous to Ghana. Its two-finger picking came from Liberian Kru sailors ([Wikipedia: Highlife](https://en.wikipedia.org/wiki/Highlife)). Jùjú added talking drums in 1948 and later pedal steel ([Wikipedia: Jùjú](https://en.wikipedia.org/wiki/J%C3%B9j%C3%BA_music)). Franco turned the **sebene** from a short bridge into the centre of Congolese music, and guitar roles split into lead, mi-solo and rhythm ([Wikipedia: Soukous](https://en.wikipedia.org/wiki/Soukous); [Wikipedia: Congolese rumba](https://en.wikipedia.org/wiki/Congolese_rumba)). Mbalax rests on Wolof sabar drumming and the tama talking drum ([Wikipedia: Mbalax](https://en.wikipedia.org/wiki/Mbalax)). Gqom (Durban, early 2010s, usually 120–130 BPM) is identified by **broken kicks rather than four-on-the-floor**, with sourced kick families: broken/two-step, three-step, sgubhu/four-step, distorted "taxi kick" and uThayela. It has no log drum, which separates it from amapiano ([Orphiq: gqom](https://orphiq.com/resources/what-is-gqom)). Kwaito is "house with the tempo pulled down" to about 100–110 BPM ([Orphiq: kwaito](https://orphiq.com/resources/what-is-kwaito)). Kuduro runs at about 140–150 BPM with pounding syncopated kicks (weakly sourced) ([Wikipedia: Kuduro](https://en.wikipedia.org/wiki/Kuduro)). Afroswing is "largely defined by its melody rather than a specific tempo", and **the snare lands on the third beat** rather than the fourth, with a recurring three-note grouping inside 4/4 ([Wikipedia: Afroswing](https://en.wikipedia.org/wiki/Afroswing)).

```
AFROBEAT (95-130; convention from the four-limb description, not a transcription)
Hat       x x o x | x x o x | x x o x | x x o x
Kick      X . . . | . . X . | . . X . | . . . x
Snare     g . g . | X . g g | . g . g | X . g .
TenorGtr  x x . x | . x x . | x . x x | . x . x   (muted high single notes, 2-bar loop)
RhythmGtr . . X . | . . . X | . . X . | . . . X   (short chops)
Bass      X . . x | . . X . | . X . . | X . . .   (2-bar riff for minutes)

HIGHLIFE (clave placement derived from sourced 3-2 relationship)   SOUKOUS SEBENE / CAVACHA (125-160)
Bell  X . . X | . . X . | . . X . X . . .                         Kick  X . . . | X . . . | X . . . | X . . .
Gtr1  X . x X | . x X . | x . X . X x . x                         Snare x x X x | x x X x | x x X x | x x X x
Gtr2  . x . . | x . . x | . x . x . . x .                         Bass  X . . X | . . X . | X . . X | . . X .
Bass  X . . X | . . X . | X . . . | X . . .

GQOM BROKEN (120-130)                  KWAITO (100-110)                  KUDURO (140-150)                 AFROSWING (95-110)
Kick X . . . | . . X . | . . . . | . . X .  Kick X . . . | X . . . | X . . . | X . . .  Kick X . . X | . . X . | X . . X | . . X .  Kick  X . . X | . . X . | . . . . | X . . .
Tom  . . . . | . . . . | . x x x | x . . .  Clap 5 & 13; OpHat every "and"    Clap 5 & 13; sirens/whistles     Snare . . . . | . . . . | X . . . | . . . .
Clap . . . . | X . . . | . . . . | . . . .  Bass X . . X | . . X . | . X . . | X . X .                          Rim   . . . X | . . X . | . . . X | . . X .
ETHIO-JAZZ 12/8 (12 steps): Kick X . . | . . x | X . . | . . x ; Snare on 4 and 10; Bass X . x | . X . | X . x | . X .
```

Ethio-jazz blends pentatonic Amharic melodies with jazz harmony and vibraphone ([Wikipedia: Ethio-jazz](https://en.wikipedia.org/wiki/Ethio-jazz)). It is built on four **qenet** modes: tizita, bati, ambassel and anchihoye. They are pentatonic with characteristically long intervals and are untempered on traditional instruments ([Wikipedia: Qenet](https://en.wikipedia.org/wiki/Qenet)). Sources disagree on some spellings, so the skill should store them with a flag. Tizita major is C D E G A ([Chromatone](https://chromatone.center/theory/scales/ethiopian/)). Ambassel is C Db F G Ab per Wikipedia ([Wikipedia: Ambassel](https://en.wikipedia.org/wiki/Ambassel_scale)) but C D Eb G Ab ("minor") per Chromatone. Anchihoye is C Db F F# A per one guitar reference ([guitarcomposerstoolbox](https://guitarcomposerstoolbox.com/guitar-scales/c-anchihoye/)) but C D Eb G Ab per Chromatone. Bati major is C D F G A per Chromatone. Tizita, meaning memory or nostalgia, is used for slow emotive songs ([Chromatone](https://chromatone.center/theory/scales/ethiopian/)). For the "Yègellé Tezeta" sound, use ambassel or tizita minor over a single Cm or C5 so the pentatonic gaps carry the colour (derived).

| Card | BPM (conv. unless cited) | Harmony | Signature | Form | Sounds fake when |
|---|---|---|---|---|---|
| Afrobeat (Fela) | 95–130 | Dm7 or Dm7–G7 Dorian for minutes; horns in 4ths/octaves | interlocking muted tenor + chop guitars, unison horns, busy hats | 10–20+ min: instrumental build drums→bass→guitars→keys→horns, head, solos, vocal call-response | quantized, velocity-flat percussion |
| Highlife | 100–135 | G–C–D–G in 1–2-bar cycles, 3rds/6ths | clave-shaped arpeggios, horns | — | — |
| Jùjú | 95–120 | I–IV–V, 1–2 chords | talking drum (pitch envelope per hit), pedal steel | long medleys | — |
| Rumba / soukous | rumba 100–120; sebene 125–160 | E–A–B vamps | high looping sebene lead, mi-solo, cavacha snare | two-part: vocal rumba → fast sebene, 6–10 min | — |
| Mbalax | 110–140, 12/8 implied | — | sabar + tama phrases cutting across a pop band | — | — |
| Gqom | 120–130 ([Orphiq](https://orphiq.com/resources/what-is-gqom)) | one dark chord, chant samples | broken kick, tom rolls, no log drum | long repetition | four-on-floor kick |
| Kwaito | 100–110 ([Orphiq](https://orphiq.com/resources/what-is-kwaito)) | 2–4-chord loops | slow four, fat synth bass, township chants | — | — |
| Kuduro | 140–150 (weak) | — | tresillo kick, sirens, shouts | — | — |
| Afro-house roots | ~118–124 | modal minor | from kwaito, mbaqanga, deep/soulful house; House Afrika label 1994 ([Wikipedia](https://en.wikipedia.org/wiki/Afro_house)) | — | — |
| Bongo flava | 95–115; singeli 200–300 (unsourced) | — | Swahili R&B, taarab melisma; "bongopiano" amapiano fusion ([Wikipedia](https://en.wikipedia.org/wiki/Bongo_Flava)) | — | — |
| Ethio-jazz | 6/8 at 100–130; tizita ballads 60–80 | i–iv or i–bVI under qenet | vibraphone, organ, horns, Mulatu Astatke | — | — |
| Afroswing | 95–110 | happy or dark chords (Steel Banglez, [Wikipedia](https://en.wikipedia.org/wiki/Afroswing)) | snare on 3, melodic London rap | — | snare on 4 |
| Alté | 80–110 | maj9/min11 | hazy lo-fi afro-R&B, Tems, Odunsi ([Wikipedia](https://en.wikipedia.org/wiki/Alt%C3%A9)) | — | — |

The common fake tells across Caribbean and African styles are derived from the definitions above. They are quantized, velocity-flat percussion; long sustained pads where the style uses short chops; a busy kick where the genre is defined by kick absence (one drop) or kick irregularity (gqom); and the wrong swing, since reggae hats need a shuffle while soca and kuduro are straight. Era mix targets are convention: 1960s ska mono-ish and mid-forward; roots and dub bass-heavy with spring and tape; digital dancehall dry and sparse; modern soca and dancehall loud; 1970s Afrobeat and highlife warm, bleedy and less loud.

## Asian, South Asian and Middle Eastern pop is decided by scale system and drum language

### Maqam needs microtuning only in four families, and FL can do it per note

Middle Eastern styles are built from **maqamat** assembled from 3–5-note cells (ajnas). A maqam has a lower and an upper jins; the upper jins' first note (ghammaz) is the second most important note, and maqam families are classified by the lower jins ([Wikipedia: Arabic maqam](https://en.wikipedia.org/wiki/Arabic_maqam)). Most musicians agree on at least eight main ajnas: rast, bayati, sikah, hijaz, saba, kurd, nahawand and ajam ([Wikipedia: Arabic music](https://en.wikipedia.org/wiki/Arabic_music)). Four map cleanly to Western equal temperament: 'Ajam is approximately major, Nahawand minor, Kurd Phrygian, and Hijaz Phrygian dominant (Hijaz Kar is double harmonic) ([Wikipedia: Arabic maqam](https://en.wikipedia.org/wiki/Arabic_maqam)). Rast, Bayati, Saba and Sikah need "half-flat" notes. The 24-tone quarter-tone grid is a notational convention, real intonation is finer, and Saba's opening contains seconds of about 160 and 140 cents ([Wikipedia: Arabic maqam](https://en.wikipedia.org/wiki/Arabic_maqam)). Turkish makam theory divides the octave into 53 commas, so Turkish accidentals that look like quarter tones are comma shifts ([Wikipedia: Turkish makam](https://en.wikipedia.org/wiki/Turkish_makam)). Phrygian dominant is the single most pan-regional colour. It is Hijaz, klezmer Freygish, Persian Homayun, and appears in flamenco, Balkan and Indian music ([Wikipedia: Phrygian dominant](https://en.wikipedia.org/wiki/Phrygian_dominant_scale)). Mizrahi pop, notably, used Arabic instruments with "typically Western" intonation and no quarter tones ([Wikipedia: Mizrahi music](https://en.wikipedia.org/wiki/Mizrahi_music)).

FL Studio has no native Scala tuning in the sources checked, but it can handle microtones note by note. The piano roll's per-note **Fine pitch** ranges −1200 to +1200 cents in 10-cent steps ([Image-Line forum](https://forum.image-line.com/viewtopic.php?p=1966980)). The piano-roll scripting API exposes `pitchofs` in tenths of a semitone ([FL scripting API](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/pianoroll_scripting_api.htm)). Sytrus supports microtuning via envelope files, while users still request .scl/.tun and maqam presets ([Image-Line forum](https://forum.image-line.com/viewtopic.php?p=2017165)). A half-flat is therefore the natural note with Fine pitch −50 cents. The spellings below are derived from the jins definitions (maqam pages at [maqamworld](https://www.maqamworld.com/en/maqam/rast.php)).

| Maqam | Spelling ("½" = −50 cents) | 12-TET safe? | Western neighbour |
|---|---|---|---|
| Rast | C D E½ F G A B½ C (descending often Bb) | no | — |
| Bayati | D E½ F G A Bb C D | no | — |
| Saba | D E½ F Gb A Bb C | no | — |
| Sikah | E½ F G A B½ C D | no | — |
| Hijaz | D Eb F# G A Bb C D | yes | Phrygian dominant |
| Kurd | D Eb F G A Bb C D | yes | Phrygian |
| Nahawand | C D Eb F G Ab B C (descending Bb) | yes | harmonic/natural minor |
| 'Ajam | Bb C D Eb F G A Bb | yes | major |
| Hijaz Kar | C Db E F G Ab B C | yes | double harmonic |

The skill should default to 12-TET-safe maqamat for pop contexts (Arabic pop, arabesk, Mizrahi, Bollywood "exotic" lines). It should use −50 cents only on the half-flat degrees of Rast, Bayati, Saba or Sikah tracks, and approximate Turkish koma degrees at −20 to −40 cents (derived). Quarter-tone maqamat are harmonised sparsely, with drones and open fifths, because full triads clash (derived). The skill also needs three non-maqam scale systems. Indian ragas are defined by scale, vadi/samvadi and pakad, grouped into ten Hindustani thaats ([Wikipedia: Raga](https://en.wikipedia.org/wiki/Raga)). The conventional mapping is Bilaval = Ionian, Kalyan = Lydian, Khamaj = Mixolydian, Kafi = Dorian, Asavari = Aeolian, Bhairavi = Phrygian, and Bhairav = C Db E F G Ab B. The J-pop **royal road** is IVmaj7–V7–iii7–vi7, in C Fmaj7–G7–Em7–Am7, with variants IVmaj7–V7–III7–vi7 and a full chain resolving through ii7–V7–I ([Wikipedia: Royal road progression](https://en.wikipedia.org/wiki/Royal_road_progression)). East Asian pentatonics are convention: Chinese gong C D E G A and yu A C D E G; Japanese yonanuki major C D E G A, yonanuki minor A B C E F, and in-scale E F A B C.

### Dum-tek cycles, talas and the bhangra chaal, as grids

Arabic rhythmic cycles (iqa'at) number about 100 ([Wikipedia: Iqa'](https://en.wikipedia.org/wiki/Iqa%27)). Dum is the low centre stroke, tek the high rim stroke and ka the weaker other-hand rim ([Wikipedia: Baladi](https://en.wikipedia.org/wiki/Baladi)). The stroke patterns below are sourced ([BabaYagaMusic](https://www.babayagamusic.com/Music/oriental-dance-rhythm-diagrams-and-descriptions.htm); [Wikipedia: Baladi](https://en.wikipedia.org/wiki/Baladi); [Wikipedia: Tsifteteli](https://en.wikipedia.org/wiki/%C3%87iftetelli)). Gulf rhythms are polyrhythmic, played by several drums at once, so single-drum versions are approximations. Teentaal is 16 matras with claps on 1, 5 and 13 and the "wave" on 9 ([Wikipedia: Teental](https://en.wikipedia.org/wiki/Teental)). Keherwa is 8 matras with sam on 1 and khali on 5 and is used in film songs ([Wikipedia: Keherwa](https://en.wikipedia.org/wiki/Keherwa)). The bhangra **chaal** is a 4/4 rhythm with each beat divided in three, a "booma-chicka" long-short ([Vaia](https://vaia.com/en-us/explanations/punjabi/punjabi-music/punjabi-rhythm-patterns)). Its grid below is derived from that description, since no notated source was found. Map dum to a darbuka low or tuned 808 blip, tek to darbuka tek, rim or snap, and ka to a rim ghost at 40–60% velocity, and every rhythm here becomes programmable on the Channel Rack (derived).

```
MAQSUM (4/4; pop 90-110, shaabi/mahraganat 120+)   BALADI / MASMOUDI SAGHIR           SAIDI
Dum  X . . . | . . . . | X . . . | . . . .        Dum X . X . | . . . . | X . . . | . . . .   Dum X . . . | . . X . | X . . . | . . . .
Tek  . . x . | . . x . | . . . . | x . . .        Tek . . . . | . . x . | . . . . | x . . .   Tek . . x . | . . . . | . . . . | x . . .
Ka   . . . . | g g . . | . . g g | . . g g        Ka  . . . . | g g . . | . . g g | . . g g

MALFUF (2/4 3+3+2, written twice)    KHALEEJI (3+3+2 at quarter scale)    AYYUB (2/4, zar)
Dum  X . . . | . . . . | X . . . | . . . .   Dum  X . . . | . . X . | . . . . | . . . .   Dum X . . . | X . . . | X . . . | X . . .
Tek  . . . x | . . x . | . . . x | . . x .   Tek  . . . . | . . . . | . . . . | x . x .   Tek . . . g | . . x . | . . . g | . . x .
                                              Claps x . . . | . . x . | . . . . | x . . .  (2-3 layers offset 5-15 ms)
CHIFTETELLI (8/4 = 2 bars; slow; last beat silent)
Bar1 Dum X . . . | . . . . | . . . . | . . . .   Tek . . . . | . . x . | . . . . | x . . .
Bar2 Dum X . . . | X . . . | . . . . | . . . .   Tek . . . . | . . . . | x . . . | . . . .

PERSIAN 6/8 (12 steps = one bar in 16ths)        TURKISH 9/8 (2+2+2+3, 9 eighths)
Dum  X . . . . . | X . . . . .                    Dum X . . . X . . . .
Tek  . . . . x . | . . x . x .                    Tek . . x . . . x . x

TEENTAAL (16 matras, 1 step = 1 matra)            KEHERWA (8 matras; filmi plays it as one 4/4 bar)
Bols dha dhin dhin dha | dha dhin dhin dha | dha tin tin ta | ta dhin dhin dha
Bass (bayan) on dha/dhin; none on tin/ta (khali)  Bass   X . x . | . . . . | . . . . | x . . .
Tali X . . . | x . . . | o . . . | x . . .        Treble . . . . | x . x . | x . x . | . . x .

BHANGRA CHAAL (12 steps = 4 beats x triplet)      FILMI DHOLAK (keherwa feel)
Dhol dagga (bass)   X . . | . . x | X . . | . . x Bass   X . . x | . . X . | X . . x | . . X .
Dhol tilli (treble) x . x | x . x | x . x | x . x Treble . x x . | x x . x | . x x . | x x . x
Pop layer: Kick X . . | . . . | X . . | . . . ; Clap on beats 2 and 4
```

Players swing tek and ka slightly late, so apply light swing or 5–15 ms late offsets to ka ghosts (convention). Distinguishing by ear (derived): maqsum has a single dum then "tek-tek"; baladi has two dums at the start; saidi has dums pushing into beat 3; malfuf and Khaleeji have a 3+3+2 lilt, with Khaleeji slower and clap-heavy; chiftetelli is a slow 8-beat sway with a silent last beat; Persian is a 6/8 gallop; and bhangra is a triplet dhol bounce.

### Two to four signature timbres do the identity work in each region

Each region has two to four signature timbres. Khaliji uses rebab, oud, violin, mirwas, tabl and duff ([Wikipedia: Khaliji](https://en.wikipedia.org/wiki/Khaliji_(music))). Egyptian al jeel paired oud, qanun, ney and violin with "almost always" a Roland TR-707 ([Wikipedia: Al Jeel](https://en.wikipedia.org/wiki/Al_Jeel)). Mahraganat is synths, a DAW, darbuka, sagat and heavy Auto-Tune ([Wikipedia: Mahraganat](https://en.wikipedia.org/wiki/Mahraganat)). Bhangra's dhol is played with two sticks alongside tumbi, sarangi and dholak ([Wikipedia: Bhangra](https://en.wikipedia.org/wiki/Bhangra_(music))). The tumbi is a single high metal string over a gourd ([Wikipedia: Tumbi](https://en.wikipedia.org/wiki/Tumbi)). The qanun has 26 courses of three strings with a range of about A2–E6 ([Wikipedia: Qanun](https://en.wikipedia.org/wiki/Qanun_(instrument))). The emulation rules are convention. The key Arabic and Turkish texture is **heterophony**: all melody instruments play the same line with individual ornaments, and the violin section plays in unison and octaves, not in harmony. **Harmonising the melody in thirds is the most common fake giveaway.** Other emulation defaults: oud with slides, mordents and 32nd tremolo and no strummed chords; qanun in octaves with trills; ney with breath noise and glides; darbuka with dum, tek, ka, slap and 32nd rolls at falling velocity; tabla with the bayan "ge" glide via slide notes; dhol dagga plus tilli with a kick under dagga and a clap under tilli in pop; tumbi high (around MIDI 72–84) with short decay; sitar meend up to ±2 semitones; a tanpura drone on Sa–Pa; erhu slides between pentatonic notes; and guzheng glissandi that stay pentatonic. Stock FL synths cannot fake plucked or bowed microtonal ornaments convincingly, so use dedicated sample libraries.

| Card | BPM (conv. unless cited) | Scale / harmony | Rhythm | Signature | Form | Sounds fake when |
|---|---|---|---|---|---|---|
| K-pop | 95–130 (120); club sub-styles 130–145 | minor 2–4-chord loops Am–F–C–G; i–bVI–bVII; final chorus +1/+2 semitones | section-specific: trap verse, four-floor chorus, Jersey/2-step | layered synths, 808s, EDM risers, stacked vocals ([Tunee](https://tunee.ai/music-generator/korean), weak) | intro 4–8, V 8–16, pre 8, C 8–16, post 8, V2, pre, C 16, bridge 8, **dance break 8**, final C 16; 2:45–3:30 | one groove for the whole song, no dance break |
| J-pop | ballads 70–90; main 120–150; anime 150–180 | royal road; IVmaj7–III7–vi7–v7–I7 (Fmaj7–E7–Am7–Gm7–C7); secondary dominants | band 8th rock-pop | live band + strings/brass | intro, A 8, B 8, sabi 8–16, A, B, sabi, C-melo/ōsabi 8, final sabi often key-raised ([Yakuaru](https://posts.yakuaru.com/Common%20Japanese%20Song%20Composition%20Terminologies%20%E3%82%B5%E3%83%93%20%E8%90%BD%E3%81%A1%E3%82%B5%E3%83%93%20A%E3%83%A1%E3%83%AD%201%E7%95%AA%20%E3%83%95%E3%83%AC%E3%83%BC%E3%82%BA%20and%20others)) | only a 4-chord loop, no B-melo lift, trap sub |
| City pop | 95–125 (110), swing 52–55% | maj7, m9, dom13, dim passing ([Wikipedia](https://en.wikipedia.org/wiki/City_pop)) | 16th hats, snare 2 & 4 | Rhodes/DX7, CS-80, CZ-101, TR-808, slap bass | verse-pre-chorus ×2, sax solo | trap hats, triads |
| Anime song / J-rock | 160–200 (180) | minor royal road, bVI–bVII–i climbs | double-time fills, half-time breaks | distorted guitars, strings/brass hits | TV size ≈ 89–90 s: intro 4, A 8, B 8, sabi 16 | slow tempo, quiet vocals |
| Vocaloid / net music | 130–200+ | royal road, rapid modulation | rock 8ths or four-floor, glitches | Vocaloid 6 / Synthesizer V voice ([Wikipedia](https://en.wikipedia.org/wiki/Vocaloid)) | J-pop form, short intros | flat robotic pitch everywhere |
| Mandopop / zhongguofeng | ballads 65–85 (72); R&B 80–100 | pentatonic melody over diatonic chords ([Wikipedia](https://en.wikipedia.org/wiki/Mandopop)); Canon I–V–vi–iii–IV–I–IV–V | ballad backbeat; half-time R&B | piano, strings; erhu, guzheng, pipa | V–pre–C ×2, bridge, final C up | non-pentatonic 4th/7th on strong beats in "Chinese-style" songs |
| Bollywood / filmi | romantic 70–90; dance 100–130 | raga-coloured minor, i–VII–VI–VII, Bhairav for drama | keherwa (dadra 6/8 for ghazal) | playback singers ([Wikipedia](https://en.wikipedia.org/wiki/Filmi)), tabla/dholak, strings, sitar | mukhda–interlude–antara 1–mukhda–antara 2–mukhda ×2 | Western I–V–vi–IV with a sitar sample on top |
| Bhangra | modern 95–110 (chaal triplets) | drone or i–VII, Mixolydian/Dorian | chaal | dhol + tumbi + shouts; UK scene since the 1970s ([Wikipedia](https://en.wikipedia.org/wiki/Bhangra_(music))) | tumbi intro 4, V 8, C 8, dhol break | straight 16ths, tabla instead of dhol |
| Punjabi pop / hip hop | 80–105 | minor 2–4-chord loops, guitar arpeggios | trap or dancehall kit + chaal layer | 808, dhol one-shots, tumbi ([Spotify](https://newsroom.spotify.com/tag/punjabi-101)) | hook-first, 2:30–3:30 | generic trap with no Punjabi inflection |
| Indian classical (fusion basis) | vilambit 30–60, madhya 60–120, drut 120–300+ matras/min | one raga, no chords | tala | tanpura drone, sitar, tabla | alap → bandish → improvisation → tihai on sam | chord changes, missing drone |
| Arabic pop / al jeel | 90–120 (100) | Hijaz D–Eb–D; i–bVII–bVI; sparse chords | maqsum or baladi | oud, qanun, ney, violin section, darbuka, riq | lazma riff 8, V 8–16, C 8, lazma, V2, C, taqsim/mawwal, C | Western changes every bar, string harmony in 3rds |
| Khaleeji | ~95–110 | Bayati/Rast/Hijaz/Saba, sparse | Khaleeji 3+3+2 | layered handclaps, oud, mirwas, tabl | group-clapped chorus | straight 8ths, missing claps |
| Mahraganat | 120–140 (130) | one-chord Hijaz/minor riff | maqsum with doubled rolls ([Wikipedia](https://en.wikipedia.org/wiki/Mahraganat)) | extreme Auto-Tune, sirens, shouted MCs | 4–6-min loops | clean mix, slow tempo |
| Turkish pop / arabesk | arabesk 70–90; pop 100–125; 9/8 dances | Hicaz, Kürdi, Uşşak, Nihavend; comma-based ornaments | chiftetelli, 9/8 | bağlama, string orchestra ([Wikipedia](https://en.wikipedia.org/wiki/Arabesque_(Turkish_music))) | string intro, verse, chorus | string harmony, no ornaments |
| Persian pop | 6/8 dance 120–140; ballads 65–80 | Shur (koron 2nd ≈ −40 to −50 c), Homayun ≈ Hijaz, Mahur ≈ major | 6/8; Bandari faster ([Wikipedia](https://en.wikipedia.org/wiki/Bandari_music)) | santur, tar, tombak, LA-era DX7 synths ([Wikipedia](https://en.wikipedia.org/wiki/Persian_pop_music)) | intro riff, V, C, santur solo | 4/4 dance beat with Persian vocals |
| Mizrahi | 95–125 | Freygish/Hijaz, **12-TET** | chiftetelli or maqsum + pop kit | oud, kanun, darbuka, bouzouki ([Wikipedia](https://en.wikipedia.org/wiki/Mizrahi_music)) | verse-chorus + bouzouki breaks | quarter-tone tuning (wrong for the style) |
| Uzbek pop | 100–130; 6/8 dances | Phrygian, Hijaz, Dorian; i–VII–VI | doira patterns | doira, rubab, dutar, sato ([Wikipedia](https://en.wikipedia.org/wiki/Music_of_Uzbekistan)) | tempo-up lazgi-style finale | Arabic maqsum instead of doira |

K-pop's production model explains its collage form. Melodies are composed overseas, especially in Sweden, refined by US producers and recorded in Seoul, and agencies run multi-day song camps ([Korea Times](https://www.koreatimes.co.kr/amp/entertainment/k-pop/20260317/composed-in-sweden-recorded-in-korea-k-pop-production-goes-global)). For the skill this means planning 8-bar modules that can each change drum style, signalling transitions with a riser or one-bar stop, putting the dance break after chorus 2, and raising the final chorus a semitone (derived). J-pop differs by ear (derived). It has denser chord changes, a sabi that often opens the song, band timbres and many syllables per bar. K-pop has 2–4-chord loops, beat-driven sections, abrupt genre switches and chant hooks. The global proof points are recent. "Golden" from *KPop Demon Hunters* became only the second UK No. 1 by a South Korean act ([Music Week](https://www.musicweek.com/talent/read/with-the-return-of-bts-and-golden-still-top-10-is-k-pop-set-for-another-blockbuster-year-in-the-uk/093318)). Rosé and Bruno Mars' "APT." was YouTube's top song of 2025 ([Gulf News](https://gulfnews.com/amp/story/entertainment%2Fmusic-rewind-2025-from-apt-to-golden-these-songs-defined-2025-1.500393086)). Yoasobi's "Idol" was the first Japanese song to top Billboard's Global Excl. US chart ([Wikipedia: J-pop](https://en.wikipedia.org/wiki/J-pop)). Kenshi Yonezu's "Kick Back" was the first Japanese-language song certified RIAA gold ([Wikipedia: Anime song](https://en.wikipedia.org/wiki/Anime_song)). Punjabi pop reached Coachella, Fallon and the Canadian Hot 100 in 2024 by fusing dhol with trap, afrobeat and dancehall grooves ([Furtados](https://furtadosschoolofmusic.com/blog/why-punjabi-pop-is-now-a-worldwide-phenomenon/)).

## Classical, film, game and experimental music are rule systems rather than grooves

### Each era has a harmonic fingerprint a generator can enforce

Concert and screen music swaps the drum grid for rules about harmony, texture, form and performance data. The era fingerprints are well sourced. **Baroque** (1600–1750) runs on basso continuo, with a chord instrument realising a figured bass over cello, bass or bassoon ([Wikipedia: Figured bass](https://en.wikipedia.org/wiki/Figured_bass)). It formalised key-centred tonality ([Wikipedia: Baroque music](https://en.wikipedia.org/wiki/Baroque_music)), and its harmony moves continually "without a sense of arrival". The **Classical** era (c. 1730–1820) favoured brief four-bar phrases, homophony over Alberti-type accompaniment and strong tonic-dominant contrast ([Wikipedia: Classical period](https://en.wikipedia.org/wiki/Classical_period_(music))). Alberti bass is a broken chord ordered lowest–highest–middle–highest ([Wikipedia: Alberti bass](https://en.wikipedia.org/wiki/Alberti_bass)). **Romantic** music adds chromaticism, the expanded orchestra, Berlioz's idée fixe and Wagner's leitmotif ([Wikipedia: Romantic music](https://en.wikipedia.org/wiki/Romantic_music)). It also adds chromatic mediants: C major's are E, A, Eb and Ab major, rare before the Romantics ([Wikipedia: Chromatic mediant](https://en.wikipedia.org/wiki/Chromatic_mediant)). Neo-Riemannian P, R and L moves (C↔Cm, C↔Am, C↔Em; hexatonic pole C↔Abm) describe late-Romantic chromaticism ([Wikipedia: Neo-Riemannian theory](https://en.wikipedia.org/wiki/Neo-Riemannian_theory)). The Tristan chord is F–B–D#–G# ([Wikipedia: Tristan chord](https://en.wikipedia.org/wiki/Tristan_chord)). **Impressionism** uses whole-tone and pentatonic scales, unresolved 9th/11th/13th chords shifted in parallel ("planing") and ambiguous tonality ([Wikipedia: Impressionism in music](https://en.wikipedia.org/wiki/Impressionism_in_music)). John Williams' "Rebel Fanfare" is a planing example ([Wikipedia: Parallel harmony](https://en.wikipedia.org/wiki/Planing_(music))). **Minimalism** is repetition, drones, consonance and process: Riley's *In C* (1964, 53 modules), Reich's phasing, and Glass's additive 1, 1 2, 1 2 3 ([Wikipedia: Minimal music](https://en.wikipedia.org/wiki/Minimal_music)). Clapping Music made the phase shift immediate ([Wikipedia: Phase music](https://en.wikipedia.org/wiki/Phase_music)). Einaudi-style **modern piano** pairs "arpeggiated repetition in the left hand and melodic motifs in the right", prefers natural minor ([Pianist Magazine](https://www.pianistmagazine.com/blogs/how-to-play-contemporary-classical-piano/)), and Nils Frahm mixes pianos with a Juno-60, Rhodes and drum machines ([Wikipedia: Nils Frahm](https://en.wikipedia.org/wiki/Nils_Frahm)).

| Style | Tempo (conv.) | Harmony (spelled) | Texture / rhythm | Form | Sounds fake when |
|---|---|---|---|---|---|
| Baroque | Allegro 100–132, Adagio 50–70 | circle of fifths C–F–B°–Em–Am–Dm–G–C; lament Dm–Am/C–Gm/Bb–A; Pachelbel D–A–Bm–F#m–G–D–G–A | 16th harpsichord figuration over walking 8th continuo; terraced dynamics | binary AABB, ritornello, fugue (exposition, episodes, stretto, [Wikipedia](https://en.wikipedia.org/wiki/Fugue)), ground bass | crescendos and pads, wide vibrato, 7th/9th colour, missing continuo |
| Classical | Allegro 120–150, Andante 70–90, Minuet ~120–140 in 3/4 | C–F–C/G–G7–C; antecedent I–ii6–V / consequent I–IV–V7–I; Am–Dm–E7–Am | Alberti `C G E G` 16ths; 4+4 periods | sonata, minuet & trio, rondo, variations | unresolved extended chords, phrases without cadences |
| Romantic | 50–70 to 140+, rubato ±5–10% | C–Ab–F–G; C–E mediant; Cm–Db/F–G7–Cm (Neapolitan); Tristan → E7 | wide nocturne LH spans in 12/8; tremolo strings | expanded sonata, symphonic poem, leitmotif networks | static velocity and CC, metronomic timing |
| Impressionist | 50–90, rubato | planing Cmaj9–Dmaj9–Emaj9; whole-tone C+ ↔ D+; Gmaj7–Dmaj7 | pedalled washes, free arpeggios; harp, flute, celesta | loose ABA, 3–6 min | V–I cadences everywhere, quantized arps, dry sound |
| Serial / sound-mass | free | 12-tone row with P/I/R/RI ([Wikipedia: Serialism](https://en.wikipedia.org/wiki/Serialism)); clusters (Penderecki's *Threnody* for 52 strings, [Wikipedia](https://en.wikipedia.org/wiki/Threnody_to_the_Victims_of_Hiroshima)) | pointillistic or massed; no grid | through-composed | accidental tonal triads, steady pulse |
| Minimalism | 100–200 pulse | Am–F; Am–Dm–F–E; slow change | Clapping Music cell `X X X . X X . X . X X .` (12/8), copy shifted 1 step every N repeats; Glass 3-vs-4 | additive/phase process, 5–60+ min | changing too much too fast |
| Neoclassical / modern piano | 60–90 | Am–C–Em–F (Einaudi "Experience" transposed, snippet-level); Am–F–C–G | LH 8th arpeggio root–5th–octave–10th; felt piano with mechanical noise | intro motif 8 → A 16 → A' + strings 16 → climax 16 → strip back 8 | quantized full-velocity piano, too many chord changes |

### Film styles map affects onto specific harmonic devices

Film music's emotional devices are specific enough to encode. Frank Lehman's *Hollywood Harmony* frames non-functional "pantriadic" chromaticism as film's main route to **wonder** ([Tufts](https://as.tufts.edu/music/people/faculty/frank-lehman)). **Lydian**'s #4 pulls up to 5 and is "the sound directors reach for when they want awe rather than triumph", but only if the harmony does not imply the key a fifth below ([Mark Slater](https://markslater.net/unlocking-the-power-of-the-lydian-mode/)). Ostinato "propels scenes that lack dynamic visual action" ([Wikipedia: Ostinato](https://en.wikipedia.org/wiki/Ostinato)). Zimmer's *Inception* circles a four-chord theme without resolving over an insistent ostinato ([MFiles](https://www.mfiles.co.uk/reviews/hans-zimmer-inception.htm)), and *Dunkirk* stacks Shepard tones for an endless rise ([Kottke](https://kottke.org/18/05/hans-zimmers-clever-use-of-the-shepard-scale-in-dunkirk)). Horror relies on sul ponticello and glissando ([Bradford College](https://digitalspace.bradfordcollege.ac.uk/10626277/?p=5408)) plus clusters, col legno and aleatoric textures. Scores are built from cues timed to picture via SMPTE, with leitmotifs per character ([Wikipedia: Film score](https://en.wikipedia.org/wiki/Film_score)), and Mickey Mousing syncs music to on-screen action ([Wikipedia: Mickey Mousing](https://en.wikipedia.org/wiki/Mickey_Mousing)).

| Cue type | Tempo (conv.) | Harmony | Texture / grid | Cue form | Sounds fake when |
|---|---|---|---|---|---|
| Orchestral adventure (Williams lineage) | marches 110–130; wonder 70–90 | Lydian #4; C–Ab–Bb–C; C–E lift; C–Fm for poignancy; mediant shift every 4 bars | horn theme with 4ths/5ths and triplet pickups; march `X . x x` ×4 on snare/strings; timpani 1 & 3 | intro hit → theme → development → climax → button | theme only in strings, everything legato |
| Horror | unmetered or 50–70 heartbeat `X . . X \| . . . . \| X . . X \| . . . .` | tritones, minor-2nd clusters, C↔Abm hexatonic pole, Phrygian | sul pont, col legno, tremolo, glissando, waterphone, sub drone MIDI 24–36 | long build → false calm (silence) → stinger → tail | melodic minor themes, constant loudness |
| Tension / thriller | 90–140 16th ostinato, accents `X . . x \| X . . x \| X . x . \| X . x .` | minor/Phrygian pedal, i–bII, Shepard rise, unresolved sus | spiccato, ticking percussion, low brass, synth arps | escalate a layer every 4–8 bars, cut to silence | resolving to major, melody too prominent |
| Emotional drama | 55–80 | 4–3 and 9–8 suspensions; IV–I; C–G/B–Am–F; borrowed Fm in C | solo cello/oboe/piano over strings; no drums | solo intro → theme → full strings → retreat, 2–3 min | identical CC curves on every part |
| Hybrid / "Zimmer-style" | 60–80 half-time or 120–140 ostinato | one 4-chord minor loop (Am–F–C–G); root-5th power voicings | 3-3-2 cello/synth ostinato `X . . X \| . . X . \| X . . X \| . . X .`; taiko; braams; organ | layer every 8 bars: pad 8 → ostinato 8 → perc 8 → brass theme 16 → peak 8 → cut | too many chords, thin lows |

The Shepard rise for tension is derived. Use three copies of a rising chromatic line an octave apart and crossfade them every 8-bar loop, so the top copy fades out while the bottom fades in. For horror clusters, stack 6–12 semitones across string divisi, ramp CC1 from 0 to 127 over 8 bars, and detune layers by 10–25 cents (convention).

### Games add loop seams and stems; chiptune adds hard voice limits

Game music's defining constraint is that it must loop and adapt. Looping is its most common form ([Wikipedia: Video game music](https://en.wikipedia.org/wiki/Video_game_music)). Horizontal resequencing switches between segments, vertical layering fades stems in and out ([Wikipedia: Adaptive music](https://en.wikipedia.org/wiki/Adaptive_music)), and hybrids are common ([Game Developer, GDC 2021](https://www.gamedeveloper.com/game-platforms/hybrid-horizontal-vertical-structure-for-game-music-composers-from-spyder-to-sackboy-gdc-2021-)). The skill's template is derived. Write a pickup that plays once plus a loop body of 8–32 bars whose last bar leads back to bar 1. Copy reverb tails from the end under the start so the seam is clean. Keep every layer in the same key and progression, with loop lengths of 1, 2, 4 or 8 bars that divide the master length. Export each Mixer track as a stem, plus 1–2-bar transition stingers and an ending. RPG defaults (convention) are field 90–120, town 80–100 and battle 140–180 BPM, with a bVI–bVII–I victory cadence (Ab–Bb–C) and an i–bVI–bVII–i battle loop (Am–F–G–Am).

**Chiptune** has hard, sourced voice limits. The NES 2A03 offers two pulse channels with four duty cycles (12.5, 25, 50, 75%), a stepped triangle with no volume control, LFSR noise and 1-bit DPCM, and most games used only four channels ([Wikipedia: Ricoh 2A03](https://en.wikipedia.org/wiki/Ricoh_2A03)). Game Boy and C64 SID differ in channel layout, and quick arpeggios stand in for chords ([Wikipedia: Chiptune](https://en.wikipedia.org/wiki/Chiptune)). In Mega Man-style roles, the pulses carry melody and harmony or an offset echo, the triangle plays bass and pitched toms, and noise plays percussion. One writer built this in FL Studio with a triangle waveform rather than FamiTracker ([DDRKirby(ISQ)](https://ddrkirby.com/articles/nes-chiptunes-unlock-everything/nes-chiptunes-unlock-everything.html)). Magical 8bit Plug 2 is a free emulator with duty, pitch and volume envelopes and an arpeggiator ([KVR](https://www.kvraudio.com/product/magical-8bit-plug-by-ymck)). The FL recipe (derived) is four monophonic channels at 120–180 BPM. Pulse 1 leads at 25% duty, Pulse 2 plays harmony or a 1/8–3/16 echo copy at lower volume, the triangle plays the bass in 8ths with octave jumps, and noise plays drums (kick as a short burst or a triangle drop from MIDI 48 to 36 in about 50 ms, snare 80–120 ms, hats 20–40 ms). Arpeggiate chord tones at 1/32–1/64 and use no reverb. Polyphonic pads, reverb and more than four or five voices sound fake.

The experimental cards are short because their rules are negative. **Drone** is "the sustained tone branch of minimalism" ([Wikipedia: Drone music](https://en.wikipedia.org/wiki/Drone_music)). Hold one pitch or open fifth for the whole piece and automate filter and LFO with 30–120 s periods. **Dark ambient** uses evolving dissonant drones and processed found sound ([Wikipedia: Dark ambient](https://en.wikipedia.org/wiki/Dark_ambient)). **New age** aims at relaxation, with Cadd9–Fadd9 Lydian or Mixolydian vamps, long reverbs and no tension ([Wikipedia: New-age music](https://en.wikipedia.org/wiki/New-age_music)). **Musique concrète** (Schaeffer, 1940s) transforms recorded "sound objects" with loops, speed change, reversal and splicing ([Wikipedia: Musique concrète](https://en.wikipedia.org/wiki/Musique_concr%C3%A8te)). In FL that means Edison and Slicex. **Noise** runs from Russolo's 1913 manifesto to Merzbow and harsh noise wall ([Wikipedia: Noise music](https://en.wikipedia.org/wiki/Noise_music)): distortion chains on noise generators, limited for safety.

### Orchestral realism is a data problem: ranges, divisi and controller curves

Orchestral MIDI succeeds or fails on performance data more than notes. In Spitfire's convention, CC1 crossfades sampled dynamic layers (timbre plus volume), CC11 is volume only, and CC21 controls vibrato ([Spitfire](https://support.spitfireaudio.com/en/articles/11816091-what-is-the-difference-between-dynamics-vibrato-and-expression)). Legato patches sample real interval transitions, keyswitches sit below the playable range, octave doublings should be played in separately rather than copy-transposed, and random humanise is less convincing than real performance ([Sound On Sound](https://www.soundonsound.com/techniques/sampled-orchestra-part3)). String practical ranges are violin G3–C7, viola C3–C6, cello C2–C5 and double bass E1–G3 ([Soundhouse](https://www.soundhouse.co.jp/en/contents/column/index?post=2830), snippet). The rest of the range table is standard orchestration convention, in MIDI (sounding).

| Instrument | Full | Sweet spot | Instrument | Full | Sweet spot |
|---|---|---|---|---|---|
| Violin | 55–103 | 55–93 | Horn in F | 34–77 | 41–74 |
| Viola | 48–88 | 48–81 | Trumpet Bb | 52–84 | 55–81 |
| Cello | 36–81 | 36–72 | Tenor trombone | 40–72 | 40–67 |
| Double bass | 28–67 | 28–55 | Bass trombone | 34–67 | 34–62 |
| Flute | 60–96 | 62–91 | Tuba | 26–65 | 28–58 |
| Oboe | 58–93 | 60–86 | Timpani (4) | 38–57 | — |
| Clarinet Bb | 50–94 | 50–89 | Harp | 23–104 | — |
| Bassoon | 34–75 | 36–69 | Choir S/A/T/B | 60–81 / 53–74 / 48–69 / 40–62 | — |

The performance recipe is convention, built on the sources above. For long notes, velocity sets the attack and CC1 draws phrase arcs (for example 40→90→55), while CC11 handles fades in the 90–127 range. For short notes, velocity carries the dynamics: 95–110 on downbeats and 70–85 on offbeats. Overlap legato notes by 10–40 ms. Put keyswitches one tick before the note. Humanise timing ±5–15 ms and velocity ±5–10. Space chords wide at the bottom with no 3rds below about MIDI 48, double the melody at the octave, and split chords into divisi tracks rather than playing 3–4 notes into one ensemble patch. One workspace-specific constraint matters. The fl-studio-mcp piano-roll tools queue notes only, so CC1, CC11 and CC64 must arrive through automation clips or an imported MIDI file (mido `control_change`) (derived from the tool description). Classical bar templates are convention: a binary dance is 8+8 with repeats (32 bars); sonata exposition 40–80, development 30–60, recap 40–80, coda 8–20; rondo ABACA with 8–16-bar refrains. Binary form modulates to the dominant in major or the relative major in minor ([Wikipedia: Binary form](https://en.wikipedia.org/wiki/Binary_form)), and sonata form recapitulates the second subject in the tonic ([Wikipedia: Sonata form](https://en.wikipedia.org/wiki/Sonata_form)). For film hit points, set BPM = 60 × beats ÷ seconds between hits, or insert a 2/4 bar so hits land on downbeats (derived).

## Fusion works as "carrier plus colour", and 2024–2026 rewarded it

### The hits keep one genre's engine intact and swap only the surface layers

Hit fusions of 2019–2025 follow one pattern. They keep an authentic rhythmic engine from one scene and take the melody, form and vocal from mainstream pop, country or K-pop. "Old Town Road" put country imagery over a trap beat and spent 19 weeks at No. 1 ([XXL](https://www.xxlmag.com/lil-nas-x-old-town-road-removed-billboard-country-chart/)). Shaboozey's "A Bar Song (Tipsy)" tied that record, led Hot Country Songs for 23+ weeks and earned Grammy nominations in both country and rap fields, without star remixes ([Billboard Canada](https://ca.billboard.com/music/chart-beat/shaboozey-record-no-1-hot-100)). Tyla's "Water" set amapiano log drums and piano runs under a pop/R&B topline, peaked at No. 7 on the Hot 100 and won the first Grammy for Best African Music Performance. Grammy.com's line that it was "the first African song to enter the Hot 100 since 1968" is loosely worded, because Nigerian hits charted earlier ([Grammy.com](https://grammy.com/news/tyla-winner-best-african-music-performance-water-2024-grammys-meaning)). NewJeans' "Ditto" put Baltimore-club rhythm under a soft K-pop topline ([Wikipedia: Ditto](https://en.wikipedia.org/wiki/Ditto_(song))). Bad Bunny's album pairs Puerto Rican traditional styles with urbano production ([PBS](https://www.pbs.org/newshour/arts/bad-bunny-wins-album-of-the-year-at-the-2026-grammy-awards-making-history-for-a-spanish-language-album)). Splice/MIDiA's 2025 download data attributes pop's comeback to "genre-blending styles", with bedroom pop up 297% ([MIDiA](https://midiaresearch.com/sounds-of-2026)).

No academic study of why fusions succeed or fail was found, so the method below is producer convention distilled from those cases. **The carrier-plus-colour rule** says to pick one carrier genre that sets the tempo band, the kick/snare grid and the bass type. The second genre contributes at most two or three of these: harmony, lead or hook instrument, vocal style, lyrical imagery, or one signature sound (cowbell, log drum, bed squeak, steel guitar, accordion, dhol). **Tempo bridging** joins genres through half-time and double-time relations: 70↔140 (trap and drill ↔ UK garage and dubstep), 85↔170 (hip hop ↔ DnB), 100↔200 (Jersey club over 100-BPM pop). Amapiano and afro house sit next to house, and reggaeton sits at pop and R&B ballad tempos.

| Fusion | Carrier (drums, bass, tempo) | Colour layers |
|---|---|---|
| Country trap | trap drums + 808 at 70/140, or boom-bap 85–95 | banjo/acoustic or slide loop on I–V–vi–IV, twang or melodic-rap vocal, rural imagery |
| Drill remix of pop | UK/NY drill grid at 140 with sliding 808 | interpolated pop hook, re-harmonised to minor |
| Amapiano / afro-pop | log drum + shaker groove at ~110–115 | jazzy or gospel 7th/9th chords, R&B topline; keep it sparse |
| Jersey club pop | club kick stutters and bed squeak at 140–150 | pop topline felt in half-time, often chorus- or remix-only |
| Afro-house global hit | 120–124 four-floor + tribal percussion | minor vocal hook, often a reworked older song |
| Emo rap / pop-punk trap | trap drums and 808, or live pop-punk kit | emo guitar loop; trap hat rolls in verses |
| Orchestral hip hop | boom bap 80–95 or trap 140 | strings/brass ostinati, choir, i–VI–III–VII over a pedal |
| Latin roots + urbano | dembow 3+3+2 | cuatro, accordion, bachata guitar, plena or salsa percussion and horns |
| Brazilian phonk | funk/tamborzão percussion + distorted 808 at 125–150 | phonk cowbell melody, montagem vocal chops |
| Metal + R&B (Sleep Token, Bad Omens) | section-switching: each section keeps its own carrier | R&B verse, djent/metalcore breakdown, pop hook |
| Punjabi + trap/afro | trap or dancehall kit | dhol chaal layer at low velocity, tumbi riff, Punjabi melisma |

The failure checklist (convention) gives the skill seven lint rules:

1. Two drum grids fighting, such as a dembow kick under four-on-the-floor hats with no plan.
2. A tempo forced into an unnatural spot, such as DnB breaks slowed to 120 so they drag.
3. Surface signifiers only (one banjo sample on a pop song), which the source scene reads as a costume.
4. Clashing mix conventions, such as a lo-fi vocal over a hyper-loud EDM master, or an 808 and a busy bass guitar in the same register.
5. Clashing harmony vocabularies, such as jazzy 9ths over a drill menace loop.
6. Clashing forms, such as a 16-bar DJ intro inside a 2:30 TikTok-first pop song.
7. A social mismatch in topic, language or visuals that invites gatekeeping, as the "Old Town Road" chart removal shows ([Okayplayer](https://www.okayplayer.com/news/lil-nas-x-old-town-road-billboard-hot-country-songs-chart.html)).

### The 2024–2026 landscape: shrinking rap share, rising rock, Latin, country, funk and afro house

The data points one way: the mainstream is a federation of scenes. Luminate's 2025 report counted **5.1 trillion global on-demand streams (+9.6%)**, and only 43% of US streams came from 2021–2025 releases, so catalogue leads. US on-demand audio volumes in 2025 (2024 in brackets) were R&B/hip-hop 349.9B (341.6), **rock 260.5B (234.2)**, pop 167.2B (165.5), country 122.5B (117.6) and Latin 120.9B (113.0). Christian/gospel posted the fastest growth at +18.5% ([AP via News4Jax](https://www.news4jax.com/entertainment/2026/01/14/music-streams-hit-5-trillion-in-2025-christian-rock-and-latin-lead-growth-in-the-us/)). The AP summary's own growth percentages do not match the ratios of those volumes, so quote volumes, not percentages. By H1 2026, R&B/hip-hop was about one in four US on-demand audio streams and down 1.7% year on year. English-language share was at a record low of 87.1% against 9.4% Spanish, and the top albums were Morgan Wallen, Ella Langley and Bad Bunny ([AP via WTOP](https://wtop.com/entertainment/2026/07/latin-and-country-surge-in-the-us-as-more-music-is-being-streamed-than-ever-before/)). Globally, IFPI put 2025 recorded revenue at **$31.7B (+6.4%)**. Latin America grew fastest (+17.1%), followed by Sub-Saharan Africa and MENA (+15.2%) ([Music Week](https://www.musicweek.com/public_html/index.php/labels/read/ifpi-global-recorded-music-revenue-up-6-in-2025-as-industry-embraces-the-future-on-ai/093789)). Some summaries mix in the previous report's 2024 figures of about +22%, so check the year before quoting. Spotify reports that funk was the fastest-growing genre worldwide in 2025 among genres earning over US$50M (+36%), ahead of K-pop, Latin trap and reggaeton ([Spotify Newsroom](https://newsroom.spotify.com/2026-05-11/artistas-brasileiros-alto-e-claro/)). Bad Bunny was 2025's top global artist with 19.8B streams, and a K-pop soundtrack song ("Golden") was the No. 2 global track ([NBC New York](https://www.nbcnewyork.com/entertainment/entertainment-news/spotify-wrapped-2025-bad-bunny-dethrones-taylor-swift-most-streamed-artist/); [AP via News4Jax](https://www.news4jax.com/entertainment/2026/01/14/music-streams-hit-5-trillion-in-2025-christian-rock-and-latin-lead-growth-in-the-us/)).

Creator data shows where producers are heading. Splice/MIDiA's 2024 data had Jersey club as Berlin's fastest-growing genre (+452%), Brazilian phonk up about 5× in São Paulo and pluggnb up 343% in Los Angeles ([Splice](https://splice.com/blog/?p=34341)). The 2025 data crowned **afro house "sound of the year" at +778%**, about 70% of all house growth, lifted house to the No. 2 genre, and showed triple-digit growth for speed garage, hard techno, jump-up DnB and hard dance. Hip hop stayed No. 1 for a third year, but trap's growth slowed as throwback and experimental styles rose ([MIDiA](https://midiaresearch.com/sounds-of-2026); [Mixmag](https://mixmag.net/read/hip-hop-most-downloaded-genre-on-splice-for-third-year-in-a-row-news)). Rock's revival runs through pop stars adopting guitar aesthetics and bands such as Sleep Token, Turnstile and Geese ([RUSSH](https://www.russh.com/why-is-everyone-making-rock-albums-now/)), and through a new shoegaze era ([Stereogum](https://www.stereogum.com/2482752/the-10-best-shoegaze-albums-of-2025/lists/year-in-review/2025-in-review)). AI music moved from novelty to volume. **Fully AI-generated tracks rose from about 10% of Deezer's daily uploads in January 2025 to 44% in April 2026 and over 50% by mid-2026** ([TechCrunch](https://www.techcrunch.com/2026/04/20/deezer-says-44-of-songs-uploaded-to-its-platform-daily-are-ai-generated/); [DJ Mag](https://djmag.com/news/ai-generated-music-surpasses-50-of-daily-uploads-deezer)). The Velvet Sundown, an AI "psych-rock band", passed a million monthly Spotify listeners before admitting it ([The FADER](https://www.thefader.com/2025/07/07/the-velvet-sundown-ai-band-story-explained)). AI country act Breaking Rust topped a Billboard country sales chart ([Iowa Public Radio](https://www.iowapublicradio.org/studioone/news/2025-12-08/ai-generated-music-breaking-rust-velvet-sundown-teddy-swims)), and an AI afro-house rework of Stromae's "Papaoutai" drew 210.7M streams outside the US in H1 2026 ([AP via WTOP](https://wtop.com/entertainment/2026/07/latin-and-country-surge-in-the-us-as-more-music-is-being-streamed-than-ever-before/)). AI output clusters in country, afro-house reworks and functional styles. For a composing skill, that makes generic genre-correctness cheap and pushes value toward the idiomatic detail and fake-tell avoidance this report catalogues. Trend data ages fast, so the skill should state the data year.

## One identification tree and one card schema turn the map into a skill

### Identify by the order the ear locks on, then report a ranked guess

The tree below integrates every family. It is synthesis. Its anchors are sourced in the sections above (house tempo and kick, jungle breaks, drill slides, dembow, one-drop placement, Jersey club kicks, gqom broken kicks, the afroswing snare on 3, the bachata derecho, the bluegrass chop), but no peer-reviewed by-ear scheme exists to validate it. Because MIR systems confuse adjacent genres, the skill should output a ranked guess with the cues it used.

```
STEP 0  Pulse?  None or rubato -> ambient / drone / film underscore / Indian alap / classical (go to STEP 6)
STEP 1  Kick on every beat (four-on-the-floor)?
  100-115  amapiano (log drum) | kwaito (slow house, fat synth bass) | moombahton (dembow snare over four, 108) | nu-disco
  115-126  house family (deep / afro / tech / Chicago) | disco & Philly (live drums, loud 16th open hat, strings) |
           French touch (909 + sidechain + filtered loop) | Motown (tambourine 2&4, ~120-140) | rockers reggae (rim on 3, ~75 counted)
  126-140  techno | speed garage | trance (supersaw, 138) | stomp-clap folk (stomps, claps, "hey") | industrial metal (machine riffs)
  140-170  hard techno | power soca (iron/brake drum, ~160) | bouyon (keyboard ostinato) | gospel shout (snare+clap on every "and")
STEP 2  Kick only on beat 3 with the snare/rim, beat 1 empty, skank on 2&4 -> ONE DROP reggae / dub (echo throws) / lovers rock
STEP 3  Snare position at the felt tempo
  2 & 4, swung triplet long-short ........ blues shuffle | rock'n'roll | jump blues | swing jazz (ride + walking bass) | doo-wop 12/8
  2 & 4, straight, live kit .............. rock / pop-rock / soul (check guitars vs keys) / J-pop / sertanejo / Americana
  2 & 4, no drums, chop + banjo 8ths ..... BLUEGRASS          2 & 4 + every-offbeat skank, fast ......... SKA
  heavy "one", one chord, scratch guitar . FUNK               2 & 4 claps, no four-floor, synth bass 110 . BOOGIE
  swung 16th triplets, giant snare ~104 .. NEW JACK SWING     late "drunk" snare, m9/m11 Rhodes ~84 ..... NEO-SOUL
  snare every "and" at punk tempo ........ skank punk / thrash skank (thrash if palm-muted chromatic riffs)
  snare on 3 (half-time) ................. trap / drill / dubstep / future bass (see earlier cards) |
                                           AFROSWING (~100, UK rap, 3-note grouping) | metalcore breakdown | country trap
STEP 4  A cell other than backbeat governs the bar
  3+3+2 dembow snare 4,7,12,15 at 88-105 .. reggaeton | dancehall (patois, synth-bass hook) | Latin pop
  2-bar clave + anticipated bass, no beat-1 bass .. son (tres, 85-120) | salsa (160-220 quoted, montuno, horns) |
                                           cha-cha (~120, flute+violins) | mambo (big band) | highlife (bell + arpeggios) | Latin jazz
  scraper on every beat + root-fifth bass .. cumbia (~95) | vallenato (accordion + caja) | merengue (fast, tambora roll)
  continuous guira 8ths + bongo, chorused requinto ~125 .. BACHATA
  low drum accent on beat 2 of 2/4 + 16th pandeiro .. SAMBA; soft cross-stick clave + maj7 + nylon guitar .. BOSSA
  distorted 808 3-3-2 at 130 / 150, chant hook .. BAILE FUNK (+ cowbell melody = Brazilian phonk)
  bass on beats, chords on offbeats (oom-pah) .. norteno / banda polka (+ requinto, 12-string chop, tololoche = TUMBADOS)
  dum-tek cycle on darbuka .. maqsum (Arabic pop, mahraganat if fast + Auto-Tune) | baladi | saidi | Khaleeji 3+3+2 + claps | chiftetelli 8/4
  triplet dhol "booma-chicka" + tumbi .. BHANGRA / Punjabi pop     tabla theka over drone .. filmi / Indian classical
  broken irregular kick 120-130, tom rolls, no log drum .. GQOM    tresillo kick ~145, sirens .. KUDURO
  one-chord vamp, muted tenor guitar vs chop guitar, horns .. AFROBEAT     fast high looping guitar second half .. SOUKOUS
STEP 5  Meter and density
  6/8 or 12/8 ... jig (Celtic) | Persian 6/8 | Ethio-jazz | Nashville/Stax/doo-wop ballads | huapango | indie folk
  3/4 ... country waltz | ranchera vals | minuet | Gymnopedie-style     odd meters ... prog | math rock | Turkish 9/8 | djent cycles
  blast beats / double kick ... black (un-muted tremolo, trebly) | death (growls, chromatic) | power (major-ish anthems)
STEP 6  Confirm with timbre and vocal
  steel + fiddle = honky-tonk; strings + choir croon = Nashville sound; banjo loop + 808 = country trap
  heterophonic violin unison + qanun + maqam ornaments = Arabic pop; half-flat notes = Rast/Bayati/Saba/Sikah
  royal road + many syllables + key-raised final sabi = J-pop; section-switching modules + dance break = K-pop
  pentatonic hook + erhu/guzheng = zhongguofeng; ambassel/tizita pentatonic + vibraphone = Ethio-jazz
  harpsichord continuo = Baroque; Alberti bass + 4-bar periods = Classical; planing 9ths = Impressionist
  2 pulse + triangle + noise only = chiptune; Lydian + mediant lifts + brass = film adventure; clusters + silence = horror
STEP 7  Use place, era and language to split close relatives, and report hybrids as "carrier + colour"
```

### The skill architecture follows from the card schema

The findings imply a router plus a library rather than one monolithic prompt (derived). A genre router takes a request, resolves synonyms and microgenre names to a family and a card, and asks for or infers fusion as carrier plus colour. It also states the data year whenever it cites a trend. Each card is stored as structured data in the eleven-field schema from the first section. Every numeric field carries an evidence flag (sourced, convention or derived) and, where sources conflict, both values with a note. Examples are the one-drop counting, ambassel spellings, the cáscara stroke list, bossa tempo counting and Slipknot's tuning. A gene library holds the seven reusable rhythmic layers and the special grids (12-step, CYCLE16, dum-tek, matra, 7/8, 9/8). That lets a new genre be assembled as genes plus tempo plus bass job plus timbre. A harmony library holds the spelled progressions, Nashville-number charts, maqam spellings with Fine-pitch offsets, thaats, qenet and pentatonics, and the soulify ladder. A performance layer applies per-family realism: tempo-dependent jazz swing, Channel Rack swing for 16th-swing genres, per-note offsets for neo-soul and Dilla feel, velocity bands, strum offsets, palm-mute lengths, CC1/CC11 curves for orchestral parts, and ornaments (cuts, rolls, meend, slides, maqam turns).

FL delivery has four hard constraints from the sources. Program by MIDI number because FL labels MIDI 60 "C5". Swing jazz 8ths on a triplet snap, because the Channel Rack swings 16ths and needs both global and channel swing above zero. Use native instruments when slides or portamento are needed. Deliver CC data through automation clips or MIDI import, because the MCP piano-roll tools only queue notes. Last, a lint pass checks each output against its card's fake tells before delivery. Across all families, the universal tells are:

- flat velocities and 100% quantize where the genre is played by humans;
- cloned left-right doubles;
- a downbeat-heavy kick or bass in anticipation-driven genres (Latin, reggae, gqom);
- the wrong swing subdivision or amount;
- sustained pads where the style uses chops or stabs;
- Western functional harmony imposed on modal, maqam, raga or Celtic melodies;
- melodies harmonised in thirds where the style is heterophonic;
- the wrong drum engine for the genre (blasts in nu metal, trap hats in thrash, a drum kit in bluegrass);
- an era-wrong low end, such as an 808 sub under Motown, Philly or 1970s Afrobeat.

## Conclusion

The map changes how a composing skill should think about genre. Genre is not a style label to imitate. It is mostly a choice of time-line and bass behaviour, and seven rhythmic genes reach much farther than their names suggest. The 3+3+2 cell links a Celtic reel's guitar push, a bluegrass banjo roll, Gulf Khaleeji claps, Rio's tamborzão, Jamaican dembow, highlife's bell, djent's groupings and a Zimmer cello ostinato. The triplet shuffle links the Chicago blues, the Nashville ballad, the bhangra chaal and the Persian 6/8. That means a skill can be small and general: a gene library plus per-genre timbre, harmony and ornament layers can produce styles it was never explicitly taught, and it can fuse them correctly by keeping one carrier's genes intact. The hits of 2019–2026 follow that rule: an authentic engine from one scene, a mainstream topline and form from another.

The second implication is that authenticity now lives in the small, unglamorous details. AI-generated tracks already make up most new uploads on at least one platform, so a correct BPM and chord loop are commodities. What separates a convincing result is performance data and idiom: tempo-dependent swing, ghost notes, the half-flat on the right degree, cuts and rolls, the bass resting on beat 1 in reggae and avoiding it in salsa, the 808 added last rather than first. The fake-tell lists are therefore the most valuable part of the cards. Most numbers in them are convention, so they should ship as editable defaults with evidence flags and be checked by ear against a reference track before they become canon.
