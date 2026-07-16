# HW4 — GRPO VLM Adaptation with an SFT Warm Start

**Primary artifacts:** [Full final notebook](notebooks/hw4_grpo_vlm_sft_warm_start.ipynb) · [Full original final report (PDF)](hw4_report.pdf)

## Assignment context

This folder preserves the complete final HW4 notebook and report, with data, checkpoints, credential material, caches, and local paths removed from the public copy.

## Problem

The project examines whether supervised fine-tuning (SFT) provides a useful initialization for GRPO training on structured visual mixed-integer linear programming (MILP) summaries.

## What I implemented

- Custom parsing and partial-credit reward logic for structured MILP answers.
- A LoRA-based SFT stage with answer-only loss masking.
- Initialization logic that carries an SFT adapter into `trl.GRPOTrainer` or starts GRPO from a fresh LoRA adapter.
- Archived evaluation logic for formatting and partial-credit scoring.

## Core method / learning objective

The original workflow formats image-and-text examples as structured MILP summaries, applies an optional SFT warm start, and then configures GRPO with task-specific rewards.

## Archived evidence or evaluation

| Measure | Archived value |
|---|---:|
| SFT warm-start reward | 0.4936 |
| Cold-start reward | 0.2179 |
| Held-out formatting success | 100% |
| Mean partial score | 0.667 |

The reward values are mean accuracy rewards reported over 50 logged GRPO steps in the original coursework. They are not results from a rerun of this curated artifact.

## How to inspect

Read the complete [notebook](notebooks/hw4_grpo_vlm_sft_warm_start.ipynb), then consult the [final report](hw4_report.pdf) and [results notes](results/README.md).

## Reproducibility and limitations

This is a static archival coursework artifact. Full training was not rerun during repository curation. Original datasets, checkpoints, credentials, and large raw per-sample evaluation records are intentionally excluded. Any required external data or model access must be obtained separately.

## Folder contents

- `notebooks/hw4_grpo_vlm_sft_warm_start.ipynb` — complete final notebook with only data/cache, credential, and local-path material sanitized.
- `hw4_report.pdf` — unmodified 11-page original final report.
- `results/README.md` — archived metric provenance and interpretation.
- `environment.md` — archived environment notes, not a recreated runtime.
