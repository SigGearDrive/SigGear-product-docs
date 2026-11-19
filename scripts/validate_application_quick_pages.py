#!/usr/bin/env python3
"""Verify concise supplier-first OEM application pages and first-screen downloads."""
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
APP=ROOT/"docs/applications"
PAGES=sorted(p for p in APP.glob("*.md") if p.name not in {"index.md","planetary-gearbox-application-families.md"})
MODELS=["8P","10P","12P","14P","16P","20P","22P","24P","28P","32P","36P","42P"]
assert len(PAGES)==32, f"Expected 32 distinct application pages, found {len(PAGES)}"
DETAILED_APPLICATION_PAGES={"robot-gripper-gear-motors.md"}

for page in PAGES:
    s=page.read_text(encoding="utf-8")
    assert s.startswith("---\n") and "\n---\n" in s[4:], page
    assert len(re.findall(r"^# ",s,re.M))==1, page

    if page.name in DETAILED_APPLICATION_PAGES:
        # High-value engineering answer pages may be longer than the concise
        # supplier-first template, but must still expose real model files,
        # selector context and an engineering inquiry path.
        assert len(s)<9000, f"{page.name}: detailed page too long at {len(s)} chars"
        for m in ("8P","10P","12P","14P","16P"):
            assert f"../products/planetary-gearboxes/{m.lower()}-planetary-gearbox.md" in s, (page.name,m)
            assert f"{m}_Full_Assembly.step" in s
            assert f"{m}_2D_Drawing.pdf" in s
            assert f"{m}_Planetary_Gearhead_Datasheet_Rev" in s
        assert "../selection-guides/planetary-gearhead-quick-selector.md?app=dexterous_hand_gripper#preliminary-ratio-stage-finder" in s, page
        assert "../request-cad-sample-quote.md?app=dexterous_hand_gripper" in s, page
        assert "rated allowable" in s.lower() and "not claims" in s.lower(), page
        continue

    assert len(s)<3700, f"{page.name}: too long at {len(s)} chars"
    assert "SigGear is an OEM supplier" in s, page
    for link in ("../engineering-resources/motors/index.md",
                 "../engineering-resources/planetary-gearboxes/public-cad-release-v1.md",
                 "../custom-engineering/motor-gearbox-integration.md",
                 "../request-cad-sample-quote.md"):
        assert link in s, f"{page.name}: missing supplier/download path {link}"
    assert "Rated torque and length depend on the selected stage/ratio" in s, page
    found=[m for m in MODELS if f"../products/planetary-gearboxes/{m.lower()}-planetary-gearbox.md" in s]
    assert 3<=len(found)<=4, f"{page.name}: {len(found)} model choices"
    for m in found:
        assert f"{m}_Full_Assembly.step" in s and f"{m}_2D_Drawing.pdf" in s
        assert f"{m}_Planetary_Gearhead_Datasheet_Rev" in s
index=(APP/"index.md").read_text(encoding="utf-8")
assert len(index)<6500, "Application index too long"
for page in PAGES:
    assert page.name in index, f"Application index does not link {page.name}"
for name, token in (
 ("electric-pruning-shears-planetary-gearbox.md","electric_pruning_shears"),
 ("electric-curtain-blind-window-opener-gear-motors.md","electric_curtain_blind"),
 ("smart-toilet-bidet-planetary-gear-motors.md","smart_toilet_bidet"),
 ("robot-gripper-gear-motors.md","dexterous_hand_gripper")):
    s=(APP/name).read_text(encoding="utf-8")
    assert "?app="+token+"#preliminary-ratio-stage-finder" in s, name
for page,required in {
 "electric-pruning-shears-planetary-gearbox.md":["32P","36P","42P"],
 "electric-curtain-blind-window-opener-gear-motors.md":["16P","20P","22P"],
 "robot-gripper-gear-motors.md":["8P","10P","12P","14P","16P"]
}.items():
    s=(APP/page).read_text(encoding="utf-8")
    for m in required:
        assert f"{m.lower()}-planetary-gearbox.md" in s, (page,m)
# Guard against generic, near-identical intent text on the six focused home-device pages.
focused_intent = {
    "electric-curtain-blind-window-opener-gear-motors.md": ("curtain rail", "roller blind", "pulley radius"),
    "smart-toilet-bidet-planetary-gear-motors.md": ("toilet lid", "bidet nozzle", "moisture barrier"),
    "smart-pet-feeder-litter-box-planetary-gearheads.md": ("feeder auger", "litter-box drum", "pellets bridge"),
    "access-control-smart-lock-security-gear-motors.md": ("door lock", "bolt or cam", "emergency-egress"),
    "consumer-appliance-home-device-gear-motors.md": ("appliance lids", "rotary valves", "cleaning"),
    "smart-hardware-gear-motors.md": ("cabinet latch", "IoT rotary", "standby current"),
}
for name, terms in focused_intent.items():
    body = (APP / name).read_text(encoding="utf-8").lower()
    for term in terms:
        assert term.lower() in body, (name, term)
    assert "## " in body and ("pdf / step" in body.lower() or "pdf / 2d / step" in body.lower()), name

