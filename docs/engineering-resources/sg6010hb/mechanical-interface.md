---
title: SG-6010HB Mechanical Interface | Drawing and STEP Status | SigGear
description: SG-6010HB public 67 mm mounting reference, 25.57 mm catalog envelope and separate exchange STEP verification hold. Request an approved configuration-matched STEP / drawing.
---

# SG-6010HB Mechanical Interface v1.0

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-09  
**Public product model:** **SG-6010HB**  
**3D source review:** 2026-11-19 — geometry reconciliation required

This page summarizes mechanical-interface information from the supplied SG-6010HB 2D reference, pending exact drawing-revision confirmation for early design review. These values must be checked against the final ordered model and drawing revision.

!!! warning
    This page is **not** a manufacturing drawing. The supplied SG-6010HB exchange STEP is not yet matched to the published dimensional envelope. Request an engineering-approved, configuration-matched 2D drawing and CAD before final design.

## Envelope

| Item | Controlled drawing reference |
| --- | --- |
| Maximum outside diameter | Ø67.00 mm, drawing tolerance −0.08 / −0.10 mm |
| Main body axial thickness | 22.57 ±0.50 mm |
| Output-side axial extension shown on drawing | 3.00 ±0.30 mm |
| Nominal overall product thickness | 25.57 mm |
| Catalog product weight | 298.5 g |

The 22.57 mm main-body dimension plus the 3.00 mm reference extension numerically equals the **25.57 mm** catalog thickness. The exact datum-to-datum measurement still needs configuration-level confirmation; these 2D values do **not** validate the separate STEP source.

## Output-Side / Mechanical Interface

The supplied 2D reference drawing lists multiple output-side / housing interface features, including:

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

The exchange STEP submitted for **SG-6010HB** was successfully imported on 2026-11-19 as a millimetre-based AP203 assembly with 46 solid bodies.

Its **all-solid bounding envelope** is approximately **72.53 mm × 34.86 mm × 72.53 mm**, compared with the current catalogue's **Ø67 mm × 25.57 mm** nominal product envelope. The all-solid bounding box may include protruding or non-housing parts, so it is **not** by itself a controlled housing dimension. Nevertheless, this difference prevents automatic approval as a configuration-matched SG-6010HB installation model.

**Release decision:** The raw internal assembly STEP is **not a public download**. The source identity, solid ownership, body envelope and permitted simplified geometry require engineering sign-off before any public external-interface STEP is offered.

For packaging, interference checking or design-in, request the configuration-matched CAD from SigGear. A simplified public external-interface STEP may be released separately after geometry simplification and engineering review.

[Request SG-6010HB CAD / Controlled Drawing](mailto:luffy@siggear.com?subject=SigGear%20Engineering%20Inquiry){ .md-button .md-button--primary }

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

**Luffy Wang**  
International Sales / Sales Engineer, SigGear  
[luffy@siggear.com](mailto:luffy@siggear.com)
