# Asian, South Asian & Middle Eastern Genres — FL Studio Recipe Reference

Scope: K-pop, J-pop, city pop, anime/J-rock, Vocaloid, C-pop/Mandopop, Bollywood/filmi, bhangra, Punjabi pop, Indian classical basics (raga/tala), Arabic pop + maqam/iqa' basics (incl. Khaleeji, mahraganat), Turkish pop/arabesk, Persian pop, Mizrahi, Central Asian/Uzbek pop (estrada).
Number tags: (sourced) = backed by the linked source; (convention) = widespread practitioner practice, not verified against a source in this pass; (derived) = computed from sourced facts.
Grid notation (per genre-card-format.md): 16 steps = one 4/4 bar of 16ths; step 1 = beat 1, 5 = beat 2, 9 = beat 3, 13 = beat 4. X accent, x normal, g ghost, . rest, o open hat. Middle Eastern drum lanes: **Dum** = low centre stroke (map to darbuka low / kick), **Tek** = high rim stroke (darbuka high / rim / clap), **ka** = weaker other-hand rim (ghost). Non-4/4 grids say their step count.

---

## Q1. What scales/modes define each style (maqamat, quarter tones + FL Studio microtuning, ragas, royal road, East Asian pentatonics)?

### Takeaway
Middle Eastern styles are built from maqamat assembled out of 3–5-note cells (ajnas); some (Rast, Bayati, Saba, Sikah) need "half-flat" notes ~50 cents low that 12-TET cannot play, while Hijaz, Kurd, Nahawand and 'Ajam map cleanly to 12-TET (Phrygian dominant, Phrygian, minor, major). In FL Studio the practical microtuning tool is the per-note **Fine pitch** property (±1200 cents in 10-cent steps), so a half-flat is simply the note below/above with −50/+50 cents. East Asian pop leans on pentatonic melody over Western functional/jazz harmony (J-pop "royal road" IVmaj7–V7–iii7–vi; city-pop maj7/dim chords); Indian styles use raga (scale + characteristic phrases + emphasized notes) over a tonic drone.

