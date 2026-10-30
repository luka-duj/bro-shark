# Validation record

## Extended master

The selected 1536×2288 transparent PNG passed:

- The creation pipeline's structural atlas validation.
- Its unmodified final quality gate, including jump lift, registration, scale, and direction evidence.
- Three independent blind direction reviews and the combined majority check.
- The Pets service preflight for the exact final bytes.

The master is 1,862,454 bytes. Its SHA-256 is `352fb6b4afd98fb057946c3211b19c4ee79c2974f3d3ee3578a142f2a6b6da66`.

Both coherent look rows were refined with a compact, tucked tail following user review. The final sheet passed without waiving the quality gate. Some near-level intermediate look pitches remain intentionally subtle. Measured jump lift is 54 pixels and the landing differs from the resting baseline by 1 pixel.

## Codex compatibility export

The nine-row sprite is a direct crop of rows 0–8 of that master. No pose was redrawn, resized, or individually recentered. The 57 action frames and transparent unused cells retain the master pixels.

The repository verification script checks asset hashes, PNG dimensions, and local manifest fields. The installer additionally checks its source sprite before any destination writes. Package preparation checks pixel equality of the cropped region with the master and runs the bundled nine-row structural validator.

## Scope

Private service pet IDs, expiring URLs, upload sessions, absolute workstation paths, original chat transcripts, and unrelated workspace files are excluded from this repository. The portable `pet.json` is a local Codex manifest, not an export of an owner's remote pet record.

The local installer is tested against workspace test directories, including an identical reinstall and a conflicting existing folder. The checks do not claim that live dragging, terminal image rendering, or every desktop build has been exercised. See [installation notes](INSTALL.md) for version-dependent discovery.
