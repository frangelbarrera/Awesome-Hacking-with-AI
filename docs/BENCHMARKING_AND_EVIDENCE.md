# Benchmarking and Evidence Guide

This guide explains how to evaluate AI systems used in security work without confusing a compelling demonstration, a benchmark score, and an operationally reliable capability. It applies to code-review assistants, security agents, model adaptations, RAG systems, MCP-connected agents, and automated remediation workflows.

> **Core principle:** report what was measured, under what conditions, and what was not measured. A benchmark score is evidence about one configured system in one setting; it is not a general guarantee of performance, safety, or authorization.

## 1. Start with an Evaluation Claim

Every evaluation begins with a narrow claim. “The best security agent” is not a testable claim. “This specified agent configuration identifies affected files in a versioned vulnerability-localization benchmark under a stated time and tool budget” is testable.

| Weak claim | Testable replacement | Why the replacement is stronger |
|---|---|---|
| The model is secure. | The configured system resisted the stated test suite, with the recorded false-positive and task-completion outcomes. | It identifies the system and the tests rather than asserting a universal property. |
| The agent can pentest. | The agent completed specified tasks in an isolated benchmark with an explicit target, scope, budget, and verifier. | It separates controlled evaluation from permission to assess real systems. |
| Fine-tuning improved the model. | The adaptation improved a named task metric relative to stated baselines while retained safety tests and held-out tasks showed the recorded outcomes. | It prevents task gains from obscuring regression or overfitting. |
| Our MCP integration is safe. | The versioned integration met selected controls, passed defined authorization and adverse-input tests, and retained audit evidence. | It connects security to mechanisms and evidence. |

## 2. Create an Evaluation Card Before Running

A short evaluation card forces a team to document decisions that otherwise become invisible after a result is produced. Store the card with the experiment configuration, raw or privacy-preserving trace references, and analysis.

| Field | Record |
|---|---|
| Objective | The precise capability, reliability, safety, or security property under test. |
| System under test | Model identifier, provider or artifact digest, agent/harness version, prompt/policy version, tools, MCP servers, and dependencies. |
| Environment | Benchmark or lab version, target type, network boundary, input data classification, isolation controls, and reset procedure. |
| Access and assistance | Source access, hints, tool availability, internet/egress setting, human intervention, feedback channels, and prior task exposure. |
| Budget | Maximum time, turns, tool calls, tokens, cost, retries, concurrency, and stopping conditions. |
| Metrics | Success definition, security/resilience measure, precision/recall or false-positive measure where relevant, cost, latency, and failure classes. |
| Trials | Sample count, seeds, temperature/randomness, aggregation rule, excluded runs, and timeout handling. |
| Safety controls | Scope, authorization, egress policy, credentials, monitoring, kill switch, human approval, and post-run review. |
| Limitations | Contamination, target-selection, evaluator-model, benchmark-age, generalization, and measurement limitations. |
| Reproducibility | Config digest, code revision, dataset version, artifact location, evaluator/validator, and review date. |

## 3. Measure Capability, Safety, and Operations Separately

An agent can complete a task while violating a policy. A system can refuse unsafe requests while failing most useful tasks. An evaluation should make these dimensions visible instead of collapsing them into one headline score.

| Dimension | Example questions | Suitable evidence |
|---|---|---|
| Task capability | Did the system identify the affected component, complete the investigation, or produce a correct patch? | Ground-truth comparison, independent validator, task-level outcomes. |
| Security resilience | Did hostile or untrusted content alter tool use, authorization, retrieval, memory, or output behavior? | Controlled adversarial suite, policy-decision traces, safe-failure rate. |
| Precision and calibration | Are alerts and stated confidence aligned with independently confirmed results? | Precision, recall, false positives, duplicates, confidence calibration, rejected findings. |
| Operational reliability | Does the system recover safely from tool failure, ambiguity, rate limits, or malformed input? | Failure-injection tests, timeout/retry records, recovery and escalation evidence. |
| Containment | Could a failed or compromised system exceed its intended authority? | Network policy, identity scope, sandbox evidence, denied-action logs, revocation test. |
| Human workload | Does automation reduce verified work or merely move it to reviewers? | Analyst time, validation burden, escalation quality, override rate. |

