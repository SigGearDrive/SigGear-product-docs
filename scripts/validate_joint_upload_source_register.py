#!/usr/bin/env python3
"""Source-level 2D drawing/photo release gate (2026-11-19 uploads).

The source register records user-provided PDFs and photos without asserting
approval for drawings that are not yet present in the public git tree.
"""
from __future__ import annotations
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REGISTER = ROOT / ".github/joint-drawing-photo-inbox/source_register_2026-11-19.json"

def check() -> None:
    data = json.loads(REGISTER.read_text(encoding="utf-8"))
    photos = data["photos"]
    drawings = data["drawings"]
    assert len(photos) == 6
    assert len(drawings) == 6
    assert len(data["excluded"]) == 1
    published = [p for p in photos if p["status"].startswith("published_")]
    assert len(published) == 1, "Known uploaded photos must be explicitly verified"
    for p in published:
        source = ROOT / p["target"]
        assert source.is_file(), f"Public image missing: {source}"
        assert hashlib.sha256(source.read_bytes()).hexdigest() == p["targetSha256"], p["target"]
        page = DOCS / "products/cycloidal-joint-modules/cpm78-39.md"
        assert source.name in page.read_text(encoding="utf-8"), "CPM-78-39 image not linked"
    for p in photos:
        if not p["status"].startswith("published_"):
            assert not (ROOT / p["target"]).is_file(), "Unreviewed photo unexpectedly published"
    for d in drawings:
        if d["status"] == "source_checked_not_uploaded":
            assert d["target"]
            assert not (ROOT / d["target"]).is_file(), "Drawing file has not been checked for public release"
        else:
            assert d["target"] is None, "Blocked drawing must never declare a public path"
    blocked = next(d for d in drawings if d["model"] == "SG-6010HB")
    assert blocked["status"] == "blocked_dimension_conflict"
    assert "22.57" in blocked["matches"] and "25.57" in blocked["matches"]
    identity = next(d for d in drawings if d["model"] == "CPM-78-39")
    assert identity["status"] == "hold_pending_model_code_signoff"
    assert "SG2368B" in identity["matches"]
    assert data["excluded"][0]["model"] == "SG-6010D"
    print("PASS model-specific photo checksum, original drawing release holds and dimension-conflict gate")

if __name__ == "__main__":
    check()
