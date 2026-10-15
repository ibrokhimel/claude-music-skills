# Arrangement and Orchestration for Modern Music Production

Note-numbering convention used throughout: scientific pitch, MIDI 60 = C4 = 261.6 Hz (A4 = MIDI 69 = 440 Hz). FL Studio's piano roll labels MIDI 60 as "C5", so FL label = scientific octave + 1 (e.g. scientific C2 / MIDI 36 shows as "C3" in FL).

## 1. Instrument roles: what each role does and which space it fills

### Takeaway
Producers think in a small number of functional roles, not in track counts: a foundation (drums + bass), a sustained harmonic bed (pad), a counter-rhythm layer that adds motion, a lead (vocal or lead instrument), and fills/answers that live in the gaps of the lead. Each role is defined by a distinct combination of register, rhythmic activity and prominence, and only 3-4 roles should demand attention at once.

### Cited Findings
- Bobby Owsinski's five arrangement elements: **Foundation** (rhythm section, usually bass + drums; rhythm guitar/keys count as foundation if they play the same rhythm), **Pad** (a long sustained note or chord; historically Hammond/Rhodes, now synths, strings or guitar power chords), **Rhythm** (parts playing *counter* to the foundation, e.g. shakers, tambourine, strummed guitar, congas, used to add motion and excitement), **Lead** (lead vocal, lead instrument, solo), **Fills** (occur in the spaces between lead lines, or act as a signature line; they "answer" the lead) — [Bobby Owsinski Blog](https://bobbyowsinskiblog.com/song-arrangement-elements/)
- Same source: usually no more than **four** arrangement elements should play at the same time; three often works well; five rarely works and the arrangement becomes cluttered and confusing — [Bobby Owsinski Blog](https://bobbyowsinskiblog.com/song-arrangement-elements/)
- Orchestration groups sound into three "planes": Foreground (most present), Middleground, Background (least present). The foreground must stand out: usually louder, a strongly characteristic timbre, and prominently placed — [Andy Brick, Orchestration II class notes, Stevens](https://personal.stevens.edu/~abrick/orchestration2/files/HMU398_notes_02.html)
- In melody-and-accompaniment texture the melody is placed in its best range, often at the top, and is contrasted from the accompaniment through timbre, register and rhythmic activity — [Open Music Theory, Core Principles of Orchestration](https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_(Gotham_et_al.)/10%3A_Orchestration/10.01%3A_Core_Principles_of_Orchestration)
- Film-scoring practice: an ostinato pairs naturally with drones/pads (harmonic context) and with melodic lines floating above; contrast between melody and ostinato comes from opposing rhythmic styles or contrasting instrumentation/register — [search summary of film-scoring sources incl. IRPR Sound glossary](https://sounddesign.irpr.agency/glossary/ostinato/)
- Breakdown/break sections in dance music typically strip elements (often removing the kick) and rebuild tension; a riser (often arpeggiated) commonly precedes the chorus/drop — [Home DJ Studio](https://homedjstudio.com/edm-song-structure/)

### Inferences
- Mapping roles to a modern beat/track (for the skill):
  - Foundation = kick + snare/clap + bass/808 (low register, rhythmic anchor).
  - Rhythm (counter-rhythm) = hats, shakers, percussion loops, plucked/strummed comping, arps (high register, busy, low prominence).
  - Pad/harmony = pads, sustained keys, strings, chord stabs (mid register, sustained, background).
  - Lead = vocal, topline, lead synth, main riff/hook (mid-high register, foreground).
  - Fills/counter-melody/ear candy = call-and-response licks, vocal chops, FX, one-shot ear candy placed in the lead's rests.
  - Texture/atmosphere = noise beds, vinyl crackle, field recordings, reverb tails (background; usually full-bandwidth but quiet and filtered).
- A useful rule for the skill: every new part must be assigned a role AND a plane (foreground/middle/background) before being written; if it would become a 5th foreground element, it must replace something or be pushed to background (lower level, filtered, panned, less active).

### Gaps
- No single authoritative source defines "ear candy" or "texture" as formal roles; these are common producer vocabulary rather than a defined taxonomy.

## 2. Why instruments fit together: frequency slotting, register, rhythm, timbre, stereo, figure/ground, masking

### Takeaway
Parts "make sense" together when they differ on at least one (ideally several) axes: frequency/register, rhythmic density, timbre, stereo position and prominence. Masking is mostly an arrangement problem (two parts in the same register doing the same kind of rhythm), and mix EQ can only partly fix it.

### Cited Findings
**Frequency ranges (iZotope EQ cheat sheet; treat as starting points):**

| Instrument | Low end | Body | Mud/boxy zone | Presence/attack | Air |
|---|---|---|---|---|---|
| Kick | 60-80 Hz | 100-200 Hz | 200-500 Hz | 1-5 kHz (click) | - |
| Snare | (cut below 80 Hz) | 150-250 Hz | 300-500 Hz | 2-3.5 kHz | 8 kHz+ |
| Hi-hats | - | - | - | 3-7 kHz | - |
| Toms | 60-120 Hz | - | 250-600 Hz | 800 Hz-1.5 kHz | - |
| Cymbals/overheads | (cut below 150 Hz) | - | - | 4 kHz | 8-12 kHz |
| Bass | 40-120 Hz | 120-250 Hz | 300-500 Hz | 800 Hz-1 kHz | - |
| Acoustic guitar | (cut below 70 Hz) | 200-400 Hz | - | 1.5-2.5 kHz | 8-12 kHz |
| Electric guitar | (cut below 100 Hz) | 150-300 Hz | 200-300 Hz | 2-5 kHz | - |
| Piano | 20-60 Hz | 60-200 Hz | 200-500 Hz | 2-4 kHz | - |
| Vocals | (cut below 100-250 Hz) | - | 500 Hz-1.2 kHz | 5-8 kHz | 10 kHz+ |
| Strings | (cut below 100 Hz) | - | 200-500 Hz | 1-4 kHz | 10 kHz+ |
| Brass | (cut below 150 Hz) | - | 500-800 Hz | 1-5 kHz | 5 kHz+ |
| FX/reverb returns | (cut below 500 Hz) | - | - | 800 Hz-3 kHz | 7 kHz+ |

Source for the whole table: [iZotope EQ cheat sheet](https://izotope.com/en/learn/eq-cheat-sheet)

- Alternative kick breakdown: 40-60 Hz bottom, 60-100 Hz thump, 100-200 Hz body, 200-2,000 Hz ring/hollowness, 2-4 kHz beater attack; snare body 200-400 Hz, ring 400-800 Hz; vocal fullness ~120 Hz, brightness above 10 kHz — [Sonicbids EQ cheat sheet (via search summary)](https://blog.sonicbids.com/the-ultimate-eq-cheat-sheet-for-every-common-instrument)
- Fundamental ranges: double bass approx. 40-200 Hz; piccolo approx. 630 Hz-5 kHz. Charts only show fundamentals; harmonics extend to the limit of hearing and are what let you tell instruments apart. Presence for voice is around 3 kHz even though no sung fundamental is that high. The author warns to treat frequency charts with caution — [Audio Masterclass](https://www.audiomasterclass.com/blog/what-frequencies-do-different-instruments-produce)
- Muddy bass usually lives around 150-500 Hz; harsh vocals around 2.5-4 kHz — [Sound On Sound / EQ sources via search summary](https://www.soundonsound.com/techniques/using-eq)
- Kick vs bass: they must not fight in the arrangement; they can play together rhythmically or never together, but low-frequency parts getting in each other's way is "a fundamental arranging mistake" that no plug-in fully fixes. Kick tone is constant through a song while the bass fundamental moves with the notes — [Sonarworks](https://www.sonarworks.com/blog/learn/eliminate-competition-between-the-kick-and-bass)
- DnB practice: keep sub bass mono and low-passed around 80 Hz; sidechain the sub to the kick to avoid clashing — [Beatportal](https://www.beatportal.com/articles/818379-step-by-step-guide-to-producing-drum-and-bass-like-sub-focus-a-m-c-and-delta-heavy)
- Voicing/spacing: use wider intervals in the bass register and smaller gaps higher up; close voicing gives density and cohesion, open voicing gives clarity and breadth — [Open Music Theory (LibreTexts)](https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_(Gotham_et_al.)/10%3A_Orchestration/10.01%3A_Core_Principles_of_Orchestration)
- Register: middle registers are the most natural/balanced zone for most instruments; low registers add depth and power but muddy when overused — [orchestration sources via search summary, Alan Belkin](https://alanbelkinmusic.com/orchestration-basic-notions-pt-2/)
- Rule of three: the brain can effectively focus on about three elements at once; limit attention-pulling parts to three and keep the rest consistent and unflashy (e.g. if guitar riff + key vocal + cool bassline happen together, the drums should take a back seat). An "element" is what is *heard* as one part: several drum tracks, or several guitars playing the same rhythm, count as one. Attributed to producers such as Max Martin and Jack Joseph Puig — [Dave Johnston, Music Factory](https://musicfactory.davejohnston.nz/p/less-is-more-using-the-rule-of-three?r=11vles); [EDMProd 3 Tips (via search)](https://www.edmprod.com/3-tips-for-better-song-arrangements/)

### Inferences
- **Register map for the skill (derived from MIDI/frequency math, f = 440 x 2^((n-69)/12); not a cited chart):**

| Zone | Approx Hz (fundamentals) | MIDI range (sci. pitch) | FL label | Typical occupants |
|---|---|---|---|---|
| Sub | 30-60 Hz | 23-34 (B0-A#1) | B1-A#2 | 808/sub fundamentals, kick body |
| Bass | 60-130 Hz | 35-48 (B1-C3) | B2-C4 | bassline, 808 upper notes, kick punch |
| Low-mid | 130-260 Hz | 48-60 (C3-C4) | C4-C5 | chord roots/5ths, left hand piano, male vocal low |
| Mid (harmony core) | 260-1000 Hz | 60-83 (C4-B5) | C5-B6 | pads, chords, guitars, vocals, most leads |
| Upper-mid | 1-4 kHz | 84-107 (C6-B7) | C7-B8 | lead/bell tops, plucks, arps (and the presence harmonics of everything) |
| High | 4 kHz+ | (mostly harmonics, noise) | - | hats, shakers, cymbals, air, noise FX |

  Reference points: C1 = MIDI 24 = 32.7 Hz; C2 = 36 = 65.4 Hz; C3 = 48 = 130.8 Hz; C4 = 60 = 261.6 Hz; C5 = 72 = 523.3 Hz; C6 = 84 = 1046.5 Hz.
- **Practical slotting rules the skill can apply:**
  1. Only ONE part owns the region below ~100 Hz at any moment (808/sub OR bass, with the kick either sidechained against it or rhythmically interlocked).
  2. Bass/808 notes roughly MIDI 28-47 (E1-B2); avoid chords below ~MIDI 48 (C3) — keep only root, root+octave or root+5th down there (consistent with "wide intervals low" above).
  3. Chord/pad voicings mostly MIDI 48-76 (C3-E5), close-ish voicing in the middle, wider spacing at the bottom.
  4. Lead/topline sits above the chord bed (roughly MIDI 60-84) or, if the chord bed is high, moves to a different register or timbre; the lead should be the top or most distinctive voice.
  5. Counter-melody goes in a different register (usually above or below the lead by an octave-ish) and plays in the lead's rests (call/response).
  6. Rhythmic complementarity: if a part is busy (e.g. 1/16 hats, rolling arp, rapid vocal), its neighbours in the same register should be sustained or sparse; busy + busy is only OK when they are in different registers.
  7. Timbral contrast: when two parts share a register, make them contrast in timbre (e.g. soft pad vs bright pluck) or in stereo (pad wide, lead centre).
  8. Stereo: kick, snare, bass/808, lead vocal centred; pads, doubled guitars, backing vocals, percussion and FX spread wider (common practice; not individually cited above).
- Ear candy and atmosphere should be background plane: lower level, filtered (high-pass), wider, and placed in gaps rather than over the lead.

### Gaps
- The Independent Recording Network interactive frequency chart could not be fetched; the iZotope table above is the primary cited chart. No authoritative source gave MIDI-note playable ranges for synth roles (those are inferred above from frequency math).
- Stereo placement conventions are widely repeated but no fetched source stated them with specifics.

## 3. Orchestration principles applied to production (doubling, voicing, counterpoint, texture, focal elements)

### Takeaway
Classical orchestration contributes four reusable ideas: (a) organise the texture into foreground/middleground/background planes, (b) double lines in octaves/unisons for weight and colour, but avoid constant doubling which sounds "grey", (c) space chords like the harmonic series (wide low, close high), and (d) build intensity by adding instrument families, widening the range and mixing long and short note values.

### Cited Findings
- Three planes of sound (foreground/middleground/background); foreground is louder, more characteristic in colour and prominently placed — [Andy Brick, Stevens](https://personal.stevens.edu/~abrick/orchestration2/files/HMU398_notes_02.html)
- Everyone playing independent counterpoint all the time tires the ear; on the other hand, lots of doubling sounds grey and uninteresting. Composers sketch clear leading lines first, then elaborate around what is most audible; most of the time only part of the orchestra plays — [Alan Belkin, Orchestration Basic Notions Pt. 2](https://alanbelkinmusic.com/orchestration-basic-notions-pt-2/)
- Octave doublings can be used expressively to colour a chord; individualising doublings into a pseudo-counterpoint (rather than mechanical duplication) adds nuance — [Alan Belkin (via search summary)](https://alanbelkinmusic.com/orchestration-basic-notions-pt-2/)
- Texture types: polyphonic (instruments balanced and blended), melody-and-accompaniment (melody in its best range, often at the top, contrasted by timbre/register/rhythm), antiphonal (material passed between groups). Blend via equally strong instruments and registers; Mozart example doubles in three octaves across winds and strings. Crescendo by adding instruments (strings -> winds -> brass -> percussion), expanding the overall range, and diversifying note values (sustains + short figures) — [Open Music Theory (LibreTexts)](https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_(Gotham_et_al.)/10%3A_Orchestration/10.01%3A_Core_Principles_of_Orchestration)
- Film scoring: start with a quiet ostinato and gradually add layers, raise dynamics and thicken the orchestration to build tension — [search summary, film-scoring sources incl. IRPR glossary](https://sounddesign.irpr.agency/glossary/ostinato/)
- Focal-element limit: 3 (rule of three) to 4 (Owsinski) simultaneous attention-pulling elements — [Owsinski](https://bobbyowsinskiblog.com/song-arrangement-elements/); [Music Factory](https://musicfactory.davejohnston.nz/p/less-is-more-using-the-rule-of-three?r=11vles)

### Inferences
- Production translations:
  - **Octave doubling** of a lead/hook (e.g. lead at MIDI 72 + layer at 60 or 84) = more weight/brightness without adding a new focal element; use it in choruses/drops, remove it in verses for contrast.
  - **Unison layering** (two synths, same notes, different timbres, or a vocal double) thickens without changing the line.
  - **Voicing chords across instruments**: bass plays root (low), pad plays 3rd/7th/extensions in the middle, keys or pluck plays upper voicing; do not duplicate the 3rd in multiple low parts.
  - **Counterpoint**: counter-melody moves when the lead holds or rests; contrary motion and different rhythm values keep them separable.
  - **Texture types in beat terms**: monophonic = a single line/sample alone (intros, drop-outs); homophonic = melody over chord bed (most verses/choruses); polyphonic = several independent lines (climax sections, only if they are separated by register and rhythm).
  - **Orchestral crescendo recipe for builds**: add a family (perc -> pads -> lead layers), widen the range (add sub octave and top octave), and add shorter note values (1/8 -> 1/16 -> 1/32 rolls) over sustained notes.

### Gaps
- Rimsky-Korsakov's Principles of Orchestration was not directly accessed (only mirror PDFs of uncertain provenance surfaced); no specific Rimsky-Korsakov rules are cited here.
- Berklee Online course pages were found but not content-rich enough to cite.

## 4. Song structures and bar counts by genre; why 4/8/16-bar multiples

### Takeaway
Modern genres are built from 4-bar phrases grouped into 8- and 16-bar sections. Hip-hop: 16-bar verses, 8-bar hooks. EDM: intro 16-32, build 8-16, drop 16-32, breakdown 16-32, outro 16-32 (club) or compressed for streaming. Pop: first chorus around 40 seconds, ~3-3.5 minutes total.

### Cited Findings
- Electronic arrangements move in multiples of 8 bars; the ear expects these blocks; 7- or 9-bar deviations work only as a deliberate effect — [Inspired by Beatz](https://www.inspiredbybeatz.com/en/edm-arrangement-from-loop-to-exciting-track/)
- EDM section lengths: Intro 16-32 bars (low energy), Build-up 8-16 (rising), Drop 16-32 (high), Breakdown 16-32 (low-medium), Outro 16-32 (falling); six to eight sections in most tracks (Intro, Build, Drop, Breakdown, Build 2, Drop 2, Outro) — [Inspired by Beatz](https://www.inspiredbybeatz.com/en/edm-arrangement-from-loop-to-exciting-track/)
- Streaming vs club: on streaming the first 30 s matter and the drop arrives within ~30-60 s, radio edit 3.5-4 min; club/extended mixes 5-7 min with long beatmatch-friendly intros/outros — [Inspired by Beatz](https://www.inspiredbybeatz.com/en/edm-arrangement-from-loop-to-exciting-track/)
- Alternative EDM template: Intro 8-16, Build 8, Drop 16-32, Breakdown 8-16, Build, Drop, Outro — [ai-creator-toolkit song-structure knowledge file (search summary; secondary source)](https://cdn.jsdelivr.net/npm/ai-creator-toolkit@1.4.0/skills/composer/knowledge/song-structure.md)
- Dance music: 4 beats per bar and 4 bars per phrase (16 beats); intros are kick + percussion so DJs can beatmatch; outro mirrors intro, removing elements so the next record can mix in — [Home DJ Studio](https://homedjstudio.com/edm-song-structure/)
- Dance tunes generally progress in 16-bar sections; within them elements are 1-, 2-, 4- or 8-bar repeating phrases and tend to change every 4 or 8 bars; DJ phrases are 8 or 16 bars — [Wikipedia: Phrasing (DJ)](https://en.wikipedia.org/wiki/Phrasing_(DJ)); [DJ.Studio](https://dj.studio/blog/phrasing-dj-mixing)
- Mixed In Key's guidance is deliberately non-prescriptive: 8- and 16-bar phrases are "useful starting points, not mandatory lengths"; suggested exercise is a rough 64-bar layout with four labelled sections (intro, main section, contrast section, return) — [Mixed In Key](https://mixedinkey.com/?p=5367). (A search snippet attributed a fuller template — Intro 8/16/32, Verse 8/16/32, Chorus 8/16, Breakdown 8/16/32, etc. — to Mixed In Key, but the fetched page did not contain it; treat that template as unverified.)
- Different dance sub-genres emphasise different sections: DnB is all about the first drop; house tends to build steadily — [Mixed In Key (search summary)](https://mixedinkey.com/?p=5367)
- Hip-hop sections: Intro (fewer elements, builds to verse/hook), Verse (simpler beat leaving room for vocals, usually 16 bars), Hook (most elements, usually 8 bars), Bridge (usually 8 bars, more in R&B/pop, before last verse), Outro (fades). Structures: Intro-V-H-V-H-V-H-Outro or Intro-H-V-H-V-H-V-H-Outro; R&B: Intro-V-H-V-H-Bridge-H-H-Outro — [HipHopMakers](https://hiphopmakers.com/how-to-make-beats-song-arrangements)
- Typical rap song: 4-8 bar intro, three 16-bar verses, three 8-bar hooks, optional 4-8 bar bridge between hook 2 and verse 3, outro — [search summary of rap-structure sources](https://oude-site.samenvoorbiodiversiteit.nl/how-many-bars-are-in-a-rap/) (low-authority source)
- Trap blueprint: intro 8 bars; verse/drop 16 bars with kick, 808, hats (+ vocal); hook 16 bars with bigger 808 and extra layers — [WA Production blueprints (search snippet; page not fully fetched)](https://blog.waproduction.com/arrangement-blueprints-10-proven-song-maps-that-just-work)
- Lo-fi: work in 4-bar sections and loop them; a full beat is typically 64-96 bars (intro, verses, hooks, outro); 3-bar loops can also be effective; 8-20% swing for human bounce — [search summaries of Lunacy Audio](https://lunacy.audio/how-to-make-lofi-music/), [Violet Recording](https://violetrecording.com/how-long-should-a-beat-be/), [BeatTips on 3-bar loops](https://beattips.com/beattips-tutorials-working-from-3-bar-loop-arrangement-schemes-2/)
- DnB (174 BPM) timeline: Intro 0:00-0:45 (pads, arps, risers), Build 0:45-1:00 (drums and bass filter in), Drop 1:00-2:00 (full drums + bass), Breakdown 2:00-2:30 (stripped, melodic), Drop 2 2:30-3:30 (variation), Outro 3:30-4:00 — [Beatportal](https://www.beatportal.com/articles/818379-step-by-step-guide-to-producing-drum-and-bass-like-sub-focus-a-m-c-and-delta-heavy). Another source gives bars: 16-bar intro, 8-bar build, 32-bar Drop 1, 16-bar breakdown, 32-bar Drop 2, 8-16-bar outro — [Violet Recording (search summary)](https://violetrecording.com/how-to-make-drum-and-bass/)
- Pop: Billboard Hot 100 #1s 2020-2023 reportedly reach the first chorus at ~38 s on average vs 55+ s in earlier decades; Taylor Swift hits average ~42 s; #1 pop hit average length 3:44 with 3:00-3:29 the most common range; ABABCB (verse-chorus-verse-chorus-bridge-chorus) in 67% of #1 pop hits; hook recurs every 30-45 s — [Hit Songs Deconstructed (Taylor Swift structure PDF)](https://hitsongsdeconstructed.com/wp-content/uploads/2024/04/The-Taylor-Swift-Evolution-Structure.pdf); [djwillgill.com aggregator](https://djwillgill.com/how-to-write-band-music-in-2026/) — note: several of these figures came through an aggregator summary and were not verified on the primary HSD report pages.
- Peer-reviewed study of 14,556 tracks (1956-2020): average length 3.95 min — [reported via djwillgill.com aggregator](https://djwillgill.com/how-to-write-band-music-in-2026/) (primary paper not located)

### Inferences
- Why multiples of 4/8: 4/4 bars group into 2-bar call/response, 4-bar phrases, 8-bar periods; listeners and DJs anticipate change at 8/16-bar boundaries, so placing changes on those boundaries feels "right", and breaking it (e.g. a 6-bar pre-chorus or 1-bar drop-out) becomes a deliberate surprise.
- Time conversions for the skill: bar length (s) = 240 / BPM. At 140 BPM a 16-bar verse = 27.4 s; at 128 BPM 32 bars = 60 s; at 174 BPM 32 bars = 44 s; at 90 BPM (hip-hop/lo-fi) 16 bars = 42.7 s.
- Genre templates (synthesised from the cited figures above + common practice; validate per reference track):
  - **Trap / hip-hop beat (130-160 BPM half-time feel, or 70-80):** Intro 4-8 (melody/sample only, maybe filtered) -> Hook 8 (full: kick, 808, hats with rolls, snare/clap, melody, counter) -> Verse 16 (drop a melodic layer or simplify hats; keep 808 + drums) -> Hook 8 -> Verse 16 (vary: new perc, 808 pattern change, drop-outs on bar 8/16) -> Bridge/breakdown 4-8 (melody alone or no drums) -> Hook 8 -> Outro 4-8 (melody alone/fade). Total ~ 72-96 bars.
  - **Pop (100-125 BPM):** Intro 4-8 -> Verse 8-16 -> Pre-chorus 4-8 -> Chorus 8 -> Verse 2 8-16 -> Pre 4-8 -> Chorus 8 -> Bridge 8 -> Final chorus 8-16 (double chorus) -> Outro 4-8; first chorus target ~40 s; total ~3:00-3:30.
  - **House / techno (120-130 BPM, club):** Intro 16-32 (kick + perc only for DJs) -> Groove/verse 32 (add bass, hats, then lead/hook every 8-16 bars) -> Breakdown 16-32 (no kick; pads/vocal/main idea) -> Build 8 -> Main section/drop 32 -> second breakdown or "cool down" 16 -> Outro 16-32 (strip back to kick + perc). 6-7 min extended.
  - **EDM festival (126-150 BPM):** Intro 16 -> Breakdown/verse 16 -> Build 8-16 -> Drop 16-32 -> Breakdown 16 -> Build 8 -> Drop 2 16-32 (variation) -> Outro 16. Radio edit 3-4 min, drop within 30-60 s.
  - **Lo-fi (70-90 BPM):** 4-bar loops; Intro 4-8 (keys/sample with filter, vinyl texture) -> A 16 (drums + bass + keys) -> B 8-16 (variation: chord change, drum drop-out, added melody) -> A 16 -> outro 4-8; total 64-96 bars (~2-3 min).
  - **R&B (60-100 BPM):** Intro 4-8 -> Verse 16 (sparse drums, keys/pads, bass) -> Pre 4 -> Hook 8 -> Verse 16 -> Hook 8 -> Bridge 8 -> Hook x2 -> Outro.
  - **Drum & bass (170-176 BPM):** Intro 16-32 (atmospheric, DJ-friendly) -> Build 8 -> Drop 1 32 -> Breakdown 16-32 -> Build 8 -> Drop 2 32 (variation: new bass, switch-up) -> Outro 16-32.
  - **Cinematic cue:** usually not bar-quantised to 8s; structure follows picture. Typical build: ostinato alone -> add low drone/pad -> add melody -> add brass/percussion and widen range -> climax -> pull back to a single sustained element.

### Gaps
- No primary source fetched gave verified bar-count templates specifically for R&B, house vs techno differences, or cinematic cues; those templates are inferences.
- Hit Songs Deconstructed primary reports are paywalled; pop statistics are from a PDF and an aggregator, not independently verified.

## 5. Energy and tension management: curves, builds, drops, breakdowns, transitions

### Takeaway
Treat tension (expectation of release) and energy (intensity/momentum) as separate controls. Plan an energy map (score each section 1-9) before arranging; build tension at macro scale with layered risers/snare rolls/filter sweeps over 8-16 bars, and at micro scale with fills, kick removals and reverse crashes every 4-8 bars; drops only work if the previous section cleared space.

### Cited Findings
- Tension = the perceived need for relaxation/release created by listener expectations; energy = overall intensity and momentum, which can exist without tension (a steady 4/4 kick has energy but little tension). Energy types: overall (genre/tempo), rhythmic (kick + bass groove), sonic (mix quality) — [EDMProd, Advanced Guide to Tension and Energy](https://edmprod.com/tension)
- Macro-tension (section scale): risers, snare rolls, automated filtering, melodic shifts. Micro-tension: short fills, kick removals, reverse crashes, one-bar breaks, chord/melody changes — [EDMProd](https://edmprod.com/tension)
- Tension tools: white-noise sweeps, pitched risers (rising 5-24 semitones), rhythmic risers (saw/square); snare rolls typically 4-8 bars with optional pitch automation; high-pass filter automation; leaps larger than a fifth; dominant 7ths, deceptive cadences, suspensions, pedal tones — [EDMProd](https://edmprod.com/tension)
- Energy-mapping method: rate each section of reference tracks 1 (lowest) to 9 (highest) and draw a planned energy curve before arranging — [EDMProd](https://edmprod.com/tension)
- EDMProd worked example (bar numbers): Intro 1-32 — layer 1 (drum additions: clap at bar 8, filtered hat from bar 12), layer 2 at bar 16 (noise sweep + pitched riser, subtle), layer 3 at bar 24 (snare roll starts, kick removed, rhythmic riser at full volume) -> Verse 32-64 (no new tension for first 8 bars, new instrument at bar 16 of section, build in last 8 bars) -> Breakdown 64-96 (main idea, 3-chord progression) -> Build 96-104 (reuse intro build, repeat dominant chord, **one bar of silence before the drop**) -> Chorus/drop 104-136 — [EDMProd](https://edmprod.com/tension)
- Layered build analysis (MAKJ "Springen"): layer 1 riff + noise sweeps/subtle pitch risers; layer 2 adds snare roll + pluck riser; layer 3 repeats a single note of the riff, speeds up the snare roll and adds vocal samples — [EDMProd](https://edmprod.com/tension)
- Reverse crash + crash: duplicate a crash, reverse the copy, place it before the hit; heard every 8, 16 or 32 bars; keep the reverse quieter and end it slightly before the real crash; adding reverb/delay before reversing gives a better swell — [EDMProd](https://edmprod.com/tension)
- Energy is relative: a drop only hits if the breakdown before it clears space; when everything plays at once there is no room to escalate. Transition tools: risers, sweeps, snare rolls, split-second silence before the drop; filter cutoff opening over the build; reverb throws at phrase ends; volume swells under risers. Mistakes: everything at once, no breakdown, second drop identical to the first — [Inspired by Beatz](https://www.inspiredbybeatz.com/en/edm-arrangement-from-loop-to-exciting-track/)
- Signal transitions with fills, held notes or gaps; avoid repeating the same fill every time — save the strongest signal for the biggest change — [Mixed In Key](https://mixedinkey.com/?p=5367)
- Orchestral crescendo: add instrument families, expand total range, mix longer and shorter values — [Open Music Theory (LibreTexts)](https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_(Gotham_et_al.)/10%3A_Orchestration/10.01%3A_Core_Principles_of_Orchestration)

### Inferences
- Default energy curves (1-9 scale) the skill can use:
  - Pop: Intro 3 -> V1 4 -> Pre 5 -> Ch1 7 -> V2 5 -> Pre 6 -> Ch2 8 -> Bridge 4-5 -> Final Ch 9 -> Outro 3.
  - EDM: Intro 3 -> Break 4 -> Build 5->7 -> Drop 9 -> Breakdown 3 -> Build 5->8 -> Drop2 9 -> Outro 3.
  - Trap: Intro 3 -> Hook 8 -> Verse 6 -> Hook 8 -> Verse 6-7 -> Bridge 4 -> Hook 9 -> Outro 3.
  - Each repeat of a section should sit at or slightly above its previous instance (add a layer, octave double, or new percussion).
- Build recipe (8 bars before a drop/chorus): bars 1-4 snare/clap on quarters -> bars 5-6 eighths -> bar 7 sixteenths -> bar 8 32nds/triplets; white-noise riser over all 8 bars; high-pass filter on music bus sweeping up; pitch riser 12 semitones; remove kick and/or bass in last 1-2 bars; optional 1 beat to 1 bar of silence or a vocal pickup; drop lands with crash + sub/808 hit + full drums.
- Rule of contrast: adjacent sections should differ on at least 2 of: element count, low-end presence (bass/kick on/off), rhythmic density (hat subdivision), register span, stereo width, lead type (vocal vs instrumental).

### Gaps
- No numeric research (e.g., listener studies) was found quantifying how long a breakdown must be for the next drop to feel bigger; guidance is practitioner-based.

## 6. Turning a loop into a song: workflows and keeping listener interest

### Takeaway
The dominant workflow is subtractive: build the densest section (drop/hook) as an 8- or 16-bar loop, duplicate it across the timeline, then mute parts to create intro/verse/breakdown, and add something new or take something away at every 8- or 16-bar boundary, with small fills/variations every 4 bars. Reference-track mirroring and section markers are common aids.

### Cited Findings
- Subtractive workflow: finish the drop first, copy it, strip drums (keep kick or one element) for the breakdown, strip further for the intro; "subtraction is faster than addition" — [Inspired by Beatz](https://www.inspiredbybeatz.com/en/edm-arrangement-from-loop-to-exciting-track/)
- Map the strongest section first (where drums, bass and hook combine), then create contrast by subtraction (mute bass, remove percussion layers) before adding effects; rough out a 64-bar version with four labelled sections — [Mixed In Key](https://mixedinkey.com/?p=5367)
- Attack Magazine's four ways out of the loop: (1) jam it out — record clip launches live into the arrangement; (2) copy it out — drop a reference track into the DAW and mirror its decisions (when it adds a kick, you add a kick; when it cuts the bass, you cut yours); (3) turn it out — start with the kick and add a new element every 8-16 bars, then subtract approaching the end; (4) mark it out — place markers (Intro, Breakdown 1, Drop 1, Breakdown 2, Drop 2, Cool Down, Outro) as scaffolding — [Attack Magazine](https://www.attackmagazine.com/technique/tutorials/4-ways-to-break-out-of-the-loop/)
- Within 16-bar sections, elements change every 4 or 8 bars — [Wikipedia: Phrasing (DJ)](https://en.wikipedia.org/wiki/Phrasing_(DJ))
- Use automation to keep the track evolving — [Beatportal](https://www.beatportal.com/articles/818379-step-by-step-guide-to-producing-drum-and-bass-like-sub-focus-a-m-c-and-delta-heavy)
- Lo-fi variation: loop drums and bass but vary the keys (e.g., key/chord change) so the groove can settle while small changes keep interest — [search summary, Lunacy Audio / MusicRadar lo-fi guides](https://lunacy.audio/how-to-make-lofi-music/)
- Fills answer the lead in its gaps (call and response) — [Bobby Owsinski Blog](https://bobbyowsinskiblog.com/song-arrangement-elements/)

### Inferences
- Step-by-step for an FL Studio skill (loop -> song):
  1. Make the "full" 8-bar loop as separate patterns per role (drums split into kick / snare-clap / hats / perc; 808/bass; chords; lead; counter; FX).
  2. Decide genre template + BPM; compute bars per section (section 4 table) and place markers in the playlist.
  3. Paste the full loop across all high-energy sections (hook/drop/chorus).
  4. Subtract for each lower section: intro = 1-2 elements (melody filtered, or drums only for DJ tools); verse = remove lead layer/counter, simplify hats, keep bass + kick; breakdown = remove kick and bass, keep pad/lead/vocal.
  5. Make "B" variants of patterns (hat pattern with rolls, 808 with slides/octave jumps, chord inversion change, melody with different ending) and alternate them every 4 or 8 bars so no exact 8-bar block repeats more than twice in a row.
  6. At every 8-bar boundary: something enters, leaves or changes. At every 4-bar end: a micro-variation (fill, drum drop-out on the last beat, 808 slide, reverse crash).
  7. Insert transitions on section boundaries: riser/snare roll into high-energy sections, crash/impact on downbeat 1, reverse cymbal or vocal pickup before hooks, one beat-to-one bar of silence before the biggest hit, downlifter/filter-close leaving high-energy sections.
  8. Add automation movement: filter cutoff, reverb send, volume swells, panning, so even repeated loops evolve.
  9. Verify the focal-element count per section is 3-4 and the low-end has one owner at any time.

### Gaps
- No quantitative source was found for "a new element every 8 bars" beyond the Attack Magazine 8-16 bar guidance and the DJ-phrasing 4/8-bar change convention.

## 7. Genre arrangement templates (summary of what plays where)

### Takeaway
Templates differ mainly in (a) section lengths, (b) whether the energy peak is a vocal chorus, a hook, or an instrumental drop, and (c) how DJ-functional intros/outros must be. The cited data supports hip-hop (16/8), EDM (8-bar multiples, 16-32 bar sections), DnB (32-bar drops) and pop (early chorus) most strongly; lo-fi, R&B, house/techno specifics and cinematic cues rely more on inference.

### Cited Findings
- Hip-hop: verse = simpler beat leaving room for vocal (16 bars); hook = most elements (8 bars); intro has fewer elements and builds; R&B adds a bridge before final hooks — [HipHopMakers](https://hiphopmakers.com/how-to-make-beats-song-arrangements)
- Trap: intro 8 bars; verse 16 with kick, 808, hats (+vocal); hook 16 with bigger 808 and extra layers — [WA Production (search snippet)](https://blog.waproduction.com/arrangement-blueprints-10-proven-song-maps-that-just-work)
- EDM: Intro/Build/Drop/Breakdown/Build/Drop/Outro; drop is the highest-energy section; breakdown low-medium energy — [Inspired by Beatz](https://www.inspiredbybeatz.com/en/edm-arrangement-from-loop-to-exciting-track/)
- House/techno: start with the kick and add new elements every 8 or 16 bars; DJ-friendly intro is kick + percussion; outro mirrors intro — [Attack Magazine](https://www.attackmagazine.com/technique/tutorials/4-ways-to-break-out-of-the-loop/); [Home DJ Studio](https://homedjstudio.com/edm-song-structure/)
- DnB: 172-176 BPM; 2-bar breakbeat with snares on 2 and 4, clean sub underneath, then intro/drop/breakdown/second drop; second drop introduces variation — [Violet Recording (search summary)](https://violetrecording.com/how-to-make-drum-and-bass/); [Beatportal](https://www.beatportal.com/articles/818379-step-by-step-guide-to-producing-drum-and-bass-like-sub-focus-a-m-c-and-delta-heavy)
- Lo-fi: kick typically on 1 and 3, snare on 2 and 4; 4-bar sections; 64-96 bars total — [search summary of Lunacy Audio / Violet Recording](https://lunacy.audio/how-to-make-lofi-music/)
- Cinematic: begin with a quiet ostinato and gradually add layers, raise dynamics, thicken orchestration; pads/drones give harmonic context with melody above — [IRPR Sound glossary (search summary)](https://sounddesign.irpr.agency/glossary/ostinato/)
- Pop: ABABCB structure dominant among #1 pop hits; first chorus ~38-42 s — [Hit Songs Deconstructed PDF / aggregator](https://hitsongsdeconstructed.com/wp-content/uploads/2024/04/The-Taylor-Swift-Evolution-Structure.pdf)

### Inferences
- Element matrix (X = plays, ~ = partial/filtered, - = out) for a trap beat as a model the skill can generalise:

| Section (bars) | Kick | 808 | Snare/clap | Hats | Perc | Chords/sample | Lead/hook melody | Counter/ear candy | FX/transitions |
|---|---|---|---|---|---|---|---|---|---|
| Intro (8) | - | - | - | ~ | - | ~ (filtered) | ~ | - | riser into hook |
| Hook (8) | X | X | X | X (rolls) | X | X | X | X | crash on 1 |
| Verse 1 (16) | X | X | X | X (simpler) | ~ | X | - | ~ (bar 8/16 fills) | drop-out on bar 16 |
| Hook (8) | X | X | X | X | X | X | X | X | reverse cymbal in |
| Verse 2 (16) | X | X (new pattern) | X | X (variation) | X (new) | X | ~ | X | |
| Bridge (8) | - | ~ | - | ~ | - | X | X | - | silence/impact |
| Hook (8) | X | X | X | X | X | X | X (+ octave layer) | X | |
| Outro (8) | - | - | - | - | - | X (fading) | ~ | - | downlifter |

- Same matrix logic for EDM: Intro (kick+perc, or pads) / Breakdown (no kick, pads + lead idea + vocal) / Build (snare roll, riser, HPF, kick removed last bars) / Drop (kick, bass, lead, full drums, sidechained pads) / Outro (kick + perc).
- For pop: verse = drums (lighter), bass, one harmony instrument, vocal; pre-chorus adds pad/rhythm layer and rising harmony; chorus adds backing vocals, octave-doubled hook, fuller drums, wider stereo; bridge drops drums or changes harmony; final chorus adds one more layer than chorus 2.

### Gaps
- Primary per-genre bar studies for R&B, lo-fi and house vs techno (distinct from generic EDM) were not found in authoritative sources during this session; MusicRadar's club-track arrangement article could not be retrieved (truncated page). A "Mixed In Key" bar template surfaced in search snippets but was not present on the fetched page.
