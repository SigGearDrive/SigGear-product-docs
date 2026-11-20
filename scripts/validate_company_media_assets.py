#!/usr/bin/env python3
"""Verify owner-provided SigGear manufacturing, inspection, branding and 80-21 media.

The three 80-21 product-render source files were identified as SG-8021
by the owner on 2026-11-20. They are released as renders, NOT photography.
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
    published = [record for record in records if record["status"] == "owner_confirmed_sg8021_render"]
    if len(photos) != 8 or len(published) != 3:
        fail("Expect eight original equipment photos and three owner-confirmed SG-8021 renders")

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

    product = (DOCS / "products/robot-joint-actuators/sg8021.md").read_text(encoding="utf-8")
    if "product renderings" not in product or "not physical product photographs" not in product:
        fail("SG-8021 render/photo identity boundary absent from product page")
    if len(published) != 3:
        fail("SG-8021 original product views must be front, side and rear")
    for orientation in ("front", "side", "rear"):
        files = [row for row in published if f"-{orientation}-render.jpg" in row["path"]]
        if len(files) != 1 or files[0]["path"] != (
            f"docs/assets/images/products/robot-joint-actuators/sg8021/"
            f"sg8021-robot-joint-actuator-{orientation}-render.jpg"
        ):
            fail(f"Missing exact confirmed SG-8021 {orientation} media source")
        if files[0]["path"].removeprefix("docs/") not in product:
            fail(f"Confirmed SG-8021 {orientation} render not published on product page")

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
    print("PASS: 3 owner-confirmed SG-8021 product renders, correctly labelled not photographs")


if __name__ == "__main__":
    main()
