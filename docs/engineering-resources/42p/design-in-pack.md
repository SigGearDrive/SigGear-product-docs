---
title: 42P Planetary Gearbox Design-In Pack | 42 mm Gearbox | SigGear
description: Engineering Design-In Pack for the SigGear 42P 42 mm planetary gearbox with datasheet, controlled mechanical interface, CAD request path, data boundaries and sample validation workflow.
---

# 42P Planetary Gearbox - Design-In Pack

This page brings together the current engineering resources for the SigGear **42P 42 mm planetary gearbox** so an engineer can move from preliminary frame selection to interface review, configuration-specific CAD request and sample validation.

The 42P currently has a public Datasheet, a public Mechanical Interface based on controlled drawing **SG01PD42**, and a simplified public 4-stage STEP for early mechanical packaging and Design-In.

For early design-in, use the published envelope and interface references below. For final CAD placement, tooling or design freeze, request the configuration-matched controlled CAD.

## Design-In Path

1. **Check frame size, ratio range and torque range** in the Technical Datasheet.
2. **Review the output and motor-side interfaces** in the Mechanical Interface.
3. **Select the likely stage count and body length** from the published configuration table.
4. **Send the selected ratio / stage and motor interface** to request configuration-matched CAD.
5. **Validate the selected gearbox with a sample** under the real load, speed and duty cycle.
6. **Freeze the configuration only after the controlled drawing / CAD revision is confirmed.**

## Current Public Selection Reference

| Item | Public reference |
| --- | ---: |
| Model | 42P |
| Nominal outer diameter | 42 mm |
| Number of stages | 1-4 |
| Gearbox body length range | 35.6-69.5 mm |
| Reduction ratio range | 3.8:1-660.7:1 |
| Rated allowable torque range | 80.0-150.0 kgf.cm |
| Maximum momentary torque range | 160.0-300.0 kgf.cm |
| Efficiency range | 66-90% |
| Backlash at no load | <= 1.2 deg |
| Continuous permissible input speed | <= 8,000 rpm |
| Operating temperature range | -40 to 120 C |
| Radial load, 10 mm from flange | <= 16.0 kgf |
| Shaft axial load | <= 8.0 kgf |
| Radial shaft play | <= 0.04 mm |
| Thrust shaft play | <= 0.3 mm |
| Housing / gear material | Steel / Steel |
| Output bearing | Ball bearings |
| Adapted DC motor voltage | 3-48 VDC |
| Adapted DC motor power | below 200 W |

Maximum momentary torque is not a continuous operating rating.

## Stage, Length and Ratio Reference

| Stages | Gearbox body length L | Available reduction ratios | Rated allowable torque | Maximum momentary torque | Efficiency |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | 35.6 mm | 3.8 / 4.3 / 5.1 | 80.0 kgf.cm | 160.0 kgf.cm | 90% |
| 2 | 46.9 mm | 14.4 / 16.3 / 18.6 / 19.2 / 21.8 / 25.7 | 100.0 kgf.cm | 200.0 kgf.cm | 80% |
| 3 | 58.2 mm | 54.4 / 61.9 / 70.4 / 72.8 / 80.1 / 82.8 / 94.2 / 97.4 / 110.8 / 130.3 | 120.0 kgf.cm | 240.0 kgf.cm | 73% |
| 4 | 69.5 mm | 206.4 / 234.6 / 266.8 / 276 / 303.5 / 313.9 / 345 / 357 / 369.2 / 406 / 419.9 / 477.5 / 493.93 / 561.70 / 660.7 | 150.0 kgf.cm | 300.0 kgf.cm | 66% |

## Mechanical Interface Reference

The current controlled drawing reference is **SG01PD42**.

Published interface information includes:

- nominal gearbox diameter: **42 mm**
- output-side extension shown on drawing: **29.5 mm (+0.1 / -0.3 mm)**
- output-side mounting: **4 x M4 threaded holes, depth 6 mm**
- output-side reference circle: **35.0 +/- 0.1 mm**
- output keyway reference: **DIN 6885-A4x4x20**
- motor-side center opening: **16.0 mm**
- motor-side mounting: **2 x 3.1 mm holes**
- opposed motor-side mounting-hole spacing: **25.0 +/- 0.1 mm**

[Open 42P Mechanical Interface v1.1](mechanical-interface.md){ .md-button .md-button--primary }

## Technical Datasheet

Use the Datasheet for stage, ratio, body length, torque, efficiency, backlash and motor-matching references.

[Open 42P Technical Datasheet v1.1](datasheet.md){ .md-button .md-button--primary }

## Motor Integration

For projects starting from an existing DC motor or requiring a matched motor + gearbox assembly, use the 42P Motor Integration Guide.

[Open 42P Motor Integration Guide](motor-integration.md){ .md-button .md-button--primary }

## CAD Release Status

**Public simplified STEP:** released as a 4-stage reference.

[Download 42P Simplified STEP - 4-Stage Reference](../../assets/downloads/42p/42P_Public_Simplified_STEP_v1.0_4-Stage.step){ .md-button .md-button--primary }

**Detailed full-assembly STEP:** reviewed internally and retained as configuration-controlled engineering CAD.

The detailed assembly contains internal planetary transmission geometry and is therefore not published as a raw public download.

For early packaging or mechanical integration, request the CAD that matches the selected:

- reduction ratio
- stage count
- motor interface
- output interface

[Request 42P Controlled CAD](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

## Public Data Gaps - Confirmation Required

The current 42P specification sheet now confirms the main mechanical operating limits used for preliminary design-in: continuous permissible input speed, operating temperature, radial load, axial load and shaft-play limits.

The following values are still **not confirmed from the current 42P source**:

- service-life data
- noise data

These items remain **to be confirmed** from a controlled specification, test record or engineering approval before they are used in a quotation, customer Datasheet or application claim.

## What Can Be Done With the Current Pack

The currently released information is suitable for:

- preliminary model comparison
- stage and ratio selection
- gearbox envelope review
- mounting-interface review
- motor-side packaging review
- initial engineering discussion
- controlled CAD request
- sample planning

It is not sufficient by itself for final tooling or production release.

## Sample Validation Before Design Freeze

A drawing or CAD fit check does not replace application validation. Test the selected gearbox under the intended motor, output load, output speed, duty cycle and installation condition before design freeze.

[Open Sample Validation Workflow](../../engineering-center/sample-validation-workflow.md){ .md-button }

[Open Design-In Checklist](../../engineering-center/design-in-checklist.md){ .md-button }

## Information to Send for 42P Review

For a fast engineering review, send:

- application
- target output speed or reduction ratio
- continuous and momentary output torque
- motor type, voltage, speed and power
- motor shaft dimensions
- available installation space
- output shaft / mounting requirements
- radial or axial external load if relevant
- duty cycle
- prototype quantity and estimated annual quantity

## Request CAD, Sample or Quote

[Request 42P CAD, Sample and Quote](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

## Related Product Resources

[View 42P Product Page](../../products/planetary-gearboxes/42p-planetary-gearbox.md){ .md-button }

[Compare 8P-42P Planetary Gearboxes](../../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
