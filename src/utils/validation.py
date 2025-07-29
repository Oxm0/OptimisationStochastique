def validate_data(data):
    """
    Valide les données importées.

    Args:
        data (pd.DataFrame): DataFrame contenant les données à valider.

    Returns:
        bool: True si les données sont valides, False sinon.
    """
    required_columns = ['Process', 'Montant', 'Couleur', 'Unité', 'Type Entité', 'Energie', 'Débit moyen', 'Volatilité (0-1)']
    for column in required_columns:
        if column not in data.columns:
            return False
    return True
