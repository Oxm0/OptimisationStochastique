import unittest
import numpy as np
from src.models.stochastic_models import MarkovProcess

class TestStochasticModels(unittest.TestCase):
    def test_markov_process(self):
        transition_matrix = np.array([[0.7, 0.3], [0.4, 0.6]])
        process = MarkovProcess(transition_matrix, initial_state=0)
        states = process.simulate(10)
        self.assertEqual(len(states), 10)

if __name__ == '__main__':
    unittest.main()
