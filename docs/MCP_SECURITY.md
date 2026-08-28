# MCP Security Guide

The Model Context Protocol (MCP) connects AI applications to resources, prompts, and tools. It can make security workflows more useful, but it can also create a broad authority path from natural-language input to data access or execution. This guide explains how to assess that risk before enabling a server.

> **Security posture:** an MCP server is not merely a convenience integration. It is an application component with an identity, dependencies, permissions, data flows, logs, and potentially consequential tools.

## 1. What MCP Adds to the Attack Surface

The MCP specification identifies hosts, clients, and servers. Servers may expose resources, prompts, and tools; clients can also expose capabilities such as sampling, roots, and elicitation. The specification stresses explicit consent, data privacy, user control, and caution around tool descriptions from untrusted servers.[1]

| Component | Security question | Practical implication |
|---|---|---|
| Host | Does the host present tool effects and approvals clearly? | Users need understandable control over sensitive data and actions. |
| Client | Does it restrict where it connects and what metadata it follows? | Clients can become a path to SSRF, credential exposure, or untrusted discovery. |
| Server | Which resources, prompts, and tools are exposed? | Every exposed capability must have an owner, purpose, permission model, and log. |
| Tool | Is it read-only, write-capable, or execution-capable? | Side effects determine approval and isolation requirements. |
| Resource | Is data classified and access-controlled? | Retrieval can expose sensitive context or inject untrusted instructions. |
| Prompt | Is the source trusted and its effect understood? | A prompt is executable influence over a model’s behavior, not harmless documentation. |

## 2. The Minimum Review Before Enabling a Server

Do not enable a server based solely on a directory listing, a package name, or a familiar underlying tool. Perform a lightweight but explicit review.

| Review area | Questions to answer | Evidence to retain |
|---|---|---|
| Provenance | Who maintains it? Is the source canonical? Are releases, commits, and dependencies visible? | Repository URL, maintainer, license, version, artifact hash where applicable. |
| Purpose | What approved workflow does it serve? Can a less-privileged integration meet the same need? | Use case, owner, data classification, approved environment. |
| Capability inventory | Which resources, prompts, and tools does it expose? | Machine-readable tool list, schemas, descriptions, effects. |
| Permissions | What identity, scopes, files, ports, API keys, and cloud permissions does it need? | Permission register and least-privilege design. |
| Data flow | What enters, leaves, and is logged by the server? | Data-flow diagram and redaction/retention rules. |
| Isolation | Is it local, remote, containerized, sandboxed, or network-restricted? | Deployment design, mounts, egress rules, resource limits. |
| Authentication | How are users and clients authenticated and authorized? | Identity flow, token audience, scope mapping, session policy. |
| Observability | Can investigators reconstruct calls, inputs, approvals, results, and errors? | Audit schema, log destination, alerting, retention. |
| Lifecycle | Who patches it and how are deprecations handled? | Update owner, review date, vulnerability-monitoring plan. |
| Protocol version | Which MCP version, transport, authentication flow, and deprecated features are in use? | Pinned specification/SDK version, migration plan, interoperability tests, and compatibility owners. |

## 3. Protocol Version and Migration Review

MCP implementations evolve. Treat a protocol upgrade as a security-relevant change: review the exact specification and SDK version, compare authentication and interaction changes, verify the effect on proxies and gateways, and rerun integration tests before rollout. The 2026-07-28 specification introduced a new lifecycle for active/deprecated/removed features and changed core interaction patterns; deployment guidance must therefore be version-qualified rather than copied between releases.[4]

| Review item | Evidence of completion |
|---|---|
| Exact protocol and SDK version | Version pin, release notes, and component inventory. |
| Transport behavior | Test plan covering local and remote transport, reconnect/error paths, and any state or session assumption. |
| Authorization compatibility | Client registration path, redirect/issuer/audience validation, resource binding, scope changes, and a rollback path. |
| Gateway and observability behavior | Updated routing, policy, rate-limit, logs, and alert rules for the actual request/metadata structure. |
| Deprecated capabilities | Migration owner, deadline, compatibility test, and documented removal decision. |

## 4. Permission Tiers

