# Song-form templates, bar maps and element matrices by genre

Section lists with bar counts, what plays in each section, timing targets and the bars-to-seconds math. Bars are FL bars at the project tempo unless stated.

## Contents
1. Why 4/8/16-bar blocks
2. Bars-to-seconds table and formulas
3. Hip hop, trap, drill, boom bap, R&B, afrobeats, amapiano, jersey club, lo-fi
4. Pop (with timing data)
5. EDM, house, techno, trance, DnB, dubstep, future bass, UKG, synthwave, hyperpop, ambient
6. Cinematic three-act cue
7. Element matrices (trap section grid, EDM, pop, house)
8. How to adapt a template
9. Sources

## 1. Why 4/8/16-bar blocks

- 4/4 bars group into 2-bar call/response, 4-bar phrases and 8-bar periods; listeners and DJs expect change at 8/16-bar boundaries **(derived)**.
- Electronic arrangements move in multiples of 8 bars; 7- or 9-bar deviations work only as a deliberate effect (Inspired by Beatz) **(sourced)**.
- Dance tunes progress in 16-bar sections whose elements are 1/2/4/8-bar loops changing every 4 or 8 bars; DJ phrases are 8 or 16 bars (Wikipedia: Phrasing (DJ)) **(sourced)**.
- Mixed In Key treats 8/16-bar phrases as "useful starting points, not mandatory lengths"; not every track needs a breakdown **(sourced)**.
- Deliberate odd lengths (convention): a 2-bar pre-hook tag, a 6-bar pre-chorus, a 1-bar drop-out or a 9th bar of silence before the drop. Use one per song, as a surprise.

## 2. Bars to seconds

Formulas **(derived)**: `bar s = 240 / BPM`; `section s = bars x 240 / BPM`; `bars = s x BPM / 240`; section start bar (FL, 1-based) = 1 + sum of earlier section lengths; start time = (start bar - 1) x 240 / BPM.

| BPM | 1 bar | 4 | 8 | 16 | 32 | 64 | bars in 30 s | bars in 60 s |
|---|---|---|---|---|---|---|---|---|
| 70 | 3.43 | 13.7 | 27.4 | 54.9 | 109.7 | 219.4 | 8.8 | 17.5 |
| 75 | 3.20 | 12.8 | 25.6 | 51.2 | 102.4 | 204.8 | 9.4 | 18.8 |
| 85 | 2.82 | 11.3 | 22.6 | 45.2 | 90.4 | 180.7 | 10.6 | 21.2 |
| 90 | 2.67 | 10.7 | 21.3 | 42.7 | 85.3 | 170.7 | 11.2 | 22.5 |
| 100 | 2.40 | 9.6 | 19.2 | 38.4 | 76.8 | 153.6 | 12.5 | 25.0 |
| 105 | 2.29 | 9.1 | 18.3 | 36.6 | 73.1 | 146.3 | 13.1 | 26.2 |
| 110 | 2.18 | 8.7 | 17.5 | 34.9 | 69.8 | 139.6 | 13.8 | 27.5 |
| 120 | 2.00 | 8.0 | 16.0 | 32.0 | 64.0 | 128.0 | 15.0 | 30.0 |
| 124 | 1.94 | 7.7 | 15.5 | 31.0 | 61.9 | 123.9 | 15.5 | 31.0 |
| 128 | 1.88 | 7.5 | 15.0 | 30.0 | 60.0 | 120.0 | 16.0 | 32.0 |
| 138 | 1.74 | 7.0 | 13.9 | 27.8 | 55.7 | 111.3 | 17.2 | 34.5 |
| 140 | 1.71 | 6.9 | 13.7 | 27.4 | 54.9 | 109.7 | 17.5 | 35.0 |
| 145 | 1.66 | 6.6 | 13.2 | 26.5 | 53.0 | 105.9 | 18.1 | 36.2 |
| 150 | 1.60 | 6.4 | 12.8 | 25.6 | 51.2 | 102.4 | 18.8 | 37.5 |
| 160 | 1.50 | 6.0 | 12.0 | 24.0 | 48.0 | 96.0 | 20.0 | 40.0 |
| 174 | 1.38 | 5.5 | 11.0 | 22.1 | 44.1 | 88.3 | 21.8 | 43.5 |

