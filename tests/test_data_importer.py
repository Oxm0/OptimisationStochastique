import unittest
import pandas as pd
from src.data.data_importer import import_data
import os
import tempfile

class TestDataImporter(unittest.TestCase):
    def setUp(self):
        # Créer un fichier Excel de test
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
        df = pd.DataFrame(data)
        self.excel_file = tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False)
        df.to_excel(self.excel_file.name, index=False)

        # Créer un fichier JSON de test
        self.json_file = tempfile.NamedTemporaryFile(suffix='.json', delete=False)
        df.to_json(self.json_file.name, orient='records')

    def test_import_excel(self):
        data = import_data(self.excel_file.name, file_type='excel')
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(len(data), 3)

    def test_import_json(self):
        data = import_data(self.json_file.name, file_type='json')
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(len(data), 3)

    def tearDown(self):
        # Supprimer les fichiers de test
        if os.path.exists(self.excel_file.name):
            os.remove(self.excel_file.name)
        if os.path.exists(self.json_file.name):
            os.remove(self.json_file.name)

if __name__ == '__main__':
    unittest.main()
