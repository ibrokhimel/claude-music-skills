# Mastering and loudness - deep reference

Platform targets, why loudness does not win, the FL stock master chain with starting settings (Parametric EQ 2, Fruity Limiter, Maximus, Soundgoodizer, Soft Clipper), and the mastering procedure for beats.

## Contents
1. Platform targets
2. Loudness and preference: what the research says
3. Preparing the mix for mastering
4. Master chain (FL stock)
5. Plugin starting settings
6. Procedure to hit a target
7. Delivery and export notes
8. Sources

## 1. Platform targets

| Destination | Integrated loudness | True peak | Notes | Evidence |
|---|---|---|---|---|
| Spotify | −14 LUFS | < −1 dBTP; < −2 dBTP if master is louder than −14 LUFS | turns loud masters down; raises quiet ones only within headroom (e.g. a −20 LUFS track at −5 dBTP is raised only to −16) | sourced |
| YouTube | −14 LUFS | < −1 dBTP | turns loud down, does not raise quiet | sourced |
| Apple Music (Sound Check) | −16 LUFS | < −1 dBTP | | sourced |
| TIDAL | album normalization, loudest track at −14 | | | sourced |
| AES TD1008 (2021) | music −16, speech −18, mixed −17 LUFS | ≤ −1 dBTP | distribution recommendation | sourced |
| Competitive hip-hop / beat lease | −8 to −10 LUFS | ≤ −1 dBTP | normalization will turn it down on streaming | sourced (Violet Recording) |
| Amazon Music, SoundCloud | unconfirmed | | do not quote numbers | gap |

Choosing (convention): streaming release → −14 LUFS, ≤ −1 dBTP. Beat lease/YouTube type-beat where artists compare loudness → −9 to −10 LUFS, ≤ −1 dBTP (−2 dBTP is safer for lossy encodes). Always ask which the user wants; default to −14 if unknown.

## 2. Loudness and preference: what the research says

- Vickers (2010, AES 129th Convention; J. AES 2011) reviewed the loudness war: loudness does not correlate with sales, has little effect on preference between songs, and listeners tend to dislike the side effects of hypercompression and prefer more dynamic music; also discusses listening fatigue (sourced).
- Direct evidence is mixed: an Aalborg study found no effect of compression on preference; a Goldsmiths study found heavier compression lowered quality judgements (sourced).
- Chill/peak moments align with loudness increases and section entries, especially in the ~1–4.5 kHz band (Nagel/Grewe group, 2008) (sourced). A master that is already maxed has no room to climax.
- Louder always sounds better in A/B, so compare any decision at matched loudness (standard practice).
- Platforms normalize, so a slammed master is turned down and keeps only its side effects (widely reported).

Rule: moderate compression is fine; never let limiting erase section-to-section contrast. Check that the hook/drop measures louder (short-term LUFS) than the verse after mastering - aim for at least 2–3 LU difference (convention).

## 3. Preparing the mix for mastering

- Master track peaks about −6 dBFS with no master-bus processing (sourced: Studio 11). One author suggests the mix around −20 LUFS integrated (iZotope, single-author preference).
- Low end under control: 808 note levels even (a 6 dB spread pumps the limiter - sourced), sub mono.
- No clipping anywhere; remove "mix-time" master plugins (Soundgoodizer, limiters) before judging.
- Bounce a reference: if mastering in the same project, put the chain on the Master insert; if mastering separately, export the mix as 24-bit or 32-bit float WAV at the project sample rate and master it in a new project.

## 4. Master chain (FL stock)

Order (convention):

1. **Fruity Parametric EQ 2** (optional, gentle): broad moves of 0.5–1.5 dB only.
2. **Glue compression**: Fruity Limiter COMP (or Maximus master band) at 1.5–2:1 for 1–2 dB GR.
3. **Optional Fruity Soft Clipper**: shave 1–2 dB of peaks before the limiter (convention).
4. **Limiter**: Fruity Limiter LIMIT mode or Maximus, ceiling −1.0 to −1.5 dB. Fruity Limiter is not a true-peak limiter, so leave the margin (inter-sample peaks can exceed the sample-peak ceiling).
5. **Loudness meter** last (Youlean Loudness Meter, free VST; verify any native FL LUFS display before relying on it).

Avoid: reverb on the master (sourced: Image-Line), stereo wideners that widen the lows, Soundgoodizer at high amounts as the only "mastering".

## 5. Plugin starting settings

All values are starting points (convention) unless marked. Thresholds are always "lower until GR shows X dB".

**Fruity Parametric EQ 2 (master)**
```
Band 1: High Pass 25-30 Hz, 12-24 dB/oct   (rumble only, keep the 808 fundamental)
Band 3: Peaking 250-400 Hz, -1 dB, Q 1      (only if muddy)
Band 7: High Shelf 10-12 kHz, +0.5 to +1 dB (only if dull)
```

