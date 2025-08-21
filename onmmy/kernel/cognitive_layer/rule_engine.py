class RuleEngine:
    def apply(self, state, step):
        # Very simple rule: attach audit trail
        state.setdefault("log", []).append({"action": step.get("action"), "by": step.get("by","system")})
        return state
