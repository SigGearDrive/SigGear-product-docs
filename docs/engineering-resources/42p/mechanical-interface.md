---
title: 42P Planetary Gearbox Mechanical Interface | Controlled 2D / CAD Reference | SigGear
description: Public 42P mechanical-interface reference based on the current controlled 2D drawing, with full assembly CAD available after configuration review.
---

# 42P Planetary Gearbox Mechanical Interface v1.1

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-08  
**Controlled drawing code:** SG01PD42

This page summarizes the mechanical-interface information that is suitable for public early evaluation from the current SigGear controlled 2D drawing.

!!! warning
    This page is not a manufacturing drawing. Use the current controlled drawing for final tolerances, detailed shaft geometry and production design release.

## Controlled Envelope

| Item | Controlled / published reference |
| --- | --- |
| Nominal gearbox body diameter | Ø42.0 mm (0 / -0.1 mm shown on drawing) |
| Gearbox body length | **L ±0.3 mm**, stage-dependent |
| Output-side extension | 29.5 mm (+0.1 / -0.3 mm) |
| Output shaft diameter | Ø12.0 mm (0 / -0.02 mm) |
| Output-side locating / reference diameter | Ø28.0 mm (0 / -0.03 mm) |
| Output keyway | DIN 6885-A4×4×20 |
| Keyway length | 20.0 mm |
| Output-side mounting | 4 × M4 threaded holes, depth 6 mm |
| Output-side reference diameter | Ø35.0 ±0.1 mm |
| Input-side center opening | Ø16.0 mm (+0.05 / 0 mm) |
| Input-side mounting | 2 × Ø3.1 mm holes |
| Opposed input mounting-hole spacing | 25.0 ±0.1 mm |

## Stage-Dependent Length

The controlled drawing uses **L** for the gearbox body length with **±0.3 mm** shown on the drawing. L changes with the selected stage count.

| Stages | Gearbox body length L |
| ---: | ---: |
| 1 | 35.6 mm |
| 2 | 46.9 mm |
| 3 | 58.2 mm |
| 4 | 69.5 mm |

Use the selected stage / ratio and the controlled drawing revision before final production release.

[View 42P Product Data](../../products/planetary-gearboxes/42p-planetary-gearbox.md){ .md-button }

## Published Mechanical Limits

| Item | Public value |
| --- | ---: |
| Radial load, 10 mm from flange | ≤ 16.0 kgf |
| Shaft axial load | ≤ 8.0 kgf |
| Radial shaft play | ≤ 0.04 mm |
| Thrust shaft play | ≤ 0.3 mm |
| Continuous permissible input speed | ≤ 8,000 rpm |
| Operating temperature range | −40 to 120 °C |

These limits come from the current 42P specification sheet and should be checked against the actual application load direction, duty cycle and selected configuration.

## CAD Status

A full 42P assembly STEP has been reviewed internally.

The supplied STEP is a detailed multi-component assembly and is **not released as a public raw download**, because it contains internal planetary transmission geometry.

For packaging or design-in, request the configuration-matched CAD. A simplified public external-interface STEP may be released separately after review.

[Request 42P CAD / Controlled Drawing](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

[Open 42P Motor Integration Guide](motor-integration.md){ .md-button }

## Design-In Boundary

Before final design freeze, confirm:

- Stage count and reduction ratio
- Exact gearbox body length L
- Output shaft / mounting interface
- Motor-side pilot and shaft interface
- Motor speed and torque operating point
- Radial / axial load condition where relevant
- Configuration-specific CAD revision

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
