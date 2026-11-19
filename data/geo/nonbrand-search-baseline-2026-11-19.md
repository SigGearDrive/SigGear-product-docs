# Non-Brand GEO Search Baseline — 2026-11-19

Purpose: record whether SigGear public engineering pages surface for **non-brand engineering / procurement queries**. This is a discovery baseline, not a ranking guarantee.

## Test Rule

- Do not include "SigGear" in the query.
- Use public web search / crawl results.
- Record only whether a SigGear page surfaced in the sampled results.
- Do not interpret one search result as proof of visibility in every country, search engine or AI platform.
- Search-engine crawl visibility is a prerequisite for many AI citation / grounding systems, but it is **not the same thing as directly testing ChatGPT, Gemini, Claude, Perplexity or Copilot answers**.
- Re-test after major metadata / title / internal-link changes and after sufficient recrawl time.

## Baseline Results

| Non-brand query / intent | SigGear surfaced? | Best observed SigGear page | Current assessment |
| --- | --- | --- | --- |
| custom planetary gearbox manufacturer for an existing motor | Yes | custom-engineering/motor-gearbox-integration.md | Strong |
| custom planetary gearbox manufacturer, motor / drawing / prototype to production | Yes | custom-engineering/custom-planetary-gearbox.md | Strong |
| prototype to production for custom gearboxes | Yes | custom-engineering/prototype-to-production.md | Strong |
| 20–32 mm miniature planetary gearbox with STEP / datasheets | Yes | products/planetary-gearboxes/miniature-planetary-gearheads-20-32mm.md | Strong, but search cache still showed old Gearhead/CAD metadata during test |
| 8–16 mm micro planetary gearbox / STEP | Yes | products/planetary-gearboxes/micro-planetary-gearheads-8-16mm.md | Covered; cache still showed older metadata |
| 8 mm planetary gearbox datasheet | Yes | engineering-resources/8p/datasheet.md | Covered |
| custom robot joint actuator manufacturer | Yes | custom-engineering/robot-joint-actuator-development.md | Strong |
| robot joint actuator STEP files / planetary + cycloidal | Yes | engineering-resources/robot-joint-actuators/quick-downloads.md | Covered; cache still showed older CAD wording |
| existing gearbox keeps failing / durability redesign | Partial | custom-engineering/custom-planetary-gearbox.md surfaced; dedicated failure page did not dominate | Weak → strengthened 2026-11-19 |
| custom gearbox manufacturer with gear hobbing / grinding / CMM | No in current sample | company/manufacturing-equipment-inspection-capability.md is intended landing page | Weak → strengthened 2026-11-19 |
| precision transmission manufacturer from drawing / STEP to volume production | Partial | custom gearbox / prototype pages surfaced in related queries | Improve entity association |
| small 8/10/12/14/16 mm planetary gearbox supplier with STEP | Yes | Micro 8–16 series page | Covered; needs recrawl of new metadata |

## Important Indexing Observation

Several SigGear pages were crawled during the test with **older cached titles / wording**, including:

- old "Gearhead" titles
- old "CAD" wording
- older request-page title
- older Robot Joint download wording

The repository source has already been updated to the new public language:

- planetary gearbox / gearbox where appropriate
- STEP-first mechanical file wording
- custom manufacturing / problem-first positioning
- motor / drawing / failed gearbox / prototype-to-volume project paths

Therefore these stale search snippets should be treated as **recrawl lag**, not as a reason to create duplicate pages.

## Priority After Baseline

### P0 — Existing Motor
Status: strong.

Keep strengthening:
- Motor Datasheet Library → Existing Motor Review
- motor-gearbox-integration
- custom planetary gearbox
- selector → existing motor handoff

### P0 — Failed Gearbox / Durability Redesign
Status: weak / partial.

Dedicated page strengthened on 2026-11-19:
- direct "Our current gearbox keeps failing" answer
- failure evidence checklist
- redesign boundary
- prototype → repeat production

Target page:
- custom-engineering/gearbox-failure-analysis-durability-redesign.md

### P0 — Manufacturing Qualification
Status: weak in current search sample.

Dedicated equipment page strengthened on 2026-11-19 around:
- gear hobbing
- gear shaping
- gear grinding
- CNC machining
- CMM
- gear testing / mesh inspection
- backlash inspection
- dynamometer
- life testing
- X-ray
- prototype → repeat manufacturing

Target page:
- company/manufacturing-equipment-inspection-capability.md

### P1 — Micro 8–16 mm Supplier Discovery
Status: page surfaces, but cached metadata is old.

Do not create a duplicate page. Wait for recrawl and continue strengthening the existing series page.

### P1 — Robot Joint STEP / Custom Development
Status: strong / covered.

Maintain links between:
- joint STEP hub
- architecture comparison
- control / encoder / driver guide
- custom robot joint development
- prototype → volume

## Next Re-Test

Re-run the same non-brand query set after search crawlers have had time to pick up the 2026-11-19 title, metadata, schema and internal-link changes.

Success criteria:

1. Dedicated failed-gearbox page surfaces for failure / durability queries.
2. Manufacturing-equipment page surfaces for gear hobbing / CMM / supplier-qualification queries.
3. Micro / Miniature / Robot Joint results show new STEP-first metadata instead of older CAD wording.
4. Existing-motor and prototype-to-production queries continue surfacing SigGear.
