#!/usr/bin/env python3
"""Validate the 8P-42P public CAD stage boundary."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODELS = ["8P","10P","12P","14P","16P","20P","22P","24P","28P","32P","36P","42P"]

PUBLIC_CAD_PAGE = ROOT / "docs" / "engineering-resources" / "planetary-gearboxes" / "public-cad-release-v1.md"
CANDIDATE_PACK = ROOT / "docs" / "engineering-resources" / "planetary-gearboxes" / "candidate-design-in-pack.md"


def main() -> None:
    public_cad_text = PUBLIC_CAD_PAGE.read_text(encoding="utf-8")
    candidate_pack_text = CANDIDATE_PACK.read_text(encoding="utf-8")

    if "4-stage reference only" not in public_cad_text:
        raise ValueError("Public CAD page must state that released files are 4-stage references only.")

    if "1-, 2- or 3-stage" not in candidate_pack_text:
        raise ValueError("Candidate Design-In Pack must explain the 1/2/3-stage boundary.")

    for model in MODELS:
        slug = model.lower()
        expected = ROOT / "docs" / "assets" / "downloads" / slug / f"{model}_Public_Simplified_STEP_v1.0_4-Stage.step"
        if not expected.exists():
            raise FileNotFoundError(f"Missing expected 4-stage public STEP: {expected}")

        model_dir = expected.parent
        forbidden = []
        for stage in (1, 2, 3):
            forbidden.extend(model_dir.glob(f"*{stage}-Stage.step"))
            forbidden.extend(model_dir.glob(f"*{stage}-Stage.stp"))
        if forbidden:
            raise ValueError(
                f"{model}: found stage-specific public STEP file(s) that violate the current public CAD boundary: "
                + ", ".join(str(path.name) for path in forbidden)
            )

    print("Public planetary CAD boundary validated: all 12 released STEP files are 4-stage references only.")


if __name__ == "__main__":
    main()
