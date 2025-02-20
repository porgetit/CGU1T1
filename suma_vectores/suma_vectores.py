import numpy as np # type: ignore

def suma_vectores(v1, v2):
    """Suma dos vectores.

    Args:
        v1 (np.ndarray): Vector 1.
        v2 (np.ndarray): Vector 2.

    Raises:
        TypeError: Si alguno de los dos argumentos no es un array de NumPy.
        ValueError: Si los vectores no tienen la misma longitud.

    Returns:
        np.ndarray: Vector resultante de la suma.
    """
    if not isinstance(v1, np.ndarray) or not isinstance(v2, np.ndarray):
        raise TypeError("Ambos vectores deben ser arrays de NumPy.")
    if v1.shape != v2.shape:
        raise ValueError("Los vectores deben tener la misma longitud.")
    return np.add(v1, v2)
