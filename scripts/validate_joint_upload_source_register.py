#!/usr/bin/env python3
"""Validate user-supplied 2D reference drawing and product-render releases."""
from pathlib import Path
import hashlib
import json
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/"docs"
REGISTER=ROOT/".github/joint-drawing-photo-inbox/source_register_2026-11-19.json"

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def check():
    d=json.loads(REGISTER.read_text(encoding="utf-8"))
    assert len(d["drawings"])==6 and len(d["photos"])==6 and len(d["excluded"])==1
    published_photos=[p for p in d["photos"] if p["status"].startswith("published_")]
    assert len(published_photos)==4, "Expected four released render assets (including existing motor view)"
    for p in d["photos"]:
        path=ROOT/p["target"]
        if p["status"].startswith("published_"):
            assert path.is_file(), p["target"]
            assert sha(path)==p["targetSha256"], p["target"]
            with Image.open(path) as image:
                assert image.format=="WEBP" and image.size==(800,800)
                image.verify()
            page=(DOCS/"products/cycloidal-joint-modules/cpm78-39.md") if p["model"]=="CPM-78-39" else (DOCS/"products/robot-joint-actuators/sg6010d.md")
            assert path.name in page.read_text(encoding="utf-8"), p["target"]
        else:
            assert not path.exists(), "Nonreleased photo exists unexpectedly: "+p["target"]
    released=[x for x in d["drawings"] if x["status"]=="published_reference_2d_pdf"]
    assert len(released)==4, "Expected four reference-only 2D PDFs"
    for x in d["drawings"]:
        if x["status"]=="published_reference_2d_pdf":
            f=ROOT/x["target"]
            assert f.is_file(), x["target"]
            b=f.read_bytes()
            assert b[:5]==b"%PDF-" and b"%%EOF" in b[-200:], x["target"]
            assert len(b)==x["publishedBytes"] and sha(f)==x["publishedSha256"], x["target"]
            assert x["rasterParityVerified"] is True and x["manufacturingControlled"] is False
            assert f.name in (DOCS/"engineering-resources/robot-joint-actuators/quick-downloads.md").read_text(encoding="utf-8")
        elif x["status"]=="source_checked_not_uploaded":
            assert not (ROOT/x["target"]).exists()
        else:
            assert x["target"] is None, "Blocked source must not have a public target"
    identity=next(x for x in d["drawings"] if x["model"]=="CPM-78-39")
    assert identity["status"]=="hold_pending_model_code_signoff" and "SG2368B" in identity["matches"]
    hb=next(x for x in d["drawings"] if x["model"]=="SG-6010HB")
    assert hb["status"]=="blocked_dimension_conflict" and "22.57" in hb["matches"] and "25.57" in hb["matches"]
    assert d["excluded"][0]["model"]=="SG-6010D"
    print("PASS: four model-matched 2D reference PDFs, four published render images and all engineering holds")

if __name__=="__main__":
    check()
