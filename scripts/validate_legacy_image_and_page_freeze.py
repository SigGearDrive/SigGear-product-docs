#!/usr/bin/env python3
"""Protect SigGear's retired pre-8000-rpm-era image assets and frozen SEO pages.

This checks repository sources and files, not pixel text inside arbitrary photos.
The old parameter/marketing graphics were explicitly retired in the 2026-11-20
cleanup; current torque, speed and geometry references must link to the official
downloadable Datasheet and 2D PDF, not removed artwork.

Five previously rewritten existing URL sources are frozen until an explicit
owner instruction updates their pinned Git blob hashes.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MANIFEST = ROOT / "data/seo/frozen-legacy-pages-2026-11-20.json"
MODELS = (8, 10, 12, 14, 16, 20, 22)
RETIRED_IMAGE_KINDS = (
    "main",
    "dimensions",
    "mechanical-details",
    "motor-compatibility",
    "structure-and-ratios",
)


def git_blob_sha(payload: bytes) -> str:
    header = b"blob " + str(len(payload)).encode("ascii") + bytes([0])
    return hashlib.sha1(header + payload).hexdigest()


def check_frozen_pages() -> None:
    spec = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert spec.get("status") == "frozen_until_explicit_owner_instruction"
    pages = spec["pages"]
    assert len(pages) == 5, "Expected exactly five frozen legacy pages"
    assert len({entry["path"] for entry in pages}) == 5, "Duplicate frozen page"
    for entry in pages:
        rel = entry["path"]
        assert rel.startswith("docs/") and rel.endswith(".md"), rel
        path = ROOT / rel
        assert path.is_file(), f"Frozen legacy page removed: {rel}"
        actual = git_blob_sha(path.read_bytes())
        expected = entry["git_blob_sha"]
        assert actual == expected, (
            f"Frozen page changed without an explicit unfreeze+manifest review: "
            f"{rel}, expected {expected}, actual {actual}"
        )


def check_retired_image_assets() -> None:
    retired_names = []
    for n in MODELS:
        folder = DOCS / f"assets/images/products/planetary-gearboxes/{n}p"
        for kind in RETIRED_IMAGE_KINDS:
            filename = f"{n}p-planetary-gearbox-{kind}.webp"
            path = folder / filename
            assert not path.exists(), f"Retired specification artwork must not ship: {path}"
            retired_names.append(filename)
        photo = folder / f"{n}p-real-product-evidence.webp"
        assert photo.is_file(), f"Real {n}P product photo must be retained: {photo}"

    # Do not leave a dead backlink in published Markdown, HTML, JS, CSS or nav.
    public_sources = list(DOCS.rglob("*.md"))
    public_sources += list(DOCS.rglob("*.html"))
    public_sources += list(DOCS.rglob("*.css"))
    public_sources += list(DOCS.rglob("*.js"))
    public_sources += [ROOT / "mkdocs.yml"]
    for source in public_sources:
        text = source.read_text(encoding="utf-8", errors="replace")
        for name in retired_names:
            assert name not in text, (
                f"Public source still references deleted legacy image {name}: "
                f"{source.relative_to(ROOT)}"
            )

    # Also reject legible old speed ceilings in retained SVGs.
    for svg in (DOCS / "assets/images").rglob("*.svg"):
        text = svg.read_text(encoding="utf-8", errors="replace")
        assert not re.search(r"8[,]?000[ ]*(?:rpm|r/min)", text, re.I), (
            f"Retained SVG mentions obsolete 8000-rpm limitation: {svg}"
        )


def check_data_source_and_photos() -> None:
    hub = (
        DOCS / "engineering-resources/planetary-gearboxes/public-cad-release-v1.md"
    ).read_text(encoding="utf-8")
    for n in MODELS:
        page = (
            DOCS / f"products/planetary-gearboxes/{n}p-planetary-gearbox.md"
        ).read_text(encoding="utf-8")
        expected_photo = f"{n}p-real-product-evidence.webp"
        assert expected_photo in page, f"{n}P model page missing real product image"
        pdf_prefix = f"../../assets/downloads/{n}p/{n}P_Planetary_Gearhead_Datasheet_"
        expected_pdf = next(
            (part.split(")", 1)[0] for part in hub.split("(")
             if part.startswith(pdf_prefix)),
            None,
        )
        assert expected_pdf, f"No approved published Datasheet for {n}P"
        assert expected_pdf in page, (
            f"{n}P product page does not link to the current published PDF"
        )
        assert f"{n}P_2D_Drawing.pdf" in page, (
            f"{n}P model page missing direct official 2D PDF"
        )

    for page in (
        DOCS / "index.md",
        DOCS / "products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md",
    ):
        source = page.read_text(encoding="utf-8")
        for n in (10, 20):
            assert f"{n}p-real-product-evidence.webp" in source, (
                f"{page.relative_to(ROOT)} missing clean {n}P product photo"
            )


def main() -> None:
    check_frozen_pages()
    check_retired_image_assets()
    check_data_source_and_photos()
    print(
        "PASS: 35 legacy parameter images retired; original Datasheet/2D and "
        "real photos retained; 5 rebuilt pages frozen at verified Git blob SHA."
    )


if __name__ == "__main__":
    main()
