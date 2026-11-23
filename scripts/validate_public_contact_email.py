#!/usr/bin/env python3
"""Audit SigGear's live public-contact address in website sources.

Only the website's current public contacts are migrated. An older
FormSubmit activation record outside docs/ is historical evidence,
not proof that the new recipient was activated.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CURRENT = "luffy@siggear.com"
EMAIL = re.compile(r"[\w.%+\-]+@siggear\.com", re.I)
TEXT_EXT = {".md", ".html", ".js", ".css", ".json", ".txt", ".yml", ".yaml", ".xml"}
ACTIVE_DATA = (
    "data/content",
    "data/distribution",
    "data/external-catalogs",
    "data/geo",
    "data/sales",
)
ESSENTIAL = (
    "docs/contact.md",
    "docs/index.md",
    "docs/request-cad-sample-quote.md",
    "docs/assets/javascripts/organization-schema.js",
    "docs/assets/javascripts/inquiry-form.js",
    "README.md",
    "data/sales/public-sales-policy.yml",
    "data/external-catalogs/planetary-gearboxes.yml",
)


def main() -> None:
    all_files = [
        f for f in DOCS.rglob("*")
        if f.is_file() and f.suffix.lower() in TEXT_EXT
    ]
    for folder in ACTIVE_DATA:
        all_files.extend(
            f for f in (ROOT / folder).rglob("*")
            if f.is_file() and f.suffix.lower() in TEXT_EXT
        )
    all_files.append(ROOT / "README.md")
    failures = []
    emails = 0
    for file in sorted(set(all_files)):
        relative = file.relative_to(ROOT).as_posix()
        text = file.read_text(encoding="utf-8", errors="replace")
        for match in EMAIL.finditer(text):
            emails += 1
            if match.group().lower() != CURRENT:
                failures.append(f"{relative}: incorrect published company mailbox {match.group()}")

    for name in ESSENTIAL:
        file = ROOT / name
        if not file.is_file() or CURRENT not in file.read_text(encoding="utf-8"):
            failures.append(f"Missing approved public sales email {CURRENT} in {name}")

    inquiry = (DOCS / "assets/javascripts/inquiry-form.js").read_text(encoding="utf-8")
    if "var ONLINE_DELIVERY_VERIFIED = false;" not in inquiry:
        failures.append("Unverified new FormSubmit recipient must have online POST disabled")
    if f'form.action = "https://formsubmit.co/{CURRENT}"' not in inquiry:
        failures.append("Future FormSubmit destination must point to approved mailbox")
    if f'mailto:{CURRENT}?subject=' not in inquiry:
        failures.append("Engineering brief's safe direct-email recipient is incorrect")

    page = (DOCS / "request-cad-sample-quote.md").read_text(encoding="utf-8")
    if "online FormSubmit option is temporarily paused" not in page:
        failures.append("Public inquiry page falsely advertises unverified FormSubmit delivery")

    if failures:
        print("PUBLIC CONTACT EMAIL AUDIT FAILED")
        for issue in failures:
            print("- " + issue)
        raise SystemExit(1)
    print(f"PASS: {len(all_files)} active public source files, {emails} company email references; all {CURRENT}")
    print("PASS: safe direct-email default; FormSubmit not falsely marked as activated")


if __name__ == "__main__":
    main()
