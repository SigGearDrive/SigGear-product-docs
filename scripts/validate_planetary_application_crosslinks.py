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

        # Model-specific OEM engineering routes must prefill the selected 8P–42P
        # product and the actual project starting point in the live inquiry form.
        expected_routes = (
            ("existing_motor", "gearbox_only"),
            ("drawing_cad", None),
            ("prototype_to_volume", None),
        )
        for start, requested_path in expected_routes:
            prefix = f"../../request-cad-sample-quote.md?model={n}P&start={start}"
            if requested_path:
                prefix += f"&path={requested_path}"
            assert text.count(f"]({prefix})") == 1, (n, start)
            found = False
            for href in links.hrefs:
                resolved = urlsplit(urljoin(base, href))
                if resolved.path != "/SigGear-product-docs/request-cad-sample-quote/":
                    continue
                params = parse_qs(resolved.query)
                if params.get("model") != [f"{n}P"] or params.get("start") != [start]:
                    continue
                if requested_path and params.get("path") != [requested_path]:
                    continue
                found = True
                break
            assert found, (n, start, "prefilled engineering inquiry link not rendered")


    apps={f.stem for f in (DOCS/"applications").glob("*.md") if f.stem not in {"index","planetary-gearbox-application-families"}}
    assert len(apps)==32, f"Unexpected application source count {len(apps)}"
    assert apps==referenced, f"Application coverage differs: missing={sorted(apps-referenced)}, unexpected={sorted(referenced-apps)}"
    print("PASS 12 gearhead models, 32 applications, real engineering downloads, and model-prefilled OEM review routes")

if __name__=="__main__":
    main()
