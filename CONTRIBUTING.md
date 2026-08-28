# Contributing to Awesome Hacking with AI

Thank you for helping build a reliable, broad, and responsible reference for **AI for security** and **security for AI systems**. The goal is not to collect every project. It is to curate resources that readers can understand, verify, and evaluate safely.

Please read the [Curation Policy](docs/CURATION_POLICY.md) before opening an issue or pull request.

## How to Contribute

### Add or Update a Resource

1. Fork the repository and create a focused branch.
2. Check the relevant README section and guides to avoid duplicates.
3. Add the resource to the most specific existing category. Propose a category only when it represents a durable gap.
4. Use a neutral, concise description that explains the resource’s purpose and limits.
5. Verify the canonical URL, maintainer, license or terms, current status, and the facts in the description.
6. Include the source for quantitative, compatibility, maintenance, security, or benchmark claims.
7. Open a pull request using the provided template.

A good contribution helps a reader answer: **What is this? Who maintains it? What problem does it address? What evidence supports material claims? What are its limits or safety implications?**

### Entry Requirements

| Field | Required for | Notes |
|---|---|---|
| Canonical URL | All entries | Prefer the upstream project, publisher, DOI, or official documentation. |
| Type and category | All entries | Examples: guide, standard, paper, dataset, model, benchmark, lab, tool, agent, or MCP server. |
| Neutral description | All entries | Avoid unverified superlatives, marketing language, and ambiguous claims. |
| Maintainer and license | Software, models, datasets, MCP | Include when the information is published by the source. |
| Status and review date | All entries | Mark archived, historical, experimental, or active when known. |
| Evidence link | Material claims | Required for scores, security controls, compatibility, maintenance, or performance statements. |
| Permissions and safeguards | Agents, tools, and MCP | Explain read/write/execute effects, sensitive data, isolation, approvals, and intended authorized use. |

### Benchmark and Performance Claims

Do not add a score, ranking, “best,” “first,” “production-ready,” “fully autonomous,” cost, or performance claim without its source and test context. Benchmark claims should identify the benchmark and version, task, model, agent or scaffold, tools, environment, trials, metric, date, and limitations.

A vendor or maintainer case study is welcome when clearly framed as such. It must not be presented as independent verification.

### Agents, Tools, and MCP Servers

Resources with execution, write, network, or sensitive-data capabilities require additional context. A contribution should describe the intended authorized workflow, permissions, tool effects, authentication, data exposure, isolation, logging, dependency provenance, and human approval model. For MCP-specific guidance, use the [MCP Security Guide](docs/MCP_SECURITY.md).

### Research, Models, and Datasets

For papers, link the official publisher, DOI, author version, or canonical repository. For models and datasets, link the model or dataset card and provide license, source, intended use, known limits, and relevant evaluation context. Do not treat a preprint, model card, or benchmark as a general endorsement.

### Propose a New Category

Open an issue containing the category name, a short scope statement, at least three candidate resources, and an explanation of why existing sections are insufficient. Categories should distinguish resource types and reader goals; do not create categories solely for a single product or trend.

### Report a Broken, Moved, or Misleading Link

Open an issue with the affected resource, URL, section, observed problem, and corrected canonical URL if available. A timeout, rate limit, or authentication wall is not automatically a broken link, so please include enough context to reproduce the result.

## Responsible Contribution

This repository supports security research, detection, prevention, secure design, hardening, remediation, disclosure, controlled evaluation, and authorized assessments. It does not accept operational content designed to enable unauthorized access, evasion, malware deployment, command-and-control, data theft, impersonation, or targeting of third-party systems.

Use intentionally vulnerable labs, benchmarks, or explicit written authorization when a contribution needs practical security context. Frame dual-use topics in terms of threat understanding, safe testing, mitigation, or responsible disclosure.

## Writing Style

Write clear, professional English. Keep entries factual and concise, link to primary sources where possible, define uncommon abbreviations on first use, and use tables when they improve comparison. Do not add process commentary, generated-content notices, or promotional copy to the public documentation.

## Code of Conduct

Be respectful and professional. Focus discussion on the quality, evidence, relevance, and safety of a resource rather than the person proposing it. Self-promotion is acceptable only when the resource satisfies the same evidence and quality standard as every other entry.

## Development

This is a Markdown-first repository. Verify Markdown rendering, internal links, external URLs, and citations before submitting a pull request. The automated link checker is useful, but it does not validate factual accuracy, canonical ownership, safety, or benchmark comparability; contributors and maintainers remain responsible for those reviews.
