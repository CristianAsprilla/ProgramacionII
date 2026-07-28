# Paso 3: Leer los datos del estudiante

En este paso vas a implementar las funciones que **leen los datos del estudiante** desde la terminal usando `input()`.

## Objetivo

Implementa dos funciones:

### `leer_nombre()`

Lee el nombre del estudiante y lo devuelve como string.

```python
>>> leer_nombre()
Como te llamas? Maria
"Maria"
```

### `leer_edad()`

Lee la edad del estudiante y la devuelve como entero.

```python
>>> leer_edad()
Cuantos anos tienes? 17
17
```

## Pistas

- Usa `input("mensaje: ")` para mostrar un prompt al usuario.
- Para el nombre: `resultado = input("prompt: "); return resultado.strip()`.
- Para la edad: `return int(input("prompt: "))` (esto lanza `ValueError` si no es un numero, eso esta bien para este paso).

## ¿Como probar?

Hace clic en **Check** y verifica que los 3 tests pasen.
