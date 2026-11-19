#!/usr/bin/env python3
"""Keep the 22P public page evidence factual and configuration-aware.

The 22P page now prioritizes product data and direct CAD release status. The test guards against reused promotional graphics and verifies the new SI torque values, real product evidence, and non-selector download layout.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs/products/planetary-gearboxes/22p-planetary-gearbox.md"
OLD_MEDIA = [
    "22p-planetary-gearbox-main.webp",
    "22p-planetary-gearbox-structure-and-ratios.webp",
    "22p-planetary-gearbox-mechanical-details.webp",
    "22p-planetary-gearbox-motor-compatibility.webp",
    "22p-planetary-gearbox-dimensions.webp",
]


def main() -> None:
    src = PAGE.read_text(encoding="utf-8")
    assert "title: 22 mm Miniature Precision Planetary Gearhead (22P)" in src
    assert "# 22 mm Miniature Precision Planetary Gearhead (22P)" in src
    assert "planetary gearbox" in src.lower(), "Keep gearbox as a technical synonym for searches and legacy links"
    assert "22p-real-product-evidence.webp" in src, "Authentic sample photos must remain"
    assert "22P Mechanical Interface](../../engineering-resources/22p/mechanical-interface.md)" in src
    assert "1,000–20,000 rpm" in src
    assert "max_diameter=22#preliminary-ratio-stage-finder" not in src, "The product page should no longer surface the selector"
    # New quick-download layout replaces the old downloads table.
    # Validate the actual model-matched file targets, not legacy link labels.
    for expected in (
        "[**Download Datasheet PDF**](../../assets/downloads/22p/22P_Planetary_Gearhead_Datasheet_Rev1.0.pdf)",
        "[**Download 2D Drawing PDF**](../../assets/downloads/22p/22P_2D_Drawing.pdf)",
        "[**Download Full Assembly STEP**](../../assets/downloads/22p/22P_Full_Assembly.step)",
        "[**Download Simplified 4-Stage STEP · Reference**](../../assets/downloads/22p/22P_Public_Simplified_STEP_v1.0_4-Stage.step)",
    ):
        assert expected in src, f"22P engineering download missing or mislinked: {expected}"

    for name in OLD_MEDIA:
        assert name not in src, f"Misleading reused 22P graphic is still referenced: {name}"
    assert not re.search(r"22\s*mm\s+Micro\s+Planetary", src, re.IGNORECASE)

    # The existing text table must still provide real stage/rating information
    # after unverified diagram references are removed.
    for expected in ("## Stage, Ratio and Performance Table", "22.6 mm", "38.5 mm",
                     "784.5 mN·m", "2451.7 mN·m"):
        assert expected in src, f"Published 22P specification lost: {expected}"
    print("PASS 22P real product photos, Miniature classification and controlled technical references")


if __name__ == "__main__":
    main()
