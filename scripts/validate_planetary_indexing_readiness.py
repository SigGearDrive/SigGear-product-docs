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
    "/selection-guides/planetary-gearhead-quick-selector/",
]

RESOURCE_PAGES = []
for model in ("8p","10p","12p","14p","16p","20p","22p","24p","28p","32p","36p","42p"):
    RESOURCE_PAGES.extend([
        f"/engineering-resources/{model}/datasheet/",
        f"/engineering-resources/{model}/mechanical-interface/",
    ])

CLASS_HUB_PAGES = [
    "/products/planetary-gearboxes/micro-planetary-gearheads-8-16mm/",
    "/products/planetary-gearboxes/miniature-planetary-gearheads-20-32mm/",
    "/products/planetary-gearboxes/compact-planetary-gearheads-36-42mm/",
]

TARGETS = PRODUCT_PAGES + GENERIC_PAGES + RESOURCE_PAGES + CLASS_HUB_PAGES

def html_path(url_path: str) -> Path:
    return SITE / url_path.strip("/") / "index.html"

def md_rel(url_path: str) -> str:
    clean = url_path.strip("/")
    return clean + ".md"

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)

def check_target_count() -> None:
    require(len(TARGETS) == 44, f"Expected 44 unique planetary canonicals, found {len(TARGETS)}")
    require(len(set(TARGETS)) == 44, "Planetary canonical target list contains duplicates")

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
        full_title = title if re.search(r"\bSigGear\b", title, re.I) else f"{title} | SigGear"
        expected_title = f"<title>{html_escape(full_title, quote=False)}</title>"
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
        expected_entity_name = title.split(" | ", 1)[0].strip()
        require(schema.get("name") == expected_entity_name, f"JSON-LD model name differs from the canonical product title: {target}")
        require(schema.get("description") == description, f"JSON-LD model description differs from source: {target}")


def check_priority_gearhead_hub_metadata() -> None:
    """Prevent priority hubs and OEM application articles from losing SEO titles."""
    priority_sources = [
        "index.md",
        "products/planetary-gearboxes/index.md",
        "products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md",
        "selection-guides/planetary-gearhead-quick-selector.md",
        "engineering-resources/planetary-gearboxes/public-cad-release-v1.md",
        "engineering-resources/motors/index.md",
        "products/planetary-gearboxes/micro-planetary-gearheads-8-16mm.md",
        "products/planetary-gearboxes/miniature-planetary-gearheads-20-32mm.md",
        "products/planetary-gearboxes/compact-planetary-gearheads-36-42mm.md",
        "applications/index.md",
        "applications/electric-pruning-shears-planetary-gearbox.md",
        "applications/humanoid-robot-joint-actuators.md",
        "applications/planetary-gearbox-application-families.md",
        "applications/electric-curtain-blind-window-opener-gear-motors.md",
        "applications/robot-gripper-gear-motors.md",
    ]
    for source_rel in priority_sources:
        raw = (DOCS / source_rel).read_text(encoding="utf-8")
        require(raw.startswith("---\n"), f"Missing SEO frontmatter: {source_rel}")
        meta_yaml, sep, _ = raw[4:].partition("\n---\n")
        require(bool(sep), f"Malformed SEO frontmatter: {source_rel}")
        metadata = yaml.safe_load(meta_yaml) or {}
        title = str(metadata.get("title") or "").strip()
        description = str(metadata.get("description") or "").strip()
        require(bool(title) and bool(description), f"Missing source SEO metadata: {source_rel}")
        if source_rel == "index.md":
            built_path = SITE / "index.html"
        elif source_rel.endswith("/index.md"):
            built_path = SITE / source_rel.removesuffix("index.md") / "index.html"
        else:
            built_path = SITE / source_rel.removesuffix(".md") / "index.html"
        built = built_path.read_text(encoding="utf-8")
        full_title = title if re.search(r"\bSigGear\b", title, re.I) else f"{title} | SigGear"
        expected_title = f"<title>{html_escape(full_title, quote=False)}</title>"
        expected_description = f'<meta name="description" content="{html_escape(description, quote=True)}">'
        require(expected_title in built, f"Priority page title lost to nav label: {source_rel}")
        require(expected_description in built, f"Priority page description lost: {source_rel}")


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

    for target in CLASS_HUB_PAGES:
        filename = Path(target.strip("/")).name + ".md"
        require(filename in series, f"Series hub does not link size-group target: {target}")
        class_hub = (DOCS / "products/planetary-gearboxes" / filename).read_text(encoding="utf-8")
        require("Datasheet PDF" in class_hub and "Full assembly STEP" in class_hub,
                f"Size-group hub is missing direct engineering downloads: {target}")

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

