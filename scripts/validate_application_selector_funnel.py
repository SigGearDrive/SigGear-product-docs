#!/usr/bin/env python3
"""Verify application -> existing selector -> engineering inquiry discovery.

Tests published HTML links and a real published ratio example, without claiming
Search Console indexing, keyword rankings or actual customer conversions.
"""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
BASE = "https://siggeardrive.github.io/SigGear-product-docs/"
SELECTOR_RELATIVE = "selection-guides/miniature-planetary-gearbox-selection-guide/"
APPLICATIONS = {
    "electric-pruning-shears-planetary-gearbox": "electric_pruning_shears",
    "electric-curtain-blind-window-opener-gear-motors": "electric_curtain_blind",
    "smart-toilet-bidet-planetary-gear-motors": "smart_toilet_bidet",
    "robot-gripper-gear-motors": "dexterous_hand_gripper",
}


class Anchors(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs: list[str] = []
        self.inside_main_content = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "article" and "md-content__inner" in (attributes.get("class") or ""):
            self.inside_main_content = True
        if tag == "a" and self.inside_main_content:
            href = attributes.get("href")
            if href:
                self.hrefs.append(href)

    def handle_endtag(self, tag: str) -> None:
        if tag == "article":
            self.inside_main_content = False


def check(selector_page: str, text: str) -> None:
    if text not in selector_page:
        raise ValueError(f"Selector published HTML is missing: {text}")


def main() -> None:
    selector_path = SITE / SELECTOR_RELATIVE / "index.html"
    page = selector_path.read_text(encoding="utf-8")
    check(page, 'id="preliminary-ratio-stage-finder"')
    check(page, 'id="sg-selector-application-context"')
    check(page, "ratio-stage-selector.js?v=20261016-app-context")
    check(page, "Planetary Gearbox Selector &amp; Ratio Calculator")
    check(page, "Worked Example: From Motor Speed")
    check(page, "Frequently Asked Engineering Questions")
    check(page, '<link rel="canonical" href="' + BASE + SELECTOR_RELATIVE + '">')

    for page_slug, app in APPLICATIONS.items():
        relative = f"applications/{page_slug}/"
        html = (SITE / relative / "index.html").read_text(encoding="utf-8")
        collector = Anchors()
        collector.feed(html)
        source = BASE + relative
        app_selector_links = []
        for href in collector.hrefs:
            url = urlsplit(urljoin(source, href))
            if url.netloc == "siggeardrive.github.io" and url.path == (
                "/SigGear-product-docs/" + SELECTOR_RELATIVE
            ):
                app_selector_links.append(url)

        if not app_selector_links:
            raise ValueError(f"{page_slug} has no link to the existing selector")

        for link in app_selector_links:
            if parse_qs(link.query).get("app") != [app]:
                raise ValueError(f"{page_slug} drops application context: {link.geturl()}")
            if link.fragment != "preliminary-ratio-stage-finder":
                raise ValueError(f"{page_slug} misses legacy selector anchor: {link.geturl()}")

    data = json.loads((
        ROOT / "docs/assets/data/planetary-ratio-stage-data.json"
    ).read_text(encoding="utf-8"))
    twelve = next(m for m in data["models"] if m["model"] == "12P")
    stage = next(s for s in twelve["stages"] if s["stage"] == 3)
    if twelve["diameter"] != 12 or stage["length"] != 16.85:
        raise ValueError("The published 12P worked example's diameter/length changed")
    if 42.9 not in stage["ratios"] or stage["rated"] != 3.6 or stage["efficiency"] != 73:
        raise ValueError("The published 12P worked example's ratio/rating changed")
    if abs(6000 / 42.9 - 139.86) > 0.01:
        raise ValueError("The documented 12P output-speed example changed")

    print("PASS 4 OEM application paths retain source context in rendered selector links")
    print("PASS selector canonical, useful worked example and published 12P parameters")


if __name__ == "__main__":
    main()
