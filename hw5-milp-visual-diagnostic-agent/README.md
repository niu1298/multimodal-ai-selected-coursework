# HW5 — MILP Visual Diagnostic Agent

**Primary artifacts:** [Full final notebook](notebooks/hw5_milp_visual_diagnostic_agent.ipynb) · [Full original final report (PDF)](hw5_report.pdf)

## Assignment context

This folder preserves the final HW5 notebook and report alongside a small reusable code extract and safe aggregate results.

## Problem

Visual MILP representations can require both structured answer formatting and model-aware interpretation. This coursework artifact compares a web-tool baseline, a custom-tool configuration, and a direct vision-enabled configuration for that task.

## What I implemented

- Structured MILP-answer parsing, normalization, formatting, and partial-credit scoring utilities.
- Agent-tool interfaces for loading configured cases and returning the required answer schema.
- A portable configuration boundary for external data rather than the original local, Colab, and sibling-coursework paths.

## Core method / learning objective

The archived design routes a query through one of three configurations: a web-tool baseline, a text agent with MILP-specific tools, or direct vision-language inference. The retained architecture diagram documents the original comparison design.

## Archived evidence or evaluation

| Configuration | Success | Format compliance | Partial score |
|---|---:|---:|---:|
| Vision-enabled | 2/5 (0.40) | 5/5 (1.00) | 2/5 (0.40) |
| Built-in baseline (`A_baseline_builtin`) | 0/5 | 0/5 | 0/5 |

> This is an exploratory five-case coursework evaluation, not a statistically conclusive benchmark.

The table uses the aggregate rows in `online_eval_summary.json`. It does not combine them with the separately labeled `A_text_only` view retained in the results folder.

## How to inspect

Start with the complete [notebook](notebooks/hw5_milp_visual_diagnostic_agent.ipynb) and [final report](hw5_report.pdf), then inspect the reusable modules in [src/](src/) and the provenance in [results/README.md](results/README.md).

## Reproducibility and limitations

No credentials, raw traces, datasets, proprietary solver licenses, or executed external environments are included. The original experiments were not rerun during curation. The source package assumes separately obtained data with image, question, and answer fields, and a VLM/tool runtime; exact external assumptions are documented in [environment.md](environment.md).

## Folder contents

- `notebooks/hw5_milp_visual_diagnostic_agent.ipynb` — complete final notebook with credential, data/cache, and local-path material sanitized.
- `hw5_report.pdf` — unmodified 14-page original final report.
- `src/` — curated parsing, scoring, report, and tool-interface modules.
- `results/` — safe aggregate JSON and selected explanatory figures.
- `environment.md` — archived assumptions; not a recreated or tested environment.
