# Pre-Adoption Review

This review is required before operational use of any tool, agent, MCP server, model, dataset, lab, or benchmark whose catalog row is marked **not verified at review date**, **experimental**, **historical**, **archived**, or **Review Required**. A repository listing is a discovery aid; it is not approval to install, connect, execute, upload data, or grant credentials.

## 1. Review Record

Create a dated issue or pull request for the specific resource and retain the following record.

| Field | Required evidence |
|---|---|
| Resource and exact version | Canonical URL, release/tag/commit or artifact hash, and date checked. |
| Owner and provenance | Maintainer identity, official source, release source, dependency origin, and any transfer/supersession notice. |
| License and terms | Exact published license, model/dataset card terms, API terms, commercial restrictions, and compatibility with intended use. |
| Status | Active, experimental, archived, historical, superseded, or unknown, with the upstream evidence. |
| Intended use | Authorized workflow, environment, users, scope, owner, expiration, and prohibited uses. |
| Permissions and effects | Data stores, filesystems, network destinations, tools, credentials, and highest expected effect: knowledge, read, external query, write, or execution. |
| Data and privacy | Data classification, retention, third-party transfer, secrets/PII handling, and redaction requirements. |
| Isolation and controls | Environment separation, identity, least privilege, sandboxing, egress, resource limits, approval gates, and logging. |
| Evaluation | Test plan, expected outcome, known limitations, independent validation, and rollback/cleanup process. |
| Decision | Approved for a named scope, approved with conditions, deferred, or rejected; reviewer and next review date. |

## 2. Review Sequence

Start with provenance, terms, and status. If the resource does not have a canonical source or acceptable terms, do not proceed. Then define the authorized use, create a minimal permission design, assess data flows, and test in an isolated environment. Review tool effects and expected failure modes before connecting any production data, external endpoint, service identity, or execution capability.

For agents and MCP servers, obtain explicit human approval before any write, execution, external communication, or action against an authorized target. For models and datasets, verify cards, data origin, training or adaptation rights, and pre/post safety evaluation. For benchmarks and labs, preserve version, task conditions, attempts, and result artifacts so claims remain interpretable.

## 3. Decision Rules

| Decision | Conditions |
|---|---|
| Approved for named scope | Evidence is complete, risk is understood, required controls are in place, and a named owner accepts residual risk. |
| Approved with conditions | Low-risk evaluation only; conditions state environment, time limit, data limits, permissions, and review date. |
| Deferred | Critical provenance, terms, status, security, privacy, or evaluation evidence is missing. |
| Rejected | No canonical source, incompatible terms, unacceptable risk, unsafe operational design, or lack of an authorized use case. |

## 4. Recurring Review

Operational approval expires when the resource, model, dataset, tool definition, permission set, deployment, or environment changes materially. It also expires if the upstream project is archived, compromised, renamed, or superseded. Record these events in [MAINTENANCE.md](../MAINTENANCE.md) or the associated review issue.

## 5. Relation to the Catalog

The [Resource Catalog](RESOURCE_CATALOG.md) and [Supplement](RESOURCE_CATALOG_SUPPLEMENT.md) identify discovery-level sources, known effects, and initial adoption boundaries. This document defines the additional local review required before use. It deliberately prevents a reader from treating a catalog row with unknown or unverified upstream facts as an endorsement.
