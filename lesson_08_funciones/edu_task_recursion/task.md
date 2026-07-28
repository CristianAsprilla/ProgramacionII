# Fibonacci recursivo

La sucesión de **Fibonacci** se define así: `F(0) = 0`, `F(1) = 1` y, para `n >= 2`, `F(n) = F(n-1) + F(n-2)`. Esta definición es naturalmente recursiva: una función que se llama a sí misma con valores más pequeños hasta llegar a los casos base.

Implementá `fibonacci_recursivo(n)` siguiendo esa definición:

- `fibonacci_recursivo(0)` debe devolver `0`.
- `fibonacci_recursivo(1)` debe devolver `1`.
- Para `n >= 2`, debe devolver la suma de los dos términos anteriores.

Mantén la validación: un `n` negativo debe lanzar `ValueError("N debe ser no negativo")`.

> Tip: revisa primero el caso base para `0` y `1`; sin esa condición, la recursión nunca termina.