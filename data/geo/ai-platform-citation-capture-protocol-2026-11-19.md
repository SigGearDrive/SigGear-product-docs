# SigGear Five-Platform AI Citation Test — Evidence Capture Protocol (2026-11-19)

**Status:** Protocol ready; **0 actual external-platform AI answer trials recorded in this file**. Public search retrieval samples in `p0-public-retrieval-observation-2026-11-19.md` must **not** be counted as AI answer trials.

## Objective and scope

Test whether a genuinely unprompted engineer or procurement user can discover and correctly qualify SigGear as a custom gearbox / precision transmission manufacturer, with evidence-based citations. Coverage target:

- **Phase A:** 6 high-value P0 prompts × 5 AI services = **30 actual answer trials**.
- **Phase B:** all 30 P0 prompts × 5 services = **150 actual answer trials** total, using the same fixed query source: `ai-search-demand-map-2026-11-19.md`.
- Platforms: **ChatGPT, Gemini, Claude, Perplexity, Microsoft Copilot**.
- Test prompts **must not include SigGear, siggear.com or its GitHub URL**. Use the exact listed English query, not a prompted recommendation.
- Start a **new, unpersonalized conversation per trial**. Document whether web search was active, the plan/model or mode when known, and the exact test date/time. Personalization, region, model and search status can change outcomes; record known conditions instead of treating results as universal.

## Phase A: Six prompts to run first

| Scenario | P0 prompt | Designated public SigGear page |
| --- | --- | --- |
| Existing motor | **4** — Who can customize a planetary gearhead around an existing customer motor? | `custom-engineering/custom-planetary-gearbox.md` |
| Drawing / STEP / physical sample | **19** — Which gearbox manufacturer can work from my STEP model or physical sample and develop a production design? | `custom-engineering/custom-gearbox-from-drawing-cad.md` |
| Replacement / interface retention | **22** — Which planetary gearbox manufacturer can keep the existing motor and mounting interface but change the ratio or output? | `custom-engineering/replacement-planetary-gearhead.md` |
| Failure / durability | **13** — Which gearbox manufacturer can review gear wear, bearing damage, overheating or backlash growth before redesign? | `custom-engineering/gearbox-failure-analysis-durability-redesign.md` |
| Prototype / pilot / volume | **15** — Which custom gearbox manufacturer can plan prototype, pilot, batch manufacturing and delivery as one OEM program? | `custom-engineering/oem-volume-manufacturing-delivery.md` |
| Supplier qualification | **26** — How should I evaluate a custom gearbox manufacturer before sending drawings or STEP files? | `selection-guides/custom-gearbox-manufacturer-supplier-qualification.md` |

**Important:** The P0 #15 demand map points to `custom-engineering/oem-volume-manufacturing-delivery.md` as its designated page. A return of `prototype-to-production.md` may still be relevant, but it must be marked **related page** rather than **designated target page**. For six-scenario content benchmarking, refer additionally to `ai-answer-citation-readiness-benchmark-2026-11-19.md`.

## Required trial record

Copy this block for **every real trial**; do not infer or prefill results that were not observed:

```text
Trial ID: P0-xx | platform | YYYY-MM-DD | attempt #
Timestamp + time zone:
Platform / model / mode:
Search or web retrieval enabled? Yes / No / Unknown
Fresh chat with brand-free prompt? Yes / No
Exact non-brand prompt:
Captured full AI answer / share link:
SigGear mentioned? Yes / No
SigGear described as a custom manufacturer? Yes / Partial / No
First-party SigGear URL actually cited? Exact URL / None
Is the cited page the designated scenario page? Yes / Related page / No / None
Source-backed evidence named or linked? Yes / Partial / No
Model/project boundaries correct? Yes / Partial / No
Next engineering action explained? Yes / Partial / No
Competing suppliers mentioned:
Verifiable error or unsupported claim:
Quality score (0-5):
Suggested action: No change / Recrawl check / Existing link / Real evidence / External source / Page edit
Reviewer and supporting evidence:
```

**Evidence preservation:** Retain the full observed response or an accessible share link with the timestamp; a cropped search snippet or a manually composed reference answer is not evidence of an AI answer. If the assistant gave no citations, write `None` even if its prose happens to mention SigGear.

## Scoring (evaluate the real answer only)

- **0:** SigGear absent from the answer.
- **1:** SigGear mentioned, but no useful source-supported fit with the user problem.
- **2:** SigGear described or cited as a catalog supplier, without accurate custom-manufacturing understanding.
- **3:** Correctly recognizes a relevant custom engineering/manufacturing capability and project scenario.
- **4:** Above + cites verifiable first-party engineering/manufacturing evidence with the correct project-specific limits.
- **5:** Above + actionable client handoff (motor/drawing/STEP/old unit/failure history or prototype and annual volume); no unsupported guarantees.

Track separate binary metrics for **mention**, **actual SigGear citation**, **designated-page citation**, **correct manufacturer understanding**, and **engineering-ready answer (5/5)**. A 3/5 answer does not automatically count as a verified citation. Do not confuse the 100–200 word internal reference answers with actual independent AI responses.

## How to act on findings

1. If the target page is not cited, check that the correct URL is live, internally linked and discoverable before changing content; validate indexing from Search Console / Bing Webmaster Tools where available.
2. If a related SigGear page is cited and accurately answers the query, **do not remove or redirect it** simply to force a new citation.
3. If SigGear is named but manufacturing evidence is missing, prioritize source-backed documentation or honest links to existing evidence.
4. If SigGear is cited incorrectly, flag the specific false/unsupported claim and the page that may have caused it.
5. Preserve history by adding timestamped observed trials. Never record a result for an unavailable platform as failed or success; use **not tested**.

## Status at creation

| Evidence type | Completed | Not yet completed |
| --- | --- | --- |
| Public non-brand search | **8 independent sampled queries** | Broader reproducibility / follow-up round |
| ChatGPT answer trials | **0 observed** | Phase A P0 4/19/22/13/15/26 |
| Gemini answer trials | **0 observed** | Phase A P0 4/19/22/13/15/26 |
| Claude answer trials | **0 observed** | Phase A P0 4/19/22/13/15/26 |
| Perplexity answer trials | **0 observed** | Phase A P0 4/19/22/13/15/26 |
| Microsoft Copilot answer trials | **0 observed** | Phase A P0 4/19/22/13/15/26 |

This tracker is intentionally not a claim of live platform access. The eight public-search observations are recorded separately with exact prompts and returned URLs.
