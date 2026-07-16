# GRPO VLM Adaptation with an SFT Warm Start

This curated coursework artifact compares GRPO adaptation of a vision-language model when initialized from an SFT adapter versus a cold start.

## Problem

The project examines whether supervised fine-tuning (SFT) provides a useful initialization for GRPO training on structured visual mixed-integer linear programming (MILP) summaries.

## What I implemented

- Custom parsing and partial-credit reward logic for structured MILP answers.
- A LoRA-based SFT stage with answer-only loss masking.
- Initialization logic that carries an SFT adapter into `trl.GRPOTrainer` or starts GRPO from a fresh LoRA adapter.
- Archived evaluation logic for formatting and partial-credit scoring.

## Approach

The original workflow formats image-and-text examples as structured MILP summaries, applies an optional SFT warm start, and then configures GRPO with task-specific rewards. This repository preserves the portable implementation excerpts and documents the archived coursework results; data acquisition, authentication, downloads, and training runs are intentionally omitted.

## Key archived results

| Measure | Archived value |
|---|---:|
| SFT warm-start reward | 0.4936 |
| Cold-start reward | 0.2179 |
| Held-out formatting success | 100% |
| Mean partial score | 0.667 |

The reward values are mean accuracy rewards reported over 50 logged GRPO steps in the original coursework. They are not results from a rerun of this curated artifact.

## How to inspect this artifact

Read the curated [notebook](notebooks/grpo_vlm_sft_warm_start.ipynb), then see the metric provenance and exclusions in [results/README.md](results/README.md).

## Reproducibility and limitations

This is a curated static coursework artifact. Full training was not rerun during repository curation. Original datasets, checkpoints, credentials, and large outputs are intentionally excluded. Any required external data or model access must be obtained separately.

## Folder contents

- `notebooks/grpo_vlm_sft_warm_start.ipynb` — sanitized implementation excerpts; outputs and execution history removed.
- `results/README.md` — archived metric provenance and interpretation.
- `environment.md` — archived environment notes, not a recreated runtime.
