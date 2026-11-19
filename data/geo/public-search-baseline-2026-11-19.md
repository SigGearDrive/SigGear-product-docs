# SigGear Public Search Retrieval Baseline — 2026-11-19

Purpose: record a small external public-search sample that supports GEO operations. This is not a ranking claim and does not represent every result in ChatGPT, Gemini, Claude, Perplexity or Copilot.

## Sampled non-brand intents

### 1. 20–32 mm miniature planetary gearhead + CAD / supplier intent

Sample query:
- `20 mm miniature planetary gearhead STEP CAD supplier`

Observed:
- SigGear's **20–32 mm Miniature Planetary Gearheads** page was returned in the sampled public search results.
- The result exposes 20P / 22P / 24P / 28P / 32P and direct PDF / 2D / STEP resources.

Current assessment: **visible / strengthen citation quality**

Primary page:
- `docs/products/planetary-gearboxes/miniature-planetary-gearheads-20-32mm.md`

### 2. Robot joint actuator + STEP / CAD / datasheet supplier intent

Sample query:
- `robot joint actuator supplier STEP CAD datasheet`

Observed:
- SigGear's **Robot Joint Actuator Datasheets & CAD** resource page was returned in the sampled public search results.
- The result exposes planetary and cycloidal model specifications and public engineering files.

Current assessment: **visible / strengthen supplier-entity association**

Primary pages:
- `docs/engineering-resources/robot-joint-actuators/quick-downloads.md`
- `docs/selection-guides/robot-joint-supplier-evaluation.md`

### 3. Replacement planetary gearhead / existing motor intent

Sample query:
- `replacement planetary gearhead existing motor manufacturer`

Observed:
- No SigGear replacement-specific page appeared in the sampled result set.

Current assessment: **content gap / new page created**

Primary page added:
- `docs/custom-engineering/replacement-planetary-gearhead.md`

Next action:
- strengthen internal links from 20–32 mm, custom engineering and existing-motor pages
- allow normal crawl / indexing
- retest the same query set after the new page is publicly indexed

## Interpretation rules

- A search result appearance is evidence of retrieval, not proof that every AI assistant will cite SigGear.
- A missing result in one sample is not proof of complete invisibility.
- The main GEO KPI is qualified non-brand discovery followed by correct technical understanding, citation, referral and inquiry.
