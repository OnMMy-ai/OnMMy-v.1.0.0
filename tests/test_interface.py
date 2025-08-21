import unittest, json
from onmmy.interface.api import run
class TestInterface(unittest.TestCase):
    def test_run_demo(self):
        result = run("modules/governance/democracy.json")
        self.assertIn("outputs", result)
if __name__ == "__main__":
    unittest.main()