**Half-time genres (derived, flag to the user):** trap and drill projects usually run at 130-160 BPM with the backbeat on beat 3, so they feel like 65-80 BPM. A rapper may count a "bar" as one felt half-time bar = 2 FL bars. Templates below count FL bars. If the user says "16-bar verse" and means ~45-55 s at 140 BPM, use 32 FL bars. When unsure, give both bar counts and seconds.

## 3. Rap, urban and global

### Hip hop (general, sourced: HipHopMakers)
Sections: Intro (fewer elements, builds into the verse or hook), Verse 16 (simpler beat, room for vocals), Hook 8 (most elements), Bridge 8 (before the last verse; longer in R&B/pop), Outro (fades/strips).
Forms: `Intro-V-H-V-H-V-H-Outro` or `Intro-H-V-H-V-H-V-H-Outro`.
Default (convention): Intro 8, Hook 8, Verse 16, Hook 8, Verse 16, Hook 8, Outro 4-8; drop drums/808 for the last beat or bar before each hook.

### Trap (140 BPM; 130-160)
WA Production blueprint (snippet-level source): Intro 8, Verse 16 (kick, 808, hats + vocal), Hook 16 (bigger 808, extra layers).
Default (convention):

| Section | Bars | FL bars | Start s at 140 |
|---|---|---|---|
| Intro | 8 | 1-8 | 0.0 |
| Hook 1 | 8 | 9-16 | 13.7 |
| Verse 1 | 16 | 17-32 | 27.4 |
| Hook 2 | 8 | 33-40 | 54.9 |
| Verse 2 | 16 | 41-56 | 68.6 |
| Bridge | 8 | 57-64 | 96.0 |
| Hook 3 | 8 | 65-72 | 109.7 |
| Outro | 8 | 73-80 | 123.4 (ends 137.1 = 2:17) |

For a longer vocal song use 16-bar hooks and 32-FL-bar verses (about 3:30-4:00).

### Drill (UK 138-145; NY 140-145)
Sourced template (Beatstorapon): Intro 1-8, Hook 9-16, Verse 17-32, Hook 33-40, Verse 41-56, Bridge 57-64, Hook 65-72, Outro 73-80; make a noticeable change every 4 or 8 bars. Same bar map as trap above. Verse variation: switch hat pattern (3+3+2 vs straight), move a snare, change 808 slide placement every 8 bars (`music-drums-groove`, `music-bass-808`).

### Boom bap (85-95)
Intro 4-8 (sample alone or filtered), V 16, H 8, V 16, H 8, V 16, H 8, Outro 4-8. Variation is mostly drum-pattern B variants, sample chops changing at the hook, and scratch or vocal-sample fills on bar 8/16 (convention).

### R&B (65-100)
Sourced shape (HipHopMakers): `Intro-V-H-V-H-Bridge-H-H-Outro`.
Default (convention): Intro 4, V 8-16, Pre 4, H 8, V 8-16, Pre 4, H 8, Bridge 8, H 8, H 8 (ad-libs, extra harmony), Outro 4-8. At 80 BPM with 8-bar verses: 72 bars = 3:36. Verse: sparse drums, keys/pad, bass. Hook: add backing vocals/pad layer, fuller drums. Final double hook: add one layer (octave lead, harmonies) for the second pass.

### Afrobeats (95-115; 108 sweet spot)
Sourced (Audeobox): Intro 4-8, Verse 16, Hook 8, Bridge 8. Default: Intro 8, V 16, H 8, V 16, H 8, Bridge 8, H 8, Outro 8 = 88 bars at 108 = 3:16. Shaker/conga/guitar layers enter and leave every 8 bars; the log or bass groove stays.

