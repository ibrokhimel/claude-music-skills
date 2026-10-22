# Latin American Genres (excluding reggaeton/dembow) — FL Studio Recipe Cards

Scope: salsa, son cubano, mambo/cha-cha-chá, bachata, merengue, cumbia (Colombian, Mexican, villera, digital), vallenato, bossa nova, samba, MPB, baile funk / Brazilian funk, sertanejo, tango/electrotango, regional Mexican (banda, norteño, mariachi, corridos tumbados), Latin trap, Latin pop, Latin house/moombahton. Reggaeton/dembow, trap and house were covered earlier (see `research_notes\Music theory and beat making\`) and are only cross-referenced.

GRID CONVENTIONS USED BELOW (read first):
- **4/4 grid** (default): 16 steps = one 4/4 bar of 16ths. Step 1 = beat 1, 5 = beat 2, 9 = beat 3, 13 = beat 4. FL BPM = quoted BPM.
- **CYCLE16 grid** (Cuban clave genres, bossa, samba): 16 steps = ONE FULL 2-bar clave/partido cycle. Each step = an 8th note at the tempo dancers/US charts quote (= a 16th in Brazilian 2/4 notation). Odd steps (1,3,5,...,15) = the 8 dancer counts. **In FL: set BPM to half the quoted tempo and program it as one 16-step bar** (e.g. salsa quoted 190 BPM → FL 95 BPM), or keep the quoted BPM and spread the pattern over 2 bars at 8th-note resolution. Each card states the FL BPM explicitly.
- **12-step grid** (6/8, 3/4): stated per card.
- Symbols: X accent, x normal, g ghost, . rest, o open hat; for hand drums S = slap, O = open tone, H = heel, T = tip/toe, B = bass tone.
- Labels: (sourced) = number/claim from the cited page; (convention) = standard practice not verified by a source this session; (derived) = my calculation/inference.

## Q1–Q3: Genre recipe cards — clave/rhythmic cells as grids, harmony, bass, melody, instruments and DAW emulation

### Takeaway
Almost every genre here is identified first by its percussion "time-line" (clave, güira/guacharaca scrape, surdo accent, tamborzão, oom-pah, 3-3-2) and second by its bass placement (anticipated tumbao in Cuban styles, root-fifth on the beat in cumbia/norteño, surdo-like thumb in bossa). Get those two right at the correct tempo and the genre reads; get them wrong and no amount of correct instruments will fix it.

### Cited Findings

#### A. The core Afro-Cuban cells (shared by son, salsa, mambo, cha-cha, Latin house, Latin jazz)
- Son clave 3-2 = strokes on 1, 2&, 4 | 2, 3 of a two-bar cycle; 2-3 reverses the bar order. Rumba clave delays the third stroke of the 3-side by one pulse; bossa nova clave is son clave with the second note of the 2-side delayed one pulse (usually played as a snare cross-stick); tresillo = the first three strokes of son clave — [Wikipedia: Clave (rhythm)](https://en.wikipedia.org/wiki/Clave_(rhythm))
- The tresillo is the rhythmic basis of the ostinato bass tumbao in son, son montuno, mambo, salsa and Latin jazz; the tumbao supplies harmony and dance pulse while avoiding a plain downbeat pattern — [Wikipedia: Tumbao](https://www.wikipedia.org/wiki/Tumbao); [Soundbrenner: Tumbao](https://www.soundbrenner.com/blogs/articles/tumbao)
- On piano the repeated syncopated figure is the montuno; it outlines chords and interlocks with percussion and bass, and the piano can support or cross clave hits with anticipations — [Soundbrenner: Tumbao](https://www.soundbrenner.com/blogs/articles/tumbao); [Piano With Jonny: Piano montunos](https://pianowithjonny.com/piano-lessons/piano-montunos-the-complete-guide/)
- Cáscara is the eighth-note timbale shell pattern that works with clave; it uses high (rim) and low (shell) stroke heights — [Soundbrenner: Cascara](https://www.soundbrenner.com/blogs/articles/cascara). NOTE: that page's summarized stroke list (X--X--X- | -XX-X--X) has only 7 strokes and conflicts with the 10-stroke cáscara I give below as (convention); verify against [Wikipedia: Timbales](https://en.wikipedia.org/wiki/Timbales) notation images.

Grids (CYCLE16, each step = 8th note; FL BPM = quoted/2):
```
Son clave 3-2    X . . x | . . x . | . . x . | x . . .   (steps 1,4,7 | 11,13)  (sourced positions)
Son clave 2-3    . . x . | x . . . | x . . x | . . x .   (steps 3,5 | 9,12,15)  (derived: bar order swapped)
Rumba clave 3-2  X . . x | . . . x | . . x . | x . . .   (steps 1,4,8 | 11,13)  (sourced: 3rd stroke delayed 1 pulse)
Bossa clave      X . . x | . . x . | . . x . | . x . .   (steps 1,4,7 | 11,14)  (sourced: 2-side 2nd note delayed)
Tresillo         X . . x | . . x . |  (first half only)                         (sourced)
Cáscara 3-2      X . x x | . x . x | x . x . | x x . x   (10 strokes; 2-3 = swap halves) (convention)
Bongo bell       X . x . | X . x . | X . x . | X . x .   (quarter notes; accent "mouth" on counts 1,3,5,7) (convention)
Conga tumbao     H T S T | H T O O | H T S T | H T O O   (slap on 2, two opens on 4 & 4&; per 4/4 bar) (convention)
Bass tumbao      . . . x | . . X . | . . . x | . . X .   (2& and 4 each bar; note on 4 = NEXT chord's root, tied over the bar line; no beat 1) (convention, consistent with sourced "avoids downbeat")
Güiro            X x X x | X x X x | X x X x | X x X x   (long on beat / short on &; in real playing long-short-short) (convention)
Piano montuno    X . x x | . x . x | . x x . | x . x x   (octave-doubled broken chords, anticipations on steps 15-16 into the next cycle) (convention)
```

#### B. Son cubano
- Identity: rural Oriente (eastern Cuba) roots, urbanized in Havana in the 1920s sextetos/septetos; later conjunto format (Arsenio Rodríguez) added piano, conga and trumpets; 1997 Buena Vista Social Club revival. Refs: Septeto Nacional (Ignacio Piñeiro) "Échale salsita", Arsenio Rodríguez "Bruca maniguá", Buena Vista Social Club "Chan Chan". By ear: guitar-like tres ostinato, bongó martillo, maracas, upright bass with anticipated tumbao, call-and-response coro in the montuno — history as (convention; not fetched this session). Tumbao/tresillo basis (sourced above).
- Tempo/feel: 85–120 BPM quarter (convention; FL CYCLE16 at 43–60, or 4/4 grid at quoted BPM over 2 bars). Straight 8ths, never swung; clave usually 2-3.
- Harmony: I–IV–V7 two-chord/three-chord vamps; i–III–iv–V7 (Dm–F–Gm–A7) as in "Chan Chan"; harmonic rhythm 1 chord per bar or 2 per bar in montuno (convention).
- Melody/vocals: lead sonero + 2–3 voice coro in parallel thirds; montuno section = short coro answered by improvised pregón (convention).
- Instruments: tres (3 doubled courses — emulate with nylon/steel guitar sample doubled an octave up + slight chorus), bongó, maracas, claves, contrabass, trumpet (conjunto). Emulate tres with FL "FL Keys"/sample guitar + octave layer; use real percussion one-shots (congas/bongos packs) rather than GM sounds.
- Bass: tumbao (grid above); on old sextet records the bass also plays on beat 1 more often (convention).
- Form: intro (tres) → largo/verse (16–32 bars) → montuno (coro/pregón, open-ended) → trumpet solo → coda; 3–5 min (convention).
- FL steps: (1) FL BPM 50, 16-step clave 2-3 on claves sample. (2) Bongo martillo: 8ths all steps with open tone on step 7/15. (3) Tres guajeo: 2-bar arpeggiated 8ths following the chords, anticipating chord changes by an 8th. (4) Bass tumbao, tied note across bar. Common fake-sounding mistakes: clave reversed against the melody ("cruzado"), bass on every downbeat, quantized dead-stiff maracas with no long-short accent.

#### C. Salsa (dura, romántica, modern)
- Identity: New York 1960s–70s (Fania Records era) from son montuno, mambo and Puerto Rican influences; Héctor Lavoe & Willie Colón, Celia Cruz, Rubén Blades, Eddie Palmieri; salsa romántica 1980s (Frankie Ruiz, Eddie Santiago); modern Marc Anthony, Víctor Manuelle (history as convention). Refs: Willie Colón & Héctor Lavoe "El Día de Mi Suerte", Rubén Blades "Pedro Navaja", Marc Anthony "Vivir Mi Vida", Bad Bunny "BAILE INoLVIDABLE" (2025). By ear: fast clave-locked groove with cowbell on quarters in the montuno, piano montuno, anticipated bass, trombone/trumpet section riffs (mambos), coro-pregón.
- Salsa on Bad Bunny's 2025 album DeBÍ TiRAR MáS FOToS is part of a broader salsa resurgence also visible in Luis Fonsi, J Balvin, Rauw Alejandro and Karol G releases — [Consequence](https://concerts.consequence.net/articles/bad-bunny-wins-2026-grammy-album-of-the-year)
- Tempo: 160–220 quoted BPM; dura 180–210, romántica 150–180 (convention). FL CYCLE16 at 80–105. Meter cut-time, straight; clave 2-3 or 3-2 set by the melody.
- Harmony: minor montunos i–iv–V7 (Am–Dm–E7); major I–IV–V–IV (C–F–G–F, one chord per 2 counts); ii–V vamps (Dm7–G7); romántica adds pop ballad progressions with maj7/add9 (convention).
- Melody/vocals: sonero improvises pregones between short coro refrains; horn mambos are 2- or 4-bar riffs layered in counterpoint, rhythmically aligned to clave (convention).
- Instruments: piano, bass (baby bass/upright or electric), congas, bongó (+ hand bell in montuno), timbales (cáscara in verses, mambo bell in montuno), güiro, maracas, 2–4 trumpets and/or trombones (Colón/Palmieri trombone sound), lead + coro voices. DAW: dedicated Latin percussion multisamples (multi-velocity slaps/opens are essential), real brass libraries (FL stock brass sounds fake — layer at least two trumpet patches + humanize), FL Grand Piano/"FL Keys" bright piano doubled in octaves for montuno.
- Rhythm: see Section A grids (all apply). Verse: timbales on cáscara, bongó martillo; montuno/coro: timbal switches to bell, bongocero to hand bell — the section change is audible as an energy lift (convention).
- Bass: tumbao on 2& and 4, anticipating chords; root/fifth of upcoming chord (convention; tumbao principle sourced above).
- Form: intro (horns/piano) → verses (canto) 32–48 bars → coro-pregón montuno 32+ bars → mambo (horn section) 8–16 bars → moña (layered horn riffs) → coro return → coda/cierre; 4–6 min (convention).
- Mix: live-room ambience, piano and horns bright and forward, congas panned (tumbadora L/R), cowbell present but not harsh; modest loudness vs urban (convention).
- Subgenres: salsa dura (hard, horn-heavy, faster), salsa romántica (slower, smoother strings/synths, love lyrics), timba (Cuban 1990s: funk/rock bass slaps, gear-shifting "presiones", busier), salsa choke (Colombian Pacific, urban-dance hybrid) (convention).
- FL steps: (1) FL 95 BPM, CYCLE16. (2) Program clave first (even if muted later), then conga tumbao, cáscara/bell, güiro. (3) Bass tumbao with tied anticipations. (4) Piano montuno in octaves, aligned with clave. (5) Horn riff answering vocal coro. Fake tells: kick drum four-on-floor, bass on beat 1, clave direction flipping between sections, MIDI brass without breath/legato, everything hard-quantized (congas need ±5–15 ms and velocity variation).

#### D. Mambo and cha-cha-chá
- Cha-cha-chá was introduced by Enrique Jorrín (violinist with charanga Orquesta América) in the early 1950s, developed from the danzón-mambo; he made melodies that marked the first downbeat strongly with less syncopation, and the dancers' triple step gave the onomatopoeic name — [Wikipedia: Cha-cha-cha (dance)](https://en.wikipedia.org/wiki/Cha-cha-cha_(dance))
- In 1953 many orchestras played Pérez Prado's mambo "El cerezo rosa" as a cha-cha-chá, and Prado recorded it that way too — [Wikipedia: Cha-cha-cha (dance)](https://en.wikipedia.org/wiki/Cha-cha-cha_(dance))
- Mambo identity (convention): Cachao/Arcaño danzón-mambo (1938) → Pérez Prado big-band mambo ("Qué Rico el Mambo", "Mambo No. 5") and NYC Palladium bands (Machito, Tito Puente, Tito Rodríguez). By ear: big-band saxes vs trumpets in clave-locked riffs, shouts, very fast. Cha-cha: charanga flute + violins in unison, moderate tempo, clear "4-&-1" triple feel.
- Tempo: mambo 180–210 quoted (convention; FL CYCLE16 90–105); cha-cha 112–128 BPM (convention; ballroom cha-cha ≈ 120–128).
- Harmony: major-key I–V7 and ii–V vamps; mambo riffs built on dominant 7ths and 6th chords; cha-cha melodies diatonic and singable (convention).
- Cha-cha grid (4/4 grid, ~120 BPM) (convention):
```
Cowbell (cencerro) X . . . | x . . . | X . . . | x . . .
Güiro              X . . . | x . x . | X . . . | x . x .   (long on 1/3, short-short on 2, 2& / 4, 4&)
Conga              H . T . | S . T . | H . T . | O . O .   (opens on 4, 4& = the "cha-cha")
Timbal/paila       x . x . | x . x . | x . x . | x . x .   (8ths on shell or bell)
Bass               X . . . | . . . . | x . . . | . . x .   (1, 3 and pickup on 4& — less anticipated than salsa)
```
- Instruments: charanga = flute, violins, piano, bass, timbales, güiro, conga (cha-cha); big band = 4–5 saxes, 4 trumpets, trombones, rhythm section (mambo).
- FL steps: (1) cha-cha at 120 straight 16ths, cowbell quarters first. (2) Flute + violin unison melody with slight detune. (3) Mambo: write two independent horn riffs (sax low, trumpets high) each 2 bars, staggered against clave. Fake tells: swing applied (never), flute samples with no breath attacks.

#### E. Bachata (traditional and modern)
- Bachata songs use three percussion "rhythms" by section: derecho (verses: bongos and güira play all eight 8th notes; bongo accents beats 1, 3, 4 with the lowest-pitched hit on 4; güira equal emphasis), majao (bongo and güira drop the upbeats and play only the four downbeats, güira with longer scrapes; bongo low hit still on 4) and mambo (instrumental break where players improvise and the singer usually stops) — [Ubisoft/Rocksmith: Breaking Down Bachata Pt 2](https://www.ubisoft.com/en-us/game/rocksmith/plus/news-updates/3DgS3IltlNGQk5RL2CvHgZ/breaking-down-bachata-part-2-percussion); guitar roles in [Part 3](https://www.ubisoft.com/en-ca/game/rocksmith/plus/news-updates/42YP2fih1AY3wVyZhWhLrZ/breaking-down-bachata-part-3-guitars); overview [Part 1](https://www.ubisoft.com/en-au/game/rocksmith/plus/news-updates/4JGuRsatSHe2lZ4XuGxuUF/breaking-down-bachata-part-1-overview)
- Identity (convention): Dominican Republic, 1960s guitar bolero roots (José Manuel Calderón), stigmatized "amargue" music of the 1970s–80s; electric guitar era (Blas Durán, Antony Santos, Raulín Rodríguez); Juan Luis Guerra "Bachata Rosa" (1990) polish; urban/modern bachata via Aventura "Obsesión" (2002), Romeo Santos "Propuesta Indecente", Prince Royce "Stand By Me". By ear: bright, chorus-drenched requinto guitar arpeggios between vocal lines + continuous güira scrape + bongo.
- Tempo: 120–140 BPM traditional, modern/sensual 110–130 (convention). Straight 16ths (requinto) over even 8ths.
- Harmony: I–IV–V7 (C–F–G7), i–iv–V7 (Am–Dm–E7), modern i–VI–III–VII (Am–F–C–G); harmonic rhythm 1 chord per bar; frequent minor keys and V7 with b9 passing (convention).
- Melody/vocals: crying/tender tenor, melisma at phrase ends, falsetto in modern style; requinto plays answer phrases in 3rds/6ths with hammer-ons and fast 16th-triplet runs (convention).
- Instruments: requinto (lead electric/nylon-ish guitar, heavy chorus), segunda (rhythm guitar: arpeggiated/chopped), electric bass (melodic, syncopated), bongó, güira; modern adds pads, 808-ish subs, reggaeton-hybrid drums. DAW: clean electric guitar sample + Chorus + short plate; FL "Fruity Chorus"; güira = metal scraper loop (use real loops — synthesized noise sounds fake).
- Grids (4/4, ~125 BPM):
```
DERECHO (verse)                                           (sourced: all 8ths; accents 1,3,4; low tone 4)
Güira        x . x . | x . x . | x . x . | x . x .
Bongo        X . x . | x . x . | X . x . | B . x .     (B = low/bass-pitched hit on beat 4)
MAJAO (chorus)                                            (sourced: downbeats only)
Güira        X . . . | X . . . | X . . . | X . . .     (longer scrapes)
Bongo        x . . . | x . . . | x . . . | B . . .
Bass         X . . . | . . x . | x . . . | . . x .     (1, 2&, 3, 4&) (convention)
```
- Form: intro (requinto riff 4–8 bars) → verse (derecho) → chorus (majao) → verse → chorus → mambo/instrumental break (8–16 bars, requinto/bongo improvisation, singer silent) → chorus → outro; 3.5–4.5 min (sections sourced; bar counts convention).
- Subgenres: traditional/amargue (rawer, acoustic-electric, rural), bachata urbana/sensual (Aventura/Romeo: R&B harmony, polished, softer drums), bachata-reggaeton hybrids (dembow under requinto) (convention).
- FL steps: (1) 125 BPM. (2) Güira + bongo derecho loop, majao alternate for choruses. (3) Requinto arpeggio 16ths on chord tones with chorus/delay. (4) Syncopated bass. (5) Section-switch drums for the mambo. Fake tells: no rhythm change between verse and chorus, dry requinto, using a drum kit backbeat.

#### F. Merengue
- Merengue típico (perico ripiao) is the oldest style, from the Dominican Republic; instruments accordion, bass guitar, güira, conga, tambora — [Wikipedia: Merengue típico](https://en.wikipedia.org/wiki/Merengue_t%C3%ADpico)
- The tambora is a two-headed horizontal drum played with one stick and one bare hand (open tones, slaps, rim/shell); the güira interlocks with it; the basic merengue feel is a straightforward 1-2, 1-2 beat; the paseo is a slow promenade introduction now mainly in folkloric settings — [Wikipedia: Merengue típico](https://en.wikipedia.org/wiki/Merengue_t%C3%ADpico); [Soundbrenner: Merengue rhythm](https://www.soundbrenner.com/blogs/articles/merengue-rhythm); [All Around This World: Tambora](https://www.allaroundthisworld.com/instrument/tambora/)
- Identity (convention): orquesta merengue — Johnny Ventura, Wilfrido Vargas, Juan Luis Guerra ("Ojalá que llueva café"), Los Hermanos Rosario, Elvis Crespo "Suavemente". By ear: very fast duple pulse, relentless güira 16ths, tambora roll into the downbeat, rapid alto-sax riffs in parallel 3rds.
- Tempo: 130–170 BPM (convention; perico ripiao can exceed 160). Meter 2/4 felt in 4/4 grid, straight.
- Harmony: I–V7 vamps (C–G7), I–IV–V7; jaleo section alternates two chords (convention).
- Grid (4/4, ~150 BPM) (convention):
```
Güira        X . x x | X . x x | X . x x | X . x x     (long scrape + two shorts per beat)
Tambora      x . S . | x . S . | x . S . | x x x x     (stick/rim with hand slap; roll steps 13-16 every 2nd bar into beat 1)
Conga        . . S . | . . S . | . . O O | . . O .
Bass         X . . . | . . . . | x . . . | . . x .     (roots on 1 & 3, anticipating pickup 4&)
Kick (orq.)  X . . . | X . . . | X . . . | X . . .     (modern orchestra/merengue de calle often quarter kicks)
```
- Form: paseo (intro, optional) → merengue (verse/chorus) → jaleo (call-and-response section with horn/sax mambos and piano guajeos, energy peak); 3–4 min (paseo/jaleo naming convention; paseo sourced above).
- Subgenres: típico/perico ripiao (accordion-led, raw), orquesta merengue (horns, piano), merengue de calle/mambo urbano (bridges to dembow — cross-ref reggaeton/dembow notes) (convention).
- FL steps: 150 BPM; güira loop + tambora with roll; bass root/fifth; two-alto-sax riff in 3rds 16ths; jaleo after second chorus. Fake tells: too slow, missing tambora roll, saxes not tight/doubled.

#### G. Cumbia (Colombian, Mexican, villera, digital)
- Guacharaca pattern: down-stroke on the beat, then a down + quick up stroke as two 16ths on the "&-a"; repeated on each beat; practice exercise tempo 88 BPM — [Music Will: Cumbia lessons PDF](https://jamzone.musicwill.org/wp-content/uploads/2021/04/Cumbia-Print-Lessons-2.pdf)
- Cumbia tempo sits around 80–110 BPM; guacharaca gives a dry even grain, tambora gives weight with open/muted strokes, llamador keeps a compact offbeat — [Suno: Cumbia](https://suno.com/music-library/genres/cumbia) (low-authority AI-tool genre page; treat as supporting only)
- Cumbia villera emerged from the villas miserias (shantytowns) — [The National](https://www.thenational.ae/arts-culture/music/zzk-label-takes-genre-from-the-music-of-the-poor-to-the-next-big-thing-1.482304)
- Digital cumbia was born in late-2000s Buenos Aires (Zizek Club); synths, drum machines and samples replace/enrich traditional instruments, mixing dub, villera, Andean folk, bass music and ambient — [Festt: Digital Cumbia](https://festt.io/en/festivals/genre/digital-cumbia); ZZK Records founded March 2008, artists Chancha Vía Circuito, El Remolón, Fauna, Tremor — [Sounds and Colours](https://soundsandcolours.com/articles/argentina/classic-yet-modern-zzk-records-and-digital-cumbia-10942/); Chancha Vía Circuito (Pedro Canale) explores minimal digital cumbia with dub, IDM and downtempo — [Sounds and Colours: Los Pastores](https://soundsandcolours.com/articles/argentina/chancha-via-circuito-los-pastores-mixtape-1395/)
- Identity (convention): Colombian Caribbean coast; folk ensemble = gaita/millo flute, tambor alegre, llamador, tambora, maracas/guacharaca; big-band cumbia of Lucho Bermúdez/Pacho Galán; Los Corraleros de Majagual; Totó la Momposina. Mexican cumbia: Los Ángeles Azules, Celso Piña (accordion), Selena ("Baila Esta Cumbia"), cumbia sonidera (DJ shout-outs, echo FX), cumbia rebajada (slowed). Villera: Damas Gratis (Pablo Lescano keytar), Yerba Brava. By ear: steady "chi-ki-chi" scraper on every beat, bass bouncing root-fifth, offbeat llamador, accordion/keyboard melody, laid-back mid tempo.
- Harmony: I–V7 two-chord vamps (C–G7), I–IV–V7; minor cumbias i–iv–V7 or Andalusian i–VII–VI–V (Am–G–F–E) in Peruvian/Andean-influenced styles (convention).
- Grid (4/4, ~95 BPM; Colombian folk often written in cut time) (guacharaca sourced; rest convention):
```
Guacharaca/güiro X . x x | X . x x | X . x x | X . x x
Llamador         . . x . | . . x . | . . x . | . . x .
Tambora          X . . . | . . . . | x . g . | . . . .
Conga (Mex.)     . . . . | S . . . | . . O O | S . . .
Bass             X . . . | . . x . | X . . . | . . x .     (root on 1, 5th on 3, 8th pickups)
Timbal (villera) . . . . | x . . . | . . . . | x . . .     (plus fills; Casio-style keys on offbeats)
Kick (digital)   X . . . | . . . . | X . . . | . . . .     (dub-style 1 & 3, sub bass)
```
- Instruments in DAW: guacharaca/güiro loops (real), accordion (Mexican/vallenato style button accordion sample), Farfisa/organ or cheap Casio keyboard patch (villera/sonidera: FL "3x Osc" square/saw with vibrato works), gaita flute → pan-flute/ocarina samples, dub delays (FL "Fruity Delay 3") for digital cumbia.
- Form: intro (accordion/keys riff) → verse → chorus → instrumental riff break; repetitive 3–4 min; sonidera adds spoken saludos over breaks (convention).
- Subgenre differences: Colombian (acoustic drums/flute or big band, brighter, airy), Mexican (accordion/keyboards, güiro, round electric bass, romantic vocals, slower 85–100), villera (cheap synth keys, harsh timbales, street lyrics, ~95–100), rebajada (pitched-down, slow, smeared), digital/electro-cumbia (drum machine, sub-bass, dub FX, 85–105) (convention).
- FL steps: guacharaca first; root-fifth bass; offbeat llamador; accordion/keys riff in thirds; for digital: replace live drums with 808 kick on 1 & 3 + filtered guacharaca loop + dub delay throws. Fake tells: kick on all four beats (that's moombahton/house), scraper without the 16th "&-a" flick, too fast.

#### H. Vallenato
- Originated on Colombia's Caribbean coast; accordion + guacharaca + caja vallenata; four "airs": son and paseo in 2/4, merengue and puya in 6/8; son is slow and mournful, accented on the accordion's left-hand bass notes; puya is played faster in recent decades and features solos for each of the three instruments — [Wikipedia: Vallenato](https://en.wikipedia.org/wiki/Vallenato); [Wikipedia: Caja vallenata](https://en.wikipedia.org/wiki/Caja_vallenata)
- Identity (convention): Alejo Durán, Diomedes Díaz, Binomio de Oro, Silvestre Dangond, Carlos Vives (vallenato-pop "La Gota Fría"). By ear: diatonic button accordion constantly ornamenting, scraper, small hand drum (caja), romantic storytelling vocals.
- Tempo: paseo 90–115, puya 120–170 (felt in 6/8) (convention).
- Harmony: I–IV–V7 major, keys set by accordion tuning; accordion fills in 3rds/6ths (convention).
- Grid paseo (4/4 grid = two 2/4 bars, ~100 BPM) (convention): `Guacharaca X . x x | X . x x | X . x x | X . x x`; `Caja O . S . | O . S . | O . S . | O . S .`; `Bass X . . . | x . . . | X . . . | x . . .` (root–fifth). Puya: 12-step 6/8 grid, guacharaca on every 8th with accents 1 and 4.
- FL: accordion sample with fast mordents/grace notes, guacharaca loop, caja = high conga/tom with slaps. Fake tells: piano-style accordion voicings with no bellows ornaments.

#### I. Bossa nova
- Emerged in Rio de Janeiro in the 1950s combining simple samba-derived rhythms with extended jazz harmony; one guitar pattern places upper chord notes on upbeats; surdo-derived bass foot/thumb pattern — [Premier Guitar: Brazilian guitar 101](https://www.premierguitar.com/rhythm-rules-brazilian-guitar-101); [JazzGuitar.be: Latin jazz guitar rhythms](https://jazzguitar.be/blog/latin-jazz-guitar-rhythms)
- Getz/Gilberto (João Gilberto with Stan Getz) won Grammy Album of the Year in 1965 — [Guinness World Records](https://www.guinnessworldrecords.com/world-records/782166-first-spanish-language-album-to-win-a-grammy-award-for-album-of-the-year)
- Identity (convention): João Gilberto, Tom Jobim, Vinícius de Moraes, Astrud Gilberto; refs "Chega de Saudade" (1958), "Desafinado", "The Girl from Ipanema". By ear: soft nylon guitar with syncopated chord plucks over a steady thumb bass, near-whispered vocal, rich maj7/9/13 harmony, brushes/cross-stick.
- Tempo: 120–144 BPM US quarter (cut time) = 60–72 in Brazilian 2/4 (convention). FL: CYCLE16 at 60–72 BPM. Straight (light "push" feel, not swing).
- Harmony: maj7, m7, 7(9), 7(13), 7(b9), m7b5, dim7, chromatic descending lines; e.g. Imaj7–II7–iim7–V7(b9) = Fmaj7–G7(9)–Gm7–C7(b9); ii–V chains; tritone subs (Gm7–Gb7–Fmaj7) (convention).
- Melody/vocals: stepwise, long notes over moving harmony, quiet intimate delivery, minimal vibrato (convention).
- Grid (CYCLE16, FL 65 BPM) (bossa clave sourced; rest convention):
```
Cross-stick   X . . x | . . x . | . . x . | . x . .   (bossa clave)
Kick/thumb    X . . x | X . . x | X . . x | X . . x   (surdo figure: dotted-8th + 16th; root on beats, 5th on pickups)
Shaker/hat    x x x x | x x x x | x x x x | x x x x   (soft, accent each beat)
Guitar chords x . . x | . . x . | . . x . | . x . .   (fingers follow clave; vary bar 2)
```
- Bass: alternates root (beat) and fifth (pickup before beat) like surdo; upright bass doubles thumb (convention).
- Form: AABA or ABAC 32-bar song forms, head–solo (sax/piano/guitar)–head; 2.5–5 min (convention).
- Mix: intimate, close-miked, little compression, short room reverb, quiet (convention).
- FL steps: nylon guitar sample (or FL "FL Keys" for Rhodes variant) with 4-note jazz voicings, thumb bass separate; brushes or cross-stick; vocal very close and soft. Fake tells: triads only, loud drum kit, swing quantize.

#### J. Samba (including partido alto)
- Partido alto is a samba variant/ pattern: one description is a reverse-bossa bar followed by the original bossa bar; hand patterns in samba centre on it — [JazzGuitar.be](https://jazzguitar.be/blog/latin-jazz-guitar-rhythms); partido alto has roots in jongo religious parties, present in samba from the 1930s, choral refrain + soloed/competitive verses, pandeiro with a dry palm snap in the head centre — [Wikipedia: Partido alto](https://en.wikipedia.org/wiki/Partido_alto)
- The surdo marks the low pulse; pandeiro and tamborim add quick accents — [Premier Guitar](https://www.premierguitar.com/rhythm-rules-brazilian-guitar-101)
- Identity (convention): Rio de Janeiro, early 20th c. (Donga "Pelo Telefone" 1917), escolas de samba (samba-enredo), samba-canção, pagode (Fundo de Quintal, Zeca Pagodinho), modern pagode (Thiaguinho, Menos é Mais). By ear: 2/4 with heavy LOW surdo on beat 2, buzzing 16th shakers/snares, cavaquinho strumming, call-and-response.
- Tempo (FL BPM = surdo pulse): pagode/samba de roda 90–110, samba-enredo/batucada 130–150 (convention).
- Harmony: major keys; I–VI7–ii–V7 (C–A7–Dm–G7), secondary dominants, 7-string guitar bass runs (baixaria) between chords; minor sambas i–iv–V7 (convention).
- Grid (4/4 grid = two 2/4 bars, step = 16th, FL BPM = surdo pulse) (convention unless marked):
```
Surdo 2a (mark)   x . . . | . . . . | x . . . | . . . .   (beat 1 of each 2/4 bar, muted/short)
Surdo 1a (low)    . . . . | X . . . | . . . . | X . . .   (beat 2 of each 2/4 bar = THE accent)
Pandeiro/ganzá    x g g X | x g g X | x g g X | x g g X   (accent the 4th 16th of each beat)
Tamborim          X . x x | . x . x | X . x x | . x . x   (teleco-teco style, variable)
Partido alto      . x . . | x . x . | x . . x | . x . .   (steps 2,5,7 | 9,12,14) — (convention; verify)
Caixa/snare       x g x g | x g x X | x g x g | x g x X
```
- Instruments in DAW: real samba percussion packs (surdos, caixa, repinique, tamborim, pandeiro, agogô, cuíca), cavaquinho sample (bright 4-string strums on 16ths), 7-string nylon guitar, banjo (pagode). FL stock drums cannot make surdo — use samples.
- FL steps: surdo beat-2 accent first; 16th pandeiro with accent; cavaquinho partido-alto rhythm; voices in unison chorus. Fake tells: kick on beat 1 being the loudest, 8th-note shakers, swing quantize (real samba has slight 16th "drag" on the 2nd and 3rd 16ths — humanize by hand, not swing knob).

#### K. MPB (Música Popular Brasileira)
- (Convention; no source fetched) Post-1965 umbrella for Brazilian song: Elis Regina, Chico Buarque, Caetano Veloso, Gilberto Gil (Tropicália 1967–68), Milton Nascimento, Djavan, Marisa Monte; contemporary Liniker, Anavitória. By ear: bossa-derived extended harmony + pop/rock/regional rhythms (baião, ijexá, frevo, maracatu), poetic lyrics, acoustic + band arrangements. Tempo varies 70–130. Baião cell (zabumba): `X . . x | . . x . | X . . x | . . x .` (3-3-2) (convention). FL: start from the specific regional rhythm, then add maj7/9 voicings, nylon guitar and Rhodes. Fake tell: treating it as one groove — specify the underlying rhythm.

#### L. Baile funk / funk carioca / Brazilian funk
- Developed in Rio from the late 1980s from Miami bass and electro; DJ Marlboro's "Funk Brasil" (1989); sound crews like Furacão 2000; international attention via Daniel Haaksman and Diplo releases (2004) — [Orphiq: What Is Baile Funk](https://orphiq.com/resources/what-is-baile-funk)
- Bases: Volt Mix ~125–128 BPM (looped from "8 Volt Mix", 1990s); Tamborzão ~130 BPM created 1998 by DJ Luciano Oliveira combining atabaque figures from candomblé, capoeira and maculelê with 808 kicks; 150 BPM movement from the mid-2010s (DJ Polyvox, Rennan da Penha, Kevin o Chris); São Paulo: ostentação, mandelão, automotivo, bruxaria; Recife: brega funk; producers work from shared rhythmic bases, chopping/pitching percussion, short call-and-response hooks — [Orphiq](https://orphiq.com/resources/what-is-baile-funk)
- Eras: Volt Mix (1990s), Tamborzão (2000–2009), Beatbox (2010 onward) — [Redalyc PDF](https://www.redalyc.org/pdf/4056/405641280009.pdf); tamborzão politics/sonority — [Revista IEB/USP](https://revistas.usp.br/rieb/en/article/view/82394)
- Tamborzão = syncopated, surdo-derived kick-and-clap groove with deliberately overdriven sub; empty space is part of the beat; classic ~130 BPM, modern global wave ~150 BPM; automotivo/mandelão often ~150 — [Music Production Wiki](https://musicproductionwiki.com/articles/how-to-make-brazilian-funk); [Orphiq](https://orphiq.com/resources/what-is-baile-funk)
- Funk automotivo is built for car sound systems with intense bass — [Billboard Brasil](https://billboard.com.br/brazilian-phonk-crescimento-global-tiktok-funk/)
- Grid (4/4, 130 tamborzão / 150 funk 150 / mandelão) (convention — no authoritative stroke-level transcription found; verify against a reference loop):
```
Kick (808)     X . . x | . . x . | X . . x | . . x .   (3-3-2 tresillo per half bar)
Atabaque/tom   . . x . | . x . x | . . x . | . x . .   (fills the gaps; pitch-varied hand-drum hits)
Clap/snare     . . . . | x . . . | . . . . | x . . x
Vocal chop     X . . . | . . . . | x . . x | . . . .   (short shouted hook, call/response)
```
- Harmony/melody: often no chords; MC chant over drums; melodic funk (funk melody) borrows pop progressions; mandelão/automotivo uses one-note distorted synth stabs ("tuin"), sirens, whistles, chopped vocal "montagens" (convention).
- Bass: distorted 808 kick/sub as the bass; automotivo/mandelão heavily saturated and clipped (sourced: overdriven sub).
- Form: 2–3 min, hook-first, DJ-editable 8-bar blocks, frequent drops to silence (convention).
- Mix: loud, clipped, raw; vocals dry and up-front (convention).
- Subgenres: Volt Mix/Miami-bass funk (electro, 125–128), tamborzão (130, atabaque samples), funk 150 (faster, tighter), mandelão (SP, minimal, distorted, aggressive), automotivo (car-audio bass, repetitive synth), bruxaria (dark, eerie samples), brega funk (Recife, more melodic, ~ slower bounce), Brazilian phonk (phonk cowbell melodies + funk rhythm; see trends) — (sourced names; distinguishing details convention).
- FL steps: (1) 130 or 150 BPM. (2) Distorted 808 kick on 3-3-2 (Fruity Fast Dist/Soundgoodizer + clipper). (3) Chop atabaque/conga hits into gaps, pitch them. (4) One-line vocal chant hook, repeat. (5) Mute everything for 1-beat "breaks". Fake tells: four-on-floor kick, clean mix, too many melodic layers.

#### M. Sertanejo (raiz, universitário, agronejo)
- Sertanejo universitário adapted sertanejo for younger urban audiences: more danceable, influences of axé, pop and funk, keeping viola and violão but adding guitar, bass, drums and percussion; artists Henrique & Juliano, Jorge & Mateus, Gusttavo Lima, Luan Santana — [O Povo](https://www.opovo.com.br/vidaearte/2023/07/24/conheca-a-origem-do-sertanejo-universitario.html)
- Agronejo (agro + sertanejo) celebrates agribusiness and rural youth life; Ana Castela (b. 2003) is a key name, launched by a viral homemade video of "Vaqueiro Apaixonado" — [Canal Rural](https://www.canalrural.com.br/curiosidades/agronejo-o-som-do-campo-que-conquistou-o-brasil/); [Wikipedia: Ana Castela](https://en.wikipedia.org/wiki/Ana_Castela); boom context — [National Geographic](https://www.nationalgeographic.com/culture/article/brazil-sertanejo-country-music)
- Musical traits (convention): duplas singing in parallel 3rds/6ths, nasal tenor timbre; viola caipira (10-string), acoustic guitar, accordion (sanfona); major keys, I–V–vi–IV (G–D–Em–C); "sofrência" heartbreak ballads (Marília Mendonça) 70–90 BPM; upbeat 110–140 with pop backbeat or vanera/arrasta-pé 2/4 polka-like bounce. Grid (pop sertanejo): `Kick X . . . | . . . . | X . x . | . . . .`, `Snare . . . . | X . . . | . . . . | X . . .`, `Acoustic gtr x . x x | . x x . | x . x x | . x x .`. FL: two vocal lines harmonized in 3rds, steel acoustic strums + sanfona fills, polished pop mix. Fake tell: single unharmonized vocal, no accordion/viola colour.

#### N. Tango and electrotango
- Tango rhythm: marcato marks a dry step, síncopa displaces it, arrastre delays the arrival (a drag into the beat); signature timbre = bandoneon (imported by German immigrants) with guitar — [Suno: Tango](https://suno.com/es/music-library/genres/tango) (low-authority page); [Yale Globalist: A Tale of Two Tangos](https://globalist.yale.edu/?p=4172)
- Gotan Project formed 1999 (Philippe Cohen Solal, Christoph H. Müller, Eduardo Makaroff), blending tango with electronic/downtempo; electrotango acts sample tango orchestras (violin, bandoneon, bass, piano) and overlay electronic beats (DnB, house, chill out, trip-hop) — [Equipboard: Gotan Project](https://equipboard.com/band/gotan-project); [Every Genre Project: Electrotango](https://reidht.substack.com/p/every-genre-project-september-7-electrotango); album "La Revancha del Tango" (2001) — [6moons](https://6moons.com/worldmusic/gotan.html)
- Identity (convention): Buenos Aires/Montevideo late 19th c.; golden-age orquestas típicas 1935–55 (D'Arienzo, Di Sarli, Troilo, Pugliese); Piazzolla's nuevo tango; electrotango: Gotan Project, Bajofondo, Tanghetto. By ear: bandoneon + violins + piano, dramatic minor key, staccato marcato chords with sudden rubato legato phrases.
- Tempo: dance tango 110–130 BPM quarter, milonga faster 2/4 (habanera/3-3-2), vals 3/4; electrotango 95–125 (convention).
- Harmony: harmonic minor; i–iv–V7–i (Am–Dm–E7–Am); dim7 passing chords (G#dim7); descending chromatic bass (Am–Am/G#–Am/G–Am/F#); Piazzolla adds 9ths, 11ths, clusters (convention).
- Grids (4/4, ~120) (convention):
```
Marcato in 4  X . . . | x . . . | X . . . | x . . .   (piano LH + bass, short, accented)
Síncopa       X . . . | . . x . | . . . . | . . . .   (anticipated 2nd hit, tied)
3-3-2         X . . . | . . x . | . . . . | x . . .   (steps 1,7,13 — Piazzolla/milonga)
Arrastre      . . . . | . . . . | . . . . | . . g x   (crescendo/drag smear on steps 15-16 landing on next bar's beat 1)
Electrotango kick X . . . | . . . . | X . . . | . . . .  + snare 2 & 4, or 4-on-floor in house versions
```
- Melody: violin/bandoneon legato with portamento, rubato, ornaments; spoken/dramatic vocals; electrotango often uses sampled spoken word.
- FL steps: accordion/bandoneon sample (reedy, with bellows dynamics via CC), string ensemble, piano marcato; electrotango: downtempo kick/snare, sub-bass doubling the marcato, filtered bandoneon loops, dub delays. Fake tells: swing, rock backbeat in traditional tango, bandoneon with static velocity.

#### O. Regional Mexican: norteño, banda, mariachi, corridos tumbados / música mexicana
- Norteño developed in late-19th-century northeastern Mexico, blending Mexican traditions with Central European polka/waltz (German, Polish, Czech immigrants); button accordion, bajo sexto (12-string), electric or double bass (replacing tololoche since the 1970s), drums, sometimes alto sax; rhythms include polka, redova, huapango, schottische; artists Los Alegres de Terán, Los Tigres del Norte, Intocable, Los Tucanes de Tijuana; connected to corridos and banda — [Wikipedia: Norteño (music)](https://en.wikipedia.org/wiki/Norte%C3%B1o_(music))
- Corridos tumbados: emerged late 2010s when young Mexican/US artists performed corridos over sierreño instrumentation while styling themselves like rappers; core: requinto/lead guitar melody, rhythm guitars, tololoche or tuba bass; charcheta (alto horn) provides chugging chordal accompaniment (in banda); instrumentals usually 100–130 BPM in polka- or waltz-derived feel (range 80–150+); trap borrowings: occasional 808 sub, tighter mixes, rap-cadence phrasing — [Beats To Rap On: Corridos tumbados](https://beatstorapon.com/music/latin/corridos-tumbados); [Beats To Rap On: Sierreño](https://beatstorapon.com/music/latin/sierreno); [Soundtrap blog](https://blog.soundtrap.com/what-is-corridos-tumbados)
- Corridos tumbados mix regional Mexican sound with reggaeton/urbano — [Noticias RCN](https://www.noticiasrcn.com/tendencias/karol-g-peso-pluma-una-nueva-version-corridos-tumbados-451695)
- Banda sinaloense (convention): Sinaloa brass band — clarinets, trumpets, trombones, tubas (sousaphone bass), charchetas (alto horns, offbeat chords), tambora (bass drum + cymbal), tarola (snare); Banda El Recodo, Banda MS, La Arrolladora. Mariachi (convention): Jalisco; violins, trumpets, vihuela, guitarrón (bass), guitar, sometimes harp; forms son jalisciense (6/8–3/4 sesquialtera), ranchera (valseada 3/4, polka 2/4, bolero), huapango (6/8, falsetto leaps); Mariachi Vargas, Vicente Fernández, Christian Nodal, Ángela Aguilar.
- Harmony (convention): mostly major I–IV–V7 (C–F–G7) with V7/V (D7), parallel 3rds/6ths between accordion/clarinets/voices; sierreño/tumbados and sad corridos often minor: i–iv–V7 (Am–Dm–E7), Andalusian i–VII–VI–V (Am–G–F–E7); harmonic rhythm slow (1–2 bars per chord).
- Melody/vocals: ranchera = operatic belting with sobs and grito; norteño = nasal straight tone, duet thirds; tumbados = low-key, half-sung, rap-influenced cadence, vocal fry, ad-libs; requinto = fast 16th/16th-triplet runs, hammer-ons, chromatic approach notes, slides (convention).
- Grids (convention):
```
POLKA 2/4 (norteño/banda/corrido) — 4/4 grid = two 2/4 bars, FL 95–125 BPM (each FL beat = polka beat)
Bass/tuba/tololoche X . . . | x . . . | X . . . | x . . .   (root on 1, fifth on 2 — oom)
Bajo sexto/charcheta . . x . | . . x . | . . x . | . . x .   (offbeat chords — pah)
Snare/tarola        . . x . | . . x . | . . x . | . . x x   (offbeats + rolls into phrase)
Kick/tambora        X . . . | X . . . | X . . . | X . . .
VALS/RANCHERA 3/4 — 12-step grid = one 3/4 bar of 16ths
Bass/guitarrón      X . . . | . . . . | . . . .
Vihuela/guitar      . . . . | x . . . | x . . .
HUAPANGO / SON JALISCIENSE — 12-step grid = two 6/8 bars, each step = one 8th note
Strum accents       X . . X . . | X . X . X .   (6/8 then 3/4 sesquialtera)
CORRIDO TUMBADO (sierreño) — polka or 6/8 feel, 100–130 (sourced range)
Tololoche/tuba      X . . . | x . . . | X . . . | x . . .   (+ slides/ghost slaps)
12-string "charcheteo" . . X . | . . X . | . . X . | . . X .  (muted chop on offbeats)
Requinto            continuous 16th runs in fills between vocal lines
Optional 808/hat    sparse sub on 1, trap hat rolls (bélico/urban crossovers)
```
- Form: corrido = narrative strophic verses (4-line stanzas) with instrumental requinto/accordion interludes, no big chorus in traditional corridos; tumbados add hooks; 2.5–3.5 min; ranchera has intro (trumpets/violins), verses, grito, instrumental bridge (convention).
- Mix: tumbados = dry intimate guitars, upfront slightly saturated vocal, low tololoche/tuba, modern loudness; banda = huge brass, tuba sub-heavy; norteño = accordion forward (convention).
- Subgenres: sierreño (guitar trio, requinto + 12-string + tololoche), sierreño con tuba, tumbados (urban attitude), corridos bélicos (aggressive), sad sierreño/romantic tumbado, norteño-banda (accordion + brass), norteño-cumbia (Grupo Frontera style) (sourced names partly; differences convention).
- FL steps: (1) 110 BPM polka grid or 3/4. (2) Tuba/tololoche root-fifth (FL "Tuba" in Fruity GM or a sampled tuba; tololoche = upright bass slap samples). (3) Offbeat 12-string chop + requinto runs (sampled acoustic/12-string guitar libraries; FL stock guitar is weak). (4) Accordion (norteño) fills in 3rds. (5) Tumbado: lower vocal register, optional 808 sub doubling tuba. Fake tells: straight rock/pop drums, guitar strummed on downbeats, requinto quantized to rigid 8ths.

#### P. Latin trap
- Latin trap originated in Puerto Rico as a descendant of Southern hip hop/trap, influenced by reggaeton, R&B and urbano; origin debated (2007 "El Pistolón"; De la Ghetto says he started trap in 2005–06); gained prominence ~2014 (Alvaro Díaz, Myke Towers, Fuete Billete); hits like Anuel AA "47 Remix", Bryant Myers "Esclava Remix"; Bad Bunny rose mid-2016 with "Diles"; Anuel AA's mixtape "Real Hasta la Muerte" after signing with Maybach Music — [Wikipedia: Latin trap](https://en.wikipedia.org/wiki/Latin_trap); [Vibe: Latin trap history](https://www.vibe.com/2017/08/latin-trap-history)
- Recipe: use the trap card from earlier notes (130–150 BPM half-time, 808 glides, hat rolls) and change: Spanish-language melodic/half-sung flows, minor or Phrygian/harmonic-minor loops (Am–F–E7), nylon/flamenco guitar or dark piano samples, occasional dembow snare switch for the chorus, more reverb-heavy autotuned vocals. Neighbours: Argentine trap (Duki, Trueno), Spanish trap. (convention)

#### Q. Latin pop
- (Mostly convention) Spanish-language pop from Julio Iglesias/balada to the 1999 "Latin explosion" (Ricky Martin, Shakira, Enrique Iglesias) to the urbano-pop era (Luis Fonsi & Daddy Yankee "Despacito" 2017, Karol G, Camilo, Sebastián Yatra, Rosalía flamenco-pop). By ear today: modern pop production at 90–105 BPM with dembow-lite percussion, acoustic/nylon guitar, Andalusian cadence (Am–G–F–E) or I–V–vi–IV, bilingual hooks. Recipe = modern-pop card + reggaeton card (both earlier notes) + nylon guitar/Latin percussion layer.

#### R. Latin house and moombahton
- Moombahton: created by Dave Nada late 2009 in Washington, D.C., by slowing Afrojack's remix of Silvio Ecomo & Chuckie's "Moombah!" from 128 to 108 BPM; mixes Dutch house with reggaeton's slower tempo (usually 100–110) and bouncy reggaeton percussion; first EP March 2010 on T&A Records — [Wikipedia: Moombahton](https://en.wikipedia.org/wiki/Moombahton); [SPIN 2011](https://www.spin.com/2011/07/hot-new-sound-moombahton-goes-boom/); Caribbean roots — [LargeUp](https://largeup.com/2012/01/06/check-it-deeply-david-heartbreak-munchi-and-moombahtons-caribbean-roots/)
- Moombahton grid (4/4, 108 BPM) (convention; snare = dembow positions from earlier reggaeton notes):
```
Kick     X . . . | X . . . | X . . . | X . . .
Snare    . . . x | . . x . | . . . x | . . x .   (steps 4,7,12,15)
Hat      . . o . | . . o . | . . o . | . . o .
Toms     fills / timbale rolls into drops
```
  Sounds: Dutch-house squeaky saw/square leads, pitched vocal chops, wobble bass (moombahcore ~110 with dubstep bass). Neighbours: Major Lazer-style moombah-pop (2015 "Lean On" era) (convention).
- Latin house (convention): 1990s NYC (Masters at Work / Nuyorican Soul, Louie Vega, Kenny "Dope"), Latin tech house today. Recipe = house card (earlier notes) at 122–126 + conga tumbao, bongos, timbale fills, cowbell, piano montuno in clave, Spanish vocal chops; keep clave 2-3 aligned to the 4-on-floor (one FL bar = half a clave cycle at 124 BPM, so clave spans 2 bars at 16th resolution).

### Inferences
- Tell-apart cheat sheet by ear (derived from the cards above):
  - **Scraper on every beat, root–fifth bass, ~95 BPM** → cumbia; same but faster with accordion and caja → vallenato paseo; very fast with tambora roll and sax riffs → merengue.
  - **Continuous güira 8ths + bongo, chorus-drenched guitar arpeggios, ~125** → bachata.
  - **Clave + cowbell quarters + anticipated bass (nothing on 1) + piano montuno** → salsa (fast) / son (slower, tres, no big horns) / cha-cha (~120, flute+violins, "4-&-1") / mambo (very fast big-band saxes).
  - **Low drum accent on beat 2 of a 2/4 bar + 16th pandeiro** → samba; same family whispered over maj7 chords with cross-stick clave → bossa nova.
  - **Distorted 808 in 3-3-2, chant hooks, 130/150** → baile funk; versus reggaeton (dembow snare 4,7,12,15 at 90–100) and moombahton (dembow over 4-on-floor at 108).
  - **Oom-pah (bass on beats, chords on offbeats)** → norteño/banda polka; add requinto runs + 12-string chop + tololoche + rap-like vocal → corridos tumbados; 3/4 oom-pah-pah with trumpets/violins → mariachi ranchera.
  - **Bandoneon + staccato marcato + minor + 3-3-2** → tango; with downtempo/house beat → electrotango.
- The biggest single "fake" tell across Afro-Latin genres is downbeat-heavy bass/kick; these grooves are carried by anticipation and offbeats, and FL's default 4-on-floor/beat-1 instincts work against them.
- For composer-AI implementation: model Cuban/Brazilian genres as 2-bar cycles (CYCLE16) with an explicit clave-direction parameter, and keep all parts (montuno, horn riffs, melody) phase-locked to it.

### Gaps
- No authoritative stroke-level transcriptions were retrieved for: cáscara (summarized source conflicted), partido alto (Wikipedia page lacks notation), tamborzão/funk 150 kick/perc layout, merengue tambora, Mexican cumbia bass, tango síncopa. Those grids are marked (convention) and should be verified against reference recordings or a percussion method book (e.g. Frank Malabe/Bob Weiner "Afro-Cuban Rhythms for Drumset", Duduka da Fonseca "Brazilian Rhythms for Drumset").
- BPM ranges for salsa, son, mambo, cha-cha, bachata, merengue, bossa nova, samba, tango, sertanejo and regional Mexican were not sourced this session (only cumbia, baile funk, moombahton and corridos tumbados were) — all others are (convention).
- Several cited pages are low-authority (Suno/Beats To Rap On genre pages, search-result summaries); corroborate with Wikipedia/ethnomusicology sources before treating as definitive.
- MPB, Latin pop, Latin house and mariachi received no dedicated source fetch; their cards are brief and convention-based.

## Q4: Current trends 2024–2026 (música mexicana, Brazilian funk globally, Latin trap / urbano, salsa revival)

### Takeaway
The three strongest Latin production currents in 2025–2026 are (1) música mexicana/corridos tumbados as a global streaming force led by Peso Pluma and Fuerza Regida, (2) Brazilian funk — especially automotivo/"Brazilian phonk" — as Spotify's fastest-growing genre, and (3) a roots revival inside urbano (salsa, plena, bomba) crowned by Bad Bunny's DeBÍ TiRAR MáS FOToS winning the 2026 Grammy Album of the Year.

### Cited Findings
- Bad Bunny's DeBÍ TiRAR MáS FOToS became the first Spanish-language album to win Album of the Year at the 68th Grammys (Feb 1, 2026); Bad Bunny is the third Latino act to win it after João Gilberto (with Stan Getz, 1965) and Santana (2000) — [Guinness World Records](https://www.guinnessworldrecords.com/world-records/782166-first-spanish-language-album-to-win-a-grammy-award-for-album-of-the-year); [Miami New Times](https://www.miaminewtimes.com/music/bad-bunny-wins-historic-grammy-for-debi-tirar-mas-fotos-40522044/)
- The album weaves salsa, bomba and reggaetón; it also won Best Música Urbana Album and "EoO" won Best Global Music Performance; the salsa resurgence reflects Gen Z/millennial nostalgia and cultural pride, echoed by Luis Fonsi, J Balvin, Rauw Alejandro, Karol G — [Consequence](https://concerts.consequence.net/articles/bad-bunny-wins-2026-grammy-album-of-the-year)
- Peso Pluma, pioneer of corridos tumbados, was the first recipient of the Billboard "Vanguardia" award (Billboard Latin Music Awards, Oct 2025) — [El Imparcial](https://www.elimparcial.com/espectaculos/2025/09/30/peso-pluma-sera-el-primer-artista-en-recibir-premio-billboard-vanguardia-por-revolucionar-musica-mexicana/)
- Peso Pluma was the only Mexican artist in Spotify Wrapped 2025's global top 10 (No. 7, 11.6 billion streams) — [SDP Noticias](https://www.sdpnoticias.com/espectaculos/musica/orgullo-mexicano-un-artista-aparece-entre-los-mas-escuchados-del-mundo-en-spotify-wrapped-2025/)
- Fuerza Regida (Jesús Ortiz Paz, from San Bernardino, CA) is described as the most-streamed project from Mexico, releasing corrido tumbado tracks and flirting with urban sounds — [Latina](https://latina.com/the-mexican-sound-wave-regional-music-takes-center-stage/)
- Brazilian funk was Spotify's fastest-growing genre to clear $100M in payouts in 2025, with about half of the average artist's streams coming from abroad — [Bloomberg Línea](https://www.bloomberglinea.com/estilo-de-vida/funk-brasileno-desbanca-al-k-pop-como-el-genero-que-mas-crece-en-spotify/)
- #brazilianfunk posts grew 34% and #brazilianphonk 62% in Europe between Feb and May 2026; "Brazilian phonk" on platforms mixes funk automotivo, montagens, São Paulo bruxaria funk, electronic music and international phonk — [Billboard Brasil](https://billboard.com.br/brazilian-phonk-crescimento-global-tiktok-funk/)
- "Automotivo Bibi Fogosa" (Bibi Babydoll & DJ Brunin XM) topped Ukraine's Spotify chart for days in Jul–Aug 2023 — [Billboard Brasil](https://billboard.com.br/brazilian-phonk-crescimento-global-tiktok-funk/); Brazilian phonk "Montagem" tracks reach hundreds of millions of streams with contested money splits — [Interspace Music](https://interspacemusic.com/blog/brazilian-phonk-money-splits-problem-montagem-argentina-400-million-spotify/); funk carioca's rise in chart data — [Chartmetric](https://hmc.chartmetric.com/brazilian-music-genres-funk-carioca/)
- Ana Castela consolidated in 2025 as one of the most-mentioned sertanejo names (agronejo) — [Wikipedia: Ana Castela](https://en.wikipedia.org/wiki/Ana_Castela); [Canal Rural](https://www.canalrural.com.br/curiosidades/agronejo-o-som-do-campo-que-conquistou-o-brasil/)
- Digital cumbia's international spread was driven by ZZK Records — [Huck](https://huckmag.com/article/zzk-records)

### Inferences
- For a 2025–2026 "current" sound: corridos tumbados = sierreño guitars + tuba/tololoche + modern dry/loud vocal with optional 808; Brazilian funk/phonk = 130–150 BPM distorted 808 tresillo + phonk cowbell melody + chopped vocal "montagem"; urbano-roots = reggaeton/trap toolkit plus real salsa/plena percussion and horn sections (derived from cited trends + cards).
- Brazilian phonk is the most "producer-portable" trend (sample-based, short, loopable) and is likely the most requested Latin style from bedroom producers alongside corridos (inference, not measured).

### Gaps
- No verified 2026 chart data was found for Latin trap specifically, bachata's current position (e.g. Romeo Santos/Prince Royce activity), or Latin house/moombahton revival; these trend claims are omitted rather than guessed.
- Specific new 2025–2026 tumbado/bélico artists (e.g. Netón Vega, Xavi, Tito Double P) were not verified in sources this session.
