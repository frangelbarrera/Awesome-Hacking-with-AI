<p align="center">
  <img src="assets/images/logo.png" alt="Awesome Hacking with AI Logo" width="700">
</p>

---

<div align="center">

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-blue.svg)](https://github.com/frangelbarrera/Awesome-Hacking-with-AI/pulls)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re/)
[![Stars](https://img.shields.io/github/stars/frangelbarrera/Awesome-Hacking-with-AI?style=social)](https://github.com/frangelbarrera/Awesome-Hacking-with-AI)
[![Last Updated](https://img.shields.io/github/last-commit/frangelbarrera/Awesome-Hacking-with-AI)](https://github.com/frangelbarrera/Awesome-Hacking-with-AI/commits/main)

</div>

---

# Awesome Hacking with AI

> A curated, evidence-led guide to **AI for security** and **security for AI systems**. It brings together authorized security testing, application security, AI agents, model adaptation, datasets, benchmarks, MCP security, defensive automation, and research.

This repository is for security practitioners, AI engineers, researchers, educators, and authorized red teams. It is deliberately broad: the aim is to explain **what a resource does, why it matters, what evidence supports it, and where it belongs in a responsible workflow**.

## Responsible Use

All practical security work must be explicitly authorized, legally compliant, and proportionate to the agreed scope. This repository supports research, education, hardening, validation, detection, remediation, disclosure, and authorized testing. It does not provide instructions for unauthorized access, evading protections, deploying malware, operating command-and-control, impersonating people, or targeting third-party systems.

> If you cannot demonstrate authorization for a target, do not test it. Use a lab, a benchmark, a capture-the-flag environment, or an intentionally vulnerable training application instead.

For coordinated disclosure guidance, consult the [OWASP Vulnerability Disclosure Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html) and [CERT/CC](https://certcc.github.io/CERT-Guide-to-CVD/).

## Contents

- [How to Navigate](#how-to-navigate)
- [Foundations, Governance, and Threat Taxonomies](#foundations-governance-and-threat-taxonomies)
- [Security for AI Systems](#security-for-ai-systems)
  - [LLM, RAG, and Agent Security](#llm-rag-and-agent-security)
  - [MCP Security](#mcp-security)
  - [AI Red Teaming and Evaluation](#ai-red-teaming-and-evaluation)
- [AI for Security](#ai-for-security)
  - [Application Security and Vulnerability Research](#application-security-and-vulnerability-research)
  - [Authorized Security Agents](#authorized-security-agents)
  - [Threat Intelligence and Security Operations](#threat-intelligence-and-security-operations)
- [Models, Data, and Adaptation](#models-data-and-adaptation)
- [Benchmarks, Cyber Ranges, and Evaluation](#benchmarks-cyber-ranges-and-evaluation)
- [MCP Servers for Security Workflows](#mcp-servers-for-security-workflows)
- [Research and Architecture Case Studies](#research-and-architecture-case-studies)
- [Learning Path](#learning-path)
- [Extended Guides](#extended-guides)
- [Contributing and Curation](#contributing-and-curation)

## How to Navigate

The collection follows two complementary paths. **AI for security** concerns how AI can improve code review, vulnerability management, detection engineering, threat intelligence, incident response, and authorized assessments. **Security for AI systems** concerns models, data, RAG, agents, memory, tools, MCP servers, and their software supply chain.

| Reader goal | Start with | Then continue with |
|---|---|---|
| Secure an LLM, RAG, or agentic application | [LLM, RAG, and Agent Security](#llm-rag-and-agent-security) | [MCP Security](#mcp-security) and [AI Security Guide](docs/AI_SECURITY_GUIDE.md) |
| Evaluate security agents responsibly | [Authorized Security Agents](#authorized-security-agents) | [Benchmarks](#benchmarks-cyber-ranges-and-evaluation) and [Agentic Security Guide](docs/AGENTIC_SECURITY_GUIDE.md) |
| Specialize a model for a security task | [Models, Data, and Adaptation](#models-data-and-adaptation) | [Models, Data, and Evaluation Guide](docs/MODELS_DATA_AND_EVALUATION.md) |
| Build an approved MCP workflow | [MCP Security](#mcp-security) | [MCP server directory](#mcp-servers-for-security-workflows) and [MCP Security Guide](docs/MCP_SECURITY.md) |
| Learn systematically | [Learning Path](#learning-path) | Foundations, extended guides, benchmarks, and labs |

## Foundations, Governance, and Threat Taxonomies

Security work involving AI benefits from a shared vocabulary, a lifecycle view, and an evidence model. The following resources help teams reason about risk before selecting a tool or model.

| Resource | Type | Why it matters |
|---|---|---|
| [OWASP GenAI LLM Top 10](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) | Guidance | Current OWASP guidance for LLM and generative AI application risks; the former site is maintained as a historical entry point.[1] |
| [OWASP AI Security and Privacy Guide](https://owasp.org/www-project-ai-security-and-privacy-guide/) | Guidance | Broad security and privacy reference for AI-system design, deployment, and operation. |
| [NIST AI RMF](https://airc.nist.gov/airmf-resources/) | Framework | Voluntary framework organized around **Govern**, **Map**, **Measure**, and **Manage**.[2] |
| [NCSC Secure AI System Development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development) | Lifecycle guidance | Secure design, development, deployment, and operation/maintenance for AI systems.[3] |
| [OWASP AI Security Verification Standard (AISVS)](https://github.com/OWASP/AISVS) | Verification standard | Versioned, testable security requirements across data, models, infrastructure, identities, agents, MCP, adversarial robustness, and monitoring.[20] |
| [MITRE ATLAS](https://atlas.mitre.org/) | Threat knowledge base | Living knowledge base of threats to AI-enabled systems, with techniques, mitigations, and case studies.[4] |
| [NIST Adversarial ML Taxonomy](https://csrc.nist.gov/pubs/ai/100/2/e2023/final) | Taxonomy | Shared terminology for adversarial ML threats and mitigations. |
| [AI Incident Database](https://incidentdatabase.ai/) | Incident resource | Documented AI incidents to inform risk discovery and governance exercises. |
| [AVID Taxonomy](https://avidml.org/taxonomy/) | Risk taxonomy | Structured vocabulary for AI risk identification and documentation. |
| [MLSecOps Top 10](https://ethical.institute/security.html) | Practice guide | Security perspective on the ML lifecycle and operational controls. |

## Security for AI Systems

### LLM, RAG, and Agent Security

An AI application is more than a model. Prompts, retrieval sources, vector stores, identities, tool definitions, code execution paths, logs, memory, deployment infrastructure, providers, and users are all part of the security boundary. Secure design should consider the whole system.[2] [3]

| Resource | Category | Description |
|---|---|---|
| [OWASP GenAI Security Project](https://genai.owasp.org/) | Community guidance | Active home for LLM, agentic AI, red teaming, incident response, and data-security resources. |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | Testing framework | Declarative evaluation, red teaming, and regression testing for LLM applications, agents, and RAG systems. |
| [Garak](https://github.com/NVIDIA/garak) | LLM probing | Open-source LLM vulnerability scanner for systematic model-behavior probing. |
| [PyRIT](https://github.com/Azure/PyRIT) | AI risk assessment | Microsoft framework for identifying and mitigating generative-AI risks. |
| [Purple Llama](https://github.com/meta-llama/PurpleLlama) | Safety resources | Meta tools and research artifacts for trust, safety, and LLM security evaluation. |
| [FuzzyAI](https://github.com/cyberark/FuzzyAI) | Fuzzing | Automated LLM fuzzing for resilience and jailbreak testing. |
| [Open Prompt Injection](https://github.com/liu00222/Open-Prompt-Injection) | Benchmark | Benchmark resources for studying prompt injection and defenses. |
| [Agentic Radar](https://github.com/splx-ai/agentic-radar) | Agent security | CLI scanner for issues in agentic workflows. |
| [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector) | Skill and extension security | Scanner for agent skills and related supply-chain, permission, prompt-injection, and data-flow risks. Treat optional model-assisted analysis as an explicit data-handling decision.[21] |
| [Agent Threat Rules](https://github.com/Agent-Threat-Rule/agent-threat-rules) | Detection-rule format | Machine-readable agent-threat detection rules and reference implementations. The upstream format is a working draft; assess maturity and test coverage before enforcement.[22] |
| [OWASP Agent Memory Guard](https://github.com/OWASP/www-project-agent-memory-guard) | Memory security | OWASP project for detecting and preventing agent memory poisoning. |
| [Semgrep AI Best Practices](https://github.com/semgrep/ai-best-practices) | Secure development | Security rules for code integrating LLM providers, MCP, assistants, and agent frameworks. |
| [Giskard](https://github.com/Giskard-AI/giskard-oss) | Evaluation | Open-source evaluation and testing for AI and LLM systems. |
| [DeepTeam](https://github.com/confident-ai/deepteam) | Red teaming | LLM red-team testing for engineering workflows. |

### MCP Security

The Model Context Protocol (MCP) standardizes how hosts, clients, and servers expose resources, prompts, and tools to AI systems. That composability is powerful, but tools are security boundaries: they can access data or cause actions, and untrusted tool descriptions must be handled with caution.[5]

| Resource | Type | Description |
|---|---|---|
| [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28) | Protocol | Canonical concepts and trust-and-safety principles for resources, prompts, tools, authorization, and user interaction. Pin review to the deployed specification version.[5] |
| [MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) | Technical guidance | Covers authorization, consent, token passthrough, SSRF, state handling, and local-server compromise.[6] |
| [MCP Security Bench (MSB)](https://github.com/dongsenzhang/MSB) | Research benchmark | End-to-end evaluation of MCP-specific attacks across planning, invocation, and response handling. Use only in controlled evaluation and report both security and task-performance conditions.[23] |
| [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) | Threat model | OWASP project in beta covering token exposure, scope creep, tool poisoning, supply chain, execution, and telemetry.[7] |
| [OWASP Third-Party MCP Guide](https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/) | Consumer guidance | Secure discovery, authentication, authorization, sandboxing, least privilege, and human oversight.[8] |
| [MCP Security Checklist](https://github.com/slowmist/MCP-Security-Checklist) | Checklist | Community review aid; validate its advice against protocol guidance and the local environment. |
| [Awesome MCP Security](https://github.com/Puliczek/awesome-mcp-security) | Curated list | Complementary directory of MCP-security resources, tools, research, and guides. |
| [Agent Scan (formerly mcp-scan)](https://github.com/snyk/agent-scan) | Security scanner | Tooling for inspecting MCP server exposures before adoption. |
| [Cisco MCP Scanner](https://github.com/cisco-ai-defense/mcp-scanner) | Security scanner | Multi-engine scanner for MCP servers and tools. |

Before connecting a server, establish source provenance, transport, identities, requested scopes, filesystem and network access, whether it can read/write/execute, logging behavior, dependency posture, and approval steps for consequential actions. See the [MCP Security Guide](docs/MCP_SECURITY.md).

### AI Red Teaming and Evaluation

AI red teaming is disciplined testing of models and AI applications under defined rules, controlled data, and measurable outcomes. Its purpose is remediation—not bypassing safeguards in deployed third-party systems.

| Resource | Focus | Description |
|---|---|---|
| [Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox) | Classical ML | IBM library for adversarial ML attacks, defenses, and robustness evaluation. |
| [Counterfit](https://github.com/Azure/counterfit) | Classical ML | Automation layer for assessing security risks in ML systems. |
| [CleverHans](https://github.com/cleverhans-lab/cleverhans) | Classical ML | Library for adversarial examples and defense benchmarking. |
| [Foolbox](https://github.com/bethgelab/foolbox) | Classical ML | Robustness-evaluation toolbox across common ML frameworks. |
| [TextAttack](https://github.com/QData/TextAttack) | NLP robustness | Framework for adversarial NLP testing, augmentation, and training. |
| [AI Red Teaming Playground Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs) | Training | Learning materials and labs for AI red teaming. |
| [RAMPART](https://github.com/microsoft/RAMPART) | Agentic AI testing | Pytest-native framework for safety and security testing of agentic applications. |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) | Agent-security benchmark | Dynamic environment for prompt-injection attacks and defenses in tool-using agents. Use in an isolated test environment; its API is under active development.[24] |
| [AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) | Platform | AI-security platform with infrastructure, MCP, and jailbreak evaluation components. |

## AI for Security

### Application Security and Vulnerability Research

The high-value role of AI in AppSec is improving discovery, triage, validation, reporting, remediation, and learning while keeping people accountable for security decisions. Strong workflows combine model reasoning with deterministic checks, reproducible evidence, source-code context, and independent validation.[9] [10]

| Resource | Area | Description |
|---|---|---|
| [DARPA AI Cyber Challenge](https://aicyberchallenge.com/) | Vulnerability research | Public effort around cyber reasoning systems for discovering and patching vulnerabilities in critical open-source software. |
| [AIxCC Open Source Archive](https://archive.aicyberchallenge.com/) | Open systems | Competition systems, artifacts, and resources released for study and defensive research. |
| [AutoPatchBench](https://engineering.fb.com/2025/04/29/ai-research/autopatchbench-benchmark-ai-powered-security-fixes/) | Secure repair | Benchmarking for automated repair of fuzzing-detected vulnerabilities. |
| [VLoc Bench](https://github.com/cisco-foundation-ai/vulnerability-localization-benchmark) | Localization | Benchmark for repository navigation, vulnerability localization, and patch verification. |
| [Vulnhalla](https://github.com/cyberark/Vulnhalla) | CodeQL triage | LLM-assisted triage for vulnerability-hunting workflows. |
| [VulnHuntr](https://github.com/protectai/vulnhuntr) | Code review | Open-source vulnerability-hunting assistance for codebases. |
| [Semgrep](https://github.com/semgrep/semgrep) | Static analysis | Deterministic companion to AI-assisted code review. |
| [CodeQL](https://github.com/github/codeql) | Code analysis | Semantic code analysis and query ecosystem. |
| [OSS-Fuzz](https://github.com/google/oss-fuzz) | Fuzzing | Continuous fuzzing for critical open-source projects. |
| [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html) | Interoperability | Standard format for static-analysis results and review. |

The AIxCC final reported 54 synthetic vulnerabilities found out of 63 and 43 patched, alongside responsibly disclosed non-synthetic findings. The useful lesson is not a headline number: it is the importance of end-to-end validation, patch quality, and transparent scoring.[11]

### Authorized Security Agents

There is no universal “best” security agent. Capability depends on task, target access, permitted tools, scaffold, model, evaluation protocol, and human oversight. The directory therefore groups resources by role and avoids global performance claims without comparable evidence.

| Resource | Role | Curation note |
|---|---|---|
| [PentAGI](https://github.com/vxcontrol/pentagi) | Authorized pentesting agent | Multi-agent system for complex security testing with sandboxing, multiple providers, knowledge-graph integrations, and observability. Review current permissions and deployment boundaries. |
| [PentestGPT](https://github.com/GreyDGL/PentestGPT) | Human-guided testing | GPT-empowered assistance for penetration-testing research and authorized workflows. |
| [HackingBuddyGPT](https://github.com/ipa-lab/hackingBuddyGPT) | Research agent | LLM-assisted security agent and benchmark resources. |
| [Shannon](https://github.com/KeygraphHQ/shannon) | Web and API security | Autonomous application-security project; assess any performance claim in its stated test setting. |
| [Strix](https://github.com/usestrix/strix) | Application security | Agents for dynamic code analysis and validation. |
| [Zen-AI-Pentest](https://github.com/SHAdd0WTAka/Zen-Ai-Pentest) | Framework | Multi-agent security testing framework; its tool integrations are privileged operations. |
| [CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI) | Platform | AI-native tool orchestration, roles, and lifecycle management. |
| [BugTraceAI](https://github.com/BugTraceAI/BugTraceAI) | Authorized security agent | Active Apache-2.0 open-source platform maintained by BugTraceAI for authorized security testing with multi-agent orchestration, independent validation, evidence capture, and reporting. Review tool permissions, scope, and isolation before use. |
| [OpenHack](https://github.com/openhackai/OpenHack) | Code security | Multi-agent source-code scanner and validation system. |
| [CAI — archived](https://github.com/aliasrobotics/cai) | Historical artifact | The project reports that it is archived and will receive no further fixes or security patches; retain as research context, not an active dependency. |
| [BoxPwnr](https://github.com/0ca/BoxPwnr) | Lab agent | Agent resources for controlled security challenges. |
| [NYU CTF Agents](https://github.com/NYU-LLM-CTF/nyuctf_agents) | Research agents | Agents associated with scalable CTF evaluation research. |
| [Cyber Security LLM Agents](https://github.com/NVISOsecurity/cyber-security-llm-agents) | Automation examples | LLM-agent examples for common security workflows. |

Strong agent designs separate architecture mapping, hypothesis generation, deterministic scanning, targeted testing, independent validation, evidence capture, deduplication, reporting, and remediation. A single agent that discovers and grades its own finding is a weak design.[9] [10]

### Threat Intelligence and Security Operations

AI can reduce toil in intelligence gathering, alert triage, detection engineering, and incident response. These workflows should default to read-only access, source citation, data minimization, analyst review, and explicit escalation paths.

| Resource | Area | Description |
|---|---|---|
| [MITRE ATT&CK](https://attack.mitre.org/) | Threat knowledge | General adversary-behavior knowledge base that complements ATLAS. |
| [OpenCTI](https://github.com/OpenCTI-Platform/opencti) | CTI platform | Open platform for structuring and sharing threat knowledge. |
| [MISP](https://github.com/MISP/MISP) | Threat sharing | Open-source threat-intelligence sharing platform. |
| [Sigma](https://github.com/SigmaHQ/sigma) | Detection engineering | Open generic signature format for shared detections. |
| [YARA](https://github.com/VirusTotal/yara) | Pattern matching | Rule-based pattern matching for research and classification. |
| [Wazuh](https://github.com/wazuh/wazuh) | Security operations | Open-source XDR/SIEM platform. |
| [Elastic Detection Rules](https://github.com/elastic/detection-rules) | Detection engineering | Public detection rules and rule-development resources. |
| [Splunk Boss of the SOC Dataset](https://github.com/splunk/botsv3) | Training | Dataset and environment for SOC-investigation practice. |
| [CTI-Bench](https://huggingface.co/datasets/AI4Sec/cti-bench) | Benchmark | LLM benchmark focused on cyber-threat-intelligence tasks. |
| [SECURE](https://github.com/aiforsec/SECURE) | Benchmark | Cybersecurity scenario dataset for extraction, understanding, and reasoning. |

## Models, Data, and Adaptation

Model specialization is not synonymous with training a model from scratch. **RAG** adds context at inference time without changing weights. **Instruction tuning** adapts behavior to instruction-response examples. **PEFT/LoRA** updates a small parameter subset. **Domain-adaptive continuous pretraining** adds domain knowledge through further pretraining. **Distillation** transfers behavior from a larger model to a smaller one. The right approach depends on objectives, data, permissions, risk tolerance, and evaluation.[12]

| Resource | Type | Why it belongs here |
|---|---|---|
| [Primus](https://arxiv.org/abs/2502.11191) | Paper, datasets, models | Cybersecurity resources spanning pretraining, instruction tuning, and reasoning distillation, with ablations and benchmark evaluation.[13] |
| [Trend Micro Primus Collection](https://huggingface.co/collections/trendmicro-ailab/primus) | Models and data | Canonical collection referenced by the Primus paper. |
| [Foundation-Sec](https://huggingface.co/fdtn-ai/Foundation-Sec-8B) | Specialized model | Cybersecurity-focused foundation model family; inspect model card, terms, data, and evaluation. |
| [Antares Collection](https://huggingface.co/collections/fdtn-ai/antares) | Specialized models | Security-oriented models for vulnerability-localization workflows. |
| [SecureBERT](https://huggingface.co/ehsanaghaei/SecureBERT) | Specialized model | BERT-family model for cybersecurity text tasks. |
| [Llama-Primus](https://huggingface.co/trendmicro-ailab/Llama-Primus-Base) | Specialized model | Cybersecurity model family associated with the Primus work. |
| [Less Data, More Security](https://arxiv.org/html/2507.02964v1) | Research | Empirical study of domain-adaptive continuous pretraining with a curated corpus and multiple benchmarks.[12] |
| [HackMentor](https://github.com/tmylla/HackMentor) | Historical project | Repository separating data construction, training, and evaluation for a cybersecurity LLM. |
| [CyberLLMInstruct safety study](https://arxiv.org/html/2505.09974v1) | Safety research | Why cybersecurity-oriented fine-tuning needs safety evaluation before and after adaptation.[14] |
| [CyberLLMInstruct (ACM AISec 2025)](https://dl.acm.org/doi/10.1145/3733799.3762968) | Dataset and paper | Pseudo-malicious cybersecurity instruction data and an empirical safety-performance trade-off study. Treat it as research material requiring local rights, risk, and pre/post safety review—not as a default training corpus.[25] |
| [Model Cards](https://huggingface.co/docs/hub/model-cards) | Documentation | Document intended use, provenance, limitations, evaluation, and ethical considerations. |
| [Dataset Cards](https://huggingface.co/docs/hub/datasets-cards) | Documentation | Document source, composition, license, processing, and limitations. |

Any model, dataset, or adapter entry should state its license, source, intended use, limitations, data provenance, safety evaluation, benchmark protocol, and review date. The safety study found reduced safety resilience after fine-tuning in its evaluated settings; utility gains must not substitute for safety testing.[14]

## Benchmarks, Cyber Ranges, and Evaluation

A benchmark score is meaningful only when task, model, agent scaffold, tools, environment, trials, feedback channels, budget, and metric are known. Do not compare white-box and black-box results, different numbers of attempts, hidden grader feedback, or contaminated tasks as though they were equivalent.

| Resource | Focus | Description |
|---|---|---|
| [CyBench](https://cybench.github.io/) | Cyber capability | Professional CTF tasks with subtask measurement, metric definitions, logs, and cautions about comparability.[15] |
| [CyberGym](https://arxiv.org/abs/2506.02548) | Real-world vulnerabilities | Large-scale benchmark across real vulnerabilities and projects; its abstract reports roughly 20% success even for the best evaluated combinations.[16] |
| [NYU CTF Bench](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench) | Agent evaluation | Dockerized CTF challenges for controlled LLM-agent evaluation. |
| [CyberSecEval](https://meta-llama.github.io/PurpleLlama/CyberSecEval/docs/intro) | Model evaluation | Cybersecurity capability and safety evaluation resources. |
| [SecBench](https://huggingface.co/datasets/secbench-hf/SecBench) | Security knowledge | Multi-dimensional cybersecurity benchmark dataset. |
| [CVE-Bench](https://github.com/uiuc-kang-lab/cve-bench) | Web security | Vulnerable web applications and CVEs for controlled agent evaluation. |
| [BountyBench](https://github.com/bountybench/bountybench) | Research impact | Benchmark for vulnerability detection, validation, and patching. |
| [AgentCyberRange](https://github.com/AgentCyberRange) | Cyber-range research | Open research infrastructure for evaluating agents in isolated multi-host web-exploitation and post-exploitation scenarios. Interpret reported scores only with stated prompts, budgets, and verification methods.[26] |
| [AISI multi-step cyber-range study](https://arxiv.org/html/2603.11214v1) | Capability research | Controlled study of multi-step cyber-range performance. Its findings show why budgets, repeated runs, containment, and task design need explicit reporting.[27] |
| [AI Cyber Model Arena](https://www.wiz.io/cyber-model-arena) | Agent/model matrix | Wiz Research evaluation across real-world domains in isolated containers; interpret it as a specific methodology.[17] |
| [BotsBench](https://botsbench.com/) | SOC investigation | Evaluation of agents on security-operations investigation tasks. |
| [DefenseBench](https://defensebench.ai/) | Defensive agents | Evaluation of agents on defensive cybersecurity operations. |

## MCP Servers for Security Workflows

These are not plug-and-play endorsements. Prefer read-only access, minimal scopes, isolated environments, visible tool calls, and explicit human approval before any action that changes a system or sends traffic outside a lab.

| Server or collection | Area | Notes |
|---|---|---|
| [PortSwigger Burp Suite MCP Server](https://github.com/PortSwigger/mcp-server) | Application security | Official integration between Burp Suite and MCP clients; constrain any configuration-changing capabilities. |
| [MCP Security Hub](https://github.com/FuzzingLabs/mcp-security-hub) | Tool collection | Dockerized collection; its documentation describes non-root containers, dropped capabilities, limits, health checks, and CI scanning. Inspect each server individually.[18] |
| [mcp-for-security](https://github.com/cyproxio/mcp-for-security) | Community collection | Independently verify each upstream, package, and permission boundary. |
| [OpenCTI MCP Server](https://github.com/CooperCyberCoffee/opencti_mcp_server) | Threat intelligence | Begin with a read-only service identity and audit access to intelligence data. |
| [Wazuh MCP Server](https://github.com/gensecaihq/Wazuh-MCP-Server) | SOC operations | Separate telemetry queries from response or configuration capabilities. |
| [Semgrep MCP](https://github.com/semgrep/mcp) | Code security | Integration for static-analysis workflows. |
| [radare2 MCP](https://github.com/radareorg/radare2-mcp) | Binary analysis | Use isolated sample handling and read-only mounts. |
| [VirusTotal MCP](https://github.com/w0h1v/mcp-virustotal) | Threat intelligence | Protect API credentials and comply with data-sharing terms. |
| [MCP Servers](https://github.com/modelcontextprotocol/servers) | Discovery | Official project collection and references; apply the same review to every server. |

## Research and Architecture Case Studies

Case studies are useful when read for design choices and stated limitations, not as independent rankings. The transferable lessons are task decomposition, independent validation, durable evidence, model diversity, controlled execution, and human decision ownership.

| Source | Focus | Lesson |
|---|---|---|
| [AWS Security Agent](https://aws.amazon.com/blogs/security/inside-aws-security-agent-a-multi-agent-architecture-for-automated-penetration-testing/) | Multi-agent testing | Baseline coverage, specialized workers, validation, structured evidence, and explicit recognition that plausible findings require rigorous validation.[9] |
| [Cloudflare Vulnerability Harness](https://blog.cloudflare.com/build-your-own-vulnerability-harness/) | Fleet-scale code security | External state, narrow agent context, separate hunting and validation, deduplication, and reproducible evidence before triage.[10] |
| [Wiz AI Cyber Model Arena](https://www.wiz.io/blog/introducing-ai-cyber-model-arena-a-real-world-benchmark-for-ai-agents-in-cybersec) | Evaluation design | Separate model effects from agent effects, use ground truth, repeat trials, and isolate environments.[17] |
| [Praetorian CVE Researcher](https://www.praetorian.com/blog/how-ai-agents-automate-cve-vulnerability-research/) | CVE automation | Research, technology correlation, detection design, critique, validation, and human review as distinct phases.[19] |
| [Team Atlanta](https://team-atlanta.github.io/blog/post-afc/) | AIxCC | Finalist retrospective and implementation-level learning. |
| [Trail of Bits Buttercup](https://trailofbits.com/buttercup/) | AIxCC | Defensive automated vulnerability-research and remediation case study. |
| [Theori RoboDuck](https://theori.io/blog/aixcc-and-roboduck-63447) | AIxCC | Finalist retrospective and resources. |
| [Agent security stack design](https://developer.nvidia.com/blog/where-security-fits-in-an-ai-agent-stack/) | Practitioner guidance | Separate behavioral guidance from the runtime control plane: the agent proposes actions, while identity, policy, egress, and audit controls enforce allowed effects.[28] |
| [AISI cyber-evaluation incident report](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) | Safety case study | A controlled-evaluation incident that reinforces explicit egress decisions, real-time monitoring, solvable task scope, and containment that does not depend on model behavior.[29] |

## Learning Path

| Stage | Focus | Suggested starting resources | Outcome |
|---|---|---|---|
| 1. Foundations | Application security, ML concepts, threat modeling | OWASP, NIST, NCSC, ATT&CK/ATLAS | Vocabulary for risks, assets, controls, and evidence. |
| 2. Secure AI applications | LLM, RAG, prompts, tools, and data flows | OWASP GenAI, Promptfoo, Garak, PyRIT | A test plan for an AI application and integrations. |
| 3. Agents and MCP | Permissions, memory, tools, isolation, logs | MCP specification, MCP guidance, OWASP MCP | A least-privilege architecture and review checklist. |
| 4. AI-assisted AppSec | Code analysis, fuzzing, validation, remediation | Semgrep, CodeQL, OSS-Fuzz, AIxCC | Reproducible, reviewable findings. |
| 5. Adaptation | RAG, SFT, PEFT, domain adaptation, safety | Primus, Foundation-Sec, DAP research | A documented retrieval-versus-tuning decision. |
| 6. Evaluation | Benchmarks, ranges, cost, failure analysis | CyBench, CyberGym, VLoc Bench | An evaluation plan with limitations. |
| 7. Operations | Monitoring, governance, disclosure, maintenance | NIST, NCSC, OWASP | An auditable program rather than a demo. |

## Extended Guides

| Guide | Focus |
|---|---|
| [AI Security Guide](docs/AI_SECURITY_GUIDE.md) | Securing LLM, RAG, and agentic applications across the lifecycle. |
| [MCP Security Guide](docs/MCP_SECURITY.md) | Evaluating and adopting MCP servers with secure permissions, identity, isolation, logs, and supply chain. |
| [Models, Data, and Evaluation Guide](docs/MODELS_DATA_AND_EVALUATION.md) | Responsible cybersecurity-model specialization, dataset review, tuning, RAG, benchmarks, and release decisions. |
| [Agentic Security Guide](docs/AGENTIC_SECURITY_GUIDE.md) | Authorized AI-assisted security workflows with validation, evidence, autonomy boundaries, and human review. |
| [Benchmarking and Evidence Guide](docs/BENCHMARKING_AND_EVIDENCE.md) | Evaluation cards, comparable results, model-adaptation release gates, MCP-loop testing, cyber-range containment, and evidence reporting. |
| [Curation Policy](docs/CURATION_POLICY.md) | Inclusion rules, evidence standards, review cadence, deprecation, and contributor expectations. |
| [Resource Catalog](docs/RESOURCE_CATALOG.md) | Normalized metadata, status, evidence, effects, and adoption boundaries for high-impact resources. |
| [Resource Catalog Supplement](docs/RESOURCE_CATALOG_SUPPLEMENT.md) | Metadata and authorized-use boundaries for the remaining discovery resources promoted in this repository. |
| [Catalog Maintenance Guide](docs/CATALOG_MAINTENANCE.md) | Reproducible catalog regeneration, integrity checks, review authority, evidence requirements, and link-triage procedure. |
| [Maintenance Register](MAINTENANCE.md) | Visible review cadence, evidence to record, current baseline, and retirement rules. |
| [Pre-Adoption Review](docs/PRE_ADOPTION_REVIEW.md) | Required local verification before operational use of an unverified, experimental, historical, or high-impact resource. |

## Contributing and Curation

Contributions are welcome. A high-quality contribution gives readers enough information to assess relevance, activity, evidence, and safe use. Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Curation Policy](docs/CURATION_POLICY.md) before opening an issue or pull request.

Every proposed entry should include a canonical URL, resource type, neutral description, maintainer, license, current status, relevant task or security domain, verification date, and evidence for quantitative claims. Entries involving tools, automation, or MCP must explain permissions, data exposure, actions, isolation, and authorized use. Archived, unmaintained, or experimental projects can be historically valuable, but must be labeled prominently.

## References

[1]: https://owasp.org/www-project-top-10-for-large-language-model-applications/ "OWASP Top 10 for Large Language Model Applications"
[2]: https://airc.nist.gov/airmf-resources/ "NIST AI Risk Management Framework"
[3]: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development "NCSC Secure AI System Development"
[4]: https://atlas.mitre.org/ "MITRE ATLAS"
[5]: https://modelcontextprotocol.io/specification/2025-06-18 "MCP Specification"
[6]: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices "MCP Security Best Practices"
[7]: https://owasp.org/www-project-mcp-top-10/ "OWASP MCP Top 10"
[8]: https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/ "OWASP Third-Party MCP Guide"
[9]: https://aws.amazon.com/blogs/security/inside-aws-security-agent-a-multi-agent-architecture-for-automated-penetration-testing/ "AWS Security Agent"
[10]: https://blog.cloudflare.com/build-your-own-vulnerability-harness/ "Cloudflare Vulnerability Harness"
[11]: https://aicyberchallenge.com/finals-winners-announcement/ "AI Cyber Challenge Final Competition Winners Announcement"
[12]: https://arxiv.org/html/2507.02964v1 "Less Data, More Security"
[13]: https://arxiv.org/abs/2502.11191 "Primus"
[14]: https://arxiv.org/html/2505.09974v1 "CyberLLMInstruct Safety Study"
[15]: https://cybench.github.io/ "CyBench"
[16]: https://arxiv.org/abs/2506.02548 "CyberGym"
[17]: https://www.wiz.io/blog/introducing-ai-cyber-model-arena-a-real-world-benchmark-for-ai-agents-in-cybersec "Wiz AI Cyber Model Arena"
[18]: https://github.com/FuzzingLabs/mcp-security-hub "MCP Security Hub"
[19]: https://www.praetorian.com/blog/how-ai-agents-automate-cve-vulnerability-research/ "Praetorian CVE Researcher"
[20]: https://github.com/OWASP/AISVS "OWASP AI Security Verification Standard"
[21]: https://github.com/NVIDIA/SkillSpector "NVIDIA SkillSpector"
[22]: https://github.com/Agent-Threat-Rule/agent-threat-rules "Agent Threat Rules"
[23]: https://proceedings.iclr.cc/paper_files/paper/2026/hash/5fc47800ee5b30b8777fdd30abcaaf3b-Abstract-Conference.html "MCP Security Bench"
[24]: https://github.com/ethz-spylab/agentdojo "AgentDojo"
[25]: https://dl.acm.org/doi/10.1145/3733799.3762968 "CyberLLMInstruct"
[26]: https://arxiv.org/html/2606.14295v1 "AgentCyberRange"
[27]: https://arxiv.org/html/2603.11214v1 "Measuring AI Agents’ Progress on Multi-Step Cyber Attack Scenarios"
[28]: https://developer.nvidia.com/blog/where-security-fits-in-an-ai-agent-stack/ "Where Security Fits in an AI Agent Stack"
[29]: https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing "Incident Report: unsanctioned agent behaviour during cyber testing"
