"""Paso 9: reporte de ventas por mes."""


def ventas_por_mes(matriz_ventas):
    """Calcula el total de ventas por mes.

    Args:
        matriz_ventas (list): matriz (lista de listas) con ventas por dia.
            Cada fila es un dia, cada columna es un mes. Ej: 4 dias x 3 meses.

    Returns:
        list: lista con el total de cada mes.
    """
    # TODO: para cada columna, suma los valores. Retorna una lista con esos totales
    return []


def mejor_dia(matriz_ventas):
    """Encuentra el dia con mayores ventas totales.

    Args:
        matriz_ventas (list): matriz de ventas.

    Returns:
        int: indice del mejor dia (0-based), o -1 si la matriz esta vacia.
    """
    # TODO: si la matriz esta vacia retorna -1. Si no, retorna el indice de la fila con mayor suma
    return -1


def promedio_diario(matriz_ventas):
    """Calcula el promedio de ventas por dia.

    Args:
        matriz_ventas (list): matriz de ventas.

    Returns:
        float: promedio de los promedios diarios, o 0 si la matriz esta vacia.
    """
    # TODO: retorna el promedio de los promedios diarios (suma los promedios de cada fila, dividido por la cantidad de dias)
    # Para [[10, 20], [30, 40]]: promedios por dia son 15 y 35, promedio final = (15+35)/2 = 25
    return 0.0


if __name__ == "__main__":
    ejemplo = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]]
    print(f"Ventas por mes: {ventas_por_mes(ejemplo)}")
    print(f"Mejor dia: {mejor_dia(ejemplo)}")
    print(f"Promedio diario: {promedio_diario(ejemplo)}")
