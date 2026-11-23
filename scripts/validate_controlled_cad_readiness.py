#!/usr/bin/env python3
"""Verify controlled CAD is protected without blocking a first inquiry."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTACT = ROOT / "docs/request-cad-sample-quote.md"
PACK = ROOT / "docs/engineering-resources/planetary-gearboxes/candidate-design-in-pack.md"
PACK_JS = ROOT / "docs/assets/javascripts/candidate-design-in-pack.js"

def main():
    contact = CONTACT.read_text(encoding="utf-8")
    pack = PACK.read_text(encoding="utf-8")
    js = PACK_JS.read_text(encoding="utf-8")

    if "mailto:luffy@siggear.com" not in contact or "<form" in contact:
        raise ValueError("Engineering inquiry must not require an online form.")
    if "not mandatory fields or gates for contacting us" not in pack and "not mandatory fields to contact us" not in pack:
        raise ValueError("CAD review inputs must not be first-contact gates.")
    for token in ("Candidate configuration", "Output interface", "Load / duty",
                  "Installation envelope", "controlled CAD"):
        if token.lower() not in pack.lower():
            raise ValueError("Controlled CAD technical boundary lost: " + token)
    if "mailto:luffy@siggear.com?subject=" not in js:
        raise ValueError("Candidate pack inquiry should open direct email.")
    if "sample-validation-workflow/" not in js:
        raise ValueError("Optional technical sample-validation path was broken.")
    print("PASS: direct first contact, optional engineering details, controlled CAD boundary intact")

if __name__ == "__main__":
    main()
