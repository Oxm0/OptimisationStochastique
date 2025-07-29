import numpy as np

class MarkovProcess:
    def __init__(self, transition_matrix, initial_state):
        """
        Initialise un processus de Markov.

        Args:
            transition_matrix (np.ndarray): Matrice de transition.
            initial_state (int): État initial.
        """
        self.transition_matrix = transition_matrix
        self.current_state = initial_state

    def step(self):
        """
        Effectue une étape du processus de Markov.

        Returns:
            int: Nouvel état.
        """
        self.current_state = np.random.choice(
            len(self.transition_matrix),
            p=self.transition_matrix[self.current_state]
        )
        return self.current_state

    def simulate(self, n_steps):
        """
        Simule le processus de Markov sur un certain nombre d'étapes.

        Args:
            n_steps (int): Nombre d'étapes à simuler.

        Returns:
            list: Liste des états visités.
        """
        states = []
        for _ in range(n_steps):
            states.append(self.current_state)
            self.step()
        return states
