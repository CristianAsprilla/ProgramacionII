# Ejercicio: precedencia de operadores

En Python (y en matematicas), la multiplicacion se evalua **antes** que la suma. En esta actividad vas a implementar una funcion que respeta este orden.

## Objetivo

Implementa `calcular_expresion(a, b, c)` que retorne el resultado de `a + b * c` respetando la precedencia.

## Ejemplos

```python
>>> calcular_expresion(1, 2, 3)   # 1 + 2*3 = 1 + 6 = 7
7

>>> calcular_expresion(5, 1, 4)   # 5 + 1*4 = 5 + 4 = 9
9
```

## Pistas

- En Python, `1 + 2 * 3` devuelve `7` (no `9`).
- Si queres que se evalue de izquierda a derecha, usa parentesis: `(1 + 2) * 3` = `9`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 5 tests pasen.