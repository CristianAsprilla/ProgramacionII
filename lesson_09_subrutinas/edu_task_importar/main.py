def es_primo(n: int) -> bool:
    """Devuelve True si n es primo, False en caso contrario.

    Un número primo es mayor que 1 y solo es divisible por 1 y por sí mismo.
    Ejemplos:
    >>> es_primo(2)
    True
    >>> es_primo(7)
    True
    >>> es_primo(1)
    False
    >>> es_primo(9)
    False
    """
    # TODO: devuelve True si n es primo, False si no
    return False


def lista_primos(n: int) -> list[int]:
    """Devuelve una lista con todos los primos hasta n (inclusive).

    Ejemplos:
    >>> lista_primos(10)
    [2, 3, 5, 7]
    >>> lista_primos(2)
    [2]
    >>> lista_primos(1)
    []
    """
    # TODO: usa es_primo para construir y devolver la lista de primos hasta n
    return []


if __name__ == "__main__":
    print(es_primo(17))
    print(lista_primos(20))