Classifying MCP tools by their effect makes approval design concrete. A server can expose tools across multiple tiers, but the client should not grant blanket approval.

| Tier | Tool effect | Examples of security control |
|---|---|---|
| 0 — Static knowledge | Returns public, fixed, non-sensitive documentation | Source verification and citation display. |
| 1 — Read-only scoped data | Reads an approved repository, dataset, CTI source, or telemetry view | Service identity, row/field filtering, redacted logs. |
| 2 — Query with external impact | Performs an approved query against an external service | Domain allowlist, rate limits, egress proxy, action log. |
| 3 — Controlled write | Creates a draft report, a ticket, or a non-production change | Explicit preview, human confirmation, rollback, audit record. |
| 4 — Execution or privileged change | Runs commands, scans, changes configuration, deploys, or modifies access | Isolated environment, narrow role, time limit, dual approval, replayable evidence. |

Default to the lowest tier. A security agent should not inherit an administrator’s full access merely because a task occasionally needs a privileged query.

## 5. Core MCP Risks and Controls

OWASP’s MCP Top 10 is currently a beta project and should be treated as evolving guidance. It highlights token/secret exposure, scope creep, tool poisoning, dependency compromise, command execution, intent-flow subversion, inadequate authentication, weak telemetry, shadow servers, and context over-sharing.[2]

| Risk | What can go wrong | Control direction |
|---|---|---|
| Token and secret exposure | Credentials appear in configuration, prompts, tool results, memory, or logs | Secret manager, short-lived scoped tokens, redaction, scanning, audience validation. |
| Scope creep | A server or agent accumulates permissions beyond its original task | Time-bounded scopes, periodic review, permission inventory, separate service identities. |
| Tool poisoning | Tool definitions or outputs manipulate the agent’s behavior | Trust provenance, signed releases, treat output as untrusted data, approval gates. |
| Supply-chain compromise | A dependency or package changes behavior | Pin/verify artifacts, SBOM, dependency monitoring, build isolation, maintainer review. |
| Command execution | Model-controlled arguments create unsafe execution paths | Strong schemas, allowlists, sandboxing, no implicit shell, human approval. |
| Intent subversion | Retrieved content steers an agent away from the user’s goal | Instruction/data separation, context labeling, policy checks, critical-action confirmation. |
| Weak authentication | A client or user receives access that cannot be verified or constrained | Strong identity, authorization checks at every tool, no possession-only state. |
| Missing telemetry | Incidents cannot be reconstructed | Immutable, privacy-aware logs of calls, approvals, errors, and results. |
| Shadow servers | Unsanctioned integrations bypass review and governance | Server inventory, discovery controls, allowlists, developer policy, periodic scans. |
| Context over-sharing | Data from one user, task, or source reaches another | Tenant isolation, memory scoping, explicit retrieval policy, data minimization. |

## 6. Authorization and Network Safety

The MCP security guidance calls out several concrete design risks. A proxy must obtain consent per client and validate redirect URIs exactly to avoid confused-deputy attacks. Servers must not accept tokens that were not issued for them. Clients should account for SSRF when resolving authorization metadata and redirects, including private addresses, cloud metadata paths, and DNS rebinding.[3]

| Area | Minimum expectation |
|---|---|
| Consent | The approving user can identify the client, the server, the scopes, the action, and the target data. |
| Redirects | Exact redirect-URI matching, one-time state, short expiry, CSRF protection, and visible consent. |
| Tokens | Validate issuer, signature, expiry, audience, and scopes; do not forward client tokens blindly downstream. |
| Discovery | Do not follow arbitrary metadata URLs without network and URL controls. |
| Egress | Require HTTPS in production, validate every redirect hop, block private/reserved ranges where appropriate, and use egress controls. |
| State | Bind server-side state handles to the authenticated principal; unpredictable IDs are not authorization. |
| Local servers | Verify source, run with least privilege, restrict filesystem/network, and do not assume localhost is automatically trusted. |

## 7. Safe Deployment Patterns

The following patterns increase safety without sacrificing the usefulness of MCP for security work.

