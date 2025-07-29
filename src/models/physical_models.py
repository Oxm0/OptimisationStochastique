def calculate_flow_rate(velocity, area):
    """
    Calcule le débit en fonction de la vitesse et de la section transversale.

    Args:
        velocity (float): Vitesse du fluide.
        area (float): Section transversale.

    Returns:
        float: Débit.
    """
    return velocity * area

def calculate_heat_transfer(mass, specific_heat, delta_temperature):
    """
    Calcule le transfert de chaleur en fonction de la masse, de la capacité thermique spécifique et de la différence de température.

    Args:
        mass (float): Masse du fluide.
        specific_heat (float): Capacité thermique spécifique.
        delta_temperature (float): Différence de température.

    Returns:
        float: Chaleur transférée.
    """
    return mass * specific_heat * delta_temperature

def calculate_bernoulli(pressure, density, velocity, height, gravity=9.81):
    """
    Calcule la constante de Bernoulli en fonction de la pression, de la densité, de la vitesse, de la hauteur et de la gravité.

    Args:
        pressure (float): Pression.
        density (float): Densité du fluide.
        velocity (float): Vitesse du fluide.
        height (float): Hauteur.
        gravity (float): Accélération due à la gravité (par défaut 9.81).

    Returns:
        float: Constante de Bernoulli.
    """
    return pressure + 0.5 * density * velocity**2 + density * gravity * height
