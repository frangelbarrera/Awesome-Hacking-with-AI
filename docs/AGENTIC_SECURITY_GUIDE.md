# Agentic Security Guide

Security agents can accelerate research, code review, evidence gathering, detection engineering, validation, and remediation preparation. They also increase risk because they can combine model reasoning with tools, state, permissions, and long-running execution. This guide describes how to design and evaluate agents for **authorized** security workflows.

> **An agent is a system, not a prompt.** Its effective capability is determined by model, scaffold, context, memory, tools, permissions, network access, environment, validators, policy checks, and human approvals.

## 1. Separate Automation from Autonomy

Teams should explicitly choose the level of automation permitted in each workflow. More autonomy is not automatically more valuable. A constrained, auditable process with a clear human decision point is often superior to an unconstrained system that produces unverifiable findings.

| Level | Description | Suitable examples |
|---|---|---|
| Assistive | Generates drafts or suggestions; no tool execution | Triage summaries, threat-model drafts, code-review hypotheses. |
| Guided | Uses narrow read-only tools under direct supervision | Repository exploration, alert enrichment, evidence collection. |
| Bounded workflow | Executes predefined steps in a controlled environment | Running approved checks in a lab, preparing a validation package. |
| Approval-gated | Plans and prepares consequential actions, but a human approves each one | Creating remediation drafts, opening review-ready tickets, controlled test execution. |
| High autonomy | Adapts goals, tools, or scope over long periods | Research only, and only with isolation, strict boundaries, monitoring, and accountable ownership. |

The correct choice depends on impact. Tasks that touch production data, accounts, external systems, code, cloud resources, or communications should require explicit approval and a clear rollback path.

## 2. A Reference Workflow for Authorized Security Work

A credible workflow separates discovery from validation and validation from decision-making. This structure is more reliable than a monolithic agent because each stage can be tested, logged, and improved independently.

| Stage | Objective | Required controls |
|---|---|---|
| Scope and authorization | Establish what may be assessed and how | Written authorization, asset list, time window, allowed actions, owner, stop conditions. |
| Architecture mapping | Understand components, data flows, trust boundaries, and assumptions | Read-only access where possible; versioned architecture notes; no external action. |
| Hypothesis generation | Identify potential weaknesses or coverage gaps | Explain threat model, affected boundary, confidence, and evidence needed. |
| Deterministic analysis | Run approved analyzers, queries, or checks | Pinned tools, structured results, time and resource limits. |
| Targeted validation | Test the hypothesis in a lab or authorized scope | Isolated environment, narrow target list, visible action log, stop conditions. |
| Independent review | Attempt to disprove or reproduce the result | Separate validator identity or model; no ability to self-file findings. |
| Evidence packaging | Produce a reviewable result | Affected version, trace, timestamps, raw evidence, limitation, remediation context. |
| Human decision | Decide disclosure, remediation, escalation, or closure | Security owner approval and documented rationale. |

This pattern is reflected in several public architecture discussions. AWS describes specialized exploration, validators, structured evidence, and the need to verify plausible model outputs.[1] Cloudflare emphasizes stage separation, externalized state, deterministic checks, independent validation, and deduplication.[2]

## 3. Design Principles

| Principle | Practical meaning |
|---|---|
| Scoped authorization | The agent receives an explicit target inventory, activity boundary, budget, and expiration. |
| Least privilege | Separate discovery, analysis, validation, and remediation identities; default to read-only. |
| Structured actions | Tools accept narrow schemas and return structured evidence instead of unconstrained command strings. |
| Observable execution | Record task, plan, requested tool call, approval, response, artifact, error, and policy decision. |
| Independent validation | A validator should try to falsify the result and should not be rewarded for creating new findings. |
| Reproducible evidence | Findings should point to unmodified inputs, exact versions, repeatable tests, and bounded conclusions. |
| State discipline | Persist task state deliberately with provenance and expiration rather than relying on an opaque context window. |
| Authority boundary | Keep identity, policy enforcement, credential release, egress controls, and audit below the agent/harness layer; the agent may propose, but must not grant itself authority.[6] [7] |
| Extension supply chain | Review agent skills, plugins, MCP manifests, and tool definitions as executable dependencies before installation or enablement. |
| Failure containment | Limit retries, time, cost, network, filesystem, concurrency, and external impact. |
| Human ownership | A person owns the target, risk acceptance, remediation decision, and external communication. |

## 4. Agent Roles That Scale Safely

