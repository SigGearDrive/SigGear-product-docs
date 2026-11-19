#!/usr/bin/env python3
"""Build six standard and separate SG-6010HB public-reference datasheets from catalogue YAML.

No claims are inferred. These are preliminary catalogue summaries, NOT a
controlled production drawing, final electrical variant, or CAD release.
"""
from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape
import re

import yaml
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/products"
OUT = ROOT / "docs/assets/downloads/joint-actuators"
REVISION = "Rev0.1"
RELEASE_DATE = "2026-11-18"
MODELS = {
    "SG-6010C": "sg-6010c",
    "SG-6010D": "sg-6010d",
    "SG-8021": "sg-8021",
    "SG-6010HB": "sg-6010hb",
    "CPM-78-39": "cpm-78-39",
    "CPM-80-25": "cpm-80-25",
    "CPM-100-25": "cpm-100-25",
}
NAVY = colors.HexColor("#16396B")
BLUE = colors.HexColor("#2366A2")
PALE = colors.HexColor("#F0F5FA")
GRAY = colors.HexColor("#536173")

def ascii_technical(value: object) -> str:
    s = str(value)
    for a, b in [
        ("\u2013", "-"), ("\u2014", "-"), ("\u2212", "-"),
        ("\u00b1", "+/-"), ("\u00b0", " deg"), ("\u00b5", "u"),
        ("\u03bc", "u"), ("\u03a9", "Ohm"), ("\u00d7", "x"),
        ("\u00b7", "."), ("\u2264", "<="), ("\u2265", ">="),
        ("\u223c", "~"), ("\u2019", "'"), ("\u00a0", " "),
    ]:
        s = s.replace(a, b)
    s = re.sub(r"[^\x20-\x7e]", "", s)
    return s

def p(text: object, style: ParagraphStyle) -> Paragraph:
    return Paragraph(escape(ascii_technical(text)), style)

def draw_footer(canvas, document) -> None:
    canvas.saveState()
    width, _ = A4
    canvas.setStrokeColor(colors.HexColor("#C8D4E1"))
    canvas.line(35, 45, width - 35, 45)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(GRAY)
    canvas.drawString(36, 33, "Guangdong SigGear Drive Intelligent Technology Co., Ltd. | siggear.com")
    canvas.drawRightString(width - 36, 33, "Public reference | Page %d" % document.page)
    canvas.restoreState()

