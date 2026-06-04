# How to Choose a Robot Joint for Your Robot

## Introduction

Selecting the right robotic joint is one of the most important decisions in robot design.

The performance of a robot is heavily influenced by the actuator's torque, size, weight, backlash and communication interface.

This guide explains the key factors to consider when choosing a robotic joint module.

---

## Step 1: Determine Required Torque

The first step is to calculate:

* Rated Torque
* Peak Torque

Rated torque represents normal working conditions.

Peak torque represents short-term maximum load requirements.

### Typical Examples

| Application    | Recommended Torque |
| -------------- | ------------------ |
| Robot Hand     | 1–5 Nm             |
| Robot Wrist    | 3–10 Nm            |
| Robot Elbow    | 5–20 Nm            |
| Robot Shoulder | 10–40 Nm           |
| Robot Hip      | 20–100 Nm          |
| Robot Knee     | 20–100 Nm          |

---

## Step 2: Evaluate Available Space

Robotic systems often have strict size constraints.

Important factors include:

* Diameter
* Thickness
* Weight

Compact designs improve:

* Mobility
* Energy Efficiency
* Mechanical Integration

---

## Step 3: Consider Backlash

Backlash affects:

* Position Accuracy
* Motion Smoothness
* Force Control
* Stability

### Recommended Backlash Levels

| Application        | Recommended Backlash |
| ------------------ | -------------------- |
| Educational Robots | <1°                  |
| Service Robots     | <0.5°                |
| Industrial Robots  | <0.2°                |
| Humanoid Robots    | <0.1°                |

Cycloidal reducers generally provide lower backlash than planetary reducers.

---

## Step 4: Select Communication Interface

Common robotic communication interfaces include:

* CAN
* EtherCAT
* UART
* RS485

### CAN

Advantages:

* Simple Integration
* Cost Effective
* Widely Used

### EtherCAT

Advantages:

* Real-Time Performance
* High Speed
* Multi-Axis Synchronization

Recommended for:

* Humanoid Robots
* Industrial Robots
* High-End Automation

---

## Step 5: Choose the Transmission Type

### Planetary Transmission

Advantages:

* Compact
* Lightweight
* Efficient
* Cost Effective

Recommended for:

* Service Robots
* Educational Robots
* Mobile Robots

---

### Cycloidal Transmission

Advantages:

* Low Backlash
* High Torque Density
* Shock Resistance
* Long Service Life

Recommended for:

* Humanoid Robots
* Quadruped Robots
* Industrial Robot Joints

---

## SigGear Product Recommendations

### Lightweight Robots

Recommended Product:

* SG6010C

Typical Applications:

* Robot Hands
* Robot Necks
* Educational Robots

---

### Medium Payload Robots

Recommended Products:

* SG8021
* CPM80-25

Typical Applications:

* Robot Arms
* Exoskeletons
* Service Robots

---

### High Torque Robots

Recommended Product:

* CPM100-25

Typical Applications:

* Humanoid Hips
* Humanoid Knees
* Industrial Robot Joints

---

## Quick Selection Table

| Product   | Rated Torque | Application        |
| --------- | ------------ | ------------------ |
| SG6010C   | 6 Nm         | Small Robots       |
| SG8021    | 10 Nm        | Medium Robots      |
| CPM80-25  | 10 Nm        | Dynamic Robots     |
| CPM100-25 | 25 Nm        | High Torque Robots |

---

## Need Help Selecting a Joint?

SigGear engineers can assist with:

* Joint Selection
* Mechanical Integration
* Communication Interface Selection
* Custom Transmission Development

---

## Contact

Website:

https://www.siggear.com

Email:

[wwang109@163.com](mailto:wwang109@163.com)
