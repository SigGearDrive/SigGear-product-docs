#!/usr/bin/env python3
"""Actual visual and raster quality preflight for released SigGear motor datasheets.

Run after the 8 mm original-PDF assembly; use PyMuPDF and Pillow to render real
pages. No source PDF bytes are modified. For a one-time QA review, pass
--emit-preview to print chunked JPEG contact sheets in GitHub Actions logs.
"""
from __future__ import annotations

import argparse
import base64
import io
import json
import re
from pathlib import Path

import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
MOTORS = ROOT / "docs/assets/downloads/motors"
INDEX = ROOT / "docs/engineering-resources/motors/index.md"


def required_pdfs():
    body = INDEX.read_text(encoding="utf-8")
    links = sorted(set(re.findall(
        r"\]\((\.\./\.\./assets/downloads/motors/[^)\s]+\.pdf)(?:\s+\"[^\"]*\")?\)",
        body
    )))
    paths = [(INDEX.parent / rel).resolve() for rel in links]
    if len(paths) != 33 or not all(p.is_file() for p in paths):
        raise RuntimeError(f"Expected 33 real motor PDFs, got {len(paths)}")
    return paths


def quality_record(pdf_file: Path):
    document = fitz.open(pdf_file)
    records = []
    for page in document:
        text_words = len(page.get_text("words"))
        image_records = []
        for image in page.get_images(full=True):
            xref = image[0]
            image_width, image_height = image[2], image[3]
            try:
                rects = page.get_image_rects(xref)
            except Exception:
                rects = []
            for rect in rects:
                if rect.width <= 0 or rect.height <= 0:
                    continue
                visual_width = rect.width / 72
                visual_height = rect.height / 72
                dpi_x = image_width / visual_width
                dpi_y = image_height / visual_height
                significant = visual_width >= 1.0 and visual_height >= 1.0
                image_records.append({
                    "pixel_dimensions": [image_width, image_height],
                    "placed_inches": [round(visual_width,2),round(visual_height,2)],
                    "effective_dpi": round(min(dpi_x,dpi_y)),
                    "large_raster": significant,
                })
        significant_dpi = [x["effective_dpi"] for x in image_records if x["large_raster"]]
        records.append({
            "page": page.number + 1,
            "text_words": text_words,
            "image_objects": len(image_records),
            "large_image_min_dpi": min(significant_dpi) if significant_dpi else None,
        })
    return {
        "file": pdf_file.name,
        "diameter": pdf_file.parent.name,
        "pages": len(document),
        "bytes": pdf_file.stat().st_size,
        "detail": records,
    }


def render_thumbnail(path: Path, page_index: int, width: int) -> Image.Image:
    document = fitz.open(path)
    pg = document[page_index]
    scale = max(.25, width / max(1, pg.rect.width))
    pix = pg.get_pixmap(matrix=fitz.Matrix(scale,scale),colorspace=fitz.csRGB,alpha=False)
    return Image.frombytes("RGB",(pix.width,pix.height),pix.samples)


def emit(label: str, preview: Image.Image) -> None:
    output = io.BytesIO()
    preview.save(output,format="JPEG",quality=53,optimize=True)
    encoded = base64.b64encode(output.getvalue()).decode("ascii")
    print(f"SIGGEAR_MOTOR_QA_IMG_BEGIN {label} {len(encoded)}")
    for i in range(0,len(encoded),2800):
        print(f"SIGGEAR_MOTOR_QA_IMG_CHUNK {label} {i//2800} {encoded[i:i+2800]}")
    print(f"SIGGEAR_MOTOR_QA_IMG_END {label}")


def montage(paths: list[Path]) -> Image.Image:
    representative = {}
    for path in paths:
        representative.setdefault(path.parent.name, path)
    # Use one real, rendered first page from each published motor diameter.
    choices = [representative[f"{d}mm"] for d in [8,10,12,14,16,20,22,24,28,32]]
    cols = 4
    tile_width = 365
    tile_height = 490
    rows = (len(choices)+cols-1)//cols
    canvas = Image.new("RGB",(cols*tile_width,rows*tile_height),"white")
    draw = ImageDraw.Draw(canvas)
    for i,path in enumerate(choices):
        picture = render_thumbnail(path,0,tile_width-22)
        picture.thumbnail((tile_width-24,tile_height-58))
        x = (i%cols)*tile_width+12
        y = (i//cols)*tile_height+34
        canvas.paste(picture,(x,y))
        draw.text((x,y-28),f"{path.parent.name}  {path.name[0:26]}",fill="black")
    return canvas


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--emit-preview",action="store_true")
    args=parser.parse_args()
    paths=required_pdfs()
    results=[quality_record(p) for p in paths]
    total_pages=sum(row["pages"] for row in results)
    uncertain=[]
    for row in results:
        for p in row["detail"]:
            if p["large_image_min_dpi"] is not None and p["large_image_min_dpi"] < 150:
                uncertain.append({"file":row["file"],"page":p["page"],"dpi":p["large_image_min_dpi"]})
    counts={d:sum(x["diameter"]==d for x in results) for d in sorted({x["diameter"] for x in results})}
    print("SIGGEAR_MOTOR_QA_SUMMARY "+json.dumps({
        "pdfs":len(results),"total_pages":total_pages,
        "files_per_diameter":counts,"under_150dpi_large_raster":uncertain[:80],
        "count_low_dpi_pages":len(uncertain),
        "samples":[{"file":x["file"],"pages":x["pages"],"details":x["detail"][:3]} for x in results if x["diameter"] in {"8mm","10mm","22mm","28mm","32mm"}][:13],
    },separators=(",",":")))
    if not args.emit_preview:
        return
    emit("all_diameters",montage(paths))
    chosen=[
        ("motor_8mm_source",next(p for p in paths if "HS-816-Q_Winding_Set_A" in p.name)),
        ("motor_10mm_draft",next(p for p in paths if "10mm_DC_Motor_Series_01" in p.name)),
        ("motor_22mm_sheet02",next(p for p in paths if "22mm_DC_Motor_Sheet02" in p.name)),
        ("motor_28mm_sheetB",next(p for p in paths if "28mm_DC_Motor_SheetB" in p.name)),
        ("motor_32mm_mechB",next(p for p in paths if "32mm_DC_Motor_Series02_MechanicalB" in p.name)),
    ]
    for label,path in chosen:
        with fitz.open(path) as doc:
            page_index=len(doc)-1
        emit(label,render_thumbnail(path,page_index,1050))


if __name__=="__main__":
    main()
