# Ejercicio: factorial modular

## Objetivo

Implementa `factorial_modular(n)` que calcule n! = n * (n-1) * ... * 2 * 1.

## Ejemplos

```python
>>> factorial_modular(5)
120   # 5 * 4 * 3 * 2 * 1

>>> factorial_modular(0)
1     # por definicion
```

## Pistas

- Caso base: 0! = 1 y 1! = 1.
- Recursivo: `n! = n * (n-1)!`.
- Iterativo: usa un bucle `for` con un acumulador.

## ¿Como probar?

Hace clic en **Check** y verifica que los 6 tests pasen.