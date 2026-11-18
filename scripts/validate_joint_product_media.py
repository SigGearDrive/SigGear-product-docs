#!/usr/bin/env python3
"""Check six joint product images, public CAD honesty and built reference PDFs."""
from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote
import re
import xml.etree.ElementTree as ET

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MODELS = {
    "SG-6010C": ("robot-joint-actuators","sg6010c"),
    "SG-6010D": ("robot-joint-actuators","sg6010d"),
    "SG-8021": ("robot-joint-actuators","sg8021"),
    "CPM-78-39": ("cycloidal-joint-modules","cpm78-39"),
    "CPM-80-25": ("cycloidal-joint-modules","cpm80-25"),
    "CPM-100-25": ("cycloidal-joint-modules","cpm100-25"),
}
STEP_ALLOWED = {
    "SG-6010C": ["SG-6010C_Public_Simplified_STEP_v1.0.step"],
    "CPM-80-25": [
        "CPM-80-25_Public_Simplified_STEP_v1.0_No_Driver.step",
        "CPM-80-25_Public_Simplified_STEP_v1.0_Integrated_Driver.step",
    ],
}

def main() -> None:
    for model, (family, slug) in MODELS.items():
        page = DOCS / "products" / family / (slug+".md")
        text = page.read_text(encoding="utf-8")
        pdf = DOCS / "assets/downloads/joint-actuators" / (
            model+"_Public_Reference_Datasheet_Rev0.1.pdf"
        )
        if not pdf.is_file() or pdf.stat().st_size < 2000:
            raise ValueError("Missing generated reference PDF: "+model)
        raw=pdf.read_bytes()
        if not raw.startswith(b"%PDF-") or b"%%EOF" not in raw[-200:]:
            raise ValueError("Invalid PDF signature: "+model)
        if pdf.name not in text:
            raise ValueError("Product page lacks PDF direct link: "+model)

        paths = re.findall(r'<img\b[^>]*\bsrc=["\x27]([^"\x27]+)', text)
        if len(paths) != len(set(paths)):
            raise ValueError("Duplicate product image references: "+model)
        if model == "CPM-78-39" and paths:
            raise ValueError("CPM-78-39 has no verified repository product image yet")
        for url in paths:
            if url.startswith(("http:","https:","data:")):
                raise ValueError("Hotlinked or synthetic image in standard page: "+model)
            file=(page.parent / unquote(url.split("?")[0])).resolve()
            if not file.is_relative_to(DOCS) or not file.is_file():
                raise ValueError("Missing or unsafe product image "+model+" "+url)
            if file.suffix.lower() == ".svg":
                root=ET.parse(file).getroot()
                if root.tag.rsplit("}",1)[-1] != "svg":
                    raise ValueError("Invalid SVG "+str(file))
            elif file.suffix.lower() == ".webp":
                header=file.read_bytes()[:16]
                if header[:4] != b"RIFF" or header[8:12] != b"WEBP":
                    raise ValueError("Invalid WebP header "+str(file))
                with Image.open(file) as img:
                    img.verify()
            else:
                raise ValueError("Unexpected image format "+str(file))

        step_names = re.findall(r'(?i)[\w-]+\.step', text)
        expected=STEP_ALLOWED.get(model,[])
        for name in expected:
            if name not in text:
                raise ValueError("Missing approved public STEP link: "+model+" "+name)
        if not expected and step_names:
            raise ValueError("Unreleased joint CAD advertised on "+model)
        if not expected and "No downloadable STEP is currently approved" not in text:
            raise ValueError("CAD release status is missing on "+model)
        if len(text)>4800:
            raise ValueError("Joint product page too long for quick-download UX: "+model)
        print("PASS",model,"PDF",pdf.stat().st_size,"images",len(paths),"STEP",len(expected))
    print("PASS six joint-module catalogue reference PDFs, image integrity and CAD release gates")

if __name__ == "__main__":
    main()
