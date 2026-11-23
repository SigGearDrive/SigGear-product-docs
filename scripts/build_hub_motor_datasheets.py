#!/usr/bin/env python3
"""Generate source-backed SG-2877 / SG-2878 PUBLIC REFERENCE PDF datasheets.

This script intentionally publishes no unverified 2D file or Parasolid geometry.
Performance points are source-test data, not continuous or allowable peak ratings.
"""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, PageBreak, Table, TableStyle
import yaml

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data/products"
AUDIT=ROOT/"data/engineering/hub-motor-reference-sources-20261119.yml"
OUT=ROOT/"docs/assets/downloads/hub-gear-motors"
NAVY=colors.HexColor("#183D72")
PALE=colors.HexColor("#ECF3F9")
BLUE=colors.HexColor("#236BA4")
BORDER=colors.HexColor("#D2DDE9")
GRAY=colors.HexColor("#4B5968")
REV="Rev0.1"
DATE="2026-11-19"

SMALL=ParagraphStyle("small",fontName="Helvetica",fontSize=7.8,leading=11.2,textColor=GRAY)
BODY=ParagraphStyle("body",fontName="Helvetica",fontSize=8.5,leading=12.0)
LABEL=ParagraphStyle("label",parent=SMALL,fontSize=8.1)
VALUE=ParagraphStyle("value",fontName="Helvetica-Bold",fontSize=8.4,leading=12)
HEADER=ParagraphStyle("header",fontName="Helvetica-Bold",fontSize=19,leading=23,textColor=NAVY)
SECTION=ParagraphStyle("section",fontName="Helvetica-Bold",fontSize=10.8,leading=15,textColor=NAVY,spaceBefore=10,spaceAfter=5)
WHITE=ParagraphStyle("white",fontName="Helvetica-Bold",fontSize=7.8,leading=10,textColor=colors.white)

def par(s,style=BODY):
    return Paragraph(escape(str(s)),style)

def foot(can,doc):
    can.saveState()
    w,h=A4
    can.setFillColor(NAVY);can.rect(0,h-11,w,11,stroke=0,fill=1)
    can.setStrokeColor(BORDER);can.line(35,47,w-35,47)
    can.setFillColor(GRAY);can.setFont("Helvetica",7)
    can.drawString(35,34,"Guangdong SigGear Drive Intelligent Technology Co., Ltd. | siggear.com")
    can.drawRightString(w-35,34,"Public reference | "+REV+" | Page "+str(doc.page))
    can.restoreState()

def table(rows,widths,pad=6,heading=False,shade=True):
    t=Table(rows,colWidths=widths,repeatRows=1 if heading else 0,hAlign="LEFT")
    style=[
      ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
      ("LEFTPADDING",(0,0),(-1,-1),pad),("RIGHTPADDING",(0,0),(-1,-1),pad),
      ("TOPPADDING",(0,0),(-1,-1),pad),("BOTTOMPADDING",(0,0),(-1,-1),pad),
      ("LINEBELOW",(0,0),(-1,-1),0.35,BORDER),
    ]
    if shade:style.append(("ROWBACKGROUNDS",(0,0),(-1,-1),[colors.white,colors.HexColor("#F7FAFC")]))
    if heading:style.append(("BACKGROUND",(0,0),(-1,0),NAVY))
    t.setStyle(TableStyle(style))
    return t

def banner(model,info):
    return [
      Paragraph("SIGGEAR / ELECTROMECHANICAL TRANSMISSION",
                ParagraphStyle("brand",fontName="Helvetica-Bold",fontSize=9,textColor=BLUE,leading=14)),
      Spacer(1,7),Paragraph(model,HEADER),
      par(("3 Nm" if model=="SG-2877" else "6 Nm")+" Hub Gear Motor | 24 VDC | Planetary 9.75:1",SMALL),
      Spacer(1,11),
      table([[par("PUBLIC CATALOGUE REFERENCE  |  "+REV+"  |  "+DATE,VALUE)]],[A4[0]-70],pad=9,shade=False),
      Spacer(1,12)
    ]

