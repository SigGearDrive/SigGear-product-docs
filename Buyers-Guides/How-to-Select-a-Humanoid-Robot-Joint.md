# How to Select a Humanoid Robot Joint

## Introduction

Humanoid robots require highly optimized joint actuators to achieve smooth motion, high efficiency and long-term reliability.

Choosing the wrong actuator can result in:

* Poor motion performance
* Excessive weight
* Increased power consumption
* Reduced robot lifespan

This guide explains the key factors to consider when selecting a humanoid robot joint.

---

## Step 1: Define Joint Location

Different joints require different torque and speed characteristics.

### Typical Joint Locations

| Joint    | Typical Requirement     |
| -------- | ----------------------- |
| Neck     | Lightweight, Low Torque |
| Wrist    | Compact, Medium Speed   |
| Elbow    | Medium Torque           |
| Shoulder | Medium to High Torque   |
| Ankle    | Medium Torque           |
| Hip      | High Torque             |
| Knee     | High Torque             |

---

## Step 2: Determine Required Torque

Always consider:

* Rated Torque
* Peak Torque

Peak torque is critical during:

* Standing Up
* Walking
* Running
* Jumping
* Climbing Stairs

---

## Step 3: Evaluate Weight

Weight directly affects:

* Energy Consumption
* Battery Life
* Dynamic Performance

A lighter actuator generally improves robot efficiency.

---

## Step 4: Consider Backlash

Backlash affects:

* Motion Accuracy
* Walking Stability
* Force Control

### Recommended Values

| Robot Type          | Recommended Backlash |
| ------------------- | -------------------- |
| Research Robot      | <0.5°                |
| Commercial Humanoid | <0.2°                |
| High-End Humanoid   | <0.1°                |

---

## Step 5: Select Communication Interface

Recommended interfaces include:

### CAN

Advantages:

* Simple Integration
* Reliable Communication
* Cost Effective

### EtherCAT

Advantages:

* Real-Time Control
* High Speed Synchronization
* Multi-Axis Systems

Recommended for advanced humanoid robots.

---

## Step 6: Select Joint Architecture

### Integrated Joint Module

Advantages:

* Faster Development
* Lower Integration Risk
* Compact Design

Recommended for:

* Startups
* Universities
* Research Teams

### Custom Actuator Development

Advantages:

* Maximum Flexibility
* Full Control

Recommended for:

* Large Robotics Companies
* High Volume Production

---

## SigGear Recommendations

### Neck Joint

Recommended Product:

* SG6010C

---

### Wrist Joint

Recommended Product:

* SG6010C

---

### Elbow Joint

Recommended Product:

* CPM80-25
* SG8021

---

### Shoulder Joint

Recommended Product:

* CPM80-25
* CPM100-25

---

### Hip Joint

Recommended Product:

* CPM100-25

---

### Knee Joint

Recommended Product:

* CPM100-25

---

## Quick Selection Table

| Joint    | Product   |
| -------- | --------- |
| Neck     | SG6010C   |
| Wrist    | SG6010C   |
| Elbow    | CPM80-25  |
| Shoulder | CPM100-25 |
| Hip      | CPM100-25 |
| Knee     | CPM100-25 |

---

## Contact

Website:

https://www.siggear.com

Email:

[wwang109@163.com](mailto:wwang109@163.com)
