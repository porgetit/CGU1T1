import numpy as np # type: ignore

def angulo_vectores(v1, v2):
    """Calcula el ángulo entre dos vectores.

    Args:
        v1 (np.ndarray): Vector 1.
        v2 (np.ndarray): Vector 2.

    Raises:
        TypeError: Si alguno de los dos argumentos no es un array de NumPy.
        ValueError: Si los vectores no tienen la misma longitud.

    Returns:
        float: Ángulo entre los dos vectores en radianes.
    """
    if not isinstance(v1, np.ndarray) or not isinstance(v2, np.ndarray):
        raise TypeError("Ambos vectores deben ser arrays de NumPy.")
    if v1.shape != v2.shape:
        raise ValueError("Los vectores deben tener la misma longitud.")
    return np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

def producto_escalar(v1, v2):
    if not isinstance(v1, np.ndarray) or not isinstance(v2, np.ndarray):
        raise TypeError("Ambos vectores deben ser arrays de NumPy.")
    if v1.shape != v2.shape:
        raise ValueError("Los vectores deben tener la misma longitud.")
    return np.dot(v1, v2)