# Import Bro Shark into Codex

## Quick local install

Download and extract the repository, then run the commands in the root README. Use `py` on Windows or `python3` on macOS/Linux. The installer uses the Python standard library only and validates the PNG dimensions and checksum before writing files.

The installed folder is:

```text
<CODEX_HOME>/pets/bro-shark/
  pet.json
  spritesheet.png
```

`CODEX_HOME` defaults to `~/.codex`. On native Windows this is normally `%USERPROFILE%\.codex`. A WSL CLI normally has a separate Linux home unless you have deliberately configured a shared Codex home.

To use an explicitly chosen Codex directory without changing environment variables or settings:

```text
python3 tools/install.py --codex-home /path/to/your/codex-directory --dry-run
python3 tools/install.py --codex-home /path/to/your/codex-directory
```

On Windows, use `py` and a Windows path instead. The installer refuses to replace an existing different or incomplete `bro-shark` folder. An identical installation is a no-op. Review a conflicting folder yourself or choose another Codex home; there is no destructive force option.

## Manual installation

1. Locate the Codex home used by the app or CLI you want to use.
2. Open its `pets` directory, creating that directory if needed.
3. Check whether `bro-shark` already exists. Preserve it if it does.
4. Copy this repository's entire `pets/bro-shark` folder into that `pets` directory.
5. Confirm that `pet.json` and `spritesheet.png` are next to each other, not inside another nested folder.
6. Refresh the desktop pet picker or restart the interactive CLI, then select Bro Shark.

Use the **nine-row** sheet next to `pet.json`. Renaming the eleven-row master will not convert it to the dimensions the current CLI expects.

## Codex CLI

In an interactive session:

```text
/pets
```

Choose Bro Shark, or select it directly:

```text
/pets bro-shark
```

Turn terminal pets off with `/pets off` if desired. Terminal rendering requires iTerm2 3.6 or later, or a terminal that supports Kitty graphics or Sixel. Pets are unavailable in tmux and Zellij. CLI pets show work status and do not provide a desktop floating overlay. The IDE extension has no pet picker.

## Desktop assisted import

First try the local install followed by **Settings → Pets → Refresh**, if Refresh is available, and choose Bro Shark. The official desktop documentation describes **Create pet** but does not define a universal manual import button or guarantee discovery of this local manifest in every build.

If your build does not discover it:

1. Open **Settings → Pets → Create pet**. This loads the app's bundled `hatch-pet` skill.
2. Give the resulting chat the extracted repository path and this request:

```text
Install the existing Bro Shark artwork from this repository into this desktop app's supported local pet format. Use pets/bro-shark/pet.json and pets/bro-shark/spritesheet.png as the nine-row compatibility bundle. Preserve the artwork, name, and action frames; do not regenerate images. Inspect the currently installed hatch-pet skill and use its supported registration process. Keep existing pets and settings intact. If this build supports the eleven-row format, assets/bro-shark-v2.png also preserves all sixteen look directions. Validate the imported result, then tell me how to select it.
```

3. Review any requested local installation permission.
4. Return to Pets, refresh if offered, and choose Bro Shark.

This assisted route intentionally asks the installed skill to handle the current app's schema rather than assuming that all desktop releases use the CLI format unchanged.

## Other Pets surfaces

The official ChatGPT web documentation describes uploading a transparent 1536×1872 PNG or WebP no larger than 20 MiB. Use `pets/bro-shark/spritesheet.png` for that documented format. Local desktop installation does not automatically sync to the web. The eleven-row master is included for hosts that explicitly accept extended v2 sheets; current public documentation does not establish universal v2 support.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Bro Shark is missing | Confirm the correct `CODEX_HOME`, folder nesting, and that both files were copied. Restart or refresh the picker. |
| Invalid sheet dimensions | Use the nine-row local sheet, not `assets/bro-shark-v2.png`. |
| No animation | Check the host's pet support and reduced-motion setting. Reduced motion can intentionally show a still frame. |
| Unsupported terminal | Use a terminal with the graphics support listed above, outside tmux/Zellij. |
| Installer stops on an existing folder | It preserves existing files. Inspect that folder or choose another home. |

## Sources and limits

- [Official Pets documentation](https://learn.chatgpt.com/docs/pets): desktop controls, CLI selection, platform limits, and documented web upload dimensions.
- [Codex local manifest loader](https://github.com/openai/codex/blob/13ab0b254e7b9ed0ab473d38d978fa100bf417ae/codex-rs/tui/src/pets/model.rs): manifest fields, local `pets/<id>` lookup, safe relative sprite paths, dimensions, and default animations.
- [Codex frame constants](https://github.com/openai/codex/blob/13ab0b254e7b9ed0ab473d38d978fa100bf417ae/codex-rs/tui/src/pets/catalog.rs): 192×208 cells and an 8×9 compatibility grid.
- [Codex home environment variable](https://learn.chatgpt.com/docs/config-file/environment-variables): `CODEX_HOME` and its default.

The format was checked against the pinned OpenAI source above on 2026-10-30. Live playback on every app version and operating system has not been tested.
