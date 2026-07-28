# Paso 1: Agregar y listar notas

En este primer paso vas a implementar las dos funciones más básicas de la
calculadora: una para **agregar notas** con validación y otra para **listar**
las notas que ya están en memoria.

## `agregar_nota(notas, nota)`

Esta función debe:

1. Verificar que la `nota` esté en el rango **0 a 100** (inclusive).
2. Si es válida, agregarla a la lista `notas` con `append` y devolver `True`.
3. Si no es válida, **no agregarla** y devolver `False`.

```python
>>> notas = []
>>> agregar_nota(notas, 85)
True
>>> notas
[85]
>>> agregar_nota(notas, 150)
False
>>> notas
[85]
```

## `listar_notas(notas)`

Esta función debe devolver un `str` listo para imprimir:

- Si la lista está vacía: `"No hay notas todavía."`
- Si hay notas: una por línea, numerada. Por ejemplo:

```
1. 80
2. 90
3. 100
```

## Pistas

- Para validar el rango usa un `if` con `0 <= nota <= 100`.
- Para listar las notas numeradas puedes usar `enumerate` o un contador manual
  con un `for`.
- Los tests verifican los **contenidos**, no el formato exacto de la lista
  numerada, así que no te preocupes por los detalles.

## ¿Cómo probar?

Hacé clic en **Check** y verifica que pasan los 7 tests.
