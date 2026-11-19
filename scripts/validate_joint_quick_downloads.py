#!/usr/bin/env python3
"""Verify the six-model first-screen PDF/CAD links in built GitHub Pages.

Covers links and variant visibility, not manufacturing approval of CAD geometry.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
BASE = "https://siggeardrive.github.io/SigGear-product-docs/"
ASSETS = "assets/downloads/"
HUB = "engineering-resources/robot-joint-actuators/quick-downloads/"
PRODUCTS = {
    "SG-6010C": "products/robot-joint-actuators/sg6010c/",
    "SG-6010D": "products/robot-joint-actuators/sg6010d/",
    "SG-8021": "products/robot-joint-actuators/sg8021/",
    "CPM-78-39": "products/cycloidal-joint-modules/cpm78-39/",
    "CPM-80-25": "products/cycloidal-joint-modules/cpm80-25/",
    "CPM-100-25": "products/cycloidal-joint-modules/cpm100-25/",
}
PDFS = {
    model: "joint-actuators/" + model + "_Public_Reference_Datasheet_Rev0.1.pdf"
    for model in PRODUCTS
}
ORIGINAL_CAD = {
    "SG-6010C": ["SG-6010C_Original_Full_Assembly_20261118.step"],
    "SG-6010D": ["SG-6010D_Original_Full_Assembly_20261118.step"],
    "SG-8021": ["SG-8021_Driver_Version_Original_Full_Assembly_20261118.step"],
    "CPM-78-39": ["CPM-78-39_Original_Full_Assembly_20261118.step"],
    "CPM-80-25": [
        "CPM-80-25_Original_Full_Assembly_No_Driver_20261118.step",
        "CPM-80-25_Original_Full_Assembly_Integrated_Driver_20261118.step",
    ],
    "CPM-100-25": [
        "CPM-100-25_Original_Full_Assembly_No_Driver_20261118.step",
        "CPM-100-25D_Dual_Encoder_Driver_Original_Full_Assembly_20261118.step",
    ],
}
SIMPLIFIED = {
    "SG-6010C": "sg6010c/SG-6010C_Public_Simplified_STEP_v1.0.step",
    "CPM-80-25 NO DRIVER": "cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_No_Driver.step",
    "CPM-80-25 DRIVER": "cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_Integrated_Driver.step",
}

DRAWINGS = {
    "SG-6010D": ["SG-6010D_2D_Assembly_Drawing.pdf"],
    "CPM-80-25": [
        "CPM-80-25_2D_No_Driver_29p7mm.pdf",
        "CPM-80-25_2D_Integrated_Driver_41p2mm.pdf",
    ],
    "CPM-100-25": ["CPM-100-25D_2D_Dual_Encoder_Driver_48mm.pdf"],
}

class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
    def handle_starttag(self, tag, attrs) -> None:
        if tag.lower() == "a":
            data = dict(attrs)
            if data.get("href"): self.hrefs.append(data["href"])

def page(path: str) -> str:
    file = SITE / path / "index.html"
    if not file.is_file():
        raise ValueError("Published page missing: " + str(file))
    return file.read_text(encoding="utf-8")

def links(html: str, relative_page: str) -> set[str]:
    parser = LinkCollector()
    parser.feed(html)
    return {urlsplit(urljoin(BASE + relative_page, href)).path for href in parser.hrefs}

def asset(model: str, relative_file: str, expected_links: set[str]) -> None:
    expected_path = "/SigGear-product-docs/" + ASSETS + relative_file
    if expected_path not in expected_links:
        raise ValueError(model + " missing direct download: " + expected_path)
    path = SITE / ASSETS / relative_file
    if not path.is_file():
        raise ValueError(model + " published file 404: " + str(path))
    if path.suffix.lower() == ".pdf":
        with path.open("rb") as f:
            if not f.read(5) == b"%PDF-": raise ValueError("Invalid PDF: " + str(path))
    elif path.suffix.lower() == ".step":
        with path.open("rb") as f:
            if not f.read(14).startswith(b"ISO-10303-21;"):
                raise ValueError("Invalid STEP: " + str(path))
    else:
        raise ValueError("Unexpected release type: " + str(path))

def main() -> None:
    hub = page(HUB)
    article = hub.split("<article",1)[-1]
    first_table = re.search(r"<table\b[^>]*>(.*?)</table>", article, re.S | re.I)
    if not first_table:
        raise ValueError("No first-screen joint download matrix")
    if 'class="siggear-joint-downloads"' not in article:
        raise ValueError("The six-model matrix must expose the responsive download wrapper")
    th_count = len(re.findall(r"<th\b",first_table.group(1),re.I))
    if th_count != 4:
        raise ValueError("Expected four-column download matrix (specs, datasheet, 2D, STEP); got " + str(th_count))
    before_fold = article.split("<details",1)[0]
    if "Original Full STEP" not in before_fold:
        raise ValueError("Full STEP must be visible before optional detail panel")
    hub_links = links(hub,HUB)
    for model, product_path in PRODUCTS.items():
        html = page(product_path)
        page_links = links(html,product_path)
        if model not in html:
            raise ValueError("Wrong product page: " + model)
        pdf = PDFS[model]
        asset(model,pdf,hub_links)
        asset(model,pdf,page_links)
        asset(model,pdf,links(before_fold,HUB))
        for filename in ORIGINAL_CAD[model]:
            relative_file = "joint-actuators/" + filename
            asset(model,relative_file,hub_links)
            asset(model,relative_file,page_links)
            asset(model,relative_file,links(before_fold,HUB))
        for filename in DRAWINGS.get(model, []):
            relative_file = "joint-actuators/" + filename
            asset(model, relative_file, hub_links)
            asset(model, relative_file, page_links)
            asset(model, relative_file, links(before_fold, HUB))
        body = html.split("<article",1)[-1]
        pdf_pos = body.index(pdf) if pdf in body else -1
        image_pos = body.find("siggear-joint-media")
        if pdf_pos < 0 or (image_pos >= 0 and pdf_pos > image_pos):
            raise ValueError(model + " PDF link must precede product photos")
        if model in ("CPM-80-25","CPM-100-25") and len(ORIGINAL_CAD[model]) != 2:
            raise ValueError("Driver/encoder variants must not be conflated")
        print("PASS",model,"PDF +",len(ORIGINAL_CAD[model]),"original STEP variants")
    for label,relative in SIMPLIFIED.items():
        asset(label,relative,hub_links)
    if "No downloadable STEP is currently approved" in hub:
        raise ValueError("Download hub incorrectly lists released CAD as unavailable")
    if "SG2368B cross-reference pending" not in first_table.group(1) or "SG-6010HB" in first_table.group(1):
        raise ValueError("Unverified model-code drawing or SG-6010HB must not be presented as released")
    # Both family overview pages must expose direct files, not only model links.
    family_models = {
        "products/robot-joint-actuators/": ("SG-6010C", "SG-6010D", "SG-8021"),
        "products/cycloidal-joint-modules/": ("CPM-78-39", "CPM-80-25", "CPM-100-25"),
    }
    for family_path, models in family_models.items():
        family_html = page(family_path)
        family_article = family_html.split("<article", 1)[-1]
        if 'class="siggear-joint-downloads"' not in family_article:
            raise ValueError("Family page missing responsive download wrapper: " + family_path)
        family_table = re.search(r"<table\\b[^>]*>(.*?)</table>", family_article, re.S | re.I)
        if not family_table:
            raise ValueError("Family page missing direct-download matrix: " + family_path)
        family_section = family_table.group(0)
        if len(re.findall(r"<th\\b", family_section, re.I)) != 4:
            raise ValueError("Family page table must have four columns: " + family_path)
        if len(re.findall(r"<tr\\b", family_section, re.I)) != 4:
            raise ValueError("Family table must contain exactly three models: " + family_path)
        family_links = links(family_section, family_path)
        for model in models:
            if model not in family_section:
                raise ValueError("Model absent from family table: " + model)
            asset(model, PDFS[model], family_links)
            for name in ORIGINAL_CAD[model]:
                asset(model, "joint-actuators/" + name, family_links)
            for name in DRAWINGS.get(model, []):
                asset(model, "joint-actuators/" + name, family_links)
        print("PASS family overview", family_path, "three models, direct PDF/2D/STEP")

    stylesheet = SITE / "assets/stylesheets/joint-product-quick.css"
    if not stylesheet.is_file():
        raise ValueError("Joint mobile presentation CSS missing")
    css = stylesheet.read_text(encoding="utf-8")
    if "@media (max-width: 52rem)" not in css or 'content: "2D drawing";' not in css:
        raise ValueError("Mobile download cards or 2D labels missing")
    print("PASS six product pages, responsive download hub, two family matrices, 6 PDF datasheets, 4 2D PDFs and 8 full STEP variants")

if __name__ == "__main__":
    main()
