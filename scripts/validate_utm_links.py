#!/usr/bin/env python3
"""Validate SigGear UTM taxonomy and external-platform tracking settings."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
TAXONOMY_PATH = ROOT / "data" / "seo" / "utm-source-taxonomy.yml"
PLATFORM_PATHS = {
    "traceparts": ROOT / "data" / "external-catalogs" / "platforms" / "traceparts.yml",
    "3dfindit": ROOT / "data" / "external-catalogs" / "platforms" / "3dfindit.yml",
}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")
ALLOWED_MEDIUMS = {"social", "video", "referral"}


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def fail(message: str) -> None:
    raise ValueError(message)


def main() -> None:
    taxonomy = load_yaml(TAXONOMY_PATH)
    base = taxonomy["canonical_base"]
    base_parts = urlsplit(base)
    sources = taxonomy["manual_sources"]
    campaigns = taxonomy["campaigns"]

    for key, config in sources.items():
        source = config["utm_source"]
        medium = config["utm_medium"]
        if source != source.lower() or not SLUG_RE.fullmatch(source):
            fail(f"{key}: invalid utm_source {source!r}")
        if medium not in ALLOWED_MEDIUMS:
            fail(f"{key}: unsupported utm_medium {medium!r}")

    for campaign in campaigns:
        if not SLUG_RE.fullmatch(campaign):
            fail(f"Invalid campaign slug {campaign!r}")

    for name, item in taxonomy.get("ready_links", {}).items():
        destination = urlsplit(item["destination"])
        tracked = urlsplit(item["tracked_url"])
        if tracked.scheme != base_parts.scheme or tracked.netloc != base_parts.netloc:
            fail(f"{name}: tracked URL must stay on canonical SigGear host")
        if (destination.scheme, destination.netloc, destination.path) != (
            tracked.scheme,
            tracked.netloc,
            tracked.path,
        ):
            fail(f"{name}: tracked URL destination path changed")
        params = parse_qs(tracked.query)
        for field in ("utm_source", "utm_medium", "utm_campaign", "utm_content"):
            if len(params.get(field, [])) != 1:
                fail(f"{name}: expected exactly one {field}")
        source = params["utm_source"][0]
        medium = params["utm_medium"][0]
        campaign = params["utm_campaign"][0]
        content = params["utm_content"][0]
        if source not in {v["utm_source"] for v in sources.values()}:
            fail(f"{name}: unknown source {source!r}")
        expected_medium = next(v["utm_medium"] for v in sources.values() if v["utm_source"] == source)
        if medium != expected_medium:
            fail(f"{name}: medium {medium!r} does not match source {source!r}")
        if campaign not in campaigns:
            fail(f"{name}: unknown campaign {campaign!r}")
        if not SLUG_RE.fullmatch(content):
            fail(f"{name}: invalid content slug {content!r}")

    for key, path in PLATFORM_PATHS.items():
        platform = load_yaml(path)
        tracking = platform.get("tracking", {})
        source_config = sources[key]
        for field in ("utm_source", "utm_medium", "utm_campaign"):
            if field not in tracking:
                fail(f"{key}: missing tracking.{field}")
        if tracking["utm_source"] != source_config["utm_source"]:
            fail(f"{key}: source differs from taxonomy")
        if tracking["utm_medium"] != source_config["utm_medium"]:
            fail(f"{key}: medium differs from taxonomy")
        if tracking["utm_campaign"] not in campaigns:
            fail(f"{key}: campaign not defined in taxonomy")

    print("UTM taxonomy and platform tracking configuration validated.")


if __name__ == "__main__":
    main()
