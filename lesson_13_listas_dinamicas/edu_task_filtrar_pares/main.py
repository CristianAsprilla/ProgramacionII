"""Filtra los numeros pares de una lista."""


def filtrar_pares(lista):
    """Retorna solo los numeros pares de una lista.

    Args:
        lista (list): lista de numeros.

    Returns:
        list: nueva lista solo con los pares.
    """
    # TODO: retorna una nueva lista con solo los numeros pares
    return []


if __name__ == "__main__":
    print(filtrar_pares([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
    print(filtrar_pares([1, 3, 5]))            # []
    print(filtrar_pares([]))                   # []
    print(filtrar_pares([0, -2, -3, 4]))       # [0, -2, 4]