def build(model,info,source):
    spec=info["published_specifications"]
    OUT.mkdir(parents=True,exist_ok=True)
    dst=OUT/(model+"_Public_Reference_Datasheet_"+REV+".pdf")
    doc=SimpleDocTemplate(str(dst),pagesize=A4,leftMargin=35,rightMargin=35,topMargin=35,bottomMargin=59,
                          title=model+" Public Reference Datasheet "+REV,
                          author="Guangdong SigGear Drive Intelligent Technology Co., Ltd.")
    width=A4[0]-70
    flow=banner(model,info)
    metrics=[
      ("DIAMETER",spec["outer_diameter"]),
      ("RATED TORQUE",spec["rated_torque"]),
      ("RATED SPEED",spec["rated_speed"]),
      ("RATIO",spec["reduction_ratio"])
    ]
    flow.append(table([[par(k,LABEL) for k,v in metrics],
                       [par(v,VALUE) for k,v in metrics]],[width/4]*4,pad=8))
    flow.append(Paragraph("Published specifications",SECTION))
    items=[
      ("Rated voltage",spec["rated_voltage"]),("Rated motor power",spec["rated_power"]),
      ("Rated current",spec["rated_current"]),("No-load output speed",spec["no_load_speed"]),
      ("Rated output speed",spec["rated_speed"]),("Rated output torque",spec["rated_torque"]),
      ("Momentary peak torque",spec["peak_torque"]),("Reduction ratio",spec["reduction_ratio"]),
      ("Housing diameter",spec["outer_diameter"]),("Body thickness",source["drawing_body_thickness"]),
      ("Published overall length",spec["overall_length_including_shaft"]),
      ("Source 2D overall",source["drawing_overall_length"]),
      ("Gear / housing",source["gear_material"]+" / "+source["housing_material"]),
      ("Mechanical backlash",spec["backlash"]),("Ingress protection",spec["waterproof_rating"]),
      ("Weight",spec["weight"]),
    ]
    half=(len(items)+1)//2
    rows=[]
    for i in range(half):
        row=[]
        for part in (items[:half],items[half:]):
            row += [par(part[i][0],LABEL),par(part[i][1])] if i<len(part) else ["",""]
        rows.append(row)
    flow.append(table(rows,[117,147,117,width-381],pad=5))
    flow.append(Paragraph("Motor / controller reference",SECTION))
    electrical=[
      ("Standard feedback","Hall sensors, "+source["hall_angle"]),
      ("Motor structure",source["motor_topology"]),
      ("Insulation",source["insulation_class"]),
      ("Motor rated load",source["motor_rated_load"]),
      ("Phase resistance",source["phase_resistance"]),
      ("Phase inductance",source["phase_inductance"]),
      ("Full-range phase current","15 A max (catalogue)"),
      ("Rated bus-current limit","7.5 A max (catalogue)"),
      ("Locked-rotor current","< 8 A (catalogue)"),
    ]
    h=(len(electrical)+1)//2
    rows=[]
    for i in range(h):
        row=[]
        for part in (electrical[:h],electrical[h:]):
            row += [par(part[i][0],LABEL),par(part[i][1])] if i<len(part) else ["",""]
        rows.append(row)
    flow.append(table(rows,[117,147,117,width-381],pad=4))
    flow.append(Spacer(1,8))
    flow.append(par("Standard: BLDC motor, planetary reduction and Hall feedback. External controller required unless explicitly included. No standard CANopen, RS485, integrated driver or full control kit is claimed.",SMALL))
    flow.append(PageBreak())
    flow+=banner(model,info)
    flow.append(Paragraph("24 V factory-source test observations",SECTION))
    flow.append(par("Feature points copied from the supplied performance table. Ambient: "+source["ambient"]+". These are bench measurements, not permissible continuous duty points."))
    flow.append(Spacer(1,8))
    cols=["Feature point","Speed rpm","Torque N.m","Out W","U V","I A","In W","Eff."]
    rows=[[par(x,WHITE) for x in cols]]
    rows += [[par(x) for x in row] for row in source["test_points"]]
    flow.append(table(rows,[101,57,63,53,52,57,52,width-435],pad=5,heading=True))
    flow.append(Spacer(1,9))
    flow.append(par("The test table may include loads above the published momentary peak-torque rating. Maximum torque in a test is NOT a safe rated or peak operating limit.",SMALL))
    flow.append(Paragraph("Mechanical reference / CAD status",SECTION))
    drawing=[
      ("Reference drawing",source["original_2d_label"]+" / revision "+source["source_drawing_rev"]),
      ("Drawing date",source["source_drawing_date"]),
      ("Drawing outer diameter",source["drawing_diameter"]),
      ("Drawing overall length",source["drawing_overall_length"]),
      ("3D exchange format",source["source_parasolid_format"]),
      ("2D source release","Reference drawing only; not approved manufacturing tolerances"),
      ("CAD release","Source geometry not validated for public integration")
    ]
    flow.append(table([[par(k,LABEL),par(v)] for k,v in drawing],[173,width-173],pad=6))
    flow.append(Paragraph("Source reconciliation and design-in",SECTION))
    flow.append(par(source["source_discrepancy"]))
    flow.append(Spacer(1,7))
    for msg in (
      "Confirm version-matched pilot, shaft, housing envelope and mounting requirements with SigGear engineering.",
      "Choose controller, continuous duty, ambient temperature and protection method for final assembly. Peak torque is not the continuous rating.",
      "This PDF is a public reference. Do not substitute it for the original 2D drawing, factory-controlled tolerances or an approved Parasolid / STEP design release."
    ):
        flow.append(par("- "+msg,SMALL));flow.append(Spacer(1,5))
    flow.append(Spacer(1,11))
    flow.append(Paragraph("Engineering enquiries",SECTION))
    flow.append(par("luffy@siggear.com  |  www.siggear.com",SMALL))
    doc.build(flow,onFirstPage=foot,onLaterPages=foot)
    if not dst.read_bytes().startswith(b"%PDF-"):raise ValueError("Bad generated PDF "+str(dst))
    return dst


