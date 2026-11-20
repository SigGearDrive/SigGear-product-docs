#!/usr/bin/env python3
"""Audit all 12 public planetary product photos and their published references.

This is a source/build-time media gate. It checks real pixel decoding (Pillow),
not merely presence of files or a green MkDocs build. Live browser/deployment
rendering is a separate check.

All 12 model pages must retain their authentic 2048 x 1365 PNG originals.
The 8–42 mm family index additionally uses one owner-supplied, unaltered
2048 x 1365 JPEG group photograph, checked by SHA-256 for exact provenance.
"""
from __future__ import annotations

import re
import hashlib
from pathlib import Path
from urllib.parse import unquote, urlsplit

from PIL import Image, UnidentifiedImageError

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PHOTOS = DOCS / "assets/images/products/planetary-gearboxes"
PRODUCTS = DOCS / "products/planetary-gearboxes"
MODELS = (8, 10, 12, 14, 16, 20, 22, 24, 28, 32, 36, 42)
EXPECTED_PNG = {n: f"{n}p-real-product-evidence.png" for n in MODELS}
LINEUP_IMAGE = (PHOTOS / "siggear-8-42mm-planetary-gearheads-real-lineup.jpg").resolve()
LINEUP_SHA256 = "45c2766dd7f1527bcfe89151a527b1e86f3a46f997219ecdc40c28d7e39bd901"
MODEL_IMAGE = re.compile(r"/planetary-gearboxes/(\d+)p/[^/?#]+\.(?:webp|png|jpe?g)$", re.I)
MD_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
HTML_IMAGE = re.compile(r"<img\b[^>]*\bsrc\s*=\s*['\"]([^'\"]+)['\"]", re.I)
EXTENSION_FORMAT = {".png": "PNG", ".webp": "WEBP", ".jpg": "JPEG", ".jpeg": "JPEG"}


def image_refs(source: Path) -> list[tuple[int, str, Path]]:
    text = source.read_text(encoding="utf-8")
    refs: list[tuple[int, str, Path]] = []
    for pattern in (MD_IMAGE, HTML_IMAGE):
        for hit in pattern.finditer(text):
            original = hit.group(1)
            url = urlsplit(original)
            if url.scheme or url.netloc or original.startswith("//"):
                continue
            path = unquote(url.path)
            if "/assets/images/products/planetary-gearboxes/" not in path:
                continue
            if path.startswith("/SigGear-product-docs/"):
                resolved = DOCS / path[len("/SigGear-product-docs/") :]
            elif path.startswith("/assets/"):
                resolved = DOCS / path.lstrip("/")
            elif path.startswith("/"):
                raise AssertionError(f"{source}: non-site-root image URL {original}")
            else:
                resolved = source.parent / path
            resolved = resolved.resolve()
            if not resolved.is_relative_to(DOCS.resolve()):
                raise AssertionError(f"{source}: image escapes docs tree: {original}")
            refs.append((text.count("\n", 0, hit.start()) + 1, original, resolved))
    return refs


def decode_photo(path: Path, expected_size: tuple[int, int] | None = None) -> str:
    if not path.is_file():
        raise AssertionError(f"Missing referenced photo: {path.relative_to(ROOT)}")
    if path.stat().st_size < 200:
        raise AssertionError(f"Truncated/empty photo: {path.relative_to(ROOT)}")
    extension = path.suffix.lower()
    expected_format = EXTENSION_FORMAT.get(extension)
    if not expected_format:
        raise AssertionError(f"Unsupported photo extension: {path}")
    try:
        with Image.open(path) as im:
            fmt, size = im.format, im.size
            im.verify()
        with Image.open(path) as im:
            im.load()  # verify() alone does not decompress/check the actual pixels
    except (OSError, ValueError, UnidentifiedImageError) as exc:
        raise AssertionError(f"Undecodable photo {path.relative_to(ROOT)}: {exc}") from exc
    if fmt != expected_format:
        raise AssertionError(f"Incorrect image format {path}: {fmt}, expected {expected_format}")
    if expected_size and size != expected_size:
        raise AssertionError(f"Wrong replacement dimensions {path}: {size}, expected {expected_size}")
    if size[0] <= 0 or size[1] <= 0:
        raise AssertionError(f"Invalid photo dimensions: {path}")
    return f"{size[0]}x{size[1]} {fmt}"


