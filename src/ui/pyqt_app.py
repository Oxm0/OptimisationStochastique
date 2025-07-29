import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTabWidget, QFileDialog, QMessageBox
from PyQt6.QtCore import Qt
import pandas as pd
from src.data.data_importer import import_data
from src.models.optimization_models import optimize_with_pso, monte_carlo_simulation
from src.visualization.plotly_plots import plot_bar_chart, plot_scatter_plot, plot_heatmap, plot_production_load
from src.utils.equations import show_equations
from src.production.production_means import ProductionMeansManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application d'Optimisation Stochastique")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget()
        self.layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.tabs.addTab(self.tab1, "Importation des Données")
        self.tabs.addTab(self.tab2, "Optimisation")
        self.tabs.addTab(self.tab3, "Visualisation")
        self.tabs.addTab(self.tab4, "Équations")
        self.tabs.addTab(self.tab5, "Moyens de Production")

        self.layout.addWidget(self.tabs)
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

        self.init_tab1()
        self.init_tab2()
        self.init_tab3()
        self.init_tab4()
        self.init_tab5()

    def init_tab1(self):
        layout = QVBoxLayout()
        self.import_button = QPushButton("Importer un fichier Excel ou JSON")
        self.import_button.clicked.connect(self.import_file)
        layout.addWidget(self.import_button)
        self.tab1.setLayout(layout)

    def init_tab2(self):
        layout = QVBoxLayout()
        self.optimize_pso_button = QPushButton("Optimiser avec PSO")
        self.optimize_pso_button.clicked.connect(self.optimize_with_pso)
        layout.addWidget(self.optimize_pso_button)

        self.optimize_mc_button = QPushButton("Optimiser avec Monte Carlo")
        self.optimize_mc_button.clicked.connect(self.optimize_with_mc)
        layout.addWidget(self.optimize_mc_button)
        self.tab2.setLayout(layout)

    def init_tab3(self):
        layout = QVBoxLayout()
        self.plot_bar_button = QPushButton("Histogramme des débits moyens")
        self.plot_bar_button.clicked.connect(self.plot_bar_chart)
        layout.addWidget(self.plot_bar_button)

        self.plot_scatter_button = QPushButton("Diagramme de dispersion")
        self.plot_scatter_button.clicked.connect(self.plot_scatter_plot)
        layout.addWidget(self.plot_scatter_button)

        self.plot_heatmap_button = QPushButton("Carte thermique")
        self.plot_heatmap_button.clicked.connect(self.plot_heatmap)
        layout.addWidget(self.plot_heatmap_button)

        self.plot_production_button = QPushButton("Charge des groupes de production")
        self.plot_production_button.clicked.connect(self.plot_production_load)
        layout.addWidget(self.plot_production_button)
        self.tab3.setLayout(layout)

    def init_tab4(self):
        layout = QVBoxLayout()
        self.equations_button = QPushButton("Afficher les équations")
        self.equations_button.clicked.connect(self.show_equations)
        layout.addWidget(self.equations_button)
        self.tab4.setLayout(layout)

    def init_tab5(self):
        layout = QVBoxLayout()
        self.production_button = QPushButton("Créer des moyens de production")
        self.production_button.clicked.connect(self.create_production_means)
        layout.addWidget(self.production_button)

        self.simulate_impact_button = QPushButton("Simuler l'impact des moyens de production")
        self.simulate_impact_button.clicked.connect(self.simulate_impact)
        layout.addWidget(self.simulate_impact_button)
        self.tab5.setLayout(layout)

    def import_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "", "Excel Files (*.xlsx *.xls);;JSON Files (*.json)")
        if file_path:
            if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                self.data = import_data(file_path, file_type='excel')
            elif file_path.endswith('.json'):
                self.data = import_data(file_path, file_type='json')

            QMessageBox.information(self, "Succès", "Données importées avec succès.")

    def optimize_with_pso(self):
        if hasattr(self, 'data'):
            def objective_function(x):
                return x[0]**2 + x[1]**2  # Exemple de fonction à minimiser

            bounds = [(-5, 5), (-5, 5)]  # Exemple de bornes
            result = optimize_with_pso(objective_function, bounds)
            QMessageBox.information(self, "Résultat PSO", str(result))
        else:
            QMessageBox.warning(self, "Avertissement", "Veuillez d'abord importer un fichier.")

    def optimize_with_mc(self):
        if hasattr(self, 'data'):
            def objective_function(x):
                return x[0]**2 + x[1]**2  # Exemple de fonction à minimiser

            bounds = [(-5, 5), (-5, 5)]  # Exemple de bornes
            result = monte_carlo_simulation(objective_function, bounds)
            QMessageBox.information(self, "Résultat Monte Carlo", str(result))
        else:
            QMessageBox.warning(self, "Avertissement", "Veuillez d'abord importer un fichier.")

    def plot_bar_chart(self):
        if hasattr(self, 'data'):
            fig = plot_bar_chart(self.data, 'Process', 'Débit moyen', 'Histogramme des débits moyens')
            fig.show()
        else:
            QMessageBox.warning(self, "Avertissement", "Veuillez d'abord importer un fichier.")

    def plot_scatter_plot(self):
        if hasattr(self, 'data'):
            fig = plot_scatter_plot(self.data, 'Débit moyen', 'Volatilité (0-1)', 'Diagramme de dispersion')
            fig.show()
        else:
            QMessageBox.warning(self, "Avertissement", "Veuillez d'abord importer un fichier.")

    def plot_heatmap(self):
        if hasattr(self, 'data'):
            fig = plot_heatmap(self.data, 'Process', 'Energie', 'Débit moyen', 'Carte thermique')
            fig.show()
        else:
            QMessageBox.warning(self, "Avertissement", "Veuillez d'abord importer un fichier.")

    def plot_production_load(self):
        if hasattr(self, 'data'):
            fig = plot_production_load(self.data, 'Time', 'Load', 'Charge des groupes de production', '1 jour')
            fig.show()
        else:
            QMessageBox.warning(self, "Avertissement", "Veuillez d'abord importer un fichier.")

    def show_equations(self):
        equations = show_equations()
        QMessageBox.information(self, "Équations", equations)

    def create_production_means(self):
        if hasattr(self, 'data'):
            production_manager = ProductionMeansManager()
            production_means = production_manager.create_production_means(self.data)
            QMessageBox.information(self, "Moyens de Production", str(production_means))
        else:
            QMessageBox.warning(self, "Avertissement", "Veuillez d'abord importer un fichier.")

    def simulate_impact(self):
        if hasattr(self, 'data'):
            production_manager = ProductionMeansManager()
            production_means = production_manager.create_production_means(self.data)
            simulation_results = production_manager.simulate_impact(self.data)
            QMessageBox.information(self, "Simulation", f"Résultats de la simulation :\n{simulation_results}")
        else:
            QMessageBox.warning(self, "Avertissement", "Veuillez d'abord importer un fichier.")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
