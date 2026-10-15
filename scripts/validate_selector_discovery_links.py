#!/usr/bin/env python3
"""Validate published model-to-selector links after the MkDocs build.

Checks the emitted HTML, not only Markdown source, so fragment/query URL
rewrites cannot silently break the Google-to-product-to-selector journey.
"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BUILT = ROOT / "site"
MODELS = (8, 10, 12, 14, 16, 20, 22, 24, 28, 32, 36, 42)
SITE_ORIGIN = "https://siggeardrive.github.io"
SITE_PREFIX = "/SigGear-product-docs"
SELECTOR_PATH = SITE_PREFIX + "/selection-guides/miniature-planetary-gearbox-selection-guide/"


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
            self.links.append((self.current_href, "".join(self.current_text)))
            self.current_href = None
            self.current_text = []


def main() -> None:
    selector_html = BUILT / "selection-guides/miniature-planetary-gearbox-selection-guide/index.html"
    if not selector_html.exists():
        raise ValueError(f"Selector is not present in the built site: {selector_html}")

    selector_text = selector_html.read_text(encoding="utf-8")
    if 'id="preliminary-ratio-stage-finder"' not in selector_text:
        raise ValueError("Legacy/homepage selector anchor is missing in built HTML.")

    for diameter in MODELS:
        suffix = f"products/planetary-gearboxes/{diameter}p-planetary-gearbox/"
        page = BUILT / suffix / "index.html"
        if not page.exists():
            raise ValueError(f"Missing built {diameter}P model page: {page}")

        collector = AnchorCollector()
        collector.feed(page.read_text(encoding="utf-8"))
        links = [(url, label) for url, label in collector.links
                 if "Open SigGear Planetary Gearbox Selector" in label]
        if len(links) != 1:
            raise ValueError(f"{diameter}P must have exactly one selector CTA, got {len(links)}")

        source_url = SITE_ORIGIN + SITE_PREFIX + "/" + suffix
        destination = urlsplit(urljoin(source_url, links[0][0]))
        if destination.netloc != "siggeardrive.github.io" or destination.path != SELECTOR_PATH:
            raise ValueError(f"{diameter}P selector CTA has a broken destination: {destination}")
        if parse_qs(destination.query).get("max_diameter") != [str(diameter)]:
            raise ValueError(f"{diameter}P diameter hint was not preserved: {destination.query}")
        if destination.fragment != "preliminary-ratio-stage-finder":
            raise ValueError(f"{diameter}P legacy selector anchor missing: {destination.fragment}")

    print("PASS all 12 published model pages link to selector with correct diameter and anchor.")


if __name__ == "__main__":
    main()
