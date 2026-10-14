#!/usr/bin/env python3
"""Validate SigGear documentation structure and internal references."""

from __future__ import annotations

import re
import os
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"
MODEL_INDEX = DOCS / "knowledge-base" / "product-model-index.md"

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
H1_RE = re.compile(r"^#\s+\S", re.MULTILINE)
NAV_PATH_RE = re.compile(r"(?:^|:\s+)([A-Za-z0-9_./\u2013-]+\.md)\s*$", re.MULTILINE)


def markdown_files() -> list[Path]:
    return sorted(DOCS.rglob("*.md"))


def link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    return target.split(maxsplit=1)[0]


def validate_h1(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        count = len(H1_RE.findall(text))
        if count != 1:
            errors.append(f"{path.relative_to(ROOT)}: expected exactly one H1, found {count}")
    return errors


def validate_links(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = link_target(raw)
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith(("#", "//")):
                continue
            relative_path = unquote(parsed.path)
            if not relative_path:
                continue
            resolved = (path.parent / relative_path).resolve()
            try:
                resolved.relative_to(DOCS.resolve())
            except ValueError:
                errors.append(
                    f"{path.relative_to(ROOT)}: link leaves docs directory: {target}"
                )
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing target: {target}")
    return errors


def validate_navigation(files: list[Path]) -> list[str]:
    errors: list[str] = []
    text = MKDOCS.read_text(encoding="utf-8")
    nav_paths = set(NAV_PATH_RE.findall(text))
    doc_paths = {str(path.relative_to(DOCS)) for path in files}

    for nav_path in sorted(nav_paths):
        if not (DOCS / nav_path).exists():
            errors.append(f"mkdocs.yml: navigation target does not exist: {nav_path}")

    missing_from_nav = sorted(doc_paths - nav_paths)
    for doc_path in missing_from_nav:
        errors.append(f"mkdocs.yml: documentation page is missing from navigation: {doc_path}")
    return errors


def validate_product_index() -> list[str]:
    errors: list[str] = []
    if not MODEL_INDEX.exists():
        return ["Product model index is missing"]

    index_text = MODEL_INDEX.read_text(encoding="utf-8")
    product_pages = sorted(
        path
        for path in (DOCS / "products").rglob("*.md")
        if path.name != "index.md"
    )
    for page in product_pages:
        relative = Path(os.path.relpath(page, MODEL_INDEX.parent)).as_posix()
        if relative not in index_text:
            errors.append(
                f"{page.relative_to(ROOT)}: canonical product page is not linked from the product model index"
            )
    return errors



def validate_key_product_image_files() -> list[str]:
    """Check that product-page WebP files can be read as complete RIFF containers.

    In particular, a one-character loss in a base64 transfer creates a file
    that GitHub Pages publishes successfully but browsers cannot decode.
    """
    errors: list[str] = []
    models = ("8p", "32p")
    for model in models:
        page = DOCS / "products" / "planetary-gearboxes" / f"{model}-planetary-gearbox.md"
        text = page.read_text(encoding="utf-8")
        for raw in IMAGE_RE.findall(text):
            target = link_target(raw)
            uri = urlsplit(target)
            if uri.scheme or not uri.path.lower().endswith(".webp"):
                continue
            file = (page.parent / unquote(uri.path)).resolve()
            if not file.exists():
                errors.append(f"{page.relative_to(ROOT)}: missing image: {target}")
                continue
            data = file.read_bytes()
            if len(data) < 20 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
                errors.append(f"{file.relative_to(ROOT)}: not a valid WebP RIFF container")
                continue
            declared = int.from_bytes(data[4:8], "little") + 8
            if declared != len(data):
                errors.append(
                    f"{file.relative_to(ROOT)}: truncated or malformed WebP "
                    f"(RIFF declares {declared} bytes, actual {len(data)})"
                )
    return errors


def main() -> int:
    files = markdown_files()
    errors = []
    errors.extend(validate_h1(files))
    errors.extend(validate_links(files))
    errors.extend(validate_navigation(files))
    errors.extend(validate_product_index())
    errors.extend(validate_key_product_image_files())

    if errors:
        print("Documentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Documentation validation passed: {len(files)} Markdown pages, "
        "navigation, local links and product index checked."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
