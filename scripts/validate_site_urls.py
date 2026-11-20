#!/usr/bin/env python3
"""Validate generated MkDocs output before GitHub Pages deployment."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from xml.etree import ElementTree

# SEO validation covers build-time JSON-LD and sitemap freshness.
SITE_DIR = Path("site")
EXPECTED_BASE = "https://siggeardrive.github.io/SigGear-product-docs/"
HOST_BASE = "https://siggeardrive.github.io/"
URL_PATTERN = re.compile(r"https://siggeardrive\.github\.io/[^\s\"'<>)]*")

PLANETARY_MODELS = ["8P", "10P", "12P", "14P", "16P", "20P", "22P", "24P", "28P", "32P", "36P", "42P"]

EXPECTED_REDIRECTS = [
    "Applications/6-42mm-planetary-gear-reducer/index.html",
    "Applications/micro-robotics-gear-motor/index.html",
    "Applications/humanoid-robot-joint-reducer/index.html",
    "Selection-Guides/planetary-gearbox-selection-guide/index.html",
    "Comparisons/cycloidal-vs-harmonic-drive/index.html",
    "Developers/ros2-robot-joint-actuator/index.html",
    "CPM100-25/index.html",
    "CPM80-25/index.html",
    "SG6010C/index.html",
    "SG8021/index.html",
    "Selection-Guides/humanoid-robot-joint-gearbox-selection-guide/index.html",
    "custom-robotic-joint-actuator-oem-gearbox-solutions/index.html",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_required_files() -> None:
    required = [
        SITE_DIR / "index.html",
        SITE_DIR / "sitemap.xml",
        SITE_DIR / "sitemap-index.xml",
        SITE_DIR / "robots.txt",
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        fail("Missing generated files: " + ", ".join(missing))


def check_home_canonical() -> None:
    html = (SITE_DIR / "index.html").read_text(encoding="utf-8")
    if f'<link rel="canonical" href="{EXPECTED_BASE}">' not in html:
        fail("Homepage canonical is incorrect")


def check_sitemap() -> None:
    root = ElementTree.parse(SITE_DIR / "sitemap.xml").getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    url_nodes = root.findall("sm:url", ns)
    urls = [(node.findtext("sm:loc", default="", namespaces=ns) or "") for node in url_nodes]
    if not urls:
        fail("Sitemap has no URLs")
    bad = [url for url in urls if not url.startswith(EXPECTED_BASE)]
    if bad:
        fail("Sitemap contains non-project URLs: " + ", ".join(bad[:5]))

    today = date.today()
    missing_lastmod = []
    invalid_lastmod = []
    for node in url_nodes:
        loc = node.findtext("sm:loc", default="", namespaces=ns) or ""
        value = node.findtext("sm:lastmod", default="", namespaces=ns) or ""
        if not value:
            missing_lastmod.append(loc)
            continue
        try:
            parsed = date.fromisoformat(value[:10])
        except ValueError:
            invalid_lastmod.append(f"{loc}: {value}")
            continue
        if parsed > today:
            invalid_lastmod.append(f"{loc}: future date {value}")

    if missing_lastmod:
        fail("Sitemap URLs missing lastmod: " + ", ".join(missing_lastmod[:5]))
    if invalid_lastmod:
        fail("Sitemap contains invalid lastmod values: " + ", ".join(invalid_lastmod[:5]))

    index_root = ElementTree.parse(SITE_DIR / "sitemap-index.xml").getroot()
    entries = index_root.findall("sm:sitemap", ns)
    target = next(
        (
            entry for entry in entries
            if entry.findtext("sm:loc", default="", namespaces=ns)
            == EXPECTED_BASE + "sitemap.xml"
        ),
        None,
    )
    if target is None:
        fail("Sitemap index does not reference the project sitemap")
    recorded_date = target.findtext("sm:lastmod", default="", namespaces=ns)
    actual_date = max(
        (
            node.findtext("sm:lastmod", default="", namespaces=ns) or ""
            for node in url_nodes
        ),
        default="",
    )
    if recorded_date != actual_date:
        fail(
            f"Sitemap-index lastmod is stale: {recorded_date}, "
            f"expected {actual_date}"
        )



def _json_ld_blocks(html: str) -> list[dict]:
    blocks = []
    pattern = re.compile(
        r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',
        re.IGNORECASE | re.DOTALL,
    )
    for raw in pattern.findall(html):
        try:
            blocks.append(json.loads(raw))
        except json.JSONDecodeError:
            continue
    return blocks


def check_structured_data() -> None:
    targets = {
        "products/robot-joint-actuators/sg6010d/index.html": {"BreadcrumbList", "ItemPage"},
        "products/cycloidal-joint-modules/cpm80-25/index.html": {"BreadcrumbList", "ItemPage"},
        "products/planetary-gearboxes/20p-planetary-gearbox/index.html": {"BreadcrumbList", "ItemPage"},
        "products/planetary-gearboxes/32p-planetary-gearbox/index.html": {"BreadcrumbList", "ItemPage"},
        "applications/humanoid-robot-joint-actuators/index.html": {"BreadcrumbList"},
    }

    for relative, expected_types in targets.items():
        path = SITE_DIR / relative
        if not path.is_file():
            fail(f"Structured-data test page missing: {relative}")
        blocks = _json_ld_blocks(path.read_text(encoding="utf-8"))
        found = {block.get("@type") for block in blocks if isinstance(block, dict)}
        missing = expected_types - found
        if missing:
            fail(
                f"Structured data missing on {relative}: "
                + ", ".join(sorted(missing))
            )

        # Verify that each model's JSON-LD identifies the correct model.
        if "ItemPage" in expected_types:
            item_page = next(b for b in blocks if b.get("@type") == "ItemPage")
            model = item_page.get("mainEntity") or {}
            if model.get("@type") != "Thing" or not model.get("identifier"):
                fail(f"Missing engineering model identity on {relative}")

    # Prevent a recurrence of Google's invalid Product-snippet enhancement:
    # only emit Product markup when genuine offer/review/rating data is supplied.
    for html_path in (SITE_DIR / "products").glob("*/*/index.html"):
        for block in _json_ld_blocks(html_path.read_text(encoding="utf-8")):
            if block.get("@type") == "Product" and not any(
                block.get(key) for key in ("offers", "review", "aggregateRating")
            ):
                fail(
                    "Unqualified Product rich-result markup (no verified offers "
                    f"or reviews): {html_path.relative_to(SITE_DIR)}"
                )


def check_planetary_real_image_seo() -> None:
    representative_image = (
        EXPECTED_BASE
        + "assets/images/products/planetary-gearboxes/36p/36p-real-product-evidence.png"
    )
    real_model_images = [
        "assets/images/products/planetary-gearboxes/16p/16p-real-product-evidence.png",
        "assets/images/products/planetary-gearboxes/22p/22p-real-product-evidence.png",
        "assets/images/products/planetary-gearboxes/36p/36p-real-product-evidence.png",
    ]
    for photo in real_model_images:
        asset = SITE_DIR / photo
        if not asset.is_file():
            fail(f"Representative real product photo missing from output: {photo}")
        if asset.stat().st_size < 100000:
            fail(f"Representative photo is suspiciously small / overcompressed: {photo}")
    family_targets = [
        ("index.html", None),
        ("products/planetary-gearboxes/8-42mm-planetary-gear-reducer/index.html", "CollectionPage"),
    ]

    for relative, schema_type in family_targets:
        path = SITE_DIR / relative
        if not path.is_file():
            fail(f"Real-image SEO test page missing: {relative}")
        html = path.read_text(encoding="utf-8")
        if "8-42mm-planetary-gearbox-family-real.webp" in html:
            fail(f"Previously blurred 9 KB lineup is still used on {relative}")
        if 'class="siggear-planetary-photo-grid"' not in html:
            fail(f"Responsive real-product photo gallery missing on {relative}")
        for photo in real_model_images:
            if f'/SigGear-product-docs/{photo}' not in html:
                fail(f"Required model photo missing from {relative}: {photo}")
        if f'<meta property="og:image" content="{representative_image}">' not in html:
            fail(f"Representative product image missing from og:image on {relative}")
        if f'<meta name="twitter:image" content="{representative_image}">' not in html:
            fail(f"Representative product image missing from twitter:image on {relative}")
        if schema_type:
            blocks = _json_ld_blocks(html)
            block = next((b for b in blocks if b.get("@type") == schema_type), None)
            if block is None or representative_image not in json.dumps(block, ensure_ascii=False):
                fail(f"Representative product image missing from {schema_type} JSON-LD on {relative}")

    # Only the overview carries all 12 pictures; family pages carry exactly
    # their matching subset. Keep home page at three representative images.
    photo_directory_pages = {
        "products/planetary-gearboxes/8-42mm-planetary-gear-reducer/index.html": PLANETARY_MODELS,
        "products/planetary-gearboxes/micro-planetary-gearheads-8-16mm/index.html": PLANETARY_MODELS[:5],
        "products/planetary-gearboxes/miniature-planetary-gearheads-20-32mm/index.html": PLANETARY_MODELS[5:10],
        "products/planetary-gearboxes/compact-planetary-gearheads-36-42mm/index.html": PLANETARY_MODELS[10:],
    }
    for relative, models in photo_directory_pages.items():
        path = SITE_DIR / relative
        if not path.is_file():
            fail(f"Real photo directory missing from built site: {relative}")
        html = path.read_text(encoding="utf-8")
        if html.count('class="siggear-planetary-photo-grid"') < 1:
            fail(f"Photo directory grid absent from {relative}")
        img_refs = re.findall(
            r'<img\\b[^>]*\\bsrc="(/SigGear-product-docs/assets/images/products/planetary-gearboxes/[^"]+)"',
            html,
        )
        expected = [
            f"/SigGear-product-docs/assets/images/products/planetary-gearboxes/"
            f"{model.lower()}/{model.lower()}-real-product-evidence.png"
            for model in models
        ]
        if img_refs != expected:
            fail(f"Wrong / duplicate product photos in {relative}: {img_refs}")
        for model in models:
            slug = model.lower()
            expected_product = f"/SigGear-product-docs/products/planetary-gearboxes/{slug}-planetary-gearbox/"
            if expected_product not in html:
                fail(f"{relative} photo does not link to {model} model page")
            if f"Authentic SigGear {model}" not in html:
                fail(f"{relative} photo lacks model-specific alt text")

    for model in PLANETARY_MODELS:
        slug = model.lower()
        relative = f"products/planetary-gearboxes/{slug}-planetary-gearbox/index.html"
        filename = f"{slug}-real-product-evidence.png"
        image_asset = f"assets/images/products/planetary-gearboxes/{slug}/{filename}"
        image_url = EXPECTED_BASE + image_asset
        legacy_bad = (
            EXPECTED_BASE + f"assets/images/products/planetary-gearboxes/{slug}/"
            + f"{slug}-real-product-evidence.webp"
        )
        path = SITE_DIR / relative
        if not path.is_file():
            fail(f"Real-image SEO model page missing: {relative}")
        html = path.read_text(encoding="utf-8")
        if legacy_bad in html:
            fail(f"Broken legacy WebP still advertised for {slug}")
        if not (SITE_DIR / image_asset).is_file():
            fail(f"Approved original PNG missing from published build: {image_asset}")
        if f'<meta property="og:image" content="{image_url}">' not in html:
            fail(f"Real product image missing from og:image on {relative}")
        if f'<meta name="twitter:image" content="{image_url}">' not in html:
            fail(f"Real product image missing from twitter:image on {relative}")

        blocks = _json_ld_blocks(html)
        item_page = next((b for b in blocks if b.get("@type") == "ItemPage"), None)
        if item_page is None:
            fail(f"ItemPage JSON-LD missing while checking real image on {relative}")
        if image_url not in json.dumps(item_page, ensure_ascii=False):
            fail(f"Real product image missing from ItemPage JSON-LD on {relative}")


def check_robots() -> None:
    robots = (SITE_DIR / "robots.txt").read_text(encoding="utf-8")
    if "User-agent: *" not in robots or "Allow: /SigGear-product-docs/" not in robots:
        fail("robots.txt does not allow the project path")
    if f"Sitemap: {EXPECTED_BASE}sitemap.xml" not in robots:
        fail("robots.txt does not reference the project sitemap")


def check_redirects() -> None:
    missing = [path for path in EXPECTED_REDIRECTS if not (SITE_DIR / path).is_file()]
    if missing:
        fail("Missing redirect pages: " + ", ".join(missing))


def check_generated_urls() -> None:
    invalid = []
    for path in SITE_DIR.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".html", ".xml", ".txt", ".js", ".json"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for url in URL_PATTERN.findall(text):
            if url.startswith(HOST_BASE) and not url.startswith(EXPECTED_BASE):
                invalid.append((str(path), url))
    if invalid:
        fail("Root-domain URLs found: " + "; ".join(f"{p}: {u}" for p, u in invalid[:5]))


def main() -> None:
    if not SITE_DIR.is_dir():
        fail("Missing site build directory")
    check_required_files()
    check_home_canonical()
    check_sitemap()
    check_structured_data()
    check_planetary_real_image_seo()
    check_robots()
    check_redirects()
    check_generated_urls()
    print("Site validation passed.")


if __name__ == "__main__":
    main()
