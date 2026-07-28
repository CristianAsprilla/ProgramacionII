"""Suma la diagonal secundaria de una matriz cuadrada."""


def suma_diagonal_secundaria(matriz):
    """Suma los elementos de la diagonal secundaria de una matriz cuadrada.

    La diagonal secundaria va desde la esquina superior derecha
    hasta la esquina inferior izquierda.

    Args:
        matriz (list): lista de listas de igual tamano.

    Returns:
        int o float: suma de la diagonal secundaria.
    """
    # TODO: suma los elementos matriz[i][n-1-i] para i en range(n)
    return 0


if __name__ == "__main__":
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    # diagonal secundaria: 3 + 5 + 7 = 15
    print(suma_diagonal_secundaria(m))