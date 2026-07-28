# Ejercicio: transponer una matriz

La transpuesta de una matriz intercambia filas por columnas. En esta actividad vas a implementar esa operacion fundamental.

## Objetivo

Implementa `transponer(matriz)` que retorne la matriz transpuesta.

## Ejemplos

```python
>>> transponer([[1, 2, 3], [4, 5, 6]])
[[1, 4], [2, 5], [3, 6]]
```

## Pistas

- Podes usar `zip(*matriz)` que es la forma mas pythonica.
- O con listas por comprension: `[[fila[i] for fila in matriz] for i in range(len(matriz[0]))]`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 5 tests pasen.