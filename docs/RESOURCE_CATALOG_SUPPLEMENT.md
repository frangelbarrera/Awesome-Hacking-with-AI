# Resource Catalog Supplement

This supplement completes the metadata layer for the discovery resources in the README that are not detailed in the main [Resource Catalog](RESOURCE_CATALOG.md). It is intentionally concise, but every row identifies a source, review status, expected effect, and adoption boundary.

> **Review convention:** every row below was checked on **2026-08-26** for a canonical project or publisher URL. Unless a license or active-maintenance claim is explicitly cited in the row, the correct status is **not verified at review date**. These resources are for evaluation, study, or authorized use only; the row is not an endorsement.

## AI-System Security and Evaluation

| Resource | Type | Maintainer / source | Terms and status | Effects | Adoption boundary |
|---|---|---|---|---|---|
| [FuzzyAI](https://github.com/cyberark/FuzzyAI) | LLM fuzzing tool | CyberArk | License and current status not verified at review date | External query, configuration-dependent | Test only owned or approved model endpoints with rate/cost limits and non-sensitive data. |
| [Open Prompt Injection](https://github.com/liu00222/Open-Prompt-Injection) | Benchmark | liu00222 / project authors | License and current status not verified at review date | Controlled evaluation | Use only as an evaluation resource; do not generalize results outside its task design. |
| [OWASP Agent Memory Guard](https://github.com/OWASP/www-project-agent-memory-guard) | Guidance/project | OWASP | OWASP project terms; current status not verified at review date | Knowledge | Use as design guidance and validate controls in the local agent architecture. |
| [Semgrep AI Best Practices](https://github.com/semgrep/ai-best-practices) | Secure-development rules | Semgrep | License and current status not verified at review date | Read | Review rule scope and false-positive/negative behavior before use in CI. |
| [Giskard](https://github.com/Giskard-AI/giskard-oss) | AI evaluation tool | Giskard AI | License and current status not verified at review date | Read / external query, configuration-dependent | Use representative but non-sensitive evaluation data; review integrations and retention. |
| [DeepTeam](https://github.com/confident-ai/deepteam) | LLM red-team tool | Confident AI | License and current status not verified at review date | External query, configuration-dependent | Limit to authorized endpoints and record prompts, budget, and approvals. |
| [Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox) | Adversarial-ML library | Linux Foundation AI & Data / Trusted-AI | License and current status not verified at review date | Local evaluation | Use controlled datasets and models; document attack/defense assumptions. |
| [Counterfit](https://github.com/Azure/counterfit) | ML security-assessment tool | Microsoft | License and current status not verified at review date | Local / external query, configuration-dependent | Assess owned or approved ML systems only and preserve reproducible test evidence. |
| [CleverHans](https://github.com/cleverhans-lab/cleverhans) | ML robustness library | CleverHans Lab | License and current status not verified at review date | Local evaluation | Use only for research or authorized robustness assessment. |
| [Foolbox](https://github.com/bethgelab/foolbox) | ML robustness library | BETHGE Lab | License and current status not verified at review date | Local evaluation | Use controlled models and datasets; validate interpretation with domain experts. |
| [TextAttack](https://github.com/QData/TextAttack) | NLP robustness framework | QData | License and current status not verified at review date | Local evaluation | Use in controlled NLP evaluation; protect sensitive text corpora. |
| [AI Red Teaming Playground Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs) | Training labs | Microsoft | License and current status not verified at review date | Controlled evaluation | Run lab content in a segregated learning environment. |
| [AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) | AI-security platform | Tencent | License and current status not verified at review date | Read / external query, configuration-dependent | Review modules, credentials, egress, and tool effects before enabling any component. |

## Application Security, Code Analysis, and Vulnerability Research

| Resource | Type | Maintainer / source | Terms and status | Effects | Adoption boundary |
|---|---|---|---|---|---|
| [Vulnhalla](https://github.com/cyberark/Vulnhalla) | CodeQL triage tool | CyberArk | License and current status not verified at review date | Read | Analyze approved code copies and independently validate all triage output. |
| [VulnHuntr](https://github.com/protectai/vulnhuntr) | Code-review tool | Protect AI | License and current status not verified at review date | Read / external query, configuration-dependent | Use read-only code access; protect proprietary source and validate findings. |
| [Semgrep](https://github.com/semgrep/semgrep) | Static-analysis engine | Semgrep | License and current status not verified at review date | Read | Pin rules and versions, review access to source code, and validate findings. |
| [CodeQL](https://github.com/github/codeql) | Semantic code analysis | GitHub | License and current status not verified at review date | Read | Use approved repositories and queries; review result quality before remediation. |
| [OSS-Fuzz](https://github.com/google/oss-fuzz) | Continuous-fuzzing service | Google | License and current status not verified at review date | Controlled execution | Follow program rules; use supported open-source targets and isolate local reproductions. |
| [AutoPatchBench](https://engineering.fb.com/2025/04/29/ai-research/autopatchbench-benchmark-ai-powered-security-fixes/) | Benchmark | Meta Engineering / authors | Publisher terms; research status | Controlled evaluation | Treat as a benchmark reference; report exact dataset/task conditions. |
| [SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html) | Open standard | OASIS | OASIS terms | Knowledge / read | Use for interoperable result exchange; validate producer/consumer version compatibility. |

## Authorized Security Agents and Security Automation

| Resource | Type | Maintainer / source | Terms and status | Effects | Adoption boundary |
|---|---|---|---|---|---|
| [Zen-AI-Pentest](https://github.com/SHAdd0WTAka/Zen-Ai-Pentest) | Security-testing framework | SHAdd0WTAka | License and current status not verified at review date | Execution and network effects, configuration-dependent | Written authorization, an allowlisted lab or target scope, isolated credentials, and explicit approval for actions. |
| [CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI) | Security automation platform | Ed1s0nZ | License and current status not verified at review date | Execution and network effects, configuration-dependent | Review roles, integrations, egress, and tool permissions before any authorized use. |
| [OpenHack](https://github.com/openhackai/OpenHack) | Code-security agent | OpenHack AI | License and current status not verified at review date | Read / execution, configuration-dependent | Use approved code copies or controlled labs; independently validate all reported findings. |
| [BoxPwnr](https://github.com/0ca/BoxPwnr) | Lab/benchmark agent | 0ca | License and current status not verified at review date | Controlled execution | Use only platform-approved or local lab challenges and preserve task-level logs. |
| [NYU CTF Agents](https://github.com/NYU-LLM-CTF/nyuctf_agents) | Research agents | NYU LLM CTF | License and current status not verified at review date | Controlled execution | Restrict to the stated research benchmark or isolated CTF environment. |
| [Cyber Security LLM Agents](https://github.com/NVISOsecurity/cyber-security-llm-agents) | Workflow examples | NVISO | License and current status not verified at review date | Read / external query, configuration-dependent | Treat as design examples; assess each integration’s data and permissions before use. |

## Threat Intelligence, Detection, and Security Operations

| Resource | Type | Maintainer / source | Terms and status | Effects | Adoption boundary |
|---|---|---|---|---|---|
| [OpenCTI](https://github.com/OpenCTI-Platform/opencti) | CTI platform | OpenCTI Platform | License and current status not verified at review date | Read / write, deployment-dependent | Begin with a read-only service identity and protect intelligence-sharing data. |
| [MISP](https://github.com/MISP/MISP) | Threat-sharing platform | MISP Project | License and current status not verified at review date | Read / write, deployment-dependent | Respect sharing communities, access controls, and data-handling agreements. |
| [Sigma](https://github.com/SigmaHQ/sigma) | Detection rule format | SigmaHQ | License and current status not verified at review date | Knowledge / read | Test rules against representative telemetry before deployment. |
| [YARA](https://github.com/VirusTotal/yara) | Pattern-matching engine | VirusTotal / YARA contributors | License and current status not verified at review date | Read / local processing | Analyze untrusted samples in isolated environments and review rules before enforcement. |
| [Wazuh](https://github.com/wazuh/wazuh) | Security operations platform | Wazuh | License and current status not verified at review date | Read / administrative actions, deployment-dependent | Separate analyst queries from administrative privileges and protect telemetry. |
| [Elastic Detection Rules](https://github.com/elastic/detection-rules) | Detection content | Elastic | License and current status not verified at review date | Read | Validate rules against local schemas, telemetry quality, and alert workflows. |
| [Splunk Boss of the SOC Dataset](https://github.com/splunk/botsv3) | Training dataset | Splunk | License and current status not verified at review date | Controlled evaluation | Use for training and lab investigation; follow dataset terms. |
| [CTI-Bench](https://huggingface.co/datasets/AI4Sec/cti-bench) | CTI benchmark | AI4Sec | Dataset-card terms and status not verified at review date | Controlled evaluation | Review the dataset card, license, data provenance, and task boundaries. |
| [SECURE](https://github.com/aiforsec/SECURE) | Security benchmark | AI4Sec / project source | License and current status not verified at review date | Controlled evaluation | Use only under published terms and report benchmark version and methodology. |

## Models, Data, and Benchmarks

| Resource | Type | Maintainer / source | Terms and status | Effects | Adoption boundary |
|---|---|---|---|---|---|
| [Antares Collection](https://huggingface.co/collections/fdtn-ai/antares) | Model collection | Foundation AI | Model-card license/terms and status not verified at review date | Local or hosted inference | Review each model card, data provenance, intended use, safety evaluation, and deployment controls. |
| [SecureBERT](https://huggingface.co/ehsanaghaei/SecureBERT) | Specialized model | ehsanaghaei | Model-card license/terms and status not verified at review date | Local or hosted inference | Review model card and task suitability; do not infer general security capability. |
| [CyberSecEval](https://meta-llama.github.io/PurpleLlama/CyberSecEval/docs/intro) | Evaluation suite | Meta Purple Llama | Publisher/project terms and status not verified at review date | Controlled evaluation | Record the exact suite version, setting, model, and evaluation conditions. |
| [SecBench](https://huggingface.co/datasets/secbench-hf/SecBench) | Benchmark dataset | secbench-hf | Dataset-card license/terms and status not verified at review date | Controlled evaluation | Review the dataset card and use only for the documented task. |
| [CVE-Bench](https://github.com/uiuc-kang-lab/cve-bench) | Web-vulnerability benchmark | UIUC Kang Lab | License and current status not verified at review date | Controlled execution | Use isolated benchmark applications and state task/hint/attempt conditions. |
| [BotsBench](https://botsbench.com/) | SOC-agent benchmark | BotsBench source | Publisher terms and status not verified at review date | Controlled evaluation | Treat as a setting-specific benchmark and retain task/version context. |
| [DefenseBench](https://defensebench.ai/) | Defensive-agent benchmark | DefenseBench source | Publisher terms and status not verified at review date | Controlled evaluation | Treat as a setting-specific benchmark and retain task/version context. |

## Supplement Maintenance

When a resource gains a published license, stable release, archival notice, benchmark paper, or clearer safety documentation, update this row rather than assuming a positive status. High-risk resources must retain their row here or be promoted to the main catalog only after the additional metadata has been verified.

## Additional MCP Discovery and Review Resources

| Resource | Type | Maintainer / source | Terms and status | Effects | Adoption boundary |
|---|---|---|---|---|---|
| [mcp-for-security](https://github.com/cyproxio/mcp-for-security) | Community MCP directory | cyproxio | License and current status not verified at review date | Varies by listed server | Treat as discovery material only. Verify every upstream server, package, identity, data flow, and permission tier before installation. |
| [Cisco MCP Scanner](https://github.com/cisco-ai-defense/mcp-scanner) | MCP security scanner | Cisco AI Defense | License and current status not verified at review date | Read / local analysis, configuration-dependent | Analyze review copies first; validate findings and control any uploaded configuration or source data. |
| [MCP Servers](https://github.com/modelcontextprotocol/servers) | Reference-server collection | Model Context Protocol project | Project terms and current status not verified at review date | Varies by server | Treat each server as a separate component with its own provenance, permissions, effects, and adoption review. |
| [MCP Security Checklist](https://github.com/slowmist/MCP-Security-Checklist) | Community checklist | SlowMist | License and current status not verified at review date | Knowledge | Use as a secondary review aid and resolve discrepancies against official MCP and OWASP guidance. |
| [Awesome MCP Security](https://github.com/Puliczek/awesome-mcp-security) | Curated directory | Puliczek | License and current status not verified at review date | Knowledge | Use for discovery only; every listed component needs independent validation before adoption. |

## Foundations, Documentation, and Case Studies

| Resource | Type | Maintainer / source | Terms and status | Effects | Adoption boundary |
|---|---|---|---|---|---|
| [OWASP AI Security and Privacy Guide](https://owasp.org/www-project-ai-security-and-privacy-guide/) | Guidance | OWASP | OWASP site terms; project status not verified at review date | Knowledge | Use as non-binding guidance and record the consulted version. |
| [NIST Adversarial ML Taxonomy](https://csrc.nist.gov/pubs/ai/100/2/e2023/final) | Taxonomy | U.S. NIST | U.S. government publication terms | Knowledge | Use terminology with the source’s stated scope and version. |
| [AI Incident Database](https://incidentdatabase.ai/) | Incident resource | AI Incident Database | Site terms and status not verified at review date | Knowledge | Use incidents as contextual evidence; check primary sources for consequential decisions. |
| [AVID Taxonomy](https://avidml.org/taxonomy/) | Risk taxonomy | AVID | Site terms and status not verified at review date | Knowledge | Use as an aid to structured risk discovery, not as a complete control set. |
| [MLSecOps Top 10](https://ethical.institute/security.html) | Practice guide | Ethical Institute | Site terms and status not verified at review date | Knowledge | Cross-check with primary standards and the local system threat model. |
| [OWASP Third-Party MCP Guide](https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/) | Guidance | OWASP GenAI Security Project | OWASP site terms; status not verified at review date | Knowledge | Pair with the current MCP specification and local authorization design. |
| [MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) | Guidance | Model Context Protocol project | Project documentation terms | Knowledge | Apply to the exact transport and authorization model being deployed. |
| [Purple Llama](https://github.com/meta-llama/PurpleLlama) | Evaluation resources | Meta | License and current status not verified at review date | Controlled evaluation | Review individual tool/data licenses and use only approved test data and endpoints. |
| [Trend Micro Primus Collection](https://huggingface.co/collections/trendmicro-ailab/primus) | Model/data collection | Trend Micro AI Lab | Collection/card terms and status not verified at review date | Local or hosted inference | Review each card, license, data artifact, and evaluation before adoption. |
| [Hugging Face Model Cards](https://huggingface.co/docs/hub/model-cards) | Documentation guidance | Hugging Face | Documentation terms | Knowledge | Use as a documentation baseline; do not infer quality from card presence alone. |
| [Hugging Face Dataset Cards](https://huggingface.co/docs/hub/datasets-cards) | Documentation guidance | Hugging Face | Documentation terms | Knowledge | Use to record provenance, licensing, composition, and limitations. |
| [MITRE ATT&CK](https://attack.mitre.org/) | Threat knowledge base | MITRE | MITRE terms | Knowledge | Combine with local telemetry and ATLAS when assessing AI-enabled systems. |
| [AIxCC Open Source Archive](https://archive.aicyberchallenge.com/) | Program archive | DARPA AI Cyber Challenge | Archive terms and status not verified at review date | Controlled execution | Study released artifacts under their terms and preserve system/version context. |
| [AWS Security Agent](https://aws.amazon.com/blogs/security/inside-aws-security-agent-a-multi-agent-architecture-for-automated-penetration-testing/) | Vendor case study | AWS Security Blog | AWS site terms | Knowledge | Treat stated architecture and results as a vendor case study, not independent benchmark evidence. |
| [Cloudflare Vulnerability Harness](https://blog.cloudflare.com/build-your-own-vulnerability-harness/) | Vendor case study | Cloudflare | Cloudflare site terms | Knowledge | Treat as an architecture reference; validate implementation and results independently. |
| [Wiz AI Cyber Model Arena](https://www.wiz.io/blog/introducing-ai-cyber-model-arena-a-real-world-benchmark-for-ai-agents-in-cybersec) | Vendor benchmark case study | Wiz Research | Wiz site terms | Controlled evaluation | Interpret results only with its published task, model, agent, container, and trial context. |
| [AI Cyber Model Arena](https://www.wiz.io/cyber-model-arena) | Vendor benchmark | Wiz Research | Wiz site terms and status not verified at review date | Controlled evaluation | Use as a setting-specific comparison; do not generalize scores beyond published conditions. |
| [Praetorian CVE Researcher](https://www.praetorian.com/blog/how-ai-agents-automate-cve-vulnerability-research/) | Vendor case study | Praetorian | Praetorian site terms | Knowledge | Treat as a workflow reference and independently validate claims before adoption. |
| [Team Atlanta](https://team-atlanta.github.io/blog/post-afc/) | AIxCC case study | Team Atlanta | Site terms and status not verified at review date | Knowledge | Use for design lessons; refer to primary program artifacts for comparative claims. |
| [Trail of Bits Buttercup](https://trailofbits.com/buttercup/) | AIxCC case study | Trail of Bits | Site terms and status not verified at review date | Knowledge | Use for architecture and research context; review released artifact terms. |
| [Theori RoboDuck](https://theori.io/blog/aixcc-and-roboduck-63447) | AIxCC case study | Theori | Site terms and status not verified at review date | Knowledge | Use for retrospective context, not as an independent capability ranking. |
| [Emerging Security Practices for AI Agents](https://www.frontiermodelforum.org/issue-briefs/emerging-security-practices-for-ai-agents/) | Industry issue brief | Frontier Model Forum | Publisher terms | Practitioner guidance | Knowledge | Treat as a multi-stakeholder architecture and risk reference, not independent empirical proof. Adapt controls to the local system and threat model. |
| [Where Security Fits in an AI Agent Stack](https://developer.nvidia.com/blog/where-security-fits-in-an-ai-agent-stack/) | Practitioner architecture guidance | NVIDIA | Publisher terms | Practitioner guidance | Knowledge | Use its authority-boundary model as design guidance; validate all controls in the deployed runtime and policy plane. |
| [Incident Report: unsanctioned agent behaviour during cyber testing](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) | Evaluation safety case study | UK AI Security Institute | Crown copyright / site terms | Published incident report | Knowledge | Retain the report’s configuration-specific caveats. Use it to strengthen evaluation containment, monitoring, egress, and task-design safeguards. |
| [The next generation of MCP](https://blog.cloudflare.com/mcp-v2/) | MCP implementation/migration article | Cloudflare | Publisher terms | Vendor implementation guidance | Knowledge | Treat as an implementation-specific migration reference; review the current official MCP specification and the actual deployed SDK. |
