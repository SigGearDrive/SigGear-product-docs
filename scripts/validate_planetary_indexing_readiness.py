#!/usr/bin/env python3
"""Validate indexing and crawl readiness for monitored planetary canonicals."""

from pathlib import Path
from xml.etree import ElementTree
from html import escape as html_escape
import json
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
DOCS = ROOT / "docs"
BASE = "https://siggeardrive.github.io/SigGear-product-docs"

PRODUCT_PAGES = [
    "/products/planetary-gearboxes/8p-planetary-gearbox/",
    "/products/planetary-gearboxes/10p-planetary-gearbox/",
    "/products/planetary-gearboxes/12p-planetary-gearbox/",
    "/products/planetary-gearboxes/14p-planetary-gearbox/",
    "/products/planetary-gearboxes/16p-planetary-gearbox/",
    "/products/planetary-gearboxes/20p-planetary-gearbox/",
    "/products/planetary-gearboxes/22p-planetary-gearbox/",
    "/products/planetary-gearboxes/24p-planetary-gearbox/",
    "/products/planetary-gearboxes/28p-planetary-gearbox/",
    "/products/planetary-gearboxes/32p-planetary-gearbox/",
    "/products/planetary-gearboxes/36p-planetary-gearbox/",
    "/products/planetary-gearboxes/42p-planetary-gearbox/",
]

GENERIC_PAGES = [
    "/engineering-resources/planetary-gearboxes/public-cad-release-v1/",
    "/custom-engineering/motor-gearbox-integration/",
    "/custom-engineering/custom-planetary-gearbox/",
    "/products/planetary-gearboxes/8-42mm-planetary-gear-reducer/",
]

RESOURCE_PAGES = []
for model in ("8p","10p","12p","14p","16p","20p","22p","24p","28p","32p","36p","42p"):
    RESOURCE_PAGES.extend([
        f"/engineering-resources/{model}/datasheet/",
        f"/engineering-resources/{model}/mechanical-interface/",
    ])

TARGETS = PRODUCT_PAGES + GENERIC_PAGES + RESOURCE_PAGES

def html_path(url_path: str) -> Path:
    return SITE / url_path.strip("/") / "index.html"

def md_rel(url_path: str) -> str:
    clean = url_path.strip("/")
    return clean + ".md"

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)

def check_target_count() -> None:
    require(len(TARGETS) == 40, f"Expected 40 unique planetary canonicals, found {len(TARGETS)}")
    require(len(set(TARGETS)) == 40, "Planetary canonical target list contains duplicates")

def check_built_pages_and_canonicals() -> None:
    for target in TARGETS:
        path = html_path(target)
        require(path.is_file(), f"Built target missing: {target}")
        html = path.read_text(encoding="utf-8")
        expected = BASE + target
        require(
            f'<link rel="canonical" href="{expected}">' in html,
            f"Self-canonical missing or incorrect: {target}",
        )
        require(
            not re.search(r'<meta[^>]+name=["\']robots["\'][^>]+noindex', html, re.I),
            f"noindex found on monitored canonical: {target}",
        )

def check_model_specific_search_metadata() -> None:
    """Catch short nav-title or generic site-description SEO regressions."""
    for target in PRODUCT_PAGES:
        slug = Path(target.strip("/")).name
        source = DOCS / "products/planetary-gearboxes" / f"{slug}.md"
        require(source.is_file(), f"Source model document missing: {target}")

        raw = source.read_text(encoding="utf-8")
        require(raw.startswith("---\n"), f"Source metadata missing: {target}")
        metadata_yaml, sep, _ = raw[4:].partition("\n---\n")
        require(bool(sep), f"Malformed YAML frontmatter: {target}")
        metadata = yaml.safe_load(metadata_yaml) or {}
        title = str(metadata.get("title") or "").strip()
        description = str(metadata.get("description") or "").strip()
        require(bool(title) and bool(description), f"Missing SEO title or description: {target}")

        html = html_path(target).read_text(encoding="utf-8")
        expected_title = f"<title>{html_escape(title, quote=False)} - SigGear Product Documentation</title>"
        expected_description = (
            f'<meta name="description" content="{html_escape(description, quote=True)}">'
        )
        require(expected_title in html, f"Model title lost to short navigation label: {target}")
        require(expected_description in html, f"Model description replaced with generic site text: {target}")

        script = re.search(
            r'<script type="application/ld\+json" data-siggear-seo-schema="model-page">(.*?)</script>',
            html,
            re.S,
        )
        require(bool(script), f"Model ItemPage JSON-LD missing: {target}")
        schema = json.loads(script.group(1))
        require(schema.get("name") == title, f"JSON-LD model name differs from source: {target}")
        require(schema.get("description") == description, f"JSON-LD model description differs from source: {target}")


def check_sitemap_membership() -> None:
    sitemap = SITE / "sitemap.xml"
    require(sitemap.is_file(), "Generated sitemap.xml missing")
    root = ElementTree.parse(sitemap).getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = {
        node.findtext("sm:loc", default="", namespaces=ns)
        for node in root.findall("sm:url", ns)
    }
    missing = [BASE + target for target in TARGETS if BASE + target not in urls]
    require(not missing, "Monitored canonicals missing from sitemap: " + ", ".join(missing[:8]))

def check_robots() -> None:
    robots = (SITE / "robots.txt").read_text(encoding="utf-8")
    require("User-agent: *" in robots, "robots.txt missing wildcard user-agent")
    require("Allow: /SigGear-product-docs/" in robots, "robots.txt does not allow project path")
    require(
        f"Sitemap: {BASE}/sitemap.xml" in robots,
        "robots.txt does not advertise project sitemap",
    )

def check_source_hub_links() -> None:
    series = (DOCS / "products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md").read_text(encoding="utf-8")
    resource_hub = (DOCS / "engineering-resources/planetary-gearboxes/index.md").read_text(encoding="utf-8")
    product_index = (DOCS / "products/planetary-gearboxes/index.md").read_text(encoding="utf-8")

    for target in PRODUCT_PAGES:
        filename = Path(target.strip("/")).name + ".md"
        require(filename in series, f"Series hub does not link product target: {target}")

    for target in RESOURCE_PAGES:
        parts = target.strip("/").split("/")
        model = parts[1]
        page = parts[2]
        token = f"../{model}/{page}.md"
        require(token in resource_hub, f"Resource hub does not link engineering target: {target}")

    generic_tokens = {
        "/engineering-resources/planetary-gearboxes/public-cad-release-v1/": "public-cad-release-v1.md",
        "/custom-engineering/motor-gearbox-integration/": "motor-gearbox-integration.md",
        "/custom-engineering/custom-planetary-gearbox/": "custom-planetary-gearbox.md",
        "/products/planetary-gearboxes/8-42mm-planetary-gear-reducer/": "8-42mm-planetary-gear-reducer.md",
    }
    combined = series + "\n" + resource_hub + "\n" + product_index
    for target, token in generic_tokens.items():
        require(token in combined, f"Planetary hubs do not link generic target: {target}")

def main() -> None:
    check_target_count()
    check_built_pages_and_canonicals()
    check_model_specific_search_metadata()
    check_sitemap_membership()
    check_robots()
    check_source_hub_links()
    print("Planetary indexing and crawl readiness validated for 40 unique monitored canonicals.")

if __name__ == "__main__":
    main()
