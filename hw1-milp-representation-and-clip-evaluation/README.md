# HW1 — MILP Representation Foundations and CLIP Evaluation

**Primary artifacts:** [Full final notebook](notebooks/hw1_milp_representation_and_clip_evaluation.ipynb) · [Full original final report (PDF)](hw1_report.pdf)

## Assignment context

This folder preserves the final HW1 notebook and report as coursework artifacts. The notebook contains an MILP representation study and a separate Hateful Memes CLIP bonus experiment.

## Problem

The first component develops structured representations for synthetic mixed-integer linear programs (MILPs). The separate bonus component compares frozen CLIP multimodal features with simple feature baselines for Hateful Memes classification.

## What I implemented

- Synthetic generation of 180 MILP instances across six problem families.
- Constraint-matrix, bipartite-graph, and symbolic-feature representations.
- t-SNE, sparsity, degree, feature-distribution, correlation, and graph-layout analyses.
- A separate frozen-CLIP embedding workflow with logistic-regression evaluation for the Hateful Memes bonus experiment.

## Core method / learning objective

The MILP component examines how numerical, graph, and symbolic views expose optimization structure. The bonus component uses CLIP image and text embeddings as fixed multimodal features for downstream classification; it is not a CLIP-based MILP verifier.

## Archived evidence or evaluation

The archived Hateful Memes bonus comparison reports a CLIP AUROC of **0.601**. That value is specific to the bonus experiment and was not rerun during curation. Other baseline values and sample counts differ between the report and notebook, so this portfolio makes no comparison claim beyond the consistently supported CLIP AUROC.

## How to inspect

Read the complete [notebook](notebooks/hw1_milp_representation_and_clip_evaluation.ipynb), then consult the [final report](hw1_report.pdf) and [results notes](results/README.md).

## Reproducibility and limitations

This is a static archival artifact. Hateful Memes data, images, model downloads, caches, and local output paths are excluded; separately obtained licensed data and pretrained assets would be required to rerun the bonus experiment. The MILP study is a representation foundation, not a trained or evaluated verifier.

## Folder contents

- `notebooks/hw1_milp_representation_and_clip_evaluation.ipynb` — complete final notebook with only data/cache and local-path material sanitized.
- `hw1_report.pdf` — unmodified 19-page original final report.
- `results/README.md` — metric provenance and interpretation.
- `environment.md` — archived assumptions, not a recreated runtime.
