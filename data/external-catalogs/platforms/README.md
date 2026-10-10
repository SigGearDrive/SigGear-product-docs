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

Still required from SigGear before final submission:
- official SigGear logo on a white background, minimum height 40 px

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
