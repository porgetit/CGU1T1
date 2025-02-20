from math import sqrt

def caida_libre(h, g):
    """Calculo el tiempo que tarda un objeto en caer desde una altura h en un campo gravitatorio g.

    Args:
        h (float): Altura desde la que cae el objeto.
        g (float): Campo gravitatorio en el que cae el objeto.

    Returns:
        float: Tiempo que tarda el objeto en caer desde la altura h en el campo gravitatorio g.
    """
    return sqrt((2*h)/g)
