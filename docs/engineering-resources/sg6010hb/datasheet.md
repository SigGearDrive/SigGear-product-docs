---
title: SG-6010HB Datasheet | 67 mm Planetary Exoskeleton Joint Motor | SigGear
description: Public SG-6010HB engineering datasheet with 67 mm diameter, 25.57 mm thickness, 9.67:1 ratio, 6 Nm rated torque, 18 Nm peak torque and 310 rpm rated speed.
---

# SG-6010HB Technical Datasheet v1.0

**Status:** Public engineering evaluation reference  
**Online record:** 2026-10-09 · **Reference PDF:** Rev0.1, 2026-11-19  
**Public source:** Current SigGear product catalog

[**Download SG-6010HB Reference Datasheet PDF**](../../assets/downloads/joint-actuators/SG-6010HB_Public_Reference_Datasheet_Rev0.1.pdf){ .md-button .md-button--primary }

The PDF summarizes the **catalogue product**, not an independently approved 2D/3D CAD envelope.

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

The supplied SG2908B 2D source has been reviewed for its readable nominal mounting features. The separate SG2908B exchange STEP was imported on 2026-11-19, but its full-assembly envelope still requires engineering reconciliation with the catalogue.

Public early-design information is summarized in the [SG-6010HB Mechanical Interface](mechanical-interface.md), including the 67 mm envelope, 22.57 ±0.50 mm main body thickness, nominal 3.00 ±0.30 mm output-side extension, selected mounting patterns and wiring references.

The controlled production drawing and detailed internal assembly STEP remain **request-only**. No downloadable SG-6010HB STEP is approved; request configuration-matched exterior CAD and the current drawing revision before design freeze.

[View Mechanical Interface](mechanical-interface.md){ .md-button .md-button--primary }
[View Thermal Test Record](thermal-test-record.md){ .md-button }
[View Driver & Communication](driver-communication.md){ .md-button }
[Request CAD / Drawing](../../request-cad-sample-quote.md){ .md-button }

## Driver-Equipped Configuration

SigGear has confirmed that the present **driver-equipped SG-6010HB configuration** uses the SG6010 driver platform documented in the current user manual.

Confirmed platform-level integration features include:

- 15–48 V DC rated driver voltage
- 16-bit single-turn absolute main encoder
- CAN Simple
- CANopen (CiA301 / CiA302 / CiA402)
- RS485 / Modbus RTU with the corresponding interface configuration
- Position, velocity, torque and MIT-style motion control
- Type-C debugging / host communication
- Second-encoder interface through I2C or UART

[View Driver & Communication Reference](driver-communication.md){ .md-button .md-button--primary }

!!! note
    The actuator catalog states 12–48 V, while the driver manual states 15–48 V DC rated driver operation and a 12 V minimum boundary. For the driver-equipped system, do not treat 12 V as a rated operating point without engineering confirmation.

Driver hardware revision, firmware, second-encoder hardware, cable / connector set, brake behavior and expansion interfaces must still be matched to the ordered configuration.

## Related Resources

[SG-6010HB Product Page](../../products/robot-joint-actuators/sg6010hb.md){ .md-button }
[Exoskeleton Joint Selection Guide](../../applications/exoskeleton-joint-actuators.md){ .md-button }
[Custom Robot Joint Development](../../custom-engineering/robot-joint-actuator-development.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
