# AI Security Guide

This guide provides a practical, lifecycle-based approach to securing applications that use LLMs, RAG, AI agents, or model-connected tools. It is intended for engineers and security teams who need a repeatable method, not a one-off prompt test.

> **Core idea:** secure the system around the model as seriously as the model itself. Prompts, retrieved data, tool outputs, identities, memory, logs, network paths, and human approvals are all part of the attack surface.

## 1. Start with a System Boundary

Before choosing a scanner or writing a test, document the application’s assets, data flows, identities, trust boundaries, and possible effects. NIST’s AI RMF frames risk work around governing, mapping, measuring, and managing risk, while NCSC guidance organizes work through design, development, deployment, and operation.[1] [2]

| Question | Evidence to capture | Why it matters |
|---|---|---|
| What is the intended task? | User journeys, system purpose, acceptable outputs | Defines what “correct” and “safe” mean. |
| What data enters the system? | User input, documents, connectors, APIs, files, prompts | Reveals untrusted content and confidentiality risks. |
| What can the system access? | Data stores, secrets, filesystems, services, tool permissions | Establishes the blast radius of a failure. |
| What can the system change? | Write paths, tickets, code, cloud resources, external messages | Identifies actions that require explicit approval. |
| Which identities are involved? | User, service account, agent, tool, and vendor identities | Prevents confused-deputy and over-privilege problems. |
| What evidence is retained? | Logs, tool calls, prompts, approvals, model/version, results | Enables investigation, reproducibility, and accountability. |

## 2. Threat Modeling for LLM, RAG, and Agentic Systems

Threat models should identify assets, attackers, preconditions, abuse paths, controls, and residual risk. MITRE ATLAS provides an AI-specific knowledge base of tactics, techniques, mitigations, and case studies; OWASP maintains active resources for generative AI and agentic systems.[3] [4]

| Surface | Typical risk questions | Control direction |
|---|---|---|
| Prompt and instruction handling | Can untrusted input override trusted intent or leak hidden context? | Separate instructions from data; constrain tool execution; test direct and indirect injection. |
| Retrieval and RAG | Can documents poison responses, expose sensitive content, or create misleading citations? | Content provenance, access controls, segmentation, source display, retrieval tests. |
| Tools and APIs | Can model output cause harmful API calls, command execution, or data changes? | Least privilege, structured parameters, allowlists, approval gates, sandboxing. |
| Agent memory | Can a malicious or stale observation persist and influence later tasks? | Scoped memory, provenance, expiry, review, poisoning detection. |
| Model and data supply chain | Are model weights, adapters, datasets, packages, prompts, and agent skills authentic and documented? | Provenance, signing, dependency review, license checks, scanning, and release review. |
| User and service identity | Can one user or agent act with another principal’s permissions? | Strong authorization, audience validation, service separation, short-lived credentials. |
| Observability | Can a team reconstruct what the application did and why? | Redacted audit trails, retention policy, tamper resistance, alerting. |

## 3. Secure by Design

Security requirements must be explicit before implementation. A useful design review should specify which actions are safe to automate, which require confirmation, which are prohibited, and how the application fails safely.

| Design principle | Practical application |
|---|---|
| Minimize authority | Give each component only the data and tool scope it needs for one task. Prefer read-only access. |
| Put authority below the agent | Treat prompts, models, and orchestration as behavioral guidance. Enforce identity, credential release, egress, policy, and auditing in a component the agent cannot override.[6] [7] |
| Separate duties | Do not let the same component generate a finding, validate it, and authorize remediation. |
| Treat external text as data | Documents, web pages, tickets, tool output, and retrieved content may contain adversarial instructions. |
| Make consequences visible | Show the user intended tool effects, data destinations, and requested permissions before approval. |
| Build for containment | Execute untrusted code and high-risk tools in isolated environments with constrained filesystems, networks, time, and resources. |
| Preserve human ownership | Require explicit human approval for external communications, destructive changes, privilege changes, or high-impact remediation. |
| Design for failure | Timeouts, parser errors, tool failures, and uncertain model outputs must fail closed when the consequence is material. |

## 4. Secure Development

Development controls should be testable and repeatable. Secure coding guidance for AI integrations can complement ordinary AppSec controls, while model and dataset cards improve documentation of provenance, intended use, and limitations.[5]

| Control | What good evidence looks like |
|---|---|
| Input and output handling | Schemas, validation, encoding, context separation, output allowlists, and tests for unsafe downstream use. |
| Tool contracts | Narrow JSON schemas, validated arguments, explicit effects, error handling, and no implicit shell construction. |
| Secret management | No credentials in prompts, source code, logs, datasets, or agent memory; scoped short-lived service credentials. |
| Dependency management | Locked versions, provenance, vulnerability scanning, license review, and update ownership. |
| Test corpus | Benign, adversarial, malformed, privacy-sensitive, and regression cases with expected outcomes. |
| Evaluation automation | Repeatable checks in CI that distinguish expected refusal, correct completion, safe escalation, and malformed output. |
| Documentation | System card, data-flow diagram, permissions register, model/dataset cards, and known limitations. |
| Verification standard | Map controls and test evidence to a versioned assurance target such as OWASP AISVS rather than relying on a generic claim of “secure AI.”[8] |

