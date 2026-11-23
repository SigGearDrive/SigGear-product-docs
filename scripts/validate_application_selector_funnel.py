#!/usr/bin/env python3
"""Validate application -> selector -> engineering inquiry discovery paths.

The site now uses the current Planetary Gearhead Quick Selector as the primary
route while keeping the legacy selector available for historical URLs. This
validator accepts either route, but still requires application context, model
links, public engineering files and an inquiry path.
"""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
BASE = "https://siggeardrive.github.io/SigGear-product-docs/"

SELECTOR_PATHS = {
    "/SigGear-product-docs/selection-guides/planetary-gearhead-quick-selector/",
    "/SigGear-product-docs/selection-guides/miniature-planetary-gearbox-selection-guide/",
}

APPLICATIONS = {
    "electric-pruning-shears-planetary-gearbox": "electric_pruning_shears",
    "electric-curtain-blind-window-opener-gear-motors": "electric_curtain_blind",
    "smart-toilet-bidet-planetary-gear-motors": "smart_toilet_bidet",
    "robot-gripper-gear-motors": "dexterous_hand_gripper",
}

PRIORITY_APPLICATION_MODEL_PATHS = {
    "electric-pruning-shears-planetary-gearbox": ("32p", "36p", "42p"),
    "electric-curtain-blind-window-opener-gear-motors": ("16p", "20p", "22p"),
    "robot-gripper-gear-motors": ("8p", "10p", "12p", "14p", "16p"),
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


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    # At least one current/legacy selector page must build with the expected form.
    selector_pages = [
        SITE / "selection-guides/planetary-gearhead-quick-selector/index.html",
        SITE / "selection-guides/miniature-planetary-gearbox-selection-guide/index.html",
    ]
    built_selectors = [p for p in selector_pages if p.exists()]
    require(bool(built_selectors), "No planetary selector page was built")
    require(
        any('id="siggear-ratio-stage-selector"' in p.read_text(encoding="utf-8")
            for p in built_selectors),
        "Built selector pages are missing the ratio-stage form",
    )

    for page_slug, app in APPLICATIONS.items():
        relative = f"applications/{page_slug}/"
        page_path = SITE / relative / "index.html"
        require(page_path.exists(), f"Missing rendered application page: {page_slug}")

        html = page_path.read_text(encoding="utf-8")
        collector = Anchors()
        collector.feed(html)
        source = BASE + relative

        selector_links = []
        rendered_paths = set()

        for href in collector.hrefs:
            resolved = urlsplit(urljoin(source, href))
            rendered_paths.add(resolved.path)
            if (
                resolved.netloc == "siggeardrive.github.io"
                and resolved.path in SELECTOR_PATHS
            ):
                selector_links.append(resolved)

        require(selector_links, f"{page_slug} has no link to a planetary selector")

        if not any(parse_qs(link.query).get("app") == [app] for link in selector_links):
            raise ValueError(f"{page_slug} drops application context in selector links")

        # The anchor is preferred on at least one application-aware link.
        context_links = [
            link for link in selector_links
            if parse_qs(link.query).get("app") == [app]
        ]
        if not any(link.fragment == "preliminary-ratio-stage-finder" for link in context_links):
            raise ValueError(f"{page_slug} has no application-aware selector anchor")

        if page_slug in PRIORITY_APPLICATION_MODEL_PATHS:
            required_paths = {
                "/SigGear-product-docs/products/planetary-gearboxes/"
                + model + "-planetary-gearbox/"
                for model in PRIORITY_APPLICATION_MODEL_PATHS[page_slug]
            }
            required_paths.add(
                "/SigGear-product-docs/engineering-resources/planetary-gearboxes/public-cad-release-v1/"
            )
            direct_inquiry_links = [
                href for href in collector.hrefs
                if href.startswith("mailto:luffy@siggear.com")
            ]
            require(direct_inquiry_links, f"{page_slug} is missing one-click email inquiry")

            missing = sorted(required_paths - rendered_paths)
            if missing:
                raise ValueError(
                    f"{page_slug} has broken model/CAD/inquiry discovery paths: {missing}"
                )

    data = json.loads(
        (ROOT / "docs/assets/data/planetary-ratio-stage-data.json").read_text(encoding="utf-8")
    )
    twelve = next(m for m in data["models"] if m["model"] == "12P")
    stage = next(s for s in twelve["stages"] if s["stage"] == 3)

    require(twelve["diameter"] == 12, "12P published diameter changed")
    require(stage["length"] == 16.85, "12P 3-stage length changed")
    require(42.9 in stage["ratios"], "12P 42.9:1 ratio missing")
    require(stage["rated"] == 3.6, "12P 3-stage rated torque changed")
    require(stage["efficiency"] == 73, "12P 3-stage efficiency changed")

    print("PASS application pages retain source context to current or legacy selector")
    print("PASS priority application pages expose model, CAD and inquiry paths")
    print("PASS published 12P selector reference data remains intact")


if __name__ == "__main__":
    main()
