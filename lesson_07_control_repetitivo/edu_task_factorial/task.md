# Factorial iterativo

El **factorial** de un entero no negativo `n` se define como el producto de todos los enteros desde `1` hasta `n`:

```
n! = 1 × 2 × 3 × … × n
```

Por convención, `0! = 1` y `1! = 1`. Por ejemplo, `5! = 120`.

Implementa `factorial_iterativo(n)` usando un ciclo (`for` o `while`). No uses recursión: en esta lección practicamos cómo acumular un resultado dentro de un lazo. Mantén la validación: un valor negativo debe lanzar `ValueError("N debe ser no negativo")`.