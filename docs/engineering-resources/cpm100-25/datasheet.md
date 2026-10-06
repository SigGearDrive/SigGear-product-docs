---
title: CPM-100-25 Datasheet | 25 Nm Cycloidal Robot Joint Module | SigGear
description: Public CPM-100-25 engineering reference with published dimensions, torque, speed, electrical parameters, load limits and configuration notes for early evaluation.
---

# CPM-100-25 Technical Datasheet v1.0

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-06

CPM-100-25 is a 100 mm integrated cycloidal robot joint module with a 25:1 reduction ratio, 25 Nm rated output torque and 60 rpm rated output speed.

This page consolidates values already published on the current CPM-100-25 product page. Driver, encoder, communication and closed-loop functions depend on the ordered configuration and must be confirmed in the quotation.

## Key Performance

| Parameter | Published value |
| --- | --- |
| Transmission structure | Cycloidal pinwheel |
| Outer diameter | 100 mm |
| Product thickness | 29.5 mm |
| Reduction ratio | 25:1 |
| Backlash | 5-10 arcmin |
| Operating voltage | 24-48 VDC |
| Rated motor power | 213 W |
| Rated output speed | 60 rpm |
| No-load output speed | 90 rpm |
| Rated output torque | 25 Nm |
| Peak output torque | 75 Nm |
| Weight | 630 g |
| Allowable radial force | 500 N |
| Allowable axial force | 300 N |

!!! warning
    Peak torque is not a continuous rating. Peak-torque duration depends on operating voltage, current limit, duty cycle and thermal conditions.

## Motor and Electrical Parameters

| Parameter | Published value |
| --- | --- |
| Motor KV value | 63 rpm/V |
| Thermistor | 10 kOhm, B3435, +/-1% |
| Phase inductance | 290 uH |
| Phase current full scale | 33 A |
| Rated bus current | 15 A |
| Static working bus current | 0.08 A |
| Back-EMF constant | 0.143 Vs/rad |

## Available Configuration Paths

The current public CPM-100-25 page shows two representative supply configurations:

- **Without integrated driver:** motor and cycloidal transmission assembly for use with an external drive solution selected for the project.
- **With integrated driver:** selected driver housing and interface arrangement integrated with the module.

Final encoder, connector, cable, communication and control functions must be confirmed in the quotation and technical agreement.

A separate **dual-encoder configuration** is confirmed under the controlled drawing code **SG2556D**. It has a different axial package, weight and no-load speed from the base configuration and is documented separately.

[View CPM-100-25 Dual Encoder Variant](dual-encoder-variant.md){ .md-button }

## Mechanical and Load Evaluation

For early evaluation, use the public envelope and load limits above.

Final suitability depends on:

- Mounting geometry
- Load direction and load offset
- Duty cycle
- Speed
- Shock loading
- Thermal conditions
- Driver-equipped or non-driver configuration

[View CPM-100-25 Mechanical Interface Reference](mechanical-interface.md){ .md-button }

## CAD, Drawings and Integration Documentation

A public STEP model is **not currently released in this repository** for CPM-100-25.

Detailed STEP models, 2D drawings, mounting drawings and configuration-specific integration documents are available after project review.

[Request CAD, Drawing or Integration Files](../../request-cad-sample-quote.md){ .md-button .md-button--primary }

## Noise, Life and Thermal Data

Noise-test records, service-life parameters and application-specific thermal limits are not published here as universal ratings because they depend on installation, load, speed, lubrication, duty cycle and thermal conditions.

Request project-specific information when these factors are part of the selection requirement.

## Selection Information Required

Please provide:

- Application and joint position
- Rated and peak torque
- Required peak-torque duration
- Required output speed
- Operating voltage
- Installation envelope
- Duty cycle
- Radial and axial load condition
- Driver, encoder and communication requirements
- Prototype quantity and estimated annual quantity

## Related Pages

[CPM-100-25 Product Page](../../products/cycloidal-joint-modules/cpm100-25.md){ .md-button }
[Custom Cycloidal Transmission Engineering](../../custom-engineering/custom-cycloidal-transmission.md){ .md-button }
[Robot Joint Selection Guide](../../selection-guides/robot-joint-actuator-selection-guide.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
