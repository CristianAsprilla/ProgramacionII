# Paso 5: validar los datos del estudiante

En este paso vas a anadir **validacion** para que la tarjeta no acepte datos invalidos. Implementa tres funciones.

## Objetivo

### `validar_nombre(nombre)`

Retorna `True` si el nombre tiene al menos 2 caracteres (despues de quitar espacios).

### `validar_edad(edad)`

Retorna `True` si la edad esta entre 5 y 100 (inclusivo).

### `pedir_nombre_valido()`

Pide el nombre al usuario en un bucle hasta que ingrese uno valido (usa `validar_nombre`).

```python
>>> pedir_nombre_valido()
Tu nombre: A
Nombre invalido, intenta de nuevo.
Tu nombre: Maria
"Maria"
```

## Pistas

- Para `validar_nombre`: `return len(nombre.strip()) >= 2`.
- Para `validar_edad`: `return 5 <= edad <= 100`.
- Para `pedir_nombre_valido`: usa un bucle `while True` con `input()` y `validar_nombre`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 7 tests pasen.
