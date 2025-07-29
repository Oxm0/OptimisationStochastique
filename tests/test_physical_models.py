import unittest
from src.models.physical_models import calculate_flow_rate, calculate_heat_transfer, calculate_bernoulli

class TestPhysicalModels(unittest.TestCase):
    def test_calculate_flow_rate(self):
        self.assertEqual(calculate_flow_rate(2, 3), 6)

    def test_calculate_heat_transfer(self):
        self.assertEqual(calculate_heat_transfer(2, 3, 4), 24)

    def test_calculate_bernoulli(self):
        self.assertAlmostEqual(calculate_bernoulli(1, 1, 1, 1), 1 + 0.5 + 1*9.81, places=2)

if __name__ == '__main__':
    unittest.main()
