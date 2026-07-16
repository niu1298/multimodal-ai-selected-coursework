"""Small helpers for plotting figures and writing CSV/JSON summaries."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def save_architecture_diagram(out_path: Path) -> Path:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis("off")

    boxes = [
        (5, 11, "User query\n(sample id, image, question)"),
        (5, 9, "Agent planner / memory"),
        (5, 7, "MILP tools\nload_milp_case  |  get_milp_answer_schema"),
        (5, 5, "Vision model (Qwen2.5-VL) / text model"),
        (5, 3, "Self-check & revise"),
        (5, 1, "Final structured MILP answer"),
    ]
    for (x, y, text) in boxes:
        ax.add_patch(
            plt.Rectangle((x - 3.6, y - 0.55), 7.2, 1.1, fc="#eef5ff", ec="#205493", lw=1.5)
        )
        ax.text(x, y, text, ha="center", va="center", fontsize=10)

    arrows = [(11, 9.5), (9, 7.5), (7, 5.5), (5, 3.5), (3, 1.5)]
    for i in range(len(boxes) - 1):
        x1, y1 = boxes[i][0], boxes[i][1] - 0.55
        x2, y2 = boxes[i + 1][0], boxes[i + 1][1] + 0.55
        ax.annotate(
            "",
            xy=(x2, y2),
            xytext=(x1, y1),
            arrowprops=dict(arrowstyle="->", color="#205493", lw=1.6),
        )

    ax.text(
        5,
        12,
        "MILP Visual Diagnostic Agent",
        ha="center",
        va="bottom",
        fontsize=13,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out_path


def save_comparison_bar(
    rows: List[Dict[str, Any]],
    metrics: Iterable[str],
    out_path: Path,
    title: str = "Configuration comparison",
) -> Path:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    metrics = list(metrics)
    configs = [r["config"] for r in rows]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    width = 0.8 / max(len(metrics), 1)
    x = list(range(len(configs)))
    for i, m in enumerate(metrics):
        vals = [float(r.get(m, 0.0) or 0.0) for r in rows]
        ax.bar([xi + i * width for xi in x], vals, width=width, label=m)
    ax.set_xticks([xi + width * (len(metrics) - 1) / 2 for xi in x])
    ax.set_xticklabels(configs, rotation=10)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("score")
    ax.set_title(title)
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out_path


def save_safety_bar(comparison: List[Dict[str, Any]], out_path: Path) -> Path:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    ids = [c["prompt_id"] for c in comparison]
    before = [int(c["pass_before_mitigation"]) for c in comparison]
    after = [int(c["pass_after_mitigation"]) for c in comparison]
    x = list(range(len(ids)))
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar([xi - 0.2 for xi in x], before, width=0.4, label="before mitigation", color="#cc4444")
    ax.bar([xi + 0.2 for xi in x], after, width=0.4, label="after mitigation", color="#33aa55")
    ax.set_xticks(x)
    ax.set_xticklabels(ids, rotation=15)
    ax.set_ylim(0, 1.2)
    ax.set_ylabel("pass (1=safe)")
    ax.set_title("Safety probes: before vs after mitigation")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out_path


def write_json(obj: Any, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, default=str)
    return path