### Amapiano (110-115)
Sourced (Beatstorapon): Intro 8-16, Foundation 16, Development 16-32, Breakdown 8-16, Outro 8-16. Long-form, DJ-friendly; log drum is the hook, so its entry or return is the energy event. Default at 112: Intro 16, Foundation 16, Development 32, Breakdown 16, Development 2 32, Outro 16 = 128 bars = 4:34.

### Jersey club (130-145; 140 default)
Sourced (Native Instruments): elements layer in every 8 bars; lead/vocal drops at bar 41 and returns at bar 49; then progressive removal. DJ-friendly 8-bar blocks; for rap versions thin the chops in verses and restore them at hooks.

### Lo-fi (60-90)
Sourced (search summaries of Lunacy Audio, NI): 4-bar loops, elements introduced in 4- or 8-bar phrases with reverse-crash transitions; full beat 64-96 bars.
Default (convention) at 85: Intro 4-8 (keys/sample filtered, vinyl texture), A 16 (drums + bass + keys), B 8-16 (chord change, drum drop-out, added melody), A 16, Outro 4-8. Loop drums and bass, vary the keys. 48-64 bars = 2:15-3:00.

## 4. Pop

Timing data (treat as soft):
- 2025 Billboard Year-End Hot 100 median length 3:13, mean 3:24; share over 3:30 rose from 22% (2019) to 37% (2025) (DEV Community analysis) **(sourced)**. Spotify-charting songs averaged about 3:00 in 2024 (Hypebot) **(sourced)**; the two populations differ.
- First chorus at about 38 s for Hot 100 number-ones 2020-2023 versus 55+ s earlier; ABABCB in 67% of number-one pop hits; hook recurs every 30-45 s. These came through an aggregator and were not verified on the primary reports **(sourced, unverified)**.

Default (convention, 100-125 BPM):

| Section | Bars | At 115 BPM |
|---|---|---|
| Intro | 4 (or cold open on the hook) | 0:00 |
| Verse 1 | 8 | 0:08 |
| Pre-chorus | 8 (4 at faster tempos) | 0:25 |
| Chorus 1 | 8 | 0:42 |
| Post-chorus | 4 (instrumental or chop hook) | 0:58 |
| Verse 2 | 8 (shorter or busier) | 1:07 |
| Pre-chorus | 8 | 1:23 |
| Chorus 2 | 8 | 1:40 |
| Post-chorus | 4 | 1:57 |
| Bridge | 8 (strip down or change harmony) | 2:05 |
| Final chorus | 16 (double chorus; add harmonies, optional key lift) | 2:22 |
| Outro | 4 | 2:55 -> ends 3:04 |

First-chorus rule: bars before chorus 1 = 40 x BPM / 240 (about 19 bars at 115, 20 at 120, 17 at 100). If the template overshoots, cut the intro to 2-4 bars, shorten the pre to 4, or open on the hook.

## 5. Electronic

### EDM / festival (126-150; 128 default)
Sourced (Inspired by Beatz): Intro 16-32, Build 8-16, Drop 16-32, Breakdown 16-32, Outro 16-32; six to eight sections (Intro, Build, Drop, Breakdown, Build 2, Drop 2, Outro); streaming drop within 30-60 s; radio edit 3.5-4 min; club 5-7 min.
Radio default at 128: Intro 16 (0:00), Break/verse 16 (0:30), Build 8 (1:00), Drop 16 (1:15), Breakdown 16 (1:45), Build 8 (2:15), Drop 2 16 (2:30, variation), Outro 16 (3:00) = 112 bars = 3:30. For a 30 s drop: Intro 8, Build 8, Drop at bar 17 (30 s).

### House / tech house / afro house (122-126; DJ extended, convention)