def build_interface_reference(model,source):
    """Source-derived DIMENSION CHECKLIST only, never a reproduction of controlled 2D."""
    OUT.mkdir(parents=True,exist_ok=True)
    dst=OUT/(model+"_Source_Dimension_Reference_Rev0.1.pdf")
    doc=SimpleDocTemplate(str(dst),pagesize=A4,leftMargin=35,rightMargin=35,
        topMargin=35,bottomMargin=59,
        title=model+" Mechanical Dimension Reference Rev0.1",
        author="Guangdong SigGear Drive Intelligent Technology Co., Ltd.")
    width=A4[0]-70
    values=[
       ("Nominal housing outer diameter","99 mm (catalogue)"),
       ("Drawing body thickness",source["drawing_body_thickness"]),
       ("Overall length shown in Rev A source",source["drawing_overall_length"]),
       ("Front mounting pilot / locating diameter","80.8 +0/-0.15 mm"),
       ("Reference face diameter","93 +/-0.1 mm"),
       ("Rear interface reference diameter","84 +/-0.1 mm"),
       ("Output shaft / internal bore","16 -0.05/-0.12 mm / 10.5 mm"),
       ("Output shaft reference length","28 +0/-0.2 mm"),
       ("Drawing rear face mounting","4 x M4 equally spaced"),
       ("Source drawing identifier",source["original_2d_label"]),
       ("Source drawing revision / date","A / 2025-07-04"),
    ]
    story=banner(model,{"display_name":model})
    story.append(Paragraph("Mechanical dimension checklist - 2D source reference",SECTION))
    story.append(par("Values transcribed from the supplied 2025-07-04 Rev A 2D drawing. This sheet is a searchable, simplified dimensional reference and is NOT the original 2D drawing, a released STEP or a tolerance-controlled manufacturing drawing."))
    story.append(Spacer(1,11))
    story.append(table([[par(x,LABEL),par(y)] for x,y in values],[225,width-225],pad=8))
    story.append(Spacer(1,12))
    story.append(Paragraph("Configuration and release control",SECTION))
    story.append(par(source["source_discrepancy"]))
    story.append(Spacer(1,8))
    story.append(par("The source assembly is Parasolid .x_t, not STEP. Its exact geometry has not been validated for public integration. Use the original engineering drawing and configuration-matched source CAD only after engineering approval."))
    story.append(Spacer(1,8))
    story.append(par("This checklist is not a substitute for mounting pitch circle dimensions, hole depth, wiring routing, tolerances, seal compression, shaft engagement or installation datum review."))
    story.append(Spacer(1,16))
    story.append(Paragraph("Request original 2D / approved CAD",SECTION))
    story.append(par("Contact luffy@siggear.com | siggear.com",SMALL))
    doc.build(story,onFirstPage=foot,onLaterPages=foot)
    if not dst.read_bytes().startswith(b"%PDF-"):
        raise ValueError("Bad mechanical reference PDF "+str(dst))
    return dst

