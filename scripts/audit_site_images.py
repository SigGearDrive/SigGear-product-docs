#!/usr/bin/env python3
"""Audit SigGear public website images, including full pixel decoding.

Modes:
  --mode repo : inspect every image file under docs/ with Pillow / SVG XML
  --mode live : fetch every canonical sitemap page, discover its image references,
                HTTP GET the unique images, and decode their complete contents
  --mode both : both checks (default)

This does not create or infer missing authentic product images. It reports
8P/10P/12P/14P/20P as pending until owners upload real source PNGs.
The live check confirms HTML references, HTTP delivery and image decoding.
CSS visibility and real-browser screenshot reviews are independent checks.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urljoin, urlparse
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET

from PIL import Image, UnidentifiedImageError
from io import BytesIO

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = "https://siggeardrive.github.io/SigGear-product-docs/"
HOST = urlparse(SITE).netloc
PREFIX = urlparse(SITE).path
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".avif"}
BINARY_EXT = IMAGE_EXT - {".svg"}
MODEL_IDS = (8, 10, 12, 14, 16, 20, 22, 24, 28, 32, 36, 42)
KNOWN_CORRUPT_SOURCES = {
    "docs/assets/brand/siggear-logo-white.webp",
    "docs/assets/images/evidence/manufacturing/siggear-manufacturing-quality-evidence.webp",
    "docs/assets/images/evidence/planetary/8-42mm-planetary-gearbox-family-real.webp",
    "docs/assets/images/evidence/planetary/compact-gearmotor-measurement-caliper.webp",
    "docs/assets/images/evidence/planetary/compact-gearmotor-size-reference.webp",
    "docs/assets/images/evidence/planetary/micro-gearmotor-size-reference.webp",
    "docs/assets/images/products/planetary-gearboxes/32p/32p-real-product-evidence.webp",
    "docs/assets/images/products/robot-joint-actuators/sg8021/sg8021-robot-joint-actuator-front-angle.webp",
}
EXPECTED_PRODUCT_IMAGES = {n: f"{n}p-real-product-evidence.png" for n in MODEL_IDS}
USER_AGENT = "SigGear-Public-Image-Audit/2026-11-20"
STYLE_URL = re.compile(r"url\(\s*['\"]?([^)'\"\s]+)", re.I)


def get(url: str) -> tuple[bytes, str]:
    error = None
    for attempt in range(2):
        try:
            req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
            with urlopen(req, timeout=25) as response:
                body = response.read()
                final = response.geturl()
                if urlparse(final).netloc != HOST:
                    raise ValueError(f"unexpected off-host redirect to {final}")
                if response.status != 200:
                    raise ValueError(f"HTTP {response.status}")
                return body, response.headers.get("Content-Type", "")
        except (HTTPError, URLError, TimeoutError, OSError, ValueError) as exc:
            error = str(exc)
            if attempt:
                break
    raise ValueError(error or "unknown fetch error")


def check_bytes(blob: bytes, name: str) -> str:
    extension = Path(urlparse(name).path).suffix.lower()
    if not blob or len(blob) < 80:
        raise ValueError(f"empty/too-short image ({len(blob)} bytes)")
    if extension == ".svg":
        root = ET.fromstring(blob)
        if root.tag not in ("{http://www.w3.org/2000/svg}svg", "svg"):
            raise ValueError("SVG root is not <svg>")
        return f"SVG {len(blob)} bytes"
    try:
        with Image.open(BytesIO(blob)) as image:
            expected = {".webp": "WEBP", ".jpg": "JPEG", ".jpeg": "JPEG",
                        ".png": "PNG", ".gif": "GIF", ".avif": "AVIF"}[extension]
            if image.format != expected:
                raise ValueError(f"{extension} extension contains {image.format}, not {expected}")
            width, height = image.size
            image.verify()
        with Image.open(BytesIO(blob)) as image:
            image.load()
            if getattr(image, "n_frames", 1) > 1:
                for frame in range(image.n_frames):
                    image.seek(frame)
                    image.load()
    except (OSError, ValueError, UnidentifiedImageError) as exc:
        raise ValueError(f"pixel decoding failed: {exc}") from exc
    if width < 1 or height < 1:
        raise ValueError("zero-sized image")
    return f"{width}x{height} {expected} {len(blob)} bytes"


class ImageRefs(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        attr = dict(attrs)
        if tag in ("img", "source"):
            for key in ("src", "data-src"):
                if attr.get(key):
                    self.refs.append((f"{tag}.{key}", attr[key]))
            for key in ("srcset", "data-srcset"):
                if attr.get(key):
                    for part in attr[key].split(","):
                        # srcset: URL [width/density descriptor]
                        candidate = part.strip().split()
                        if candidate:
                            self.refs.append((f"{tag}.{key}", candidate[0]))
        if tag == "video" and attr.get("poster"):
            self.refs.append(("video.poster", attr["poster"]))
        if tag == "meta":
            prop = (attr.get("property") or attr.get("name") or "").lower()
            if prop in ("og:image", "og:image:url", "twitter:image", "twitter:image:src"):
                if attr.get("content"):
                    self.refs.append((f"meta.{prop}", attr["content"]))
        if tag == "link" and attr.get("href"):
            relationship = (attr.get("rel") or "").lower()
            if any(x in relationship for x in ("icon", "image_src", "apple-touch")):
                self.refs.append(("link."+relationship, attr["href"]))
        if attr.get("style"):
            for found in STYLE_URL.findall(attr["style"]):
                self.refs.append(("style.url", found))


def same_site_ref(page_url: str, value: str) -> tuple[str | None, str | None]:
    value = (value or "").strip()
    if not value or value.startswith(("data:", "blob:", "#", "javascript:")):
        return None, None
    resolved = urljoin(page_url, value)
    parsed = urlparse(resolved)
    if parsed.scheme not in ("https", "http") or parsed.netloc != HOST:
        return None, resolved
    if not parsed.path.startswith(PREFIX):
        raise ValueError(f"same-host URL is outside SigGear project: {resolved}")
    return parsed._replace(query="", fragment="").geturl(), None


def repo_audit() -> dict:
    assets = [
        path for path in DOCS.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_EXT
    ]
    result = {"count": len(assets), "verified": [], "failed": []}
    for path in sorted(assets):
        rel = path.relative_to(ROOT).as_posix()
        try:
            info = check_bytes(path.read_bytes(), rel)
            result["verified"].append({"path": rel, "info": info})
        except Exception as exc:
            result["failed"].append({"path": rel, "reason": str(exc)})
    return result


def fetch_page(url: str) -> tuple[str, list[tuple[str, str]], str | None]:
    try:
        body, content_type = get(url)
        if "text/html" not in content_type.lower():
            raise ValueError(f"HTML URL returned content type {content_type}")
        parser = ImageRefs()
        parser.feed(body.decode("utf-8", errors="replace"))
        return url, parser.refs, None
    except Exception as exc:
        return url, [], str(exc)


def fetch_image(url: str) -> tuple[str, str | None, str | None]:
    try:
        blob, content_type = get(url)
        suffix = Path(urlparse(url).path).suffix.lower()
        if content_type and "image/" not in content_type.lower() and suffix in IMAGE_EXT:
            raise ValueError(f"unexpected Content-Type {content_type}")
        info = check_bytes(blob, url)
        return url, info, None
    except Exception as exc:
        return url, None, str(exc)


def live_audit(workers: int) -> dict:
    sitemap_body, _ = get(urljoin(SITE, "sitemap.xml"))
    root = ET.fromstring(sitemap_body)
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    pages = sorted({
        loc.text.strip()
        for loc in root.findall(f".//{ns}url/{ns}loc")
        if loc.text and loc.text.strip().startswith(SITE)
    })
    # Explicitly include the 12 most important product detail pages.
    pages = sorted(set(pages) | {
        urljoin(SITE, f"products/planetary-gearboxes/{n}p-planetary-gearbox/")
        for n in MODEL_IDS
    })
    pages.append(SITE) if SITE not in pages else None
    if not 50 <= len(pages) <= 1000:
        raise ValueError(f"unexpected number of canonical pages: {len(pages)}")

    references: dict[str, set[str]] = defaultdict(set)
    result = {
        "page_count": len(pages), "page_failures": [],
        "image_count": 0, "image_verified": [], "image_failed": [],
        "external_image_refs": [], "referencing_pages": {},
        "models_with_live_image": [], "models_pending_original_png": []
    }
    ext_refs: set[tuple[str, str]] = set()
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(fetch_page, url) for url in pages]
        for future in as_completed(futures):
            page, found, err = future.result()
            if err:
                result["page_failures"].append({"page": page, "reason": err})
                continue
            for tag, ref in found:
                try:
                    local, external = same_site_ref(page, ref)
                except ValueError as exc:
                    result["image_failed"].append({"page": page, "reference": ref,
                                                  "reason": str(exc)})
                    continue
                if external:
                    ext_refs.add((page, external))
                elif local:
                    references[local].add(page)

    result["external_image_refs"] = [
        {"page": pg, "url": url} for pg, url in sorted(ext_refs)
    ]
    result["image_count"] = len(references)
    result["referencing_pages"] = {img: sorted(pages) for img, pages in sorted(references.items())}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(fetch_image, url) for url in references]
        for future in as_completed(futures):
            url, info, err = future.result()
            if err:
                result["image_failed"].append(
                    {"image": url, "reason": err, "pages": sorted(references[url])}
                )
            else:
                result["image_verified"].append({"image": url, "info": info})

    model_pages = {
        n: urljoin(SITE, f"products/planetary-gearboxes/{n}p-planetary-gearbox/")
        for n in MODEL_IDS
    }
    for n, page in model_pages.items():
        filename = EXPECTED_PRODUCT_IMAGES[n]
        expected = urljoin(
            SITE, f"assets/images/products/planetary-gearboxes/{n}p/{filename}"
        )
        if page in references.get(expected, set()):
            result["models_with_live_image"].append(n)
        else:
            result["image_failed"].append({
                "page": page,
                "image": expected,
                "reason": f"{n}P product page lacks approved high-resolution PNG",
            })
    result["image_verified"].sort(key=lambda x: x["image"])
    result["image_failed"].sort(key=lambda x: (x.get("image", ""), x.get("page", "")))
    result["page_failures"].sort(key=lambda x: x["page"])
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["repo", "live", "both"], default="both")
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--report", default="site-image-audit-report.json")
    args = parser.parse_args()
    report: dict = {"site": SITE, "scope": args.mode, "files": {}, "live": {}}
    failures = []
    try:
        if args.mode in ("repo", "both"):
            report["files"] = repo_audit()
            local = report["files"]
            print(f"Repository: {len(local['verified'])}/{local['count']} image assets fully decoded")
            known = [issue for issue in local["failed"] if issue["path"] in KNOWN_CORRUPT_SOURCES]
            print(f"Known invalid original assets pending owner replacement: {len(known)}")
            for issue in known:
                print(f"PENDING AUTHENTIC SOURCE: {issue['path']}")
            for issue in local["failed"]:
                if issue["path"] not in KNOWN_CORRUPT_SOURCES:
                    failures.append(f"NEW CORRUPT FILE {issue['path']}: {issue['reason']}")
        if args.mode in ("live", "both"):
            report["live"] = live_audit(max(1, min(24, args.workers)))
            live = report["live"]
            print(f"Live: {live['page_count']} sitemap/product pages inspected, "
                  f"{len(live['image_verified'])}/{live['image_count']} referenced images "
                  "returned HTTP 200 and fully decoded")
            print(f"12 models with actual image refs: {live['models_with_live_image']}")
            print(f"Product images waiting for genuine PNG: {live.get('models_pending_original_png', [])}")
            print(f"External image refs not validated here: {len(live['external_image_refs'])}")
            for issue in live["page_failures"]:
                failures.append(f"PAGE {issue['page']}: {issue['reason']}")
            for issue in live["image_failed"]:
                failures.append("IMAGE " + json.dumps(issue, ensure_ascii=False))
    except Exception as exc:
        failures.append(f"RUN: {exc}")

    report["failures"] = failures
    Path(args.report).write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    for err in failures:
        print("FAIL:", err, file=sys.stderr)
    print(f"Detailed audit written to {args.report}")
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
