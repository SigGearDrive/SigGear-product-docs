#!/usr/bin/env python3
"""Verify that the live inquiry page loads the active FormSubmit JS and its email fallback."""

from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "site/request-cad-sample-quote/index.html"
VERSIONS = {
    "inquiry-form.js": "20261123-luffy-formsubmit-active",
    "inquiry-form.css": "20261123-luffy-mail-safe",
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
        raise ValueError(f"Exactly one {filename} resource must be loaded, got {len(matches)}")
    if VERSIONS[filename] not in matches[0].query:
        raise ValueError(f"{filename} has not been cache-busted: {matches[0].geturl()}")


def main():
    doc = PAGE.read_text(encoding="utf-8")
    parser = Assets()
    parser.feed(doc)
    verify(parser.scripts, "inquiry-form.js")
    verify(parser.styles, "inquiry-form.css")
    for id_ in ("sg-brief-primary", "sg-email-brief",
                "sg-contact-email", "sg-online-consent-wrap"):
        if f'id="{id_}"' not in doc:
            raise ValueError(f"Inquiry page is missing activation control {id_}")
    if "Send Engineering Request Online" not in doc or "Prepare Email Instead" not in doc or "luffy@siggear.com" not in doc:
        raise ValueError("Public brief must offer verified online submission and direct email fallback")
    # Customer-facing wording may change, but the legacy query/form machine
    # values must stay stable for historical product deep links and prefill.
    requirements = (
        ('value="gearbox_only">Planetary gearbox', "Planetary gearbox label missing"),
        ('value="motor_gearbox">Complete motor + gearbox assembly', "Motor + Gearbox label missing"),
        ('href="#engineering-project-brief"', "First-screen form jump missing"),
        ('id="engineering-project-brief"', "Engineering brief anchor missing"),
        ("engineering-resources/motors/", "Motor Datasheet shortcut missing"),
    )
    for marker, message in requirements:
        if marker not in doc:
            raise ValueError(message)
    if "Gearhead only — I already have a motor" in doc:
        raise ValueError("Legacy Gearhead-only customer label still present")
    js_path = ROOT / "docs/assets/javascripts/inquiry-form.js"
    js = js_path.read_text(encoding="utf-8")
    if "var ONLINE_DELIVERY_VERIFIED = true;" not in js:
        raise ValueError("FormSubmit recipient must be enabled after owner-confirmed inbox verification")
    if "https://formsubmit.co/luffy@siggear.com" not in js:
        raise ValueError("Future FormSubmit recipient is not the new approved mailbox")
    for label in ("Planetary Gearbox Engineering Review", "Motor + Gearbox Engineering Review"):
        if label not in js:
            raise ValueError("Outdated customer email subject: " + label)
    for code in ('"gearbox_only"', '"motor_gearbox"'):
        if code not in js or code not in doc:
            raise ValueError("Internal project-path value changed: " + code)
    print("PASS new Luffy FormSubmit online default, verified JS cache key and email fallback")


if __name__ == "__main__":
    main()
