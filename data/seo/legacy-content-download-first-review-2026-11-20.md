# SigGear Legacy SEO Content — File-First Review (2026-11-20)

## Goal and evidence limits

**Owner request:** Evaluate **existing** GitHub Pages URLs using genuine Google exposure/click evidence, protect newly published GEO pages while they are recrawled, and replace long / weak legacy content **in place** with concise, directly downloadable SigGear Datasheet PDFs, 2D Drawings and Full STEP models.

**Available evidence:**
- Source: historical **Google Search Console Search Analytics via Windsor.ai**, saved in `data/seo/underperforming-content-audit-2026-11-19.yml` and `data/seo/planetary-gsc-ctr-baseline-2026-11-15.yml`.
- Baselines: 2026-10-18 → 11-15 and 2026-10-20 → 11-16. **These two windows overlap heavily and are both before the November 18–19 content rewrites.** Changes between their totals cannot establish a sustained decline or a response to the recent releases.
- Current Windsor.ai GA4 readout: November 1–19 had **15 dated sessions, 57 page views and 1 active user**, with country report limited to **China**; includes confirmed internal testing. Do **not** use these sessions as an independent ranking of overseas page quality.
- **Live Search Console account is not selected in Windsor.ai** on November 20. No new post-release GSC measurements were invented. A missing page row does not mean verified zero impressions or indexing failure.

## Historical URL-level GSC signals

| Existing public URL path | GSC 2026-10-20 to 11-16 impressions | Clicks | Decision |
| --- | ---: | ---: | --- |
| `/applications/humanoid-robot-joint-actuators/` | 737 | 0 | **Observe** after November 19 joint PDF / 2D / exact STEP download-first rewrite; do not undo |
| `/products/planetary-gearboxes/8-42mm-planetary-gear-reducer/` | 114 | 0 | **Observe** after November 18–19 12-model PDF/2D/STEP-first revisions |
| `/products/planetary-gearboxes/10p-planetary-gearbox/` | 27 | 0 | **Observe** after direct 10P PDF / 2D / full STEP and stage-specific data already moved to first screen |
| `/applications/planetary-gearbox-application-families/` | 6 | 0 | **Rewrite in place for concrete asset usability**, but do **not** claim SEO failure from six impressions |
| `/engineering-resources/planetary-gearboxes/public-cad-release-v1/` | **141** | **15** | **Protect** working 12-model download landing page and all binary files |
| `/applications/electric-pruning-shears-planetary-gearbox/` | 27 | 1 | **Protect** observed click; direct-files first-screen is already live |

**No sustained decline is established** for any page in these snapshots. The priority is documented download usability and a fair post-recrawl comparison, not deleting indexed URLs.

## First batch executed on existing URLs only

### 1) Existing-motor integration / OEM gearhead path

**Path:** `docs/custom-engineering/motor-gearbox-integration.md`  
**URL:** `/custom-engineering/motor-gearbox-integration/`

- Replaced **380-line** legacy prose with **99 lines** of download-first, customer-question-oriented engineering content.
- Added **12 model rows × 3** exact original downloadable assets: SigGear published **Datasheet PDF**, **2D Drawing PDF** and **Full Assembly STEP** for 8P through 42P, derived from the protected download center, not invented.
- Kept the original H1 topic, same existing URL and key mechanical, ratio, duty and manufacturing claims with project-specific limits; preserved real motor/gearbox photo, 32P/42P integration-guide links, manufacturing evidence and confidential-project guidance.
- Added direct motor-PDF library and prefilled engineering request links. Does **not** claim that every customer motor is compatible with the 12 frames.
- **Reason for edit:** objectively long 380-line copy and no direct model file table at the start. Public search has retrieved this older URL for non-brand motor matching, so retain its path. **Do not describe it as proven low-ranking in GSC** without page data.

### 2) Mechanism-to-gearhead application-family guide

**Path:** `docs/applications/planetary-gearbox-application-families.md`  
**URL:** `/applications/planetary-gearbox-application-families/`

- Rebuilt the existing six-row mechanism guide around **6 model choices × 3 real direct files = 18 download links**, without making any product adoption/fit claims.
- Each row now links to its specific **Datasheet PDF**, original **2D Drawing PDF**, **Full Assembly STEP** and engineering check. These filenames are sourced from the currently published 12-model download center.
- Retains the same URL and application-to-gearhead purpose; the selector, Motor Datasheet library and 12-model download center are prominent.
- **Evidence boundary:** 6 impressions / 0 clicks is too small to show decline. The actionable issue was relying on a generic download-hub button instead of individual product file access.

## Protected and awaiting verification

- All **13 new GEO public pages** and the additional product page from November 19 remain unchanged. Allow Google/AI systems to discover them before making outcome claims.
- All **32 application pages** have already been given model-specific PDF / 2D / STEP first-screen layouts in the latest November 19 deployment. No duplication of that work in this batch.
- **Protected working file center** `/engineering-resources/planetary-gearboxes/public-cad-release-v1/` retains all 12 models, original PDF, 2D, full and simplified STEP links; do not rename it despite legacy `cad` path.
- All existing page URLs and canonical paths remain stable. **Do not delete and republish a new URL** just to refresh content, which could discard existing links and indexing history.
- No CAD binary, Datasheet PDF, model parameter, drawing approval, production claim or related sitemap route was changed.

