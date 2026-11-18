#!/usr/bin/env python3
"""Reassemble user-approved original robot joint STEP assemblies from gzip binary parts.

Public release is intentional. The uploaded CAD files are full source assembly
models and are kept distinct from previously published simplified STEP files.
"""
from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART_ROOT = ROOT / '.github' / 'joint_cad_upload_parts'
OUT = ROOT / 'docs' / 'assets' / 'downloads' / 'joint-actuators'
RELEASE_VERSION = '2026-11-18'
RELEASES = {
    'SG-6010D': {
        'slug': 'sg6010d',
        'parts': 4,
        'source_file': '【西格·马】6010D.STEP',
        'download_file': 'SG-6010D_Original_Full_Assembly_20261118.step',
        'compressed_sha256': '27616bb4402343d1e2d905ab9209d36a0ac591ad10a4de94d123eeea637528f6',
        'sha256': '29013caf3e470c43f6a60a875786ed46140604288654b4483b37710dcb1d7dda',
        'bytes': 11653945,
        'variant': 'original assembly / variant to be checked against selected installation',
    },
    'SG-6010C': {
        'slug': 'sg6010c',
        'parts': 8,
        'source_file': '【西格·马】6010C.STEP',
        'download_file': 'SG-6010C_Original_Full_Assembly_20261118.step',
        'compressed_sha256': 'd5048db48c9f6de94be0d92428c1e200b4a2d91409858446c6b4269387982295',
        'sha256': 'c7feb40848ac3c7469a1fb35567a1ee0fdf65cba752e3f164ea52d9f0491ae2b',
        'bytes': 22348448,
        'variant': 'original assembly / separate from legacy public simplified STEP',
    },
    'SG-8021': {
        'slug': 'sg8021-driver',
        'parts': 7,
        'source_file': 'SG8021（驱动版）装配体3D.STEP',
        'download_file': 'SG-8021_Driver_Version_Original_Full_Assembly_20261118.step',
        'compressed_sha256': '3d89662b70ec5385f820c3c6f8c4f3e03dfb1d73d44c44b290e79cef3360251c',
        'sha256': '9591a7f2143d1a0418e39a876cc9d047c21289c3e80cc9c265aad40a1156f95d',
        'bytes': 19380522,
        'variant': 'driver-equipped assembly ONLY; not a driverless model',
    },
    'CPM-78-39': {
        'slug': 'cpm78-39',
        'parts': 5,
        'source_file': '78-39装配体.stp',
        'download_file': 'CPM-78-39_Original_Full_Assembly_20261118.step',
        'compressed_sha256': '3d907abc7821a5f9bda73ad80a340259bec438bc8a18d495f8f7fa9ddcf7e7e8',
        'sha256': '4a7791ede4c5b4c1430f75cc86325900bcb6bb65490c6deaf9c41d8149389d3b',
        'bytes': 16521809,
        'variant': 'original cycloidal joint assembly',
    },
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def reconstruct(model: str, spec: dict) -> dict:
    source_dir = PART_ROOT / spec['slug']
    paths = [source_dir / f'part{i:02d}.bin' for i in range(1, spec['parts'] + 1)]
    missing = [x for x in paths if not x.is_file()]
    if missing:
        raise FileNotFoundError(f'{model}: missing {len(missing)} CAD upload parts: {missing[:3]}')

    OUT.mkdir(parents=True, exist_ok=True)
    gz_path = OUT / (spec['download_file'] + '.gz.tmp')
    target = OUT / spec['download_file']
    try:
        with gz_path.open('wb') as stream:
            for part in paths:
                stream.write(part.read_bytes())
        digest = sha256_file(gz_path)
        if digest != spec['compressed_sha256']:
            raise ValueError(f'{model}: compressed binary transfer SHA mismatch: {digest}')
        with gzip.open(gz_path, 'rb') as source, target.open('wb') as output:
            for block in iter(lambda: source.read(1024 * 1024), b''):
                output.write(block)
        if target.stat().st_size != spec['bytes']:
            raise ValueError(f'{model}: decompressed size mismatch ({target.stat().st_size} != {spec["bytes"]})')
        digest = sha256_file(target)
        if digest != spec['sha256']:
            raise ValueError(f'{model}: original STEP SHA mismatch: {digest}')
        with target.open('rb') as stream:
            header = stream.read(32)
            stream.seek(-128, 2)
            tail = stream.read(128)
        if not header.startswith(b'ISO-10303-21;') or b'END-ISO-10303-21;' not in tail:
            raise ValueError(f'{model}: invalid STEP header / terminator')
        return {
            'model': model,
            'source_filename': spec['source_file'],
            'published_path': str(target.relative_to(ROOT / 'docs')),
            'published_sha256': digest,
            'bytes': spec['bytes'],
            'status': 'original_full_assembly_public_release',
            'variant': spec['variant'],
            'revision_label': RELEASE_VERSION,
        }
    finally:
        gz_path.unlink(missing_ok=True)


def main() -> None:
    releases = [reconstruct(model, spec) for model, spec in RELEASES.items()]
    for item in releases:
        print('PASS', item['model'], f'{item["bytes"]:,}', item['published_sha256'])
    manifest = OUT / 'original-full-assembly-release-manifest.json'
    manifest.write_text(
        json.dumps({
            'release': 'SigGear - Four Original Full Assembly Robot Joint STEP Files',
            'release_date': RELEASE_VERSION,
            'release_type': 'user_authorized_public_release',
            'models': releases,
        }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
    )
    print('PASS manifest:', manifest.relative_to(ROOT))


if __name__ == '__main__':
    main()