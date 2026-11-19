#!/usr/bin/env python3
"""Verify concise supplier-first OEM application pages and first-screen downloads."""
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
APP=ROOT/"docs/applications"
PAGES=sorted(p for p in APP.glob("*.md") if p.name not in {"index.md","planetary-gearbox-application-families.md"})
MODELS=["8P","10P","12P","14P","16P","20P","22P","24P","28P","32P","36P","42P"]
assert len(PAGES)==32, f"Expected 32 distinct application pages, found {len(PAGES)}"
for page in PAGES:
    s=page.read_text(encoding="utf-8")
    assert s.startswith("---\n") and "\n---\n" in s[4:], page
    assert len(re.findall(r"^# ",s,re.M))==1, page
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
 "robot-gripper-gear-motors.md":["8P","14P","20P"]
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
    assert "## " in body and "pdf / step" in body.lower(), name

print("PASS 32 concise supplier-first application pages, 3 supply routes, file links and legacy selector context")
