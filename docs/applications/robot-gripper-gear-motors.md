---
title: "Micro Planetary Gearheads for Dexterous Hands & Robot Grippers | SigGear"
description: "Evaluate SigGear Ø8–16 mm micro planetary gearheads for dexterous hands, tendon spools, finger joints and compact robot grippers. Compare published ratios, torque, PDF datasheets, 2D drawings and STEP CAD."
---

# Micro Planetary Gearheads for Dexterous Hands & Robot Grippers

For a dexterous hand, robotic finger or compact gripper, the gearhead should be selected from the **mechanism geometry, motor operating speed, required output motion, available diameter and continuous load** rather than from diameter alone.

SigGear publishes five micro planetary gearhead frame sizes from **Ø8 mm to Ø16 mm**. These are engineering starting points for compact mechanisms; they are **not claims that every model is already qualified for a specific robotic hand**.

[**Find a Gearhead by Motor RPM / Output RPM / Torque**](../selection-guides/planetary-gearhead-quick-selector.md){ .md-button .md-button--primary }
[**All 8–42 mm PDF / 2D / STEP Downloads**](../engineering-resources/planetary-gearboxes/public-cad-release-v1.md){ .md-button }
[**Already have a motor? Send the motor for matching**](../custom-engineering/custom-planetary-gearbox.md){ .md-button }

## Which SigGear Micro Gearhead Sizes Can Be Evaluated?

| Model | Nominal diameter | Published ratio range | Gearhead body length | Rated allowable torque range |
| --- | ---: | ---: | ---: | ---: |
| [8P](../products/planetary-gearboxes/8p-planetary-gearbox.md) | 8 mm | 3.8:1–731.16:1 | 10.15–18.10 mm | 19.6–39.2 mN·m |
| [10P](../products/planetary-gearboxes/10p-planetary-gearbox.md) | 10 mm | 3.5:1–428.7:1 | 10.25–18.50 mm | 127.5–196.1 mN·m |
| [12P](../products/planetary-gearboxes/12p-planetary-gearbox.md) | 12 mm | 3.5:1–509.1:1 | 11.35–19.60 mm | 196.1–411.9 mN·m |
| [14P](../products/planetary-gearboxes/14p-planetary-gearbox.md) | 14 mm | 3.75:1–443.3:1 | 15.20–26.60 mm | 343.2–588.4 mN·m |
| [16P](../products/planetary-gearboxes/16p-planetary-gearbox.md) | 16 mm | 3.85:1–459.5:1 | 17.55–30.45 mm | 392.3–882.6 mN·m |

The torque values above are **published rated allowable ranges across stages**, not one constant torque rating for every ratio. Use the model page or datasheet for the selected stage and ratio.

For a larger mechanism, continue with the [20–32 mm Miniature Planetary Gearhead range](../products/planetary-gearboxes/miniature-planetary-gearheads-20-32mm.md).

## Direct Micro Gearhead Downloads

| Model | Datasheet PDF | 2D drawing | Full STEP |
| --- | --- | --- | --- |
| 8P | [PDF](../assets/downloads/8p/8P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D](../assets/downloads/8p/8P_2D_Drawing.pdf) | [STEP](../assets/downloads/8p/8P_Full_Assembly.step) |
| 10P | [PDF](../assets/downloads/10p/10P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D](../assets/downloads/10p/10P_2D_Drawing.pdf) | [STEP](../assets/downloads/10p/10P_Full_Assembly.step) |
| 12P | [PDF](../assets/downloads/12p/12P_Planetary_Gearhead_Datasheet_Rev1.1.pdf) | [2D](../assets/downloads/12p/12P_2D_Drawing.pdf) | [STEP](../assets/downloads/12p/12P_Full_Assembly.step) |
| 14P | [PDF](../assets/downloads/14p/14P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D](../assets/downloads/14p/14P_2D_Drawing.pdf) | [STEP](../assets/downloads/14p/14P_Full_Assembly.step) |
| 16P | [PDF](../assets/downloads/16p/16P_Planetary_Gearhead_Datasheet_Rev1.0.pdf) | [2D](../assets/downloads/16p/16P_2D_Drawing.pdf) | [STEP](../assets/downloads/16p/16P_Full_Assembly.step) |

## What Does a Dexterous-Hand Engineer Need to Define?

A useful first selection usually needs:

- **Mechanism type** — tendon spool, direct rotary finger joint, linkage, screw or jaw mechanism
- **Required force / load** — fingertip force, tendon pull or mechanism resistance
- **Mechanism geometry** — spool radius, lever arm or linkage dimensions
- **Motor** — model, loaded speed, shaft diameter and mounting interface if already selected
- **Required output speed** — joint speed, spool speed or jaw motion
- **Available space** — maximum gearhead diameter, body length and total motor + gearhead length
- **Duty cycle** — continuous movement, short gripping events, hold time and rest time
- **Backlash / backdrivability target** — if these affect control or human interaction
- **Feedback** — motor encoder, output encoder or other position feedback if required

For a simple tendon spool, a first mechanical relation is:

**output torque ≈ tendon force × spool radius**

This is only a screening calculation. Friction, tendon routing, finger geometry, acceleration and transmission losses must also be considered in the real mechanism.

## If the Motor Is Already Selected

Do not choose a gearhead only by matching motor diameter.

Send:

1. motor drawing or exact model
2. loaded operating speed
3. shaft diameter and usable shaft length
4. mounting-hole pattern and locating pilot
5. target output speed
6. continuous / peak load
7. available diameter and total assembly length

SigGear can then review the closest published frame and the motor-to-gearhead interface.

[Planetary Gearhead for an Existing Motor](../custom-engineering/custom-planetary-gearbox.md){ .md-button .md-button--primary }

## What This Page Does Not Claim

The listed products are published gearhead platforms that can be evaluated for compact robotic mechanisms.

This page does **not** claim that:

- every listed size has been validated in a production dexterous hand
- rated gearhead torque equals verified fingertip force
- one ratio is suitable for every finger or gripper
- a standard motor interface will match every customer motor

Final selection depends on the actual mechanism, motor, ratio, duty cycle, interface and prototype test.

## Start a Project Review

If you already have the motor or hand mechanism, the fastest starting point is the motor drawing plus the required output motion and available space.

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Request Engineering Review](../request-cad-sample-quote.md?app=dexterous_hand_gripper){ .md-button .md-button--primary }

**Related:** [Micro Robotics Gear Motors](micro-robotics-gear-motors.md) · [8–16 mm Micro Gearheads](../products/planetary-gearboxes/micro-planetary-gearheads-8-16mm.md)
