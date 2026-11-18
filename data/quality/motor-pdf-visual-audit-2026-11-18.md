# SigGear motor Datasheet PDF visual-quality review

**Audit date:** 2026-11-18  
**Public source:** `docs/assets/downloads/motors/` (33 published motor-only PDFs; no binaries changed)  
**Method:** PyMuPDF rendered actual source pages, inspected text spans and image placement; representative full-page images were visually reviewed. Embedded-image effective DPI is estimated from pixels divided by displayed physical size. Only raster images placed at least 1 × 1 inch were included in the low-DPI check. This is a **legibility screen, not engineering certification**.

## Result

| Scope | Observed |
| --- | --- |
| Published files | 33 motor-only PDFs across Ø8, 10, 12, 14, 16, 20, 22, 24, 28 and 32 mm |
| Total pages rendered / examined | 79 |
| Pages containing large embedded rasters below 150 effective DPI | **30** |
| Notable affected groups | Ø10 (12 occurrences), Ø16 (8), Ø28 Sheet B (1), Ø32 (9) |
| Unaffected by structural integrity | All 33 files passed the separate PDF parse, nonempty-download and link checks |
| Engineering ratings | Not requalified, reinterpreted or changed |

**Important:** A low effective DPI is not the same as the entire PDF being unreadable. Many datasheets have clear vector-text specification tables, while their *source-image* curves and original mechanical drawing panels remain low resolution. Conversely, an image above 150 DPI is not proof its engineering dimensions are readable or verified.

## Visual review — actual rendered pages

| Priority | Published diameter / pages | Finding and action |
| --- | --- | --- |
| P0 | **Ø10 mm**, 4 PDFs, pages 3–4 | Source performance-chart panels around **63–67 DPI**, with another large source raster around 128–129 DPI on page 2. Vector-typeset model tables are clearer than the source curves. Obtain the original high-resolution chart or validated numeric test points for an approved vector redraw; **do not infer values from pixel interpolation** |
| P0 | **Ø16 mm**, 8 Draft V0.9 PDFs, first pages | Original large drawings/figures around **63–89 DPI**. Some labels/dimension annotations are not suitable for controlled production use at normal page size. Request source CAD / higher-resolution original drawings and review draft source anomalies, including duplicated 120132 family records |
| P0 | **Ø32 mm**, 3 PDFs, pages 3–5 | Original drawings and curves around **72–73 DPI**. Full-page manual rendering confirms blurred small dimensions, source annotations and curve numbers. Request original Mechanical A / Mechanical B drawings; keep distinct mounting variants separate |
| P1 | **Ø28 mm Sheet B**, page 2 | Representative chart about **115 DPI**; the re-typeset thermal / bearing tables are readable. The source +155 °C ambient note and unassigned curve require engineering review, independent of raster quality |
| Review | **Ø8 mm D1, Ø22 mm** | Representative source pages rendered and generally legible at larger zoom. Ø22 Sheet 02/03 differ in mechanical interface and speed despite sharing codes; legibility does not resolve that conflict |
| Review | **Ø12, Ø14, Ø20, Ø24 mm** | No large-raster-under-150-DPI occurrence detected. Still require model-specific engineer review before any final drawing or motor+gearhead performance claim |

## Remediation boundaries

1. Do **not** artificially upscale old bitmaps to imply more precise dimensions, measured performance, or published test accuracy. Do not replace manufacturer source curves using guessed points.
2. Obtain true high-resolution supplier images, controlled 2D dimension drawings or original vector CAD, and controlled motor performance curves or raw test results.
3. Have the engineering team approve each model, winding, output shaft/mounting, curves, units, and version before publishing revised PDFs. Preserve historical controlled revisions.
4. Keep the direct-link navigation and all 33 original public PDFs accessible until approved replacements exist; visibly identify Draft / source-quality limitations.
5. Repeat the render-and-compare workflow after replacement and check that the new first-page charts/dimensions genuinely improve at target on-screen scale.

## Analytics caution

Google Search Console impressions and clicks cannot assess the visual fidelity of PDF drawings. On-site GA4 click instrumentation measures **intent to open a PDF**, not proof that a CAD file was downloaded successfully or that a sales lead was generated. Google Search Console re-crawl results after 2026-11-18 changes are not yet available as a meaningful before/after sample.

**Reproducibility:** `python -m pip install 'PyMuPDF>=1.25,<1.28'`, then `python scripts/inspect_motor_pdf_visual.py` after reconstructing motor PDF upload parts. For authorized public-source image inspection only, `--emit-preview` writes base64 JPEG previews to CI logs; do not enable this in every routine build.
