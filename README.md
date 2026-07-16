# Multimodal AI — Coursework Portfolio (HW1–HW5)

This repository is a curated, end-to-end portfolio of five Multimodal AI homework assignments. Together, they trace a progression from visual verification and multimodal representation learning to parameter-efficient VLM adaptation, reinforcement learning, and tool-using agents.

| Homework | Focus | Methods | Archived evidence |
|---|---|---|---|
| [HW1](hw1-milp-representation-and-clip-evaluation/) | MILP representation foundations and a separate CLIP bonus evaluation | Synthetic MILP matrices, bipartite graphs, symbolic features, visualization; frozen CLIP embeddings | CLIP AUROC **0.601** for the Hateful Memes bonus experiment only |
| [HW2](hw2-multimodal-fusion-contrastive-learning/) | Multimodal fusion and contrastive learning | Early/late/tensor fusion and graph–text representation alignment | Complete archived notebook; no single reconciled public metric claim |
| [HW3](hw3-vlm-lora-milp-visuals/) | LoRA adaptation of a VLM for MILP visuals | Image-QA data construction, LoRA adaptation, held-out evaluation | Reported 30-held-out results: binary **6.7% → 76.7%**; integer **3.3% → 53.3%** |
| [HW4](hw4-grpo-vlm-sft-warm-start/) | GRPO VLM adaptation with an SFT warm start | LoRA SFT, task-specific reward design, GRPO | Archived warm-start reward **0.4936** vs. cold-start reward **0.2179** |
| [HW5](hw5-milp-visual-diagnostic-agent/) | MILP visual diagnostic agent | Tool-using VLM workflow and structured MILP reasoning | Exploratory five-case comparison: vision-enabled **2/5** vs. built-in baseline **0/5** |

## Learning progression

visual verification → multimodal representation learning → VLM adaptation → policy optimization → tool-using reasoning

## Curation note

Each homework folder preserves a complete final notebook and, where a separate final report exists, the original PDF. The artifacts are static archival records: they were not rerun during curation. Raw datasets, model weights, checkpoints, caches, credentials, local paths, raw experiment logs, and standalone course/project materials are excluded. Source-specific caveats and metric provenance are documented in each folder.

## Related project

[Semantic Feedback for LLM-Generated Optimization Code Repair](https://github.com/niu1298/semantic-feedback-for-llm-generated-optimization-code-repair)

## Copyright and Scope

This repository is a public portfolio rather than an open-source release. It contains individually completed coursework artifacts and does not grant a blanket license to course, third-party, or separately identified material. See [NOTICE.md](NOTICE.md).
