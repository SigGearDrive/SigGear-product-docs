"""Build-time SEO metadata for SigGear MkDocs output.

- Inject static JSON-LD BreadcrumbList on important content pages.
- Inject semantic ItemPage JSON-LD for B2B model documentation without public offers.
- Rewrite sitemap lastmod values from Git history so deploy date is not
  incorrectly reported as the modification date of every page.

No pricing, ratings, reviews, or unpublished technical values are invented.
"""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
from xml.etree import ElementTree

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "products"
DOCS_DIR = ROOT / "docs"

FAMILY_META = {
    "robot_joint_actuator": {
        "name": "Robot Joint Actuators",
        "url": "products/robot-joint-actuators/",
    },
    "cycloidal_joint_module": {
        "name": "Cycloidal Joint Modules",
        "url": "products/cycloidal-joint-modules/",
    },
    "planetary_gearbox": {
        "name": "Planetary Gearboxes",
        "url": "products/planetary-gearboxes/",
    },
    "hub_gear_motor": {
        "name": "Hub Gear Motors",
        "url": "products/hub-gear-motors/",
    },
}

SECTION_META = {
    "applications": ("Applications", "applications/"),
    "selection-guides": ("Selection Guides", "selection-guides/"),
    "custom-engineering": ("Custom Engineering", "custom-engineering/"),
    "engineering-center": ("Engineering Center", "engineering-center/"),
    "company": ("Company", "company/"),
    "knowledge-base": ("Knowledge Base", "knowledge-base/"),
}

_product_by_src = {}
_resource_product = {}


def _resource_slug(src_uri: str) -> str:
    stem = Path(src_uri).stem
    if stem.endswith("-planetary-gearbox"):
        stem = stem[: -len("-planetary-gearbox")]
    return stem