Role specialization is useful when the outputs and authority of each role are clear. Not every project needs every role; start with the smallest set that improves a measurable bottleneck.

| Role | Produces | Must not be allowed to do alone |
|---|---|---|
| Scope controller | Authorized task statement, boundaries, budgets, and stop conditions | Expand target scope or privilege. |
| Reconnaissance/architecture analyst | System map, entry points, data flows, dependency notes | Perform consequential external actions. |
| Research analyst | Cited information, standards, advisories, configuration context | Treat web content as trusted instruction. |
| Hunter | Bounded hypotheses and candidate findings | Grade or self-approve its own findings. |
| Deterministic analyzer | Tool outputs, static-analysis results, schema checks | Convert noisy output into confirmed risk without validation. |
| Validator | Reproduction or disproof evidence | Create new findings from scratch or bypass approval boundaries. |
| Deduplicator | Clusters and root-cause links | Silently discard findings without traceability. |
| Reporter | Structured report and remediation context | Invent evidence or severity. |
| Remediation assistant | Patch or configuration proposal | Apply production changes without review and tests. |

## 5. Making Findings Trustworthy

A model can produce a plausible narrative that is incorrect, incomplete, or generated from a flawed threat model. A finding should therefore be an evidence package, not a paragraph.

| Finding field | Why it is needed |
|---|---|
| Scope and authorization ID | Proves the work was bounded and permitted. |
| Asset and version | Identifies the affected component precisely. |
| Threat model | Explains the attacker, boundary, precondition, and impact. |
| Evidence | Links exact files, logs, test artifacts, raw tool output, or controlled reproduction. |
| Validation outcome | States whether an independent validator reproduced, rejected, or could not assess it. |
| Confidence and limitations | Prevents certainty language unsupported by the evidence. |
| Severity rationale | Connects impact, likelihood, and environment rather than relying on a model guess. |
| Remediation context | Offers a reviewable mitigation, test, and rollout consideration. |
| Disclosure status | Protects unpublished issues and assigns a responsible owner. |

A system should reject a finding that cannot identify a boundary crossed or assumption violated. It should also distinguish “candidate,” “validated,” “duplicate,” “not reproducible,” and “closed” rather than collapsing every model suggestion into an alert.

## 6. Evaluation: Measure the Whole System

It is misleading to call an agent “best” because it solved a few tasks or has high repository visibility. Evaluation must separate model effects from agent scaffolding, account for feedback provided by the environment, and record cost, time, tools, trials, and success definition.

| Evaluation question | What to report |
|---|---|
| Which task? | Code review, vulnerability localization, remediation, CTI, alert investigation, lab challenge, or MCP review. |
| Which target condition? | White-box, gray-box, or black-box; static or dynamic; synthetic or real-world; isolated or networked. |
| Which system version? | Model, agent scaffold, prompt/policy, tools, dependencies, and date. |
| What inputs and help? | Context window, hints, source access, grader feedback, internet access, and human intervention. |
| What metric? | Precision, validated outcomes, patch correctness, subtask success, time, cost, harmful-action attempts, and user effort. |
| How many trials? | Number of attempts, randomness settings, aggregation rule, and failures/timeouts. |
| What limitations? | Leakage/contamination concerns, dataset coverage, target selection, and non-comparable results. |

