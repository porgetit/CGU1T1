def calculo_desplazamiento(vi, a, t):
    """Calcula el desplazamiento de un objeto en movimiento rectilíneo uniformemente acelerado.

    Args:
        vi (int, float): Velocidad inicial del objeto.
        a (int, float): Aceleración del objeto.
        t (int, float): Tiempo que ha transcurrido.

    Raises:
        ValueError: Todos los valores deben ser números reales.

    Returns:
        int, float: Desplazamiento del objeto.
    """
    if not isinstance(vi, (int, float)) or not isinstance(a, (int, float)) or not isinstance(t, (int, float)):
        raise ValueError("Todos los valores deben ser números reales.")
    return vi*t + 0.5*a*t**2
