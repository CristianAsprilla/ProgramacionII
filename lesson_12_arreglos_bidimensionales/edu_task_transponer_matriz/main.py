"""Transpone una matriz (intercambia filas y columnas)."""


def transponer(matriz):
    """Retorna la transpuesta de una matriz.

    Args:
        matriz (list): lista de listas.

    Returns:
        list: matriz transpuesta.
    """
    # TODO: construye la transpuesta intercambiando filas y columnas
    return []


if __name__ == "__main__":
    m = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    # Transpuesta: [[1, 4], [2, 5], [3, 6]]
    for fila in transponer(m):
        print(fila)