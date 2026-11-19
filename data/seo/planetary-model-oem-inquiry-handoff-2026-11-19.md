# Product model to custom engineering conversion — November 19, 2026

Scope: all 12 existing planetary gearhead product pages (8P, 10P, 12P, 14P, 16P, 20P, 22P, 24P, 28P, 32P, 36P, 42P).

## Verified gap
Each model already has the four first-screen PDF/2D/original STEP/simplified STEP buttons and a concise specification table, but had no model-specific direct inquiry link. A lower-page Motor + Gearhead Integration link was present, requiring another page visit and manual model selection.

## Changes
Insert one short OEM engineering handoff directly after the existing model specification row, **without moving the four direct download buttons**:
- Existing motor: `model=<current P>&start=existing_motor&path=gearbox_only`
- Drawing or CAD: `model=<current P>&start=drawing_cad`
- Prototype to volume: `model=<current P>&start=prototype_to_volume`

The current inquiry JavaScript explicitly supports `model` and `start` query parameters and the three enumerated starting points; the model is preselected if valid. These are engineering review invitations, not guaranteed stock/certification or a claim of a specific custom ratio.

## Release safeguards
- Every original PDF, 2D, Full Assembly STEP and simplified STEP link remains identical.
- No change to product specifications, materials, drawings, URLs, original source revisions or SEO title/description.
- No more general prose added: just one short, model-specific conversion line.
- Extended the existing 12-model application link validator to test **all 36 source and rendered URL parameters**, including each model's start condition.
- Do not infer Google clicks or inquiry conversion improvements from publication alone.
