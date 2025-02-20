def conversion_velocidades(v, option):
    """Conversor de velocidades entre km/h y m/s

    Args:
        v (float): Velocidad a convertir
        option (int): Opción de conversión (1: km/h a m/s, 2: m/s a km/h)

    Returns:
        float: Velocidad convertida
    """
    if option == 1: # km/h a m/s
        return v * 1000 / 3600
    elif option == 2: # m/s a km/h
        return v * 3600 / 1000
    else:
        return "Opción no válida"