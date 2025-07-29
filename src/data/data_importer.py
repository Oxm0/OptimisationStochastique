import pandas as pd
import json

def import_data(file_path, file_type='excel'):
    """
    Importe les données depuis un fichier Excel ou JSON.

    Args:
        file_path (str): Chemin vers le fichier.
        file_type (str): Type de fichier ('excel' ou 'json').

    Returns:
        pd.DataFrame: DataFrame contenant les données importées.
    """
    if file_type == 'excel':
        df = pd.read_excel(file_path)
    elif file_type == 'json':
        with open(file_path, 'r') as f:
            data = json.load(f)
        df = pd.DataFrame(data)
    else:
        raise ValueError("Type de fichier non pris en charge.")

    return df