| Pattern | Use when | Benefit |
|---|---|---|
| Read-only analysis server | Reviewing code, logs, CTI, or artifacts | Reduces side effects and simplifies authorization. |
| Isolated lab integration | Evaluating security tools or untrusted samples | Limits filesystem, network, credentials, time, and resource exposure. |
| Approval-gated executor | A workflow occasionally needs a write or command | Preserves automation for preparation while retaining human control over impact. |
| Split identities | Discovery, analysis, and remediation have different duties | Prevents one compromised path from receiving every privilege. |
| Brokered egress | Tools need controlled access to external APIs | Enforces destinations, logging, policy, and rate limits centrally. |
| Ephemeral credentials | High-risk integrations or temporary investigations | Limits the duration and reuse value of exposure. |
| Independent validator | An agent proposes a result that affects risk or remediation | Reduces self-confirming model behavior and false positives. |

## 8. Evaluating Security-Workflow MCP Servers

Security MCP servers deserve additional care because they may invoke scanners, parse untrusted samples, access cloud APIs, read repositories, or transmit data to intelligence providers. The [MCP Security Hub](https://github.com/FuzzingLabs/mcp-security-hub) is a useful example of a collection that documents container hardening and CI checks, but every included server still needs its own permission and dependency review.[5]

Use a versioned verification baseline as well as a threat checklist. OWASP AISVS provides testable controls spanning agentic security and MCP security; select a level appropriate to the system and record the exact requirement version used as evidence.[6] For adversarial evaluation of an MCP-connected agent, [MCP Security Bench](https://github.com/dongsenzhang/MSB) offers a research harness that measures both task performance and resilience across the tool-use lifecycle. Treat its scenarios as controlled evaluation material, not production testing instructions.[7]

| Review question | Good answer |
|---|---|
| Does the server offer an authorized, bounded workflow? | The user can define environment, scope, and allowed activity before use. |
| Are tool parameters narrow and structured? | Schemas make unsafe values or ambiguous effects difficult to pass. |
| Is a scan or external call visible before it happens? | The client shows the target, effect, and approval state. |
| Can the server reach production networks by default? | No; egress is restricted and lab/prod contexts are separated. |
| Are volume mounts and credentials minimized? | Only necessary read-only data and short-lived scoped tokens are exposed. |
| Is there a maintained security process? | Releases, vulnerability reporting, dependencies, tests, and ownership are visible. |
| Can results be independently verified? | Outputs contain raw evidence, timestamps, tool versions, and a review path. |

## 9. Operational Checklist

Use this checklist whenever an MCP server is proposed for a security workflow.

| Check | Status |
|---|---|
| Canonical source, license, maintainer, version, and dependencies are recorded. |  |
| Approved purpose, data classification, environment, and owner are defined. |  |
| Resources, prompts, and tools are inventoried and assigned a permission tier. |  |
| The server has only the minimum identity, scope, filesystem, network, and secret access. |  |
| External content and tool output are treated as untrusted data. |  |
| User approvals are required for material writes, execution, or external effects. |  |
| Token audience, scopes, redirect handling, state binding, and session handling are reviewed. |  |
| Egress, SSRF protections, sandboxing, resource limits, and logs are tested. |  |
| The update, incident, and deprecation owner is known. |  |
| The deployed protocol and SDK versions, transports, and lifecycle/deprecation choices are documented. |  |
| The integration has versioned verification evidence appropriate to its assurance level. |  |
| A re-evaluation date is set before the integration is enabled. |  |

## References

[1]: https://modelcontextprotocol.io/specification/2026-07-28 "MCP Specification"
[2]: https://owasp.org/www-project-mcp-top-10/ "OWASP MCP Top 10"
[3]: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices "MCP Security Best Practices"
[4]: https://blog.cloudflare.com/mcp-v2/ "The next generation of MCP"
[5]: https://github.com/FuzzingLabs/mcp-security-hub "MCP Security Hub"
[6]: https://github.com/OWASP/AISVS "OWASP AI Security Verification Standard"
[7]: https://proceedings.iclr.cc/paper_files/paper/2026/hash/5fc47800ee5b30b8777fdd30abcaaf3b-Abstract-Conference.html "MCP Security Bench"
