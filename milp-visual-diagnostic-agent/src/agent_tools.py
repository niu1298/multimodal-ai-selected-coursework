"""Optional agent-facing interfaces for externally configured MILP cases.

No dataset, ground-truth answer, absolute path, or credential is bundled with
this artifact. Offline evaluation remains in :mod:`milp_utils`.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Mapping, Protocol

try:
    from smolagents import Tool as _SmolagentsTool
except ImportError:  # pragma: no cover - supports static inspection without extras
    _SmolagentsTool = None

from .milp_utils import INSTRUCTION_SUFFIX, MILP_FIELD_NAMES


class _MissingSmolagentsTool:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        raise ImportError(
            "smolagents is required to construct MILP agent tools. "
            "Install it in a separately configured runtime."
        )


ToolBase = _SmolagentsTool or _MissingSmolagentsTool

ANSWER_SCHEMA_TEXT = (
    "Answer: Variables: <int>, Constraints: <int>, Density: low|medium|high, "
    "Binary: <int>%, Integer: <int>%, Objective: minimize|maximize"
)


class CaseLoader(Protocol):
    """Adapter supplied by an integrator for rights-cleared external data."""

    def load_case(self, split: str, sample_index: int) -> Mapping[str, Any]:
        """Return a mapping containing a question and an optional relative asset ref."""


def _safe_asset_ref(value: object) -> str | None:
    if not isinstance(value, str) or not value:
        return None
    path = Path(value)
    return None if path.is_absolute() else value


class LoadMILPCaseTool(ToolBase):
    name = "load_milp_case"
    description = (
        "Load one externally configured MILP case by split and zero-based sample index. "
        "Returns a case ID, question, and only a relative asset reference when available."
    )
    inputs = {
        "split": {
            "type": "string",
            "description": "Dataset split supplied by the configured case loader.",
            "nullable": True,
        },
        "sample_index": {
            "type": "integer",
            "description": "Zero-based sample index into the configured split.",
            "nullable": True,
        },
    }
    output_type = "object"

    def __init__(self, case_loader: CaseLoader) -> None:
        super().__init__()
        self.case_loader = case_loader

    def forward(self, split: str = "test", sample_index: int = 0) -> Dict[str, Any]:
        index = int(sample_index)
        if index < 0:
            raise ValueError("sample_index must be non-negative")
        row = self.case_loader.load_case(split, index)
        result: Dict[str, Any] = {
            "case_id": f"{split}:{index}",
            "question": str(row.get("question", "")),
        }
        asset_ref = _safe_asset_ref(row.get("image"))
        if asset_ref is not None:
            result["asset_ref"] = asset_ref
        return result


class GetMILPAnswerSchemaTool(ToolBase):
    name = "get_milp_answer_schema"
    description = "Return the structured MILP answer schema required by the parser."
    inputs: Dict[str, Any] = {}
    output_type = "object"

    def forward(self) -> Dict[str, Any]:
        return {
            "schema": ANSWER_SCHEMA_TEXT,
            "fields": MILP_FIELD_NAMES,
            "instruction_suffix": INSTRUCTION_SUFFIX,
        }


def build_milp_toolset(case_loader: CaseLoader) -> List[ToolBase]:
    """Build the public, inference-only tools for an injected data adapter."""
    return [LoadMILPCaseTool(case_loader), GetMILPAnswerSchemaTool()]