## Next evidence gate — require comparable Google data

1. Restore access to **Search Console Search Analytics** without sacrificing the currently working GA4 account if Windsor.ai's free plan limits connectors. A GSC **Pages** export with clicks, impressions, CTR and average position for **two non-overlapping complete 28-day windows** is sufficient for the next decision. Also include **Queries** for the affected URLs and **Country** where available.
2. Identify pages with repeated meaningful non-brand impressions but no clicks, falling impressions **and** comparable position/coverage, or genuinely unusable first-screen files. Distinguish **no row** from zero.
3. Use current **URL Inspection** if a critical page lacks a row after recrawl; one public search sample or a live sitemap is not proof of Google indexing.
4. For eligible pages, **rewrite the body on the same URL** with first-screen exact downloads and a brief engineering check; preserve useful existing product facts and relevant links.
5. Leave pages already changed November 18–19 in observation until a fresh post-release window exists. Do not re-edit titles repeatedly or invent ratio/torque/grade/lifetime numbers.
6. Keep **confirmed real inquiries** separate from internal GA4 test events. Watch first-party model PDF/STEP clicks, then project-fit email/engineering conversations.

## Release acceptance

- [ ] MkDocs source and compiled HTML validate
- [ ] All 12 motor-integration PDF, 2D and Full STEP links match protected center and exist
- [ ] All 6 mechanism-to-model PDF, 2D and Full STEP links match protected center and exist
- [ ] All original URL slugs and self-canonical behavior retained
- [ ] Official 12-model download center and recently updated 32 applications untouched
- [ ] New post-release GSC performance explicitly pending (not presented as measured)

**This review replaces copy, not historical identity or engineering proof.**

## Second batch on 2026-11-20 — existing engineering guides only

### A) Robot Joint Actuator and Gearbox Selection Guide

- **Existing canonical path:** `/selection-guides/robot-joint-actuator-selection-guide/`; do **not** change the URL.
- Source file was **371 lines** with ten generic navigation actions before any direct released files. It is now **149 lines**; the original short SEO topic is retained.
- A historic October GSC audit recorded approximately **254 impressions** for the robot-joint selector. That is a **historical visibility signal**, **not a verified current decline**, and the available record does not establish that URL's clicks or current ranking.
- First substantive block is **six public planetary/cycloidal joint reference modules** with **18 distinct released model-specific files**: six reference PDF Datasheets, four existing engineering-reference 2D PDFs and eight exact full assembly STEP variants. Rows were sourced from the already published `docs/engineering-resources/robot-joint-actuators/quick-downloads.md` file; missing 2D files remain Request/pending, not fabricated.
- Preserves key engineering value: gravity / inertia / external-force torque equations, continuous vs peak duty, installation envelope, external loads, thermal behavior, encoder/driver/protocol limits, brake and safety, prototype validation. Drops duplicated broad lead-in and long generic checklists, and provides a concise first-contact requirement list.
- **Variant guards:** SG-8021 driver-equipped STEP, CPM-80-25 two thickness/driver variants, CPM-100-25D 48 mm 2D vs standard 29.5 mm STEP, CPM-78-39 drawing match pending. Public Rev0.1 sheets and available 2Ds are engineering references, not approved production drawings.

### B) Planetary Gearbox Engineering Resources index

- **Existing canonical path:** `/engineering-resources/planetary-gearboxes/` — keep unchanged.
- Former directory offered **12 outline 2D PDFs** and linked to the separate download center for PDF Datasheets and STEP files. It now shows **12 models × 3 exact downloadable files = 36 direct links** in its first model table, plus online specifications and mechanical interface pages.
- Asset filenames come from the **protected existing 12-model central download page** and remain unchanged. This separate index is for engineers browsing the resources tree; the already-performing original download center retains its canonical role.
- Source page content is concise and includes boundaries around stage-specific length and motor/ratio compatibility. No claims of a universal input-speed limit or automatic motor compatibility.

### Automated QA added

- `scripts/validate_joint_quick_downloads.py`: checks the new first selection-guide table has exactly six models, four columns, all actual joint PDF / available 2D / correct STEP variants and non-approval warnings.
- `scripts/validate_planetary_download_assets.py`: checks the legacy planetary resource index exposes all 12 × Datasheet PDF / original 2D / Full Assembly STEP and that their built hrefs resolve to generated real public files.
- The two edited URLs are maintained; **no binary PDF/STEP assets are modified**, no new application/product page is created, and the 2026-11-19 new GEO pages stay in observation.

**Reassessment gate:** await fresh **non-overlapping**, page-level GSC exposure/click/CTR/rank data and post-recrawl observations before labelling any legacy URL as *continually declining*. The current Windsor.ai connection still contains GA4 but no selected GSC property; no post-rewrite uplift or traffic loss is claimed here.
