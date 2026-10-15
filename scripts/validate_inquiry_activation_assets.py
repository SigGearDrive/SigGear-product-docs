#!/usr/bin/env python3
"""Verify that the generated online activation page loads current, cache-busted assets."""

from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "site/request-cad-sample-quote/index.html"
VERSION = "20261015-activation-fix"


class Assets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts = []
        self.styles = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "script" and attrs.get("src"):
            self.scripts.append(attrs["src"])
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.styles.append(attrs.get("href", ""))


def verify(items, filename):
    matches = [urlsplit(s) for s in items if filename in s]
    if len(matches) != 1:
        raise ValueError(f"Exactly one {filename} resource must be loaded, got {len(matches)}")
    if VERSION not in matches[0].query:
        raise ValueError(f"{filename} has not been cache-busted: {matches[0].geturl()}")


def main():
    doc = PAGE.read_text(encoding="utf-8")
    parser = Assets()
    parser.feed(doc)
    verify(parser.scripts, "inquiry-form.js")
    verify(parser.styles, "inquiry-form.css")
    for id_ in ("sg-brief-primary", "sg-email-brief",
                "sg-online-activation-indicator", "sg-online-consent-wrap"):
        if f'id="{id_}"' not in doc:
            raise ValueError(f"Inquiry page is missing activation control {id_}")
    print("PASS online activation: one current JS/CSS asset and all test-mode controls")


if __name__ == "__main__":
    main()
