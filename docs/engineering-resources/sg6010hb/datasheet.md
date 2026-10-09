---
title: SG-6010HB Datasheet | 67 mm Planetary Exoskeleton Joint Motor | SigGear
description: Public SG-6010HB engineering datasheet with 67 mm diameter, 25.57 mm thickness, 9.67:1 ratio, 6 Nm rated torque, 18 Nm peak torque and 310 rpm rated speed.
---

# SG-6010HB Technical Datasheet v1.0

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-09  
**Public source:** Current SigGear product catalog

SG-6010HB is a compact planetary joint motor published by SigGear for exoskeleton joint applications. This datasheet consolidates the current catalog values without adding unpublished driver, encoder or interface claims.

## Key Performance

| Parameter | Published value |
| --- | --- |
| Transmission structure | Planetary structure |
| Outer diameter | 67.0 mm |
| Product thickness | 25.57 mm |
| Reduction ratio | 9.67:1 |
| Backlash | 15–20 arcmin |
| Motor power | 328 W |
| Rated voltage | 12–48 V |
| Rated output speed | 310 rpm |
| No-load output speed | 400 rpm |
| Rated output torque | 6 Nm |
| Peak output torque | 18 Nm |
| Weight | 298.5 g |
| Allowable radial force | 250 N |
| Allowable axial force | 100 N |

!!! warning
    Peak torque is not a continuous working rating. Peak duration, duty cycle and thermal suitability require application-specific confirmation.

A source-backed [SG-6010HB Thermal Test Record](thermal-test-record.md) is available. It records time from 30°C to 100°C at several torque levels under stall and 110 rpm load conditions; it does not by itself establish a continuous-duty thermal rating.

## Electrical and Motor Parameters

| Parameter | Published value |
| --- | --- |
| Phase damping | 224 µΩ |
| Phase inductance | 235 µH |
| Phase current full scale | 33 A |
| Rated bus current | 12 A |
| Static working bus current | 0.08 A |
| Motor structure | 18N20P |
| Motor torque constant | 0.0606 Nm/A |
| Thermistor | 10 kΩ B3435 ±1% |
| NTC B value | 3435 |
| Back EMF constant | 0.0727 Vs/rad |
| Motor KV value | 104 KV (catalog notation) |

**Terminology note:** “Phase damping” and “104 KV” are retained from the published catalog. Confirm the electrical definition and unit before using those two values in controller calculations.

## Published Application Positioning

The current SigGear catalog identifies SG-6010HB as an **exoskeleton joint motor**.

This identifies a real intended application direction; it does not mean the product is limited to exoskeletons or that every exoskeleton joint can use the same configuration.

## Mechanical Data Boundary

The SG2908B controlled drawing has now been reviewed.

Public early-design information is summarized in the [SG-6010HB Mechanical Interface](mechanical-interface.md), including the 67 mm envelope, 22.57 ±0.50 mm main body thickness, nominal 3.00 ±0.30 mm output-side extension, selected mounting patterns and wiring references.

The controlled production drawing and detailed assembly STEP remain request-only. Request the current configuration-matched drawing / CAD before design freeze.

[View Mechanical Interface](mechanical-interface.md){ .md-button .md-button--primary }
[View Thermal Test Record](thermal-test-record.md){ .md-button }
[Request CAD / Drawing](../../request-cad-sample-quote.md){ .md-button }

## Electronics and Integration Boundary

The catalog source does not establish a standard integrated driver, encoder, communication protocol or firmware package for SG-6010HB.

Confirm the required:

- Driver
- Encoder / feedback
- CAN / RS485 / other communication
- Position, speed or torque control
- Connector / cable
- Brake or holding behavior

before quotation and integration.

## Related Resources

[SG-6010HB Product Page](../../products/robot-joint-actuators/sg6010hb.md){ .md-button }
[Exoskeleton Joint Selection Guide](../../applications/exoskeleton-joint-actuators.md){ .md-button }
[Custom Robot Joint Development](../../custom-engineering/robot-joint-actuator-development.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
