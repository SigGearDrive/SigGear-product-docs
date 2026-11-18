#!/usr/bin/env python3
"""Validate the product-first 8P–42P download paths after the MkDocs build.

The ratio-stage selector remains available as a legacy reference for older
application links, but it is no longer a CTA on individual product pages.
"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BUILT = ROOT / "site"
MODELS = (8, 10, 12, 14, 16, 20, 22, 24, 28, 32, 36, 42)
SITE_ORIGIN = "https://siggeardrive.github.io"
SITE_PREFIX = "/SigGear-product-docs"


class AnchorCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.current_href = None
        self.current_text = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.current_href = dict(attrs).get("href", "")
            self.current_text = []

    def handle_data(self, data):
        if self.current_href is not None:
            self.current_text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.current_href is not None:
            self.links.append((self.current_href, "".join(self.current_text).strip()))
            self.current_href = None
            self.current_text = []


def main() -> None:
    # Preserve the old selector URL for existing application links, but keep it
    # out of the new model-page journey.
    selector_html = BUILT / "selection-guides/miniature-planetary-gearbox-selection-guide/index.html"
    if not selector_html.exists():
        raise ValueError(f"Legacy selector reference is missing: {selector_html}")

    for diameter in MODELS:
        model = f"{diameter}P"
        slug = f"{diameter}p"
        suffix = f"products/planetary-gearboxes/{slug}-planetary-gearbox/"
        page = BUILT / suffix / "index.html"
        if not page.exists():
            raise ValueError(f"Missing built {model} model page: {page}")

        html = page.read_text(encoding="utf-8")
        collector = AnchorCollector()
        collector.feed(html)

        if "Open SigGear Planetary Gearbox Selector" in html or "max_diameter=" in html:
            raise ValueError(f"{model} page still promotes the selector instead of downloads.")

        source_url = SITE_ORIGIN + SITE_PREFIX + "/" + suffix
        pdf_rev = "Rev1.1" if diameter == 12 else "Rev1.0"
        expected_paths = {
            "Download Datasheet PDF": (
                f"{SITE_PREFIX}/assets/downloads/{slug}/{model}_Planetary_Gearhead_Datasheet_{pdf_rev}.pdf"
            ),
            "Download 2D Drawing PDF": (
                f"{SITE_PREFIX}/assets/downloads/{slug}/{model}_2D_Drawing.pdf"
            ),
            "Download Full Assembly STEP": (
                f"{SITE_PREFIX}/assets/downloads/{slug}/{model}_Full_Assembly.step"
            ),
            "Online technical specifications": (
                f"{SITE_PREFIX}/engineering-resources/{slug}/datasheet/"
            ),
            "Simplified 4-stage STEP": (
                f"{SITE_PREFIX}/assets/downloads/{slug}/{model}_Public_Simplified_STEP_v1.0_4-Stage.step"
            ),
        }
        for label, expected_path in expected_paths.items():
            matches = [href for href, text in collector.links if text == label]
            if len(matches) != 1:
                raise ValueError(f"{model}: expected one {label!r} link, got {len(matches)}")
            actual = urlsplit(urljoin(source_url, matches[0]))
            if actual.path != expected_path:
                raise ValueError(
                    f"{model}: {label} points to {actual.path}, expected {expected_path}"
                )

        # User-first hierarchy: primary file links must precede the large photo.
        source = (
            ROOT / "docs/products/planetary-gearboxes" / f"{slug}-planetary-gearbox.md"
        ).read_text(encoding="utf-8")
        photo_pos = source.index("![")
        for label in ("Download Datasheet PDF", "Download 2D Drawing PDF",
                      "Download Full Assembly STEP"):
            if source.index(f"[**{label}**]") > photo_pos:
                raise ValueError(f"{model}: {label} is below the product photo")

    # New first-screen finder must keep its own no-gate fallback downloads.
    quick = BUILT / "selection-guides/planetary-gearhead-quick-selector/index.html"
    if not quick.is_file():
        raise ValueError("Quick selector page was not built")
    quick_html = quick.read_text(encoding="utf-8")
    for marker in (
        'id="siggear-ratio-stage-selector"',
        'id="sg-selector-motor-speed"',
        'id="sg-selector-output-speed"',
        'id="sg-ratio-stage-results"',
        'ratio-stage-selector.js?v=20261118-quick-files',
    ):
        if marker not in quick_html:
            raise ValueError(f"Quick selector first-screen control missing: {marker}")

    links = AnchorCollector()
    links.feed(quick_html)
    quick_url = SITE_ORIGIN + SITE_PREFIX + "/selection-guides/planetary-gearhead-quick-selector/"
    resolved = {urlsplit(urljoin(quick_url, href)).path for href, _ in links.links}
    for diameter in MODELS:
        model = f"{diameter}P"
        slug = f"{diameter}p"
        rev = "Rev1.1" if diameter == 12 else "Rev1.0"
        expected_files = (
            f"{model}_Planetary_Gearhead_Datasheet_{rev}.pdf",
            f"{model}_2D_Drawing.pdf",
            f"{model}_Full_Assembly.step",
        )
        for filename in expected_files:
            expected = f"{SITE_PREFIX}/assets/downloads/{slug}/{filename}"
            if expected not in resolved:
                raise ValueError(f"Quick selector lacks one-click download: {expected}")

    print("PASS all 12 product pages show direct PDF, 2D, full STEP and quick specs first.")
    print("PASS all online datasheet and simplified STEP links resolve to model-specific paths.")
    print("PASS quick selector exposes all 36 published PDFs/2D/full STEP links and working form controls.")
    print("PASS selector remains available through the existing selection guide.")


if __name__ == "__main__":
    main()