[CyBench](https://cybench.github.io/) provides task/subtask metrics and calls out a historical answer-leak issue; [CyberGym](https://arxiv.org/abs/2506.02548) evaluates agents on a much larger set of real-world vulnerabilities; the [AI Cyber Model Arena](https://www.wiz.io/blog/introducing-ai-cyber-model-arena-a-real-world-benchmark-for-ai-agents-in-cybersec) explicitly separates agent and model effects in a multi-domain matrix.[3] [4] [5]

[AgentDojo](https://github.com/ethz-spylab/agentdojo) adds a controlled environment for measuring prompt-injection resilience in tool-using agents. It should complement, rather than replace, task-capability evaluation: an agent can be capable on a benchmark and still be unsafe under hostile tool or data conditions. [AISI’s multi-step cyber-range study](https://arxiv.org/html/2603.11214v1) further illustrates why repeated trials, compute budget, scenario design, containment configuration, and evidence of result verification belong in every capability report.[8] [9]

## 7. Labs and Controlled Evaluation

Use controlled environments for education, benchmarking, or experimental validation. A lab is valuable when it has a defined purpose, isolated data and networks, visible scoring, reset/cleanup behavior, and a clear safety boundary.

| Resource | Intended use |
|---|---|
| [NYU CTF Bench](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench) | Dockerized CTF challenges for agent evaluation. |
| [CyBench](https://cybench.github.io/) | Professional CTF tasks with staged evaluation. |
| [CyberGym](https://arxiv.org/abs/2506.02548) | Real-world vulnerability benchmark with research context. |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) | Prompt-injection attack/defense evaluation for tool-using agents. |
| [AgentCyberRange](https://github.com/AgentCyberRange) | Isolated multi-host cyber-range research; report prompt, budget, run count, verification, and containment setting. |
| [Damn Vulnerable MCP Server](https://github.com/harishsg993010/damn-vulnerable-MCP-server) | Intentionally vulnerable MCP environment for learning. |
| [Vulnerable MCP Servers Lab](https://github.com/appsecco/vulnerable-mcp-servers-lab) | Training environment for MCP-security assessment. |
| [Damn Vulnerable LLM Agent](https://github.com/ReversecLabs/damn-vulnerable-llm-agent) | Deliberately vulnerable agent environment for safe learning. |
| [AI Red Teaming Playground Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs) | Training and evaluation materials for AI red teaming. |

## 8. Evaluation Safety and Containment

A benchmark is not a permission boundary. The risk of a security-agent evaluation depends on its capabilities, connectivity, task design, monitoring, and the possibility of effects outside the intended environment. The 2026 UK AI Security Institute incident report is a particularly important safety case: it argues for explicitly justified egress, real-time monitoring, tasks designed to be solvable within their stated scope, and containment that does not rely on the model choosing to remain in bounds.[10]

| Evaluation control | Minimum condition |
|---|---|
| Environment | Disposable, isolated environment with no route to production systems, personal data, or external targets unless separately and explicitly authorized. |
| Network | Default-deny egress; allowlisted destinations only when essential to the stated evaluation. |
| Task | A clear objective, safe solution path, stop conditions, time/cost limits, and no need for interaction with uninvolved people or systems. |
| Monitoring | Live visibility for anomalous tool use, traffic, identity changes, unexpected persistence, or departures from scope. |
| Human control | An accountable operator can pause, revoke credentials, quarantine the environment, and preserve evidence. |
| Post-run review | Inspect traces, artifacts, denied actions, and any unexpected external effect before reuse or publication. |

## 9. Operational Readiness Checklist

| Check | Status |
|---|---|
| The task has written authorization, owner, scope, expiration, budget, and stop conditions. |  |
| Identities, tools, data, and network access are least-privilege and environment-specific. |  |
| The agent cannot silently expand scope, use unapproved tools, or trigger high-impact actions. |  |
| Every consequential tool call is visible, logged, and approval-gated. |  |
| Untrusted data, retrieved content, and tool output are not treated as trustworthy instructions. |  |
| Candidate findings must include a threat model and reproducible evidence. |  |
| A separate validation step can disprove findings and cannot self-file new ones. |  |
| Logs protect secrets and personal data while retaining enough evidence for investigation. |  |
| Benchmark claims include task, setting, version, trials, tools, cost/time, and limitations. |  |
| Disclosure, remediation, rollback, and incident ownership are defined. |  |

## References

[1]: https://aws.amazon.com/blogs/security/inside-aws-security-agent-a-multi-agent-architecture-for-automated-penetration-testing/ "AWS Security Agent Architecture"
[2]: https://blog.cloudflare.com/build-your-own-vulnerability-harness/ "Cloudflare Vulnerability Harness"
[3]: https://cybench.github.io/ "CyBench"
[4]: https://arxiv.org/abs/2506.02548 "CyberGym"
[5]: https://www.wiz.io/blog/introducing-ai-cyber-model-arena-a-real-world-benchmark-for-ai-agents-in-cybersec "Wiz AI Cyber Model Arena"
[6]: https://developer.nvidia.com/blog/where-security-fits-in-an-ai-agent-stack/ "Where Security Fits in an AI Agent Stack"
[7]: https://www.frontiermodelforum.org/issue-briefs/emerging-security-practices-for-ai-agents/ "Emerging Security Practices for AI Agents"
[8]: https://github.com/ethz-spylab/agentdojo "AgentDojo"
[9]: https://arxiv.org/html/2603.11214v1 "Measuring AI Agents’ Progress on Multi-Step Cyber Attack Scenarios"
[10]: https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing "Incident Report: unsanctioned agent behaviour during cyber testing"