# Check that engineering search intent stays specific rather than generic.
round3_intent = {
    "powered-screwdriver-planetary-gearbox.md": ("screw run-down", "momentary rating", "bit-holder"),
    "hvac-smart-vent-damper-gear-motors.md": ("seal contact", "breakaway torque", "fire/smoke"),
    "industrial-automation-servo-planetary-gearboxes.md": ("indexing fixture", "reversal backlash", "control loop"),
    "packaging-labeling-conveyor-gear-motors.md": ("label-feeder roller", "line pull", "bearing support"),
    "precision-instruments-optical-mechanisms.md": ("filter wheel", "optical stage", "lost motion"),
    "optical-imaging-camera-module-gear-motors.md": ("focus barrel", "vibration", "direct drive"),
    "medical-device-micro-gear-motors.md": ("non-patient-contact", "traceability", "risk controls"),
    "laboratory-automation-diagnostic-equipment-gear-motors.md": ("reagent carousel", "sample-handling carriage", "splash boundary"),
}
for name, terms in round3_intent.items():
    body = (APP / name).read_text(encoding="utf-8").lower()
    assert all(word.lower() in body for word in terms), (name, terms)
    assert "pdf" in body and ("2d & step" in body or "pdf / 2d / step" in body), name

# A visitor should see the exact model PDF/2D/STEP grid BEFORE prose and
# before any generic resource hubs.  On mobile the links become three-button cards.
firstscreen_file_pages = ["semiconductor-electronics-inspection-equipment-gear-motors.md","office-automation-business-equipment-gear-motors.md","pump-valve-fluid-control-gear-motors.md","agriculture-outdoor-equipment-gear-motors.md","automotive-vehicle-small-motion-gear-motors.md","energy-battery-charging-equipment-actuators.md","food-beverage-coffee-equipment-gear-motors.md","vending-dispensing-kiosk-gear-motors.md"]
for name in firstscreen_file_pages:
    source = (APP / name).read_text(encoding="utf-8")
    before_files = source.split("## Direct Downloads", 1)[0]
    assert len(before_files) < 450, (name, "Downloads not near page top")
    assert source.index("## Direct Downloads") < source.index("**Application:**"), name
    assert source.index("_Full_Assembly.step") < source.index("**Application:**"), name
    assert source.count("[**↓ PDF**]") == 3, name
    assert source.count("[**↓ 2D**]") == 3, name
    assert source.count("[**↓ STEP**]") == 3, name
    assert len(source) < 2150, (name, len(source))
    assert '<div class="siggear-app-quick" markdown="1">' in source, name
    rendered = ROOT / "site/applications" / name.removesuffix(".md") / "index.html"
    assert rendered.is_file(), (name, "Rendered page missing")
    html = rendered.read_text(encoding="utf-8")
    assert 'class="siggear-app-quick"' in html, (name, "Download block not rendered")
    start = html.index('class="siggear-app-quick"')
    end = html.index("</div>", start)
    grid = html[start:end]
    assert "<table>" in grid and "</table>" in grid, (name, "Direct model download matrix lost")
    assert grid.count("_Full_Assembly.step") == 3, (name, "Full STEP links missing from matrix")
    assert grid.count("_2D_Drawing.pdf") == 3, (name, "2D links missing from matrix")
    assert grid.count("_Planetary_Gearhead_Datasheet_Rev") == 3, (name, "PDF links missing from matrix")
    assert "application-quick-downloads.css?v=20261119-firstscreen" in html, name

# Additional high-value micro gearhead application pages use the proven file-first
# layout, while retaining every original model/PDF/2D/STEP URL.
round5_files = {"electric-curtain-blind-window-opener-gear-motors.md":3,"smart-toilet-bidet-planetary-gear-motors.md":4,"smart-pet-feeder-litter-box-planetary-gearheads.md":4,"access-control-smart-lock-security-gear-motors.md":3,"consumer-appliance-home-device-gear-motors.md":3,"smart-hardware-gear-motors.md":3,"powered-screwdriver-planetary-gearbox.md":3,"micro-robotics-gear-motors.md":3,"furniture-seating-adjustable-mechanism-gear-motors.md":3}
for name, count in round5_files.items():
    src = (APP / name).read_text(encoding="utf-8")
    assert src.count("## Direct Downloads") == 1, name
    assert src.index("## Direct Downloads") < src.index("**Application:**"), name
    assert src.index("_Full_Assembly.step") < src.index("**Application:**"), name
    assert len(src.split("## Direct Downloads", 1)[0]) < 620, (name, "model downloads buried")
    assert len(src) < (2850 if count == 4 else 2500), (name, len(src))
    for label in ("PDF", "2D", "STEP"):
        assert src.count("[**↓ " + label + "**]") == count, (name, label)
    rendered = ROOT / "site/applications" / name.removesuffix(".md") / "index.html"
    assert rendered.is_file(), (name, "missing rendered HTML")
    html = rendered.read_text(encoding="utf-8")
    assert 'class="siggear-app-quick"' in html, name
    start = html.index('class="siggear-app-quick"')
    end = html.index("</div>", start)
    grid = html[start:end]
    assert "<table>" in grid and "</table>" in grid, name
    assert grid.count("_Full_Assembly.step") == count, (name, "STEP")
    assert grid.count("_2D_Drawing.pdf") == count, (name, "2D")
    assert grid.count("_Planetary_Gearhead_Datasheet_Rev") == count, (name, "PDF")
    assert "application-quick-downloads.css?v=20261119-firstscreen" in html, name

print("PASS 31 concise application pages plus 1 detailed dexterous-hand engineering page with real files and selector context")