**Fruity Limiter COMP (glue)**
```
RATIO 1.5-2:1, KNEE soft, ATT 10-30 ms (or 0 ms if PDC is off - manual), REL 100-300 ms, THRES until 1-2 dB GR, GAIN = makeup to match bypass loudness
```

**Fruity Limiter LIMIT (final)** - LIMIT mode is a very high ratio (>10:1) capping output, used for mastering (sourced)
```
CEIL -1.0 dB (-1.5 dB if the master is louder than -10 LUFS), ATT 0 ms, REL 100-300 ms (too short distorts - manual), SAT 0, GAIN raised until the meter reads the target LUFS
```

**Maximus** (sourced: three bands Low/Mid/High plus master; includes compressor, limiter, gate, expander, ducker, de-esser; intended as the last effect on the Master; the manual warns against over-compression)
- Start from a gentle preset or with bands at unity; use the master band for limiting, ceiling −1.0 dB.
- Low band: narrow stereo separation toward mono to keep lows centered; light per-band SAT only if the 808 needs presence.
- Keep per-band GR to 1–3 dB; if a band works harder, fix it in the mix.
- Exact knob names and preset list were not verified for FL 21 - describe intent and let the user find the control.

**Soundgoodizer** (sourced: built on the Maximus engine; four presets A–D and one amount knob that works like Maximus's LMH mix)
- Quick "louder/brighter" tool; easy to overdo. If the user wants it: preset A or B at 15–30% amount on the master at the very end, then re-check the true-peak ceiling (convention). Never during mixing. Prefer explicit Limiter/Maximus settings when control matters.

**Fruity Soft Clipper (master, optional)**
- Raise input until 1–2 dB of peaks are rounded; match output; A/B at equal loudness (convention, no primary source).

## 6. Procedure to hit a target

1. Confirm the target (−14 LUFS streaming or −8 to −10 beat lease) and the ceiling (−1 dBTP; −2 for loud masters on Spotify).
2. Loop the whole song (not just the drop) and play it through once with the meter reset: integrated LUFS needs the full length.
3. Raise the limiter input gain in 1 dB steps until integrated loudness reaches the target. If GR on the drop exceeds about 4–6 dB before the target is reached, stop: reduce peaks earlier (drum-bus clipping, 808 level evening, transient control) rather than pushing the limiter (convention).
4. Check short-term LUFS of verse vs hook: the hook should stay louder (≥ 2–3 LU, convention).
5. Check true peak with the meter; lower the ceiling if it exceeds the limit.
6. A/B mastered vs unmastered at matched loudness. If the mastered version sounds smaller, back off.
7. Check on phone/laptop speakers, earbuds and a car or club system if available.

## 7. Delivery and export notes

- Export WAV 24-bit at the project sample rate for distribution; add dither only when reducing bit depth (FL's export dialog handles it). MP3 for previews at 320 kbps (convention).
- Leave the tail: export with "leave remainder" so reverb/delay tails are not cut (FL option; verify in the user's build).
- Loudness and true peak are measured on the final file; re-measure after export if possible.
- Beat-lease bundles commonly include: mastered WAV, untagged MP3, and track-outs (stems) printed pre-master at the same fader settings (convention).

## 8. Sources

- Spotify for Artists, loudness normalization: https://support.spotify.com/artists/article/loudness-normalization/
- Production Advice, AES TD1008: https://productionadvice.co.uk/td1008/
- Production Expert, AES update: https://www.production-expert.com/production-expert-1/aes-update-loudness-recommendations-for-audio-only-streaming
- Production Expert, Apple chooses −16 LUFS: https://www.production-expert.com/production-expert-1/apple-choose-16lufs-loudness-level-for-apple-music-heres-why?format=amp
- Meterplugs, Apple switch to LUFS: https://www.meterplugs.com/blog/2022/03/23/apple-switch-to-lufs.html
- Mastering The Mix, mastering for streaming: https://masteringthemix.com/blogs/learn/76296773-mastering-audio-for-soundcloud-itunes-spotify-and-youtube
- Violet Recording, how to master hip hop: https://violetrecording.com/how-to-master-hip-hop/
- Studio 11 Chicago, −6 dB: https://mastering.studio11chicago.com/mastering-6db/
- Vickers 2010, The Loudness War (AES e-library): https://aes2.org/publications/elibrary-page/?id=15598 ; CDM summary: https://cdm.link/from-the-trenches-of-the-loudness-wars-a-broad-survey-of-research/
- Aalborg compression preference study: https://vbn.aau.dk/da/publications/perceptual-effects-of-dynamic-range-compression-in-popular-music-
- Goldsmiths SysMus14: https://bjmh.gold.ac.uk/index.php/sysmus14/article/view/236
- Nagel et al. 2008 chills psychoacoustics: https://jyx.jyu.fi/handle/123456789/19439?show=full
- Image-Line manuals: Maximus, Soundgoodizer, Fruity Limiter, Fruity Reeverb 2 (https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/)
