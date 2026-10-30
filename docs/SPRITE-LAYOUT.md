# Bro Shark sprite layout

Both exports use 192×208 cells in eight columns. Frame indices in a grid are `row * 8 + column`, with rows and columns counted from zero.

| Row | State | Frames used | Frame indices |
| --- | --- | ---: | --- |
| 0 | idle | 6 | 0–5 |
| 1 | running-right / swimming right | 8 | 8–15 |
| 2 | running-left / swimming left | 8 | 16–23 |
| 3 | waving | 4 | 24–27 |
| 4 | jumping | 5 | 32–36 |
| 5 | failed | 8 | 40–47 |
| 6 | waiting | 6 | 48–53 |
| 7 | running / focused work | 6 | 56–61 |
| 8 | review | 6 | 64–69 |

Unused cells are transparent. The nine-row export is 1536×1872 and contains 57 populated cells plus 15 unused cells. The local manifest uses Codex's default animation tracks, aliases, and timing; it does not replace those with uniform-rate custom tracks.

The extended master adds these two rows:

| Row | Clockwise directions |
| --- | --- |
| 9 | 000°, 022.5°, 045°, 067.5°, 090°, 112.5°, 135°, 157.5° |
| 10 | 180°, 202.5°, 225°, 247.5°, 270°, 292.5°, 315°, 337.5° |

Here 000° means up, 090° right, 180° down, and 270° left in screen coordinates. The extended sheet is 1536×2288 and contains 73 populated cells. The two look rows are not installed into the current nine-row Codex CLI loader.

## Preview timing

The supplied GIF previews use these durations. They demonstrate source motion; each host controls its own playback and state transitions.

| State | Durations in milliseconds |
| --- | --- |
| idle | 280, 110, 110, 140, 140, 320 |
| swimming right / left | 120 per frame; last 220 |
| waving | 140 per frame; last 280 |
| jumping | 140 per frame; last 280 |
| failed | 140 per frame; last 240 |
| waiting | 150 per frame; last 260 |
| working | 120 per frame; last 220 |
| review | 150 per frame; last 280 |

The current CLI source uses a slower calm idle and repeats active tracks before settling back into idle. Keeping the manifest's `animations` field absent preserves that host behavior.
