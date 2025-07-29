def show_equations():
    """
    Affiche les rappels des équations physiques et stochastiques en format LaTeX.
    """
    equations = """
    Équations Physiques et Stochastiques :

    1. Équation de débit :
       $$ Q = V \\times A $$
       où Q est le débit, V est la vitesse, et A est la section transversale.

    2. Équation de transfert de chaleur :
       $$ Q = m \\times c \\times \\Delta T $$
       où Q est la chaleur, m est la masse, c est la capacité thermique spécifique, et ΔT est la différence de température.

    3. Équation de Bernoulli :
       $$ P + \\frac{1}{2} \\rho v^2 + \\rho gh = \\text{constante} $$
       où P est la pression, ρ est la densité, v est la vitesse, g est l'accélération due à la gravité, et h est l'altitude.

    4. Modèle de volatilité :
       $$ \\sigma = \\sqrt{\\text{Var}(X)} $$
       où σ est la volatilité et Var(X) est la variance de X.

    5. Processus de Markov :
       $$ P(X_{n+1} = x | X_1 = x_1, \\dots, X_n = x_n) = P(X_{n+1} = x | X_n = x_n) $$
       où X_n est l'état du processus à l'étape n.
    """
    return equations
