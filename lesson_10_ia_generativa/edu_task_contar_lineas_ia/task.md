# Ejercicio: contar lineas de codigo

La IA generativa produce codigo que a veces incluye comentarios innecesarios o lineas vacias. En esta actividad vas a implementar una funcion que cuenta las lineas que tienen codigo real.

## Objetivo

Implementa `contar_lineas_codigo(codigo)` que cuente lineas que NO son comentarios (no empiezan con #) NI vacias.

## Ejemplos

```python
>>> contar_lineas_codigo("x = 1\ny = 2")
2

>>> contar_lineas_codigo("# hola\nx = 1")
1
```

## Pistas

- Divide con `splitlines()`.
- Ignora lineas que empiezan con `#`.
- Ignora lineas que solo tienen espacios (usa `.strip()`).
- Ignora lineas vacias.

## ¿Como probar?

Hace clic en **Check** y verifica que los 5 tests pasen.