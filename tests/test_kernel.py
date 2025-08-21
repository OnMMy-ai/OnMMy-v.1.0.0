import unittest
from onmmy.kernel.machine_layer.cpu_manager import CPUManager
class TestKernel(unittest.TestCase):
    def test_cpu(self):
        self.assertIn("cores", CPUManager().info())
if __name__ == "__main__":
    unittest.main()