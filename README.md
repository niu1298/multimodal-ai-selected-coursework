# Multimodal AI — Coursework Portfolio (HW1–HW5)

This repository is a curated, end-to-end portfolio of five Multimodal AI homework assignments. Together, they trace a progression from visual verification and multimodal representation learning to parameter-efficient VLM adaptation, reinforcement learning, and tool-using agents.

| Homework | Focus | Primary artifacts | Archived evidence |
|---|---|---|---|
| [HW1 — MILP representation foundations and CLIP evaluation](hw1-milp-representation-and-clip-evaluation/) | Synthetic MILP representations, graphs, symbolic features, visualization, and a separate frozen-CLIP bonus evaluation | [Final notebook](hw1-milp-representation-and-clip-evaluation/notebooks/hw1_milp_representation_and_clip_evaluation.ipynb) · [Final report](hw1-milp-representation-and-clip-evaluation/hw1_report.pdf) | CLIP AUROC **0.601** for the Hateful Memes bonus experiment only |
| [HW2 — Multimodal fusion and contrastive learning](hw2-multimodal-fusion-contrastive-learning/) | Early/late/tensor fusion and graph–text representation alignment | [Final notebook](hw2-multimodal-fusion-contrastive-learning/notebooks/hw2_multimodal_fusion_contrastive_learning.ipynb) · No separate final report | Complete archived notebook; no single reconciled public metric claim |
| [HW3 — LoRA adaptation of a VLM for MILP visuals](hw3-vlm-lora-milp-visuals/) | Image-QA construction, LoRA adaptation, and held-out VLM evaluation | [Final notebook](hw3-vlm-lora-milp-visuals/notebooks/hw3_vlm_lora_milp_visuals.ipynb) · [Final report](hw3-vlm-lora-milp-visuals/hw3_report.pdf) | 30-held-out results: binary **6.7% → 76.7%**; integer **3.3% → 53.3%** |
| [HW4 — GRPO VLM adaptation with SFT warm start](hw4-grpo-vlm-sft-warm-start/) | LoRA SFT, task-specific reward design, and GRPO | [Final notebook](hw4-grpo-vlm-sft-warm-start/notebooks/hw4_grpo_vlm_sft_warm_start.ipynb) · [Final report](hw4-grpo-vlm-sft-warm-start/hw4_report.pdf) | Warm-start reward **0.4936** vs. cold-start reward **0.2179** |
| [HW5 — MILP visual diagnostic agent](hw5-milp-visual-diagnostic-agent/) | Tool-using VLM workflow and structured MILP reasoning | [Final notebook](hw5-milp-visual-diagnostic-agent/notebooks/hw5_milp_visual_diagnostic_agent.ipynb) · [Final report](hw5-milp-visual-diagnostic-agent/hw5_report.pdf) | Exploratory five-case comparison: vision-enabled **2/5** vs. built-in baseline **0/5** |

> Each folder also contains a short guide to the assignment’s method, implementation, result provenance, and runtime limitations. The notebooks and reports above are the primary final coursework artifacts.

## Learning progression

visual verification → multimodal representation learning → VLM adaptation → policy optimization → tool-using reasoning

## Curation note

Each homework folder preserves a complete final notebook and, where a separate final report exists, the original PDF. The artifacts are static archival records: they were not rerun during curation. Raw datasets, model weights, checkpoints, caches, credentials, local paths, raw experiment logs, and standalone course/project materials are excluded. Source-specific caveats and metric provenance are documented in each folder.

## Related project

[Semantic Feedback for LLM-Generated Optimization Code Repair](https://github.com/niu1298/semantic-feedback-for-llm-generated-optimization-code-repair)

## Copyright and Scope

This repository is a public portfolio rather than an open-source release. It contains individually completed coursework artifacts and does not grant a blanket license to course, third-party, or separately identified material. See [NOTICE.md](NOTICE.md).
