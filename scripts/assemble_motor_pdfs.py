#!/usr/bin/env python3
"""Reconstruct published SigGear motor-only PDF downloads from verified binary pieces.

The source PDFs are preserved byte for byte. The upload pieces are Git blobs in
.github/motor_pdf_upload_parts/, not part of the public download directory.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART_ROOT = ROOT / ".github" / "motor_pdf_upload_parts" / "8mm"
DOWNLOAD_ROOT = ROOT / "docs" / "assets" / "downloads" / "motors" / "8mm"

RELEASES = {
    "hs816-set-a": {
        "filename": "SigGear_8mm_HS-816-Q_Winding_Set_A_D1.pdf",
        "parts": 6,
        "size": 6210672,
        "sha256": "eaa2bc3b04671bbcedc6a7281b114fbb4eeaf0869222bdd073f34841be38dac9",
    },
    "hs816-set-b": {
        "filename": "SigGear_8mm_HS-816-Q_Winding_Set_B_D1.pdf",
        "parts": 6,
        "size": 6383731,
        "sha256": "6825c3e2cacc4b34685bf8da0d33f08d044b302dd3e0c0075eb1d32397ddafcc",
    },
    "hs820-set-c": {
        "filename": "SigGear_8mm_HS-820-Q_Winding_Set_C_D1.pdf",
        "parts": 9,
        "size": 10072498,
        "sha256": "39c35560ef99784ab02351cdd592cbd4e1ffbfac36713692740d0919b3344b3d",
    },
}


def reconstruct(model: str, spec: dict) -> dict:
    parent = PART_ROOT / model
    if not parent.exists():
        raise FileNotFoundError(f"{model}: required binary part directory is missing")
    parts = [parent / f"part-{i:03d}.bin" for i in range(1, spec["parts"] + 1)]
    missing = [x.name for x in parts if not x.is_file()]
    if missing:
        raise FileNotFoundError(f"{model}: missing PDF upload parts {missing}")
    unexpected = [x.name for x in parent.glob("part-*.bin") if x not in parts]
    if unexpected:
        raise ValueError(f"{model}: unexpected PDF parts {unexpected}")

    DOWNLOAD_ROOT.mkdir(parents=True, exist_ok=True)
    target = DOWNLOAD_ROOT / spec["filename"]
    temp = target.with_suffix(target.suffix + ".tmp")
    digest = hashlib.sha256()
    total = 0
    try:
        with temp.open("wb") as dest:
            for part in parts:
                chunk = part.read_bytes()
                if not chunk:
                    raise ValueError(f"{model}: empty PDF part {part.name}")
                digest.update(chunk)
                total += len(chunk)
                dest.write(chunk)
        if total != spec["size"]:
            raise ValueError(f"{model}: wrong PDF byte length {total} != {spec['size']}")
        if digest.hexdigest() != spec["sha256"]:
            raise ValueError(f"{model}: SHA-256 checksum mismatch")
        with temp.open("rb") as src:
            if src.read(5) != b"%PDF-":
                raise ValueError(f"{model}: invalid PDF header")
            src.seek(max(0, total - 1024))
            if b"%%EOF" not in src.read():
                raise ValueError(f"{model}: PDF terminator missing")
        temp.replace(target)
    finally:
        temp.unlink(missing_ok=True)

    print(f"PASS {model}: {total:,} bytes, SHA-256 {digest.hexdigest()}")
    return {
        "motor": model,
        "published_file": spec["filename"],
        "relative_url": f"assets/downloads/motors/8mm/{spec['filename']}",
        "bytes": total,
        "sha256": digest.hexdigest(),
        "parts": len(parts),
        "status": "assembled_and_validated",
    }


def main() -> None:
    result = [reconstruct(model, spec) for model, spec in RELEASES.items()]
    (DOWNLOAD_ROOT / "release-manifest.json").write_text(
        json.dumps({"release": "SigGear 8 mm DC motor datasheets D1", "models": result}, indent=2) + "\n",
        encoding="utf-8",
    )
    print("PASS 8 mm motor PDF release manifest")


if __name__ == "__main__":
    main()
