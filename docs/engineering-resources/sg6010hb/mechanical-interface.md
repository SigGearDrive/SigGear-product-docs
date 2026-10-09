---
title: SG-6010HB Mechanical Interface | SG2908B Controlled Drawing Reference | SigGear
description: Public SG-6010HB mechanical-interface reference based on the current SG2908B controlled drawing, including 67 mm envelope, 25.57 mm nominal overall thickness, mounting patterns and wiring references.
---

# SG-6010HB Mechanical Interface v1.0

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-09  
**Controlled drawing code:** **SG2908B**

This page summarizes the SG-6010HB mechanical-interface information that is suitable for public early design evaluation from the current controlled drawing.

!!! warning
    This page is **not** a manufacturing drawing. Use the current configuration-controlled SG2908B drawing and CAD supplied by SigGear for final tolerances, datum control, interface release and production design.

## Envelope

| Item | Controlled drawing reference |
| --- | --- |
| Maximum outside diameter | Ø67.00 mm, drawing tolerance −0.08 / −0.10 mm |
| Main body axial thickness | 22.57 ±0.50 mm |
| Output-side axial extension shown on drawing | 3.00 ±0.30 mm |
| Nominal overall product thickness | 25.57 mm |
| Catalog product weight | 298.5 g |

The **25.57 mm** catalog thickness is consistent with the controlled drawing when the 22.57 mm main body thickness and the nominal 3.00 mm output-side extension are considered together.

## Output-Side / Mechanical Interface

The current SG2908B drawing defines multiple output-side / housing interface features, including:

| Feature | Drawing reference |
| --- | --- |
| Mounting pattern | 6 × M4 equally spaced |
| M4 effective thread depth | 5.0 mm |
| Secondary bolt circle | 6 × M3 on Ø47.0 mm P.C.D. |
| Precision holes | 3 × Ø4.00 ±0.02 mm, equally spaced |
| Reference diameter | Ø24 ±0.07 mm |
| Section reference diameters | Ø52.00 mm, Ø40.00 +0.05/0 mm, Ø37.00 mm, Ø12.00 mm |

These features must be read together with the controlled drawing before manufacturing. Do not reconstruct production geometry from this summary alone.

## Opposite-Side Mounting Pattern

| Feature | Drawing reference |
| --- | --- |
| Mounting holes | 4 × M2 through holes, equally spaced |
| Pitch circle diameter | Ø40 ±0.1 mm P.C.D. |

## Shaft / Center Features

The controlled section view includes the following center-feature references:

- Ø6.0 mm
- Ø21.00 mm
- Ø35.00 mm

Their exact functional definition, datum relationship and tolerances must be taken from the controlled drawing rather than inferred from this public summary.

## Wiring Reference

The controlled drawing also specifies:

- Motor three-phase wire length: **120 mm**
- Motor phase wire: **AWG18**
- Stripped / tinned end length: **3 mm**
- Two thermistor wires: **120 mm**
- Thermistor wire diameter: approximately **Ø0.5 mm**
- Stripped / tinned end length: **3 mm**

Cable termination and connector configuration can vary by project and must be confirmed for the ordered version.

## CAD Status

A detailed SG2908B / SG-6010HB assembly STEP has been reviewed internally.

The supplied STEP contains detailed internal motor and planetary-transmission geometry, so the raw assembly is **not released as a public download**.

For packaging, interference checking or design-in, request the configuration-matched CAD from SigGear. A simplified public external-interface STEP may be released separately after geometry simplification and engineering review.

[Request SG-6010HB CAD / Controlled Drawing](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

## Design-In Boundary

Before final design freeze, confirm:

- Output-side mounting pattern and datum
- Opposite-side mounting pattern
- Shaft / hub interface
- Cable exit direction and connector choice
- Radial, axial and overturning load condition
- Driver and encoder configuration
- Brake / power-off behavior
- Controlled drawing revision
- Configuration-matched CAD revision

## Related Resources

[SG-6010HB Product Page](../../products/robot-joint-actuators/sg6010hb.md){ .md-button }
[SG-6010HB Technical Datasheet](datasheet.md){ .md-button }
[Exoskeleton Joint Selection Guide](../../applications/exoskeleton-joint-actuators.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
