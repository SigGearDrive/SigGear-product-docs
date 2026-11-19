#!/usr/bin/env python3
"""SG-6010HB public-reference PDF and confidential/unmatched CAD release gate.

CAD geometry metadata was inspected manually with OCP and saved as an
independent source audit. This CI check does NOT re-import the 24 MB raw
assembly, which is intentionally not in the public repository.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import yaml
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MODEL = DOCS / "products/robot-joint-actuators/sg6010hb.md"
TECH = DOCS / "engineering-resources/sg6010hb"
PDF_NAME = "SG-6010HB_Public_Reference_Datasheet_Rev0.1.pdf"
PDF = DOCS / "assets/downloads/joint-actuators" / PDF_NAME
AUDIT = ROOT / ".github/joint-drawing-photo-inbox/sg6010hb_exchange_step_intake_20261119.json"
PRODUCT_DATA = ROOT / "data/products/sg-6010hb.yml"
SITE = ROOT / "site"
EXPECTED_SHA = "352c043b6fd11ee869b8ef9c85774fd16d1dba6da63d9ec649789596c236e31b"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    record = json.loads(AUDIT.read_text(encoding="utf-8"))
    source = yaml.safe_load(PRODUCT_DATA.read_text(encoding="utf-8"))
    cfg = source["cad_control"]
    require(source["model"] == "SG-6010HB", "Wrong source model")
    require(cfg["source_step_sha256"] == EXPECTED_SHA, "Changed source STEP SHA")
    require(record["source_sha256"] == EXPECTED_SHA, "Source file audit SHA mismatch")
    require(record["source_bytes"] == 24656102, "Source file audit size mismatch")
    require(record["public_model"] == "SG-6010HB", "Mismatched public product model")
    require(record["assembly_solids"] == 46, "OCP import evidence missing")
    box = record["all_solid_bounding_box_mm"]
    require(72.4 < box["x"] < 72.6 and 34.8 < box["y"] < 35.0,
            "Source geometry audit envelope changed without review")
    require(record["public_cad_release"] is False,
            "Raw internal SG-6010HB CAD must not be auto-released")
    require("HOLD" in record["publication_status"], "Missing geometry release hold")
    require(cfg["public_raw_assembly_step"] is False, "YAML permits raw internal STEP")
    require("hold" in cfg["source_step_geometry_status"], "CAD source not under review")

    # The full assembly cannot silently appear in any publicly published asset.
    for step in DOCS.rglob("*"):
        if step.is_file() and step.suffix.lower() in (".step", ".stp"):
            require(not re.search(r"sg.?6010hb", step.name, re.IGNORECASE),
                    "Unapproved SG-6010HB source CAD publicly packaged: " + str(step))
            if step.stat().st_size == record["source_bytes"]:
                require(hashlib.sha256(step.read_bytes()).hexdigest() != EXPECTED_SHA,
                        "Unapproved SG-6010HB source STEP published under another file name")

    require(PDF.is_file() and PDF.stat().st_size >= 2500,
            "SG-6010HB reference PDF not built")
    raw = PDF.read_bytes()
    require(raw.startswith(b"%PDF-") and b"%%EOF" in raw[-1024:],
            "SG-6010HB reference PDF failed format preflight")
    reader = PdfReader(str(PDF), strict=False)
    require(1 <= len(reader.pages) <= 2, "Unexpected reference datasheet length")
    extracted = " ".join((page.extract_text() or "") for page in reader.pages)
    for marker in ("SG-6010HB", "67.0 mm", "25.57 mm",
                   "6 Nm", "18 Nm", "CAD release hold"):
        require(marker in extracted, "SG-6010HB reference PDF missing: " + marker)

    model_text = MODEL.read_text(encoding="utf-8")
    mech_text = (TECH / "mechanical-interface.md").read_text(encoding="utf-8")
    datasheet_text = (TECH / "datasheet.md").read_text(encoding="utf-8")
    for page_text in (model_text, datasheet_text):
        require(PDF_NAME in page_text, "SG-6010HB lacks direct reference PDF link")
    require("Not publicly released" in model_text,
            "SG-6010HB CAD status not clearly marked")
    require("72.53 mm" in mech_text and "34.86 mm" in mech_text,
            "2D / 3D envelope audit note absent")
    require("configuration-matched" in mech_text.lower(),
            "CAD engineering signoff request missing")
    require(not re.search(r"\]\([^)]*\.st(?:ep|p)(?:\?[^)]*)?\)", model_text, re.I),
            "Unapproved SG-6010HB STEP direct-download link advertised")

    # The public website needs both the generated file and a first-screen link.
    html_file = SITE / "products/robot-joint-actuators/sg6010hb/index.html"
    published_pdf = SITE / "assets/downloads/joint-actuators" / PDF_NAME
    require(html_file.is_file() and published_pdf.is_file(),
            "Built SG-6010HB page or reference PDF not published")
    html = html_file.read_text(encoding="utf-8")
    article = html.split("<article", 1)[-1]
    first_spec = article.find("<table")
    require(first_spec >= 0 and PDF_NAME in article[:first_spec],
            "SG-6010HB PDF must be linked before specifications")
    require(hashlib.sha256(published_pdf.read_bytes()).hexdigest()
            == hashlib.sha256(raw).hexdigest(),
            "Published SG-6010HB PDF differs from generated source")
    print("PASS SG-6010HB PDF, 2D-versus-STEP geometry hold and public CAD release gate")


if __name__ == "__main__":
    main()
