#!/usr/bin/env python3
"""Verify 2877/2878 public PDF source status, page links and no false STEP."""
from pathlib import Path
import re
import yaml
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/"docs"
SITE=ROOT/"site"
DATA=ROOT/"data/products"
SOURCE=ROOT/"data/engineering/hub-motor-reference-sources-20261119.yml"
FILES=DOCS/"assets/downloads/hub-gear-motors"

def req(ok,msg):
    if not ok:raise ValueError(msg)

def main():
    audit=yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
    req(audit["excluded_reference"]["label"]=="SG2557-80PG-9.75B",
        "Different IP66/old-model source must remain excluded")
    family=(DOCS/"products/hub-gear-motors/index.md").read_text(encoding="utf-8")
    familyhtml=(SITE/"products/hub-gear-motors/index.html").read_text(encoding="utf-8")
    for model,slug in (("SG-2877","sg2877"),("SG-2878","sg2878")):
        data=yaml.safe_load((DATA/(model.lower()+".yml")).read_text(encoding="utf-8"))
        source=audit["models"][model]
        req(data["model"]==source["public_model"]==model,"Product identity mismatch "+model)
        req(source["source_drawing_rev"]=="A" and source["source_drawing_date"]=="2025-07-04",
            "Supplier source date/revision changed "+model)
        req(source["source_parasolid_format"].endswith("(not STEP)"),
            "Source CAD was not received as STEP "+model)
        req(source["cad_release"]=="not_yet_verified_for_public_download",
            "Unverified CAD prematurely released "+model)
        req(len(source["test_points"])==4,"Missing 24 V test points "+model)
        pdf=model+"_Public_Reference_Datasheet_Rev0.1.pdf"
        asset=FILES/pdf
        siteasset=SITE/"assets/downloads/hub-gear-motors"/pdf
        req(asset.is_file() and siteasset.is_file() and asset.stat().st_size>=4000,
            "Public source PDF missing "+model)
        reader=PdfReader(str(asset),strict=False)
        req(len(reader.pages)==2,"Expected concise two-page reference PDF "+model)
        text=" ".join((page.extract_text() or "") for page in reader.pages)
        for marker in (model,"PUBLIC CATALOGUE REFERENCE","24 V factory-source test observations",
                       source["drawing_overall_length"],source["source_parasolid_format"]):
            req(marker in text,"Public PDF missing "+model+" marker: "+marker)
        req(asset.read_bytes()==siteasset.read_bytes(),"Published PDF differs from source "+model)
        modeldoc=(DOCS/f"products/hub-gear-motors/{slug}.md").read_text(encoding="utf-8")
        html=(SITE/f"products/hub-gear-motors/{slug}/index.html").read_text(encoding="utf-8")
        for doc in (modeldoc,html,family,familyhtml):
            req(pdf in doc,"Missing direct PDF button "+model)
            req("SG2557-80PG-9.75B" not in doc,"Wrong model source leaked to customer page")
        req(modeldoc.index(pdf)<modeldoc.index("## Product Overview"),"PDF not visible first-screen "+model)
        req(".x_t" in modeldoc and "not a verified STEP" in modeldoc,
            "Source Parasolid status not clear "+model)
        req(not re.search(r"\]\([^)]+\.(?:step|stp|x_t)\)",modeldoc,re.I),
            "Model page wrongly advertises unverified CAD as a direct download "+model)
        req(("SG2877-3Nm" if model=="SG-2877" else "SG2878-6Nm") in text,
            "Source drawing identity missing "+model)
        if model=="SG-2878":
            for marker in ("125 mm","127 +/-0.5 mm"):
                req(marker in modeldoc and marker in text,
                    "SG-2878 drawing versus catalog length issue hidden: "+marker)
        print("PASS",model,"2-page PDF, source test points, first-screen download, CAD hold")
    print("PASS both hub motor source-backed references and original drawing boundary")

if __name__=="__main__":main()
