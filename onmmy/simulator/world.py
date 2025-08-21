class World:
    def __init__(self):
        self._state = {"time": "T0", "env": "sandbox"}
    def state(self):
        return dict(self._state)
