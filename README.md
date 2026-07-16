# Multimodal AI — Selected Coursework

This repository contains two curated projects from a 2026 Multimodal AI course, selected for their implementation depth in reinforcement learning, vision-language models, agents, and optimization.

| Project | Focus | Evidence |
|---|---|---|
| [GRPO VLM adaptation with SFT warm start](grpo-vlm-sft-warm-start/) | GRPO, VLM adaptation, training initialization | Archived warm-start reward 0.4936 vs. cold-start reward 0.2179; held-out formatting success 100% |
| [MILP visual diagnostic agent](milp-visual-diagnostic-agent/) | Tool-using VLM agent, optimization reasoning | Exploratory five-case comparison: vision-enabled success 2/5 vs. 0/5 built-in baseline |

## Repository structure

- [`grpo-vlm-sft-warm-start/`](grpo-vlm-sft-warm-start/) — a curated notebook on GRPO adaptation for a vision-language model with an SFT warm start.
- [`milp-visual-diagnostic-agent/`](milp-visual-diagnostic-agent/) — a curated implementation and archived aggregate results for diagnosing visual MILP representations.

## Interpretation

The MILP visual diagnostic agent is intentionally presented as an exploratory case study: its archived comparison covers five cases, so it is not a statistically conclusive benchmark.

## Coursework curation note

Course PDFs, raw data, model weights, credentials, raw logs, historical drafts, environments, and large generated outputs are intentionally excluded. The archived results are reported from the original coursework experiments; neither project was rerun during curation.

## Related project

[Semantic Feedback for LLM-Generated Optimization Code Repair](https://github.com/niu1298/semantic-feedback-for-llm-generated-optimization-code-repair)

## Copyright and Scope

This repository is a public portfolio rather than an open-source release. It contains curated excerpts of individually completed coursework; excluded materials include course handouts, starter code, datasets, model weights, credentials, and raw logs. See [NOTICE.md](NOTICE.md).
