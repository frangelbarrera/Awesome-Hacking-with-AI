# Curation Policy

This repository is a curated reference, not an unfiltered directory. The purpose of curation is to preserve breadth while helping readers distinguish primary guidance from commentary, active projects from archived artifacts, evaluation from marketing, and safe authorized workflows from material that would enable misuse.

## 1. Inclusion Standard

A resource may be included when it makes a clear contribution to AI for security, security for AI systems, authorized security research, or security education. The entry must give readers enough context to evaluate it responsibly.

| Requirement | Minimum evidence |
|---|---|
| Relevance | Clear connection to an existing repository area and an articulated user need. |
| Canonical source | Official website, upstream repository, DOI, publisher, or author-controlled project page. |
| Resource type | Guidance, standard, taxonomy, paper, dataset, model, benchmark, lab, tool, framework, agent, MCP server, or case study. |
| Neutral description | Concise description of function and scope, without unverified superlatives. |
| Ownership | Maintainer, author, organization, or publication venue when available. |
| License or terms | Software/data/model license or access terms, when applicable. |
| Status | Active, experimental, archived, historical, or unknown, with a verification date. |
| Safety context | Permission model, intended authorized use, risks, and meaningful safeguards for tools or integrations. |
| Evidence | Source for performance, compatibility, security controls, or other material claims. |

## 2. Entry Metadata

Use the following metadata as a review checklist. A short README row does not need to display every field, but maintainers should be able to recover each field from the proposal or linked documentation.

| Field | Applies to | Purpose |
|---|---|---|
| Name and canonical URL | All entries | Prevents duplicate, stale, or unofficial references. |
| Type and category | All entries | Keeps tools, benchmarks, papers, and datasets discoverable without conflation. |
| Neutral summary | All entries | Explains use without turning the list into advertising. |
| Maintainer and license | Software, models, data, MCP | Supports provenance and reuse decisions. |
| Status and verification date | All entries | Makes maintenance state explicit. |
| Evidence link | Claims and benchmarks | Connects claims to methods, data, and limitations. |
| Environment and dependencies | Tools, agents, MCP | Makes operational cost and risk visible. |
| Permissions and effects | Agents, tools, MCP | Distinguishes read, write, execution, network, and data access. |
| Controls and limitations | Agents, models, MCP | Records isolation, approvals, logs, privacy, and known gaps. |
| Intended use | All entries | Clarifies whether the resource is research, lab, defensive, or authorized assessment material. |

## 3. Evidence and Benchmark Claims

A tool may be useful without a benchmark, but it may not claim superiority without relevant evidence. Do not write “best,” “first,” “fully autonomous,” “production-ready,” a success rate, a cost reduction, or a coverage statement unless the canonical source and conditions are available.

| Claim type | Required context |
|---|---|
| Benchmark score | Benchmark name/version, task, model, agent/scaffold, tools, environment, trial count, metric, date, and source. |
| Security control | Design or documentation showing scope, permission, isolation, logging, and limitations. |
| Maintenance | Current release or activity signal, owner, and verification date. |
| Compatibility | Version, transport, runtime, platform, and integration constraints. |
| Vulnerability or incident | Primary advisory, CVE, responsible disclosure, or reputable research source. |

If the evidence comes from a vendor or project maintainer, identify it as a project or case-study claim. Do not present it as independent verification.

## 4. Dual-Use Safety Review

The repository supports legitimate security learning and authorized work, but it is not a venue for lowering the barrier to abuse. A contribution should improve prevention, detection, validation, remediation, or safe research.

| Usually in scope | Out of scope |
|---|---|
| Secure design, threat modeling, testing methodology, detection, response, code review, vulnerability validation in labs, remediation, disclosure, benchmarks, and intentionally vulnerable learning environments | Instructions designed to gain unauthorized access, evade defenses, deploy malware, operate botnets/C2, exfiltrate data, impersonate people, or target third-party systems |
| Descriptions of threats with mitigation and cited context | Operational payloads, bypass playbooks, web shells, target profiling for manipulation, or evasion-oriented prompts |
| Tools with documented authorized uses, permissions, and safeguards | Unscoped mass scanning, destructive automation, credential theft, persistence, or tooling that hides actions from the operator |

Entries with meaningful execution, write, network, or sensitive-data capabilities require closer review. They should explain scope, authorization, isolation, approval, logging, and responsible disclosure. Any row marked unverified, experimental, historical, archived, or review required must complete the [Pre-Adoption Review](PRE_ADOPTION_REVIEW.md) before operational use.

## 5. MCP-Specific Review

MCP servers deserve a dedicated review because natural-language reasoning can trigger tool calls and context can affect intent. Follow the official MCP security guidance and OWASP resources when evaluating an entry.[1] [2] [3]

| MCP review item | Expected evidence |
|---|---|
| Server origin | Canonical repository, release artifacts, maintainer, license, and dependency provenance. |
| Transport and identity | Local/remote transport, authentication, authorization, token audience, and scope. |
| Tools and effects | Tool list and clear classification as knowledge, read, external query, write, or execution. |
| Data exposure | Inputs, outputs, logs, retention, third-party destinations, and secret handling. |
| Isolation | Filesystem mounts, network egress, container/user privileges, resource limits, and sandbox boundaries. |
| Approval | User visibility and confirmation for material writes, execution, or external effects. |
| Observability | Audit trail, correlation, errors, alerts, and incident response ownership. |
| Lifecycle | Update cadence, vulnerability process, deprecation plan, and next review date. |

## 6. Archived and Historical Resources

Archived projects can be essential to understanding a research field, but they must never be presented as current production dependencies. Mark an entry as **Archived**, **Historical**, or **Experimental** when appropriate, state why it remains useful, and link readers toward maintained successors where one is documented.

## 7. Review and Maintenance Cadence

| Cadence | Activity |
|---|---|
| Continuous | Review new issues and pull requests against this policy. |
| Weekly | Check external links and triage failures. HTTP 429 is treated as a tentative reachable response by automation, but a recurring 429 or redirect must be manually rechecked and recorded before an entry is considered healthy. |
| Monthly | Revisit high-risk, rapidly moving, or top-level project entries for status and canonical URL changes. |
| Quarterly | Update standards, taxonomies, model families, benchmark links, and MCP guidance. |
| Semiannual | Audit the full collection for stale claims, duplicate entries, dual-use drift, and missing metadata. |

## 8. Rejection and Deprecation

A contribution may be rejected when it lacks canonical sourcing, duplicates an existing entry, does not add context, makes unsupported claims, has no meaningful connection to the repository scope, or fails the dual-use review. Existing entries may be removed or marked historical when they become unmaintained, lose their canonical source, materially change purpose, or no longer meet the safety standard.

Constructive rejection is part of keeping the collection useful. Maintainers should state which missing field, evidence gap, safety issue, or category mismatch needs correction.

## References

[1]: https://modelcontextprotocol.io/specification/2025-06-18 "MCP Specification"
[2]: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices "MCP Security Best Practices"
[3]: https://owasp.org/www-project-mcp-top-10/ "OWASP MCP Top 10"
