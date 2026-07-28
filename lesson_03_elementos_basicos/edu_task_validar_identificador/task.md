# Ejercicio: validar identificadores en Python

Los identificadores en Python siguen reglas estrictas. En esta actividad vas a implementar una funcion que las verifica.

## Objetivo

Implementa `es_identificador_valido(nombre)` que reciba un string y retorne `True` si puede usarse como nombre de variable, funcion o clase en Python.

## Reglas de identificadores validos

1. Debe empezar con letra (a-z, A-Z) o guion bajo (`_`).
2. Despues puede tener letras, digitos (0-9) o guiones bajos.
3. **NO** puede ser una palabra reservada (keyword) de Python.

## Ejemplos

```python
>>> es_identificador_valido("edad")
True

>>> es_identificador_valido("2edad")
False

>>> es_identificador_valido("mi-variable")
False
```

## Pistas

- Verifica que `nombre` no este vacio.
- Verifica que el primer caracter sea letra o `_`: `nombre[0].isalpha() or nombre[0] == "_"`.
- Verifica que todos los caracteres sean alfanumericos o `_`: `nombre.isidentifier()` de Python hace esto, pero intenta implementarlo manualmente.
- Verifica que no sea keyword: `import keyword; keyword.iskeyword(nombre)`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 8 tests pasen.