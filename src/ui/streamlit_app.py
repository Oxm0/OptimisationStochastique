import streamlit as st
import pandas as pd
import plotly.express as px
from src.data.data_importer import import_data
from src.models.optimization_models import optimize_with_pso, monte_carlo_simulation
from src.visualization.plotly_plots import plot_bar_chart, plot_scatter_plot, plot_heatmap, plot_production_load
from src.utils.equations import show_equations
from src.production.production_means import ProductionMeansManager

def main():
    st.title("Application d'Optimisation Stochastique")

    # Sidebar pour la navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Aller à", ["Importation des Données", "Optimisation", "Visualisation", "Équations", "Moyens de Production"])

    if page == "Importation des Données":
        st.header("Importation des Données")
        uploaded_file = st.file_uploader("Choisissez un fichier", type=["xlsx", "json"])

        if uploaded_file is not None:
            if uploaded_file.name.endswith('.xlsx'):
                data = import_data(uploaded_file, file_type='excel')
            elif uploaded_file.name.endswith('.json'):
                data = import_data(uploaded_file, file_type='json')

            st.write("Données importées avec succès :")
            st.dataframe(data)

            # Sauvegarder les données dans la session de Streamlit
            st.session_state.data = data

    elif page == "Optimisation":
        st.header("Optimisation")

        if 'data' in st.session_state:
            data = st.session_state.data

            st.subheader("Optimisation par Essaim de Particules (PSO)")
            # Exemple de fonction objectif et de bornes (à adapter selon les besoins)
            def objective_function(x):
                return x[0]**2 + x[1]**2  # Exemple de fonction à minimiser

            bounds = [(-5, 5), (-5, 5)]  # Exemple de bornes
            result = optimize_with_pso(objective_function, bounds)
            st.write("Résultat de l'optimisation PSO :")
            st.write(result)

            st.subheader("Tir de Monte Carlo")
            n_samples = st.slider("Nombre d'échantillons", 100, 10000, 1000)
            result = monte_carlo_simulation(objective_function, bounds, n_samples=n_samples)
            st.write("Résultat de la simulation de Monte Carlo :")
            st.write(result)

        else:
            st.warning("Veuillez d'abord importer des données.")

    elif page == "Visualisation":
        st.header("Visualisation")

        if 'data' in st.session_state:
            data = st.session_state.data

            # Exemple de visualisation : histogramme des débits moyens
            st.subheader("Histogramme des débits moyens")
            fig = plot_bar_chart(data, 'Process', 'Débit moyen', 'Histogramme des débits moyens')
            st.plotly_chart(fig)

            # Exemple de visualisation : diagramme de dispersion
            st.subheader("Diagramme de dispersion")
            fig = plot_scatter_plot(data, 'Débit moyen', 'Volatilité (0-1)', 'Diagramme de dispersion')
            st.plotly_chart(fig)

            # Exemple de visualisation : carte thermique
            st.subheader("Carte thermique")
            fig = plot_heatmap(data, 'Process', 'Energie', 'Débit moyen', 'Carte thermique')
            st.plotly_chart(fig)

            # Exemple de visualisation : charge des groupes de production
            st.subheader("Charge des groupes de production")
            time_range = st.selectbox("Laps de temps", ["1 heure", "1 jour", "1 semaine", "1 mois", "1 année"])
            fig = plot_production_load(data, 'Time', 'Load', 'Charge des groupes de production', time_range)
            st.plotly_chart(fig)

        else:
            st.warning("Veuillez d'abord importer des données.")

    elif page == "Équations":
        st.header("Équations Physiques et Stochastiques")
        equations = show_equations()
        st.markdown(equations)

    elif page == "Moyens de Production":
        st.header("Création des Moyens de Production")

        if 'data' in st.session_state:
            data = st.session_state.data

            st.subheader("Créer des moyens de production")
            production_manager = ProductionMeansManager()
            production_means = production_manager.create_production_means(data)
            st.write("Moyens de production créés :")
            st.json(production_means)

            # Exemple de simulation d'impact
            st.subheader("Simuler l'impact des moyens de production")
            if st.button("Simuler l'impact"):
                st.write("Simulation de l'impact des moyens de production...")
                simulation_results = production_manager.simulate_impact(data)
                st.write("Résultats de la simulation :")
                st.json(simulation_results)

        else:
            st.warning("Veuillez d'abord importer des données.")

if __name__ == "__main__":
    main()