def make_datasheet(model: str, filename: str) -> Path:
    obj = yaml.safe_load((DATA / (filename + ".yml")).read_text(encoding="utf-8"))
    if obj.get("model") != model or obj.get("public_page_status") != "published":
        raise ValueError("Missing published product data for " + model)
    values = obj["published_specifications"]
    # Keep the distinct SG-6010HB PDF compact and source-backed; full
    # electrical/controller detail stays on the online technical pages.
    if model == "SG-6010HB":
        core_keys = (
            "transmission_structure", "outer_diameter", "product_thickness",
            "reduction_ratio", "backlash", "motor_power", "rated_voltage",
            "rated_output_speed", "no_load_output_speed", "rated_output_torque",
            "peak_output_torque", "weight", "allowable_radial_force",
            "allowable_axial_force", "motor_structure", "motor_torque_constant",
        )
        if any(key not in values for key in core_keys):
            raise ValueError("SG-6010HB lacks a required catalog key")
        values = {key: values[key] for key in core_keys}
    variants = obj.get("published_variants") or {}
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / f"{model}_Public_Reference_Datasheet_{REVISION}.pdf"
    release_date = "2026-11-19" if model == "SG-6010HB" else RELEASE_DATE
    doc = SimpleDocTemplate(str(target), pagesize=A4, leftMargin=35, rightMargin=35,
                            topMargin=38, bottomMargin=58,
                            title=f"{model} Public Reference Datasheet {REVISION} | SigGear",
                            author="Guangdong SigGear Drive Intelligent Technology Co., Ltd.",
                            subject="Preliminary engineering catalogue specifications; configuration-specific approval required")
    width = A4[0] - 70
    small = ParagraphStyle("small", fontName="Helvetica", fontSize=8, leading=11, textColor=GRAY)
    body = ParagraphStyle("body", fontName="Helvetica", fontSize=8.6, leading=12)
    val_style = ParagraphStyle("value", parent=body, fontName="Helvetica-Bold", fontSize=8.4)
    sec = ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=10.5, leading=15, textColor=NAVY, spaceBefore=8, spaceAfter=4)
    banner = ParagraphStyle("banner", fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=NAVY)
    story = [
        Paragraph("SIGGEAR  /  ENGINEERING RESOURCES", ParagraphStyle("mast", fontName="Helvetica-Bold", fontSize=9, textColor=BLUE, leading=13)),
        Spacer(1, 7), Paragraph(model, banner),
        p(obj.get("display_name", model), ParagraphStyle("subtitle", parent=body, fontSize=10, leading=14)),
        Spacer(1, 9),
    ]
    t = Table([[p("PUBLIC CATALOGUE REFERENCE - " + REVISION + " - " + release_date, 
                  ParagraphStyle("tag",fontName="Helvetica-Bold",fontSize=8,leading=12,textColor=NAVY))]],
              colWidths=[width])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PALE),("BOX",(0,0),(-1,-1),0.5,colors.HexColor("#CBD9E7")),("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8),("LEFTPADDING",(0,0),(-1,-1),10)]))
    story.extend([t,Spacer(1,12)])
    quick_keys = [("outer_diameter","Diameter"),("reduction_ratio","Reduction"),("rated_output_torque","Rated output torque"),("rated_output_speed","Rated output speed")]
    quick = [[p(k, small) for _,k in quick_keys],
             [p(values.get(k,"Refer to specification"), val_style) for k,_ in quick_keys]]
    q = Table(quick,colWidths=[width/4]*4,rowHeights=[19,24])
    q.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),PALE),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),9),
        ("LINEBELOW",(0,0),(-1,0),0.4,colors.HexColor("#CBD9E7")),
    ]))
    story.extend([q,Spacer(1,11),Paragraph("Published technical specifications",sec)])
    entries = list(values.items())
    halfway = (len(entries)+1)//2
    left,right=entries[:halfway],entries[halfway:]
    cells=[]
    for i in range(halfway):
        row=[]
        for chunk in [left,right]:
            if i < len(chunk):
                key,val=chunk[i]
                row.extend([p(key.replace("_"," ").capitalize(),small),p(val,body)])
            else:
                row.extend(["",""])
        cells.append(row)
    spec=Table(cells,colWidths=[133,128,133,width-394],hAlign="LEFT")
    spec.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LINEBELOW",(0,0),(-1,-1),0.35,colors.HexColor("#DEE5EC")),
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[colors.white,colors.HexColor("#F7FAFD")]),
        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
        ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
    ]))
    story.append(spec)
    if variants:
        story.append(Paragraph("Configuration-specific variants (not standard by default)",sec))
        vr=[[p(k,small),p(v,body)] for k,v in variants.items()]
        tab=Table(vr,colWidths=[225,width-225],hAlign="LEFT")
        tab.setStyle(TableStyle([
            ("VALIGN",(0,0),(-1,-1),"MIDDLE"),("ROWBACKGROUNDS",(0,0),(-1,-1),[colors.white,colors.HexColor("#F7FAFD")]),
            ("LINEBELOW",(0,0),(-1,-1),.3,colors.HexColor("#DEE5EC")),
            ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
        ]))
        story.append(tab)
    story.extend([Spacer(1,10),Paragraph("Configuration and release scope",sec)])
    cfg=obj.get("configuration_summary") or ""
    story.append(p(cfg,body))
    if model == "CPM-78-39":
        story.append(p("Standard: Hall sensors only; no integrated driver or absolute encoder claim.",body))
    elif model == "SG-6010D":
        story.append(p("CAN Simple / CANopen / RS485 applies only to the confirmed driver-equipped hardware and firmware.",body))
    elif model == "SG-6010HB":
        story.append(p(
            "CAD release hold: supplied SG2908B exchange-assembly STEP is not "
            "verified against the catalog 67.0 mm x 25.57 mm envelope. "
            "Neither the raw assembly STEP nor a controlled 2D production drawing "
            "is publicly released. Request configuration-matched design files.", body))
        story.append(p(
            "Driver caution: actuator catalog says 12-48 V; the referenced driver "
            "platform lists 15-48 V for rated operation.", body))
    note=("Preliminary catalogue data. Peak torque is not a continuous rating. "
          "Controlled 2D mechanical interfaces, connector pinout, electronics/firmware and "
          "installation dimensions must be confirmed for the ordered configuration.")
    story.extend([Spacer(1,6),p(note,small)])
    online=obj.get("canonical_page","").removeprefix("docs/").removesuffix(".md")+"/"
    url="https://siggeardrive.github.io/SigGear-product-docs/"+online
    link_style=ParagraphStyle("link",fontName="Helvetica",fontSize=8,leading=11,textColor=BLUE,spaceBefore=8)
    story.append(Paragraph('Online technical references: <link href="%s"><u>%s</u></link>' % (url,escape(model+" specifications and CAD status")),link_style))
    doc.build(story,onFirstPage=draw_footer,onLaterPages=draw_footer)
    if target.stat().st_size < 2000 or not target.read_bytes().startswith(b"%PDF-"):
        raise ValueError("Generated PDF is missing or invalid: " + str(target))
    return target

def main() -> None:
    for model,filename in MODELS.items():
        target=make_datasheet(model,filename)
        print("PDF",model,target.stat().st_size,str(target.relative_to(ROOT)))

if __name__ == "__main__":
    main()