def build_separate_2557_source_reference(source):
    """An independently labelled 2024 Rev A SOURCE CHECKLIST, not original 2D."""
    model = source["label"]
    if model != "SG2557-80PG-9.75B":
        raise ValueError("Unexpected separately sourced model")
    OUT.mkdir(parents=True, exist_ok=True)
    dst = OUT / (model + "_Source_Dimension_Reference_Rev0.1.pdf")
    doc = SimpleDocTemplate(
        str(dst), pagesize=A4, leftMargin=35, rightMargin=35,
        topMargin=35, bottomMargin=59,
        title=model + " Source Dimension Reference Rev0.1",
        author="Guangdong SigGear Drive Intelligent Technology Co., Ltd.",
    )
    width = A4[0] - 70
    brand = ParagraphStyle(
        "source-brand", fontName="Helvetica-Bold", fontSize=9,
        leading=13, textColor=BLUE
    )
    story = [
        Paragraph("SIGGEAR / HISTORICAL ENGINEERING SOURCE REFERENCE", brand),
        Spacer(1, 8),
        Paragraph(model, HEADER),
        par("24 VDC BLDC hub motor and planetary reduction | Source drawing: Rev A / 2024-05-21", SMALL),
        Spacer(1, 10),
        par("PUBLIC SOURCE TRANSCRIPTION | Rev0.1 | 2026-11-19", VALUE),
        Spacer(1, 10),
        par("This older, independent model must not be confused with the SG-2877 or SG-2878 product configurations. Current production availability and the revision-matched installation drawing have not been confirmed.", SMALL),
        Paragraph("Source motor and output data", SECTION),
    ]
    electrical = [
        ("Nominal voltage", "24 VDC"),
        ("Motor rated current", "< 3 A (drawing)"),
        ("Motor rated speed", "1,500 +/-10% rpm"),
        ("Motor rated load", "0.3 N.m"),
        ("Motor locked-rotor current", "< 8 A"),
        ("Planetary reduction ratio", "9.75:1"),
        ("Output rated current", "< 3 A (drawing)"),
        ("Output rated speed", "130 +/-10% rpm"),
        ("Output rated torque", "3 N.m"),
        ("Source peak output torque", "10 N.m (duration / duty limit not specified)"),
        ("Ingress-protection note", "IP66 requirement on original drawing; no independent certification supplied"),
    ]
    story.append(table([[par(k, LABEL), par(v)] for k, v in electrical], [190, width-190], pad=4.5))
    story.append(Paragraph("Dimensional checklist - source dimensions only", SECTION))
    mechanical = [
        ("Axial drawing reference", "116.00 mm; not verified as full overall installed length"),
        ("Additional axial segment", "63 +/-0.1 mm"),
        ("Front feature diameters", "93 +/-0.10 mm; 80 +0/-0.15 mm"),
        ("Rear reference diameter", "84 +/-0.10 mm"),
        ("Shaft / internal bore", "16 -0.05/-0.12 mm / 10.50 mm"),
        ("Shaft projection reference", "28 +0/-0.2 mm"),
        ("Wiring", "3 motor phase leads + 6 Hall/sensor leads; lead length is customer-specific"),
    ]
    story.append(table([[par(k, LABEL), par(v)] for k, v in mechanical], [190, width-190], pad=4.5))
    story.append(Spacer(1, 8))
    story.append(par("Source: SG2557-80PG-9.75B hub reduction assembly drawing, Rev A, 2024-05-21. Technical notes also call for RoHS compliance and more than 72 h salt-spray appearance resistance; these are source requirements, not verified certificates.", SMALL))
    story.append(Spacer(1, 8))
    story.append(par("This is not the original 2D drawing, a controlled manufacturing document, an approved mounting interface, or a verified STEP / Parasolid download. Confirm tolerances, mounting datum, shaft fit, current production status and peak-duty limit with SigGear engineering before design-in.", SMALL))
    story.append(Spacer(1, 7))
    story.append(par("Engineering requests: luffy@siggear.com | siggear.com", SMALL))
    doc.build(story, onFirstPage=foot, onLaterPages=foot)
    if not dst.read_bytes().startswith(b"%PDF-"):
        raise ValueError("Bad historical source-reference PDF " + str(dst))
    return dst


def main():
    audit=yaml.safe_load(AUDIT.read_text(encoding="utf-8"))
    for model in ("SG-2877","SG-2878"):
        d=yaml.safe_load((DATA/(model.lower()+".yml")).read_text(encoding="utf-8"))
        if d.get("model")!=model:raise ValueError("Missing master data "+model)
        a=audit["models"][model]
        if a["public_model"]!=model or a["cad_release"]!="not_yet_verified_for_public_download":
            raise ValueError("Source identity / release mismatch "+model)
        if len(a["test_points"])!=4:raise ValueError("Expected four source test points")
        p=build(model,d,a)
        print("PDF",model,p.stat().st_size,str(p.relative_to(ROOT)))
        q=build_interface_reference(model,a)
        print("DIMENSION PDF",model,q.stat().st_size,str(q.relative_to(ROOT)))
    legacy=build_separate_2557_source_reference(audit["separate_source_drawing"])
    print("SOURCE-ONLY PDF SG2557",legacy.stat().st_size,str(legacy.relative_to(ROOT)))

if __name__=="__main__":main()
