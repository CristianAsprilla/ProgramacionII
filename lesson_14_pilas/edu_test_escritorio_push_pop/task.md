# Ejercicio: prueba de escritorio de pila (push/pop)

Una pila es una estructura LIFO (Last In, First Out): el ultimo en entrar es el primero en salir. En esta actividad vas a simular operaciones de pila.

## Objetivo

Implementa `simular_pila(operaciones)` que reciba una lista de operaciones y retorne el estado final de la pila.

## Formato de operaciones

- `"push X"` agrega X al tope de la pila.
- `"pop"` quita el tope de la pila (asume que no esta vacia).

## Ejemplo

```python
ops = ["push 1", "push 2", "push 3", "pop", "push 4"]
# Pila: 1 -> 1,2 -> 1,2,3 -> 1,2 (pop) -> 1,2,4
print(simular_pila(ops))  # [1, 2, 4]
```

## Pistas

- Parsea cada operacion: `parts = op.split()`; si parts[0] == "push", agregar int(parts[1]).
- Si es "pop", quita con `.pop()` o `[:-1]`.
- Trata los valores como enteros.

## ¿Como probar?

Hace clic en **Check** y verifica que los 6 tests pasen.