def main() -> None:
    errors: list[str] = []
    inspected: set[Path] = set()
    summary: list[str] = []

    sources = [DOCS / "index.md", PRODUCTS / "8-42mm-planetary-gear-reducer.md"]
    sources.extend(PRODUCTS / f"{n}p-planetary-gearbox.md" for n in MODELS)
    source_groups = {
        PRODUCTS / "micro-planetary-gearheads-8-16mm.md": (8, 10, 12, 14, 16),
        PRODUCTS / "miniature-planetary-gearheads-20-32mm.md": (20, 22, 24, 28, 32),
        PRODUCTS / "compact-planetary-gearheads-36-42mm.md": (36, 42),
    }
    sources.extend(source for source in source_groups if source not in sources)
    references: dict[Path, list[tuple[int, str, Path]]] = {}
    for source in sources:
        if not source.is_file():
            errors.append(f"Missing product/index source: {source.relative_to(ROOT)}")
            continue
        references[source] = image_refs(source)
        for line, original, target in references[source]:
            if not target.is_file():
                errors.append(f"Broken photo reference {source.relative_to(ROOT)}:{line} -> {original}")
                continue
            if target not in inspected:
                try:
                    decode_photo(target)
                except AssertionError as exc:
                    errors.append(str(exc))
                inspected.add(target)

    for n in MODELS:
        source = PRODUCTS / f"{n}p-planetary-gearbox.md"
        model_refs = references.get(source, [])
        wrong_model_refs = [
            ref for _, ref, _ in model_refs
            if (m := MODEL_IMAGE.search(urlsplit(ref).path)) and int(m.group(1)) != n
        ]
        if wrong_model_refs:
            errors.append(f"{n}P page points to another model's photo: {wrong_model_refs}")

        png = PHOTOS / f"{n}p" / EXPECTED_PNG[n]
        old_webp = PHOTOS / f"{n}p" / f"{n}p-real-product-evidence.webp"
        if n in (8, 10, 12, 14, 20) and old_webp.exists():
            errors.append(f"{n}P damaged legacy WebP was restored: {old_webp}")
        try:
            result = decode_photo(png, expected_size=(2048, 1365))
            if png not in [target for _, _, target in model_refs]:
                errors.append(f"{n}P approved PNG not referenced by product page")
            else:
                summary.append(f"{n}P: VERIFIED {result}")
        except AssertionError as exc:
            errors.append(str(exc))

    # The 12-model directory and all three category galleries must display
    # precisely their own model images; no duplicates, empty cards or cross-model reuse.
    for source, group in source_groups.items():
        observed = [
            int(match.group(1))
            for _, original, _ in references.get(source, [])
            if (match := MODEL_IMAGE.search(urlsplit(original).path))
        ]
        if observed != list(group):
            errors.append(
                f"{source.relative_to(ROOT)} gallery models {observed}; "
                f"expected {list(group)}"
            )
        if source.is_file():
            html = source.read_text(encoding="utf-8")
            if html.count('loading="lazy"') < len(group):
                errors.append(
                    f"{source.relative_to(ROOT)} gallery must lazy-load every photo"
                )

    # Homepage keeps three separately labelled genuine reference photos.
    homepage = DOCS / "index.md"
    home_refs = references.get(homepage, [])
    for n in (16, 22, 36):
        if not any(f"/{n}p/" in urlsplit(original).path for _, original, _ in home_refs):
            errors.append(f"{homepage.relative_to(ROOT)} missing approved {n}P photo")
    if not home_refs:
        errors.append("Homepage product photo grid is empty")

    # Series page intentionally uses ONE real family photograph, not twelve
    # repeated/scaled individual model photos or a synthetic collage.
    series = PRODUCTS / "8-42mm-planetary-gear-reducer.md"
    series_refs = [target for _, _, target in references.get(series, [])]
    if series_refs != [LINEUP_IMAGE]:
        errors.append(
            f"{series.relative_to(ROOT)} must reference only the exact 12-model lineup JPEG"
        )
    try:
        decode_photo(LINEUP_IMAGE, expected_size=(2048, 1365))
        actual_sha = hashlib.sha256(LINEUP_IMAGE.read_bytes()).hexdigest()
        if actual_sha != LINEUP_SHA256:
            errors.append(
                f"Series lineup JPEG bytes differ from the user's original: {actual_sha}"
            )
        else:
            summary.append("12-model real lineup JPEG: VERIFIED ORIGINAL SHA-256")
    except AssertionError as exc:
        errors.append(str(exc))

    if errors:
        raise SystemExit("Planetary image audit FAILED:\n- " + "\n- ".join(errors))
    for line in summary:
        print(line)
    print(
        f"PASS: {len(inspected)} referenced image binaries decoded; "
        "all 12 approved PNG model photos verified."
    )


if __name__ == "__main__":
    main()
