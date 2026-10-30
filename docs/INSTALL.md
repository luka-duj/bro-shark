# Import Bro Shark into Codex

## Choose an import route

- [With the Pets plugin](#with-the-pets-plugin): start from a Codex chat with the plugin selected.
- [Through Settings → Mini & pets → Create pet](#through-settings--mini--pets--create-pet): use the app's built-in pet creation chat.
- [Quick local install](#quick-local-install): run the included Python installer for the compatible local bundle.
- [Manual installation](#manual-installation): copy the two local pet files yourself.

All routes reuse the existing Bro Shark artwork. No image generation API key is needed to reuse these files. The app or plugin itself may require sign-in and availability for your account or workspace.

## With the Pets plugin

1. Open Codex and start a chat.
2. Select the **Pets** plugin from the available plugins. If it is not installed or offered, use the [settings route](#through-settings--mini--pets--create-pet).
3. Paste this request:

```text
Import Bro Shark from https://github.com/luka-duj/bro-shark so I can use it as a local pet in this Codex desktop app.

Read the repository's README and docs/INSTALL.md. Reuse the supplied pet.json and sprite sheet in pets/bro-shark. Preserve the name Bro Shark, pixel style, black sunglasses, smiling teeth, swimming fin strokes, and Bro! comic action bubbles. Do not regenerate or redraw the artwork.

Use the pet workflow supported by this app to validate and register the local bundle, or use the included tools/install.py after checking it. Use assets/bro-shark-v2.png only if this app explicitly supports the eleven-row format. Show the existing animation preview. Keep existing pets and settings intact, and let me select Bro Shark myself.

If the plugin's create operation only targets ChatGPT Work/web pets, say so and guide me through Settings → Mini & pets → Create pet for local desktop installation. Do not treat creating a web-only pet as a completed local import.
```

4. Review any installation permission the app requests.
5. After local registration, open **Settings → Mini & pets** (or **Pets**), refresh if offered, and select **Bro Shark**.

Plugin destinations vary by host. Creating a Work/web pet does not automatically install a local desktop pet; use the settings route if the available plugin only supports a web collection. The prompt above makes the intended destination explicit.

If Codex cannot retrieve the repository, download **Code → Download ZIP**, extract it, attach the existing sprite file or provide the extracted folder path, and repeat the request using that path. Access to the existing files is enough; the images do not need to be recreated.

## Through Settings → Mini & pets → Create pet

1. In Codex, open **Settings → Mini & pets → Create pet**. On builds with a different label, look for **Settings → Pets → Create pet**.
2. The app opens its pet creation chat and loads the available built-in pet creation workflow.
3. Paste:

```text
Import the existing Bro Shark pet from https://github.com/luka-duj/bro-shark into this Codex desktop app.

Read docs/INSTALL.md and reuse the existing artwork. Do not generate a new shark or restyle it. Keep the name Bro Shark, pixel-art design, black sunglasses, clearly smiling teeth, swimming animation, and Bro! comic action bubbles.

Use pets/bro-shark/pet.json and pets/bro-shark/spritesheet.png for the nine-row local compatibility format. If this app explicitly supports the eleven-row format, use assets/bro-shark-v2.png to preserve all sixteen additional look directions.

Follow this app's current built-in pet creation workflow to validate and register the existing files. Show the supplied motion preview. Keep my existing pets and settings intact, and tell me how to select Bro Shark when the import is complete.
```

4. If the chat cannot access GitHub, download and extract the repository, give it the local folder path, and ask it to import from there. The creation chat can also be given the appropriate existing sprite file as an attachment.
5. After the task finishes, return to **Mini & pets**, choose **Refresh** if available, and select **Bro Shark**.
6. Use the app's **Show pet** command, or `/pet` where supported, to show the floating companion. Dragging and work-status behavior are controlled by the host app.

The official desktop documentation describes **Create pet** and a bundled `hatch-pet` skill. Menu labels and local registration details can vary by version. Let the currently installed workflow handle the app's format; the repository supplies both supported-size artwork variants rather than assuming that every release accepts the extended sheet.

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

If a manual or Python installation does not appear in the desktop picker, use [Settings → Mini & pets → Create pet](#through-settings--mini--pets--create-pet) above. That route lets the currently installed pet creation workflow handle local registration. The Python installer and direct folder copy remain useful for compatible CLI builds.

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
