"""Calcula el factorial de un numero (version modular)."""


def factorial_modular(n):
    """Calcula n! usando recursion o bucle.

    Args:
        n (int): numero entero no negativo.

    Returns:
        int: n! (factorial de n).
    """
    # TODO: implementa el factorial de forma modular
    return 1


if __name__ == "__main__":
    print(factorial_modular(5))   # 120
    print(factorial_modular(0))   # 1
    print(factorial_modular(1))   # 1
    print(factorial_modular(10))  # 3628800