| Section | Bars | Contents |
|---|---|---|
| Intro A | 16 | kick + hats + perc only (DJ mix-in) |
| Intro B | 16 | + clap, + bass (filter opening), hook tease |
| Groove 1 | 32 | full drums + bass + hook; change something every 8 |
| Breakdown | 16 | no kick or bass; chords, vocal, FX; filter sweep |
| Build | 8 | roll, riser, high-pass on music group, 1-beat gap |
| Groove 2 / drop | 32 | full + one new layer (vocal, extra perc) |
| Break 2 (optional) | 8-16 | short tease |
| Groove 3 | 16-32 | variations |
| Outro | 32 | remove musical parts in reverse; drums only for the last 16 |

About 168-200 bars = 5:23-6:24 at 125. Deep house: same blocks, shallower breakdowns, no big risers (it avoids build/release emphasis, Wikipedia) **(sourced)**. Attack Magazine method: start with the kick and add an element every 8-16 bars, subtract toward the end **(sourced)**.

### Techno (125-150; convention)
Intro 32 (kick + hats), Main A 32, Tension 16-32 (remove kick, add rumble or acid filter automation), Main B 32-64, Outro 32. Changes every 8 or 16 bars are mostly filter, send level or a percussion layer. Peak-time adds an 8-16 bar break with a riser and a stab. 6-8 min.

### Trance (132-140; 138)
Sourced: 16/32-beat phrases, builds to 1-2 peaks; long snare rolls rising in velocity; beatless breakdowns exposing a melody or pad (Wikipedia, Orphiq).
Default: Intro 32 (DJ), Main groove 32 (bass + arps), Breakdown 1 16-32 (beatless, pads + lead theme), Build 8-16, Climax 1 32, Mid groove/second breakdown 16-32, Climax 2 32 (optional +1/+2 semitone key lift), Outro 32. Radio edit about 3:00-3:30.

### Drum and bass (170-176; 174)
Sourced: Intro 16, Build 8, Drop 1 32, Breakdown 16, Drop 2 32, Outro 8-16 (Violet Recording); timeline Intro 0:00-0:45, Build 0:45-1:00, Drop 1:00-2:00, Breakdown 2:00-2:30, Drop 2 2:30-3:30, Outro 3:30-4:00 (Beatportal); "a beat of silence right before each drop"; DnB is about the first drop (Mixed In Key).
Default: Intro 32 (drums + filtered bass, DJ), Build 8, Drop 1 32 (switch-up at bar 16 of the drop), Breakdown 16, Build 8, Drop 2 32 (new bass variation / "VIP" switch), Outro 32 = 160 bars = 3:41. 32 bars at 174 = 44 s.

### Dubstep / riddim (140-150, half-time)
Intro 16-32, Build 8 (riser + roll + vocal), Drop 1 16-32 (call-and-response bass in 2/4-bar phrases), Breakdown 16, Build 8, Drop 2 16-32 (new bass sounds; riddim = same motif with switch-ups), Outro 16. Riddim uses silence as an instrument (snippet-level source).

### Future bass (150 half-time; pop form)
Intro 8, Verse 16, Build 8 (twinkly pitch riser, pitched-up chop, kick removed), Drop 16 (pitch-bent supersaw chords, chops), Verse 2 8-16, Build 8, Drop 2 16 (variation), Bridge/outro 8. Song parts typically 4 bars (FeelYourSound) **(sourced)**.

### UK garage / 2-step (130)
Intro 16 (drums), Verse 16, Hook 16 (vocal chop), Break 8, Verse 16, Hook 16, Dub section 16 (bass-led), Outro 16.

### Synthwave (80-118)
Intro 8-16 (pad + arp), V 16, Ch 16, V 16, Ch 16, Solo 16 (sax/guitar/lead), Final Ch 16, Outro 8-16; gated tom fill in the last bar of each 8-bar phrase.

