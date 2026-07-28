# Ejercicio: contar comentarios en codigo

En esta actividad vas a usar `str.splitlines()` para iterar por las lineas de un codigo y contar las que son comentarios.

## Objetivo

Implementa `contar_comentarios(codigo)` que reciba un codigo fuente multilinea y cuente las lineas que empiezan con `#`.

## Ejemplos

```python
>>> contar_comentarios("# hola\nx = 5\n# mundo")
2

>>> contar_comentarios("x = 1\ny = 2")
0
```

## Pistas

- Divide el codigo en lineas con `codigo.splitlines()`.
- Para cada linea, verifica si `linea.startswith("#")`.
- Tambien considera lineas que son solo espacios (no cuentan como comentario).

## ¿Como probar?

Hace clic en **Check** y verifica que los 5 tests pasen.