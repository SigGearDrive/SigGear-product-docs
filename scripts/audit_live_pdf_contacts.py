#!/usr/bin/env python3
"""Verify that GitHub Pages actually serves updated emails inside PDF downloads.

The checked-in PDF revisions are preserved. After deployment, the public
downloaded PDF text must be identical to each source's text except the
authorized company-email substitution. This catches stale CDN PDFs, missing
files, corrupted PDF rewrites and accidental spec/text modifications.
"""
from __future__ import annotations

import argparse
import io
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
PDFS = ROOT / "docs/assets/downloads"
SITE = "https://siggeardrive.github.io/SigGear-product-docs/"
OLD = "wangwanrong@siggear.com"
NEW = "luffy@siggear.com"


def pages(file_or_stream) -> list[str]:
    reader = PdfReader(file_or_stream, strict=False)
    return [(page.extract_text(extraction_mode="plain") or "") for page in reader.pages]


def inspect_one(path: Path, original: list[str]) -> tuple[str, int, int]:
    relative = path.relative_to(ROOT / "docs").as_posix()
    url = SITE + quote(relative, safe="/-_.") + "?contact_revision=20261123"
    request = Request(url, headers={"User-Agent": "SigGear-contact-PDF-integrity-audit/1.0"})
    with urlopen(request, timeout=40) as response:
        body = response.read()
        status = response.getcode()
    if status != 200 or not body.startswith(b"%PDF-"):
        raise RuntimeError(f"{relative}: HTTP {status} or not a PDF")
    updated = pages(io.BytesIO(body))
    if len(original) != len(updated):
        raise RuntimeError(f"{relative}: changed PDF page count")
    count = 0
    for n, (src, deployed) in enumerate(zip(original, updated), 1):
        if OLD in deployed:
            raise RuntimeError(f"{relative}, page {n}: previous email still visible")
        if OLD in src:
            if deployed != src.replace(OLD, NEW):
                raise RuntimeError(f"{relative}, page {n}: PDF text changed beyond the approved email")
            count += src.count(OLD)
    return relative, len(updated), count


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--source-only", action="store_true", help="PR preflight without network")
    cli.add_argument("--report", default="site-pdf-contact-audit.json")
    args = cli.parse_args()

    files = sorted(PDFS.rglob("*.pdf"))
    source = {p: pages(str(p)) for p in files}
    impacted = {
        p.relative_to(ROOT / "docs").as_posix(): sum(t.count(OLD) for t in ts)
        for p, ts in source.items() if any(OLD in t for t in ts)
    }
    print(f"PDF source audit: {len(files)} original PDF files, {len(impacted)} requiring contact update")
    if args.source_only:
        return

    passed = []
    failures = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        tasks = {executor.submit(inspect_one, p, source[p]): p for p in files}
        for task in as_completed(tasks):
            path = tasks[task]
            try:
                passed.append(task.result())
            except Exception as exc:
                failures.append({"path": path.relative_to(ROOT).as_posix(), "error": str(exc)})

    validated = sum(n for _, _, n in passed)
    report = {
        "source_pdf_count": len(files),
        "public_pdf_verified": len(passed),
        "legacy_contact_pdf_count": len(impacted),
        "published_old_contact_replacements": validated,
        "failures": failures,
    }
    Path(args.report).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(
        f"PDF live verification: {len(passed)}/{len(files)} valid, "
        f"{validated} previous email occurrences corrected, {len(failures)} failures"
    )
    if failures:
        for issue in failures:
            print("FAILED PDF: " + json.dumps(issue))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
