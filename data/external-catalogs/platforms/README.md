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
