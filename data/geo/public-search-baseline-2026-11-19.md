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