def _load_products() -> None:
    if _product_by_src:
        return

    for path in sorted(DATA_DIR.glob("*.yml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if data.get("record_type") != "model":
            continue
        if data.get("public_page_status") != "published":
            continue

        canonical = str(data.get("canonical_page", ""))
        if not canonical.startswith("docs/"):
            continue
        src_uri = canonical[len("docs/") :]
        _product_by_src[src_uri] = data
        _resource_product[_resource_slug(src_uri)] = data


def _absolute(config, relative: str) -> str:
    base = str(config["site_url"]).rstrip("/") + "/"
    return urljoin(base, relative)


def _page_title(page) -> str:
    meta_title = page.meta.get("title") if getattr(page, "meta", None) else None
    return str(meta_title or page.title or "").split(" | ")[0].strip()


def _list_item(position: int, name: str, url: str) -> dict:
    return {
        "@type": "ListItem",
        "position": position,
        "name": name,
        "item": url,
    }


def _breadcrumbs(page, config) -> dict | None:
    src = page.file.src_uri.replace("\\", "/")
    current_url = _absolute(config, page.url)
    items = [_list_item(1, "SigGear", _absolute(config, ""))]

    product = _product_by_src.get(src)
    if product:
        family = FAMILY_META.get(product.get("product_family"))
        items.append(_list_item(2, "Products", _absolute(config, "products/")))
        if family:
            items.append(_list_item(3, family["name"], _absolute(config, family["url"])))
        items.append(_list_item(len(items) + 1, str(product.get("model") or _page_title(page)), current_url))

    elif src.startswith("products/"):
        parts = src.split("/")
        items.append(_list_item(2, "Products", _absolute(config, "products/")))
        if src == "products/index.md":
            return {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": items,
            }
        if len(parts) >= 3:
            category = parts[1]
            family = next((v for v in FAMILY_META.values() if v["url"] == f"products/{category}/"), None)
            if family and not src.endswith(f"{category}/index.md"):
                items.append(_list_item(3, family["name"], _absolute(config, family["url"])))
        items.append(_list_item(len(items) + 1, _page_title(page), current_url))

    elif src.startswith("engineering-resources/"):
        parts = src.split("/")
        product = _resource_product.get(parts[1]) if len(parts) > 1 else None
        if product:
            family = FAMILY_META.get(product.get("product_family"))
            items.append(_list_item(2, "Products", _absolute(config, "products/")))
            if family:
                items.append(_list_item(3, family["name"], _absolute(config, family["url"])))
            product_src = str(product["canonical_page"])[len("docs/") :]
            product_rel = product_src[:-3] + "/" if product_src.endswith(".md") else product_src
            items.append(_list_item(len(items) + 1, str(product.get("model")), _absolute(config, product_rel)))
            items.append(_list_item(len(items) + 1, _page_title(page), current_url))
        else:
            items.append(_list_item(2, "Engineering Center", _absolute(config, "engineering-center/")))
            items.append(_list_item(3, _page_title(page), current_url))

    else:
        first = src.split("/", 1)[0]
        section = SECTION_META.get(first)
        if section:
            section_name, section_url = section
            if src not in {f"{first}/index.md", f"{first}.md"}:
                items.append(_list_item(2, section_name, _absolute(config, section_url)))
            items.append(_list_item(len(items) + 1, _page_title(page), current_url))
        else:
            return None

    if len(items) < 2:
        return None

    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }


def _model_page_schema(page, config) -> dict | None:
    """Describe B2B model pages as technical item pages, not retail offers.

    Google's Product rich results require a genuine public offer, review or
    aggregate rating. SigGear's engineering series have none of those as
    verified master data, so a partial Product snippet would be misleading.
    Model identifiers and public engineering specifications remain in HTML.
    """
    src = page.file.src_uri.replace("\\", "/")
    data = _product_by_src.get(src)
    if not data:
        return None

    if data.get("product_family") not in {
        "robot_joint_actuator",
        "cycloidal_joint_module",
        "planetary_gearbox",
    }:
        return None

    url = _absolute(config, page.url)
    page_name = _page_title(page)
    catalog_name = str(data.get("display_name") or data.get("model"))
    name = page_name or catalog_name
    model = {
        "@type": "Thing",
        "@id": url + "#catalog-model",
        "name": name,
        "identifier": str(data.get("model")),
        "url": url,
    }
    if catalog_name != name:
        model["alternateName"] = catalog_name

    item_page = {
        "@context": "https://schema.org",
        "@type": "ItemPage",
        "@id": url + "#webpage",
        "name": name,
        "url": url,
        "inLanguage": "en",
        "publisher": {
            "@id": "https://www.siggear.com/#organization",
            "@type": "Organization",
            "name": "Guangdong SigGear Drive Intelligent Technology Co., Ltd.",
            "url": "https://www.siggear.com/",
        },
        "mainEntity": model,
    }

    description = page.meta.get("description") if getattr(page, "meta", None) else None
    if description:
        item_page["description"] = str(description)
        model["description"] = str(description)

    return item_page



PLANETARY_SERIES_SRC = "products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md"
PLANETARY_MODELS = ["8P", "10P", "12P", "14P", "16P", "20P", "22P", "24P", "28P", "32P", "36P", "42P"]


def _planetary_series_schema(page, config) -> dict | None:
    src = page.file.src_uri.replace("\\", "/")
    if src != PLANETARY_SERIES_SRC:
        return None

    url = _absolute(config, page.url)
    items = []
    for position, model in enumerate(PLANETARY_MODELS, start=1):
        slug = model.lower()
        model_url = _absolute(
            config,
            f"products/planetary-gearboxes/{slug}-planetary-gearbox/",
        )
        items.append(
            {
                "@type": "ListItem",
                "position": position,
                "item": {
                    "@type": "Thing",
                    "@id": model_url + "#catalog-model",
                    "name": f"SigGear {model} Planetary Gearbox",
                    "identifier": model,
                    "url": model_url,
                },
            }
        )

    return {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "@id": url + "#webpage",
        "name": _page_title(page),
        "url": url,
        "inLanguage": "en",
        "publisher": {
            "@id": "https://www.siggear.com/#organization",
            "@type": "Organization",
            "name": "Guangdong SigGear Drive Intelligent Technology Co., Ltd.",
            "url": "https://www.siggear.com/",
        },
        "mainEntity": {
            "@type": "ItemList",
            "name": "SigGear 8–42 mm Planetary Gearbox Series",
            "numberOfItems": len(items),
            "itemListElement": items,
        },
    }


def _json_script(schema: dict, marker: str) -> str:
    payload = json.dumps(schema, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return (
        f'<script type="application/ld+json" data-siggear-seo-schema="{marker}">'
        f"{payload}</script>"
    )


def on_post_page(output: str, page, config, **kwargs) -> str:
    _load_products()

    blocks = []
    breadcrumb = _breadcrumbs(page, config)
    if breadcrumb:
        blocks.append(_json_script(breadcrumb, "breadcrumb"))

    model_page = _model_page_schema(page, config)
    if model_page:
        blocks.append(_json_script(model_page, "model-page"))

    planetary_series = _planetary_series_schema(page, config)
    if planetary_series:
        blocks.append(_json_script(planetary_series, "planetary-series"))

    if not blocks or "</head>" not in output:
        return output

    return output.replace("</head>", "\n".join(blocks) + "\n</head>", 1)


def _git_date(path: Path) -> str | None:
    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        return None

    result = subprocess.run(
        ["git", "log", "-1", "--format=%cI", "--", str(rel)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    value = result.stdout.strip()
    if not value:
        return None

    try:
        # Normalize Git's timezone-aware commit timestamp to UTC before
        # converting it to a sitemap date. This prevents commits made just
        # after midnight in Asia from appearing one day in the future while
        # GitHub Actions is still on the previous UTC date.
        return datetime.fromisoformat(value).astimezone(timezone.utc).date().isoformat()
    except ValueError:
        return None


def _source_for_url(relative_url: str) -> Path | None:
    clean = relative_url.strip("/")
    if not clean:
        candidate = DOCS_DIR / "index.md"
        return candidate if candidate.is_file() else None

    candidates = [
        DOCS_DIR / f"{clean}.md",
        DOCS_DIR / clean / "index.md",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def _latest_date(*values: str | None) -> str | None:
    valid = [v for v in values if v]
    return max(valid) if valid else None


def on_post_build(config, **kwargs) -> None:
    site_dir = Path(config["site_dir"])
    sitemap = site_dir / "sitemap.xml"
    if not sitemap.is_file():
        return

    site_url = str(config["site_url"]).rstrip("/") + "/"
    hook_date = _git_date(Path(__file__))

    ElementTree.register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9")
    tree = ElementTree.parse(sitemap)
    root = tree.getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    for url_node in root.findall("sm:url", ns):
        loc_node = url_node.find("sm:loc", ns)
        if loc_node is None or not loc_node.text or not loc_node.text.startswith(site_url):
            continue

        relative = loc_node.text[len(site_url) :]
        source = _source_for_url(relative)
        source_date = _git_date(source) if source else None

        # The SEO hook changes generated structured data globally. Its latest
        # commit date is therefore also a real significant page modification.
        lastmod_value = _latest_date(source_date, hook_date)
        lastmod = url_node.find("sm:lastmod", ns)

        if lastmod_value:
            if lastmod is None:
                lastmod = ElementTree.SubElement(
                    url_node, "{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod"
                )
            lastmod.text = lastmod_value
        elif lastmod is not None:
            url_node.remove(lastmod)

    tree.write(sitemap, encoding="utf-8", xml_declaration=True)

    # Keep the sitemap index's lastmod in sync with the generated XML sitemap.
    # Its source file intentionally has no hard-coded date.
    index_path = site_dir / "sitemap-index.xml"
    if index_path.is_file():
        newest = max(
            (
                url_node.findtext("sm:lastmod", default="", namespaces=ns) or ""
                for url_node in root.findall("sm:url", ns)
            ),
            default="",
        )
        index_tree = ElementTree.parse(index_path)
        index_root = index_tree.getroot()
        for entry in index_root.findall("sm:sitemap", ns):
            loc = entry.findtext("sm:loc", default="", namespaces=ns)
            if loc != site_url + "sitemap.xml":
                continue
            date_node = entry.find("sm:lastmod", ns)
            if newest:
                if date_node is None:
                    date_node = ElementTree.SubElement(
                        entry,
                        "{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod",
                    )
                date_node.text = newest
            elif date_node is not None:
                entry.remove(date_node)
        index_tree.write(index_path, encoding="utf-8", xml_declaration=True)