### Hyperpop (2:00-2:45)
Short, maximal sections; abrupt genre or tempo switch-ups; drops into silence; glitch stutters at transitions; a final section that halves tempo or explodes into distortion.

### Ambient / chill
Through-composed: layers enter one at a time and change slowly; 5-20 min. Downtempo uses loose 16-32-bar sections.

## 6. Cinematic three-act cue

Sourced (Violet Recording): Act 1 quiet, Act 2 builds, Act 3 full climax, ending on a button or stinger; "the quiet before a hit matters as much as the hit itself". Toolkit: braam, hit/impact (transient + body + sub), riser, whoosh, sub drop, drone bed.
Default trailer, 2:00-2:30 (convention):

| Act | Time | Contents | Energy |
|---|---|---|---|
| 1 | 0:00-0:40 | sparse piano/strings motif, drone bed, occasional hit | 2-3 |
| 2 | 0:40-1:30 | string ostinato, pulses, percussion, brass swells; step up every 8 bars | 4 -> 7 |
| Gap | 1-2 beats | riser ends, silence | - |
| 3 | 1:30-2:15 | full choir, brass, taiko, braams on downbeats; widest range | 9 |
| Button | last 3-10 s | silence, final hit + sub drop | - |

Non-trailer cues follow picture, not 8-bar blocks; still build by the ostinato method (ostinato -> drone -> melody -> brass/percussion + range -> climax -> single sustained element). Act 3 ostinati often sit at 120-140 BPM.

## 7. Element matrices

Notation: `X` plays, `~` partial/filtered/variant, `-` out, `+` added layer.

### Trap section grid (convention)

| Section (bars) | Kick | 808 | Snare/clap | Hats | Perc | Chords/sample | Lead | Counter | FX |
|---|---|---|---|---|---|---|---|---|---|
| Intro (8) | - | - | - | ~ filtered | - | ~ filtered | ~ | - | riser into hook |
| Hook 1 (8) | X | X | X | X rolls | X | X | X | X | crash on 1 |
| Verse 1 (16) | X | X | X | X simpler | ~ | X | - | ~ fills bars 8/16 | drop-out on bar 16 |
| Hook 2 (8) | X | X | X | X | X | X | X | X | reverse cymbal in |
| Verse 2 (16) | X | X new pattern | X | X variation | X new | X | ~ | X | - |
| Bridge (8) | - | ~ | - | ~ | - | X | X | - | silence + impact |
| Hook 3 (8) | X | X | X | X | X | X | X + octave | X | - |
| Outro (8) | - | - | - | - | - | X fading | ~ | - | downlifter |

Verse rule: rapper takes the lead slot, so lead and counter go out or partial. Hook 3 is the fullest (adds the octave layer). The bridge clears the low end so hook 3 hits.

### EDM

| Section | Kick | Bass | Clap/snare | Hats/perc | Pads/chords | Lead | Vocal/chops | FX |
|---|---|---|---|---|---|---|---|---|
| Intro 16 | X | ~ filtered | ~ from bar 9 | X | - | - | - | sweep last 4 |
| Break/verse 16 | - or ~ | - | - | ~ | X | ~ theme | X | - |
| Build 8 | - (or quarters, removed last 2 bars) | - | roll | ~ | X high-passed | ~ repeating note | X tag | riser + noise + silence |
| Drop 16 | X | X | X | X | X sidechained | X + octave | ~ chops | crash + impact |
| Breakdown 16 | - | - | - | - | X | X exposed | X | reverse crash out |
| Build 8 | as above, faster roll | | | | | | | stronger riser |
| Drop 2 16 | X | X new patch | X | X + layer | X | X + layer | X | crash + impact |
| Outro 16 | X | ~ | X | X | - | - | - | downlifter |

