---
title: 32P Planetary Gearbox CAD & Design-In Pack | SigGear
description: Public 32P 32 mm planetary gearbox Design-In Pack with datasheet, mechanical interface, simplified 4-stage STEP, motor integration guidance and controlled CAD request path.
---

# 32P Planetary Gearbox - Public CAD Design-In Pack

This page brings together the current public engineering resources for the SigGear **32P 32 mm planetary gearbox** so an engineer can move from preliminary selection to early mechanical design-in without searching across separate pages.

The current downloadable STEP is a **simplified 4-stage reference**. It is intended for packaging, mounting and early integration work. It is not the controlled production model and must not be used as a universal 1-4 stage CAD file.

## Design-In Path

1. **Select the frame and operating range** using the Technical Datasheet.
2. **Check mounting and shaft interfaces** using the Mechanical Interface.
3. **Place the public simplified STEP** into the early assembly or packaging model.
4. **Check the motor-side interface and operating point** using the Motor Integration Guide.
5. **Validate the selected configuration with a sample** under the real application load and duty cycle.
6. **Request configuration-specific controlled CAD / drawing** before final tooling, design freeze or production release.

## Current Public Reference Configuration

| Item | Public reference |
| --- | ---: |
| Model | 32P |
| Nominal outer diameter | 32 mm |
| Public CAD stage | 4-stage reference |
| 4-stage gearbox body length | 52.95 mm |
| Nominal output shaft diameter | 8 mm |
| Output shaft extension | 21.6 mm (+0.1 / -0.3 mm) |
| Reduction ratio range of 32P family | 3.5:1-509.1:1 |
| Rated allowable torque range of 32P family | 35.0-80.0 kgf.cm |
| Maximum momentary torque range of 32P family | 70.0-160.0 kgf.cm |
| Backlash at no load | <= 1.2 deg |
| Continuous permissible input speed | <= 8,000 rpm |

Maximum momentary torque is not a continuous operating rating. The torque and ratio ranges above cover the published 1-4 stage 32P family; the public STEP itself represents only the 4-stage external envelope.

## Files in This Design-In Pack

### 1. Technical Datasheet

Use the Datasheet for stage, ratio, body length, torque, efficiency, backlash, load and motor-matching references.

[Open 32P Technical Datasheet v1.0](datasheet.md){ .md-button .md-button--primary }

### 2. Mechanical Interface

Use the Mechanical Interface for the current public output shaft, mounting-hole and motor-side interface references.

[Open 32P Mechanical Interface v1.0](mechanical-interface.md){ .md-button }

### 3. Simplified Public STEP

The public STEP retains the external geometry required for early packaging and mechanical integration while omitting internal planetary transmission geometry.

[Download 32P Simplified STEP - 4-Stage Reference](../../assets/downloads/32p/32P_Public_Simplified_STEP_v1.0_4-Stage.step){ .md-button .md-button--primary }

### 4. Motor Integration Guide

Use this guide when the project starts from an existing motor or requires a matched motor + gearbox assembly.

[Open 32P Motor Integration Guide](motor-integration.md){ .md-button }

## What the Public STEP Is For

The simplified public CAD can be used for:

- installation-envelope review
- early assembly layout
- mounting-position review
- output-shaft packaging
- motor-side packaging review
- preliminary interference checking
- early prototype mechanical design

It intentionally does not expose the internal planetary gear train, carrier details, bearings, internal fasteners or manufacturing-only internal geometry.

## What Still Requires Controlled Engineering Data

Before final tooling, design freeze or production release, confirm the exact configuration against controlled information.

Required confirmation includes:

- selected reduction ratio
- stage count
- controlled drawing revision
- motor shaft and locating interface
- output key / keyseat definition
- final mounting tolerances
- radial and axial load direction
- continuous and momentary torque
- output speed
- duty cycle
- ambient and thermal condition
- prototype and expected annual quantity

For 1-, 2- or 3-stage CAD, request the configuration-matched file rather than modifying the public 4-stage model.

## Sample Validation Before Design Freeze

A CAD fit check does not replace application testing. The selected gearbox should be evaluated under the intended motor, load, speed, duty cycle and installation condition before the design is frozen.

[Open Sample Validation Workflow](../../engineering-center/sample-validation-workflow.md){ .md-button }

[Open Design-In Checklist](../../engineering-center/design-in-checklist.md){ .md-button }

## Request the Next Engineering File or Sample

If the 32P is a possible fit, send the selected ratio or target output speed, required continuous and momentary torque, motor information and installation constraints.

[Request Controlled CAD, Sample and Quote](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

## Related Product Resources

[View 32P Product Page](../../products/planetary-gearboxes/32p-planetary-gearbox.md){ .md-button }

[Compare 8P-42P Planetary Gearboxes](../../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
