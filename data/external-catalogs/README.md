# External CAD Catalog Master Data

This directory defines the platform-neutral distribution layer for SigGear's public CAD catalog.

## Source-of-truth rule

Technical specifications are **not duplicated here**. Each external-catalog record points to an approved product master record in `data/products/`.

The export script joins:
- approved public product data;
- public product / datasheet / mechanical-interface URLs;
- released simplified STEP CAD;
- external-catalog naming and publication policy.

This reduces the risk of TraceParts, 3Dfindit, DirectIndustry, GlobalSpec and the SigGear website drifting into different values.

## Current planetary publication unit

The 8P–42P range is published externally as **12 product-family references**, not as invented orderable SKUs for every ratio and stage.

A catalog reference such as `32P` identifies the gearbox family. The final orderable configuration depends on stage count, ratio, shaft/interface and motor matching.

## CAD boundary

The released public CAD is a **simplified 4-stage reference** for preliminary packaging and mechanical Design-In.

It must not be represented as:
- detailed internal planetary geometry;
- a universal CAD model for 1-, 2-, 3- and 4-stage versions;
- a final production drawing.

Configuration-specific CAD remains controlled and requires engineering review.
