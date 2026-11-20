#!/usr/bin/env python3
"""Preflight published gearhead and motor downloads, plus built HTML link paths.

Validates parseable PDF structure and STEP boundaries, not raster sharpness,
engineering dimensional correctness, customer testing or actual HTTP response.
Run only after assemble_public_cad.py, assemble_motor_pdfs.py and mkdocs build.
"""

from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"
BASE = "https://siggeardrive.github.io/SigGear-product-docs/"
MODEL_SIZES = (8, 10, 12, 14, 16, 20, 22, 24, 28, 32, 36, 42)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def pdf_preflight(path: Path) -> dict:
    require(path.is_file(), f"Missing PDF: {path}")
    require(path.stat().st_size >= 8_000, f"Empty or implausibly short PDF: {path}")
    with path.open("rb") as src:
        require(src.read(5) == b"%PDF-", f"Invalid PDF header: {path}")
        src.seek(max(0, path.stat().st_size - 2048))
        require(b"%%EOF" in src.read(), f"PDF terminator missing: {path}")

    try:
        reader = PdfReader(str(path), strict=False)
        require(not reader.is_encrypted, f"Password-protected public PDF: {path}")
        pages = len(reader.pages)
        require(1 <= pages <= 250, f"Unexpected PDF page count: {path}: {pages}")
        # A first page must have actual page media; 2D drawings may be raster
        # pages without selectable text, so don't reject image-only originals.
        first = reader.pages[0]
        require(
            float(first.mediabox.width) > 50 and float(first.mediabox.height) > 50,
            f"Invalid first-page dimensions: {path}",
        )
        require(
            first.get_contents() is not None or bool(first.get("/Annots")),
            f"Blank PDF first-page content stream: {path}",
        )
    except Exception as exc:
        raise ValueError(f"Unparseable public PDF {path}: {exc}") from exc

    return {"pages": pages, "bytes": path.stat().st_size}


def step_preflight(path: Path, is_full: bool) -> int:
    require(path.is_file(), f"Missing STEP: {path}")
    size = path.stat().st_size
    require(size >= (1_000_000 if is_full else 10_000), f"Empty or short STEP: {path} ({size} bytes)")
    with path.open("rb") as src:
        head = src.read(2048)
        src.seek(max(0, size - 2048))
        tail = src.read()
    require(head.lstrip().startswith(b"ISO-10303-21;"), f"Invalid ISO STEP header: {path}")
    require(b"HEADER;" in head and b"DATA;" in head, f"Incomplete STEP sections: {path}")
    require(b"END-ISO-10303-21;" in tail, f"Incomplete STEP terminator: {path}")
    return size


class Hrefs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.hrefs.append(href)


def check_built_page(path: Path, page_url: str) -> int:
    require(path.is_file(), f"Published HTML page missing: {path}")
    parser = Hrefs()
    parser.feed(path.read_text(encoding="utf-8"))
    checked = 0
    for href in parser.hrefs:
        dest = urlsplit(urljoin(page_url, href))
        if dest.netloc != "siggeardrive.github.io":
            continue
        prefix = "/SigGear-product-docs/assets/downloads/"
        if not dest.path.startswith(prefix):
            continue
        relative = unquote(dest.path.removeprefix("/SigGear-product-docs/"))
        local = SITE / relative
        require(local.is_file(), f"Broken download from {page_url}: {dest.path}")
        require(local.stat().st_size > 1000, f"Empty published download from {page_url}: {dest.path}")
        checked += 1
    return checked


