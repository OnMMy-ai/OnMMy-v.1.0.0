import unittest, json, glob
from onmmy.utils.loader import load_module
class TestModules(unittest.TestCase):
    def test_schema(self):
        for path in glob.glob("modules/**/*.json", recursive=True):
            data = load_module(path)
            self.assertIn("name", data)
if __name__ == "__main__":
    unittest.main()