### Pop (convention)
- Verse: lighter drums, bass, one harmony instrument, vocal.
- Pre-chorus: + pad or rhythm layer, rising harmony, drums building (fill or roll in the last bar).
- Chorus: + backing vocals, octave-doubled hook, fuller drums, wider stereo.
- Post-chorus: hook instrument or chop alone over drums.
- Bridge: drop drums or change harmony.
- Final chorus: one more layer than chorus 2 (harmonies, counter-line, key lift optional).

### House (convention)
Kick in every section except the breakdown (and the last build bars); hats from bar 1; clap from bar 17; bass from bar 17 (filter opening to bar 32); hook from bar 25 tease, full at 33; breakdown removes kick and bass; outro removes hook, then bass, then clap, leaving kick + hats + perc for the last 16.

## 8. How to adapt a template

1. Choose by use: rapper beat (hooks/verses, 2:15-3:30), streaming single (first chorus/drop by 30-45 s, 2:45-3:30), club (32-bar DJ intro/outro, 5-7 min), sync/cue (picture-led).
2. Compute every start bar and time; print the bar map.
3. Check the first-peak time; shorten intro/verse/pre if late.
4. Add the matrix; check adjacent sections differ on 2+ axes (`references/energy-builds-transitions.md`).
5. Mirroring a reference track (Attack Magazine "copy it out"): list its sections with bar counts and the entry/exit of each element, then match its decisions with your parts.

## 9. Sources

- Inspired by Beatz, EDM arrangement: https://www.inspiredbybeatz.com/en/edm-arrangement-from-loop-to-exciting-track/
- Wikipedia, Phrasing (DJ): https://en.wikipedia.org/wiki/Phrasing_(DJ)
- Home DJ Studio, EDM song structure: https://homedjstudio.com/edm-song-structure/
- Mixed In Key, arranging dance music: https://mixedinkey.com/?p=5367 ; https://mixedinkey.com/captain-plugins/wiki/how-to-arrange-a-dance-music-track/
- HipHopMakers, beat arrangements: https://hiphopmakers.com/how-to-make-beats-song-arrangements
- Beatstorapon, drill: https://beatstorapon.com/blog/how-to-make-a-drill-beat/ ; amapiano: https://beatstorapon.com/blog/how-to-make-amapiano-beat/
- WA Production, arrangement blueprints (snippet): https://blog.waproduction.com/arrangement-blueprints-10-proven-song-maps-that-just-work
- Audeobox, afrobeats in FL Studio: https://www.audeobox.com/learn/fl-studio/how-to-make-afrobeats-in-fl-studio/
- Native Instruments, jersey club: https://blog.native-instruments.com/jersey-club/ ; lo-fi: https://blog.native-instruments.com/lo-fi-hip-hop/
- Lunacy Audio, lo-fi (search summary): https://lunacy.audio/how-to-make-lofi-music/
- Violet Recording, DnB: https://violetrecording.com/how-to-make-drum-and-bass/ ; trailers: https://violetrecording.com/sound-design-for-trailers/
- Beatportal, DnB timeline: https://www.beatportal.com/articles/818379-step-by-step-guide-to-producing-drum-and-bass-like-sub-focus-a-m-c-and-delta-heavy
- Attack Magazine, 4 ways out of the loop: https://www.attackmagazine.com/technique/tutorials/4-ways-to-break-out-of-the-loop/
- Wikipedia, Trance music; Deep house. Orphiq, trance: https://orphiq.com/resources/what-is-trance-music
- FeelYourSound, future bass: https://feelyoursound.com/articles/future-bass-tutorial/
- Song length: https://dev.to/tonywangca/are-songs-really-getting-shorter-6618-hot-100-hits-1959-2025-4cdg ; https://www.hypebot.com/hypebot/2025/04/songs-are-getting-shorter-and-the-surprising-truth-behind-it.html
- First chorus / ABABCB (aggregated, unverified): https://hitsongsdeconstructed.com/wp-content/uploads/2024/04/The-Taylor-Swift-Evolution-Structure.pdf ; https://djwillgill.com/how-to-write-band-music-in-2026/