def main() -> None:
    pdf_count = 0
    full_count = 0
    simplified_count = 0
    pdf_pages = 0
    expected_names: set[str] = set()
    for n in MODEL_SIZES:
        slug = f"{n}p"
        model = f"{n}P"
        root = DOCS / "assets/downloads" / slug
        rev = "Rev1.1" if n == 12 else "Rev1.0"

        # A customer must see all four existing model-specific files
        # before technical tables or secondary explanatory links.
        model_path = DOCS / "products/planetary-gearboxes" / f"{slug}-planetary-gearbox.md"
        require(model_path.is_file(), f"Missing product page for {model}")
        model_source = model_path.read_text(encoding="utf-8")
        first_table = model_source.find("| Ø Diameter |")
        require(first_table > 0, f"First-screen specification table missing: {model}")
        above_spec = model_source[:first_table]
        release_names = (
            f"{model}_Planetary_Gearhead_Datasheet_{rev}.pdf",
            f"{model}_2D_Drawing.pdf",
            f"{model}_Full_Assembly.step",
            f"{model}_Public_Simplified_STEP_v1.0_4-Stage.step",
        )
        for filename in release_names:
            require(
                f"../../assets/downloads/{slug}/{filename}){{ .md-button" in above_spec,
                f"Primary download not visible before specifications: {model}: {filename}",
            )
        require(
            "[**Download Simplified 4-Stage STEP · Reference**]" in above_spec,
            f"Stage limitation not explicit on direct simplified STEP: {model}",
        )
        require(
            model_source.count(release_names[-1]) == 1,
            f"Duplicate or missing simplified 4-stage STEP reference: {model}",
        )
        require(
            above_spec.count("{ .md-button") == 4,
            f"Expected four primary model-specific download actions: {model}",
        )
        pdfs = (
            root / f"{model}_Planetary_Gearhead_Datasheet_{rev}.pdf",
            root / f"{model}_2D_Drawing.pdf",
        )
        for path in pdfs:
            data = pdf_preflight(path)
            pdf_count += 1
            pdf_pages += data["pages"]
            expected_names.add(path.name)

        full = root / f"{model}_Full_Assembly.step"
        simplified = root / f"{model}_Public_Simplified_STEP_v1.0_4-Stage.step"
        step_preflight(full, is_full=True)
        step_preflight(simplified, is_full=False)
        full_count += 1
        simplified_count += 1

    manifest = DOCS / "assets/downloads/full-assembly-release-manifest.json"
    require(manifest.is_file(), "Missing published original STEP release manifest")
    data = json.loads(manifest.read_text(encoding="utf-8"))
    releases = data.get("models") or []
    require(len(releases) == 12, f"STEP manifest model count mismatch: {len(releases)}")
    for item in releases:
        path = DOCS / str(item.get("published_path", ""))
        # Manifest-relative release paths start with assets/, not docs/.
        require(path.is_file(), f"Manifest STEP missing: {path}")
        require(item.get("status") == "assembled_and_validated", f"Unvalidated STEP release: {item.get('model')}")
        require(path.stat().st_size == item.get("bytes"), f"STEP release-size mismatch: {path}")

    motor_page = DOCS / "engineering-resources/motors/index.md"
    motor_source = motor_page.read_text(encoding="utf-8")
    motor_links = sorted(set(re.findall(
        r'\]\((\.\./\.\./assets/downloads/motors/[^)\s]+\.pdf)(?:\s+"[^"]*")?\)',
        motor_source,
    )))
    require(len(motor_links) >= 25, f"Unexpectedly few motor datasheets listed: {len(motor_links)}")
    for link in motor_links:
        pdf_preflight((motor_page.parent / link).resolve())

    html_paths = [
        ("engineering-resources/planetary-gearboxes/public-cad-release-v1/", 48),
        ("engineering-resources/planetary-gearboxes/", 36),
        ("engineering-resources/motors/", len(motor_links)),
    ]
    html_paths.extend(
        (f"products/planetary-gearboxes/{n}p-planetary-gearbox/", 4)
        for n in MODEL_SIZES
    )
    html_paths.extend(
        (f"applications/{p.stem}/", 3)
        for p in (DOCS / "applications").glob("*.md")
        if p.stem not in {"index", "planetary-gearbox-application-families"}
    )
    # Protect the refreshed, legacy-URL engineering entrypoints. Their
    # published first-screen links must be actual model-specific files rather
    # than marketing copy, a form gate or an empty navigation-only page.
    motor_integration = (DOCS / "custom-engineering/motor-gearbox-integration.md").read_text(encoding="utf-8")
    family_guide = (DOCS / "applications/planetary-gearbox-application-families.md").read_text(encoding="utf-8")
    require(motor_integration.index("## Direct Model Files") < motor_integration.index("## Start With"),
            "Existing-motor page must show direct model files before general copy")
    require(family_guide.index("## Application Mechanisms") < family_guide.index("## If the Published"),
            "Mechanism guide must show real model files before the handoff")
    for size in MODEL_SIZES:
        token = f"{size}P_Planetary_Gearhead_Datasheet_"
        require(token in motor_integration, f"Motor matching page missing {size}P datasheet download")
        require(f"{size}P_2D_Drawing.pdf" in motor_integration,
                f"Motor matching page missing {size}P 2D drawing")
        require(f"{size}P_Full_Assembly.step" in motor_integration,
                f"Motor matching page missing {size}P full STEP")
    for token in ("[**↓ PDF**]", "[**↓ 2D**]", "[**↓ Full STEP**]"):
        require(family_guide.count(token) == 6,
                f"Mechanism guide must contain six exact model files for {token}")
    html_paths.extend([
        ("custom-engineering/motor-gearbox-integration/", 36),
        ("applications/planetary-gearbox-application-families/", 18),
    ])

    # The legacy planetary Engineering Resources index now must expose the
    # same real files as the protected central download page, not only 2D.
    planetary_resource_index = (
        DOCS / "engineering-resources/planetary-gearboxes/index.md"
    ).read_text(encoding="utf-8")
    require(
        planetary_resource_index.index("## 12 Models") <
        planetary_resource_index.index("## Standard Reference"),
        "Planetary Engineering Resources must show model files before prose",
    )
    for size in MODEL_SIZES:
        for token in (
            f"{size}P_Planetary_Gearhead_Datasheet_",
            f"{size}P_2D_Drawing.pdf",
            f"{size}P_Full_Assembly.step",
        ):
            require(token in planetary_resource_index,
                    f"Planetary resources missing direct {size}P asset: {token}")

    # The indexed legacy selector keeps its working calculator + deep-link
    # anchor, while first-screen model files must be immediate direct links.
    legacy_selector_path = DOCS / "selection-guides/miniature-planetary-gearbox-selection-guide.md"
    legacy_selector = legacy_selector_path.read_text(encoding="utf-8")
    require(
        legacy_selector.index("## Browse by Diameter Before Ratio Selection") <
        legacy_selector.index("## SigGear Planetary Gearbox Selector"),
        "Legacy selector must present real file downloads before the calculator",
    )
    for expected_id in (
        "preliminary-ratio-stage-finder",
        'id="siggear-ratio-stage-selector"',
        'id="sg-selector-motor-speed"',
        'id="sg-selector-output-speed"',
        'id="sg-ratio-stage-results"',
    ):
        require(expected_id in legacy_selector, f"Legacy calculator/deep-link missing {expected_id}")
    for size in MODEL_SIZES:
        for name in (
            f"{size}P_Planetary_Gearhead_Datasheet_",
            f"{size}P_2D_Drawing.pdf",
            f"{size}P_Full_Assembly.step",
        ):
            require(name in legacy_selector, f"Legacy selector missing direct {size}P file: {name}")
    require("motor- and configuration-dependent" in legacy_selector,
            "Legacy selector must not restore a universal gearbox input speed cap")
    html_paths.append(("selection-guides/miniature-planetary-gearbox-selection-guide/", 36))

    links_checked = 0
    for rel, min_download_links in html_paths:
        page_url = BASE + rel
        rendered = SITE / rel / "index.html"
        count = check_built_page(rendered, page_url)
        require(count >= min_download_links, f"Too few direct file links on {rel}: {count}")
        links_checked += count

    print(
        "PASS 12 planetary models: "
        f"{pdf_count} parseable PDFs ({pdf_pages} pages), "
        f"{full_count} full assembly STEP + {simplified_count} simplified STEP; "
        f"{len(motor_links)} motor-only PDFs; "
        f"{links_checked} rendered download hrefs resolved (four above-fold links per model)"
    )
    print("NOTE This verifies readable PDF structure, not raster image resolution or engineering approval.")


if __name__ == "__main__":
    main()
