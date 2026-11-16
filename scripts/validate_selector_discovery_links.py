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

        if "2D drawing PDF" not in html or "Full assembly STEP" not in html:
            raise ValueError(f"{model} page is missing its 2D / full assembly release status.")
        if "Open SigGear Planetary Gearbox Selector" in html or "max_diameter=" in html:
            raise ValueError(f"{model} page still promotes the selector instead of downloads.")

        source_url = SITE_ORIGIN + SITE_PREFIX + "/" + suffix
        datasheets = [(href, label) for href, label in collector.links if label == f"Open {model} datasheet"]
        steps = [(href, label) for href, label in collector.links if label == "Download 4-stage reference"]
        if len(datasheets) != 1:
            raise ValueError(f"{model} must have exactly one online datasheet link, got {len(datasheets)}")
        if len(steps) != 1:
            raise ValueError(f"{model} must have exactly one current simplified STEP link, got {len(steps)}")

        datasheet = urlsplit(urljoin(source_url, datasheets[0][0]))
        expected_datasheet = f"{SITE_PREFIX}/engineering-resources/{slug}/datasheet/"
        if datasheet.path != expected_datasheet:
            raise ValueError(f"{model} datasheet link is broken: {datasheet.path}")

        step = urlsplit(urljoin(source_url, steps[0][0]))
        expected_step = f"{SITE_PREFIX}/assets/downloads/{slug}/{model}_Public_Simplified_STEP_v1.0_4-Stage.step"
        if step.path != expected_step:
            raise ValueError(f"{model} simplified STEP link is broken: {step.path}")

    print("PASS all 12 model pages expose direct datasheet and STEP links without selector CTAs.")
    print("PASS 2D drawing and full assembly STEP release status is visible for all 12 models.")
    print("PASS legacy selector remains available for existing application links.")


if __name__ == "__main__":
    main()
