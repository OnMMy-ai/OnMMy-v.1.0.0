from __future__ import annotations
import json, pathlib
from typing import Any, Dict

def load_module(path: str) -> Dict[str, Any]:
    p = pathlib.Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Module not found: {path}")
    with p.open("r", encoding="utf-8") as f:
        data = json.load(f)
    # Minimal schema check
    for key in ["name", "category", "inputs", "outputs", "steps"]:
        if key not in data:
            raise ValueError(f"Module schema missing key: {key}")
    return data
