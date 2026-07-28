# Ejercicio: prueba de escritorio de diccionario

En esta actividad vas a simular operaciones de insercion y acceso sobre un diccionario.

## Objetivo

Implementa `simular_diccionario(operaciones)` que reciba una lista de operaciones y retorne los valores obtenidos en cada operacion `get`.

## Formato de operaciones

- `"set clave valor"` inserta el par clave:valor en el diccionario.
- `"get clave"` obtiene el valor asociado a la clave.

## Ejemplo

```python
ops = ["set nombre Ana", "set edad 17", "get nombre", "get ciudad"]
# ciudad no existe, asi que retorna None
print(simular_diccionario(ops))  # ["Ana", None]
```

## Pistas

- Parsea cada operacion con `op.split(maxsplit=2)`.
- Si `parts[0] == "set"`, haz `dict[parts[1]] = parts[2]`.
- Si es "get", agrega `dict.get(parts[1])` a la lista de resultados.
- `.get()` retorna None si la clave no existe (no lanza error).

## ¿Como probar?

Hace clic en **Check** y verifica que los 6 tests pasen.