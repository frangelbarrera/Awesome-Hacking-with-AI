# Catalog Maintenance Guide

The Markdown catalogs are the human-readable source of truth for promoted resources. `docs/resource-catalog.json` is a generated artifact for tools and checks; do not edit it by hand.

> **Goal:** every promoted resource remains traceable to a canonical source and carries enough context for readers to assess its status, effects, and safe adoption boundary.

## 1. Update Procedure

When adding, changing, or retiring a resource, update the applicable row in `docs/RESOURCE_CATALOG.md` or `docs/RESOURCE_CATALOG_SUPPLEMENT.md` first. Then regenerate and validate the JSON artifact from the repository root.

```shell
python3 scripts/export_catalog.py
python3 scripts/export_catalog.py --check
python3 scripts/validate_catalog_integrity.py
python3 scripts/validate_catalog_coverage.py
```

The first command regenerates `docs/resource-catalog.json`. The remaining commands verify that the committed JSON exactly matches the Markdown source tables, that its count and required fields are internally consistent, and that README discovery resources have catalog metadata.

| Source artifact | Role | Editing rule |
|---|---|---|
| `docs/RESOURCE_CATALOG.md` | Detailed metadata for high-impact resources. | Update directly when an entry is promoted, materially revised, or retired. |
| `docs/RESOURCE_CATALOG_SUPPLEMENT.md` | Metadata for discovery resources not yet promoted to the detailed catalog. | Update directly for secondary or discovery-stage entries. |
| `docs/resource-catalog.json` | Machine-readable export of the two Markdown catalogs. | Regenerate only with `scripts/export_catalog.py`; never hand-edit. |
| `README.md` | Discovery and navigation layer. | Promote a resource only after an appropriate catalog row exists. |

## 2. Who May Mark a Resource as Verified

Only a repository maintainer with review authority may change an entry from an unverified/review-required condition to **Verified** or an equivalent positive assertion about license, maintenance, provenance, or a security property. The reviewer must preserve the date and a link to the supporting canonical source in the pull request or linked issue.

| Claim being made | Minimum evidence |
|---|---|
| Canonical source or maintainer | Official project, publisher, organization, or repository ownership record. |
| License or terms | License file, package metadata, model/dataset card, or other canonical terms page. |
| Current maintenance status | Recent release/commit history plus maintainer statement or a formal archive/deprecation notice. |
| Security property or performance claim | Primary paper, official technical documentation, reproducible evaluation, or an explicitly labeled vendor result. |
| Safe operational use | Permission inventory, data-flow review, isolated test result, and an authorized adoption decision for the local environment. |

A positive metadata change should never be inferred from popularity, stars, a package name, a search result, or an unaudited third-party directory.

## 3. Status and Review Rules

Use cautious labels when evidence is incomplete. **Review Required** means the resource may still be useful for research or discovery, but the repository does not attest to its current terms, maintenance, or operational suitability. **Experimental**, **Historical**, **Archived**, and **Superseded** should remain visible when they provide unique context, with their limitation stated plainly.

| Change event | Required action |
|---|---|
| New README resource | Add a catalog row before or in the same change; run all four commands above. |
| License/status evidence found | Update the row, retain the evidence link, identify the review date in the change record, and regenerate JSON. |
| Upstream archive, transfer, or major release | Update status and canonical URL; check dependent documentation and links. |
| Security concern or dual-use issue | Follow `SECURITY.md`; avoid publishing sensitive details before responsible review. |
| Repeated 429, redirect, or link failure | Record the check date and outcome in an issue or pull request; replace, retain with note, or retire the link. |

## 4. Review Record

Use the existing issue and pull-request templates. A review record must identify the reviewer, date, resources changed, sources consulted, validation commands run, decision, and any follow-up date. The [Maintenance Register](../MAINTENANCE.md) defines the recurring review cadence; this guide defines the reproducible implementation of the catalog portion of that cadence.
