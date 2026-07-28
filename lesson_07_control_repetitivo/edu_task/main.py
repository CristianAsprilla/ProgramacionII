def fibonacci(n: int) -> list[int]:
    """Devuelve los primeros n números de Fibonacci.

    Ejemplos:
    >>> fibonacci(0)
    []
    >>> fibonacci(1)
    [0]
    >>> fibonacci(5)
    [0, 1, 1, 2, 3]

    Si n es negativo, lanzar ValueError con el mensaje "N no puede ser negativo".
    """
    # TODO: construye y devuelve los primeros n números de Fibonacci
    return []


def imprimir_fibonacci(n: int) -> None:
    """Imprime la serie de Fibonacci de tamaño n, separada por espacios."""
    print(*fibonacci(n))
