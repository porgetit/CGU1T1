import numpy as np

def alcance(vi, theta):
    """Calcula el alcance de un proyectil lanzado con una velocidad inicial y un ángulo dados.

    Args:
        vi (float): Velocidad inicial en m/s.
        theta (float): Ángulo de lanzamiento en grados.

    Returns:
        float: Alcance en metros.
    
    Raises:
        TypeError: Si vi o theta no son números.
        ValueError: Si theta no está en el rango 0°-90° o vi es negativo.
    """
    if not isinstance(vi, (int, float)) or not isinstance(theta, (int, float)):
        raise TypeError("La velocidad inicial y el ángulo deben ser números.")
    if vi < 0:
        raise ValueError("La velocidad inicial no puede ser negativa.")
    if theta < 0 or theta > 90:
        raise ValueError("El ángulo debe estar entre 0 y 90 grados para un alcance válido.")
    if vi == 0:
        return 0

    g = 9.81
    return (vi**2 * np.sin(2 * np.radians(theta))) / g


def altura_max(vi, theta):
    """Calcula la altura máxima alcanzada por un proyectil.

    Args:
        vi (float): Velocidad inicial en m/s.
        theta (float): Ángulo de lanzamiento en grados.

    Returns:
        float: Altura máxima en metros.

    Raises:
        TypeError: Si vi o theta no son números.
        ValueError: Si theta no está en el rango 0°-180° o vi es negativo.
    """
    if not isinstance(vi, (int, float)) or not isinstance(theta, (int, float)):
        raise TypeError("La velocidad inicial y el ángulo deben ser números.")
    if vi < 0:
        raise ValueError("La velocidad inicial no puede ser negativa.")
    if theta < 0 or theta > 180:
        raise ValueError("El ángulo debe estar entre 0 y 180 grados.")
    if vi == 0:
        return 0

    g = 9.81
    return (vi**2 * np.sin(np.radians(theta))**2) / (2*g)
