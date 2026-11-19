#!/usr/bin/env python3
"""Verify motor PDF quick-download layout, real files and source-revision labels."""
from __future__ import annotations

from collections import Counter
import hashlib
import json
import re
from pypdf import PdfReader
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/engineering-resources/motors/index.md"
HTML = ROOT / "site/engineering-resources/motors/index.html"
FILES = ROOT / "site/assets/downloads/motors"
BASE = "https://siggeardrive.github.io/SigGear-product-docs/engineering-resources/motors/"
SIZES = {8:3,10:5,12:1,14:2,16:8,20:3,22:8,24:2,28:2,32:3}


class MotorHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pdf_links = []
        self.ids = set()
        self.tags = []
    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        self.tags.append((tag,props))
        if "id" in props:
            self.ids.add(props["id"])
        if tag == "a" and "siggear-motor-file" in props.get("class","").split():
            self.pdf_links.append(props)


def check() -> None:
    md = DOC.read_text(encoding="utf-8")
    assert md.count("# DC / BLDC Motor Datasheets") == 1
    assert re.search(r"SigGear supplies DC\s*/\s*BLDC motors", md), "Motor source family identity missing"
    assert "37 motor PDFs" in md
    assert "Draft" in md
    assert "../../custom-engineering/custom-planetary-gearbox.md" in md, "Missing selected-motor integration path"
    assert "<details" in md and "</details>" in md
    assert md.count("siggear-motor-file") == 37, "All 37 direct PDF links must be visible by default"
    assert HTML.is_file(), "MkDocs motor hub not built"
    html = HTML.read_text(encoding="utf-8")
    parsed = MotorHTML()
    parsed.feed(html)
    expected_ids = {"siggear-motor-quick-table","siggear-motor-filter","siggear-motor-results"}
    assert expected_ids.issubset(parsed.ids), f"Missing quick-download controls: {expected_ids - parsed.ids}"
    assert any(tag == "details" for tag,props in parsed.tags), "Engineering cautions must be expandable"
    assert len(parsed.pdf_links) == 37, f"Expected 37 rendered direct PDF links, found {len(parsed.pdf_links)}"
    counter = Counter()
    seen = set()
    for link in parsed.pdf_links:
        dest = urlsplit(urljoin(BASE, link["href"]))
        assert dest.netloc == "siggeardrive.github.io" and "/assets/downloads/motors/" in dest.path,link
        relative = unquote(dest.path).split("/assets/downloads/motors/",1)[-1]
        size = int(relative.split("/",1)[0].replace("mm",""))
        assert relative not in seen, f"Duplicate motor datasheet: {relative}"
        seen.add(relative)
        counter[size] += 1
        path = FILES / relative
        assert path.is_file() and path.stat().st_size > 8000, f"Broken/short file: {path}"
        assert link.get("title","").startswith("Models:"), f"Missing winding/model search tokens: {relative}"
    assert dict(counter) == SIZES, f"Wrong diameter coverage: {dict(counter)}"
    required_new = {
        "20mm/SigGear_20mm_DC_Motor_120108_DraftV1.0.pdf",
        "20mm/SigGear_20mm_DC_Motor_120100_DraftV1.0.pdf",
        "24mm/SigGear_24mm_DC_Motor_090080-240092_DraftV1.0.pdf",
    }
    assert required_new.issubset(seen), f"New source PDFs missing: {sorted(required_new - seen)}"
    new_10mm = {
        "10mm/SigGear_10mm_DC_Motor_Series_01_DraftV1.1.pdf",
        "10mm/SigGear_10mm_DC_Motor_Series_03_DraftV1.1.pdf",
        "10mm/SigGear_10mm_DC_Motor_Series_04_DraftV1.1.pdf",
        "10mm/SigGear_10mm_DC_Motor_HS-1020-Q_SourceGroup_DraftV1.1.pdf",
    }
    assert new_10mm.issubset(seen), f"Refreshed 10 mm PDFs missing: {sorted(new_10mm - seen)}"
    assert "HS-1020-Q" in md and "ambiguous model identifiers" in md, "Unverified 10 mm source identifiers must remain disclosed"
    assert "015124" in md and "015126" in md, "Older and updated Series 04 source labels must be distinguished"
    assert (FILES / "10mm/SigGear_10mm_DC_Motor_Series_02_DraftV1.0.pdf").is_file(), "Legacy Series 02 must be retained"

    assert "HS-2016-Q" in md, "20 mm 120108 must disclose chart/source designation mismatch"
    assert "090080" in md and "240092" in md, "New 24 mm winding range missing"

    source_manifest = ROOT / "data/quality/10mm-dc-motor-datasheet-refresh-2026-11-19.json"
    records = json.loads(source_manifest.read_text(encoding="utf-8"))["records"]
    assert len(records) == 4, "Expected four refreshed 10 mm datasheets"
    for record in records:
        active = "10mm/" + record["new_pdf"]
        assert active in seen, f"Refreshed source not visible in download matrix: {active}"
        path = FILES / active
        assert hashlib.sha256(path.read_bytes()).hexdigest() == record["sha256"], f"Modified source PDF: {active}"
        doc = PdfReader(str(path), strict=False)
        assert len(doc.pages) == 3, f"Expected three legible review pages: {active}"
        first_text = doc.pages[0].extract_text() or ""
        second_text = doc.pages[1].extract_text() or ""
        assert "Draft V1.1" in first_text, f"Draft version lost: {active}"
        assert record["source_chart"] in second_text, f"Missing chart source label: {active}"
        assert record["new_pdf"].endswith("_DraftV1.1.pdf"), f"Uncontrolled filename: {active}"
        if record.get("legacy_pdf"):
            legacy = FILES / "10mm" / record["legacy_pdf"]
            assert legacy.is_file(), f"Legacy public download must be preserved: {legacy}"
    assert "source group has ambiguous model identifiers" in md, "Source code uncertainty must be visible"

    for n in SIZES:
        assert any(id_.startswith(f"{n}-mm-") for id_ in parsed.ids), f"Legacy diameter anchor missing for {n}"
    assert "motor-quick-downloads.js?v=20261118-direct-pdfs" in html
    assert "motor-quick-downloads.css?v=20261118-direct-pdfs" in html
    print("PASS 37 genuine motor PDF buttons, 10 sizes, model/winding search tokens, supplier CTA and legacy anchors")


if __name__ == "__main__":
    check()
