#!/usr/bin/env python3
"""Validate generated MkDocs output before GitHub Pages deployment."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from xml.etree import ElementTree

SITE_DIR = Path("site")
EXPECTED_BASE = "https://siggeardrive.github.io/SigGear-product-docs/"
HOST_BASE = "https://siggeardrive.github.io/"
URL_PATTERN = re.compile(r"https://siggeardrive\.github\.io/[^\s\"'<>)]*")

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
    urls = [x.text or "" for x in root.findall("sm:url/sm:loc", ns)]
    if not urls:
        fail("Sitemap has no URLs")
    bad = [url for url in urls if not url.startswith(EXPECTED_BASE)]
    if bad:
        fail("Sitemap contains non-project URLs: " + ", ".join(bad[:5]))

    index = (SITE_DIR / "sitemap-index.xml").read_text(encoding="utf-8")
    if "sitemap.xml" not in index or EXPECTED_BASE not in index:
        fail("Sitemap index does not reference the project sitemap")


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
    check_robots()
    check_redirects()
    check_generated_urls()
    print("Site validation passed.")


if __name__ == "__main__":
    main()
