#!/usr/bin/env python3
"""Check six joint product images, public CAD honesty and built reference PDFs."""
from __future__ import annotations

from pathlib import Path
import hashlib
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
    "SG-6010C": [
        "SG-6010C_Original_Full_Assembly_20261118.step",
        "SG-6010C_Public_Simplified_STEP_v1.0.step",
    ],
    "SG-6010D": ["SG-6010D_Original_Full_Assembly_20261118.step"],
    "SG-8021": ["SG-8021_Driver_Version_Original_Full_Assembly_20261118.step"],
    "CPM-78-39": ["CPM-78-39_Original_Full_Assembly_20261118.step"],
    "CPM-80-25": [
        "CPM-80-25_Public_Simplified_STEP_v1.0_No_Driver.step",
        "CPM-80-25_Public_Simplified_STEP_v1.0_Integrated_Driver.step",
        "CPM-80-25_Original_Full_Assembly_No_Driver_20261118.step",
        "CPM-80-25_Original_Full_Assembly_Integrated_Driver_20261118.step",
    ],
    "CPM-100-25": [
        "CPM-100-25_Original_Full_Assembly_No_Driver_20261118.step",
        "CPM-100-25D_Dual_Encoder_Driver_Original_Full_Assembly_20261118.step",
    ],
}

ORIGINAL_STEPS = {
    "SG-6010C": ("SG-6010C_Original_Full_Assembly_20261118.step", 22348448, "c7feb40848ac3c7469a1fb35567a1ee0fdf65cba752e3f164ea52d9f0491ae2b"),
    "SG-6010D": ("SG-6010D_Original_Full_Assembly_20261118.step", 11653945, "29013caf3e470c43f6a60a875786ed46140604288654b4483b37710dcb1d7dda"),
    "SG-8021": ("SG-8021_Driver_Version_Original_Full_Assembly_20261118.step", 19380522, "9591a7f2143d1a0418e39a876cc9d047c21289c3e80cc9c265aad40a1156f95d"),
    "CPM-78-39": ("CPM-78-39_Original_Full_Assembly_20261118.step", 16521809, "4a7791ede4c5b4c1430f75cc86325900bcb6bb65490c6deaf9c41d8149389d3b"),
}


ADDITIONAL_ORIGINAL_STEPS = {
    "CPM-80-25": [
        ("CPM-80-25_Original_Full_Assembly_No_Driver_20261118.step", 8640280,
         "866e22160181ec1296835da335f92288a00e4b60e6226c12347b364ccd58e783"),
        ("CPM-80-25_Original_Full_Assembly_Integrated_Driver_20261118.step", 12829472,
         "f990ba3abcc04a2206392d12b3fe5e1957592cbab732ef6acb012212007eaf98"),
    ],
    "CPM-100-25": [
        ("CPM-100-25_Original_Full_Assembly_No_Driver_20261118.step", 5173732,
         "53deeda1053018086e42d9e10daa26b070c711b47750ba90732fc9d23377be05"),
        ("CPM-100-25D_Dual_Encoder_Driver_Original_Full_Assembly_20261118.step", 19462788,
         "b6055fa2944efd82ff999b2270bcd41cfe2d07816cbdd7b8eeff200e3fa63d34"),
    ],
}


def main() -> None:
    media_errors = []
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
                try:
                    with Image.open(file) as img:
                        img.verify()
                except Exception as error:
                    media_errors.append(f"{model}: {file.name}: {type(error).__name__}: {error}")
            else:
                raise ValueError("Unexpected image format "+str(file))

        step_names = re.findall(r'(?i)[\w-]+\.step', text)
        expected=STEP_ALLOWED.get(model,[])
        for name in expected:
            if name not in text:
                raise ValueError("Missing approved public STEP link: "+model+" "+name)
        if model in ORIGINAL_STEPS:
            filename, expected_bytes, expected_sha = ORIGINAL_STEPS[model]
            original = DOCS / "assets/downloads/joint-actuators" / filename
            if not original.is_file() or original.stat().st_size != expected_bytes:
                raise ValueError("Original full assembly STEP missing/incorrect size: " + model)
            digest = hashlib.sha256(original.read_bytes()).hexdigest()
            if digest != expected_sha:
                raise ValueError("Original full assembly STEP failed SHA-256: " + model)
            if model == "SG-8021" and "Driver Version" not in text:
                raise ValueError("SG-8021 driver-equipped CAD variant must be labeled")
        for filename, expected_bytes, expected_sha in ADDITIONAL_ORIGINAL_STEPS.get(model, []):
            path = DOCS / "assets/downloads/joint-actuators" / filename
            if not path.is_file() or path.stat().st_size != expected_bytes:
                raise ValueError("Missing original CPM variant STEP or wrong size: " + filename)
            if hashlib.sha256(path.read_bytes()).hexdigest() != expected_sha:
                raise ValueError("Original CPM variant STEP failed SHA256: " + filename)
            if filename not in text:
                raise ValueError("Original CPM variant STEP not linked: " + filename)
        if model == "CPM-100-25" and "Dual Encoder" not in text:
            raise ValueError("CPM-100-25 dual-encoder driver variant label is missing")
        if model == "CPM-80-25" and "No Driver" not in text:
            raise ValueError("CPM-80-25 driverless variant label is missing")
        if not expected and step_names:
            raise ValueError("Unreleased joint CAD advertised on "+model)
        if not expected and "No downloadable STEP is currently approved" not in text:
            raise ValueError("CAD release status is missing on "+model)
        if len(text)>4800:
            raise ValueError("Joint product page too long for quick-download UX: "+model)
        print("PASS",model,"PDF",pdf.stat().st_size,"images",len(paths),"STEP",len(expected))
    if media_errors:
        raise ValueError("Invalid product image assets:\n" + "\n".join(media_errors))
    print("PASS six joint PDF and image integrity checks, including eight verified original full-assembly STEP variants")

if __name__ == "__main__":
    main()
