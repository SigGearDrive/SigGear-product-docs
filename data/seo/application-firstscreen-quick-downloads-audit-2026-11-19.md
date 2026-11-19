# SigGear application quick-download revision — 2026-11-19

**Goal:** put genuine model-specific Datasheet PDF, 2D Drawing PDF and Full Assembly STEP links in the first visible content block, avoiding generic hub-only buttons above them.

**Scope:** eight existing application URLs: semiconductor/electronics inspection, office paper-feed devices, micro pumps/valves, seed/irrigation equipment, vehicle interior flaps, EV charge-port service hardware, coffee dosing/grinders, and vending/kiosk dispensing.

**Evidence:** All eight source pages previously placed three generic download hub buttons and two prose paragraphs *before* the 3-row model file table. Each now places its three-model × three-file matrix immediately under the page heading, followed by one-line Application and Check descriptions. The model file URLs were compared exactly against the prior sources. The CSS renders PDF/2D/STEP as prominent links and mobile cards, without hidden JavaScript or sign-in.

**Data boundary:** These pages have no reportable page-level GSC rows in the available 2026-10-20 to 2026-11-16 pre-rewrite query. This does not prove they are unindexed or that their new SEO titles are performing. Google may need time to recrawl.

**Guardrails:** No change to any PDF or STEP byte, no new product rating, no product installation claim, no URL deletion or migration, no inferred certification, no new application pages.

**Regression:** `scripts/validate_application_quick_pages.py` now checks source order, character budget, exact first-screen PDF/2D/STEP link counts, rendered MkDocs HTML table and stylesheet presence.
