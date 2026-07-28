"""Genera una lista de numeros primos hasta N."""


def primos_hasta(n):
    """Retorna todos los primos menores o iguales a n.

    Args:
        n (int): limite superior.

    Returns:
        list: lista de primos desde 2 hasta n.
    """
    # TODO: usa es_primo() o un bucle para generar la lista
    return []


if __name__ == "__main__":
    print(primos_hasta(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
    print(primos_hasta(10))  # [2, 3, 5, 7]
    print(primos_hasta(1))   # []