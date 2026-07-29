"""Ordena fechas de lenguajes de programacion leidas desde stdin."""


def leer_anos():
    """Lee anos desde stdin hasta encontrar FIN.

    Returns:
        list: lista de anos (int).
    """
    anos = []
    while True:
        linea = input().strip()
        if linea == "FIN":
            break
        if linea:
            anos.append(int(linea))
    return anos


def ordenar_anos(anos):
    """Ordena una lista de anos de menor a mayor.

    Args:
        anos (list): lista de anos (int).

    Returns:
        list: lista ordenada de menor a mayor.
    """
    return sorted(anos)


def formatear(anos):
    """Formatea una lista de anos como string separado por comas.

    Args:
        anos (list): lista de anos.

    Returns:
        str: anos separados por ", ".
    """
    return ", ".join(str(a) for a in anos)


if __name__ == "__main__":
    anos = leer_anos()
    anos_ordenados = ordenar_anos(anos)
    print(formatear(anos_ordenados))
