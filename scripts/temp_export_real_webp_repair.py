#!/usr/bin/env python3
"""Temporary one-time restoration of exact original WebP bytes via CI logs."""
from pathlib import Path
import base64

root=Path(__file__).resolve().parents[1]
for n in (8,10,12,14,16,20,22):
    p=root / f"docs/assets/images/products/planetary-gearboxes/{n}p/{n}p-real-product-evidence.webp"
    data=p.read_bytes()
    assert len(data)>=20 and data[:4]==b"RIFF" and data[8:12]==b"WEBP",p
    declared=int.from_bytes(data[4:8],"little")+8
    print(f"SIGGEAR_IMAGE_STATUS {n}P actual={len(data)} riff={declared}",flush=True)
    if declared!=len(data):
        assert 20<=declared<len(data),f"Truncated actual image cannot be fixed by trimming: {p}"
        fixed=data[:declared]
        print(f"SIGGEAR_IMAGE_BEGIN {n}P",flush=True)
        print(base64.b64encode(fixed).decode("ascii"),flush=True)
        print(f"SIGGEAR_IMAGE_END {n}P",flush=True)
