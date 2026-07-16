# Archived result provenance

The files in this directory are safe, aggregate artifacts retained from the original coursework evaluation. They were not regenerated during repository curation.

| File | Provenance and purpose |
|---|---|
| `online_eval_summary.json` | Aggregate configuration-level summary containing sample size, rates, latency, and error rate; no prompts, model responses, paths, or traces are retained. |
| `hw5_agent_architecture.png` | Archived diagram of the baseline, custom-tool, and vision-enabled system paths. |
| `hw5_config_comparison.png` | Archived comparison of success rate, format rate, and mean partial score across configurations. |
| `hw5_text_vs_vision.png` | Archived, separately labeled `A_text_only` versus vision-enabled comparison for five normal tasks; it is not combined with the `A_baseline_builtin` row in `online_eval_summary.json`. |

The source defines the reported rates as task-level aggregate metrics: success rate, format rate, and mean partial score. `online_eval_summary.json` reports `A_baseline_builtin` at 0.00/0.00/0.00 and `B_vision_enhanced` at 0.40/1.00/0.40 for success/format/partial score. The supplementary figure uses a distinct `A_text_only` label and displays 0.00/1.00/0.13; it is retained separately rather than treated as the same baseline. The files do not support causal or statistical claims beyond the archived five-case comparison. Latency and error-rate fields, where present in the JSON, are preserved as reported rather than independently validated.

> This is an exploratory five-case coursework evaluation, not a statistically conclusive benchmark.
