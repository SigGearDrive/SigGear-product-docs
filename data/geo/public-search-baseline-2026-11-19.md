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

## Priority 0 custom-manufacturing sample — later 2026-11-19 check

### Existing motor + custom gearhead

Sample intent:
- `I already have a motor custom planetary gearhead manufacturer`

Observed:
- SigGear's custom planetary engineering / existing-motor pages were returned in the sampled public search results.

Assessment: **retrievable now; strengthen refreshed title and custom-manufacturer entity message**

### Customer drawing / OEM custom transmission

Sample intent:
- `custom gearbox manufacturer customer drawing CAD prototype production`

Observed:
- SigGear custom planetary / prototype-to-production content was returned in the sampled public search results.

Assessment: **retrievable now; new problem-first page should become the preferred citation after indexing**

### Prototype → production

Sample intent:
- `precision transmission manufacturer prototype to volume production gearbox`

Observed:
- SigGear's Prototype-to-Production page was returned directly.

Assessment: **strong retrieval signal; continue shifting public wording from catalog-product framing toward repeatable manufacturing**

### Custom robot joint development

Sample intent:
- `custom robot joint actuator manufacturer CAD prototype production`

Observed:
- SigGear's Custom Robot Joint Actuator Development page was returned directly.

Assessment: **strong retrieval signal; maintain configuration-specific electronics / interface language**

### Failing gearbox / replacement

Sample intent:
- `gearbox keeps failing replacement custom planetary manufacturer`

Observed:
- SigGear custom planetary content can be retrieved, but the new dedicated replacement / failure page has not yet become the preferred sampled result.

Assessment: **continue internal linking + wait for indexing + retest**

### Interpretation

The important change is that SigGear is already retrievable for several **non-brand custom engineering intents**, not only for searches containing the SigGear name or exact model numbers.

The next objective is to make the search / AI result describe SigGear correctly as:

**custom precision transmission manufacturer → prototype development → repeatable volume manufacturing**

rather than only as a catalog planetary gearbox supplier.

## Failure / durability and OEM volume round — 2026-11-19

### Query cluster: existing motor + custom gearhead

Observed:
- SigGear's existing-motor / motor + gearhead engineering content is retrievable in non-brand public search.
- The public result currently favors the older Motor + Gearbox Integration page rather than the newer custom-manufacturer landing page.

Action:
- retain the existing page because it already has retrieval history
- strengthen crosslinks to the newer custom-manufacturer and prototype-to-volume pages
- do not change the existing URL

### Query cluster: prototype → volume production

Observed:
- SigGear's Prototype-to-Production page is retrievable directly for non-brand prototype / production intent.
- The indexed title / snippet may lag the newest page title and wording.

Action:
- preserve URL
- continue strengthening OEM manufacturing and production-planning semantics
- allow search systems time to refresh the indexed snippet

### Query cluster: customer drawing / CAD / physical sample

Observed:
- Current non-brand search results are highly competitive.
- Competing pages frequently place “built to your drawing,” “send drawing or physical sample,” and prototype-to-production language in the first screen.

Action completed:
- added dedicated `custom-gearbox-from-drawing-cad.md`
- linked from homepage, custom engineering hub, problem-first page and inquiry intake
- kept all claims configuration-specific; no invented delivery or production numbers

### Query cluster: gearbox failure / durability redesign

Observed:
- SigGear did not yet own a dedicated public result for failure symptoms such as gear wear, bearing damage, overheating or backlash growth.

Action completed:
- added `gearbox-failure-analysis-durability-redesign.md`
- added failure-evidence field to the engineering inquiry
- connected replacement / existing-motor / prototype-to-volume paths
- new page must be allowed to index before the same query set is retested

### Query cluster: OEM volume manufacturing / delivery planning

Observed:
- Current search competition often uses explicit prototype-to-production and production-delivery language.
- Some competitors publish fixed capacity / lead-time / MOQ numbers.

SigGear policy:
- do not copy or invent fixed capacity, MOQ or lead-time claims
- publish only real manufacturing evidence and project-specific scheduling language

Action completed:
- added `oem-volume-manufacturing-delivery.md`
- published internal factory-evidence capture plan for future real batch / QC / packing evidence
- connected manufacturing evidence, prototype-to-production and inquiry planning fields

## Nine independent P0 non-brand retrieval queries — 2026-11-19

A fresh **query-by-query** public-search sample found at least one SigGear result for **6 of 9** exact non-brand P0 questions; only **1 of 9** surfaced the **designated P0 primary page**. This is a limited retrieval observation, **not** a ChatGPT/Gemini/Claude/Perplexity/Copilot citation rate or a verified Google index count.

Most important distinctions:
- The existing-motor page `motor-gearbox-integration.md` is appearing for motor and replacement-adjacent questions; keep its established URL.
- `prototype-to-production.md` is directly retrieved for broad prototype-to-volume intent, but the exact OEM planning question P0 #15 maps to the separate `oem-volume-manufacturing-delivery.md` page.
- The new Drawing / STEP / Sample, Replacement / Redesign, Failure / Durability and Supplier Qualification pages were **not** the preferred observed pages for their corresponding exact P0 questions in this sample.
- Recrawl and Search Console URL Inspection should come before any further title or content rewriting.

**Full fixed queries, returned URLs and decisions:** [P0 Public Retrieval Observation — 2026-11-19](p0-public-retrieval-observation-2026-11-19.md).  
**Separate five-AI-platform trial protocol:** [AI Platform Citation Capture Protocol](ai-platform-citation-capture-protocol-2026-11-19.md).
