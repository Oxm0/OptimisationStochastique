from scipy.optimize import dual_annealing
import numpy as np

def optimize_with_pso(objective_function, bounds):
    """
    Optimise une fonction objectif en utilisant l'optimisation par essaim de particules.

    Args:
        objective_function (function): Fonction objectif à minimiser.
        bounds (list): Liste de tuples représentant les bornes pour chaque variable.

    Returns:
        dict: Résultat de l'optimisation.
    """
    result = dual_annealing(objective_function, bounds)
    return result

def monte_carlo_simulation(objective_function, bounds, n_samples=1000):
    """
    Effectue une simulation de Monte Carlo pour optimiser une fonction objectif.

    Args:
        objective_function (function): Fonction objectif à minimiser.
        bounds (list): Liste de tuples représentant les bornes pour chaque variable.
        n_samples (int): Nombre d'échantillons à générer.

    Returns:
        dict: Résultat de la simulation.
    """
    n_dim = len(bounds)
    samples = np.random.uniform(low=[b[0] for b in bounds],
                                high=[b[1] for b in bounds],
                                size=(n_samples, n_dim))
    results = np.array([objective_function(x) for x in samples])
    best_idx = np.argmin(results)
    best_sample = samples[best_idx]
    best_result = results[best_idx]

    return {
        'best_sample': best_sample,
        'best_result': best_result,
        'samples': samples,
        'results': results
    }
