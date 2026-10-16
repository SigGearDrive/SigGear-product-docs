#!/usr/bin/env python3
"""Keep the 22P public page evidence factual and configuration-aware.

The earlier 22P page referenced the same 4 KB "Micro Planetary Gearbox"
graphic as five different technical figures (overview, performance,
shaft limits, motor compatibility and dimension drawing). Product series
22P is Miniature, and a promotional graphic is not a controlled drawing.
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
    assert "title: 22 mm Miniature Planetary Gearbox (22P)" in src
    assert "# 22 mm Miniature Planetary Gearbox (22P)" in src
    assert "22p-real-product-evidence.webp" in src, "Authentic sample photos must remain"
    assert "22P Mechanical Interface](../../engineering-resources/22p/mechanical-interface.md)" in src
    assert "1,000–20,000 rpm" in src
    assert "max_diameter=22#preliminary-ratio-stage-finder" in src
    assert "Product=27-05769189-121064&PartNumber=22p" in src

    for name in OLD_MEDIA:
        assert name not in src, f"Misleading reused 22P graphic is still referenced: {name}"
    assert not re.search(r"22\s*mm\s+Micro\s+Planetary", src, re.IGNORECASE)

    # The existing text table must still provide real stage/rating information
    # after unverified diagram references are removed.
    for expected in ("## Stage, Ratio and Performance Table", "22.6 mm", "38.5 mm",
                     "8.0 kgf·cm", "25.0 kgf·cm"):
        assert expected in src, f"Published 22P specification lost: {expected}"
    print("PASS 22P real product photos, Miniature classification and controlled technical references")


if __name__ == "__main__":
    main()
