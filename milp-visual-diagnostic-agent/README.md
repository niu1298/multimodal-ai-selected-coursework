# MILP Visual Diagnostic Agent

A tool-using vision-language agent for diagnosing visual representations of mixed-integer linear programs.

## Problem and motivation

Visual MILP representations can require both structured answer formatting and model-aware interpretation. This coursework artifact compares a web-tool baseline, a custom-tool configuration, and a direct vision-enabled configuration for that task.

## Agent workflow and system design

The archived design routes a query through one of three configurations: a web-tool baseline, a text agent with MILP-specific tools, or direct vision-language inference. The custom implementation contains utilities for parsing and scoring structured MILP answers, loading a configured case, and exposing an answer schema to a tool-using agent. The retained architecture diagram documents the original comparison design.

## What I implemented

- Structured MILP-answer parsing, normalization, formatting, and partial-credit scoring utilities.
- Agent-tool interfaces for loading configured cases and returning the required answer schema.
- A portable configuration boundary for external data rather than the original local, Colab, and sibling-coursework paths.

## Key archived evaluation results

| Configuration | Success | Format compliance | Partial score |
|---|---:|---:|---:|
| Vision-enabled | 2/5 (0.40) | 5/5 (1.00) | 2/5 (0.40) |
| Built-in baseline (`A_baseline_builtin`) | 0/5 | 0/5 | 0/5 |

> This is an exploratory five-case coursework evaluation, not a statistically conclusive benchmark.

The table uses the aggregate rows in `online_eval_summary.json`. It does not combine them with the separately labeled `A_text_only` view retained below.

## Results figures

- [Archived system design](results/hw5_agent_architecture.png) — the three comparison configurations and their tool/data flow.
- [Configuration comparison](results/hw5_config_comparison.png) — archived success, formatting, and partial-score values.
- [Supplementary text-only versus vision-enabled](results/hw5_text_vs_vision.png) — a separately labeled five-normal-task view: `A_text_only` reports 0.00 success, 1.00 formatting, and 0.13 mean partial score; it is not the `A_baseline_builtin` row used in the table above.

## How to inspect this artifact

Start with the small, reusable modules in [src/](src/), then read [results/README.md](results/README.md) for the provenance and scope of the retained aggregate artifacts.

## Configuration, data, and limitations

No credentials, raw traces, datasets, proprietary solver licenses, or executed notebooks are included. The original experiments were not rerun during curation. The source package assumes separately obtained data with image, question, and answer fields, and a VLM/tool runtime; exact external assumptions are documented in [environment.md](environment.md). No `.env.example` is included because the extracted modules do not read environment variables.

## Folder contents

- `src/` — curated parsing, scoring, report, and tool-interface modules.
- `results/` — safe aggregate JSON and selected explanatory figures.
- `environment.md` — archived assumptions; not a recreated or tested environment.
