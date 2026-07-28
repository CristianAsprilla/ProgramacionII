# Ejercicio: suma de la diagonal secundaria

La diagonal secundaria de una matriz va desde la esquina superior derecha hasta la esquina inferior izquierda.

## Objetivo

Implementa `suma_diagonal_secundaria(matriz)` que sume los elementos de la diagonal secundaria de una matriz cuadrada.

## Ejemplos

Para la matriz:

```
1 2 3
4 5 6
7 8 9
```

La diagonal secundaria es `3, 5, 7` y suma `15`.

## Pistas

- Para una matriz n x n, el elemento de la diagonal secundaria en la posicion `i` es `matriz[i][n-1-i]`.
- Itera con `for i in range(n)`.
- Podes obtener `n` con `len(matriz)`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 4 tests pasen.