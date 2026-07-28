# Ejercicio: verificar si un numero es primo

En esta actividad vas a implementar la verificacion clasica de numeros primos, una habilidad fundamental en algoritmos.

## Objetivo

Implementa `es_primo(n)` que retorne `True` si `n` es primo, `False` en caso contrario.

## Reglas

- 0 y 1 NO son primos.
- 2 es primo.
- Un numero es primo si solo es divisible por 1 y por si mismo.

## Ejemplos

```python
>>> es_primo(7)
True

>>> es_primo(10)
False   # 10 = 2 * 5

>>> es_primo(2)
True
```

## Pistas

- Casos base: n < 2 retorna False, n == 2 retorna True.
- Para n > 2, verifica que no tenga divisores entre 2 y sqrt(n).
- Si `n % i == 0` para algun i en ese rango, NO es primo.

## ¿Como probar?

Hace clic en **Check** y verifica que los 8 tests pasen.