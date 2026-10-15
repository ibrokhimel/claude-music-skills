# Roles, planes, frequency and register slotting, orchestration

Why parts placed together make sense: each owns a role, a plane, a register, a rhythmic density, a timbre and a stereo position, and no two parts share all of them.

## Contents
1. Roles (Owsinski) and the focal-element limit
2. Planes: foreground, middleground, background
3. Instrument frequency table
4. Register map with MIDI numbers and FL labels
5. Slotting rules (register, rhythm, timbre, stereo)
6. Masking: diagnosis and fixes in priority order
7. Orchestration principles for production
8. Texture types
9. Worked example: slotting a trap hook
10. Sources

## 1. Roles and the focal-element limit

Bobby Owsinski's five arrangement elements **(sourced)**:

| Role | What it does | Modern-beat members |
|---|---|---|
| Foundation | rhythmic and harmonic floor | kick, snare/clap, bass/808; rhythm keys/guitar count here if they play the same rhythm as the drums |
| Pad | long sustained notes or chords; glue | pads, sustained keys, strings, held guitar chords, choir |
| Rhythm | plays counter to the foundation; adds motion | hats, shakers, tambourine, congas, strummed or muted guitar, arps |
| Lead | the thing the listener follows | lead vocal, topline, lead synth, main sample/riff |
| Fills | answers in the lead's gaps, or a signature line | call-and-response licks, vocal chops, ear-candy one-shots |

Producer additions (convention): **texture/atmosphere** (vinyl crackle, noise beds, field recordings, reverb tails) always background; **FX/transitions** (risers, impacts, reverse crashes) live only at boundaries.

**Focal limit (sourced):** no more than four elements at once, three often best, five rarely works (Owsinski). The "rule of three" (attributed to producers such as Max Martin and Jack Joseph Puig) says the brain follows about three things; if the riff, the vocal and a cool bassline are all happening, the drums should stay plain. An element is what is heard as one: a stack of drum tracks or several guitars on one rhythm count once.

**Rule (convention):** every new part gets a role and a plane before notes are written. A would-be fifth foreground element must replace one, or be pushed back: lower level, high-passed/low-passed, wider, less active.

Counting focal elements: count lead, any rhythmically independent counter/fill, the foundation as one unit (unless the 808 is melodic and prominent, then it counts separately), and any busy rhythm layer that is loud. Pads and texture normally do not count.

## 2. Planes

| Plane | How it is made | Typical members |
|---|---|---|
| Foreground | louder, most characteristic timbre, centre or prominent position, best register (often the top voice), more rhythmic definition | lead vocal/hook, snare/clap, kick in club music |
| Middleground | moderate level, defined but less bright, some stereo offset | bass/808 (felt more than followed), counter-melody, chord stabs, main hats |
| Background | quieter, filtered, wider, more reverb, less activity | pads, texture, perc layers, ear candy |

Perception supports putting the tune on top: higher voices are encoded better for pitch, lower voices for timing (Hove et al. 2014) **(sourced)**. So the highest prominent voice is heard as the melody and the low parts carry the beat.