## 4. Compare Results Only When Configurations Are Comparable

Comparing scores requires more than comparing a model name. Systems can differ in access, tools, hints, evaluator feedback, number of attempts, budgets, and task versions. When conditions differ, present results side by side with an explicit non-comparability note.

| Comparison factor | Must be disclosed | Common interpretation error |
|---|---|---|
| Target condition | White-box/gray-box/black-box, static/dynamic, synthetic/real-world, local/networked. | Treating source access or hidden hints as an intrinsic model advantage. |
| Agent scaffold | Planner, memory, tool policy, retrieval, validators, retries, and orchestration. | Attributing harness improvements solely to a model. |
| Tooling | Tool versions, permissions, network access, shells, scanners, databases, and MCP servers. | Ignoring that tool choice changes both capability and risk. |
| Budget | Attempts, tokens, time, cost, tool-call limit, context compaction, and concurrency. | Comparing a one-attempt score to a high-budget best-of-many result. |
| Feedback | Test output, grading signals, prompts, human assistance, retries, and retry hints. | Mistaking iterative evaluator feedback for unguided completion. |
| Benchmark integrity | Version, contamination controls, answer exposure, data split, and known leakage. | Treating a memorized or leaked task as evidence of general reasoning. |
| Verification | Ground truth, independent review, patch tests, or self-report. | Counting a plausible narrative or self-asserted finding as success. |

## 5. Use a Minimum Result Table

A published result table should be sufficient for a reader to understand the decision context without searching through issue comments or prompts. The following format is intentionally neutral and applies to both positive and negative results.

| System | Task and version | Environment and access | Trials / budget | Capability result | Security / safety result | Validation method | Key limitations |
|---|---|---|---|---|---|---|---|
| `system-id@revision` | Benchmark, split, target condition | Tools, network, permissions, assistance | `n`, time/tokens/cost, aggregation | Metric with uncertainty where possible | Relevant attack-resistance and false-positive metric | Ground truth / independent reviewer / replay | Scope, contamination, selection, and generalization limits |

If a row lacks an important field, mark it **not measured** rather than implying a favorable result. A security benchmark and an ability benchmark answer different questions; neither should be used as a proxy for the other.

## 6. Evaluate Model Adaptation as a Change-Controlled Release

Fine-tuning, continued pretraining, retrieval changes, adapter updates, and distillation can alter both task behavior and safety behavior. Treat each adaptation as a release candidate with a baseline and an explicit retained-safety test set.

| Release gate | Evidence needed |
|---|---|
| Data governance | Data card, source rights, license, provenance, filtering record, sensitive-content handling, and retention/deletion decision. |
| Baseline | Base model/artifact identifier, unmodified baseline scores, baseline safety outcomes, and inference settings. |
| Adaptation record | Training method, data version, hyperparameters, compute range, adapter/weight digest, and owners. |
| Utility evaluation | Held-out task results compared to relevant baselines, with task-specific error analysis. |
| Safety evaluation | Retained safety and misuse-resistance tests before and after adaptation, with regression analysis. |
| Security evaluation | Prompt/retrieval/tool boundary tests, data-leakage checks, supply-chain review, and deployment isolation test. |
| Release decision | Approval owner, intended use, known limitations, rollback path, monitoring, and re-evaluation trigger. |

Research on cybersecurity-specialized model adaptation reports that task-specific gains can coexist with safety-resilience regressions in the evaluated settings. This is a reason to test both dimensions for the exact model, data, and deployment—not a claim that every adaptation has the same outcome.[1] [2]

## 7. Evaluate MCP-Connected Agents Across the Whole Tool-Use Loop

MCP integrations add a sequence of security-relevant decisions: discovery, server selection, tool description interpretation, authorization, argument generation, tool invocation, response handling, and memory or downstream use. Evaluate the entire loop rather than only a server’s direct output.