## 5. Secure Deployment

Deployment converts design risk into operational risk. The deployment review should confirm that a test configuration cannot accidentally become a production integration with broad access.

| Area | Baseline control |
|---|---|
| Environment separation | Separate development, evaluation, staging, and production identities, data, networks, and logs. |
| Network egress | Restrict destinations, inspect proxy logs, and prevent unexpected connections to private or metadata endpoints. |
| Data governance | Classify input data; redact or block secrets and sensitive records before third-party model calls. |
| Model endpoint governance | Pin approved model versions where possible; document provider terms, retention settings, and regional controls. |
| Tool execution | Use sandboxing, read-only mounts, resource limits, and explicit approvals for consequential actions. |
| Release readiness | Security tests, rollback plan, abuse monitoring, incident ownership, and documented residual risk. |

## 6. Secure Operation and Maintenance

AI risk changes after launch because models, providers, data sources, prompts, connectors, and attacker techniques change. Operation therefore needs an active review cycle.

| Operational practice | Purpose |
|---|---|
| Structured audit trail | Capture request correlation, model/version, retrieved sources, tool requests, approvals, results, and errors without storing unnecessary sensitive content. |
| Red-team regression testing | Re-run safety and security tests after model, prompt, retrieval, tool, dependency, or policy changes. |
| Access review | Periodically remove unused tools, scopes, service accounts, memory stores, and connectors. |
| Incident playbook | Define triage, containment, evidence preservation, disclosure, communication, and recovery for AI-specific incidents. |
| Quality review | Track false positives, unsafe completions, unauthorized tool attempts, confidence failures, and user escalations. |
| Update governance | Version prompts, policies, models, tools, datasets, and evaluation datasets; retain change rationale. |

## 7. Testing Strategy

No single tool can certify an AI application. Combine deterministic tests, adversarial probing, human review, and operational monitoring. Tools such as Promptfoo, Garak, PyRIT, RAMPART, and Giskard cover different parts of this landscape; their output still requires local interpretation.[4]

| Test layer | Example objective | Evidence of success |
|---|---|---|
| Unit and contract testing | Verify tool schemas, authorization checks, and output validation | Reproducible passing/failing cases in CI. |
| RAG evaluation | Verify retrieval quality, permission filtering, citations, and resistance to malicious documents | Test set with expected sources and negative controls. |
| Agent evaluation | Verify planning, tool boundaries, approval gates, memory scope, and recovery | Replayable traces and policy-conformant decisions. |
| Adversarial testing | Probe injection, data leakage, tool misuse, unsafe output handling, and resource exhaustion | Findings, severity, remediation owner, and regression test. |
| Human review | Judge operational context, business impact, and unsafe ambiguity | Recorded decision and accepted residual risk. |
| Production monitoring | Detect drift, abnormal tool use, denied actions, and attempted abuse | Alerting and response procedures tested in advance. |
| Skill and extension review | Reassess skills, plugins, MCP manifests, and tool descriptions before installation or update | Provenance review, static analysis, permission inventory, change review, and recorded decision. |

## 8. Practical Review Checklist

A secure AI application should be able to answer “yes” to the following questions before high-impact deployment.

| Review question | Yes/No |
|---|---|
| Is the application’s purpose, owner, data classification, and threat model documented? |  |
| Are untrusted content and trusted system instructions handled as different trust levels? |  |
| Are tools limited to the minimum data, permission, and action scope? |  |
| Are side-effecting actions explicit, visible, reversible where possible, and human-approved? |  |
| Are logs sufficient for investigation while protecting sensitive data? |  |
| Are model, prompt, tool, data, dependency, and policy versions recorded? |  |
| Has the system been evaluated against relevant security and safety failure modes? |  |
| Does a change to provider, model, prompt, RAG source, tool, or policy trigger re-evaluation? |  |
| Is there a documented incident and rollback process? |  |
| Are agent skills, MCP manifests, and other extensions reviewed as privileged dependencies before enablement? |  |
| Do the implemented controls have versioned verification evidence appropriate to the system’s assurance level? |  |

## References

[1]: https://airc.nist.gov/airmf-resources/ "NIST AI RMF"
[2]: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development "NCSC Guidelines for Secure AI System Development"
[3]: https://atlas.mitre.org/ "MITRE ATLAS"
[4]: https://genai.owasp.org/ "OWASP GenAI Security Project"
[5]: https://github.com/semgrep/ai-best-practices "Semgrep AI Best Practices"
[6]: https://developer.nvidia.com/blog/where-security-fits-in-an-ai-agent-stack/ "Where Security Fits in an AI Agent Stack"
[7]: https://www.frontiermodelforum.org/issue-briefs/emerging-security-practices-for-ai-agents/ "Emerging Security Practices for AI Agents"
[8]: https://github.com/OWASP/AISVS "OWASP AI Security Verification Standard"
