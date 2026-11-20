#!/usr/bin/env python3
"""TEMP: repair only RIFF-inconsistent genuine product photos in CI; emit base64."""
from pathlib import Path
from io import BytesIO
import base64
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES=True
root=Path(__file__).resolve().parents[1]
for n in (8,10,12,14,16,20,22):
    p=root / f"docs/assets/images/products/planetary-gearboxes/{n}p/{n}p-real-product-evidence.webp"
    data=p.read_bytes()
    assert len(data)>=20 and data[:4]==b"RIFF" and data[8:12]==b"WEBP",p
    declared=int.from_bytes(data[4:8],"little")+8
    print(f"SIGGEAR_IMAGE_STATUS {n}P actual={len(data)} riff={declared}",flush=True)
    if declared==len(data):
        continue
    try:
        source=Image.open(BytesIO(data))
        source.load()
        print(f"SIGGEAR_IMAGE_DECODE {n}P size={source.size} mode={source.mode}",flush=True)
        image=source.convert("RGB")
        out=BytesIO()
        image.save(out, format="WEBP", lossless=True, method=5)
        fixed=out.getvalue()
        assert fixed[:4]==b"RIFF" and fixed[8:12]==b"WEBP"
        assert int.from_bytes(fixed[4:8],"little")+8==len(fixed)
        check=Image.open(BytesIO(fixed))
        check.load()
        print(f"SIGGEAR_IMAGE_BEGIN {n}P",flush=True)
        print(base64.b64encode(fixed).decode("ascii"),flush=True)
        print(f"SIGGEAR_IMAGE_END {n}P",flush=True)
    except Exception as exc:
        print(f"SIGGEAR_IMAGE_UNREPAIRABLE {n}P {type(exc).__name__}: {exc}",flush=True)
