import unittest
import pandas as pd
from src.production.production_means import ProductionMeansManager

class TestProductionMeans(unittest.TestCase):
    def setUp(self):
        data = {
            'Process': ['C20', 'C40', 'P14'],
            'Montant': [1, 23, 37],
            'Couleur': ['#00BCFD', '#00BCFD', '#00BCFD'],
            'Unité': ['m³/h', 'm³/h', 'm³/h'],
            'Type Entité': ['PROCESS', 'PROCESS', 'PROCESS'],
            'Energie': ['Froid 2-7°C', 'Froid 2-7°C', 'Froid 2-7°C'],
            'Débit moyen': [1, 23, 37],
            'Volatilité (0-1)': [0.1, 0.1, 0.1]
        }
        self.data = pd.DataFrame(data)
        self.manager = ProductionMeansManager()

    def test_create_production_means(self):
        production_means = self.manager.create_production_means(self.data)
        self.assertIn('Froid 2-7°C', production_means)
        self.assertEqual(production_means['Froid 2-7°C']['capacity'], 61)  # 1 + 23 + 37

    def test_simulate_impact(self):
        self.manager.create_production_means(self.data)
        simulation_results = self.manager.simulate_impact(self.data)
        self.assertIn('Froid 2-7°C', simulation_results)
        self.assertEqual(simulation_results['Froid 2-7°C']['balance'], 0)  # capacity == demand

if __name__ == '__main__':
    unittest.main()
