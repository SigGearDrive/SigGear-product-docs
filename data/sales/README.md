# SigGear Public Sales Policy Data

This directory contains machine-readable public-safe sales rules for inquiry handling and AI-assisted retrieval.

It must not contain customer identities, customer requirements, prices, discounts, private quotations, internal costs, payment terms, negotiation strategy or confidential engineering files.

The YAML policy defines response order, qualification fields, prohibited claims and information that must remain private.

The `inquiry-measurement-schema.yml` file defines a public-safe funnel and normalized analytics dimensions. It deliberately separates website intent from an actual received inquiry and from a manually confirmed qualified inquiry.

Website analytics must use categories, counts and presence flags only. Customer-specific identities, free-text requirements, engineering values and private qualification outcomes remain outside this public repository and outside GA4 event parameters.
