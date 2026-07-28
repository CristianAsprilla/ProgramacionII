"""Paso 4: ordenar las notas."""


def ordenar_notas(notas, descendente=False):
    """Ordena una lista de notas.

    Args:
        notas (list): lista de notas (floats).
        descendente (bool): si True, ordena de mayor a menor. Por defecto False (ascendente).

    Returns:
        list: nueva lista ordenada.
    """
    # TODO: usa sorted() con reverse=descendente para retornar la lista ordenada
    return []


if __name__ == "__main__":
    ejemplo = [3.5, 5.0, 4.2, 2.8, 4.9]
    print(f"Ascendente: {ordenar_notas(ejemplo)}")
    print(f"Descendente: {ordenar_notas(ejemplo, descendente=True)}")
