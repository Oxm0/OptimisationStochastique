import plotly.express as px
import pandas as pd

def plot_bar_chart(data, x_column, y_column, title):
    """
    Crée un graphique en barres avec Plotly.

    Args:
        data (pd.DataFrame): DataFrame contenant les données.
        x_column (str): Colonne à utiliser pour l'axe x.
        y_column (str): Colonne à utiliser pour l'axe y.
        title (str): Titre du graphique.

    Returns:
        plotly.graph_objects.Figure: Figure du graphique.
    """
    fig = px.bar(data, x=x_column, y=y_column, title=title)
    return fig

def plot_scatter_plot(data, x_column, y_column, title):
    """
    Crée un diagramme de dispersion avec Plotly.

    Args:
        data (pd.DataFrame): DataFrame contenant les données.
        x_column (str): Colonne à utiliser pour l'axe x.
        y_column (str): Colonne à utiliser pour l'axe y.
        title (str): Titre du graphique.

    Returns:
        plotly.graph_objects.Figure: Figure du graphique.
    """
    fig = px.scatter(data, x=x_column, y=y_column, title=title)
    return fig

def plot_heatmap(data, x_column, y_column, z_column, title):
    """
    Crée une carte thermique avec Plotly.

    Args:
        data (pd.DataFrame): DataFrame contenant les données.
        x_column (str): Colonne à utiliser pour l'axe x.
        y_column (str): Colonne à utiliser pour l'axe y.
        z_column (str): Colonne à utiliser pour les valeurs z.
        title (str): Titre du graphique.

    Returns:
        plotly.graph_objects.Figure: Figure du graphique.
    """
    fig = px.density_heatmap(data, x=x_column, y=y_column, z=z_column, title=title)
    return fig

def plot_production_load(data, time_column, load_column, title, time_range):
    """
    Crée un graphique de la charge des groupes de production sur un laps de temps donné avec Plotly.

    Args:
        data (pd.DataFrame): DataFrame contenant les données.
        time_column (str): Colonne à utiliser pour l'axe des temps.
        load_column (str): Colonne à utiliser pour la charge.
        title (str): Titre du graphique.
        time_range (str): Laps de temps (1 heure, 1 jour, 1 semaine, 1 mois, 1 année).

    Returns:
        plotly.graph_objects.Figure: Figure du graphique.
    """
    # Filtrer les données en fonction du laps de temps
    if time_range == '1 heure':
        filtered_data = data[data[time_column] >= data[time_column].max() - pd.Timedelta(hours=1)]
    elif time_range == '1 jour':
        filtered_data = data[data[time_column] >= data[time_column].max() - pd.Timedelta(days=1)]
    elif time_range == '1 semaine':
        filtered_data = data[data[time_column] >= data[time_column].max() - pd.Timedelta(weeks=1)]
    elif time_range == '1 mois':
        filtered_data = data[data[time_column] >= data[time_column].max() - pd.Timedelta(days=30)]
    elif time_range == '1 année':
        filtered_data = data[data[time_column] >= data[time_column].max() - pd.Timedelta(days=365)]
    else:
        filtered_data = data

    fig = px.line(filtered_data, x=time_column, y=load_column, title=title)
    return fig
