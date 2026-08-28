# Maintenance Register

This register makes the repository’s curation cadence visible. It is a maintenance aid, not a claim that every third-party project remains active or safe. Review dates apply to repository curation and should be updated when a maintainer completes the stated check.

## Review Schedule

| Review | Scope | Evidence to record | Cadence |
|---|---|---|---|
| Link health | README, guides, policy files, templates, and catalog sources | Workflow result, recurring redirects/429s, repaired or retired links | Weekly |
| High-risk resource review | Agents, MCP servers, scanners, models, datasets, labs, and external-query tools | Canonical URL, ownership, license/terms, status, effects, adoption boundary, and safety notes | Monthly |
| Living guidance review | OWASP, MCP, NIST, NCSC, MITRE ATLAS, benchmarks, and protocol versions | Source edition/version, supersession notice, material taxonomy changes | Quarterly |
| Full curation audit | All categories, duplicate entries, factual claims, evidence, content safety, and navigation | Audit issue or pull request with decisions and affected entries | Semiannual |

## Current Review Baseline

| Area | Last review | Status | Next due |
|---|---|---|---|
| Repository documentation and internal references | 2026-08-26 | Initial metadata and internal-link review completed | 2026-09-26 |
| External-link availability | 2026-08-26 | Automated availability check completed; redirects require continuing manual triage | 2026-09-02 |
| High-risk agents, MCP servers, models, datasets, and labs | 2026-08-26 | Catalog metadata established; pre-adoption upstream review remains mandatory | 2026-09-26 |
| Standards, protocol, and benchmark sources | 2026-08-26 | Canonical sources recorded; check for new editions or supersession | 2026-11-26 |
| Full curation, evidence, and dual-use review | 2026-08-26 | Baseline policy and catalog review completed | 2027-02-26 |

## Maintainer Continuity

`CODEOWNERS` is the authoritative list of reviewers for high-impact documentation and policy changes. The repository currently records its active review owner there. Before any additional person reviews or merges high-impact changes, the owner must grant the appropriate repository access and add that person’s confirmed GitHub account to `CODEOWNERS`; never add an unconfirmed handle as a nominal fallback.

| Situation | Required action |
|---|---|
| Planned handover or maintainer absence | The active owner identifies a confirmed successor or co-maintainer, grants the required access, updates `CODEOWNERS`, and records the change in an issue or pull request. |
| Urgent security or content-safety matter | Follow `SECURITY.md`. The active owner or a confirmed security reviewer triages confidential information before public discussion. |
| No confirmed secondary maintainer | High-impact changes remain owner-reviewed; do not claim redundant review coverage. Maintain the repository, catalog, and review records so a confirmed successor can assume stewardship without hidden process. |
| New review authority | Record the scope of authority, expected review duties, and handover date in the accompanying issue or pull request. |

## How to Record a Review

Open an issue or pull request using the existing templates. State the date, reviewer, resources checked, evidence consulted, action taken, validation commands run, and any follow-up due date. For security or content-safety concerns, follow [SECURITY.md](SECURITY.md) and do not disclose sensitive information in a public issue. For catalog changes, also follow the [Catalog Maintenance Guide](docs/CATALOG_MAINTENANCE.md).

## Link-Triage Procedure

The scheduled workflow treats unavailable links, including `429` rate limiting, as failures rather than silently accepting them. A maintainer should inspect the source, retry later when the cause is transient, and create an issue or pull request that records the URL, date, observed result, canonical replacement or retention rationale, and next review date. Retain a temporarily unavailable canonical source only when its value and owner remain clear; otherwise replace or retire it under the retirement rules below.

## Retirement Rules

Mark a resource **Archived**, **Historical**, **Experimental**, **Superseded**, or **Review Required** when that condition is supported by the canonical source or cannot be resolved after review. Remove an entry when it lacks a canonical source, makes unrepairable material claims, duplicates a better maintained entry without distinct value, or no longer meets the responsible-use standard.
