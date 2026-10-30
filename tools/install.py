#!/usr/bin/env python3
"""Install the Codex-compatible Bro Shark bundle without replacing user files."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import struct
import sys

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'pets'/'bro-shark'
FILES=('pet.json','spritesheet.png')

def checked_sources():
    metadata=json.loads((ROOT/'assets.json').read_text(encoding='utf-8'))
    manifest=json.loads((SOURCE/'pet.json').read_text(encoding='utf-8'))
    if manifest.get('id')!='bro-shark' or manifest.get('spritesheetPath')!='spritesheet.png':
        raise ValueError('Unexpected pet identity or sprite path; no files installed.')
    if manifest.get('frame')!={'width':192,'height':208,'columns':8,'rows':9}:
        raise ValueError('Unexpected Codex frame layout; no files installed.')
    image=(SOURCE/'spritesheet.png').read_bytes()
    if image[:8]!=b'\x89PNG\r\n\x1a\n' or image[12:16]!=b'IHDR':
        raise ValueError('Sprite is not a PNG; no files installed.')
    if struct.unpack('>II',image[16:24])!=(1536,1872):
        raise ValueError('Codex-compatible sprite must be 1536x1872; no files installed.')
    expected=metadata['files']['pets/bro-shark/spritesheet.png']['sha256']
    if hashlib.sha256(image).hexdigest()!=expected:
        raise ValueError('Sprite checksum mismatch; no files installed.')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--codex-home',type=Path,help='Use a custom Codex state directory instead of CODEX_HOME or ~/.codex.')
    parser.add_argument('--dry-run',action='store_true',help='Validate and print the destination without writing anything.')
    args=parser.parse_args()
    checked_sources()
    configured=args.codex_home or os.environ.get('CODEX_HOME') or Path.home()/'.codex'
    codex_dir=Path(configured).expanduser().resolve()
    target=codex_dir/'pets'/'bro-shark'
    if target.exists():
        if target.is_dir() and all((target/name).is_file() and (target/name).read_bytes()==(SOURCE/name).read_bytes() for name in FILES):
            print('Bro Shark is already installed with identical files. Nothing changed.')
            return 0
        raise FileExistsError('Destination already exists with different or incomplete files: '+str(target)+'. No existing files were changed. Choose another --codex-home or review that folder yourself.')
    if args.dry_run:
        print('Validated. Would copy pet.json and spritesheet.png to '+str(target))
        return 0
    # Validate before creating the destination. Never overwrite or delete a pet.
    target.mkdir(parents=True,exist_ok=False)
    for name in FILES:
        with (target/name).open('xb') as output:
            with (SOURCE/name).open('rb') as source:
                shutil.copyfileobj(source,output)
    print('Installed Bro Shark to '+str(target))
    print('In an interactive Codex CLI session, enter /pets bro-shark.')
    print('In desktop builds with Pets, refresh the pet picker and select Bro Shark.')
    return 0

if __name__=='__main__':
    try:
        sys.exit(main())
    except (OSError,ValueError,KeyError) as exc:
        print('Install stopped: '+str(exc),file=sys.stderr)
        sys.exit(1)
