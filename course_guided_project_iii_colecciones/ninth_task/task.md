# Paso 9: reporte de ventas por mes

En este paso vas a implementar funciones de **reporte** sobre la matriz de ventas.

## Objetivo

### `ventas_por_mes(matriz_ventas)`

Retorna una lista con el total de ventas de cada mes (suma de cada columna).

### `mejor_dia(matriz_ventas)`

Retorna el indice (0-based) del dia con mayores ventas, o -1 si esta vacia.

### `promedio_diario(matriz_ventas)`

Retorna el promedio de ventas por dia (total / cantidad de dias), o 0 si esta vacia.

## Pistas

- Para `ventas_por_mes`: itera columnas, suma cada columna.
- Para `mejor_dia`: usa `max(range(len(matriz)), key=lambda i: sum(matriz[i]))`.
- Para `promedio_diario`: total de la matriz / numero de filas.

## ¿Como probar?

Hace clic en **Check** y verifica que los 7 tests pasen.
