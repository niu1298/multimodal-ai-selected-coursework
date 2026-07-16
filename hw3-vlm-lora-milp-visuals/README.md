# HW3 — LoRA Adaptation of a Vision-Language Model for MILP Visuals

**Primary artifacts:** [Full final notebook](notebooks/hw3_vlm_lora_milp_visuals.ipynb) · [Full original final report (PDF)](hw3_report.pdf)

## Assignment context

This folder preserves the final HW3 notebook and report. It is a parameter-efficient VLM adaptation project that precedes, but is not the same experiment as, the GRPO work in HW4.

## Problem

The work converts structured MILP information into visual heatmap questions and evaluates whether LoRA adaptation improves a vision-language model's categorical interpretation of those visuals.

## What I implemented

- Graph-JSON-to-MILP heatmap rendering and image-QA record construction.
- A held-out exact-match evaluation workflow.
- LoRA configuration and training for a Qwen2.5-VL-3B model.
- A categorical comparison visualization for binary and integer-variable interpretations.

## Core method / learning objective

The notebook uses parameter-efficient adaptation to connect visual MILP structure with structured answers. It establishes an adaptation-focused precursor to HW4's policy-optimization workflow.

## Archived evidence or evaluation

The final report records 30-held-out results improving binary-variable accuracy from **6.7% to 76.7%** and integer-variable accuracy from **3.3% to 53.3%** after LoRA adaptation. The saved post-training notebook output supports 23/30 and 16/30 outcomes.

The saved baseline stream and prompt/configuration context do not fully match the report's baseline presentation. These are reported archival results, not a rerun or causal benchmark claim.

## How to inspect

Read the complete [notebook](notebooks/hw3_vlm_lora_milp_visuals.ipynb), then use the [final report](hw3_report.pdf) and [results notes](results/README.md) for provenance.

## Reproducibility and limitations

This static artifact excludes image/JSONL data, caches, adapters, checkpoints, Drive paths, and runtime environments. Reproduction would require separately obtained data, a CUDA-capable environment, and model access; no training or evaluation was rerun during curation.

## Folder contents

- `notebooks/hw3_vlm_lora_milp_visuals.ipynb` — complete final notebook with data/cache and local-path material sanitized.
- `hw3_report.pdf` — unmodified 14-page original final report.
- `results/README.md` — evidence caveats and metric provenance.
- `environment.md` — archived environment assumptions.
