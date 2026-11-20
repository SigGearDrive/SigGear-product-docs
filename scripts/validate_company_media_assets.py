#!/usr/bin/env python3
"""Verify owner-provided SigGear manufacturing, inspection, branding and 80-21 media.

The 80-21 model identity is not confirmed as SG-8021. These three
source renders are held outside docs/ until verified by the owner.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageChops, UnidentifiedImageError

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MANIFEST = ROOT / "data/qa/owner-supplied-company-media-2026-11-20.json"
MANUFACTURING = DOCS / "company/manufacturing-and-quality-evidence.md"


def fail(message: str) -> None:
    raise SystemExit("Company media validation FAILED: " + message)


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records = data["items"]
    if len(records) != 13 or len({x["path"] for x in records}) != 13:
        fail("Expected 13 unique original/derived assets")
    photos = [record for record in records if record["status"] == "equipment_photo"]
    holds = [record for record in records if record["status"] == "identity_hold_render"]
    if len(photos) != 8 or len(holds) != 3:
        fail("Expect eight original equipment photos and three held 80-21 renders")

    for row in records:
        name = row["path"]
        path = ROOT / name
        if not path.is_file():
            fail(f"Original or derived image was not uploaded: {name}")
        if hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            fail(f"Changed image bytes, wrong original or re-encoded file: {name}")
        try:
            with Image.open(path) as im:
                if im.format != row["format"] or im.size != (
                    row["width"], row["height"]
                ):
                    fail(f"Unexpected format or original image size: {name}")
                im.verify()
            with Image.open(path) as im:
                im.load()
        except (OSError, ValueError, UnidentifiedImageError) as exc:
            fail(f"Image pixel decoding failed for {name}: {exc}")

    # White background is composited, NOT redrawn or recolored.
    official = DOCS / "assets/brand/siggear-official-wordmark-transparent.png"
    white_path = DOCS / "assets/brand/siggear-official-wordmark-white-background.png"
    with Image.open(official) as source:
        expected = Image.new("RGBA", source.size, (255, 255, 255, 255))
        expected.alpha_composite(source.convert("RGBA"))
    with Image.open(white_path) as output:
        if ImageChops.difference(expected.convert("RGB"), output.convert("RGB")).getbbox():
            fail("White logo is not the faithful alpha-composite of the owner's original")

    html = MANUFACTURING.read_text(encoding="utf-8")
    if html.count('class="siggear-company-evidence-card"') != 8:
        fail("Evidence page must contain eight original equipment photo cards")
    for row in photos:
        if row["path"].removeprefix("docs/") not in html:
            fail(f"Manufacturing evidence page does not use approved source: {row['path']}")

    for row in holds:
        if row["path"].startswith("docs/"):
            fail(f"80-21 render incorrectly published in docs/: {row['path']}")
    hold_names = [Path(row["path"]).name for row in holds]
    for md in DOCS.rglob("*.md"):
        source = md.read_text(encoding="utf-8")
        for name in hold_names:
            if name in source:
                fail(f"Unverified 80-21 reference added to public page: {md}")

    approved_logo = "docs/assets/brand/siggear-official-wordmark-white-background.png"
    for filename in (
        "data/external-catalogs/platforms/traceparts.yml",
        "data/external-catalogs/platforms/3dfindit.yml",
    ):
        if approved_logo not in (ROOT / filename).read_text(encoding="utf-8"):
            fail(f"External catalog logo metadata still refers to a missing source: {filename}")

    print("PASS: 13/13 media sources decoded and matched original SHA-256")
    print("PASS: 8 authentic workshop/inspection images placed on the evidence page")
    print("PASS: official white-background SigGear logo faithfully matches transparency source")
    print("PASS: 3 named 80-21 renders held for identity review, not mislabelled as SG-8021")


if __name__ == "__main__":
    main()
