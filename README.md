# Claude Music Skills

Seven [Claude Code skills](https://docs.claude.com/en/docs/claude-code/skills) that teach Claude how to compose, arrange and mix music, especially beats in FL Studio. They're built on a large research pass covering music theory, melody writing, drum programming and groove, bass and 808s, arrangement, mixing, about 40 genres, and the science of why music sounds good.

Every rule is concrete enough to program: MIDI note numbers, 16-step drum grids with FL Studio step-sequencer strings, velocities, BPM, swing, Hz ranges and bar counts. Each number is tagged **(sourced)**, **(convention)** or **(derived)**, so you know which defaults to tune by ear.

## The skills

| Skill | What it does |
|---|---|
| [`music-theory-core`](skills/music-theory-core/SKILL.md) | **Start here.** The hub. It routes the beat-from-scratch workflow to the other six skills. It holds the theory tables (MIDI/FL octave names, Hz, intervals, scales, modes, chords, keys), about 40 genre cards, the "budgets" philosophy, the science of musical beauty, and the FL Studio delivery workflow (a MIDI-file template plus the MCP tools). |
| [`music-chords-voicing`](skills/music-chords-voicing/SKILL.md) | A 25-progression library with voice-led MIDI voicings, plus an emotion-to-progression cheat sheet. Covers low-interval limits, keeping chords above the 808, borrowed and chromatic chords, and comping rhythms by genre. |
| [`music-melody-hooks`](skills/music-melody-hooks/SKILL.md) | Melody shape (one climax), mostly steps with occasional leaps, motif development, phrase templates, an earworm checklist, counter-melodies, genre melody styles and 9 worked examples. |
| [`music-drums-groove`](skills/music-drums-groove/SKILL.md) | What each drum does and how the parts interlock, velocity bands, swing, groove research, hi-hat rolls, fills and builds, and 16-step grids for about 28 genres. |
| [`music-bass-808`](skills/music-bass-808/SKILL.md) | Choosing bass notes, kick/bass strategies, 808 tuning, range, slides and saturation, FL Mono/Porta settings and 15 bassline styles. |
| [`music-arrangement`](skills/music-arrangement/SKILL.md) | Instrument roles and fitting each part into its own frequency range, song-form bar templates by genre, energy curves, build-ups and drops, and a loop-to-song workflow. |
| [`music-mix-master`](skills/music-mix-master/SKILL.md) | Gain staging, EQ lanes, compression and sidechain with FL stock plugins, panning, reverb/delay timing, loudness targets and an FL mixer procedure. |

## Install

Copy the skill folders into your Claude Code skills directory:

```bash
cp -r skills/music-* ~/.claude/skills/
```

They also work in a single project's `.claude/skills/` folder. Claude loads them automatically when you ask for a beat, a melody, chords, a mix, and so on.

## FL Studio integration

The FL delivery sections assume the [`fl-studio-mcp`](https://github.com/alansork/fl-studio-mcp) MCP server. They were written against a locally patched build for **FL Studio 21**, which talks over MIDI SysEx through loopMIDI. On FL 21 the piano-roll tools only queue notes, so pitched parts are delivered as `.mid` files: [`make_midi_template.py`](skills/music-theory-core/references/make_midi_template.py) uses `mido`, and you drag the files onto your channels. Tempo, step-sequencer rows, mixer volume, pan and routing go straight through the MCP tools. Some reference files mention the original author's local paths; replace them with your own.

The theory, melody, drum, bass, arrangement and mixing content works without FL Studio too, in any DAW or with plain MIDI.

## Research

- [`research/report.md`](research/report.md): the full synthesized report (about 19,500 words) with source links throughout.
- [`research/notes/`](research/notes/): the nine raw research note files the report and skills were built from.
- [`research/genres/report.md`](research/genres/report.md): a second report (about 27,000 words) that turns roughly 150 world genres into programmable parameter recipes: rock, metal, jazz and blues, soul/funk/gospel/disco, country and folk, Latin, Caribbean, African, Asian, Middle Eastern, classical, film, game and experimental.
- [`research/genres/notes/`](research/genres/notes/): the ten raw genre research note files behind it.

Main findings from the research:
- **Beauty works like a budget.** Use one surprise inside a predictable context (Cheung et al., 2019). Keep syncopation medium and the kick/snare anchors steady (Witek et al., 2014). Let 3–4 parts lead at once, with one part owning the sub.
- **Genres are mostly parameter settings over the same theory:** tempo, where the snare lands, swing, which part owns the sub, chord vocabulary and section lengths.
- **The theory layer is exact; the genre layer is convention.** Check grids and swing values against a reference track and by ear.
