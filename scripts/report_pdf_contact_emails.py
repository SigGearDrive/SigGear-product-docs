#!/usr/bin/env python3
"""Report company email strings embedded in previously released PDF downloads.

PDFs are revisioned engineering artifacts. A source-page email migration does
NOT rewrite prior PDF editions or their drawings, so flag them separately.
This audit extracts searchable text; rasterized emails may require visual QA.
"""
from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
PUBLISHED = ROOT / "docs/assets/downloads"
PATTERN = re.compile(r"[\w.%+\-]+@siggear\.com", re.I)


def main() -> None:
    pdfs = sorted(PUBLISHED.rglob("*.pdf"))
    findings = []
    failed = []
    for file in pdfs:
        try:
            reader = PdfReader(str(file), strict=False)
            for n, page in enumerate(reader.pages, 1):
                content = page.extract_text(extraction_mode="plain") or ""
                for hit in sorted(set(PATTERN.findall(content))):
                    findings.append((file.relative_to(ROOT).as_posix(), n, hit))
        except Exception as error:
            failed.append((file.relative_to(ROOT).as_posix(), type(error).__name__))
    print(f"Audited PDF download text in {len(pdfs)} existing PDFs")
    for name, page, email in findings:
        print(f"PDF_CONTACT {name} page={page} email={email}")
    print(f"PDF contact strings found: {len(findings)}; PDFs unable to inspect: {len(failed)}")
    for name, err in failed:
        print(f"PDF_TEXT_SCAN_UNAVAILABLE {name} {err}")
    print("NOTE: PDF revisions are not automatically modified by the published HTML email update.")


if __name__ == "__main__":
    main()