Moving a part between planes uses these handles (convention):
- level (2-6 dB is a plane step);
- filtering (high-pass and low-pass to narrow the band);
- reverb send (more = further back);
- stereo (wide = background, centre = foreground);
- activity (fewer notes = less attention);
- register (away from the lead's octave).

## 3. Instrument frequency table

Starting points from iZotope's EQ cheat sheet **(sourced)**. Fundamentals only cover part of a sound; harmonics extend to the top of hearing and carry identity, so read charts cautiously (Audio Masterclass).

| Instrument | Low end | Body | Mud/box | Presence/attack | Air |
|---|---|---|---|---|---|
| Kick | 60-80 Hz | 100-200 Hz | 200-500 Hz | 1-5 kHz click | - |
| Snare | cut < 80 Hz | 150-250 Hz | 300-500 Hz | 2-3.5 kHz | 8 kHz+ |
| Hi-hats | - | - | - | 3-7 kHz | - |
| Toms | 60-120 Hz | - | 250-600 Hz | 0.8-1.5 kHz | - |
| Cymbals | cut < 150 Hz | - | - | 4 kHz | 8-12 kHz |
| Bass | 40-120 Hz | 120-250 Hz | 300-500 Hz | 0.8-1 kHz | - |
| Acoustic guitar | cut < 70 Hz | 200-400 Hz | - | 1.5-2.5 kHz | 8-12 kHz |
| Electric guitar | cut < 100 Hz | 150-300 Hz | 200-300 Hz | 2-5 kHz | - |
| Piano | 20-60 Hz | 60-200 Hz | 200-500 Hz | 2-4 kHz | - |
| Vocals | cut < 100-250 Hz | ~120 Hz fullness | 0.5-1.2 kHz nasal | 5-8 kHz | 10 kHz+ |
| Strings | cut < 100 Hz | - | 200-500 Hz | 1-4 kHz | 10 kHz+ |
| Brass | cut < 150 Hz | - | 500-800 Hz | 1-5 kHz | 5 kHz+ |
| FX/reverb returns | cut < 500 Hz | - | - | 0.8-3 kHz | 7 kHz+ |

Other sourced points: muddy bass usually lives at 150-500 Hz; harsh vocals at 2.5-4 kHz; kick tone is constant while the bass fundamental moves with the notes (Sonarworks); DnB keeps the sub mono and low-passed near 80 Hz and sidechained to the kick (Beatportal). Mix-level EQ moves belong to `music-mix-master`; this table is for choosing who lives where.

Producer translations (convention):
- 808s: fundamental 30-60 Hz, distortion harmonics 100 Hz-1 kHz make it audible on phones.
- Pads: energy 200 Hz-2 kHz; high-pass them at 150-250 Hz when an 808 or bass plays.
- Plucks/bells: attack 2-5 kHz; they cut through a dense mid without needing level.
- Vocal chops: treat as lead or fills depending on prominence; their 1-4 kHz presence competes with the lead vocal, so put chops in the vocal's rests.

## 4. Register map

Derived from f = 440 x 2^((m - 69)/12) **(derived)**. FL label = scientific octave + 1.

| Zone | Fundamentals | MIDI (scientific) | FL label | Occupants |
|---|---|---|---|---|
| Sub | 30-60 Hz | 23-34 (B0-A#1) | B1-A#2 | 808/sub fundamentals, kick body |
| Bass | 60-125 Hz | 35-47 (B1-B2) | B2-B3 | basslines, upper 808 notes, kick punch |
| Low-mid | 130-250 Hz | 48-59 (C3-B3) | C4-B4 | chord roots and 5ths, piano left hand, low male vocal |
| Mid | 260 Hz-1 kHz | 60-83 (C4-B5) | C5-B6 | pads, chords, guitars, vocals, most leads |
| Upper-mid | 1-4 kHz | 84-107 (C6-B7) | C7-B8 | bell tops, plucks, arps; presence harmonics of everything |
| High | 4 kHz+ | above 107 (harmonics, noise) | - | hats, shakers, cymbals, air, noise FX |

Anchor points: MIDI 24 C1 32.7 Hz (FL C2); 28 E1 41.2 Hz (FL E2); 36 C2 65.4 Hz (FL C3); 40 E2 82.4 Hz (FL E3); 48 C3 130.8 Hz (FL C4); 60 C4 261.6 Hz (FL C5); 72 C5 523.3 Hz (FL C6); 84 C6 1046.5 Hz (FL C7); 96 C7 2093 Hz (FL C8).

Default part ranges (convention):

| Part | MIDI range | Scientific | FL label | Note |
|---|---|---|---|---|
| 808 / sub bass | 24-40 | C1-E2 | C2-E3 | keep the root note's fundamental in about 30-80 Hz; details in `music-bass-808` |
| Bass guitar / synth bass | 28-47 | E1-B2 | E2-B3 | |
| Chord roots (low voice) | 36-55 | C2-G3 | C3-G4 | root, 5th or octave only below 48 |
| Pads / chord body | 48-76 | C3-E5 | C4-E6 | close-ish voicing in the middle |
| Keys right hand | 60-84 | C4-C6 | C5-C7 | |
| Lead / topline | 60-84 | C4-C6 | C5-C7 | top or most distinctive voice |
| Bells / plucks / arps | 72-96 | C5-C7 | C6-C8 | thin, bright; doubles the lead an octave up |
| Counter-melody | lead +/- 12 | | | in the lead's rests |

## 5. Slotting rules

Eight rules (convention, consistent with the sources above):

1. **One owner below about 100 Hz** at any moment: 808/sub or bass. The kick interlocks rhythmically (plays in the 808's gaps) or is ducked by sidechain. Strategy choice: `music-bass-808`.
2. **Bass and 808 at roughly MIDI 28-47.**
3. **No chords below MIDI 48** (C3, FL: C4) except root, octave or 5th. Thirds below about MIDI 48 sound muddy because low partials crowd the same critical band (Plomp & Levelt). Voicing algorithm and low-interval limits: `music-chords-voicing`.
4. **Pads and chords mostly at MIDI 48-76.** Wider spacing at the bottom, closer spacing at the top, like the harmonic series.
5. **Lead above the chord bed** at about MIDI 60-84, or, if the bed is high, in a contrasting timbre or register. The lead must be the top or most distinctive voice.
6. **Counter-melody in a different octave, in the lead's rests.** Contrary motion and different note values keep the two separable (`music-melody-hooks`).
7. **Busy needs sustained.** If a part is busy (16th hats, rolling arp, fast vocal flow), neighbours in the same register stay sustained or sparse. Busy + busy only in different registers (hats at 8 kHz + arp at 1 kHz is fine; arp + rapid pluck both at C5 is not).
8. **Shared registers must contrast** in timbre (soft pad vs bright pluck; sine vs saw) or stereo (wide pad vs centred lead).

Rhythmic separation patterns (convention):
- Sustained pad + rhythmic pluck/stab on the same chord: the classic pairing.
- Long bass notes + short chord stabs (future bass, house) or short bass + long chords (trap: 808 follows the kick under a sustained pad).
- Melody moves while chords hold; chords change while melody holds (harmonic rhythm vs melodic rhythm interlock).
- Call and response: lead plays bars 1-2, fill answers in bar 2 beats 3-4 or bars 3-4.
- Vocal present: drop the busiest melodic layer, keep drums and harmony; reinstate it in the vocal's gaps or the hook.

Stereo placement defaults (common practice; no single source stated specifics):

| Centre (mono-ish) | Slightly off-centre (10-30% L/R) | Wide (50-100% or stereo-widened) |
|---|---|---|
| kick, snare/clap, 808/sub, bass, lead vocal, main lead | counter-melody, keys, toms, single perc pieces, hats (often slight offset) | pads, doubled guitars, backing vocals, shakers/perc layers, FX, reverb returns, texture |

Apply in FL with `fl_set_channel_pitch_pan_vol(pan)` or `fl_set_track_pan` (pan -1..1; 0.2 = 20% right). Keep sub content mono: never widen the 808. Panning detail and mono checks: `music-mix-master`.

## 6. Masking: diagnosis and fixes

Masking = one part hides another because both put dominant energy in the same critical band at the same time. It is "a fundamental arranging mistake" when low parts collide, and no plug-in fully fixes it (Sonarworks) **(sourced)**.

Diagnose with the axis check. For any two parts that feel crowded, list: register zone, rhythmic density, timbre class, stereo position, plane. If they match on 4-5 axes they will mask.

Fix in this order (convention):
1. **Move the octave.** Shift the less important part up or down 12 semitones. Cheapest, most effective.
2. **Change the rhythm.** Make one sustained and the other rhythmic, or put one in the other's gaps.
3. **Change the timbre.** Swap a saw pad for a sine/soft pad, or a full piano for a filtered Rhodes.
4. **Move in stereo.** Widen the background part, centre the foreground part.
5. **Push it back a plane.** Lower it, filter it, add reverb, thin its notes.
6. **Cut it** for this section. Use it elsewhere as a B variant.
7. Only then EQ/sidechain (`music-mix-master`).

Common collisions (convention):

| Collision | Fix |
|---|---|
| 808 + bass synth both under 100 Hz | pick one owner; the other goes up an octave or out |
| Kick + 808 on the same step every time | interlock (808 in the kick's gaps) or tune them apart and sidechain; see `music-bass-808` |
| Pad low notes + 808 | high-pass the pad; voice the pad from MIDI 52 up |
| Piano left hand + bass | piano drops its left hand when bass plays |
| Lead + vocal | lead plays only in vocal rests, or moves an octave up as a thin bell |
| Arp + hook in the same octave | arp up an octave and quieter, or hook up an octave |
| Two pads | keep one, or split them by register (low warm + high airy) |
| Snare body + guitar/keys body at 150-250 Hz | thin the keys, or move chords up |

## 7. Orchestration principles for production

**Doubling (sourced: Belkin).** Independent counterpoint everywhere tires the ear; heavy doubling sounds grey. Composers sketch clear leading lines first and most of the time only part of the orchestra plays. Octave doublings can colour a chord; individualising the doubling (small differences in rhythm or ending) makes it feel alive.

Production defaults (convention):
- **Octave-double the hook** in choruses/drops: lead at MIDI 72 plus a layer at 60 (weight) or 84 (shine). Remove it in verses. Repeat hooks get the double, first statements may not.
- **Unison layer:** two synths on the same notes with different timbres (saw + square, pluck + pad), or a vocal double. Thickens without adding a focal element.
- **Do not double the 3rd** in low parts; double roots and 5ths.
- **Never double the 808 with a second sub.** Double it with a mid-range layer (distortion, a reese) only if the arrangement needs a mid-bass voice.

**Voicing chords across instruments (convention).** Spread one chord over several parts rather than giving every part the full chord:

| Part | Takes | Range |
|---|---|---|
| Bass/808 | root (sometimes 5th) | 28-47 |
| Low pad / piano LH | root + 5th or root + 7th | 43-55 |
| Pad body | 3rd, 7th, extensions | 55-72 |
| Keys / pluck top | upper voicing, colour tones (9, 11, 13) | 67-84 |
| Lead | melody, often a chord tone on strong beats | 60-84 |

Example, Cm9 (C Eb G Bb D): 808 C1 (MIDI 24); pad C3 G3 (48, 55); pad body Eb4 Bb4 (63, 70); pluck D5 G5 (74, 79). Every chord tone is present once in the bed and the 3rd (Eb) is not below MIDI 60.

**Crescendo by adding families (sourced: Open Music Theory).** Three ways, combine them:
1. Add families: strings -> winds -> brass -> percussion (production: perc -> pads -> lead layers -> octave doubles -> FX).
2. Widen the total range: add a sub octave and a top octave.
3. Mix sustained notes with shorter figures: 1/8 -> 1/16 -> 1/32 rolls over sustained pads.

**Ostinato layering (sourced: IRPR; film practice).** Start with a quiet ostinato, then add layers, raise dynamics and thicken. An ostinato pairs with drones/pads underneath and a melody floating above; contrast it with the melody by opposing rhythm (busy vs long) or by register/instrument. Production: arp or pluck ostinato in bars 1-8, add pad drone at 9, low strings/808 pulse at 17, melody at 25, percussion and top octave at 33.

## 8. Texture types

| Texture | Definition | Use in beats |
|---|---|---|
| Monophonic | one line alone | intros, drop-outs, the bar before a drop, "sample alone" openings |
| Homophonic (melody + accompaniment) | one melody over a chord bed | most verses and choruses |
| Polyphonic | several independent lines | climaxes, final choruses, only when separated by register and rhythm |
| Antiphonal (call and response) | material passed between groups | lead vs fills, vocal vs chop, drums vs riff |
| Heterophonic | variants of one line together | vocal + loosely doubled synth; lo-fi keys + sample |

Arrangement arc (convention): monophonic intro -> homophonic verse -> homophonic + antiphonal hook -> polyphonic final hook.

## 9. Worked example: slotting a trap hook (C minor, 140 BPM)

| Part | Role | Plane | MIDI range | Density | Stereo |
|---|---|---|---|---|---|
| Kick | foundation | fore | sample at 60 | medium | centre |
| Clap/snare | foundation | fore | sample at 60 | backbeat on beat 3 | centre |
| 808 | foundation, low owner | middle | 24-36 (C1-C2, FL C2-C3) | follows kick, long | centre, mono |
| Hats | rhythm | middle | sample | busy 1/8-1/16 + rolls | 10% R |
| Perc (rim, shaker) | rhythm | back | sample | sparse | 30-50% L/R |
| Dark pad | pad | back | 51-67 (Eb3-G4) | sustained | wide |
| Bell lead | lead | fore | 72-84 (C5-C6, FL C6-C7) | medium, 2-bar motif | centre |
| Counter pluck | fills | middle | 60-72 | in the lead's rests | 25% L |
| Riser / crash | FX | boundary only | - | - | wide |

Focal count: lead, foundation (kick + clap + 808 heard as the beat), hats with rolls = 3; the counter pluck makes 4. Verse removes the bell lead and counter for the vocal, leaving 2 focal elements plus the vocal.

## 10. Sources

- Owsinski, song arrangement elements: https://bobbyowsinskiblog.com/song-arrangement-elements/
- Rule of three (Dave Johnston, Music Factory): https://musicfactory.davejohnston.nz/p/less-is-more-using-the-rule-of-three
- Planes (Andy Brick, Stevens): https://personal.stevens.edu/~abrick/orchestration2/files/HMU398_notes_02.html
- Open Music Theory, Core Principles of Orchestration (texture, spacing, crescendo): https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_(Gotham_et_al.)/10%3A_Orchestration/10.01%3A_Core_Principles_of_Orchestration
- Hove et al. 2014, high voice superiority / low-voice timing: https://pmc.ncbi.nlm.nih.gov/articles/PMC4104866
- iZotope EQ cheat sheet: https://izotope.com/en/learn/eq-cheat-sheet
- Audio Masterclass on instrument frequencies: https://www.audiomasterclass.com/blog/what-frequencies-do-different-instruments-produce
- Sonarworks, kick vs bass: https://www.sonarworks.com/blog/learn/eliminate-competition-between-the-kick-and-bass
- Plomp & Levelt 1965, tonal consonance and critical bandwidth: https://www.math.miami.edu/~armstrong/592sp15/Plomp_Levelt_1965.pdf
- Alan Belkin, Orchestration basic notions pt. 2: https://alanbelkinmusic.com/orchestration-basic-notions-pt-2/
- IRPR glossary, ostinato: https://sounddesign.irpr.agency/glossary/ostinato/
- Beatportal DnB guide (mono sub, sidechain): https://www.beatportal.com/articles/818379-step-by-step-guide-to-producing-drum-and-bass-like-sub-focus-a-m-c-and-delta-heavy
