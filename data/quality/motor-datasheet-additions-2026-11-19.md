# Motor source additions — 2026-11-19

Three **new, source-image-backed Draft V1.0** DC motor datasheets were produced from owner-provided source sheets and added to the one-click motor download hub (36 PDFs total, Ø8–32 mm).

| PDF | Source screenshot | Source motor data | Uploaded PDF SHA-256 |
| --- | --- | --- | --- |
| `SigGear_20mm_DC_Motor_120108_DraftV1.0.pdf` | `20mm 1.PNG` | Ø20 mm, 12 V, 10 g·cm nominal source torque | `a4d4059095441dbd38b91498981590af7207bc72c3f8a713d90ffda54d8feba1` |
| `SigGear_20mm_DC_Motor_120100_DraftV1.0.pdf` | `20mm 2.PNG` | Ø20 mm, 12 V, 40 g·cm nominal source torque | `c074964d522ddfad874a95496d463c979fac2a31183b2480c955b55aacc14f7f` |
| `SigGear_24mm_DC_Motor_090080-240092_DraftV1.0.pdf` | `24mm 1.PNG` | Ø24 mm, 090080 / 120074 / 150082 / 180088 / 240092 variants | `6d8571339c746af687b2a091f38f4a3c08b79e6d80460181df444de694b0ae59` |

All PDFs use vector-retypeset specification tables and preserve their original source screenshot on the appendix page, including original drawings and source curves, without pretending the raster input acquired additional detail. The source language `Mh` for inductance is retained pending verification.

**Engineering review:** The `20mm 1.PNG` source performance curve is marked **HS-2016-Q** but its source table is labeled **120108**. Motor/curve equivalence must be confirmed. Bearing arrangement, dimensional tolerances, continuous-torque conditions and motor-to-gearhead assembly interface are not independently certified here. Treat stall torque as a short-duration reference only.

These are supplier-source draft technical sheets, **not** revised/qualified mechanical drawings, controlled performance tests, or complete motor + gearhead assembly specifications. Existing published 20 mm and 24 mm BLDC sheets were retained separately.

The PDF SHA values are of the exact binary blobs uploaded to GitHub for release integrity; no new formulas or calculated motor curves were introduced.
