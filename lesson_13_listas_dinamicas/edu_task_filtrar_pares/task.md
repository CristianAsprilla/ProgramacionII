# Ejercicio: filtrar numeros pares

## Objetivo

Implementa `filtrar_pares(lista)` que retorne una **nueva** lista solo con los numeros pares.

## Ejemplos

```python
>>> filtrar_pares([1, 2, 3, 4, 5, 6])
[2, 4, 6]

>>> filtrar_pares([1, 3, 5])
[]
```

## Pistas

- Un numero es par si `n % 2 == 0`.
- Podes usar lista por comprension: `[x for x in lista if x % 2 == 0]`.
- O con un bucle `for` y `append`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 6 tests pasen.