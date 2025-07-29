import unittest
from src.models.optimization_models import optimize_with_pso, monte_carlo_simulation

class TestOptimizationModels(unittest.TestCase):
    def test_optimize_with_pso(self):
        def objective_function(x):
            return x[0]**2 + x[1]**2

        bounds = [(-5, 5), (-5, 5)]
        result = optimize_with_pso(objective_function, bounds)
        self.assertIn('x', result)
        self.assertIn('fun', result)

    def test_monte_carlo_simulation(self):
        def objective_function(x):
            return x[0]**2 + x[1]**2

        bounds = [(-5, 5), (-5, 5)]
        result = monte_carlo_simulation(objective_function, bounds, n_samples=100)
        self.assertIn('best_sample', result)
        self.assertIn('best_result', result)
        self.assertIn('samples', result)
        self.assertIn('results', result)

if __name__ == '__main__':
    unittest.main()
