class ProductionMeansManager:
    def __init__(self):
        self.production_means = {}

    def create_production_means(self, data):
        """
        Crée des moyens de production pour répondre aux besoins des processus.

        Args:
            data (pd.DataFrame): DataFrame contenant les données des processus.

        Returns:
            dict: Dictionnaire contenant les moyens de production créés.
        """
        production_means = {}

        # Exemple : créer des moyens de production pour chaque type d'énergie
        for energy in data['Energie'].unique():
            production_means[energy] = {
                'type': energy,
                'capacity': data[data['Energie'] == energy]['Débit moyen'].sum(),
                'units': []
            }

            # Ajouter des unités de production en fonction des besoins
            for _, row in data[data['Energie'] == energy].iterrows():
                production_means[energy]['units'].append({
                    'process': row['Process'],
                    'debit': row['Débit moyen'],
                    'volatility': row['Volatilité (0-1)']
                })

        self.production_means = production_means
        return production_means

    def simulate_impact(self, data):
        """
        Simule l'impact des moyens de production sur les processus.

        Args:
            data (pd.DataFrame): DataFrame contenant les données des processus.

        Returns:
            dict: Résultats de la simulation.
        """
        simulation_results = {}

        # Exemple de simulation
        for energy, means in self.production_means.items():
            total_capacity = means['capacity']
            total_demand = data[data['Energie'] == energy]['Débit moyen'].sum()
            simulation_results[energy] = {
                'capacity': total_capacity,
                'demand': total_demand,
                'balance': total_capacity - total_demand
            }

        return simulation_results
