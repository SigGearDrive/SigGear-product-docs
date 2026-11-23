#!/usr/bin/env python3
"""Validate bidirectional discovery between planetary gearhead models and OEM applications.

These links identify preliminary engineering topics, not approved application ratings.
"""
from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, parse_qs

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/"docs"
SITE=ROOT/"site"
SITE_BASE="https://siggeardrive.github.io/SigGear-product-docs/"
MODELS=[8,10,12,14,16,20,22,24,28,32,36,42]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs=[]
    def handle_starttag(self,tag,attrs):
        if tag=="a":
            href=dict(attrs).get("href")
            if href:
                self.hrefs.append(href)

def main():
    referenced=set()
    for n in MODELS:
        path=DOCS/f"products/planetary-gearboxes/{n}p-planetary-gearbox.md"
        text=path.read_text(encoding="utf-8")
        assert text.count("**Potential OEM applications**")==1, path
        assert "suitability requires engineering review" in text, path
        assert "../../custom-engineering/motor-gearbox-integration.md" in text, path
        for file in (f"{n}P_Planetary_Gearhead_Datasheet_Rev",
                     f"{n}P_2D_Drawing.pdf", f"{n}P_Full_Assembly.step"):
            assert file in text, (n,file)
        slugs=re.findall(r"\]\(\.\./\.\./applications/([a-z0-9-]+)\.md\)",text)
        slugs=[slug for slug in slugs if slug!="index"]
        assert 1<=len(slugs)<=4 and len(slugs)==len(set(slugs)),(n,slugs)
        for slug in slugs:
            assert (DOCS/"applications"/f"{slug}.md").is_file(),(n,slug)
            referenced.add(slug)
        htmlpath=SITE/f"products/planetary-gearboxes/{n}p-planetary-gearbox/index.html"
        assert htmlpath.is_file(), htmlpath
        html=htmlpath.read_text(encoding="utf-8")
        links=Links();links.feed(html)
        base=SITE_BASE+f"products/planetary-gearboxes/{n}p-planetary-gearbox/"
        targets={urlsplit(urljoin(base,x)).path for x in links.hrefs}
        for slug in slugs:
            target=f"/SigGear-product-docs/applications/{slug}/"
            assert target in targets, (n,target)
        assert "/SigGear-product-docs/custom-engineering/motor-gearbox-integration/" in targets,n

        # Customers should be able to email SigGear from the model page
        # without opening another intake form. Keep model and project topic
        # in the email subject for efficient first engineering response.
        mailto_links = [
            href for href in links.hrefs
            if href.startswith("mailto:luffy@siggear.com?subject=")
        ]
        assert mailto_links, (n, "no one-click email inquiry")
        subjects = {
            parse_qs(urlsplit(href).query).get("subject", [""])[0]
            for href in mailto_links
        }
        for topic in ("Existing Motor", "Drawing or STEP", "Prototype to Production"):
            wanted = f"SigGear Engineering Inquiry - {n}P - {topic}"
            assert wanted in subjects, (n, topic, "no topic-specific direct email")
            assert "mailto:luffy@siggear.com?subject=" in text, (n, "missing source mailto")



    apps={f.stem for f in (DOCS/"applications").glob("*.md") if f.stem not in {"index","planetary-gearbox-application-families"}}
    assert len(apps)==32, f"Unexpected application source count {len(apps)}"
    assert apps==referenced, f"Application coverage differs: missing={sorted(apps-referenced)}, unexpected={sorted(referenced-apps)}"
    print("PASS 12 gearhead models, 32 applications, real engineering downloads, and one-click model-context email inquiries")

if __name__=="__main__":
    main()