### Cited Findings
**Maqam fundamentals**
- A maqam is built from ajnas (sing. jins): usually tetrachords, sometimes trichords/pentachords; a maqam has a lower and upper jins; the upper jins' starting note is the "dominant" (ghammaz), the second most important note after the tonic; maqam families are classified by the lower jins — [Wikipedia: Arabic maqam](https://en.wikipedia.org/wiki/Arabic_maqam)
- Most musicians agree on at least 8 main ajnas: rast, bayat(i), sikah, hijaz, saba, kurd, nahawand, ajam — [Wikipedia: Arabic music](https://en.wikipedia.org/wiki/Arabic_music)
- Family equivalences: 'Ajam ≈ major scale; Nahawand ≈ (harmonic/natural) minor; Kurd ≈ Phrygian; Hijaz ≈ Phrygian dominant (Hijaz Kar ≈ double harmonic) — [Wikipedia: Arabic maqam](https://en.wikipedia.org/wiki/Arabic_maqam)
- Maqam Rast = Jins Rast on the tonic + Jins Upper Rast or Jins Nahawand on the 5th; "one of the most popular and common maqamat" — [maqamworld: Rast](https://www.maqamworld.com/en/maqam/rast.php)
- Maqam Bayati = Jins Bayati on the tonic + Jins Nahawand or Jins Rast on the 4th; Muhayyar is Bayati starting its melodic path (sayr) from the octave — [maqamworld: Bayati](https://www.maqamworld.com/en/maqam/bayati.php)
- Maqam Hijaz = Jins Hijaz on the tonic + Jins Nahawand or Jins Rast on the 4th — [maqamworld: Hijaz](https://www.maqamworld.com/en/maqam/hijaz.php)
- Phrygian dominant = Hijaz = Freygish/Ahava Rabbah (Jewish/klezmer) = Dastgah-e Homayun (Iran); found in Indian, Middle Eastern, Balkan, Greek, Central Asian and flamenco music; corresponds to North Indian raga Hijaz Bhairav/Basant Mukhari and Carnatic Vakulabharanam — [Wikipedia: Phrygian dominant scale](https://en.wikipedia.org/wiki/Phrygian_dominant_scale)
- Quarter tones: the 24-tone equal division is a *notational convention*; real intonation is finer and orally transmitted. Half-sharps are rare; the common half-flats are E-half-flat and B-half-flat, less often A-half-flat. Example: Saba's first notes D, E-half-flat, F, G-flat contain seconds of ~160 and ~140 cents and a ~95-cent minor second — [Wikipedia: Arabic maqam](https://en.wikipedia.org/wiki/Arabic_maqam)
- Turkish makam theory divides the octave into 53 Holdrian commas (whole tone = 9 commas); only 24 of the 53 positions are used; the quarter-tone-looking accidentals in Turkish notation mean comma shifts, not quarter tones — [Wikipedia: Turkish makam](https://en.wikipedia.org/wiki/Turkish_makam)
- Rast "usually starts on C"; which degrees are half-flatted differs by region and "quarter-tone is to be taken loosely" — [Ableton forum thread on Arabic scales](https://forum.ableton.com/viewtopic.php?p=467329) (forum, low authority)
- Mizrahi (Israeli) pop historically used Arabic-style instruments but "intonation was typically Western" — singers did not use quarter-tone scales — [Wikipedia: Mizrahi music](https://en.wikipedia.org/wiki/Mizrahi_music)

**Concrete scale spellings (half-flat written "Eb½" = E −50 cents)** (derived from the jins definitions above; check against maqamworld note images)
| Maqam | On C/D (common tonic) | 12-TET safe? | FL fine-pitch edits |
|---|---|---|---|
| Rast | C D Eb½ F G A Bb½ C (desc. often Bb) | No | E and B notes: −50 c |
| Bayati | D Eb½ F G A Bb C D | No | E: −50 c |
| Saba | D Eb½ F Gb A Bb C | No | E: −50 c |
| Sikah | Eb½ F G A Bb½ C D | No | E, B: −50 c |
| Hijaz | D Eb F# G A Bb C D | Yes | none (upper jins Rast variant uses B½/C) |
| Kurd | D Eb F G A Bb C D | Yes | none |
| Nahawand | C D Eb F G Ab B C (= harmonic minor; desc. Bb) | Yes | none |
| 'Ajam | Bb C D Eb F G A Bb (major) | Yes | none |
| Hijaz Kar | C Db E F G Ab B C (double harmonic) | Yes | none |
| Nikriz | C D Eb F# G A Bb | Yes | none (convention) |

**FL Studio microtuning**
- Piano-roll per-note **Fine pitch** (Note properties) ranges −1200 to +1200 cents and is adjustable in 10-cent increments; users have asked for 1-cent resolution — [Image-Line forum](https://forum.image-line.com/viewtopic.php?p=1966980)
- The piano-roll scripting API exposes `pitchofs` (pitch fine-tune offset) −120…+120 in units of 1/10 semitone (10 cents) — [FL Studio piano roll scripting API](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/pianoroll_scripting_api.htm)
- Sytrus supports microtuning via .fnv envelope files; Newtone/Pitcher are quantized to 12-TET; users have requested .scl/.tun support and maqam presets (i.e., not native) — [Image-Line forum: microtuning request](https://forum.image-line.com/viewtopic.php?p=2017165); [Image-Line forum: built-in microtuning request](https://forum.image-line.com/viewtopic.php?p=1954540)
- The FL Studio manual's piano-roll note-property section (as fetched) lists Pan, Velocity, Release, Mod X/Y and slide/portamento and mentions scale snapping, but the fetched page did not document microtuning — [FL Studio manual: Piano roll](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/pianoroll.htm)

**Indian raga basics**
- Every raga has a vadi (most emphasized note) and samvadi (second, consonant with vadi); many are defined by a pakad/chalan — a characteristic phrase that identifies the raga — [Wikipedia: Raga](https://en.wikipedia.org/wiki/Raga)
- Hindustani ragas are grouped into 10 thaats (Bhatkhande): kalyan, bilaval, khamaj, kafi, asavari, bhairavi, bhairav, purvi, marva, todi; Carnatic uses 72 melakartas — [Wikipedia: Raga](https://en.wikipedia.org/wiki/Raga)
- Charanjit Singh's 1982 "Synthesizing: Ten Ragas to a Disco Beat" (TR-808, TB-303, Jupiter-8) set ragas over a disco/acid-like electronic beat — [Wikipedia: Hindi film music](https://en.wikipedia.org/wiki/Hindi_film_music)
- Thaat → Western mode mapping (convention): Bilaval = Ionian; Kalyan (raga Yaman) = Lydian; Khamaj = Mixolydian; Kafi = Dorian; Asavari = Aeolian; Bhairavi = Phrygian; Bhairav = double harmonic (C Db E F G Ab B); Purvi = C Db E F# G Ab B; Marva = C Db E F# G A B; Todi = C Db Eb F# G Ab B.

**East Asian harmony & pentatonics**
- Royal road (ōdō shinkō / "koakuma" progression): IVmaj7–V7–iii7–vi7; variants IV–V–iii–vi (triads), IVmaj7–V7–III7–vi7 (III7 = V7/vi), IVmaj7–V7–I–vi7; resolving with ii7–V7–I gives a full descending-fifths chain IVmaj7–V7–iii7–vi–ii7–V7–I. Minor versions: VImaj7–VII7–v7–i and iv7–v7–IIImaj7–VI. The "koakuma" name was coined by producer Seiji Kameda on NHK in 2014 — [Wikipedia: Royal road progression](https://en.wikipedia.org/wiki/Royal_road_progression)
- City pop uses jazz arranging devices such as major-7th and diminished chords, borrowed from Steely Dan/Doobie Brothers-style soft rock — [Wikipedia: City pop](https://en.wikipedia.org/wiki/City_pop)
- Early Shanghai shidaiqu fused a pentatonic folk-style melody with American jazz-orchestra instrumentation; Jay Chou popularized "zhongguofeng" (Chinese-style) R&B/rap fusion — [Wikipedia: Mandopop](https://en.wikipedia.org/wiki/Mandopop)
- Pentatonic sets (convention): Chinese gong mode = C D E G A (also shang/jue/zhi/yu rotations — yu = A C D E G is the "minor" feel); Japanese yonanuki major = C D E G A (4th & 7th removed), yonanuki minor = A B C E F; in-scale (miyako-bushi) = E F A B C; ryūkyū = C E F G B.

### Inferences
- A composer-AI should default to **12-TET-safe maqamat (Hijaz, Kurd, Nahawand, 'Ajam, Hijaz Kar)** for pop contexts (Arabic pop, arabesk, Mizrahi, bhangra/Bollywood "exotic" lines) and only use half-flats for Rast/Bayati/Saba/Sikah tracks — and then only on the half-flat degrees via Fine pitch −50 c. Turkish makam nuance (comma-based, e.g., Uşşak's 2nd is lower than Arabic Bayati's) can be approximated at −30 to −40 c, but this is a derived approximation.
- Hijaz/Phrygian dominant is the single most "pan-regional" color (Arabic, Turkish, Persian Homayun, Mizrahi Freygish, Bollywood Bhairav-flavored lines); to tell genres apart, rely on rhythm + instruments, not scale.
- In FL: put all half-flat notes on their own piano-roll color/channel, or set Fine pitch per note; Sytrus/third-party synths with Scala support are the alternative for sustained quarter-tone chords. Pitch-bend/slide notes emulate oud/ney/voice glides between degrees.

### Gaps
- Could not fetch the maqamworld iqa'/jins detail pages (HTTP 500 on index) — precise cent values per maqam (e.g., Sikah's ~−35 c Turkish vs ~−50 c Arabic) not verified here.
- No authoritative source found for the exact current FL Studio (2025–2026, FL 2025/2026 builds) microtuning features; FL Studio may have added native tuning since these forum threads — verify in current manual.
- Pentatonic and thaat-to-mode mappings are standard theory but were not re-verified against a fetched source in this pass.

---

## Q2. What rhythms define each (maqsum, baladi, saidi, malfuf, chiftetelli, Khaleeji, dhol chaal, talas, K-pop grooves), written as grids?

### Takeaway
Arabic/Turkish rhythms are cycles of low "dum" and high "tek" strokes; most pop-relevant ones fit one 4/4 bar (maqsum, baladi, saidi) or a 3+3+2 cell (malfuf, Khaleeji), with chiftetelli spanning 8 beats. Indian talas are counted cycles (teentaal 16, keherwa 8, dadra 6) with sam/khali landmarks; bhangra's chaal is a swung long-short (triplet) dhol pattern. The grids below are directly programmable.

### Cited Findings
- Rhythmic cycles in Arabic music are called wazn/iqa'; ~100 cycles exist, remembered with onomatopoeic syllables — [Wikipedia: Rhythm in Arabic music](https://en.wikipedia.org/wiki/Iqa%27)
- maqamworld lists iqa'at incl. Maqsum 4/4, Baladi 4/4, Malfuf 2/4, Ayyub 2/4, Ciftetelli 8/4, Masmudi Kabir 8/4, Wahda 4/4, Sama'i Thaqil 10/8, Aqsaq 9/8, Dawr Hindi 7/8 — [maqamworld: Iqa' Maqsum (index)](https://www.maqamworld.com/en/iqaa/maqsum.php)
- Dum = dominant hand at drum centre (low); Tek = rim (high); Ka = usually the non-dominant hand at the rim — [Wikipedia: Baladi](https://en.wikipedia.org/wiki/Baladi)
- **Maqsum** (Egyptian; aka Wahda Saghira, Turkish Düyek; faster = Fallahi): `D . T . . . T . D . . . T . . .`; filled: `D . T . t k T . D . t k T . t k` — [BabaYagaMusic rhythm diagrams](https://www.babayagamusic.com/Music/oriental-dance-rhythm-diagrams-and-descriptions.htm)
- **Baladi** (= Masmoudi Saghir; "Baladi" as a single-rhythm name is a Western usage): `D . D . . . T . D . . . T . . .`; filled `D . D . t k T . D . t k T . t k` — [BabaYagaMusic](https://www.babayagamusic.com/Music/oriental-dance-rhythm-diagrams-and-descriptions.htm); Wikipedia gives the same skeleton `D-D---T-D---T---` — [Wikipedia: Baladi](https://en.wikipedia.org/wiki/Baladi)
- **Saidi** (Upper Egypt; "upside-down beledi", cane dance/tahtib): `D . T . . . D . D . . . T . . .` — [BabaYagaMusic](https://www.babayagamusic.com/Music/oriental-dance-rhythm-diagrams-and-descriptions.htm)
- **Malfuf** (2/4, rolling entrance rhythm, counted 123-123-12): `D . . T . . T .`; running: `D k t K t k T k` — [BabaYagaMusic](https://www.babayagamusic.com/Music/oriental-dance-rhythm-diagrams-and-descriptions.htm)
- **Khaleeji / Saudi** (Arabian Gulf; strong 3+3+2): `D . . D . . T .` with variants `D . . D . . T T`, `D . k D . k T k` — [BabaYagaMusic](https://www.babayagamusic.com/Music/oriental-dance-rhythm-diagrams-and-descriptions.htm). Gulf and southern-Iraqi rhythms are "polyrhythmic": different beats are played by different drums for a layered effect, so single-drum versions are approximations (Mark Bell quoted) — same source. A secondary summary describes Khaleeji as medium-speed syncopated 4/4 with dums on beats 1, 2.5 and 4 — [Atlanta Belly Dance rhythm overview](https://m.atlantabellydance.com/Overview/Rythm.html) (consistent with the 3+3+2 when doubled in length)
- **Ayyub** (2/4; Egyptian/Lebanese, Zar): `D . . k D . T .` — [BabaYagaMusic](https://www.babayagamusic.com/Music/oriental-dance-rhythm-diagrams-and-descriptions.htm)
- **Chiftetelli / Wahda Kabira** (8/4; Turkish/Greek, slow "heavy" and fast "light"; "silence is a note"): 32 sixteenth steps `D . . . . . T . . . . . T . . . | D . . . D . . . T . . . . . . .` — [BabaYagaMusic](https://www.babayagamusic.com/Music/oriental-dance-rhythm-diagrams-and-descriptions.htm); described as 8/4 with 3+3+2 eighths then 2/2/2 + silent beat — [Wikipedia: Tsifteteli](https://en.wikipedia.org/wiki/%C3%87iftetelli); Ancient-Future describes it as like el-zaffa but with a 3-3-2 accent in the first four beats — [Ancient-Future: Arabic rhythms](https://www.ancient-future.com/arab.html)
- **Bambi** (8/4, Egyptian, faster than wahda kabira): `D . . T . . T . . T . . D . D .` (8th-note grid) — [BabaYagaMusic](https://www.babayagamusic.com/Music/oriental-dance-rhythm-diagrams-and-descriptions.htm)
- Mahraganat uses fast syncopated rhythms derived from Egyptian maqsum — [Vice: Explosive mahraganat](https://www.vice.com/en/article/explosive-mahraganat-egypt) (via search summary); Wikipedia lists "Maqsoum (rhythm)" among mahraganat's typical "instruments" — [Wikipedia: Mahraganat](https://en.wikipedia.org/wiki/Mahraganat)
- Modern Persian Bandari bands use frame drum, darbuka, djembe, congas and drum kits "specialized in 6/8 rhythms" — [Wikipedia: Bandari music](https://en.wikipedia.org/wiki/Bandari_music)
- **Teentaal**: 16 beats in 4 vibhags of 4; theka `dha dhin dhin dha | dha dhin dhin dha | dha tin tin ta | ta dhin dhin dha`; claps (tali) on 1 (sam), 5, 13; wave (khali) on 9 — [Wikipedia: Teental](https://en.wikipedia.org/wiki/Teental)
- **Keherwa**: 8 beats in two vibhags of 4; sam = 1 (clap), khali = 5 (wave); variants dhumaali, bhajani, qawwali; used in film songs e.g. "Rang Barse" (Silsila, 1981) — [Wikipedia: Keherwa](https://en.wikipedia.org/wiki/Keherwa)
- Teentaal is "the most common" North Indian tala; the tabla's basic phrase is the theka; Rupak (7) and Jhaptal are other common talas — [Wikipedia: Tala (music)](https://en.wikipedia.org/wiki/Tala_(music))
- **Chaal** (bhangra): "at the heart of both traditional and modern bhangra"; played on dhol — [Elizabeth College GCSE: Bhangra](https://elizabethcollege.fireflycloud.net/music/gcse-music/topic-pages/aos3-rhythms-of-the-world/indian-musical-traditions/bhangra); a 4/4 rhythm with each beat divided in three (triplet/"dotted" 8-note long-short pattern), vocalised "booma-chicka" — [Vaia: Punjabi rhythm patterns](https://vaia.com/en-us/explanations/punjabi/punjabi-music/punjabi-rhythm-patterns) (educational aggregator); dhol = barrel drum with low bass head and high treble head — [Kennedy Center: The Dhol Drum](https://www.kennedy-center.org/education/resources-for-educators/classroom-resources/lessons-and-activities/activities/tap/the-dhol-drum-sunny-jain/)

**Programmable grids** (16-step unless stated; tempo defaults are convention)
```
MAQSUM (4/4, 90–110 BPM pop; 120+ for shaabi/mahraganat)       (sourced pattern)
Dum   X . . . | . . . . | X . . . | . . . .
Tek   . . x . | . . x . | . . . . | x . . .
Ka    . . . . | g g . . | . . g g | . . g g   (fill layer)
Riq/shaker x . x . | x . x . | x . x . | x . x .  (convention)

BALADI / MASMOUDI SAGHIR (4/4, heavier, two opening dums)     (sourced)
Dum   X . X . | . . . . | X . . . | . . . .
Tek   . . . . | . . x . | . . . . | x . . .
Ka    . . . . | g g . . | . . g g | . . g g

SAIDI (4/4, double dum straddling beat 3)                      (sourced)
Dum   X . . . | . . X . | X . . . | . . . .
Tek   . . x . | . . . . | . . . . | x . . .

MALFUF (2/4 cell 3+3+2, written twice per 4/4 bar)             (sourced, doubled)
Dum   X . . . | . . . . | X . . . | . . . .
Tek   . . . x | . . x . | . . . x | . . x .
Running fill: D k t K t k T k per half bar

KHALEEJI (3+3+2 at quarter-note scale = 1 bar of 4/4)           (sourced cell, stretched)
Dum   X . . . | . . X . | . . . . | . . . .
Tek   . . . . | . . . . | . . . . | x . x .
Claps x . . . | . . x . | . . . . | x . . .  (layered handclaps, convention)
(Optional: half-time feel at ~95–105 BPM; Gulf pop layers several drums + claps — sourced as "polyrhythmic")

AYYUB (2/4, trance/zar, driving; written twice per bar)          (sourced)
Dum   X . . . | X . . . | X . . . | X . . .
Tek   . . . g | . . x . | . . . g | . . x .

CHIFTETELLI (8/4 = 2 bars of 16 steps; slow 70–90 BPM in quarters, convention)  (sourced)
Bar1 Dum  X . . . | . . . . | . . . . | . . . .
Bar1 Tek  . . . . | . . x . | . . . . | x . . .
Bar2 Dum  X . . . | X . . . | . . . . | . . . .
Bar2 Tek  . . . . | . . . . | x . . . | . . . .   (beat 4 of bar 2 silent)

PERSIAN 6/8 "shish-o-hasht" (12 steps = one 6/8 bar in 16ths; set FL project to 6/8; tempo see card 15)  (convention)
Dum   X . . . . . | X . . . . .
Tek   . . . . x . | . . x . x .
Daf/shaker x . x . x . | x . x . x .

TEENTAAL (16 matras; 1 step = 1 matra, NOT a 16th)                (sourced)
Bols  dha dhin dhin dha | dha dhin dhin dha | dha tin tin ta | ta dhin dhin dha
Map   Bass(bayan) on dha/dhin; NO bass on tin/ta (khali, steps 9–12)
Tali  X . . . | x . . . | (khali)o . . . | x . . .

KEHERWA (8 matras; filmi pop usually plays it as 8ths in one 4/4 bar)  (structure sourced, bols convention)
Bols  Dha Ge Na Ti | Na Ka Dhi Na
16-step map: Bass(ge/dha/dhi) X . x . | . . . . | . . . . | x . . .
             Treble(na/ti/ka) . . . . | x . x . | x . x . | . . x .

DADRA (6 matras, 3+3; ballads/ghazal in 6/8)                     (convention)
Bols  Dha Dhi Na | Dha Ti Na   (bass on beats 1–2 and 4; khali on 4 in some schools)

BHANGRA CHAAL (12 steps = 4 beats x triplet; long-short "booma-chicka")  (derived from sourced description)
Dhol bass (dagga)  X . . | . . x | X . . | . . x
Dhol treble(tilli) x . x | x . x | x . x | x . x
(8 hits/bar on triplet slots 1 & 3; accent bar-start and the pickup into beat 3; modern Punjabi pop often keeps chaal over a straight/half-time trap or dancehall kit)
```
- K-pop groove grids: see Q4 (not standard drum lexicons; convention).

### Inferences
- Dum→kick-ish sample (darbuka low or tuned 808 blip), Tek→darbuka "tek"/rim/snap, Ka→ghosted rim at velocity 40–60%: this one mapping lets every Arabic/Turkish rhythm be programmed on FL's channel rack.
- Distinguishing by ear: maqsum = single dum then "tek-tek"; baladi = two dums at the start; saidi = dums pushing into beat 3; malfuf/Khaleeji = 3+3+2 lilt (Khaleeji slower, clap-heavy, "limping" swing); chiftetelli = slow 8-beat sway with a silent last beat; Persian = 6/8 gallop; bhangra = triplet dhol bounce.
- Real players swing tek/ka strokes slightly late; apply 8–15% FL swing or manual 5–15 ms late offsets to ka ghosts (convention).

### Gaps
- maqamworld's own iqa' notation pages (HTTP 500) could not be fetched; cross-check malfuf/ayyub variants there.
- No primary/ethnomusicological source found for exact Khaleeji subtypes (e.g., "sawt", "samri", "liwa") stroke maps, nor for Iraqi rhythms (jorjina 10/8, hacha'a) beyond maqamworld's index listing; Iraqi "chobi" pattern not sourced.
- No reliable source located for a notated chaal grid; the grid above is derived from verbal descriptions. Tempo of traditional bhangra (a search snippet claimed 140–180 BPM) could not be traced to a primary source.
- The Persian 6/8 pattern is convention; the only web hits on "shish-o-hasht" were low-quality/spam pages, so not cited.

---

## Q3. What instruments define each, and how to emulate them in a DAW?

### Takeaway
Each region has 2–4 signature timbres that do most of the "identity" work: oud/qanun/ney/violin section + darbuka/riq (Arabic), bağlama/saz + string orchestra (arabesk), santur/tar + 6/8 kit (Persian), dhol + tumbi (bhangra/Punjabi), tabla/dholak + sitar/shehnai/strings (filmi), erhu/guzheng/pipa (C-pop zhongguofeng), shamisen/koto/shakuhachi (J-pop "wa" flavor), doira + rubab/dutar/gijak (Uzbek). In FL, use dedicated sample libraries for these; stock synths cannot fake plucked/bowed microtonal ornaments convincingly.

### Cited Findings
- Khaliji: heavy use of rebab, oud, violin, occasional habbān (bagpipe), percussion mirwas, tabl and duff; scene centred on Iraqi, Emirati, Kuwaiti, Bahraini, Saudi artists; sub-styles liwa, moradah, sawt with East African elements — [Wikipedia: Khaliji](https://en.wikipedia.org/wiki/Khaliji_(music))
- Qanun: plucked zither, 26 courses (Turkish models) of 3 strings each, played on the lap with two picks; range ~A2–E6 (Arabic designs F2–G6) — [Wikipedia: Qanun](https://en.wikipedia.org/wiki/Qanun_(instrument))
- Al jeel (1970s–80s Egyptian pop; Hamid El Shaeri): oud, qanun, rabab, ney, violin + drum machine — "almost always" a Roland TR-707; mixes Bedouin, Nubian and Egyptian rhythms with bass and synths — [Wikipedia: Al Jeel](https://en.wikipedia.org/wiki/Al_Jeel)
- Mahraganat: synthesizer, sequencer, sampler, DAW, darbuka, sagat (finger cymbals), drum kit; heavy Auto-Tune; shaabi wedding music + EDM + hip-hop; spread via MP3/phones in taxis/tuktuks; DJ Figo et al. around the 2011 revolution — [Wikipedia: Mahraganat](https://en.wikipedia.org/wiki/Mahraganat)
- Mizrahi: oud, kanun, darbuka; Greek bouzouki influence (Aris San) — [Wikipedia: Mizrahi music](https://en.wikipedia.org/wiki/Mizrahi_music)
- Arabesk: often includes the bağlama and Middle Eastern music — [Wikipedia: Arabesque (Turkish music)](https://en.wikipedia.org/wiki/Arabesque_(Turkish_music))
- Bhangra: the dhol (double-sided, played with two sticks) is the best-known instrument, with tumbi, sarangi, dholak, plus synths and guitar — [Wikipedia: Bhangra (music)](https://en.wikipedia.org/wiki/Bhangra_(music))
- Tumbi: high-pitched, single metal string plucked over a gourd resonator; popularized by Lal Chand Yamla Jatt; adopted by Kuldeep Manak, Mohammed Sadiq, Amar Singh Chamkila — [Wikipedia: Tumbi](https://en.wikipedia.org/wiki/Tumbi)
- Dhol: double-headed barrel drum; bass head (low) and treble head (high) — [Kennedy Center](https://www.kennedy-center.org/education/resources-for-educators/classroom-resources/lessons-and-activities/activities/tap/the-dhol-drum-sunny-jain/); see also [Wikipedia: Dhol](https://en.wikipedia.org/wiki/Dhol)
- Erhu: two-stringed bowed spike fiddle, most popular of the huqin family — [Wikipedia: Erhu](https://en.wikipedia.org/wiki/Erhu)
- Shamisen: three strings, played with a large plectrum (bachi); has a "sawari" buzzing mechanism — [Wikipedia: Shamisen](https://en.wikipedia.org/wiki/Shamisen)
- Doira/daf: Central Asian/Iranian frame drum, round frame with jingles (rings), thin goat/fish-skin or synthetic head; used in Uzbekistan, Tajikistan, Iran, etc. — [Wikipedia: Doira (Daf)](https://en.wikipedia.org/wiki/Doira)
- Uzbek classical shashmaqam (Bukhara/Samarkand, late 16th c.; "six maqams"); tanbur, dutar, sato (Turgun Alimatov) — [Wikipedia: Music of Uzbekistan](https://en.wikipedia.org/wiki/Music_of_Uzbekistan)
- Classic Persian pop pairs indigenous santur/tar with Western strings, piano, drums — [search summary; source quality low — not citable as fact]; Bandari bands use frame drum, darbuka, djembe, congas, drum kit — [Wikipedia: Bandari music](https://en.wikipedia.org/wiki/Bandari_music)
- Kikuo (Vocaloid) uses folk instruments from various world cultures plus toy pianos/toy sounds in high-tempo arrangements — [Wikipedia: Kikuo](https://en.wikipedia.org/wiki/Kikuo_(musician))
- City pop gear: Casio CZ-101, Yamaha CS-80, Roland TR-808, plus Walkman/car-cassette listening culture — [Wikipedia: City pop](https://en.wikipedia.org/wiki/City_pop)

**DAW emulation table** (convention unless cited)
| Instrument | Role | FL Studio approach | Fake-sounding mistakes |
|---|---|---|---|
| Darbuka (doumbek) | lead percussion | one-shots: dum/tek/ka/slap/roll in FPC or channel rack; velocity 40–127; rolls = 32nd-note ka/tek at falling velocity | all hits same velocity; no ka ghosts; quantized dead-straight |
| Riq / def / doira / daf | jingle groove | tambourine/riq loops; frame-drum dum + jingle layer | using a pop tambourine on 2&4 |
| Oud | melody/heterophony, taqsim | oud multisample (Kontakt/Ethno libraries); add slides (FL slide notes), mordents, tremolo (repeat 32nds) | sustained pad-like notes; chords (oud rarely strums chords) |
| Qanun | fast runs, tremolo, octave doubling | qanun/kanun library or harp + short release; play melody in octaves, add trill ornaments | no octave doubling; no tremolo |
| Ney / kawala | breathy flute, glides | ney library or FL "Fruity DX10"/Sytrus breath patch + noise; slides into notes; vibrato via Fruity LFO/pitch | clean flute with no breath/air |
| Violin section (Arabic "firqa") | unison melody | strings ensemble in **unison/octaves, not harmony**; legato with portamento; heavy reverb | four-part Western string harmony |
| Bağlama/saz | arabesk/Turkish lead | saz library; fast tremolo picking; hicaz/kürdi lines | — |
| Santur | Persian hammered dulcimer | santur/hammered-dulcimer library or FL "FL Keys"+mallet-like Sytrus; tremolo 32nds | — |
| Tabla / dholak | filmi/classical groove | tabla bol libraries (dha/dhin/na/tin/ge/ke); dholak for folk/wedding; bayan pitch-bend (ge glide) via slide notes | treating tabla as bongos; no bayan glide |
| Dhol | bhangra chaal | dhol one-shots: dagga (bass, stick) + tilli (treble, cane); layer kick under dagga, clap under tilli in pop | straight 16ths instead of triplet chaal |
| Tumbi | bhangra hook | tumbi samples or plucked single-string Sytrus/Fruity Kick-style pluck high (around C5–C6), short decay, slides | low/long sustained notes |
| Sitar | filmi/raga color | sitar library; meend (bends) via slides up to ±2 semitones; sympathetic-string drone | no meend; Western chords |
| Shehnai / bansuri | wedding/devotional/flute | ethnic wind libraries; grace notes and glides | — |
| Tanpura | drone Sa–Pa | tanpura loop on tonic + 5th (or tonic + 4th/7th per raga) | omitted drone in classical-style passages |
| Erhu | C-pop/zhongguofeng | erhu library; slides, vibrato, portamento between pentatonic notes | no slides |
| Guzheng / pipa | plucked C-pop color | guzheng glissando (pentatonic sweep), pipa tremolo | non-pentatonic glissandi |
| Shamisen / koto / shakuhachi | J-rock/anime "wa" flavor (e.g., Wagakki-style) | ethnic Japanese libraries; shamisen percussive bachi attack | — |
| Rubab / dutar / gijak | Uzbek/Central Asian | rubab/dutar libraries (or oud/saz substitutes); gijak ≈ spike-fiddle (erhu/kamancheh sample) | — |
| Vocaloid/SynthV voice | Vocaloid genre | Yamaha Vocaloid 6, Synthesizer V; tune pitch/vibrato/phonemes | untuned default lines |

### Inferences
- Heterophony (all melody instruments playing the same line with individual ornaments) is the key Arabic/Turkish texture; harmonizing the melody in thirds is the most common "fake" giveaway.
- In bhangra/Punjabi pop the dhol + tumbi pair alone is enough to read as Punjabi; in K-pop/J-pop, regional instruments are optional color (e.g., gugak samples in some K-pop, shamisen in J-rock) rather than identity.

### Gaps
- No single source verified specific current commercial libraries (e.g., Kontakt ethnic libraries); recommendations above are convention.
- Did not find a citable source for qanun mandal (lever) microtuning mechanics in the fetched text (well-known, but unverified here).

---

## Q4. K-pop/J-pop song structures (sections, key changes, bridges, dance breaks) and 2024–2026 trends — plus the genre-by-genre recipe cards

### Takeaway
K-pop is a globally sourced, multi-section "collage" pop: verse/rap → pre-chorus build → chorus/drop → dance break, often switching genre or key, produced via song camps with Nordic/US/UK writers and finished in Seoul; 2024–2026 brought both minimal "easy-listening" girl-group pop and huge global hits (Rosé & Bruno Mars "APT.", KPop Demon Hunters' "Golden"). J-pop follows the Intro–A-melo–B-melo–sabi template (often twice) with a C-melo/ochi-sabi before a final (often key-raised) sabi, and royal-road harmony; anime tie-ins (Yoasobi "Idol", Kenshi Yonezu "Kick Back") are its global engine.

### Cited Findings
- K-pop is characterized by melodic quality and cultural hybridity — [Wikipedia: K-pop](https://en.wikipedia.org/wiki/K-pop)
- K-pop production model (2026): melodies composed overseas (esp. Sweden — "powerful hooks and melody-centered pop songwriting"), tracks refined by US producers, recording in Seoul; agencies run multi-day "song camps" generating dozens of tracks; Korean A&R selects demos, Korean lyrics are added; BTS, BLACKPINK, TWICE regularly credit overseas writers — [Korea Times, 2026-03-17](https://www.koreatimes.co.kr/amp/entertainment/k-pop/20260317/composed-in-sweden-recorded-in-korea-k-pop-production-goes-global)
- Typical K-pop arrangement (secondary source): rap verse, melodic pre-chorus build, anthemic chorus, dance break, frequent key change or tempo shift near the final chorus; genre switches mid-song; production: layered synths, trap 808s, EDM drops/risers, orchestral stabs, heavily stacked vocals — [Tunee.ai K-pop page](https://tunee.ai/music-generator/korean) (AI-music marketing page; treat as low-authority corroboration)
- aespa "Next Level" (2021) is a commonly cited example of distinct sections that "feel almost like separate songs stitched together" — [Cal Poly-hosted article](https://grandavehousing.calpoly.edu/news/aespas-next-level-the-melody) (questionable hosting; low authority)
- 2025: "Golden" (KPop Demon Hunters) became only the second UK No.1 by a South Korean act after "Gangnam Style"; Rosé & Bruno Mars "APT." was No.5 in the UK 2025 year-end chart; KPDH soundtrack had multiple year-end UK Top 100 entries ("Soda Pop" #36, "Your Idol" #44) — [Music Week](https://www.musicweek.com/talent/read/with-the-return-of-bts-and-golden-still-top-10-is-k-pop-set-for-another-blockbuster-year-in-the-uk/093318); "APT." was YouTube's top song of 2025 and fastest K-pop track to 1 billion views — [Gulf News](https://gulfnews.com/amp/story/entertainment%2Fmusic-rewind-2025-from-apt-to-golden-these-songs-defined-2025-1.500393086); KPDH soundtrack was Spotify's second-most-streamed album of 2025 with five Grammy nominations incl. Song of the Year for "Golden" — [Rolling Stone (PDF copy)](https://www.jaehakim.com/wp-content/uploads/2025/12/10-Moments-That-Defined-K-Pops-Huge-Year-in-2025_Rolling-Stone.pdf); Music Week notes BTS's return and Western songwriters increasingly writing for Korean acts — [Music Week](https://www.musicweek.com/talent/read/with-the-return-of-bts-and-golden-still-top-10-is-k-pop-set-for-another-blockbuster-year-in-the-uk/093318)
- J-pop structure: 1番 = Intro–A-melo–B-melo–Sabi; 2番 = A–B–Sabi; then C-melo/bridge or 大サビ (ōsabi, emotional turning point) before the final sabi; A-melo ≈ verse, B-melo ≈ pre-chorus — [Yakuaru: Japanese song composition terms](https://posts.yakuaru.com/Common%20Japanese%20Song%20Composition%20Terminologies%20%E3%82%B5%E3%83%93%20%E8%90%BD%E3%81%A1%E3%82%B5%E3%83%93%20A%E3%83%A1%E3%83%AD%201%E7%95%AA%20%E3%83%95%E3%83%AC%E3%83%BC%E3%82%BA%20and%20others)
- J-pop replaced kayōkyoku (1920s–80s term); 1990s rock bands (e.g., Glay) assimilated kayōkyoku; leading 2020s names: Yoasobi, Creepy Nuts, Ado, Fujii Kaze, LiSA, King Gnu, Mrs. Green Apple; Yoasobi's "Idol" (2023) was the first Japanese song to top Billboard Global Excl. US; 2024 popular groups ME:I, Number_i, Snow Man, NiziU; "Showa retro" popular in South Korea by 2024 — [Wikipedia: J-pop](https://en.wikipedia.org/wiki/J-pop)
- Anime song (anison): mainstream tie-ins common since TM Network's "Get Wild" (City Hunter, 1987); alt-rock entry in the 2000s (Asian Kung-Fu Generation); Kenshi Yonezu "Kick Back" (Chainsaw Man) was the first Japanese-language song certified RIAA gold — [Wikipedia: Anime song](https://en.wikipedia.org/wiki/Anime_song)
- City pop: mid-1970s Japan, peak 1980s; pop/disco/funk/R&B/boogie/jazz-fusion/Latin/Caribbean blend; Tatsuro Yamashita ("king"), Mariya Takeuchi "Plastic Love" (1984), Miki Matsubara "Mayonaka no Door (Stay with Me)" (1979; No.1 Spotify global viral, Dec 2020); online revival ~2010 → vaporwave/future funk; Universal Japan reissued 107 albums in 2022 — [Wikipedia: City pop](https://en.wikipedia.org/wiki/City_pop)
- Vocaloid: Yamaha singing synthesizer first released 15 Jan 2004; current version Vocaloid 6 — [Wikipedia: Vocaloid](https://en.wikipedia.org/wiki/Vocaloid). DECO*27: influential early-2010s producer with pop-rock style — [Wikipedia: Deco*27](https://en.wikipedia.org/wiki/Deco*27); cosMo@Bousou-P known for songs over 200 BPM — (search summary; unverified primary)
- Mandopop lineage: shidaiqu (pentatonic + jazz band) → Teresa Teng → Faye Wong → Jay Chou's zhongguofeng R&B/rap; 2020s leaders still Jay Chou, JJ Lin, Eason Chan; Douyin short video increasingly drives the market; G.E.M. "Light Years Away" most-viewed Chinese MV on YouTube (291M, Feb 2025) — [Wikipedia: Mandopop](https://en.wikipedia.org/wiki/Mandopop)
- Hindi film songs are sung by playback singers and lip-synced; 1970s–80s Bollywood disco used synths (R.D. Burman, Bappi Lahiri, Biddu/Nazia Hassan "Aap Jaisa Koi" 1980) — [Wikipedia: Hindi film music](https://en.wikipedia.org/wiki/Filmi)
- UK bhangra: Birmingham/Bradford/Leicester 1970s; Bhujhangy Group (1971), Alaap (1977, Southall); Malkit Singh & Golden Star; 1980s sales >50,000 cassettes/week via local shops — [Wikipedia: Bhangra (music)](https://en.wikipedia.org/wiki/Bhangra_(music))
- Punjabi pop 2024: AP Dhillon at Coachella, Diljit Dosanjh on Fallon, Karan Aujla "Wavy" No.7 Billboard Canadian Hot 100; fusion of dhol with trap basslines and afrobeat/dancehall grooves — [Furtados School of Music](https://furtadosschoolofmusic.com/blog/why-punjabi-pop-is-now-a-worldwide-phenomenon/) (secondary blog); [Spotify Newsroom: Punjabi tag](https://newsroom.spotify.com/tag/punjabi-101)
- Arabesk: popular in Turkey 1960s–2000s; Orhan Gencebay, Ferdi Tayfur, Müslüm Gürses, Hakkı Bulut, İbrahim Tatlıses (record sales 1978); working-class identification — [Wikipedia: Arabesque (Turkish music)](https://en.wikipedia.org/wiki/Arabesque_(Turkish_music))
- Persian pop: classic artists Googoosh, Hayedeh, Ebi, Dariush, Vigen, Andy, Shahram Shabpareh; post-1979 exile scene in Los Angeles; Shadmehr Aghili among first state-supported post-revolution pop singers; Arian first sanctioned band with female singers — [Wikipedia: Iranian pop music](https://en.wikipedia.org/wiki/Persian_pop_music)
- Mizrahi: Israel late 1950s–60s; Arabic+Turkish+Greek; Zohar Argov ("king"), Avihu Medina; cassette-era marginalization ("too Arabic"); later rock/techno/EDM/Europop/R&B absorbed while keeping Greek/Turkish/Arab roots — [Wikipedia: Mizrahi music](https://en.wikipedia.org/wiki/Mizrahi_music)
- Uzbek pop is "well developed" with mainstream radio; singers Yulduz Usmonova and Sevara Nazarkhan mix traditional melodies with modern rhythms; Sogdiana and Rayhon also successful across CIS; rap popular with youth — [Wikipedia: Music of Uzbekistan](https://en.wikipedia.org/wiki/Music_of_Uzbekistan)

### Inferences
- Arranging K-pop for an AI: plan sections as *modules* (each 8 bars) that can change drum style; signal transitions with risers, a vocal ad-lib or a one-bar drum break; place the dance break after chorus 2 and a final chorus +1 semitone (or a half-time/acapella "ochi" moment) — structural conventions consistent with the sources but not quantified by them.
- J-pop vs K-pop by ear: J-pop = denser chord changes (royal road, secondary dominants, chromatic passing chords), sabi often first/"cold open", live-band or rock-band timbres, many syllables per bar; K-pop = 2–4-chord loops, beat-driven, abrupt genre switches, chant hooks, dance break.

### Gaps
- No rigorous 2024–2026 corpus statistic on K-pop BPMs/key-change frequency located; tempo ranges below are convention.
- Producer names (Teddy Park, Pdogg, Yoo Young-jin, Black Eyed Pilseung, Ryan Jhun, Monotree, Kenzie) are well-known but not verified against fetched sources here (only a Teddy plagiarism headline appeared on the K-pop page).
- "Estrada" as a Soviet-era variety-pop term was not sourced (Wikipedia "Estrada" resolved to a surname page).

### Genre recipe cards
(Format per genre-card-format.md; (s) = sourced above, (c) = convention, (d) = derived. Cross-refs to earlier notes for trap/EDM/jersey club/R&B/afrobeats drums: `research_notes/Music theory and beat making/`.)

#### 1. K-pop (idol pop)
1. **Identity**: Seoul; 1990s (Seo Taiji & Boys, H.O.T.) → 2nd gen (Girls' Generation, BIGBANG) → 3rd/4th gen (BTS, BLACKPINK, TWICE, aespa, NewJeans, Stray Kids, LE SSERAFIM, IVE) → 5th gen (BABYMONSTER, ILLIT, KATSEYE) (c). Refs: "Next Level" (aespa), "Golden" (KPop Demon Hunters/HUNTR/X), "APT." (Rosé & Bruno Mars), "Super Shy" (NewJeans). Ear test: polished multi-section pop with a chant/onomatopoeia hook, rap verse and a dance break; changes feel mid-song (s).
2. **Tempo & feel**: 95–130 BPM, default 120 (c); 4/4 straight; half-time choruses common; jersey-club/2-step/house sub-styles run 130–145 (c).
3. **Harmony**: minor keys dominate dance tracks (c); 2–4 chord loops e.g. i–VI–III–VII (Am–F–C–G), vi–IV–I–V (Am–F–C–G in C); dramatic sections use i–♭VI–♭VII; final chorus key change +1 or +2 semitones (s for key change existing; c for intervals). Harmonic rhythm 1 chord/bar.
4. **Melody & vocals**: ensemble lines split across members (2–4 bars each); high belted "main vocal" notes in bridge; rap verse; English hook words; ad-libs; heavily stacked/tuned vocals (s).
5. **Instrumentation**: layered synths, trap 808s, EDM drops/risers, orchestral stabs (s); brass stabs, distorted 808, vocal chops (c).
6. **Rhythm** (choose per section) (c):
   - Chorus (EDM/pop): `Kick X . . . | X . . . | X . . . | X . . .` `Clap . . . . | X . . . | . . . . | X . . .` `Hat . . o . | . . o . | . . o . | . . o .`
   - Rap verse (trap half-time, cross-ref trap notes): `Kick X . . . | . . . . | . . x . | . . . .` `Snare . . . . | . . . . | X . . . | . . . .` hats 1/16 with rolls.
   - Jersey/"Super Shy"-style: see earlier jersey club notes (kick `X . . x | . . x . | X . . x | . . x .` approx.).
7. **Bass**: 808 slides in rap sections; synth/sub octave bass on root in chorus; slap/funk bass in retro tracks (c).
8. **Form** (c): Intro 4–8 | V1 (rap/sing) 8–16 | Pre 8 | Chorus 8–16 | Post-chorus/drop 8 | V2 8 | Pre 8 | Chorus 16 | Bridge (vocal showcase) 8 | Dance break 8 | Final chorus (+key) 16 | Outro 4. Length 2:45–3:30.
9. **Production**: very loud, bright, wide; dense vocal stacks; hard section cuts; sound-effect transitions (c).
10. **Subgenres**: girl-crush (aggressive, trap/EDM), "easy listening"/minimal (NewJeans/ILLIT: soft vocals, 2-step/jersey/Baltimore club, sparse), boy-group performance (hip-hop/EDM hybrids), K-ballad/OST (piano + strings, 60–80 BPM, key change), K-R&B (c).
11. **FL steps**: (a) sketch 8-bar modules on separate patterns; (b) give each section its own drum pattern (trap verse → pop chorus → 4-on-floor dance break); (c) chant hook with formant-shifted vocal chops; (d) riser + one-bar stop before chorus; (e) final chorus transposed +1 in the playlist with pitch-shifted vocals. **Fake if**: one groove for the whole song; no dance break; under-produced vocals; chords too jazzy.

#### 2. J-pop (mainstream, idol, band)
1. **Identity**: replaced kayōkyoku; 1990s boom (s); refs: Yoasobi "Idol", Official Hige Dandism "Pretender", Kenshi Yonezu "Lemon", Mrs. GREEN APPLE "Ao to Natsu" (c). Ear test: busy royal-road harmony, many syllables, A–B–sabi build, often cold-open chorus.
2. **Tempo**: ballads 70–90; mainstream 120–150; anime/Yoasobi-style 150–180 (c). 4/4 straight; band 8th-note drive.
3. **Harmony**: royal road IVmaj7–V7–iii7–vi7 (in C: Fmaj7–G7–Em7–Am7) (s); "Just the Two of Us"/marunouchi sadistic IVmaj7–III7–vi7–v7–I7 (Fmaj7–E7–Am7–Gm7–C7) (c); secondary dominants, chromatic passing diminished chords, modulation up for last sabi (c). Harmonic rhythm 2 chords/bar in sabi.
4. **Melody**: wide range, stepwise + leaps on sabi; yonanuki (major pentatonic) tinge in older/enka-influenced lines (c); fast syllabic delivery.
5. **Instrumentation**: live band (gtr, bass, drums, piano) + strings/brass; idol pop adds synths (c).
6. **Rhythm**: `Kick X . . . | . . x . | X . . . | . . x .` `Snare . . . . | X . . . | . . . . | X . . .` `Hat x . x . | x . x . | x . x . | x . x .` (8th rock-pop) (c).
7. **Bass**: busy 8ths/16ths following chord roots + passing tones; slap in funkier tracks (c).
8. **Form**: Intro 4–8 | A 8 | B 8 | Sabi 8–16 | (interlude 4) | A 8 | B 8 | Sabi 16 | C-melo/ōsabi 8 | (ochi-sabi soft 4–8) | Sabi (often +1/+2 key) 16 | Outro (s for structure, c for bars). TV-size anime cut ~89–90 s (c).
9. **Production**: mid-forward vocals, bright guitars, less sub than K-pop (c).
10. **Neighbours**: idol pop (unison group vocals), "city pop revival", anime rock (below), Vocaloid-derived "net" pop (Yoasobi, Ado).
11. **FL**: write the royal-road loop first; add chromatic bass walk; double melody with piano in sabi; key-change the final sabi. **Fake if**: only 4-chord loop, no B-melo lift, too much sub-bass/trap.

#### 3. City pop
1. **Identity**: mid-1970s–80s Japan; Tatsuro Yamashita, Mariya Takeuchi, Anri, Miki Matsubara, Taeko Ohnuki (s/c); refs "Plastic Love", "Mayonaka no Door", "Ride on Time" (c). Ear test: Japanese vocals over slick AOR/boogie with maj7 chords, slap/fingered bass, glossy 80s keys.
2. **Tempo**: 95–125, default 110 (c); straight 16ths with light swing (52–55%) (c).
3. **Harmony**: maj7, min9, dominant 13, diminished passing chords (s); progressions: IVmaj7–iii7–vi7 / ii7–V7–Imaj7 (Fmaj7–Em7–Am7, Dm7–G7–Cmaj7); royal road (c).
4. **Melody**: smooth, mid-range, melancholic; sax/guitar fills (c).
5. **Instruments**: Rhodes/DX7 EP, CS-80/CZ-101 synths, TR-808 (s); clean funk guitar, brass section, slap bass (c). FL: FL Keys/DX10/Sytrus EP, Fruity Kick/808 samples, Transistor-style bass.
6. **Rhythm**: `Kick X . . . | . . . . | X . x . | . . . .` `Snare . . . . | X . . . | . . . . | X . . .` `Hat x x x x | x x x x | x x x x | x x x x` (16th, accented 8ths) (c).
7. **Bass**: syncopated 16th octaves (disco/boogie) (c).
8. **Form**: verse–pre–chorus x2, sax/guitar solo, chorus out; 4–5 min (c).
9. **Production**: warm, wide chorus/reverb, gated-free 80s polish; modern revival = tape saturation/vaporwave pitch-down (s for vaporwave link).
10. **Neighbours**: future funk (sampled city pop, French-house filtering, 120–130 BPM), vaporwave (slowed, reverbed) (s/c).
11. **FL**: chords first (maj7/9), slap or octave bass, clean guitar skank, 16th hats, sax lead. **Fake if**: trap hats, triads only, dry mix.

#### 4. Anime song / J-rock
1. **Identity**: anison from 1970s; tie-ins since "Get Wild" (1987); refs LiSA "Gurenge", Kenshi Yonezu "Kick Back", Yoasobi "Idol", Asian Kung-Fu Generation (s/c). Ear test: fast, dramatic rock with orchestral/synth layers and a soaring sabi.
2. **Tempo**: 160–200, default 180 (c); double-time drum fills; frequent half-time breakdowns.
3. **Harmony**: minor keys with royal road and ♭VI–♭VII–i climbs (Fmaj7–G–Am); key change before last sabi (c).
4. **Vocals**: belted, high tessitura, fast syllables (c).
5. **Instruments**: distorted guitars (palm-mute 8ths), live drums, strings/brass hits, piano runs (c).
6. **Rhythm**: `Kick X . x . | . . x . | X . x . | . . x .` `Snare . . . . | X . . . | . . . . | X . . .` `Ride/Hat x . x . | x . x . | x . x . | x . x .` (c).
7. **Bass**: driving 8ths, pick bass (c).
8. **Form**: TV-size ≈ Intro 4 | A 8 | B 8 | Sabi 16 | ending hit (~90 s); full: J-pop form (c).
9. **Production**: loud, guitars wide, vocals forward (c).
10. **Neighbours**: J-rock (less orchestral), visual-kei (theatrical, metal), Vocaloid rock.
11. **FL**: program drums with fills every 4 bars; double-track guitars hard-panned. **Fake if**: slow tempo, no fills, quiet vocals.

#### 5. Vocaloid / net music
1. **Identity**: Yamaha Vocaloid (2004) (s), Hatsune Miku (2007, Crypton) (c); Nico Nico Douga scene; DECO*27 (pop rock) (s), Kikuo (world/toy instruments, fast, dark lyrics) (s), cosMo@Bousou-P (>200 BPM) (search summary). Ear test: synthetic female voice at superhuman speed/range over rock/EDM.
2. **Tempo**: 130–200+, default 170 (c/s for >200).
3. **Harmony**: royal road, rapid modulations, chromaticism (c).
4. **Melody**: wide leaps, fast rap-like syllables, high register (no breath constraints) (c).
5. **Instruments**: electric guitar, piano, synths, chiptune, toy piano (Kikuo) (s/c); voice: Vocaloid 6 / Synthesizer V.
6. **Rhythm**: rock 8ths or EDM four-on-floor; frequent stutters/glitches (c).
7. **Bass**: slap/fast 16th bass (c).
8. **Form**: J-pop form, shorter intros (c).
9. **Production**: bright, compressed, sometimes lo-fi (c).
10. **Neighbours**: Utaite (human covers), Yoasobi/Ado "net pop" (c).
11. **FL**: tune synth voice pitch curves; add vibrato on long notes only. **Fake if**: robotic flat pitch everywhere (unless intentional).

#### 6. C-pop / Mandopop (incl. zhongguofeng)
1. **Identity**: Shanghai shidaiqu (1920s–40s) → Taiwan/HK (Teresa Teng) → Faye Wong → Jay Chou, JJ Lin, Eason Chan, Mayday, G.E.M.; Douyin-driven 2020s (s). Refs: Jay Chou "Blue and White Porcelain", Teresa Teng "The Moon Represents My Heart" (s), G.E.M. "Light Years Away" (s). Ear test: ballad-heavy, piano/strings, Mandarin tones, pentatonic hooks (zhongguofeng adds erhu/guzheng/pipa).
2. **Tempo**: ballads 65–85 (default 72); R&B/zhongguofeng 80–100; Douyin dance 120–130 (c).
3. **Harmony**: I–V–vi–iii–IV–I–IV–V (Canon), I–V/7–vi–IV, 6-4-5-1 (c); key change up a semitone/tone for last chorus (c).
4. **Melody**: pentatonic (C D E G A) lines over diatonic chords (s for pentatonic heritage); melisma light; falsetto in R&B (c).
5. **Instruments**: piano, strings, acoustic guitar; erhu, guzheng (glissando), pipa (tremolo), dizi (c).
6. **Rhythm**: ballad `Kick X . . . | . . . . | X . . x | . . . .` `Snare . . . . | X . . . | . . . . | X . . .`; zhongguofeng R&B half-time with swing 55% (c).
7. **Bass**: root-fifth, sustained; R&B: syncopated (c).
8. **Form**: V–Pre–C ×2, bridge, final C (+key) ; 4–5 min (c).
9. **Production**: vocal very upfront, lush reverb (c).
10. **Neighbours**: Cantopop (Cantonese; more 80s/90s orchestral ballad), C-pop idol (K-pop-like), Chinese "guofeng" online music (heavier traditional instrumentation) (c).
11. **FL**: write a pentatonic hook, harmonize with diatonic maj/min7 chords; add guzheng gliss into choruses. **Fake if**: melody uses non-pentatonic 4th/7th on strong beats in "Chinese-style" songs.

#### 7. Bollywood / filmi
1. **Identity**: Hindi film songs, playback singers lip-synced (s); eras: Golden age (Lata Mangeshkar, Mohammed Rafi), R.D. Burman/Bappi Lahiri disco (s), A.R. Rahman (1990s+), Pritam, Vishal–Shekhar, Anirudh (2020s pan-India) (c). Refs: "Chaiyya Chaiyya", "Tum Hi Ho", "Jai Ho" (c). Ear test: Hindi/Urdu vocals with ornamented (murki) melody, dholak/tabla grooves, strings swells, item-number dance beats.
2. **Tempo**: romantic 70–90; dance/item 100–130; bhangra-fusion 95–105 (c). Keherwa 8-beat feel common (s for keherwa in film); dadra 6/8 in ghazal-ish songs (c).
3. **Harmony**: raga-colored diatonic minor; i–VII–VI–VII, i–iv–VII–III; sustained drone pads; Bhairav/Phrygian-dominant for drama (d) — chord changes slow (1–2 bars).
4. **Melody**: murki/khatka (quick ornaments), meend (glides), sargam/alaap intros; Sufi-style high belting (c).
5. **Instruments**: tabla, dholak, sitar, santoor, bansuri, shehnai, harmonium, large string section; modern: EDM/trap kit (s for synth era).
6. **Rhythm** (filmi keherwa, dholak): `Dholak-bass X . . x | . . X . | X . . x | . . X .` `Dholak-treble . x x . | x x . x | . x x . | x x . x` (c) — or tabla keherwa grid from Q2.
7. **Bass**: synth bass on root; 808 in modern Punjabi-fusion (c).
8. **Form**: Mukhda (hook/refrain) – interlude – Antara 1 – mukhda – interlude – Antara 2 – mukhda ×2; 4–5 min (c).
9. **Production**: vocals very loud and reverberant; big string pads (c).
10. **Neighbours**: Sufi/qawwali-pop (handclaps, harmonium, keherwa-qawwali variant (s)), Punjabi pop, indie-pop (Anuv Jain, Prateek Kuhad style acoustic) (c).
11. **FL**: tanpura drone, write mukhda melody with ornaments (slide notes), keherwa dholak loop, string swells between lines. **Fake if**: no ornaments, Western I–V–vi–IV pop with a sitar sample on top.

#### 8. Bhangra (UK & Punjab)
1. **Identity**: Punjabi harvest-dance folk → UK bhangra (Birmingham/Southall 1970s–80s: Bhujhangy, Alaap, Heera, Malkit Singh/Golden Star) → Panjabi MC "Mundian To Bach Ke" (1998) (s/c). Ear test: triplet dhol chaal + tumbi riff + shouts ("hoi!", "balle balle").
2. **Tempo**: modern 95–110 (chaal felt as triplets, i.e., 12/8 over 4/4); older dance up to ~150 (s weak/c).
3. **Harmony**: mostly drone/one-chord or i–VII vamps; Mixolydian/Dorian-ish folk melodies (c).
4. **Melody/vocals**: high-pitched, strong open-throated folk vocals, boliyan couplets, call-and-response shouts (c).
5. **Instruments**: dhol, tumbi, sarangi, dholak, chimta, algoza; synths/guitar later (s).
6. **Rhythm**: chaal grid (Q2) + pop layer: `Kick X . . | . . . | X . . | . . .` (12-step) `Clap . . . | X . . | . . . | X . .` (c).
7. **Bass**: synth bass doubling dhol dagga; reggae/dancehall bass in fusion (c).
8. **Form**: tumbi intro riff 4 | verse 8 | chorus 8 (dhol full) | dhol break 4–8 | ... ; 3–4 min (c).
9. **Production**: dhol loud and up front; claps; bright (c).
10. **Neighbours**: Punjabi pop (below), Bollywood bhangra (filmi strings), bhangra-dancehall/garage fusion (Jay Sean/Rishi Rich era) (c).
11. **FL**: set the grid to triplets (or swing 66% in 16-step mode); program dhol dagga/tilli with velocity accents; tumbi riff on 2–3 notes high. **Fake if**: straight 16ths; tabla instead of dhol; low tumbi.

#### 9. Punjabi pop / Punjabi hip-hop (2020s)
1. **Identity**: Sidhu Moose Wala, AP Dhillon, Diljit Dosanjh, Karan Aujla, Shubh (c); 2024 global milestones (Coachella, Fallon, Canadian Hot 100) (s). Ear test: Punjabi vocals over trap/R&B/afrobeats/dancehall with dhol or tumbi accents (s).
2. **Tempo**: 80–105 (s weak) — e.g., trap-R&B at 90 with chaal feel, afro-Punjabi at 100–110 (c).
3. **Harmony**: minor 2–4 chord loops, guitar arpeggios (AP Dhillon/Gurinder Gill "Brown Munde" style) (c).
4. **Vocals**: melismatic Punjabi folk inflection + rap cadences; ad-libs (c).
5. **Instruments**: 808, trap hats, acoustic/electric guitar loops, dhol one-shots, tumbi, flute, harmonium samples (c).
6. **Rhythm**: trap kit (cross-ref trap notes) + dhol chaal layer on top; or dancehall `Kick X . . x | . . x . | X . . x | . . x .` (c).
7. **Bass**: 808 following root, slides (c).
8. **Form**: hook-first; 2:30–3:30 (c).
9. **Production**: modern hip-hop loudness; vocal heavily reverbed/delayed (c).
10. **Neighbours**: Desi hip-hop (Hindi rap), Bollywood remixes.
11. **FL**: build trap beat → add chaal dhol at low velocity → tumbi riff. **Fake if**: generic trap without any Punjabi melodic inflection.

#### 10. Indian classical (basics for fusion)
1. **Identity**: Hindustani (North) and Carnatic (South); raga = scale + vadi/samvadi + pakad; tala = cycle with sam/khali (s). Ear test: drone, solo melody, tabla/mridangam, gradual tempo increase (alap → jor → jhala) (c).
2. **Tempo**: vilambit (slow, 30–60 matras/min), madhya (60–120), drut (120–300+) (c).
3. **Harmony**: none — tanpura drone Sa–Pa (c).
4. **Melody**: meend, gamak, andolan (oscillation), sargam (Sa Re Ga Ma Pa Dha Ni) (c).
5. **Instruments**: sitar, sarod, bansuri, sarangi, santoor, tabla; Carnatic: veena, violin, mridangam (c).
6. **Rhythm**: teentaal/keherwa/dadra grids (Q2) (s).
7. **Bass**: none; bayan glides provide low end (c).
8. **Form**: alap (free) → bandish/gat in tala → improvisations → tihai cadences (3× phrase ending on sam) (c).
9. **Production**: natural room, drone continuous (c).
10. **Neighbours**: ghazal, qawwali, filmi, fusion (Shakti) (c).
11. **FL**: tanpura loop; melody in one raga only; end phrases with a tihai on beat 1. **Fake if**: chord changes, missing drone, notes outside the raga.

#### 11. Arabic pop (Egyptian/Levantine) & al-jeel
1. **Identity**: 1970s–80s al jeel (Hamid El Shaeri; TR-707 beats) (s) → Amr Diab "Mediterranean pop" (e.g., "Habibi Ya Nour El Ain", 1996), Nancy Ajram, Elissa, Mohamed Hamaki; Levantine dabke-pop (c). Ear test: Arabic vocal with melismatic maqam ornaments over a maqsum/baladi-driven pop beat with strings/qanun answering the voice.
2. **Tempo**: 90–120, default 100 (c); maqsum in 4/4; ballads 70–80 in wahda/masmoudi (c).
3. **Harmony**: modal; often 1–3 chords (i, ♭VII, ♭VI) or none; Hijaz pop: I(maj)–♭II–I (D–Eb–D) or i–iv over Hijaz/Nahawand; quarter-tone maqamat (Bayati/Rast/Saba) are harmonized sparsely (drones, open fifths) because full triads clash (d).
4. **Melody**: maqam-based, ornamented (trills, turns, grace notes, micro-slides); mawwal free-rhythm vocal intros; call-and-response with string section (c).
5. **Instruments**: oud, qanun, ney, violin section, accordion/keyboard ("oriental" keyboards with quarter-tone tuning), darbuka, riq; drum machines/synths (s for al jeel).
6. **Rhythm**: maqsum or baladi grid (Q2) + kick on dums, clap on teks; riq 8ths (c).
7. **Bass**: follows dum strokes (D on 1 and 3/"and of 2") with root/5th (c).
8. **Form**: instrumental intro (lazma riff) 8 | verse (couplet) 8–16 | chorus 8 | instrumental lazma 8 | verse 2 | chorus | taqsim or mawwal break | chorus; 3:30–4:30 (c).
9. **Production**: vocals wet (long plate/hall), string section bright, darbuka loud (c).
10. **Neighbours**: Khaleeji (Gulf, 3+3+2, clap-heavy), mahraganat (electro-shaabi, autotune, fast), dabke (Levantine 4/4 with mijwiz), raï (Algeria; separate) (s/c).
11. **FL**: choose a 12-TET-safe maqam first (Hijaz/Kurd/Nahawand) or set fine-pitch for half-flats; program maqsum with velocity; write a 4-bar lazma riff in octaves on strings+qanun; vocal melody stepwise with turns. **Fake if**: Western chord progression changing every bar, string harmony in thirds, no darbuka ghost notes.

#### 12. Khaleeji (Gulf pop)
1. **Identity**: Saudi, Kuwaiti, Emirati, Bahraini, Iraqi artists; sawt, liwa, moradah sub-styles (s); refs: Mohammed Abdu, Abdul Majeed Abdullah, Hussain Al Jassmi, Balqees, Rashed Al-Majed (c). Ear test: lilting 3+3+2 swing, layered handclaps and frame drums, oud/violin, nasal Gulf vocal.
2. **Tempo**: ~95–110 (c); swung 3+3+2 feel.
3. **Harmony**: modal (Bayati/Rast/Hijaz/Saba common) with sparse chords (c).
4. **Melody**: narrow-range, repeated motifs, choral responses (c).
5. **Instruments**: oud, rebab, violin, mirwas, tabl, duff, habbān (s); handclap ensembles (s for polyrhythmic layered drums; c for claps).
6. **Rhythm**: Khaleeji grid (Q2) with 2–3 clap layers and a low tabl on dums (s/c).
7. **Bass**: synth bass on dums, root/5th (c).
8. **Form**: intro oud/violin, verse–chorus with group-clapped chorus (c).
9. **Production**: claps very prominent, wide; reverb on vocals (c).
10. **Neighbours**: Iraqi pop (chobi rhythm, faster), Saudi sheilat (a cappella chant) (c).
11. **FL**: build clap stack (3 claps, slight timing offsets 5–15 ms), tabl dum, riq jingles; oud riff. **Fake if**: straight 8ths, missing claps.

#### 13. Mahraganat (Egyptian electro-shaabi)
1. **Identity**: Cairo working-class neighborhoods, late 2000s; DJ Figo, Oka & Ortega, Hamo Bika, Hassan Shakosh, Wegz-adjacent crossovers (s/c). Ear test: chaotic maqsum-based electronic beat, sirens/synth leads, extreme Auto-Tune, shouted MC vocals (s).
2. **Tempo**: 120–140, default 130 (c — no reliable BPM source).
3. **Harmony**: one-chord/maqam riff (Hijaz/minor) (c).
4. **Vocals**: autotuned hard, speech-like lines + crowd hook (s).
5. **Instruments**: synths, sampler, DAW, darbuka, sagat, drum kit (s); cheap-sounding "oriental keyboard" leads, sirens (c).
6. **Rhythm**: maqsum with doubled-time darbuka rolls; kick on dums, snare/clap on teks; 16th shakers (s for maqsum basis).
7. **Bass**: distorted synth bass on dums (s: "aggressive basslines" via search summary).
8. **Form**: loop-based, long (4–6 min), MC verses, keyboard solo breaks (c).
9. **Production**: lo-fi, clipped, very loud (c).
10. **Neighbours**: shaabi (acoustic wedding pop), Egyptian trap (Wegz, Marwan Pablo) (c).
11. **FL**: Pitcher/Auto-Tune at retune 0; maqsum darbuka + kick; detuned lead in Hijaz. **Fake if**: clean mix, slow tempo.

#### 14. Turkish pop & arabesk
1. **Identity**: arabesk 1960s–2000s; Orhan Gencebay, Ferdi Tayfur, Müslüm Gürses, İbrahim Tatlıses (s); Turkish pop: Tarkan ("Şımarık"), Sezen Aksu (c). Ear test: makam-based lament vocal with sobbing ornaments over a big string orchestra, bağlama, darbuka in 4/4 or 9/8.
2. **Tempo**: arabesk ballad 70–90 (chiftetelli/sofyan); pop 100–125 (c); 9/8 karşılama/roman havası (2+2+2+3) for dance songs (maqamworld lists aqsaq 9/8 (s)).
3. **Harmony**: Hicaz, Kürdi, Uşşak, Nihavend makams (makam theory s); minor-ish chords; Hicaz: I–♭II (c).
4. **Melody**: melismatic, sobbing glottal breaks, comma-based microtones (53-comma system s).
5. **Instruments**: bağlama/saz (s), string orchestra, kanun, darbuka, clarinet (roman), ney (c).
6. **Rhythm**: chiftetelli grid (Q2) for slow; 9/8 (9 steps of 8ths): `Dum X . . . X . . . . | Tek . . x . . . x . x` (c, approximate 2+2+2+3).
7. **Bass**: root on dums (c).
8. **Form**: string intro (taksim or riff) 8 | verse | chorus | instrumental | ... (c).
9. **Production**: lush, wet, emotional; Turkish pop 1990s = Eurodance-ish with darbuka (c).
10. **Neighbours**: Turkish folk (türkü), fantezi, Anatolian rock, Greek laiko/tsifteteli (s link) (c).
11. **FL**: string ensemble in unison + octave, saz tremolo, darbuka chiftetelli; fine-pitch −20 to −40 c on Turkish "koma" degrees if aiming for authenticity (d). **Fake if**: string harmony, no ornaments.

#### 15. Persian (Iranian) pop
1. **Identity**: pre-1979 Tehran (Googoosh, Vigen, Ebi, Dariush, Hayedeh) → LA "Tehrangeles" diaspora → domestic sanctioned pop (Shadmehr Aghili, Arian) (s); 2010s–20s: Mohsen Yeganeh, Sasy, Mohsen Chavoshi (c). Ear test: 6/8 dance gallop with santur/tar flourishes and Persian modal (dastgah) melodies; or slow piano-string ballads.
2. **Tempo**: 6/8 dance ~120–140 (dotted-quarter ~60–70) (c); ballads 65–80 in 4/4 (c).
3. **Harmony**: dastgahs (Shur ≈ Bayati-like with koron (≈ quarter-flat) 2nd; Homayun ≈ Hijaz (s); Mahur ≈ major) (c except Homayun); sparse minor chords (i–VII–VI) (c).
4. **Melody**: tahrir (yodel-like ornamental breaks), stepwise motifs (c).
5. **Instruments**: santur, tar, setar, kamancheh, tombak, daf + synth/drums (c); Bandari: frame drum, darbuka, djembe, conga, kits in 6/8 (s).
6. **Rhythm**: Persian 6/8 grid (Q2) (c); Bandari 6/8 faster with synth stabs (s for 6/8).
7. **Bass**: dotted-quarter pulse on dums (c).
8. **Form**: intro riff, verse, chorus, instrumental (santur/keyboard solo), 4–5 min (c).
9. **Production**: LA-pop 80s/90s: synth-heavy, DX7 keys, drum machine (c).
10. **Neighbours**: Bandari (south Iran, African-influenced, faster 6/8), Kurdish/Azeri pop, Afghan pop (c).
11. **FL**: 12-step pattern in 6/8 (Project time signature 6/8), tombak dum/tek, santur tremolo, koron notes via fine pitch −40 to −50 c. **Fake if**: 4/4 dance beat with Persian vocals.

#### 16. Mizrahi (Israeli Mediterranean pop)
1. **Identity**: late 1950s–60s; Zohar Argov, Avihu Medina, Haim Moshe, Margalit Tzan'ani; Greek influence via Aris San; modern: Eyal Golan, Omer Adam, Static & Ben El, Noa Kirel-adjacent (s for early; c for modern). Ear test: Hebrew vocals with Arabic/Greek/Turkish ornamentation, darbuka + bouzouki/oud, but Western tuning (s).
2. **Tempo**: 95–125; often chiftetelli/maqsum-flavored 4/4 or reggaeton-crossover (c).
3. **Harmony**: Freygish/Hijaz, minor; I–♭II or i–iv–V (c); 12-TET (s).
4. **Melody**: melismatic hooks, Arabic-style trills (c).
5. **Instruments**: oud, kanun, darbuka (s), bouzouki (s link), violins, modern EDM/Europop layers (s).
6. **Rhythm**: chiftetelli or maqsum grids (Q2) with pop kick/snare (c).
7. **Bass**: synth bass on dums (c).
8. **Form**: verse–chorus pop, instrumental bouzouki/violin hook breaks (c).
9. **Production**: bright, loud, wedding-ready (c).
10. **Neighbours**: Greek laiko/skiladiko, Turkish pop, Arabic pop (s for influences).
11. **FL**: Hijaz (12-TET) melody + bouzouki tremolo + darbuka; avoid quarter tones (s). **Fake if**: quarter-tone tuning (wrong for the style), no Mediterranean ornament.

#### 17. Central Asian / Uzbek pop (estrada)
1. **Identity**: Soviet "estrada" lineage (c, unsourced); Yulduz Usmonova, Sevara Nazarkhan, Sogdiana, Rayhon (s); classical root shashmaqam (s). Ear test: Uzbek vocals with Persianate ornaments over doira-driven dance pop; lazgi (Khorezm dance) accelerations.
2. **Tempo**: 100–130 4/4 dance; 6/8 folk dances (c).
3. **Harmony**: minor/modal (Phrygian, Hijaz, Dorian), simple i–VII–VI loops (c).
4. **Melody**: wide melismas, high female vocals (c).
5. **Instruments**: doira (frame drum with jingles) (s), rubab, dutar, tanbur, sato (s), gijak, karnay/surnay (c); synths and drum machines (s "modern rhythms").
6. **Rhythm** (doira, convention): `Dum X . . x | . . X . | X . . x | . . X .` `Jingle/tek . . x . | x . . x | . . x . | x . . x` (c).
7. **Bass**: synth bass on doira dums (c).
8. **Form**: verse–chorus, instrumental dutar/rubab breaks; dance tempo-up finale (c).
9. **Production**: bright synth-pop, wedding-friendly (c).
10. **Neighbours**: Tajik pop, Kazakh Q-pop (K-pop-styled), Azerbaijani pop/meykhana (c).
11. **FL**: doira one-shots (dum, jingle, slap), rubab riff in Hijaz/Phrygian, accelerating automation of tempo in finale (lazgi-like). **Fake if**: Arabic darbuka maqsum instead of doira patterns.
