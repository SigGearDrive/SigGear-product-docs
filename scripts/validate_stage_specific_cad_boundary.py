#!/usr/bin/env python3
"""Validate simplified-reference and full-assembly STEP release boundaries."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODELS = ["8P","10P","12P","14P","16P","20P","22P","24P","28P","32P","36P","42P"]
FULL_ASSEMBLY_MODELS = {
    "8P": "8PC000_ASM",
    "10P": "10000_ASM",
    "12P": "12000_ASM",
    "14P": "14000_ASM",
}

PUBLIC_CAD_PAGE = ROOT / "docs" / "engineering-resources" / "planetary-gearboxes" / "public-cad-release-v1.md"
CANDIDATE_PACK = ROOT / "docs" / "engineering-resources" / "planetary-gearboxes" / "candidate-design-in-pack.md"


def main() -> None:
    public_cad_text = PUBLIC_CAD_PAGE.read_text(encoding="utf-8")
    candidate_pack_text = CANDIDATE_PACK.read_text(encoding="utf-8")

    if "4-stage reference only" not in public_cad_text:
        raise ValueError("Public CAD page must distinguish 4-stage simplified references from full assemblies.")
    if "1-, 2- or 3-stage" not in candidate_pack_text:
        raise ValueError("Candidate Design-In Pack must explain the 1/2/3-stage boundary.")

    for model in MODELS:
        slug = model.lower()
        model_dir = ROOT / "docs" / "assets" / "downloads" / slug
        simplified = model_dir / f"{model}_Public_Simplified_STEP_v1.0_4-Stage.step"
        if not simplified.is_file():
            raise FileNotFoundError(f"Missing expected 4-stage public STEP: {simplified}")
        forbidden = []
        for stage in (1, 2, 3):
            forbidden.extend(model_dir.glob(f"*{stage}-Stage.step"))
            forbidden.extend(model_dir.glob(f"*{stage}-Stage.stp"))
        if forbidden:
            raise ValueError(f"{model}: stage-specific public STEP file(s) violate the current public CAD boundary: " + ", ".join(p.name for p in forbidden))

    for model, expected_header_name in FULL_ASSEMBLY_MODELS.items():
        full = ROOT / "docs" / "assets" / "downloads" / model.lower() / f"{model}_Full_Assembly.step"
        if not full.is_file():
            raise FileNotFoundError(f"Missing released full-assembly STEP: {full}")
        payload = full.read_bytes()
        if not payload.startswith(b"ISO-10303-21;") or not payload.rstrip().endswith(b"END-ISO-10303-21;"):
            raise ValueError(f"{model}: full-assembly STEP signature or terminator is invalid.")
        if expected_header_name.encode("ascii") not in payload[:1024]:
            raise ValueError(f"{model}: full-assembly STEP source identity mismatch.")

    print("PASS all 12 simplified STEP references remain 4-stage-only.")
    print("PASS full assembly STEP is assembled and signature-checked for 8P, 10P, 12P and 14P.")


if __name__ == "__main__":
    main()
