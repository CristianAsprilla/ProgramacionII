"""Clasifica una edad en una categoria."""


def clasificar_edad(edad):
    """Clasifica una edad en una categoria.

    Args:
        edad (int): edad en anos.

    Returns:
        str: 'nino' (0-12), 'adolescente' (13-17), 'adulto' (18-64),
             'adulto mayor' (65+).
    """
    # TODO: clasifica segun el rango de edad
    return ""


if __name__ == "__main__":
    print(clasificar_edad(8))    # nino
    print(clasificar_edad(15))   # adolescente
    print(clasificar_edad(30))   # adulto
    print(clasificar_edad(70))   # adulto mayor