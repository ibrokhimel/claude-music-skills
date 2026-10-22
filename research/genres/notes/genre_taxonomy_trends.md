# Genre Taxonomy, Lineage, Fusion and the 2024–2026 Landscape (map section for a Claude genre skill)

Scope note: this is the "map" layer. Per-genre recipe cards (BPM, 16-step grids, harmony, arrangement) already live in `research_notes/Music theory and beat making/genres_hiphop_urban_global.md` and `genres_electronic_pop_cinematic.md`; this file only places those genres in a taxonomy and does not repeat their recipes. Research date: Oct 2026. Data years are stated next to every statistic. Items under "Inferences" are synthesis or widely-held practitioner convention not verified against a source in this session; treat them as defaults, not facts.

---

## Q1. What dimensions define a genre (musical and social), and what does MIR research say about genre classification and its limits?

### Takeaway
A genre is a bundle of musical conventions (tempo band, meter/feel, drum signature, bass type, harmony, timbre, vocal delivery, form, production aesthetic) plus social facts (scene, place, era, industry and chart category). The social half is real enough that the same audio can be ruled in or out of a genre by a chart body, and MIR research shows that automatic genre classifiers often score well without really "hearing" genre, because labels are inconsistent and datasets are flawed.

### Cited Findings
- **Genre is partly social/organisational.** Jennifer Lena and Richard Peterson ("Classification as Culture: Types and Trajectories of Music Genres", *American Sociological Review* 73(5):697–718, 2008) identify four recurring genre forms in US popular music: **Avant-garde, Scene-based, Industry-based, Traditionalist**. Lena's later book (drawing on ~60 styles from rap and bluegrass to death metal and South Texas polka) adds a fifth outside the US, the **Government-purposed** genre (China, Serbia, Nigeria, Chile). — [Vanderbilt IR](https://ir.vanderbilt.edu/items/e115978c-c9b3-449c-a607-3b8510941b41); [Princeton UP, *Banding Together*](https://press.princeton.edu/node/14985)
- **Chart bodies police genre by "elements".** In March 2019 Billboard removed Lil Nas X's "Old Town Road" (country imagery over a trap beat, sampling Nine Inch Nails) from Hot Country Songs, saying it did not embrace enough elements of today's country music. It had debuted at No. 19 there and was the first song to appear on the Hot 100, Hot Country Songs and Hot R&B/Hip-Hop Songs at once. Critics pointed to Billboard's history of drawing genre lines by race. — [XXL](https://www.xxlmag.com/lil-nas-x-old-town-road-removed-billboard-country-chart/); [Okayplayer](https://www.okayplayer.com/news/lil-nas-x-old-town-road-billboard-hot-country-songs-chart.html)
- **Genre labels themselves are inconsistent.** Pachet & Cazaly ("A Taxonomy of Musical Genres", RIAO 2000) analysed industry and internet genre taxonomies and stressed their inconsistencies, proposing a new taxonomy built on a few guiding principles. Aucouturier & Pachet followed with "Representing Musical Genre: A State of the Art" (*J. New Music Research*, 2003). — [Pachet site](https://www.francoispachet.fr/?p=4325); [Genre Across Borders bibliography](https://genreacrossborders.uwaterloo.ca/node/1255)
- **GTZAN, the standard MIR genre benchmark, is faulty.** GTZAN is 1,000 thirty-second excerpts in 10 genres, used in at least 100 published works. Sturm (2013) found 50 exact repetitions, 21 recording repetitions, 13 version repetitions, ~93 mislabelings, heavy artist repetition (e.g. over a third of Reggae is Bob Marley; Blues has only 9 artists across 100 excerpts) and distortions (clipping, static, one badly corrupted file). He estimates a fault-limited ceiling around 94.5% accuracy, so reported scores above that are suspect, and he showed the faults do not affect all systems equally (so cross-system comparison is not fair). His advice: keep using GTZAN, but with awareness of its contents. — [Sturm, arXiv 1306.1461](https://arxiv.org/abs/1306.1461); [ar5iv full text](https://ar5iv.labs.arxiv.org/html/1306.1461)
- **"Horse" systems.** Sturm showed state-of-the-art genre recognisers can be fooled by simple transformations that a human would not notice, so they cannot actually be listening to genre (a "Clever Hans" effect). A literature review found 81% of works judge genre recognition only by classification accuracy ("Classification accuracy is not enough", *J. Intelligent Information Systems*, 2013). — [QMUL news 2015](https://qmul.ac.uk/media/news/2015/se/how-music-listening-programs-can-be-easily-fooled.html); [Sturm, "The Horse Inside", arXiv 1606.03044](https://arxiv.org/abs/1606.03044v1); [AAU record](https://vbn.aau.dk/da/publications/classification-accuracy-is-not-enough-on-the-evaluation-of-music-)
- **Spotify microgenres / Every Noise at Once.** Glenn McDonald's map started as a debugging tool at The Echo Nest, where ML scored songs on attributes like danceability, energy and mood. In 2018 it showed 1,742 genres, including national and niche ones (Thai hip hop, German metal, discofox). — [Spotify for Artists blog, 2018](https://artists.spotify.com/blog/how-spotify-discovers-the-genres-of-tomorrow)
- When McDonald was laid off on 4 Dec 2023, the system had placed about 1 million artists into **6,291 named genres** (including 56 kinds of reggae, 202 kinds of folk, 230 kinds of hip hop). The site is now a frozen snapshot and is no longer updated. — [Wikipedia: Every Noise at Once](https://en.wikipedia.org/wiki/Every_Noise_at_Once); [TechCrunch, Feb 2024](https://techcrunch.com/2024/02/12/every-noise-shut-down-spotify-layoffs)

### Inferences
- **Working definition for the skill:** genre = (musical fingerprint) × (scene / place / era / industry label). The musical fingerprint is what a producer can control; the social part decides whether listeners, playlists and charts accept the label.
- **The 9 musical dimensions, in rough order of how much they decide a genre by ear:**
  1. **Tempo band and half-time feel** (e.g. 140 BPM drill vs 70 BPM felt; DnB 170–176 with half-time 85 feel).
  2. **Kick/snare placement** (backbeat on 2 and 4; four-on-the-floor; snare on 3 in half-time; dembow 3+3+2; broken/2-step).
  3. **Subdivision and swing** (straight 16ths; triplet/shuffle; MPC swing 54–62%; hi-hat rolls).
  4. **Bass type** (sliding 808; sub + mid-bass; walking/upright; slap/funk; acid 303; amapiano log drum; reese).
  5. **Harmony vocabulary** (blues I-IV-V and dominant 7ths; jazz ii-V and extensions; minor-key loops of 2–4 chords; modal/drone; church/gospel chords; Phrygian/harmonic minor for drill/trap darkness).
  6. **Signature timbres/instruments** (909 hats, Rhodes, steel guitar, accordion/bajo sexto, talking drum/shaker, synth brass, cowbell).
  7. **Vocal style** (rap flow type, melodic auto-tune, belting, crooning, toasting/chatting, call-and-response, chopped vocal samples).
  8. **Form** (verse/chorus pop; 8/16-bar DJ phrasing with build/drop; 12-bar blues; AABA; head-solos-head; long-form techno).
  9. **Production aesthetic** (lo-fi saturation, sidechain pumping, hyper-compressed loudness, vinyl crackle, room ambience vs dry, "sped-up" pitch).
- **Social dimensions:** scene (clubs, sound systems, churches, TikTok dance trends), place (city or country names are often part of the genre name: Chicago drill, UK garage, Jersey club, Brazilian phonk), era (synthwave = 1980s nostalgia), industry/chart format (Billboard Hot Country vs Hot R&B/Hip-Hop), and language (Luminate tracks Spanish-language share separately).
- **Lesson from MIR for a Claude skill:** do not trust a single-feature classifier. Identify by several independent cues (rhythm + bass + timbre + vocal), and accept hybrids and multi-labels. Spotify-style microgenres are mostly defined by listener and artist clustering plus place, not by one musical rule, so "Thai hip hop" can sound like any hip hop.

### Gaps
- Could not verify Ishkur's Guide to Electronic Music content this session; no claims from it are used.
- No current (2025–2026) peer-reviewed benchmark replacing GTZAN was checked (newer sets like FMA/MTG-Jamendo exist but were not verified here).
- Spotify's post-2023 internal genre system is not public.

---

## Q2. Major genre family trees and bridging genres

### Takeaway
Most modern popular music descends from a few African-American and Afro-Caribbean roots (blues, gospel, jazz, Jamaican sound-system music) and from disco's DJ culture. Rhythm (backbeat, four-on-the-floor, tresillo/dembow, breakbeats) is the trait most reliably passed down, so family trees are best read through drum patterns.

### Cited Findings
- **Blues → R&B → rock 'n' roll / soul / funk / disco / contemporary R&B.** R&B formed in 1940s African-American communities from jump blues, big band swing, gospel, boogie and blues (Louis Jordan, Big Joe Turner). Billboard's Jerry Wexler popularised "rhythm and blues" in 1949 to replace "race music"; the R&B chart ran June 1949–Aug 1969. R&B fed rock and roll in the 1950s; "soul" replaced the R&B label in the early 1960s; by the 1970s R&B was an umbrella for soul, funk and disco; late-1980s contemporary R&B absorbed hip hop (new jack swing). — [Wikipedia: Rhythm and blues](https://en.wikipedia.org/wiki/Rhythm_and_blues)
- **Disco → house → acid house / deep house / garage / hip house; Detroit techno alongside.** House grew in Chicago's queer Black club underground; Frankie Knuckles at the Warehouse (1977–1982) re-edited disco records with a more mechanical beat. Core: 115–130 BPM, repetitive 4/4 kick, off-beat hi-hats, claps; TR-808/909 and TB-303. Early records: Jesse Saunders "On and On" (1984), Phuture "Acid Tracks" (1987, acid house). Offshoots: deep house (Larry Heard, 1985–86), New York/New Jersey garage (more R&B), hip house (1988+), UK acid house and rave ("Second Summer of Love", 1988–89). Detroit's Belleville Three (Atkins, May, Saunderson) made the harder, machine-driven techno strand. — [Wikipedia: House music](https://en.wikipedia.org/wiki/House_music)
- **Reggae/dub sound systems + breakbeat hardcore → jungle → drum and bass.** Jungle (early-1990s UK) came out of breakbeat hardcore, combining fast, chopped breakbeats (often the Amen break) with dub/reggae/dancehall basslines and vocal samples, at about 160–180 BPM. Jamaican sound-system culture shaped it (Rebel MC, Paul Ibiza, 1990–92). Peak 1994–95; by 1996–97 it turned darker and jazzier and became drum and bass (Roni Size, Dillinja). — [Wikipedia: Jungle music](https://en.wikipedia.org/wiki/Jungle_music)
- **Jamaican dancehall → Panamanian reggae en español → Puerto Rican reggaeton → Latin trap and others.** Panama's Spanish-language reggae (dancehall brought by canal workers) plus hip hop became reggaeton in Puerto Rico's 1990s underground (DJ Playero, DJ Nelson; police raids in 1995). The rhythmic backbone is the **dembow riddim** made by Steely & Clevie and popularised by Shabba Ranks (1991). It is kick + snare + timbal in a 3+3+2 tresillo over 4/4, and Wikipedia says it is used in over 80% of reggaeton. Milestones: "Gasolina" (2004), "Hips Don't Lie" (2006); after "Despacito" (2017), offshoots include minimal dembow, Latin trap, bachaton, cubaton. — [Wikipedia: Reggaeton](https://en.wikipedia.org/wiki/Reggaeton)
- **Trap → Chicago drill → UK drill → Brooklyn drill → global drill.** Chicago drill (South Side, 2010–12; Chief Keef; producer Young Chop with synth brass, bells, busy snares) came from trap's sound with gangsta-rap lyrics. UK drill (Brixton, c. 2013; 67, LD) went to ~140 BPM with sliding 808s and syncopated snares/hats. Pop Smoke brought UK drill production (with UK producers such as 808Melo) to Brooklyn. Scenes followed in Australia, Ireland, Ghana, Netherlands, Denmark, France. — [Wikipedia: Drill music](https://en.wikipedia.org/wiki/Drill_music)
- **Baltimore club → Jersey club; and into K-pop.** NewJeans' "Ditto" (Dec 2022) reworked Baltimore club (a breakbeat/house hybrid from early-1990s Baltimore) and became the group's first Hot 100 entry (chart dated 21 Jan 2023). — [Wikipedia: Ditto (song)](https://en.wikipedia.org/wiki/Ditto_(song)) Splice describes Jersey club as Baltimore-club-derived, early 2000s, with stuttering kick patterns and the "bed squeak" sample. — [Splice, Sounds of 2025](https://splice.com/blog/?p=34341)
- **Kwaito + deep/soulful house → afro house; amapiano → afro-pop.** Splice traces afro house to a mix of kwaito, deep and soulful house in post-apartheid South Africa, and says it has overtaken amapiano as South Africa's leading export. — [Splice, Sounds of 2025](https://splice.com/blog/?p=34341) Grammy.com describes amapiano's signature as log drums and piano runs. — [Grammy.com](https://grammy.com/news/tyla-winner-best-african-music-performance-water-2024-grammys-meaning)
- **Phonk + Brazilian funk → Brazilian (drift) phonk.** Splice describes Brazilian phonk as phonk's cowbell sound combined with Brazilian funk elements. — [Splice, Sounds of 2025](https://splice.com/blog/?p=34341)
- **Plugg + 1990s R&B/gospel → pluggnb.** Splice/MIDiA defines pluggnb as trap's plugg subgenre fused with '90s R&B and gospel harmony. — [MIDiA Research blog](https://www.midiaresearch.com/blog/jersey-club-in-berlin-behind-the-scenes-and-sounds-of-2025)

### Inferences (lineage map; general music-history knowledge, not verified line by line this session)
```
ROOTS: West African rhythm (polyrhythm, call-response, clave/tresillo) + European harmony/instruments
 |
 +-- Spirituals/Gospel ---------------------------------> Soul (1960s) -> Contemporary gospel/CCM
 +-- Blues (Delta, 1900s-30s) -> Chicago electric blues (1940s-50s)
 |     +-> Jump blues/R&B (1940s) -> Rock'n'roll (1950s) -> British Invasion/rock (60s)
 |     |      rock -> hard rock/metal (70s) -> punk (76-77) -> post-punk/new wave/alt/grunge/emo
 |     |      rock + rap -> nu-metal; emo + trap -> emo rap; pop-punk revival (2020s)
 |     +-> Soul -> Funk (James Brown, late 60s: "the One", syncopated bass)
 |            Funk -> Disco (70s) -> [see EDM tree]
 |            Funk/soul breaks + Jamaican sound-system DJing -> Hip hop (Bronx, 1973+)
 |               boom bap (80s-90s) -> g-funk, Southern rap -> crunk -> TRAP (Atlanta, 2000s)
 |               trap -> drill (Chicago/UK/NY), plugg -> pluggnb, rage, Latin trap, country-trap,
 |                      phonk (Memphis rap revival) -> Brazilian/drift phonk
 +-- Ragtime/Blues/Brass bands -> Jazz (New Orleans 1910s) -> Swing (30s) -> Bebop (40s)
 |     -> cool/hard bop -> modal (1959) -> free/avant (60s) -> fusion/jazz-funk (70s)
 |     -> acid jazz/nu-jazz; jazz sampling -> boom bap/lo-fi hip hop; UK jazz scene (2010s+)
 +-- Anglo-Celtic folk + blues + gospel -> Old-time/hillbilly -> Country (1920s+)
 |     -> honky-tonk, bluegrass (40s), Nashville sound, outlaw (70s), country-pop, bro-country,
 |        country-rap/country-trap ("Old Town Road" 2019, "A Bar Song" 2024); Americana/folk revival
 +-- Caribbean: mento/ska (60s) -> rocksteady -> reggae -> dub -> dancehall (80s)
 |     dub/sound systems -> UK jungle -> DnB; dub -> dubstep (via UK garage)
 |     dancehall -> reggaeton (Panama/PR) -> Latin trap, dembow (DR), Brazilian funk ties
 |     dancehall + highlife/juju/hip hop -> Afrobeats/Afropop (Nigeria/Ghana, 2000s-10s)
 +-- Latin: son/salsa/cumbia/bachata; Mexican: corridos, banda, norteño -> corridos tumbados
 |     (Mexican/US, 2020s: corrido guitar and narrative + trap/hip hop attitude)
 +-- Southern Africa: kwaito (90s) -> gqom, afro house, amapiano (mid-2010s)

EDM TREE: Disco -> (Chicago) house -> acid/deep/garage/hip house/ghetto house -> Baltimore club -> Jersey club
          Kraftwerk/electro-funk + house -> (Detroit) techno -> minimal/tech house/hard techno
          house + techno + Euro-synths -> trance (early 90s) -> progressive/uplifting/psytrance
          Euro rave + breakbeats -> UK hardcore -> jungle -> DnB (liquid, neuro, jump-up)
          US garage/house -> UK garage/2-step (late 90s) -> grime (~2002) and dubstep (~2002-05)
          dubstep -> brostep/riddim; -> future garage; EDM (2010s big-room/electro) -> future bass
          synth-pop/80s soundtracks -> synthwave/retrowave
```
- **Key bridging genres** (each sits between two families and is a good place to "borrow" from): funk (soul ↔ hip hop/disco), disco (soul ↔ house), dub (reggae ↔ electronic bass music), UK garage (house ↔ grime/dubstep/drill), trap (hip hop ↔ EDM "trap" drops ↔ Latin trap ↔ drill), Baltimore/Jersey club (house ↔ hip hop), kwaito (house ↔ amapiano/afro house), dancehall (reggae ↔ reggaeton ↔ afrobeats), emo rap (rock ↔ trap), corridos tumbados (Mexican folk ↔ trap).
- Genres in the existing recipe notes fit here as follows: trap, drill (Chicago/UK/NY), boom bap, lo-fi, phonk, plugg/pluggnb, rage, Jersey club, R&B, afrobeats, amapiano, reggaeton/dembow → hip hop/Caribbean/African branches. House, deep/tech house, afro house, techno (Detroit/rolling/hard), trance, DnB/liquid/neuro, dubstep/riddim, UKG/2-step, future garage, future bass, synthwave, hyperpop, ambient, modern pop, trailer/cinematic → EDM/pop/screen branches. (Hyperpop sits between bubblegum pop, trance/EDM synths and internet rap. Cinematic/trailer music descends from the orchestral film-score tradition mixed with EDM sound design.)

### Gaps
- Folk/country and jazz lineages above were not checked against a source in this session (only the R&B, house, jungle, reggaeton and drill articles were fetched). Dates should be checked before quoting them as facts.
- No source fetched on trap's Atlanta origins, grime/dubstep dating, or the gqom → amapiano timeline.

---

## Q3. How do producers fuse genres convincingly, and what makes fusions fail?

### Takeaway
Hit fusions tend to keep one genre's identity carrier (usually the drum pattern and bass, or the vocal/topline language) intact and swap one or two other layers (harmony, lead timbre, imagery, lyrics). The proven 2019–2025 template: an authentic rhythmic engine from scene A, plus melody, song form and vocal from mainstream pop/country/K-pop.

### Cited Findings
- **Country-trap:** "Old Town Road" put country imagery and lyrics over a trap beat and spent 19 weeks at No. 1 on the Hot 100 (2019). — [XXL](https://www.xxlmag.com/lil-nas-x-old-town-road-removed-billboard-country-chart/); [The Needle Drop](https://theneedledrop.com/news/shaboozeys-a-bar-song-tipsy-1-for-19th-week-ties-lil-nas-xs-old-town-road/)
- **Country + hip hop (2024):** Shaboozey's "A Bar Song (Tipsy)" tied the all-time Hot 100 record with 19 weeks at No. 1 (Nov 2024), led Hot Country Songs for 23+ weeks, and earned Grammy nominations in both country and rap fields (with Beyoncé on "Spaghettii"). Billboard noted it got there without star remixes. — [Billboard Canada](https://ca.billboard.com/music/chart-beat/shaboozey-record-no-1-hot-100); [The Needle Drop](https://theneedledrop.com/news/shaboozeys-a-bar-song-tipsy-1-for-19th-week-ties-lil-nas-xs-old-town-road/)
- **Amapiano-pop:** Tyla's "Water" mixed amapiano log drums and piano runs with Western pop and R&B. It peaked at No. 7 on the Hot 100 and won the first Grammy for Best African Music Performance (Feb 2024). Grammy.com calls it "the first African song to enter the Billboard Hot 100 since 1968". That wording looks loose, because Nigerian hits such as "Calm Down" charted earlier; the usual claim is the first South African solo artist since Hugh Masekela in 1968. — [Grammy.com](https://grammy.com/news/tyla-winner-best-african-music-performance-water-2024-grammys-meaning)
- **Club rhythm in K-pop:** NewJeans' "Ditto" used Baltimore club rhythm under a soft K-pop topline and gave the group its first Hot 100 entry (2023). — [Wikipedia: Ditto](https://en.wikipedia.org/wiki/Ditto_(song))
- **Pop + K-pop + pop-punk duet:** ROSÉ & Bruno Mars "APT." was Spotify's No. 3 global song of 2025. — [MBW / NBC on Wrapped 2025](https://www.nbcnewyork.com/entertainment/entertainment-news/spotify-wrapped-2025-bad-bunny-dethrones-taylor-swift-most-streamed-artist/)
- **Traditional + urban (Latin):** Bad Bunny's *Debí Tirar Más Fotos* (mixing Puerto Rican traditional styles with reggaeton/urban production) was Spotify's most-streamed album of 2025 and won Grammy Album of the Year on 1 Feb 2026, the first Spanish-language album to do so. — [PBS NewsHour](https://www.pbs.org/newshour/arts/bad-bunny-wins-album-of-the-year-at-the-2026-grammy-awards-making-history-for-a-spanish-language-album); [MBW](https://www.musicbusinessworldwide.com/bad-bunny-was-spotifys-most-streamed-artist-globally-in-2025-with-over-19-8bn-streams)
- **Fusion as the creator trend:** Splice/MIDiA (2025 data) reports pop's comeback in sample downloads was "driven by genre-blending styles" (bedroom pop +297%), and hip hop is diversifying into throwback and experimental subgenres alongside trap. — [MIDiA Sounds of 2026](https://midiaresearch.com/sounds-of-2026); [RouteNote](https://routenote.com/blog/splice-midia-sounds-of-2026-report/)
- **Gatekeeping risk:** a fusion can be shut out of a genre's institutions (the "Old Town Road" chart removal) even while it is a hit. — [Okayplayer](https://www.okayplayer.com/news/lil-nas-x-old-town-road-billboard-hot-country-songs-chart.html)

### Inferences (fusion method for the skill; practitioner convention)
- **The "carrier + colour" rule:** pick ONE carrier genre that sets tempo band, kick/snare grid and bass type. The second genre brings at most 2–3 of: harmony, lead/hook instrument, vocal style, lyrical imagery, one signature sound (cowbell, log drum, bed squeak, steel guitar, accordion). Two competing drum grids is the most common failure.
- **Tempo bridging:** join genres through half-time or double-time relationships (70↔140: trap/drill ↔ UK garage/dubstep; 85↔170: hip hop ↔ DnB; 87.5↔175; 100↔200 for Jersey club over pop at 100). Amapiano/afro house (~110–124) sits close to house; reggaeton/dembow (~90–100) matches pop/R&B ballad tempos.
- **Fusion recipes by pairing (carrier first):**
  - *Country-trap:* trap drums + 808 at 70/140 (or boom-bap 85–95) + acoustic/banjo/slide-guitar loop on I–V–vi–IV or I–IV + twang/melodic-rap vocal + rural imagery.
  - *Drill remix of pop:* UK/NY drill grid at 140 with sliding 808s, sampling or interpolating the pop hook, re-harmonised to minor if needed ("sample drill").
  - *Amapiano-pop / afro-pop:* log drum + shaker/hat groove at ~110–115 + jazzy or gospel 7th/9th chords + R&B/pop topline; leave space (amapiano is sparse).
  - *Jersey club pop:* pop topline at ~140–150 (felt as half-time pop), club kick triplet stutters and bed squeak/vocal chops in the hook; often used only in the chorus or a remix.
  - *Afro-house global hit:* 120–124 four-on-the-floor, tribal percussion layers, minor-key vocal hook (often a sampled or reworked older song, see the AI "Papaoutai" afro-house version in Q4).
  - *Rock + trap (emo rap, pop-punk trap):* trap drums/808 under distorted or clean guitar loop, emo melody; or live-drummed pop-punk with trap hi-hat rolls in verses.
  - *Orchestral hip hop:* boom bap or trap drums at 80–95 or 140 under strings/brass ostinati and epic choirs (cinematic harmony: minor i–VI–III–VII, pedal tones).
  - *Reggaeton/Latin fusion:* dembow (3+3+2) carrier + local instrument (cuatro, accordion, bachata guitar, plena drums) for identity.
  - *Brazilian phonk:* phonk cowbell melody + distorted 808 + funk carioca/"tamborzão"-style percussion at ~125–135.
- **Why fusions fail (checklist):**
  1. Two drum grids fighting (e.g. dembow kick under four-on-the-floor hats with no plan).
  2. Tempo forced into an unnatural spot (e.g. DnB breaks slowed to 120 so they drag).
  3. Surface signifiers only (one banjo sample in a pop song) with no real borrowing of feel or harmony, which listeners in the source scene read as a costume.
  4. Mixing conventions that clash (lo-fi vocal over a hyper-loud EDM master; 808 and a busy bass guitar in the same register).
  5. Harmony vocabulary clash (jazzy 9ths over a phonk/drill minor-key menace loop).
  6. Arrangement form clash (DJ 16-bar intro inside a 2:30 TikTok-first pop song).
  7. Social mismatch: the topic, language or visuals ignore the source scene, which can lead to gatekeeping or authenticity backlash.

### Gaps
- No systematic or academic study on what makes fusions succeed or fail was found; the checklist is producer convention.
- No fetched source documents specific "drill remix of pop" or "afro-house global hit" cases beyond the AI "Papaoutai" entry in Q4.

---

## Q4. The 2024–2026 genre landscape: growth genres, data, TikTok micro-genres, AI music

### Takeaway
In the US, R&B/hip-hop still leads streams but its share is shrinking. Rock, Latin, country and Christian are the growth stories in 2025–H1 2026, and catalog music dominates listening. Globally, revenue growth is fastest in Latin America, Sub-Saharan Africa and MENA; Bad Bunny, K-pop (KPop Demon Hunters' "Golden"), Brazilian funk and afro house are the international breakouts. Creator scenes (Splice data) point to afro house, uptempo club styles (speed garage, hard techno, jump-up DnB, Jersey club) and bedroom pop. AI music went from novelty to chart presence and now makes up a large share of uploads.

### Cited Findings: industry totals
- **Luminate 2025 (calendar 2025):** global on-demand streams 5.1 trillion (+9.6% vs 2024); US on-demand audio 1.4 trillion (+4.6%). Only 43% of US streams were from tracks released 2021–2025, so catalog leads. — [AP via News4Jax, Jan 2026](https://www.news4jax.com/entertainment/2026/01/14/music-streams-hit-5-trillion-in-2025-christian-rock-and-latin-lead-growth-in-the-us/); [Luminate report](https://view.ceros.com/luminate-data/luminate-year-end-music-report-2025-1)
- **US genre volumes 2025 (on-demand audio, billions; 2024 in brackets):** Rap/R&B 349.9 (341.63); Rock 260.5 (234.22; +6.4%, the biggest share gainer, and second in current-release streams); Pop 167.2 (165.49); Country 122.5 (117.58); Latin 120.9 (113.02; +5.2%); Christian/Gospel +18.5% (the fastest growth). — [AP via News4Jax](https://www.news4jax.com/entertainment/2026/01/14/music-streams-hit-5-trillion-in-2025-christian-rock-and-latin-lead-growth-in-the-us/)
- **Luminate 2024:** pop led US growth at year end, followed by rock and Latin (Latin had been the fastest grower at mid-2024, +15.1% YoY). Regional Mexican passed Latin pop as the largest US Latin subgenre (28.57B vs 24.09B streams). K-pop and Regional Mexican have unusually high superfan shares. — [Sounds.co summary of Luminate 2024](https://sounds.co/en/post/claves-del-luminate-2024-year-end-music-report-lo-que-todo-artista-independiente-debe-saber); [Luminate 2024 report](https://luminatedata.com/reports/yearend-music-industry-report-2024/)
- **Luminate H1 2026:** global on-demand streams 2.8T (H1 2025: 2.5T; H1 2024: 2.29T); US 732.7B. US H1 genres (billions): R&B/hip-hop 180.3, rock 137.2, pop 87.8, country 63.8, Latin 63.0. R&B/hip-hop is about 1 in 4 on-demand audio streams and 30% of album-equivalent consumption; its audio volume is down 1.7% YoY. English-language share is at a record low of 87.1%, Spanish 9.4%. Casual US Latin listenership is 54% (all-time high). Global Latin streams were 363.2B. Top H1 albums: Morgan Wallen *I'm the Problem*, Ella Langley *Dandelion*, Bad Bunny *DtMF*. AP's summary: Latin and country are surging. — [AP via WTOP, Jul 2026](https://wtop.com/entertainment/2026/07/latin-and-country-surge-in-the-us-as-more-music-is-being-streamed-than-ever-before/); [Luminate blog](https://luminatedata.com/blog/luminate-2026-midyear-report-trends-in-music-television-film/)
  - Note: the AP piece also gives a 41% (2023) → 30% (H1 2026) decline for R&B/hip-hop, but it is unclear whether both numbers use the same metric. Check the Luminate PDF before quoting.
- **IFPI Global Music Report 2026 (covering 2025):** global recorded revenue $31.7B (+6.4%, 11th straight year of growth); paid subscription +8.8% (52.4% of revenue); 837M paid accounts; streaming 69.6% of revenue. Region growth: Latin America +17.1% (fastest, 16th straight year), Sub-Saharan Africa and MENA +15.2%, Asia +10.9%, Europe +5.6%, USA & Canada +3.5%. China rose to No. 4 market (+20.1%). Top global artist: Taylor Swift. — [Music Week](https://www.musicweek.com/public_html/index.php/labels/read/ifpi-global-recorded-music-revenue-up-6-in-2025-as-industry-embraces-the-future-on-ai/093789)
  - Possible confusion: some summaries of the *2025* report (covering 2024) give MENA +22.8%, SSA +22.6%, LatAm +22.5%. Those are 2024 figures, not 2025. — [MBW 11 takeaways (2024 data)](https://musicbusinessworldwide.com/11-quick-and-important-takeaways-from-ifpis-global-music-report-2025); one search snippet mixed the two years, so check the year before quoting.

### Cited Findings: genres and hits
- **Spotify Wrapped 2025:** Bad Bunny was top global artist (19.8B streams; his 4th time) and had the top album (*DtMF*). Top global songs: "Die With A Smile" (Gaga/Mars), "BIRDS OF A FEATHER" (Billie Eilish), "APT." (ROSÉ/Mars), "Ordinary" (Alex Warren), "DtMF" (Bad Bunny), "Golden" (HUNTR/X, KPop Demon Hunters). — [NBC New York](https://www.nbcnewyork.com/entertainment/entertainment-news/spotify-wrapped-2025-bad-bunny-dethrones-taylor-swift-most-streamed-artist/); [MBW](https://www.musicbusinessworldwide.com/bad-bunny-was-spotifys-most-streamed-artist-globally-in-2025-with-over-19-8bn-streams)
- Luminate's 2025 global top tracks: Gaga & Mars 2.858B, HUNTR/X 2.430B, Alex Warren 2.403B. So a K-pop soundtrack song was the No. 2 global track. — [AP via News4Jax](https://www.news4jax.com/entertainment/2026/01/14/music-streams-hit-5-trillion-in-2025-christian-rock-and-latin-lead-growth-in-the-us/)
- **Brazilian funk:** Spotify's Loud & Clear Brazil (May 2026) says funk was the fastest-growing genre worldwide in 2025 among genres earning over US$50M on Spotify (+36%), ahead of K-pop, Latin trap, Latin urban and reggaeton. Portuguese was the fastest-growing language among those earning over US$100M (+26% YoY, +51% over two years). — [Spotify Newsroom (PT)](https://newsroom.spotify.com/2026-05-11/artistas-brasileiros-alto-e-claro/)
- **Afrobeats:** Spotify data reported in Nigerian press says afrobeats listeners grew 22% globally in 2025 and more than 180% in Latin America. Amapiano streams in Nigeria grew 10,330% from 2021 to 2025. — [BusinessDay NG](https://businessday.ng/life-arts/article/afrobeats-streams-surge-by-over-5000-as-spotify-marks-five-years-in-nigeria/); [Techpoint Africa](https://techpoint.africa/news/spotify-wrapped-2025/) (secondary reports of Spotify figures)
- **Regional Mexican / corridos tumbados:** a secondary source claims Spotify Regional Mexican streams rose 49% YoY in Q1 2025, that three corridos tumbados tracks were in the Global 200 top 15 in one week, and that corridos tumbados make up over 77% of Música Mexicana streams on Spotify. This is a low-authority blog, so verify against Billboard/Spotify before use. — [Espiritu blog](https://espiritu.com/blogs/news/amplified-roots-how-regional-mexican-music-went-global-without-losing-its-accent) Firmer: Luminate 2024 shows Regional Mexican as the largest US Latin subgenre (above).
- **Country:** country is a steady US grower (122.5B streams in 2025); H1 2026 top albums are country-led (Wallen, Langley). — [AP via WTOP](https://wtop.com/entertainment/2026/07/latin-and-country-surge-in-the-us-as-more-music-is-being-streamed-than-ever-before/)

### Cited Findings: creator and micro-genre signals (Splice/MIDiA download data)
- **Sounds of 2025 (2024 data):** Jersey club was Berlin's fastest-growing genre (+452.2% downloads). Brazilian phonk downloads in São Paulo rose about 5x. Afro house +203.9% in Johannesburg. Pluggnb +342.8% and, with K-pop, the fastest-growing genre in Los Angeles. Mainstream pop and EDM downloads fell; "micro-communities drive innovation." — [Splice](https://splice.com/blog/?p=34341); [MIDiA blog](https://www.midiaresearch.com/blog/jersey-club-in-berlin-behind-the-scenes-and-sounds-of-2025)
- **Sounds of 2026 (2025 data):** afro house was "sound of the year" at +778% (6.7M downloads, 1.3M searches), about 70% of all house growth. House rose from 5th (2023) to 2nd most-downloaded genre. Melodic house surged. Speed garage, hard techno, jump-up DnB and hard dance all grew by triple digits. Hip hop is still No. 1 (third year running) but trap's growth is slowing as throwback and experimental styles rise. Pop is back in the top three via genre-blending (bedroom pop +297%). Seoul is the largest market outside the US (7.1M downloads). West Asia/North Africa is the fastest-growing region. — [MIDiA](https://midiaresearch.com/sounds-of-2026); [RouteNote](https://routenote.com/blog/splice-midia-sounds-of-2026-report/); [Mixmag](https://mixmag.net/read/hip-hop-most-downloaded-genre-on-splice-for-third-year-in-a-row-news)
- **TikTok-era formats:** sped-up versions of songs became a de facto Gen-Z format on TikTok (reported 2022), letting fans join in the way club remixes did for millennials. — [YPulse](https://www.ypulse.com/newsfeed/2022/11/14/sped-up-versions-of-songs-are-taking-over-tiktok-and-creating-their-own-genre-of-music-popular-with-gen-z/) "Krushclub" (classic EDM + house + Jersey club) is cited as a 2024 TikTok microgenre. — [EDMProd](https://www.edmprod.com/krushclub/)

### Cited Findings: AI music
- **Uploads (Deezer):** fully AI-generated tracks as a share of daily uploads went from ~10% (Jan 2025) to 18% (Apr 2025), 28% (Sep 2025), 34% (Nov 2025; ~50k/day), 39% (Jan 2026; ~60k), 44% (Apr–May 2026; ~75k), and over 50% by mid-2026 (~90k/day). — [TechCrunch, Apr 2026](https://www.techcrunch.com/2026/04/20/deezer-says-44-of-songs-uploaded-to-its-platform-daily-are-ai-generated/); [DJ Mag, >50%](https://djmag.com/news/ai-generated-music-surpasses-50-of-daily-uploads-deezer); [Paste](https://www.pastemagazine.com/music/deezer/over-half-of-new-deezer-uploads-are-ai-generated)
- **AI acts reaching listeners:** The Velvet Sundown (AI psych-rock "band", June 2025) passed 1M monthly Spotify listeners before admitting on 5 July 2025 that its music was AI-generated. — [The FADER](https://www.thefader.com/2025/07/07/the-velvet-sundown-ai-band-story-explained) Breaking Rust (AI country) hit No. 1 on Billboard Country Digital Song Sales with "Walk My Walk". — [Iowa Public Radio](https://www.iowapublicradio.org/studioone/news/2025-12-08/ai-generated-music-breaking-rust-velvet-sundown-teddy-swims) Luminate 2025 lists Xania Monet as the first AI act on a Billboard radio chart, Breaking Rust at 72.8M streams, Cain Walker at 48.1M. In H1 2026: Breaking Rust's "Livin' on Borrowed Time" had 19M US streams, and an AI "Papaoutai" (Chill77/Unjaps/Mikeeysmind, an afro-house rework of Stromae) had 210.7M streams outside the US. — [AP via News4Jax](https://www.news4jax.com/entertainment/2026/01/14/music-streams-hit-5-trillion-in-2025-christian-rock-and-latin-lead-growth-in-the-us/); [AP via WTOP](https://wtop.com/entertainment/2026/07/latin-and-country-surge-in-the-us-as-more-music-is-being-streamed-than-ever-before/)
- IFPI's 2026 position: labels want AI partnerships that "support and enhance creativity, not replace it." — [Music Week](https://www.musicweek.com/public_html/index.php/labels/read/ifpi-global-recorded-music-revenue-up-6-in-2025-as-industry-embraces-the-future-on-ai/093789)

### Inferences
- **What counts as "current" (2025–2026) for the skill:** (1) Latin urban plus traditional fusion (Bad Bunny model), corridos tumbados / Regional Mexican; (2) country and country-rap crossover; (3) K-pop as global pop (Golden, APT.); (4) Afro house and amapiano-pop, afrobeats spreading into Latin America; (5) Brazilian funk / Brazilian phonk / montagem; (6) faster club tempos: speed garage, hard techno, Jersey club, jump-up DnB, hard dance; (7) bedroom pop and genre-blended pop; (8) rock and Christian growth (largely catalog and worship); (9) trap plateauing, with pluggnb, rage and throwback boom bap as the youth edges; (10) AI-generated tracks, especially in country, afro house reworks and lo-fi/functional music.
- **Genre fragmentation:** Luminate's falling English share and R&B/hip-hop share, Splice's "micro-communities" finding, and Every Noise's 6,291 genres all point the same way: the mainstream is a federation of scenes, and fusion is the default.
- Trend data has a short shelf life. The skill should state the data year and say that 2027+ may differ.

### Gaps
- No Billboard genre-share analysis or Pitchfork/Guardian/Rolling Stone trend essay was fetched (Billboard pages were not retrieved directly).
- K-pop's and afrobeats' exact US shares for 2025 were not found in Luminate summaries.
- Música mexicana 2025 US trend: only a weak blog source claims growth; anecdotal reports of a 2025 US cool-off were not verified either way.
- No primary data on how big "sped-up"/nightcore edits are on streaming in 2025–2026.

---

## Q5. Quick "genre identification by ear" decision tree

### Takeaway
Identify by the order a listener's ear locks on: (1) tempo plus where the kick and snare fall (backbeat / four-on-the-floor / half-time / dembow / broken), (2) subdivision and swing, (3) bass type, (4) one or two signature timbres, (5) vocal style. Then check the scene, place and era to choose between close relatives. This tree is synthesis and convention (the BPM bands match the existing recipe notes); it has no academic source.

### Cited Findings
- Anchors with sources: house 115–130 BPM with 4/4 kick and off-beat hats ([Wikipedia: House](https://en.wikipedia.org/wiki/House_music)); jungle ~160–180 with chopped breaks and reggae bass ([Wikipedia: Jungle](https://en.wikipedia.org/wiki/Jungle_music)); UK drill ~140 with sliding 808s and syncopated hats/snares ([Wikipedia: Drill](https://en.wikipedia.org/wiki/Drill_music)); reggaeton = dembow 3+3+2 over 4/4 ([Wikipedia: Reggaeton](https://en.wikipedia.org/wiki/Reggaeton)); Jersey club = stuttering kicks + bed squeak; Brazilian phonk = cowbell + funk percussion ([Splice](https://splice.com/blog/?p=34341)); amapiano = log drum + piano runs ([Grammy.com](https://grammy.com/news/tyla-winner-best-african-music-performance-water-2024-grammys-meaning)).

### Inferences: decision tree (defaults; see recipe notes for exact grids)
```
STEP 1 - Is there a steady kick on every beat (four-on-the-floor)?
 YES -> STEP 2A (house/techno/trance family)    NO -> STEP 3

STEP 2A - Tempo?
  100-115  -> amapiano (log-drum bass, shakers, jazzy keys, sparse, kick often off the 4/4 or soft)
              | nu-disco/disco (live bass, strings, 110-120)
  115-126  -> house family:
              - deep house: warm chords (min7/9), soft hats, ~118-124
              - afro house: tribal/latin percussion, minor vocal chants, 120-124
              - tech house: rolling percussive bass, groove-first, 124-128
              - melodic house/techno: arpeggios, long builds, 120-124
              - Chicago/classic: 909, piano stabs, gospel vocals
  126-135  -> techno (dark, hypnotic, minimal harmony, 128-135; Detroit = chords/strings)
              | Brazilian phonk/funk (cowbell melody, distorted 808, 125-135; kick often NOT strict 4/4)
              | speed garage (UKG shuffle + 4/4 + reese/"warp" bass, ~130-135)
  135-150  -> trance (supersaw, rolling 16th bass, breakdown + uplifting chords, 136-142)
              | hard techno (distorted kick, 140-155) | hard dance/hardstyle (reverse-bass kick, 150+)
STEP 3 - Where does the main snare/clap land, and at what felt tempo?
  Snare on 2 & 4, ~60-100 BPM:
     - swung 16ths, sampled drums, dusty -> boom bap (85-95) / lo-fi (70-90, vinyl, jazzy 7ths)
     - live kit, clean backbeat -> pop/rock/soul/R&B (check guitars vs keys vs synths)
     - "the One" heavy, syncopated slap bass, horn stabs -> funk (95-115)
     - triplet-flavoured, offbeat guitar "skank" on & of each beat -> reggae (60-90)
  Kick-snare 3+3+2 tresillo ("boom-ch-boom-chick"), 88-105 -> reggaeton/dembow (Latin);
     dancehall if patois toasting, afrobeats if 95-115 with log/shaker/conga swing and highlife guitar
  Snare/clap on beat 3 of a 140-ish grid (half-time feel ~70):
     - rolling hi-hats (1/16, 1/32, triplet rolls), long 808 -> TRAP (130-160 = 65-80 felt)
     - syncopated off-grid snares + sliding 808 glides, dark minor/Phrygian, ~140 -> UK/NY DRILL
       (Chicago drill: 60-70 felt, brassy/bell synths, less slide)
     - spacey bell leads, simple 808, light hats, ~150 -> plugg; + R&B chords -> pluggnb
     - distorted synth leads, aggressive, 150-170 -> rage
     - Memphis vocal chops + cowbell + drifting 808 -> phonk
     - wobble/growl sub-bass drops, ~140 -> dubstep/riddim
  Broken/skippy kick with shuffled hats, 130-140 -> UK garage/2-step (pitched vocal chops,
     organ-ish bass); grime if square-wave bass, 140, MC
  Kick stutter triplets, bed squeak, chopped vocal loops, 130-150 -> JERSEY CLUB (Baltimore club if
     more breakbeat/"Think" break, ~130)
  Breakbeat snare on 2 & 4 at 160-180 (felt 80-90):
     - chopped Amen-type breaks + reggae sub -> jungle
     - tight 2-step DnB beat: liquid (pads, soul vocal), neurofunk (complex reese), jump-up (wobbly
       "bouncy" bass hooks), dancefloor
  No drums or barely any -> ambient / cinematic underscore / drone; check orchestra + hits/braams
     for trailer music
STEP 4 - Confirm with timbre & vocal cues
  steel/pedal guitar, fiddle, banjo, twang -> country (+ trap drums = country-trap)
  accordion + bajo sexto/requinto, narrative Spanish vocal -> norteño/corridos (+ trap 808 = tumbados)
  saturated 80s synths, gated snare -> synthwave/retro-pop
  pitched-up vocal, glitch, extreme compression -> hyperpop; whole song sped up/pitched -> sped-up edit
  supersaw drop with chopped vocal "chords", sidechain -> future bass / EDM pop
  big swung jazz harmony (ii-V, extensions), walking bass, ride cymbal -> jazz
  12-bar I-IV-V with dominant 7ths, blue notes -> blues / blues-rock
STEP 5 - Use place/era/language to pick between close relatives (UK vs NY drill, afro house vs amapiano,
  Brazilian phonk vs Memphis phonk) and report hybrids as "carrier + colour" (e.g. "trap-carrier
  with country colour").
```

### Gaps
- No peer-reviewed by-ear identification scheme exists to validate this tree against; MIR results (Q1) suggest even trained systems confuse adjacent genres, so the skill should give a ranked guess with the cues it used.
- BPM bands differ between sources; the existing recipe notes have the per-genre ranges that should take priority.
