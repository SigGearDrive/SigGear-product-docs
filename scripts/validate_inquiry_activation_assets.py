#!/usr/bin/env python3
"""Verify the customer-facing inquiry routes open direct email without a form."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
VERSIONS = {
    "direct-contact.js": "20261123-direct-email-ux",
    "direct-contact.css": "20261123-direct-email-ux",
}

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
        raise ValueError(f"Expected exactly one {filename}, found {len(matches)}")
    if VERSIONS[filename] not in matches[0].query:
        raise ValueError(f"Stale direct-email asset version: {matches[0].geturl()}")

def main():
    for slug in ("contact", "request-cad-sample-quote"):
        source = (ROOT / "docs" / f"{slug}.md").read_text(encoding="utf-8")
        html = (ROOT / "site" / slug / "index.html").read_text(encoding="utf-8")
        for token in ('class="siggear-direct-email"', "luffy@siggear.com",
                      'class="siggear-direct-contact"', "Luffy Wang",
                      "mailto:luffy@siggear.com?subject=", "Send Your Inquiry by Email"):
            if token not in source or token not in html:
                raise ValueError(f"{slug}: missing direct contact {token}")
        for forbidden in ("<form", "<input", "<textarea", "<select",
                          "FormSubmit", "formsubmit.co", "sg-contact-email", "sg-brief-primary"):
            if forbidden.lower() in source.lower():
                raise ValueError(f"{slug}: old intake form remains: {forbidden}")
        if source.index("luffy@siggear.com") > 900:
            raise ValueError(f"{slug}: public email is too far down the page")
        if "Wanrong Wang" in source or "Wanrong Wang" in html:
            raise ValueError(f"{slug}: outdated public contact name")
        parser = Assets()
        parser.feed(html)
        verify(parser.scripts, "direct-contact.js")
        verify(parser.styles, "direct-contact.css")
    print("PASS: both inquiry pages show first-screen Luffy email, no forms, and versioned assets")

if __name__ == "__main__":
    main()
