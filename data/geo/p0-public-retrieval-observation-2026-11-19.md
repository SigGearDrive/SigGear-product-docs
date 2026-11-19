# P0 Non-Brand Public Retrieval Check — 2026-11-19

**Method:** Nine independent English non-brand public web-search queries, each sent separately in one session on 2026-11-19, with the search tool's 30-day recency setting. All are exact P0 queries already documented in `data/geo/ai-search-demand-map-2026-11-19.md`. The inspected set is limited to the returned sample, not all indexed documents.

**Scope boundary:** These observations are **public web-search retrieval**, NOT a ChatGPT, Gemini, Claude, Perplexity or Copilot answer/citation test. No claim is made about those services' citations, Google Search Console indexed-page status, ranks, referral traffic or conversion.

## Independent query results

| P0 | Exact non-brand query | Any SigGear result in returned sample? | Observed SigGear page | Was designated intent page surfaced? | Interpretation |
| ---: | --- | --- | --- | --- | --- |
| 3 | Which transmission manufacturers can move from prototype to repeatable volume production? | **Yes** | [Prototype to Production](https://siggeardrive.github.io/SigGear-product-docs/custom-engineering/prototype-to-production/) | **Yes** — `prototype-to-production.md` | Direct match to this broader prototype-to-volume P0 intent |
| 4 | Who can customize a planetary gearhead around an existing customer motor? | **Yes** | [Motor + Gearbox Integration](https://siggeardrive.github.io/SigGear-product-docs/custom-engineering/motor-gearbox-integration/) and other SigGear application / guide pages | **No** — designated `custom-planetary-gearbox.md` not in inspected results | Keep the older relevant entrypoint and its established link to custom engineering |
| 19 | Which gearbox manufacturer can work from my STEP model or physical sample and develop a production design? | **Yes** | [Prototype to Production](https://siggeardrive.github.io/SigGear-product-docs/custom-engineering/prototype-to-production/) | **No** — designated `custom-gearbox-from-drawing-cad.md` not in inspected results | Search understands general SigGear development flow but did not surface the focused drawing / sample page |
| 22 | Which planetary gearbox manufacturer can keep the existing motor and mounting interface but change the ratio or output? | **Yes** | [Motor + Gearbox Integration](https://siggeardrive.github.io/SigGear-product-docs/custom-engineering/motor-gearbox-integration/) | **No** — designated `replacement-planetary-gearhead.md` not in inspected results | Existing-motor association present; replacement-focused entrypoint still needs recrawl observation |
| 13 | Which gearbox manufacturer can review gear wear, bearing damage, overheating or backlash growth before redesign? | **Not in sampled results** | — | **No** — designated `gearbox-failure-analysis-durability-redesign.md` not surfaced | Prioritize independent recrawl / indexing verification; do not claim the page is unindexed |
| 15 | Which custom gearbox manufacturer can plan prototype, pilot, batch manufacturing and delivery as one OEM program? | **Yes** | [Prototype to Production](https://siggeardrive.github.io/SigGear-product-docs/custom-engineering/prototype-to-production/) | **No** — designated P0 page is `oem-volume-manufacturing-delivery.md`; the returned page is related | Relevant engineering content was surfaced, but not the designated OEM delivery landing page |
| 26 | How should I evaluate a custom gearbox manufacturer before sending drawings or STEP files? | **Yes** | [Engineering Request](https://siggeardrive.github.io/SigGear-product-docs/request-cad-sample-quote/) | **No** — designated `custom-gearbox-manufacturer-supplier-qualification.md` not surfaced | A SigGear inquiry page surfaced but not the new qualification guide; keep the guide stable for recrawl |
| 6 | Which suppliers can customize robot joint actuators for a new humanoid or robotic-arm project? | **Not in sampled results** | — | **No** — designated `robot-joint-actuator-development.md` not surfaced | Broad robotics supplier discovery is competitive; revisit after verifying exposure rather than inventing case studies |
| 27 | Which custom gearbox supplier publishes real gear hobbing, gear grinding, CMM and inspection evidence? | **Not in sampled results** | — | **No** — designated `custom-gearbox-manufacturer-supplier-qualification.md` not surfaced | Manufacturing-evidence intent has stronger competitors; do not imitate unsupported numerical or certificate claims |

**Simple tally (retrieval sample only):** at least one SigGear result for **6 of 9** queries; the corresponding designated primary page for **1 of 9**. These are neither AI citation rates nor stable search-engine rankings. No new public SigGear URL, page, title or product claim was published as part of this observation.

## Relevant competitor result examples

- P0 3: [Hewland prototype-to-volume manufacturing](https://powertrain.hewland.com/).
- P0 13: [HaoRan Transmission failure analysis](https://haorantransmission.com/resources/failure-analysis/), [KNGEAR repair / replacement](https://kngear.com/solutions/).
- P0 19: [Belon FAQ on customer drawings and physical samples](https://www.belonmachinery.com/faqs/), [Wenlio design/production workflow](https://wenlio.com/custom-gear-rd-and-design-support-wenlio/).
- P0 26: [KNGEAR procurement FAQ](https://kngear.com/corporate-faq/), [Minchen supplier RFQ checklist](https://www.minchen-tw.com/en-US/newsc65-what-information-do-you-need-for-a-custom-gear-quotation-an-rfq-checklist-for-buyers).
- P0 27: [Nilson custom gear manufacturing and inspection](https://nilsongear.com/en/custom-solutions/), [Ontario Drive & Gear manufacturing processes](https://www.odg.com/).

These are examples of returned competitors, not an exhaustive industry comparison or an endorsement of their self-reported facts.

## Decision and follow-up

1. **Do not rewrite Supplier Qualification or change established URLs.** The page and links were recently published; lack of appearance in one sampled query is not proof of indexing failure.
2. Check the four newly emphasized intent pages (Drawing / STEP / Sample, Replacement / Redesign, Failure / Durability and Supplier Qualification) in the **correct Google Search Console URL-prefix property** for live/indexing state. Use URL Inspection and compare canonical and sitemap inclusion; indexing cannot be established from these search results.
3. Allow search systems time to refresh old cached headings and snippets. Re-run the **same exact questions** after recrawl, logging a new dated sample without overwriting this baseline.
4. Start **genuine AI response tests** in clean browser conversations on ChatGPT, Gemini, Claude, Perplexity and Copilot. Record complete response text, actual cited URLs, search mode, date/time and 0–5 evidence-quality score. Begin with six high-value scenarios × five services (30 actual response trials), then cover all 30 P0 questions × five services (150 trials). Keep unrun tests explicitly **not tested**.
5. Focus improvements on **real source evidence**, stable links and engineering-page reachability before considering additional public content. Do not fabricate customer cases, search mentions or guaranteed model-specific manufacturing figures.

For the five-platform capture method, see `data/geo/ai-platform-citation-capture-protocol-2026-11-19.md`.
