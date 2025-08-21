from __future__ import annotations
from typing import Dict, Any
from .world import World
from ..kernel.machine_layer.process_scheduler import ProcessScheduler
from ..kernel.cognitive_layer.rule_engine import RuleEngine

def run_module(module: Dict[str, Any]) -> Dict[str, Any]:
    world = World()
    scheduler = ProcessScheduler()
    rules = RuleEngine()

    state = {"world": world.state(), "inputs": module.get("inputs", {}), "outputs": {}, "log": []}
    for step in scheduler.schedule(module.get("steps", [])):
        state = rules.apply(state, step)
        # simple executor
        if step.get("action") == "plan":
            state["outputs"]["plan"] = step.get("detail", "no-detail")
        elif step.get("action") == "task":
            state["outputs"].setdefault("tasks", []).append(step.get("detail", ""))
        elif step.get("action") == "emit":
            state["outputs"]["result"] = step.get("detail", "ok")
    return state
