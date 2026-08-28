# Models, Data, and Evaluation Guide

Specializing models for cybersecurity can improve usefulness, but “fine-tuning” is not a single solution and it is never a substitute for security engineering. This guide helps teams choose among retrieval, adaptation, training, and agentic orchestration while preserving provenance, evaluation quality, and safety.

## 1. Choose the Smallest Effective Intervention

Start with the task and evidence gap. A model that lacks access to current, proprietary, or fast-changing security knowledge may need retrieval rather than weight updates. A model that cannot follow a desired reporting format may need instruction tuning. A system that needs to call tools, maintain state, or coordinate reviewers may need an agentic workflow. These decisions have different costs, risks, and maintenance duties.

| Approach | Changes model weights? | Best for | Main risks |
|---|---:|---|---|
| Prompting and structured output | No | Small behavior and formatting changes | Fragility, hidden assumptions, prompt injection. |
| RAG | No | Current or private knowledge with source visibility | Retrieval poisoning, access-control failures, stale or misleading context. |
| Fine-tuning / SFT | Yes | Domain tasks and instruction-following behavior | Data quality, privacy, overfitting, safety regression. |
| PEFT / LoRA | Partly | Resource-efficient task adaptation | Adapter provenance, base-model mismatch, evaluation gaps. |
| Continued pretraining / DAP | Yes | Broad domain knowledge and terminology | Compute cost, catastrophic forgetting, corpus licensing, contamination. |
| Distillation | Yes | Smaller models that inherit selected behavior | Teacher bias/errors, provenance, safety loss. |
| Agentic scaffold | Usually no | Multi-step workflows, tools, state, and review | Excessive agency, permission misuse, memory poisoning, unreliable validation. |

## 2. Define the Use Case and Safety Boundary

A useful training plan begins with a narrow, authorized outcome such as security-ticket classification, CVE summarization with citations, detection-rule drafting, log analysis, code-risk triage, or remediation explanation. Avoid a vague objective like “make the model better at hacking.” The latter cannot be evaluated responsibly or bounded operationally.

| Planning question | Example evidence |
|---|---|
| What task is being improved? | Task definition, inputs, outputs, intended user, decision owner. |
| What must never change? | Privacy, access-control, safety, refusal, citation, and authorization requirements. |
| What data is permitted? | License, provenance, collection date, data classification, retention, and consent basis. |
| What is the baseline? | Untuned model, existing RAG workflow, deterministic tool, or expert process. |
| How is success measured? | Held-out benchmark, human rubric, false-positive/negative review, cost, latency, safety tests. |
| What is the deployment boundary? | Allowed users, networks, integrations, tools, scopes, and incident owner. |

## 3. Dataset Governance

Security datasets are powerful because they may include code, vulnerabilities, exploit narratives, operational logs, indicators, credentials, and customer context. Their value does not remove obligations around licensing, privacy, disclosure, or dual use.

| Dataset-control area | Questions to answer before use |
|---|---|
| Provenance | Who created it? From which sources? Is every source legally reusable? |
| License | Does the dataset license permit training, redistribution, commercial use, and derivatives? |
| Sensitive data | Does it contain credentials, personal data, customer data, unpublished vulnerabilities, or harmful material? |
| Temporal context | Are dates retained so the model can distinguish historical from current information? |
| Quality and duplication | Are duplicates, low-quality samples, hallucinated examples, and benchmark leakage controlled? |
| Task fit | Does the data represent the actual input/output behavior, not only an adjacent topic? |
| Safety | Does the curation preserve defensive context, authorization, and safe handling of dual-use material? |
| Documentation | Is there a dataset card with composition, filtering, known gaps, and contact/retirement information? |

