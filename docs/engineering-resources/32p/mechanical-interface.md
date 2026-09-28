---
title: 32P Mechanical Interface | 4-Stage Planetary Gearbox CAD | SigGear
description: Approved public mechanical interface for the SigGear 32P 32 mm planetary gearbox, including 4-stage CAD, output shaft and motor-side mounting references.
---

# 32P Mechanical Interface v1.0

**Status:** Approved for Public  
**Configuration represented by current CAD:** 4-stage reference  
**Release date:** 2026-09-28

This page contains the interface information normally required for packaging, mounting and early design-in.

!!! warning
    The current public STEP represents the 4-stage reference only. It must not be treated as a universal 1-4 stage model. Request controlled CAD for the selected stage before final tooling or production release.

## Stage-Dependent Body Length

| Stages | Gearbox body length L |
| ---: | ---: |
| 1 | 28.05 mm |
| 2 | 36.35 mm |
| 3 | 44.65 mm |
| 4 | 52.95 mm |

## 4-Stage External Envelope

| Item | Public value |
| --- | ---: |
| Nominal gearbox outer diameter | 32 mm |
| Gearbox body length | 52.95 mm |
| Output shaft extension | 21.6 mm (+0.1 / -0.3 mm) |
| Nominal overall length including output shaft | 74.55 mm |

The 74.55 mm overall value is derived from the published 52.95 mm body length plus the 21.6 mm output shaft extension.

## Output-Side Interface

- 4 x M3 threaded holes, depth 4.5 mm
- Mounting-hole center radius: 9.8 mm
- Output-side reference diameter: 26.0 +/- 0.1 mm
- Nominal output shaft diameter: 8 mm
- Keyway width shown: 3.0 mm
- Keyway length shown: 12.0 mm
- Controlled drawing references DIN 6885-A3X3X3

The simplified public STEP uses nominal cylindrical thread envelopes and does not reproduce the detailed thread form or complete keyseat geometry.

## Input / Motor-Side Interface

- 2 x dia. 3.1 mm mounting holes
- Opposed mounting-hole center spacing: 22.0 +/- 0.1 mm
- Central input opening: dia. 13.0 +0.05 / 0 mm

The exact motor locating-bore tolerance remains controlled by the production drawing and should be confirmed for the selected motor.

## Public Simplified CAD

[Download 32P Simplified STEP - 4-Stage Reference](../../assets/downloads/32p/32P_Public_Simplified_STEP_v1.0_4-Stage.step){ .md-button .md-button--primary }

The public STEP retains:

- 32 mm external gearbox envelope
- 4-stage body length
- output shaft envelope
- output mounting interface
- input central opening
- input mounting-hole pattern

It intentionally omits:

- internal planet gears
- sun gear and ring gear detail
- internal carrier geometry
- bearings
- internal fasteners
- manufacturing-only internal geometry

## Final Design Release

Before final tooling or production release, confirm:

- selected ratio and stage count
- controlled drawing for that configuration
- motor shaft and locating interface
- output key / keyseat definition
- mounting tolerances
- radial and axial load direction
- duty cycle and thermal condition

[Request Controlled CAD / Engineering Support](../../request-cad-sample-quote.md){ .md-button }

## Related Resources

[32P Technical Datasheet](datasheet.md){ .md-button }
[Motor Integration Guide](motor-integration.md){ .md-button }
