"""Calcula la mediana de una lista de notas."""


def mediana(notas):
    """Calcula la mediana de una lista de notas (escala 1.0-5.0).

    Args:
        notas (list): lista de notas (numeros float).

    Returns:
        float: la mediana, o None si la lista esta vacia.
    """
    # TODO: ordena la lista y devuelve el elemento central (o el promedio de los dos centrales si son pares)
    notas_ordenadas = sorted(notas)
    return None


if __name__ == "__main__":
    print(mediana([3.0, 4.0, 5.0, 2.0, 4.5]))
