"""Calcula estadisticas de notas de una clase."""


def resumen_notas(notas):
    """Calcula promedio, maximo y minimo de una matriz de notas.

    Args:
        notas (list): lista de listas (matriz) con notas por estudiante.

    Returns:
        dict: con keys 'promedio', 'maximo', 'minimo'.
    """
    # TODO: aplana la matriz, calcula las 3 estadisticas y retorna el diccionario
    return {"promedio": 0.0, "maximo": 0.0, "minimo": 0.0}


if __name__ == "__main__":
    clase = [[4.0, 3.5, 5.0], [2.0, 4.5, 3.0], [5.0, 4.0, 4.5]]
    print(resumen_notas(clase))
