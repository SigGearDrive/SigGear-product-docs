---
title: CPM-80-25 Mechanical Interface | No-Driver and Integrated-Driver CAD | SigGear
description: Approved public CPM-80-25 mechanical interface dimensions and CAD resources for robot joint design-in.
---

# CPM-80-25 Mechanical Interface v1.0

**Status:** Approved for Public  
**Release date:** 2026-09-28

This page provides the dimensions normally required for early packaging, mounting and mechanical design-in.

!!! warning
    This is an engineering-evaluation reference, not a manufacturing drawing. Confirm the controlled drawing for the exact ordered configuration before final tooling or production release.

## Configuration Envelope

| Configuration | Max. OD | Axial thickness | Weight |
| --- | ---: | ---: | ---: |
| No integrated driver | 80 mm | 29.7 mm | 430 g |
| Current integrated-driver reference | 80 mm | 41.2 mm | 512 g |

## Output-Side Interface

- 9 x M3, depth 6 mm, equally distributed on PCD 75 mm
- 12 x M3, depth 5 mm, on PCD 25 mm
- 2.5 mm reference / locating hole, +0.02 / 0 tolerance, depth 3 mm
- Maximum outer diameter: 80 mm

## Rear / Motor-Side Interface - No Driver

- 6 x M3, depth 6 mm, on PCD 74 mm
- 4 x M2, depth 1.5 mm, on PCD 40 mm
- 2 x M2, depth 2.5 mm, on PCD 10.4 mm
- Reference diameters shown on the controlled outline include 57 h7 and 33 h7 features

## Integrated-Driver Reference

The current integrated-driver reference retains the output-side interface while using a driver housing that increases the total axial thickness to 41.2 mm and the assembly weight to 512 g.

Driver housing, connector orientation, encoder arrangement and cable routing should be confirmed for the ordered driver version.

## Public CAD

[Download Simplified STEP - No Driver](../../assets/downloads/cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_No_Driver.step){ .md-button .md-button--primary }

[Download Simplified STEP - Integrated Driver](../../assets/downloads/cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_Integrated_Driver.step){ .md-button }

The simplified files retain external envelope and design-in interfaces while omitting internal cycloidal transmission geometry, bearings, motor internals, PCB details and proprietary assembly construction.

## Final Design Release

Before final release, confirm:

- Exact driver / no-driver configuration
- Controlled mounting interface and tolerances
- Connector and cable orientation
- External radial and axial load direction
- Duty cycle and thermal condition
- Encoder and communication configuration

[Request Controlled Drawing / Engineering Support](../../request-cad-sample-quote.md){ .md-button }

## Related Resources

[Technical Datasheet v1.0](datasheet.md){ .md-button }
[Measured Performance Data](performance-test-data.md){ .md-button }
