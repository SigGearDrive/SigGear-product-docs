# SigGear Product Data Dictionary

SigGear product master-data records provide a machine-readable inventory of the claims already published on canonical product pages. They support GitHub search, AI-assisted retrieval and automated consistency checks.

## Record Location

Product records are stored in `data/products/`. One YAML file represents one published model or series.

## Record Fields

| Field | Meaning |
| --- | --- |
| `schema_version` | Version of the record structure |
| `record_id` | Stable lowercase identifier matching the YAML filename |
| `record_type` | `model` or `series` |
| `model` | Official model number for a model record |
| `display_name` | Human-readable product or series name |
| `product_family` | Controlled product-family identifier |
| `canonical_page` | Unique public page for the model or series |
| `public_page_status` | Publication state of the canonical page |
| `record_status` | Status of the structured inventory record |
| `configuration_summary` | Boundary statement for included or configuration-dependent components |
| `published_specifications` | Exact public value strings mirrored from the canonical page |
| `sales_usage` | Permitted preliminary use, confirmation requirements and prohibited shortcuts |
| `technical_review` | Public inventory status and boundary for non-public source or approval records |
| `source_control` | Public claim source and handling of non-public technical sources |
| `cad_control` | Non-sensitive CAD / drawing source status, including approved drawing reference code and whether detailed assembly CAD is public or request-only |
| `inventory_checked_on` | Date the record was compared with the public page |

## Status Meanings

`public_page_status: published` means the canonical page is publicly available. It does not replace a quotation or technical agreement.

`record_status: published_inventory` means the YAML record mirrors the current public page. It does not independently certify the engineering value.

`technical_source_status: not_recorded_in_public_repository` means drawings, test records or internal approvals are intentionally not stored in this public repository. It does not mean that no technical source exists.

## Exact-String Rule

Values in `published_specifications` preserve the text shown on the canonical page, including ranges, tolerances and units. For example, `24–48 VDC` must not be silently changed to `48 V` or converted into a different rating.

The automated validator checks that every recorded value still appears on its canonical page. If a page specification changes, the corresponding YAML record must change in the same pull request.

## Configuration Boundaries

The product record must not turn an optional function into a standard claim. Driver, encoder, brake, CAN, RS485, EtherCAT and control-mode availability remain configuration-specific unless the canonical model page explicitly states otherwise.

The `sales_usage` block identifies what may be used for preliminary selection and which topics must be confirmed before quotation or final model approval. A prohibited item is a shortcut that must never be taken, such as treating peak torque as continuous torque or promising an optional interface as standard.

## Technical Review Boundary

`technical_review.public_inventory_status: complete` means the current public page has been inventoried into the YAML record. It does not mean that this GitHub review performed engineering approval.

Controlled source documents, approval records and reviewer identities remain outside the public repository unless SigGear explicitly approves a non-sensitive reference code for publication. A product record may store that approved reference code and the review date without publishing the underlying controlled drawing. `next_internal_action` describes the reconciliation or revision-control work that remains.

## CAD Control Boundary

When `cad_control` is present:

- `controlled_2d_drawing` records only the approved non-sensitive drawing identifier.
- `full_assembly_step_status` records whether detailed assembly CAD has been reviewed and how it may be supplied.
- `public_raw_assembly_step: false` means the full internal assembly is not a public download.

The structured record does not contain the controlled drawing or full assembly CAD itself.

## Source Boundary

These records contain public product data and non-sensitive source-control metadata only. Customer files, prices, internal costs, supplier information, unreleased products, private drawings, restricted test reports and NDA material must not be added.

## Validation

Run:

```bash
python scripts/validate_product_data.py
```

The check verifies required fields, unique identifiers, canonical-page coverage and exact published-claim synchronization.
