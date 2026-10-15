# Progression library: 25 loops spelled with voice-led MIDI voicings

Each entry gives Roman numerals, a concrete key, a voice-led voicing in MIDI numbers, its emotional character, and the genres and songs that use it. Every voicing here was checked by script for three things: correct chord tones, the approximate low-interval limits, and no parallel perfect 5ths or octaves between the bass and the top voice. The one exception is the brass fanfare in #25, which is labelled as deliberate planing.

## Contents
- How to read and transpose an entry
- What the data says (Hooktheory, Cheung 2019)
- Major-key loops (1–6)
- Jazz, R&B, lo-fi and neo-soul loops (7–17)
- Minor-key loops: pop, EDM, trap, drill, cinematic (18–25)
- Sources

## How to read and transpose an entry

- Format: `Chord bass | upper voices`, with C4 = 60 (FL Studio shows MIDI 60 as "C5").
- **bass** is the keys' left hand or the bass instrument, in MIDI 36–52 (C2–E3, FL: C3–E4).
- When an **808 owns the sub**, drop the left-hand bass note. The 808 plays the same pitch class in its own range, roughly MIDI 24–40 (see `music-bass-808`). The upper voices stay as written: all of them sit at MIDI 51 or above, which respects the floor of about MIDI 48.
- **Motion** is the total number of semitones the upper voices move per change. Lower means smoother. Under 6 is the target.
- **Transposing:** add the same number of semitones to every note. Afterwards:
  - if the lowest upper voice falls below 52 (or 48 under an 808), or the top voice rises above about 79, move the upper voices by ±12 or re-run the nearest-voicing algorithm;
  - re-check the low-interval limits, because transposing down can push a 3rd or 2nd into mud.
- **(k)** marks a song example from general knowledge rather than a fetched source. The progression family is right, but check the exact chords before quoting them to the user.

## What the data says

| Finding | Evidence |
|---|---|
| In about 1,300 popular-song sections, C major and A minor were by far the most common keys. This is partly an artefact of transcribing songs into C. Bb was about 4%. | **(sourced)** Hooktheory blog |
| IV and V appear in more progressions than I, so sections often leave out the tonic. | **(sourced)** Hooktheory blog |
| After iii, the next chord was vi or IV about 93% of the time. | **(sourced)** Hooktheory blog |
| Across about 80,000 Billboard chords, pleasure peaked for two combinations: a surprising chord in a predictable context, and a predictable chord after an uncertain context. | **(sourced)** Cheung et al. 2019, *Current Biology* |
| I–V–vi–IV and its rotations are everywhere in pop. The Axis of Awesome's "Four Chords" medley (2008) strings dozens of songs together on it. | **(sourced)** Wikipedia: I–V–vi–IV |
| No corpus gives chord statistics for trap, drill or EDM specifically. Genre progressions below come from producer guides. | gap |

What to do with this: a loop that avoids I is normal, not wrong. Follow iii with vi or IV. Spend chromatic chords only where the context is predictable (see `color-devices.md`).

---

## Major-key loops

### 1. I–V–vi–IV, the "Axis" (C major)
- Triads, top voice C–B–C–C: `C 48 | 64 67 72` → `G 43 | 62 67 71` → `Am 45 | 64 69 72` → `F 41 | 65 69 72`. Motion: 3, 5, 1, 3.
- Expensive version, with E held on top: `Cadd9 48 | 55 60 62 64` → `G6 43 | 55 59 62 64` → `Am7 45 | 55 57 60 64` → `Fmaj9 41 | 55 57 60 64`. Motion: 1, 4, 0, 5.
- Character: uplifting, communal, "everyone knows it".
- Uses: pop, EDM, future bass, country, stadium rock. Songs: Beatles "Let It Be", U2 "With or Without You", Adele "Someone Like You", Journey "Don't Stop Believin'" (k).
- Rotations:
  - IV–I–V–vi (F–C–G–Am) starts lifted. Examples are Rihanna "Umbrella" and Jay Sean "Down" **(sourced)**.
  - I–V–ii–IV is a brighter variant. Examples are "All Star" and "Closing Time" **(sourced)**.