The [Hugging Face Dataset Cards guide](https://huggingface.co/docs/hub/datasets-cards) is a practical documentation baseline. The [Primus paper](https://arxiv.org/abs/2502.11191) is useful because it distinguishes resources for pretraining, instruction tuning, and reasoning distillation rather than treating all cybersecurity data as interchangeable.[1]

## 4. Continued Pretraining and Domain Adaptation

Continued pretraining, also called domain-adaptive continuous pretraining (DAP), expands a base model’s familiarity with domain language and patterns. It is an expensive intervention and should not be chosen merely because a corpus is available. It requires strong documentation of the base model, training corpus, filtering, licensing, hyperparameters, compute environment, and evaluation.

The paper *Less Data, More Security* evaluates DAP across multiple base architectures using a curated cybersecurity corpus and multiple security benchmarks. Its contribution is a useful methodology: carefully scoped corpus curation, conservative training, and evaluation against relevant tasks—not a claim that one data quantity or configuration will work universally.[2]

| DAP decision | Recommended practice |
|---|---|
| Base model | Confirm license, language coverage, known limitations, and suitability for the intended deployment. |
| Corpus | Favor authoritative, licensed, dated sources; remove secrets, personal data, duplicates, and low-quality material. |
| Training plan | Use conservative changes, checkpoints, reproducible configuration, and explicit stop criteria. |
| Retention | Preserve manifests and dataset versions so results remain explainable. |
| Evaluation | Measure target capability, general capability, robustness, safety, privacy, and contamination separately. |
| Release | Publish a model card, training summary, evaluation protocol, intended use, and limitations. |

## 5. Instruction Tuning and PEFT

Instruction tuning aligns output behavior to curated examples. PEFT methods such as LoRA can make adaptation practical where full fine-tuning is not justified. The lower compute cost is valuable, but it does not reduce the need for data governance or safety evaluation.

[HackMentor](https://github.com/tmylla/HackMentor) is a historical example that separates data construction, model training, and evaluation, and releases LoRA weights. Its older dependency context should be reviewed before any reproduction, but its separation of concerns remains instructive.[3]

| Risk | Mitigation |
|---|---|
| Training data changes safety behavior | Test pre- and post-adaptation using safety and task suites; do not assume the base model’s guardrails remain intact. |
| Data does not match production tasks | Use representative held-out examples and human review rather than generic quizzes alone. |
| Adapter is detached from base model context | Record exact base version, tokenizer, training method, parameters, and compatibility constraints. |
| Evaluation data leaks into training | Keep immutable, access-controlled held-out sets; record lineage and detect near duplicates. |
| “Good answers” hide false confidence | Require citations, evidence fields, uncertainty, and independent verification for consequential outputs. |

Research on safety risks from pseudo-malicious cybersecurity data found reduced safety resilience after fine-tuning across its evaluated models and argues for safety-aware data transformation and explicit evaluation.[4] This is a reason to adopt a safety gate, not a reason to avoid security research altogether.

## 6. RAG Is a Security System

RAG is often the right first choice for current advisories, internal runbooks, source repositories, threat intelligence, or policies. It preserves updateability and can make citations visible. However, a RAG pipeline creates an ingestion, indexing, retrieval, authorization, and output-handling system that needs its own threat model.

| RAG stage | Security control |
|---|---|
| Ingestion | Verify origin, scan uploads, classify data, extract safely, retain source metadata. |
| Chunking and indexing | Preserve document identity and access labels; avoid mixing tenant or sensitivity boundaries. |
| Retrieval | Enforce user-specific authorization before retrieval, not only after generation. |
| Context assembly | Label retrieved content as untrusted data and avoid treating it as system instruction. |
| Generation | Require source references; use output validation where generated text drives tools or decisions. |
| Monitoring | Track retrieval quality, denied access, injection attempts, stale sources, and citation failures. |

## 7. Evaluation Is a Product Requirement

Cybersecurity model evaluation should use multiple independent dimensions. Knowledge questions alone cannot establish whether a model can safely operate in a workflow, and a single CTF result cannot establish general capability.

| Dimension | What to measure | Candidate resource |
|---|---|---|
| Security knowledge | Correctness, calibration, citation quality, temporal validity | [SecBench](https://huggingface.co/datasets/secbench-hf/SecBench), [CTI-Bench](https://huggingface.co/datasets/AI4Sec/cti-bench) |
| Vulnerability localization | Correct files/functions, evidence, patch verification | [VLoc Bench](https://github.com/cisco-foundation-ai/vulnerability-localization-benchmark) |
| Controlled cyber tasks | Success, subtasks, time, cost, action trace | [CyBench](https://cybench.github.io/), [NYU CTF Bench](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench) |
| Real-world vulnerability tasks | Reproduction, impact, patch quality, false positives | [CyberGym](https://arxiv.org/abs/2506.02548), [BountyBench](https://github.com/bountybench/bountybench) |
| AI application safety | Injection, leakage, tool use, resource usage, output handling | [Promptfoo](https://github.com/promptfoo/promptfoo), [Garak](https://github.com/NVIDIA/garak), [PyRIT](https://github.com/Azure/PyRIT) |
| Agent operations | Authorization, sandbox escape resistance, approvals, replayability | Local isolated range plus an agent-specific test harness |

CyBench publishes separate unguided and subtask-guided results and warns about a known evaluation leak affecting historical scores. That transparency is exactly why benchmark context must accompany every reported number.[5] CyberGym evaluates 1,507 real-world vulnerabilities across 188 projects and reports a difficult performance ceiling in its abstract, reinforcing the need for cautious claims.[6]

## 8. A Safe Release Gate

Do not release a model, adapter, dataset, or benchmark result with only a capability score. Release decisions should be traceable and reversible.

| Gate | Required artifact |
|---|---|
| Purpose | Intended-use statement, prohibited uses, users, and operational boundary. |
| Provenance | Model/dataset card, licenses, versions, data manifest, and dependency inventory. |
| Capability | Task evaluation with baseline, held-out data, methodology, metrics, and limitations. |
| Safety | Pre/post testing for relevant threats, documented residual risk, and mitigation plan. |
| Privacy and secrets | Sensitive-data review, redaction tests, retention policy, and incident route. |
| Operations | Monitoring, reporting channel, rollback path, update owner, and deprecation date. |
| Human accountability | Named reviewer and approval for high-impact release or integration. |

## References

[1]: https://arxiv.org/abs/2502.11191 "Primus"
[2]: https://arxiv.org/html/2507.02964v1 "Less Data, More Security"
[3]: https://github.com/tmylla/HackMentor "HackMentor"
[4]: https://arxiv.org/html/2505.09974v1 "Safety Risks in LLMs Fine-Tuned with Pseudo-Malicious Cyber Security Data"
[5]: https://cybench.github.io/ "CyBench"
[6]: https://arxiv.org/abs/2506.02548 "CyberGym"
