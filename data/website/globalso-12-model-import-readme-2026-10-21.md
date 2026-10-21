# Globalso model staging (12/12) — 2026-10-21

**NOT AN OFFICIAL GLOBALSO IMPORT TEMPLATE; DO NOT IMPORT DIRECTLY WITHOUT FIELD MAPPING.**

This UTF-8 CSV is a staging file for product content and engineering QA, with all 12 verified current 8P–42P gearhead families. Every row is **draft only**, with values extracted from the official SigGear GitHub source of truth. No Globalso CMS records have been changed, created, backed up, or published.

Verified field coverage in this export: `model`, `diameter_mm`, `ratio_range`, `rated_allowable_torque_range_kgf_cm`, `step_4stage_url`, `traceparts_url`, `datasheet_url`, `mechanical_interface_url`, `photo_reference_url`. All 12 have published 1–4 stage source ranges. Published **1,000–20,000 rpm** is for **gearhead input speed**, not a motor/complete gearmotor rating. All torque ranges are **kgf·cm**, not Nm, and are stage-dependent; peak momentary torque is **not continuous**.

### Field mapping gate

Before using a Globalso CSV import:

1. Access the *actual* SigGear Globalso CMS and export the existing 76-product product, category, media, SEO and URL data. Validate permissions and a rollback route.
2. Download an actual Globalso CSV template from the live account. Map `proposed_product_name`, category, images, descriptions, SEO, and custom tech fields to the official column names. Do not assume columns in this file are accepted or recognized by CMS.
3. Do not overwrite existing **Motor + Gearhead Assembly** listings or their slugs with these gearhead-only catalogue drafts.
4. Create draft-only category and 8P/22P/42P preview pages in the CMS; check SEO canonical, images, mobile specs and working links. Require engineering signoff before expanding to other models.
5. Do not upload source URLs with query/hash modifications as canonical URLs; selector/inquiry links with query parameters are CTA only.
6. Only publish after user explicitly approves the preview. Don't invent SKUs or exact stage/ratio availability outside published tables.

### Draft grouping

* Micro 8–16 mm: 8P, 10P, 12P, 14P, 16P
* Miniature 20–32 mm: 20P, 22P, 24P, 28P, 32P
* Compact 36–42 mm: 36P, 42P

**Source**: [SigGear repository](https://github.com/SigGearDrive/SigGear-product-docs/tree/main/docs/products/planetary-gearboxes). **Draft PR**: [#217](https://github.com/SigGearDrive/SigGear-product-docs/pull/217).
