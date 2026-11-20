#!/usr/bin/env python3
"""Audit all 12 public planetary product photos and their published references.

This is a source/build-time media gate. It checks real pixel decoding (Pillow),
not merely presence of files or a green MkDocs build. Live browser/deployment
rendering is a separate check.

The five damaged legacy WebP photos (8P/10P/12P/14P/20P) were removed in
PR #286. Replacement files must be authentic 2048 x 1365 PNGs. Their absence
is reported as PENDING, never disguised with a placeholder or broken URL.
"""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from PIL import Image, UnidentifiedImageError

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PHOTOS = DOCS / "assets/images/products/planetary-gearboxes"
PRODUCTS = DOCS / "products/planetary-gearboxes"
MODELS = (8, 10, 12, 14, 16, 20, 22, 24, 28, 32, 36, 42)
PENDING_PNG = (8, 10, 12, 14, 20)
EXPECTED_EXISTING = {
    16: "16p-real-product-evidence.webp",
    22: "22p-real-product-evidence.webp",
    24: "24p-real-product-evidence.webp",
    28: "28p-real-product-evidence.webp",
    32: "32p-real-product-main-verified.webp",
    36: "36p-product-photo-20261014-v2.jpg",
    42: "42p-real-product-evidence.webp",
}
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
    pending: list[str] = []
    summary: list[str] = []

    sources = [DOCS / "index.md", PRODUCTS / "8-42mm-planetary-gear-reducer.md"]
    sources.extend(PRODUCTS / f"{n}p-planetary-gearbox.md" for n in MODELS)
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

        if n in EXPECTED_EXISTING:
            expected = PHOTOS / f"{n}p" / EXPECTED_EXISTING[n]
            if expected not in [target for _, _, target in model_refs]:
                errors.append(f"{n}P product page does not cite {expected.relative_to(ROOT)}")
            try:
                result = decode_photo(expected)
                summary.append(f"{n}P: VERIFIED {result}")
            except AssertionError as exc:
                errors.append(str(exc))
        else:
            png = PHOTOS / f"{n}p" / f"{n}p-real-product-evidence.png"
            old_webp = PHOTOS / f"{n}p" / f"{n}p-real-product-evidence.webp"
            if old_webp.exists():
                errors.append(f"{n}P corrupted legacy WebP was restored: {old_webp}")
            if png.exists():
                try:
                    result = decode_photo(png, expected_size=(2048, 1365))
                    if png not in [target for _, _, target in model_refs]:
                        errors.append(f"{n}P PNG exists but product page does not reference it")
                    else:
                        summary.append(f"{n}P: REPLACEMENT VERIFIED {result}")
                except AssertionError as exc:
                    errors.append(str(exc))
            elif model_refs:
                errors.append(f"{n}P has image references but no approved replacement PNG")
            else:
                pending.append(f"{n}P")
                summary.append(f"{n}P: PENDING authentic PNG (no broken image published)")

    for source in sources[:2]:
        refs = references.get(source, [])
        for n in (16, 22, 36):
            if not any(f"/{n}p/" in urlsplit(original).path for _, original, _ in refs):
                errors.append(f"{source.relative_to(ROOT)}: missing proven {n}P photo")
        if not refs:
            errors.append(f"{source.relative_to(ROOT)}: product photo grid is empty")

    if errors:
        raise SystemExit("Planetary image audit FAILED:\n- " + "\n- ".join(errors))
    for line in summary:
        print(line)
    print(
        f"PASS: {len(inspected)} referenced image binaries decoded; "
        f"{len(MODELS) - len(pending)}/12 models have photos; "
        f"pending originals: {', '.join(pending) if pending else 'none'}."
    )


if __name__ == "__main__":
    main()