### 2. vi–IV–I–V, the "emotional pop" rotation (A minor feel, C major)
- `Am9 45 | 55 59 60 64` → `Fmaj9 41 | 55 57 60 64` → `Cmaj9 48 | 55 59 62 64` → `G6 43 | 55 59 62 64`. Motion: 2, 4, 0, 2.
- Cmaj9 to G6 changes only the bass: the upper shape G–B–D–E stays put, and the bass decides the chord name.
- Character: melancholic but hopeful, like nostalgia with a lift.
- Uses: emotional pop, EDM and rap hooks, future bass. Songs: Cranberries "Zombie", Avicii "Wake Me Up" verse, "Despacito" (k).

### 3. I–vi–IV–V, the "doo-wop" loop (G major)
- `G 43 | 59 62 67` → `Em 40 | 59 64 67` → `C 48 | 60 64 67` → `D 38 | 57 62 66`. Motion: 2, 1, 6, 3.
- Character: innocent, retro, sweet. The V at the end drives the loop round.
- Uses: 50s pop, soul, ballads, retro R&B. Songs: Ben E. King "Stand By Me", The Police "Every Breath You Take" (k).

### 4. Pachelbel's Canon: I–V/3–vi–iii/5–IV–I/3–IV–V (D major)
- `D 50 | 57 62 66` → `A/C# 49 | 57 61 64` → `Bm 47 | 59 62 66` → `F#m/A 45 | 57 61 66` → `G 43 | 59 62 67` → `D/F# 42 | 57 62 69` → `G 43 | 59 62 67` → `A 45 | 57 61 64`. Motion: 3 to 6 per change.
- The bass walks down by step (D, C#, B, A, G, F#), and the inversions are what make it "expensive".
- Character: graceful, inevitable, wedding-warm.
- Uses: ballads, pop-punk, film. Songs: Pachelbel "Canon in D", Maroon 5 "Memories", Green Day "Basket Case" (k).

### 5. I–bVII–IV–I, Mixolydian rock/gospel (G major)
- `G 43 | 59 62 67` → `F 41 | 60 65 69` → `C 48 | 60 64 67` → back to G. Motion: 6, 3, 3.
- Character: swaggering, open, anthemic. The bVII is borrowed from the parallel minor (or comes from Mixolydian).
- Uses: rock, gospel vamps, country, pop-rock bridges. Songs: Lynyrd Skynyrd "Sweet Home Alabama" (I–bVII–IV), the coda of Beatles "Hey Jude" (k).

### 6. I–III–IV–iv, chromatic mediant plus borrowed iv (G major)
- `G 43 | 55 59 62` → `B 47 | 54 59 63` → `C 48 | 55 60 64` → `Cm 48 | 55 60 63`. Motion: 2, 3, 1, 2.
- B major is a chromatic mediant: its D# is the secondary leading tone into E. The Cm's E→Eb is the "tear".
- Character: wistful, aching, bittersweet.
- Uses: alt-rock, indie, emotional pop. Songs: Radiohead "Creep" (k).

---

## Jazz, R&B, lo-fi and neo-soul loops

### 7. ii–V–I with extensions (C major)
- `Dm9 38 | 53 57 60 64` → `G13 43 | 53 57 59 64` → `Cmaj9 36 | 52 55 59 62`. Motion: 1, 5. The loop back to Dm9 is 6.
- These are rootless A-form voicings: the guide tones fall by semitone (C→B, then F→E).
- Character: warm, resolved, sophisticated.
- Uses: lo-fi (cited as its most common progression), neo-soul, jazz, liquid DnB, amapiano. Songs: "Autumn Leaves", "Fly Me to the Moon" (k).

### 8. Minor ii–V–i (C minor)
- `Dm7b5 38 | 53 56 60` → `G7b9 43 | 53 56 59` → `Cm9 36 | 51 55 58 62`. Motion: 1, 4.
- The b9 (Ab) and the 3rd (B) of G7b9 resolve to G and C of Cm9.
- Character: dark elegance, noir.
- Uses: jazz, noir lo-fi, neo-soul, cinematic. Songs: the minor sections of "Autumn Leaves", "Blue Bossa" (k).

### 9. I–VI7–ii–V turnaround (C major)
- `Cmaj7 48 | 55 59 60 64` → `A7 45 | 55 57 61 64` → `Dm9 38 | 53 57 60 64` → `G13 43 | 53 57 59 64`. Motion: 3, 3, 1, 5.
- A7 is the secondary dominant V/ii: its C# leads up to D.
- Character: cycling, classy, "round the block again".
- Uses: lo-fi turnaround **(sourced, Audeobox)**, jazz, gospel, R&B. Songs: the A section of "I Got Rhythm" ("rhythm changes") (k).

### 10. IVmaj7–III7–vi7–v7–I7, the "Just the Two of Us" loop (C major, in a minor frame)
- `Fmaj9 41 | 55 57 60 64` → `E7 40 | 56 59 62 64` → `Am9 45 | 55 59 60 64` → `Gm9 43 | 55 57 58 65` → `C13 36 | 55 57 58 64`. Motion: 5, 3, 5, 1, 2.
- E7 is V/vi. Gm9 to C13 is a ii–V into F, so the loop tonicises IV.
- Character: sultry, urban, late-night city.
- Uses: R&B, neo-soul, city pop, J-pop, lo-fi. Songs: Grover Washington Jr. & Bill Withers "Just the Two of Us". In Japan it is called the "marusa" progression (k).

### 11. Royal road: IVmaj7–V7–iii7–vi (C major)
- `Fmaj9 41 | 55 57 60 64` → `G13 43 | 53 57 59 64` → `Em11 40 | 55 57 59 62` → `Am9 45 | 55 59 60 64`. Motion: 3, 4, 5, 2.
- Character: bittersweet, nostalgic, "anime ending". Producer Seiji Kameda called the major-V to minor-iii move playful heartbreak **(sourced)**.
- Uses: J-pop and anime **(sourced)**, future bass, kawaii and melodic EDM. Rachmaninoff's Symphony No. 2 uses IV–V7–iii–vi–ii7–V7–I **(sourced)**.

### 12. IV–iii–vi, no tonic (C major)
- `Fmaj7 41 | 53 57 60 64` → `Em7 40 | 55 59 62 64` → `Am7 45 | 55 57 60 64`. Motion: 6, 4, 2. E stays on top throughout.
- Character: floating and unresolved, because I never arrives.
- Uses: lo-fi **(sourced, Native Instruments)**, bedroom pop, R&B intros.

### 13. I–vi, two-chord float (C major)
- `Cmaj9 48 | 52 55 59 62` → `Am9 45 | 52 55 59 60`. Motion: 2. Only D→C moves.
- Character: endless, dreamy, hazy.
- Uses: lo-fi **(sourced)**, chillhop, ambient R&B. Lengthen it to I–vi–ii–V for more motion.

### 14. Dorian vamp: i9–IV9 (A Dorian)
- `Am9 45 | 55 59 60 64` → `D9 38 | 54 57 60 64`. Motion: 3.
- D9's F# is the Dorian major 6th: the one note that makes the mode audible.
- Character: cool, hopeful minor, groovy.
- Uses: neo-soul, funk, deep house, lo-fi, Latin rock. Songs: Santana "Oye Como Va" (Am7–D9); Daft Punk "Get Lucky" (Bm–D–F#m–E, where E is the Dorian IV) (k).

### 15. Backdoor: I–iv7–bVII7–I (C major)
- `Cmaj7 48 | 55 59 64` → `Fm7 41 | 56 60 63` → `Bb7 46 | 56 62 65` → back to Cmaj7. Motion: 3, 4, 5.
- Character: soulful, a soft landing. It is a jazz alternative to ii–V–I **(sourced)**.
- Uses: gospel, R&B, soul, neo-soul endings.

### 16. Gospel walk-up: I–I7/3–IV–#iv°7–I/5–VI7–ii–V (C major)
- `Cmaj9 48 | 55 59 62 64` → `C7/E 52 | 55 58 60 64` → `Fmaj7 41 | 53 57 60 64` → `F#dim7 42 | 54 57 60 63` → `C/G 43 | 52 55 60 64` → `A7 45 | 55 57 61 64` → `Dm9 38 | 53 57 60 64` → `G13 43 | 53 59 62 64`. Two chords per bar; motion 2 to 6 per change.
- The bass walks C–E–F–F#–G–A–D–G, chromatically through F#.
- Character: church warmth, a "testify" feel.
- Uses: gospel, R&B, neo-soul, worship, smooth hip hop.

### 17. Deep-house minor-9 stab chain (A minor)
- Voice-led: `Am9 45 | 60 64 67 71` → `Dm9 50 | 60 64 65 69`. Motion: 4.
- Parallel "chord memory": the same shape moved up a 4th, `Am9 45 | 60 64 67 71` → `Dm9 50 | 65 69 72 76`. Parallel motion is the genre's sound here, so the parallel-5ths rule is waived.
- Rootless trick: the upper notes of Am9 (C E G B) are a Cmaj7 shape, and the bass A turns them into Am9.
- Character: hypnotic, soulful, dusty.
- Uses: deep house, UK garage, Detroit techno **(sourced, MusicRadar summary)**. Artists: Kerri Chandler, Larry Heard (k).

---

## Minor-key loops

### 18. i–VI–III–VII, epic minor (A minor)
- `Am 45 | 64 69 72` → `F 41 | 65 69 72` → `C 48 | 64 67 72` → `G 43 | 62 67 71`. Motion: 1, 3, 3, 5.
- Aeolian variant i–VII–VI–VII, which runs on in synthwave and trance: `Am 45 | 57 60 64` → `G 43 | 59 62 67` → `F 41 | 60 65 69` → `G 43 | 59 62 67`. Motion: 7, 6, 6, 7, with the top voice moving against the bass.
- Character: yearning, anthemic, epic. It is the Axis loop with the minor chord as home.
- Uses: trance (Am–F–C–G **(sourced, Orphiq)**), synthwave, minor pop, trap melodies, trailers. Songs: Linkin Park "Numb", Lady Gaga "Poker Face" (k).

### 19. Andalusian cadence: i–bVII–bVI–V (A minor)
- `Am 45 | 60 64 69` → `G 43 | 62 67 71` → `F 41 | 60 65 69` → `E 40 | 59 64 68`. Motion: 7, 6, 3, 2.
- The top voice runs A–B–A–G#–A against the falling bass. E major's G# comes from harmonic minor.
- 808 version: the 808 slides down the tetrachord A–G–F–E (pitch classes; octave and slides in `music-bass-808`).
- Character: fateful, Spanish, dramatic.
- Uses: flamenco, surf, trap, drill, film. Songs: "Hit the Road Jack" (k); "Stray Cat Strut" and "Happy Together" **(sourced)**. Its roots go back to the Renaissance **(sourced)**.

### 20. i–iv–V7, harmonic-minor drama (A minor)
- `Am 45 | 57 60 64` → `Dm 38 | 57 62 65` → `E7 40 | 56 62 64`. Motion: 3, 2, 3.
- In E7, the tritone G#–D collapses inward onto A–C.
- Character: serious, old-world, a tragic pull home.
- Uses: classical, tango, trap and drill bells, cinematic. Use it when the loop *should* resolve.

### 21. Trap i–VI–v (F minor), with the i–v–iv variant
- `Fm 41 | 56 60 65` → `Db 37 | 56 61 65` → `Cm 36 | 55 60 63`. Motion: 1, 4, 3.
- i–v–iv: `Fm 41 | 56 60 65` → `Cm 36 | 55 60 63` → `Bbm 46 | 58 61 65`. Motion: 3, 6, 3.
- The major VI gives a lift before the minor v sinks back. F minor puts the 808 tonic at F1 (MIDI 29), in the sub sweet spot.
- Character: dark, with a flash of light.
- Uses: trap, plugg, emo rap **(sourced, eMastered)**. The article ties this family to Future's "Mask Off"; that is a blog claim, not verified.
- Colour: play the chords as m(add9) on bells, for example `Fm(add9) 41 | 56 60 67 72` (the 9 is on top).

### 22. Drill loops (G minor)
- i–v–VI: `Gm 43 | 55 58 62` → `Dm 38 | 53 57 62` → `Ebmaj7 39 | 55 58 62`. Motion: 3, 3, 0. Ebmaj7's upper notes are the Gm triad, so only the bass moves.
- i–VII–VI: `Gm 43 | 58 62 67` → `F 41 | 60 65 69` → `Eb 39 | 58 63 67`. Motion: 7, 6, 1.
- i–iv–VII–III: `Gm 43 | 58 62 67` → `Cm 48 | 60 63 67` → `F 41 | 57 60 65` → `Bb 46 | 58 62 65`. Motion: 3, 8, 3, 2.
- Menace swaps: replace v with harmonic-minor `D 38 | 54 57 62` (F#), or stab `F#dim 42 | 54 57 60` before i.
- Character: tense, circular, cold. The language is narrow on purpose: tension instead of resolution **(sourced, Orphiq summary)**.
- Uses: UK and NY drill **(sourced)**. In NY drill the sliding 808 carries most of the harmony.

### 23. Phrygian i–bII over a tonic pedal (A Phrygian)
- `Am 45 | 57 60 64` → `Bb/A 45 | 58 62 65`. Motion: 4. The bass (or the 808) holds A while Bb major grinds a semitone above it.
- Phrygian-dominant colour: `A 45 | 57 61 64` → `Bb/A 45 | 58 62 65`.
- Character: menace, threat, "villain enters".
- Uses: trap, drill, horror, metal, Middle-Eastern-flavoured leads. A bolero-style bII ostinato appears in Jefferson Airplane "White Rabbit" (k).

### 24. 12-bar blues, quick change (C), guide-tone shells
- Bars: `C7 F7 C7 C7 | F7 F7 C7 C7 | G7 F7 C7 G7`.
- Shells: `C7 48 | 58 64` → `F7 41 | 57 63` → `G7 43 | 59 65`. The 3rds and 7ths move by semitone (E→Eb, Bb→A).
- Character: earthy, funky, conversational.
- Uses: blues, boom bap samples, funk, soul **(sourced form, Wikipedia)**. Songs: Chuck Berry "Johnny B. Goode" (k).

### 25. Heroic i–bVI–bVII–i, with a "Mario" major finish (C minor)
- `Cm 48 | 55 60 63` → `Ab 44 | 56 60 63` → `Bb 46 | 53 58 62` → `Cm`. Motion: 1, 6, 5.
- For the triumphant ending, finish on C major instead (a Picardy/Mario cadence): `Ab 44 | 56 60 63` → `Bb 46 | 53 58 62` → `C 48 | 55 60 64`.
- Brass-fanfare version, with deliberate parallel triads: `Ab 44 | 60 63 68` → `Bb 46 | 62 65 70` → `C 48 | 64 67 72`.
- Character: heroic, cinematic, victorious.
- Uses: trailers, game music (the Super Mario Bros. level-clear fanfare (k)), synthwave, epic trap, EDM build payoffs.

---

## Sources
- Hooktheory, "I analyzed the chords of 1300 popular songs": https://www.hooktheory.com/blog/i-analyzed-the-chords-of-1300-popular-songs-for-patterns-this-is-what-i-found/
- Cheung et al. (2019), *Current Biology*, "Uncertainty and surprise jointly predict musical pleasure".
- Wikipedia: I–V–vi–IV progression; Andalusian cadence; Royal road progression; Twelve-bar blues; Backdoor progression; Secondary chord.
- Native Instruments, lo-fi chord progressions: https://blog.native-instruments.com/lo-fi-chord-progressions/
- Audeobox, lo-fi in FL Studio: https://www.audeobox.com/learn/fl-studio/how-to-make-lofi-beats-in-fl-studio/
- eMastered, trap and lo-fi chord progressions: https://emastered.com/blog/trap-chord-progressions
- Orphiq, drill chords (via search summary): https://orphiq.com/resources/drill-chords
- MusicRadar, deep-house minor-9th chords (via search summary).
