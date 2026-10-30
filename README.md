# Bro Shark for Codex

Bro Shark is an animated pixel-art pet for Codex with black sunglasses, a toothy grin, swimming fin strokes, and **Bro!** comic action bubbles. This repository includes ready-to-import sprite sheets, animation previews, an installer, and guides for the Pets plugin and the app's Create pet workflow.

![Bro Shark animation](previews/all-states.gif)

## Use directly in Codex

You can ask Codex to import the existing artwork without generating a new shark. Choose either route:

### With the Pets plugin

Open a Codex chat, select the **Pets** plugin if it is available, and paste:

```text
Import Bro Shark from https://github.com/luka-duj/bro-shark so I can use it as a local pet in this Codex desktop app. Read the repository's import guide and reuse its existing artwork. Keep the name Bro Shark, the pixel style, smiling teeth, sunglasses, swimming frames, and Bro! action bubbles. Do not regenerate images. Validate the compatible local bundle in pets/bro-shark and use this app's supported local pet registration or the included installer. Show me the existing motion preview. Keep my current pet selected until I choose Bro Shark. If the plugin only creates ChatGPT Work/web pets, explain that and guide me through Settings → Mini & pets → Create pet instead of creating a web-only pet.
```

Plugin capabilities vary by host. A pet created in a web/Work collection is separate from a locally installed desktop pet. The [full plugin guide](docs/INSTALL.md#with-the-pets-plugin) explains this distinction and the download fallback.

### Through Settings → Mini & pets → Create pet

1. Open **Settings → Mini & pets → Create pet**. Some builds call the section **Pets**.
2. In the creation chat, paste:

```text
Import the existing Bro Shark pet from https://github.com/luka-duj/bro-shark into this Codex desktop app. Reuse the supplied artwork; do not redraw it. Read docs/INSTALL.md. Use pets/bro-shark/pet.json and pets/bro-shark/spritesheet.png for the nine-row local format. If this app explicitly supports the eleven-row format, assets/bro-shark-v2.png also preserves all sixteen look directions. Use the current built-in pet creation workflow to validate and register Bro Shark. Preserve its name, pixel style, shades, smiling teeth, swimming animation, and Bro! action bubbles. Show the supplied preview and leave my existing pets intact.
```

3. When import finishes, return to **Mini & pets**, refresh the picker if offered, and select **Bro Shark**.

If Codex cannot fetch the repository, use **Code → Download ZIP**, extract it, and give the creation chat the extracted folder path. See [the settings guide](docs/INSTALL.md#through-settings--mini--pets--create-pet) for the complete steps.

## Install locally with Python

Download this repository with **Code → Download ZIP**, extract it, and open a terminal in the extracted folder. Python 3.9 or later is needed for the installer; no packages or API key are required.

On Windows:

```powershell
py tools/verify.py
py tools/install.py --dry-run
py tools/install.py
```

On macOS or Linux:

```bash
python3 tools/verify.py
python3 tools/install.py --dry-run
python3 tools/install.py
```

The installer copies only `pet.json` and the compatible sprite sheet into `$CODEX_HOME/pets/bro-shark/`, using `~/.codex` when `CODEX_HOME` is unset. It does not change settings, select a pet, or replace an existing different pet.

In an interactive Codex CLI session, enter:

```text
/pets bro-shark
```

For a desktop app build with Pets, open **Settings → Mini & pets** (or **Pets**), refresh the picker if offered, and select **Bro Shark**. If that build does not discover the local bundle, use the [Create pet route above](#through-settings--mini--pets--create-pet).

See [the full installation guide](docs/INSTALL.md) for manual copying, custom Codex directories, troubleshooting, and supported surfaces.

## Which file should I use?

| File | Use |
| --- | --- |
| [`pets/bro-shark/`](pets/bro-shark/) | Ready-to-install local Codex bundle: manifest plus a 1536×1872 nine-row sprite sheet. |
| [`assets/bro-shark-v2.png`](assets/bro-shark-v2.png) | Original 1536×2288 eleven-row master with all sixteen look directions. For tools that explicitly support this extended format. |
| [`previews/`](previews/) | Action GIFs, a look loop, and pose sheets for review. |

The current OpenAI Codex CLI loader expects the nine-row dimensions. The compatible export contains the original first nine rows **without resampling or redrawing**. All nine action states remain intact. The two additional look rows are preserved in the extended master but are not installed by default.

![Swimming preview](previews/running-right.gif)

## Included behavior

- Calm idle with a visible grin and shades.
- Rightward and leftward swimming with alternating fin strokes.
- Greeting, jump, failure reaction, waiting, working, and review poses.
- Readable **Bro!** speech bubbles during action frames; quiet idle has no bubble.
- Sixteen additional look poses in the extended master.

The host decides which state to play. Codex CLI uses work-status animations; floating movement and dragging belong to desktop interfaces that support them. The files add artwork, not new app controls.

## Validation and provenance

The extended master passed structural validation, the bundled pet quality gate, three independent blind direction reviews, and Pets service preflight. The local Codex export is a lossless crop of those approved action rows and is checked separately for the compatible grid. See [validation notes](docs/VALIDATION.md) and [the layout specification](docs/SPRITE-LAYOUT.md).

Artwork was generated with OpenAI image generation and refined through user review. Checksums and dimensions are recorded in [`assets.json`](assets.json).

## License

[MIT](LICENSE).
