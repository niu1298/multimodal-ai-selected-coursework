# HW2 — Multimodal Fusion and Contrastive Learning

**Primary artifacts:** [Full final notebook](notebooks/hw2_multimodal_fusion_contrastive_learning.ipynb) · No separate final report was identified for this homework.

## Assignment context

This is the complete final notebook from a Multimodal AI coursework assignment. It retains the original course prompts, technical narrative, and acknowledgements with permission, while excluding datasets, model files, checkpoints, local paths, and environment caches.

## Problem

The notebook studies multimodal learning across visual/audio digit classification, graph–text matching for optimization problems, fusion architectures, and contrastive alignment.

## What I implemented

- Unimodal and multimodal classification workflows for image and audio inputs.
- Graph and text encoders for matching MILP-style graph representations with natural-language descriptions.
- Early, late, tensor, and low-rank tensor fusion modules using `einsum`.
- A contrastive graph–text alignment model with retrieval-oriented evaluation and visual analysis.

## Core method / learning objective

The work contrasts feature-combination strategies with representation-alignment strategies. Fusion modules combine modality embeddings for classification, while the contrastive section maps graph and text representations into a shared space and evaluates retrieval alignment.

## Archived evidence or evaluation

The preserved notebook includes original training outputs, comparison tables, fusion figures, retrieval output, and an alignment visualization. These are retained as archival coursework evidence only.

The original notebook contains multiple result contexts and written interpretations that do not resolve to one comparable public benchmark. Accordingly, this repository does not identify a winning fusion method or make a consolidated quantitative performance claim.

## How to inspect

Read the complete [notebook](notebooks/hw2_multimodal_fusion_contrastive_learning.ipynb), then see the evaluation caveat in [results/README.md](results/README.md) and archived runtime assumptions in [environment.md](environment.md).

## Reproducibility and limitations

This is a static archival artifact and was not rerun during curation. The original work depends on external datasets, model downloads, GPU tooling, solver-backed preprocessing, and third-party libraries; none are included here.

The notebook preserves its original acknowledgements to Catherine Ning and Joshua Drossman for data-import/modification work and to Catherine for the negative-pair idea, along with its note about team discussion. Those acknowledgements are retained without reinterpretation.

## Folder contents

- `notebooks/hw2_multimodal_fusion_contrastive_learning.ipynb` — complete final notebook with only raw-data, local-path, and cache/checkpoint material sanitized.
- `results/README.md` — scope and evidence caveat.
- `environment.md` — archived, non-runnable dependency notes.
