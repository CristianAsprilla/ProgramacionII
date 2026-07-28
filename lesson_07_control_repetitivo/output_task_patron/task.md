# Patrón triangular de asteriscos

Lee un entero positivo `N` desde la entrada estándar e imprime un triángulo de asteriscos con `N` líneas:

- Línea 1: `*`
- Línea 2: `**`
- Línea 3: `***`
- …
- Línea N: `*` repetido `N` veces

Por ejemplo, para la entrada `3` la salida debe ser:

```
*
**
***
```

Pista: un `for` con `range(1, n + 1)` te da el número de línea; puedes multiplicar `"*"` por ese número para obtener la fila.