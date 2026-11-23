#!/usr/bin/env python3
"""Prepare contact-only PDF revisions for the published GitHub Pages build.

The checked-in PDF originals remain untouched. During Pages deployment
this tool modifies only text-showing operators that contain the exact old
email string. It leaves every geometry drawing and all other text intact,
and verifies the full extracted text of every page before publishing.

Run --preview on PRs; --in-place only in the isolated deploy worktree
after source asset integrity checks have run.
"""
from __future__ import annotations

import argparse
import os
import re
import tempfile
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, ByteStringObject, ContentStream, NameObject, TextStringObject

ROOT = Path(__file__).resolve().parents[1]
DOWNLOADS = ROOT / "docs/assets/downloads"
OLD = "wangwanrong@siggear.com"
NEW = "luffy@siggear.com"


def change_string(value):
    if isinstance(value, TextStringObject):
        original = str(value)
        if OLD in original:
            return TextStringObject(original.replace(OLD, NEW)), True
    if isinstance(value, ByteStringObject):
        original = bytes(value)
        if OLD.encode() in original:
            return ByteStringObject(original.replace(OLD.encode(), NEW.encode())), True
    return value, False


def replace_content_stream(page, writer: PdfWriter) -> int:
    source = page.get_contents()
    if source is None:
        return 0
    stream = ContentStream(source, writer)
    count = 0
    for operands, operation in stream.operations:
        if operation in (b"Tj", b"'", b'"'):
            for index, value in enumerate(operands):
                replaced, changed = change_string(value)
                if changed:
                    operands[index] = replaced
                    count += 1
        elif operation == b"TJ" and operands and isinstance(operands[0], ArrayObject):
            parts = operands[0]
            for index, value in enumerate(parts):
                replaced, changed = change_string(value)
                if changed:
                    parts[index] = replaced
                    count += 1
    if count:
        # /Contents must be an indirect stream, not a direct stream object.
        page[NameObject("/Contents")] = writer._add_object(stream)
    return count


def replace_link_actions(page) -> int:
    count = 0
    for reference in page.get("/Annots", []):
        annotation = reference.get_object()
        action = annotation.get("/A")
        if action is None:
            continue
        if hasattr(action, "get_object"):
            action = action.get_object()
        if action.get("/S") != "/URI":
            continue
        uri = action.get("/URI")
        if uri is not None and OLD in str(uri):
            action[NameObject("/URI")] = TextStringObject(str(uri).replace(OLD, NEW))
            count += 1
    return count


def extracted(reader: PdfReader) -> list[str]:
    return [(page.extract_text(extraction_mode="plain") or "") for page in reader.pages]


def patch(source: Path, destination: Path) -> tuple[int, int]:
    reader = PdfReader(str(source), strict=False)
    before = extracted(reader)
    if not any(OLD in text for text in before):
        return 0, 0

    for page in reader.pages:
        if page.get("/Annots"):
            for annot in page["/Annots"]:
                obj = annot.get_object()
                if "/ByteRange" in obj:
                    raise RuntimeError(f"Refusing to change signed PDF: {source}")

    writer = PdfWriter(clone_from=reader)
    changes = 0
    annotations = 0
    for page in writer.pages:
        changes += replace_content_stream(page, writer)
        annotations += replace_link_actions(page)

    if changes == 0:
        raise RuntimeError(f"PDF text extracts the old address but cannot replace its encoded text operators: {source}")

    # Preserve all original PDF metadata except old email references, if any.
    metadata = writer.metadata
    if metadata and any(OLD in str(value) for value in metadata.values()):
        writer.add_metadata({str(k): str(v).replace(OLD, NEW) for k, v in metadata.items() if v is not None})

    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("wb") as out:
        writer.write(out)
    revised = PdfReader(str(destination), strict=False)
    after = extracted(revised)

    if len(after) != len(before):
        raise RuntimeError(f"Changed PDF page count: {source}")
    for index, (original, updated) in enumerate(zip(before, after), 1):
        if updated != original.replace(OLD, NEW):
            raise RuntimeError(f"PDF non-contact text changed at page {index}: {source}")
        if OLD in updated:
            raise RuntimeError(f"PDF still displays previous address at page {index}: {source}")
    if sum(text.count(NEW) for text in after) < sum(text.count(OLD) for text in before):
        raise RuntimeError(f"PDF new contact not readable in text extraction: {source}")
    for original, updated in zip(reader.pages, revised.pages):
        if original.mediabox != updated.mediabox or original.cropbox != updated.cropbox:
            raise RuntimeError(f"PDF page geometry changed: {source}")
    return changes, annotations


def main() -> None:
    cli = argparse.ArgumentParser(description=__doc__)
    group = cli.add_mutually_exclusive_group(required=True)
    group.add_argument("--preview", action="store_true", help="Test conversion in temporary files only")
    group.add_argument("--in-place", action="store_true", help="Convert docs copies only in deployment workspace")
    args = cli.parse_args()

    all_pdfs = sorted(DOWNLOADS.rglob("*.pdf"))
    affected = []
    with tempfile.TemporaryDirectory(prefix="siggear-pdf-contact-") as scratch:
        for index, file in enumerate(all_pdfs):
            target = Path(scratch) / f"revised-{index}.pdf"
            operations, links = patch(file, target)
            if operations:
                if args.in_place:
                    os.replace(target, file)
                affected.append((file.relative_to(ROOT).as_posix(), operations, links))
    print(f"PASS: scanned {len(all_pdfs)} PDF downloads; {len(affected)} contact-only replacements validated")
    print(f"Mode: {'PUBLICATION WORKTREE' if args.in_place else 'PR PREVIEW (sources UNMODIFIED)'}")
    for name, changes, actions in affected:
        print(f"PDF_CONTACT_UPDATED {name} text_ops={changes} links={actions}")
    if not affected:
        print("PASS: no old email remains in searchable PDF download text")


if __name__ == "__main__":
    main()