def check_catalog_application_indexing() -> None:
    """Keep 32 application pages and joint/hub products findable and model-specific."""
    application_sources = sorted(
        p for p in (DOCS / "applications").glob("*.md")
        if p.name not in {"index.md", "planetary-gearbox-application-families.md"}
    )
    require(len(application_sources) == 32,
            f"Expected 32 application articles, found {len(application_sources)}")

    model_sources = [
        "products/robot-joint-actuators/sg6010c.md",
        "products/robot-joint-actuators/sg6010hb.md",
        "products/robot-joint-actuators/sg6010d.md",
        "products/robot-joint-actuators/sg8021.md",
        "products/cycloidal-joint-modules/cpm78-39.md",
        "products/cycloidal-joint-modules/cpm80-25.md",
        "products/cycloidal-joint-modules/cpm100-25.md",
        "products/hub-gear-motors/sg2877.md",
        "products/hub-gear-motors/sg2878.md",
    ]
    sources = application_sources + [DOCS / relative for relative in model_sources]
    sources.append(DOCS / "knowledge-base/product-model-index.md")
    root = ElementTree.parse(SITE / "sitemap.xml").getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = [
        node.findtext("sm:loc", default="", namespaces=ns)
        for node in root.findall("sm:url", ns)
    ]
    require(len(sitemap_urls) == len(set(sitemap_urls)),
            "Sitemap has duplicate canonical URLs")
    indexed_urls = set(sitemap_urls)

    for source in sources:
        require(source.is_file(), f"Missing source page: {source}")
        relative = source.relative_to(DOCS).as_posix()
        slug = relative.removesuffix(".md")
        expected_url = BASE + "/" + slug + "/"
        require(expected_url in indexed_urls,
                f"Application or joint/hub product missing from sitemap: {expected_url}")

        raw = source.read_text(encoding="utf-8")
        require(raw.startswith("---\n"), f"Missing SEO frontmatter: {relative}")
        frontmatter, sep, _ = raw[4:].partition("\n---\n")
        require(bool(sep), f"Malformed SEO frontmatter: {relative}")
        metadata = yaml.safe_load(frontmatter) or {}
        title = str(metadata.get("title") or "").strip()
        description = str(metadata.get("description") or "").strip()
        require(bool(title) and bool(description),
                f"Missing title or description: {relative}")

        built = SITE / slug / "index.html"
        require(built.is_file(), f"Missing built product/application page: {relative}")
        html = built.read_text(encoding="utf-8")
        require(f'<link rel="canonical" href="{expected_url}">' in html,
                f"Missing self-canonical: {relative}")
        require(not re.search(r'<meta[^>]+name=["\']robots["\'][^>]+noindex', html, re.I),
                f"Unexpected noindex on public page: {relative}")

        full_title = title if re.search(r"\bSigGear\b", title, re.I) else title + " | SigGear"
        require(f"<title>{html_escape(full_title, quote=False)}</title>" in html,
                f"SEO title overridden by nav/site title: {relative}")
        expected_description = (
            f'<meta name="description" content="{html_escape(description, quote=True)}">'
        )
        require(expected_description in html,
                f"Specific SEO description replaced by generic site text: {relative}")

    hb_html = (SITE / "products/robot-joint-actuators/sg6010hb/index.html").read_text(
        encoding="utf-8"
    )
    match = re.search(
        r'<script type="application/ld\+json" data-siggear-seo-schema="model-page">(.*?)</script>',
        hb_html, re.S
    )
    require(bool(match), "SG-6010HB model-specific ItemPage JSON-LD missing")
    hb_schema = json.loads(match.group(1))
    require(hb_schema.get("name") == "SG-6010HB 67 mm Planetary Joint Actuator",
            "SG-6010HB schema lost model-specific name")
    require((hb_schema.get("mainEntity") or {}).get("identifier") == "SG-6010HB",
            "SG-6010HB schema has incorrect identifier")

def main() -> None:
    check_target_count()
    check_built_pages_and_canonicals()
    check_model_specific_search_metadata()
    check_priority_gearhead_hub_metadata()
    check_sitemap_membership()
    check_robots()
    check_source_hub_links()
    check_catalog_application_indexing()
    print("Index readiness passed: 44 planetary canonicals, 32 application articles and 9 joint/hub models.")

if __name__ == "__main__":
    main()
