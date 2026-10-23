# SigGear Terminology and Units

Use these terms consistently across product pages, quotations, emails and technical discussions. A model-specific definition or test condition takes priority when explicitly stated.

## Product Terms

| Term | Controlled meaning |
| --- | --- |
| Robot joint actuator | A motor and transmission assembly for a robot joint; encoder and driver inclusion must be stated separately |
| Integrated joint module | A compact joint assembly combining multiple drive components; list the included motor, reducer, encoder, driver and brake explicitly |
| Precision planetary gearhead | **Preferred SigGear international product term** for the standalone 8–42 mm precision planetary reduction unit; select by model and configuration |
| Planetary gearbox | Engineering synonym for planetary gearhead; also retained in historical page URLs, CAD paths and legacy search terminology |
| Micro Planetary Gearheads | Published SigGear diameter class 8–16 mm: 8P, 10P, 12P, 14P and 16P |
| Miniature Planetary Gearheads | Published SigGear diameter class 20–32 mm: 20P, 22P, 24P, 28P and 32P |
| Compact Planetary Gearheads | Published SigGear diameter class 36–42 mm: 36P and 42P |
| Gearhead Only | A gearhead supplied for OEM integration with a customer-selected motor, subject to interface and operating-point review |
| Motor + Gearhead Assembly | A motor-matched gearhead drive assembled or evaluated for a specified project; exact inclusions must be confirmed |
| Cycloidal joint module | A joint-drive assembly using a cycloidal pinwheel transmission |
| Micro gear motor | A compact motor and gearbox assembly; motor type, diameter, ratio and feedback must be identified for a specific selection |
| Hub gear motor | A geared motor arranged for compact wheel or hub-drive integration |
| Standard configuration | The published baseline configuration for a model; it does not include optional functions unless stated |
| Customer-specific configuration | A configuration defined by a quotation, drawing or technical agreement for one project |

## Naming and Legacy Link Policy

Use **Gearhead** as the primary product naming convention for newly updated English product copy, title tags, model directories, application guides and inquiry labels. Keep **planetary gearbox** as a useful alternate search term in explanatory content. **Never rename a published URL path, public CAD filename, TraceParts link, or existing request parameter solely for terminology consistency.** Model-specific ratings and released engineering drawings remain the source of truth.

## Performance Terms

| Term | Controlled meaning |
| --- | --- |
| Rated torque | Output torque permitted under defined continuous or duty-rated conditions |
| Peak torque | Short-duration output torque subject to current, thermal and duty-cycle limits |
| Holding torque | Torque available while maintaining position under specified control and thermal conditions; not interchangeable with rated torque |
| Rated speed | Output speed associated with the stated rated operating point |
| No-load speed | Output speed measured without external working load under stated electrical conditions |
| Reduction ratio | Input speed divided by output speed, expressed as `ratio:1` |
| Backlash | Lost angular motion during direction reversal under a defined measurement method and load |
| Repeatability | Ability to return to the same position under repeated stated conditions |
| Accuracy | Difference between commanded or indicated position and actual position under a defined method |
| Radial load | Load acting perpendicular to the output axis |
| Axial load | Load acting along the output axis |
| Overturning moment | Bending moment applied to the output bearing or mounting structure |
| Duty cycle | Relationship between operating time, load states and rest time over a complete cycle |
| Backdrivability | Ability of an external output load to drive the mechanism backward under defined conditions |

## Electrical and Control Terms

| Term | Controlled meaning |
| --- | --- |
| Operating voltage | Permitted supply-voltage range for the confirmed configuration |
| Rated current | Current associated with a defined rated operating point; distinguish bus current from phase current |
| Encoder | Position-sensing device; state whether it measures motor-side or output-side position and whether it is incremental or absolute |
| Driver | Power electronics and control hardware used to commutate and control the motor |
| FOC | Field-oriented control for a suitable motor and feedback configuration |
| CAN | Controller Area Network physical/data-link technology; protocol and command set still require confirmation |
| RS485 | Differential serial physical layer; baud rate and application protocol require confirmation |
| EtherCAT | Industrial Ethernet fieldbus; availability must be confirmed for the selected driver and firmware |
| Closed-loop control | Control using measured feedback; identify the controlled variable, feedback location and loop implementation |

## Preferred Units and Formatting

| Quantity | Preferred unit | Example |
| --- | --- | --- |
| Torque | Nm | `25 Nm` |
| Speed | rpm | `120 rpm` |
| Power | W | `500 W` |
| Voltage | VDC | `24–48 VDC` |
| Current | A | `12 A` |
| Diameter and length | mm | `80 mm` |
| Mass below 1 kg | g | `430 g` |
| Mass at or above 1 kg | kg | `1.2 kg` |
| Backlash | arcmin | `5–10 arcmin` |
| Radial and axial force | N | `500 N` |
| Temperature | °C | `25 °C` |

Use a space between a number and its unit. Use an en dash for ranges. Do not mix output-side and motor-side values without labeling them.

