# TraceParts Smart-Publishing Mapping

This directory contains the mapping layer from SigGear's controlled product data to TraceParts Smart-Publishing fields.

## Current status

Ready from SigGear:
- 12 controlled planetary family references: 8P through 42P
- one released public simplified 4-stage STEP per family
- product page URL per family
- public datasheet URL per family
- public mechanical-interface URL per family
- approved public technical values from `data/products/*.yml`

Still required from TraceParts / the Smart-Publishing account:
- official XLS template
- valid `Classification_Category_ID`

Ready from SigGear:
- official SigGear logo on a white background: `docs/assets/brand/siggear-logo-white.webp`

## Important ordering boundary

`8P`, `10P`, ... `42P` are used as existing SigGear series references.

They are not presented as fully specified final orderable configurations. Final stage count, ratio, shaft/interface and motor matching remain configuration-dependent.

## Public CAD boundary

The attached STEP file for each series is the released **simplified 4-stage reference** for preliminary mechanical packaging and Design-In.

Do not describe it as:
- a detailed internal planetary transmission model;
- a universal model for 1-, 2-, 3- and 4-stage configurations;
- final production CAD.

## Export

After TraceParts provides the classification category ID:

```bash
python scripts/export_traceparts_catalog.py \
  --classification-category-id <TRACEPARTS_CATEGORY_ID>
```

This creates `exports/external-catalogs/traceparts-products-en.csv`, which is a field-aligned import/mapping source for the official TraceParts Excel template.

## Live international English handoff

The SigGear operator successfully generated/downloaded all 12 series STEP AP203 CAD files from the international English TraceParts site (2026-10-14). For the next publication improvement, see:

- [English product-title correction and tracked GitHub URL handoff](traceparts-english-publishing-handoff-2026-10-14.md)
- [12-model CAD validation register](traceparts-live-validation-2026-10-14.yml)

All 12 model-specific `traceparts.com/en/product/...` URLs were provided directly by the SigGear operator on 2026-10-14 and recorded in [the English model URL registry](traceparts-model-urls-2026-10-14.yml). Existing `Product` identifiers and `PartNumber` values are preserved without inventing slugs. The operator confirmed all 12 STEP AP203 downloads; independent CAD geometry validation and TraceParts Publisher title alignment remain separate tasks.

## 2026-10-14 TraceParts Publisher / sales conversion follow-up

The GitHub → TraceParts direct product link path is deployed for all 12 models, but TraceParts → GitHub website links, published product-title segmentation, and native lead/RFQ visibility still need platform-specific confirmation.

- [Ready-to-send Publisher update request with all 12 existing TraceParts Product IDs, English titles, and model-specific UTM URLs](traceparts-publisher-update-request-2026-10-14.md)
- [GA4 referral baseline and pending TraceParts native Analytics QA](traceparts-attribution-baseline-2026-10-14.yml)

Do not report UTM tracking, RFQ, or catalog download leads as verified until the actual TraceParts Publisher / Analytics backend is checked. Merely having the correct tracked URLs in the GitHub mapping exporter does not prove that they are published on TraceParts.

## DirectIndustry manufacturer onboarding (2026-10-14)

SigGear's DirectIndustry launch materials are now prepared but **not submitted or published** on the external platform:

- [DirectIndustry official exhibitor enquiry, manufacturer profile, category strategy, requested terms and launch checklist](directindustry-onboarding-2026-10-14.md)
- [First batch of four product listing drafts (10P, 20P, 32P, 42P), grounded in published SigGear master data](directindustry-first-batch-2026-10-14.md)

Official DirectIndustry form: https://www.directindustry.com/exhibit_on_directindustry/subscription

Do not create public DirectIndustry product URLs before the platform issues actual ones. The eventual site publication and subscription require SigGear's authorized account owner, real contact phone and written commercial terms.
