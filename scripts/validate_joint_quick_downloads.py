#!/usr/bin/env python3
"""Verify the six-model first-screen PDF/STEP links in built GitHub Pages.

Covers links and variant visibility, not manufacturing approval of STEP geometry.
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

MODEL_SIMPLIFIED = {
    "SG-6010C": ["sg6010c/SG-6010C_Public_Simplified_STEP_v1.0.step"],
    "CPM-80-25": [
        "cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_No_Driver.step",
        "cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_Integrated_Driver.step",
    ],
}
MANIFEST_ROWS = {
    "SG-6010C": 4, "SG-6010D": 3, "SG-8021": 3,
    "CPM-78-39": 3, "CPM-80-25": 7, "CPM-100-25": 5,
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
        # The model-level file manifest must come before specs, renders and
        # hidden extra details. Never hide a released original or simplified
        # download behind navigation or a collapsed disclosure.
        if '<h2 id="download-files">' not in body:
            raise ValueError("Model page missing download heading: " + model)
        wrapper = re.search(
            r'<div class="siggear-joint-model-files"[^>]*>(.*?)</div>', body, re.S | re.I
        )
        if not wrapper:
            raise ValueError("Model page missing visible file manifest: " + model)
        manifest_html = wrapper.group(1)
        manifest_table = re.search(r"<table\b[^>]*>(.*?)</table>", manifest_html, re.S | re.I)
        if not manifest_table:
            raise ValueError("Model file manifest does not render as table: " + model)
        table_html = manifest_table.group(0)
        if len(re.findall(r"<th\b",table_html,re.I)) != 3:
            raise ValueError("Model manifest must be three columns: " + model)
        count = len(re.findall(r"<tr\b",table_html,re.I)) - 1
        if count != MANIFEST_ROWS[model]:
            raise ValueError("Wrong model manifest row count: " + model + " " + str(count))
        if body.index('class="siggear-joint-model-files"') > body.index("<table"):
            raise ValueError("Model file manifest must be the first specification table: " + model)
        if "<details" in body.split('class="siggear-joint-model-files"',1)[0]:
            raise ValueError("Model files are hidden in collapsed disclosure: " + model)
        manifest_links = links(table_html,product_path)
        expected_direct = []
        expected_direct.append(PDFS[model])
        expected_direct += ["joint-actuators/" + filename for filename in ORIGINAL_CAD[model]]
        expected_direct += ["joint-actuators/" + filename for filename in DRAWINGS.get(model,[])]
        expected_direct += MODEL_SIMPLIFIED.get(model,[])
        for item in expected_direct:
            asset(model,item,manifest_links)
        released = sorted(x for x in manifest_links if "/assets/downloads/" in x)
        if len(released) != len(expected_direct):
            raise ValueError("Wrong or duplicate model download targets: " + model)
        print("PASS direct product file manifest",model,"files",len(released))

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
    # The older joint selection guide must present real model assets in its
    # first specification table, not ten generic navigation buttons before
    # any usable file. Preserve the exact approved variants from the hub.
    selection_path = "selection-guides/robot-joint-actuator-selection-guide/"
    selection_html = page(selection_path)
    selection_body = selection_html.split("<article", 1)[-1]
    if 'class="siggear-joint-downloads"' not in selection_body:
        raise ValueError("Robot joint selection page missing responsive file matrix")
    selection_table = re.search(r"<table\b[^>]*>(.*?)</table>", selection_body, re.S | re.I)
    if not selection_table:
        raise ValueError("Robot joint selection page missing first-screen file table")
    selection_fragment = selection_table.group(0)
    if len(re.findall(r"<th\b", selection_fragment, re.I)) != 4:
        raise ValueError("Robot joint selection table must have four file columns")
    if len(re.findall(r"<tr\b", selection_fragment, re.I)) != 7:
        raise ValueError("Robot joint selection table must list exactly six released models")
    if selection_body.find('class="siggear-joint-downloads"') > selection_body.find('<h2 id="robot-joint-reducer-specifications-to-compare">'):
        raise ValueError("Joint model download matrix must precede sizing prose")
    selection_links = links(selection_fragment, selection_path)
    for model in PRODUCTS:
        if model not in selection_fragment:
            raise ValueError("Joint selection guide missing model: " + model)
        asset(model, PDFS[model], selection_links)
        for name in ORIGINAL_CAD[model]:
            asset(model, "joint-actuators/" + name, selection_links)
        for name in DRAWINGS.get(model, []):
            asset(model, "joint-actuators/" + name, selection_links)
    if "SG2368B cross-reference pending" not in selection_fragment:
        raise ValueError("Pending CPM-78-39 drawing must not be misrepresented")
    if "SG-8021 STEP is driver-equipped" not in selection_body:
        raise ValueError("SG-8021 driver-equipped STEP variant warning missing")
    print("PASS joint sizing guide: six exact PDF / 2D / STEP reference model downloads")

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
        family_table = re.search(r"<table\b[^>]*>(.*?)</table>", family_article, re.S | re.I)
        if not family_table:
            raise ValueError("Family page missing direct-download matrix: " + family_path)
        family_section = family_table.group(0)
        if len(re.findall(r"<th\b", family_section, re.I)) != 4:
            raise ValueError("Family page table must have four columns: " + family_path)
        if len(re.findall(r"<tr\b", family_section, re.I)) != 4:
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

    # Engineering Center is a primary entry for Google and direct product
    # inquiries. It must expose exactly the verified six-model file list
    # rather than stale generic file-on-request copy.
    center_path = "engineering-center/"
    center_html = page(center_path)
    center_body = center_html.split("<article", 1)[-1]
    a = center_body.find('<h2 id="robot-joint-actuator-downloads">')
    b = center_body.find('<h2 id="planetary-gearbox-engineering-files">', a)
    if a < 0 or b <= a:
        raise ValueError("Engineering Center missing direct-download headings")
    joint_section = center_body[a:b]
    if 'class="siggear-joint-downloads"' not in joint_section:
        raise ValueError("Engineering Center mobile model matrix missing")
    center_table = re.search(r"<table\b[^>]*>(.*?)</table>", joint_section, re.S | re.I)
    if not center_table:
        raise ValueError("Engineering Center has no joint direct-download table")
    center_fragment = center_table.group(0)
    if len(re.findall(r"<th\b", center_fragment, re.I)) != 4:
        raise ValueError("Engineering Center table must contain four download columns")
    if len(re.findall(r"<tr\b", center_fragment, re.I)) != 7:
        raise ValueError("Engineering Center must list six standard joint models")
    center_table_links = links(center_fragment, center_path)
    for model in PRODUCTS:
        if model not in center_fragment:
            raise ValueError("Missing Engineering Center row: " + model)
        asset(model, PDFS[model], center_table_links)
        for name in ORIGINAL_CAD[model]:
            asset(model, "joint-actuators/" + name, center_table_links)
        for name in DRAWINGS.get(model, []):
            asset(model, "joint-actuators/" + name, center_table_links)
    hb_name = "SG-6010HB_Public_Reference_Datasheet_Rev0.1.pdf"
    asset("SG-6010HB", "joint-actuators/" + hb_name, links(joint_section, center_path))
    if "No SG-6010HB STEP is approved for public release" not in joint_section:
        raise ValueError("Engineering Center lacks SG-6010HB STEP release hold")
    if "SG2908B" in joint_section:
        raise ValueError("Internal source label leaked in Engineering Center")
    center_before_tasks = center_body.split('<h2 id="start-by-what-you-need-to-do">', 1)[0]
    if "robot-joint-actuators/quick-downloads/" not in center_before_tasks:
        raise ValueError("Engineering Center joint quick-download button not visible")
    # Prevent a stale in-page jump from surviving after a section rename.
    if 'href="#robot-joint-actuator-downloads"' not in center_body:
        raise ValueError("Engineering Center task index must jump to the live joint downloads section")
    if 'href="#public-engineering-packs"' in center_body:
        raise ValueError("Engineering Center contains deleted Public Engineering Packs anchor")
    if "Planetary Gearbox STEP Library" not in center_body:
        raise ValueError("Engineering Center must expose the planetary gearbox STEP library")

    # Motor engineering discovery: each of the ten live diameter anchors
    # must remain accessible from Engineering Center. The model-specific PDFs
    # are published in the searchable motor library, not repackaged here.
    motor_group_ids = (
        "8-mm-dc-micromotors",
        "10-mm-dc-motors",
        "12-mm-coreless-bldc-motor",
        "14-mm-dc-motors",
        "16-mm-dc-motors",
        "20-mm-bldc-motor",
        "22-mm-dc-motors",
        "24-mm-bldc-motor",
        "28-mm-dc-motors",
        "32-mm-dc-motors",
    )
    motor_html = page("engineering-resources/motors/")
    motor_article = motor_html.split("<article", 1)[-1]
    motor_section_start = center_body.find('<h2 id="motor-datasheets-by-diameter">')
    release_section_start = center_body.find('<h2 id="public-vs-configuration-specific-documentation">')
    if motor_section_start < 0 or release_section_start <= motor_section_start:
        raise ValueError("Engineering Center lacks the public motor library index")
    motor_section = center_body[motor_section_start:release_section_start]
    if "37 published DC / BLDC motor PDFs" not in motor_section:
        raise ValueError("Engineering Center motor library count or scope missing")
    if "Draft / source review" not in motor_section:
        raise ValueError("Motor Draft source warning must remain visible")
    for group_id in motor_group_ids:
        if f'id="{group_id}"' not in motor_article:
            raise ValueError("Motor download target anchor missing: " + group_id)
        if "engineering-resources/motors/#" + group_id not in motor_section:
            raise ValueError("Engineering Center does not link motor diameter: " + group_id)
    if "engineering-resources/motors/" not in center_before_tasks:
        raise ValueError("Motor Datasheets must be visible before task table")
    published_motor_pdfs = set(re.findall(
        r'href="[^"]*/assets/downloads/motors/[^"]+\.pdf"', motor_article, re.I
    ))
    if len(published_motor_pdfs) != 37:
        raise ValueError("Motor library does not expose 37 distinct PDF links: " +
                         str(len(published_motor_pdfs)))
    print("PASS Engineering Center: 10 motor diameter deep-links to 37 published PDFs, Draft scope retained")

    print("PASS Engineering Center: six standard joint models, 18 direct files + SG-6010HB reference PDF")

    stylesheet = SITE / "assets/stylesheets/joint-product-quick.css"
    if not stylesheet.is_file():
        raise ValueError("Joint mobile presentation CSS missing")
    css = stylesheet.read_text(encoding="utf-8")
    if "@media (max-width: 52rem)" not in css or 'content: "2D drawing";' not in css:
        raise ValueError("Mobile download cards or 2D labels missing")
    if '.siggear-joint-model-files' not in css or 'content: "Direct download";' not in css:
        raise ValueError("Model-level responsive download manifest styles missing")
    print("PASS six first-screen product manifests, 21 direct files, responsive hub and family matrices")

if __name__ == "__main__":
    main()