| Stage | Example property to test | Evidence |
|---|---|---|
| Discovery and selection | The client does not trust a directory listing or ambiguous server identity without review. | Allowlist decision, canonical-source record, version/provenance check. |
| Tool inventory | Every resource, prompt, and tool has an owner, effect tier, schema, and data classification. | Machine-readable inventory and reviewed permission register. |
| Authorization | Tokens, audience, scope, consent, and redirect behavior are valid for the intended server and action. | Test cases, policy logs, negative-path outcomes, and versioned configuration. |
| Invocation | Arguments remain within narrow schemas and approvals are enforced for material effects. | Requested-versus-executed action records, denied calls, and approval trace. |
| Response handling | Tool output and retrieved content remain untrusted data rather than executable instructions. | Controlled hostile-output tests and policy-conformant traces. |
| Lifecycle | Protocol/SDK updates and deprecated features do not silently change security properties. | Migration review, compatibility tests, version pin, and rollback evidence. |

MCP Security Bench is a research example of evaluating MCP-specific resilience across planning, invocation, and response handling. Its results should be read as configuration-specific research evidence and reproduced only in controlled environments.[3]

## 8. Keep Cyber Evaluations Contained

Security capability evaluation must not create an unbounded operational path. Purpose-built cyber ranges, benchmarks, CTFs, and intentionally vulnerable laboratories support measurement while providing isolation, reset behavior, and defined objectives. A benchmark does not eliminate risk: network connectivity, identity, task framing, monitoring, and external side effects still need explicit controls.

| Control | Minimum requirement |
|---|---|
| Authorization and purpose | Defined research/education/defense objective, accountable owner, approved targets, and clear stop conditions. |
| Egress | Default-deny connectivity, with only explicitly justified destinations and protocols allowed. |
| Identity and data | Disposable accounts and data; no production secrets, customer data, or standing privileged credentials. |
| Environment | Isolated and resettable lab/range, resource quotas, read-only or disposable mounts, and no implicit route to production. |
| Monitoring | Real-time visibility for unexpected tool use, external traffic, identity changes, persistence attempts, and policy violations. |
| Response | Immediate pause, credential revocation, quarantine, evidence preservation, and post-run review procedures. |

The UK AI Security Institute’s 2026 incident report provides an instructive safety case: it emphasizes that egress requires active justification, monitoring should be designed for the evaluation, tasks need a bounded feasible route, and containment should not depend on a model voluntarily staying in scope.[4]

## 9. Reporting Template

Use the following outline for a benchmark report, experiment note, or contributor submission. It is concise enough for repository curation but complete enough to distinguish evidence from marketing.

```text
Title and date

Claim under evaluation
- What capability, resilience property, or control was tested?

System and configuration
- Model/artifact, harness, policy, tools, dependencies, revisions

Environment and authorization
- Benchmark/lab version, access level, egress, identities, containment

Protocol
- Inputs, trials, randomness, budget, assistance, stop criteria, verifier

Results
- Capability, safety/resilience, precision, cost/latency, failures

Evidence
- Configuration, traces or privacy-preserving references, artifacts, validator

Limitations and non-comparability
- Known leakage/contamination, scope, selection, generalization, unmeasured properties

Decision
- Intended use, approval, next action, residual risk, re-evaluation trigger
```

## 10. Reference Resources

| Resource | Use in this workflow |
|---|---|
| [OWASP AISVS](https://github.com/OWASP/AISVS) | Versioned, testable technical controls and assurance levels for AI-enabled systems. |
| [CyBench](https://cybench.github.io/) | Cyber capability benchmark with task/subtask metrics and benchmark-integrity cautions. |
| [VLoc Bench](https://github.com/cisco-foundation-ai/vulnerability-localization-benchmark) | Repository-scale vulnerability-localization evaluation with both vulnerable and patched phases. |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) | Controlled evaluation of attacks and defenses in tool-using agents. |
| [MCP Security Bench](https://github.com/dongsenzhang/MSB) | MCP-specific agent-security research harness. |
| [AgentCyberRange](https://github.com/AgentCyberRange) | Multi-host cyber-range evaluation research under isolated conditions. |

## References

[1]: https://arxiv.org/html/2505.09974v1 "Fine-Tuning Safety Study"
[2]: https://dl.acm.org/doi/10.1145/3733799.3762968 "CyberLLMInstruct"
[3]: https://proceedings.iclr.cc/paper_files/paper/2026/hash/5fc47800ee5b30b8777fdd30abcaaf3b-Abstract-Conference.html "MCP Security Bench"
[4]: https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing "Incident Report: unsanctioned agent behaviour during cyber testing"
