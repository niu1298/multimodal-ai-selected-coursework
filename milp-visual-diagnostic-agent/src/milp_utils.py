"""Portable parsing and offline scoring helpers for structured MILP answers.

These functions are static implementation excerpts from the coursework
artifact. They do not load a dataset, call a model, or expose labels to an
agent-facing tool.
"""

from __future__ import annotations

import re
from typing import Any, Dict, Optional

MILP_FIELD_NAMES = [
    "Variables",
    "Constraints",
    "Density",
    "Binary",
    "Integer",
    "Objective",
]

INSTRUCTION_SUFFIX = (
    "\n\nAnswer in this exact format on the final line:\n"
    "Answer: Variables: <int>, Constraints: <int>, Density: low|medium|high, "
    "Binary: <int>%, Integer: <int>%, Objective: minimize|maximize"
)

MILP_LINE_RE = re.compile(
    r"(Variables:\s*\d+,\s*Constraints:\s*\d+,\s*Density:\s*\w+,\s*"
    r"Binary:\s*[\d.]+%,\s*Integer:\s*[\d.]+%,\s*Objective:\s*\w+)",
    re.IGNORECASE | re.DOTALL,
)


def extract_answer(text: str) -> Optional[str]:
    """Pull a single-line MILP answer string out of model output."""
    text = (text or "").strip()
    match = re.search(r"Answer:\s*(.+)", text, re.IGNORECASE | re.DOTALL)
    if match:
        rest = match.group(1).strip()
        for line in rest.splitlines():
            line = line.strip()
            if line:
                return line
        return rest
    m2 = MILP_LINE_RE.search(text)
    if m2:
        return m2.group(1).strip()
    return None


def parse_milp_fields(s: Optional[str]) -> Optional[Dict[str, str]]:
    """Parse the six fields in the documented structured answer format."""
    if not s:
        return None
    match = re.search(
        r"Variables:\s*(\d+),\s*Constraints:\s*(\d+),\s*Density:\s*(\w+),\s*"
        r"Binary:\s*([\d.]+%),\s*Integer:\s*([\d.]+%),\s*Objective:\s*(\w+)",
        s,
        re.I | re.DOTALL,
    )
    if not match:
        return None
    return dict(zip(MILP_FIELD_NAMES, list(match.groups())))


def normalize_field_value(value: str) -> str:
    return str(value).strip().lower()


def milp_per_field_correct(
    prediction: Optional[str], ground_truth: str
) -> Optional[Dict[str, bool]]:
    """Compare parsed prediction fields with an evaluator-supplied reference."""
    predicted_fields = parse_milp_fields(prediction)
    reference_fields = parse_milp_fields(ground_truth)
    if not predicted_fields or not reference_fields:
        return None
    return {
        field: normalize_field_value(predicted_fields[field])
        == normalize_field_value(reference_fields[field])
        for field in MILP_FIELD_NAMES
    }


def format_reward(text: str) -> float:
    """Return 1.0 for a parseable answer and 0.0 otherwise."""
    return 1.0 if parse_milp_fields(extract_answer(text)) else 0.0


def accuracy_reward(text: str, ground_truth: str) -> float:
    """Return partial credit across the six documented MILP fields."""
    field_hits = milp_per_field_correct(extract_answer(text), ground_truth)
    if field_hits is None:
        return 0.0
    return sum(field_hits.values()) / len(MILP_FIELD_NAMES)


def score_milp_answer(model_output: str, ground_truth: str) -> Dict[str, Any]:
    """Offline evaluator helper; do not register this with an agent toolset."""
    prediction = extract_answer(model_output)
    parsed_prediction = parse_milp_fields(prediction)
    parsed_ground_truth = parse_milp_fields(ground_truth)
    field_hits = milp_per_field_correct(prediction, ground_truth)
    partial_score = (
        0.0
        if field_hits is None
        else sum(field_hits.values()) / len(MILP_FIELD_NAMES)
    )
    exact = prediction is not None and " ".join(prediction.lower().split()) == " ".join(
        (ground_truth or "").lower().split()
    )
    return {
        "extracted_answer": prediction,
        "has_format": parsed_prediction is not None,
        "exact": exact,
        "partial_score": partial_score,
        "field_hits": field_hits,
        "parsed_prediction": parsed_prediction,
        "parsed_ground_truth": parsed_ground_truth,
    }
