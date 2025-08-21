from __future__ import annotations
from ..utils.loader import load_module
from ..simulator.engine import run_module

def run(path: str):
    return run_module(load_module(path))
