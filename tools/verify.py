#!/usr/bin/env python3
"""Verify bundled asset integrity and the portable pet manifest; standard library only."""
import hashlib
import json
from pathlib import Path
import struct
import sys

ROOT=Path(__file__).resolve().parents[1]

def main():
    metadata=json.loads((ROOT/'assets.json').read_text(encoding='utf-8'))
    checked=0
    for name,record in metadata['files'].items():
        relative=Path(name)
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('Asset paths must stay inside the repository.')
        data=(ROOT/relative).read_bytes()
        if len(data)!=record['bytes'] or hashlib.sha256(data).hexdigest()!=record['sha256']:
            raise ValueError('Asset checksum or size mismatch: '+name)
        checked+=1
    for name,dimensions in [('pets/bro-shark/spritesheet.png',(1536,1872)),('assets/bro-shark-v2.png',(1536,2288))]:
        data=(ROOT/name).read_bytes()
        if data[:8]!=b'\x89PNG\r\n\x1a\n' or data[12:16]!=b'IHDR' or struct.unpack('>II',data[16:24])!=dimensions:
            raise ValueError('Unexpected PNG layout: '+name)
    manifest=json.loads((ROOT/'pets/bro-shark/pet.json').read_text(encoding='utf-8'))
    if manifest.get('id')!='bro-shark' or manifest.get('displayName')!='Bro Shark' or manifest.get('spritesheetPath')!='spritesheet.png':
        raise ValueError('Unexpected portable pet manifest.')
    if manifest.get('frame')!={'width':192,'height':208,'columns':8,'rows':9}:
        raise ValueError('Unexpected portable frame grid.')
    print('Verified '+str(checked)+' asset checksums, both PNG layouts, and the Codex manifest.')
    return 0

if __name__=='__main__':
    try:
        sys.exit(main())
    except (OSError,ValueError,KeyError) as exc:
        print('Verification failed: '+str(exc),file=sys.stderr)
        sys.exit(1)
