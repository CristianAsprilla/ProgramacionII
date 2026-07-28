# Ejercicio: detectar el tipo de una variable

En esta actividad vas a implementar una funcion que devuelve el nombre del tipo de un valor como string, en lugar de usar `type()` directamente.

## Objetivo

Implementa `tipo_variable(valor)` que reciba cualquier valor y retorne:

- `"int"` para enteros
- `"float"` para numeros decimales
- `"str"` para strings
- `"bool"` para booleanos
- `"list"` para listas
- `"otro"` para todo lo demas

## Ejemplos

```python
>>> tipo_variable(5)
"int"

>>> tipo_variable(3.14)
"float"

>>> tipo_variable("hola")
"str"

>>> tipo_variable(True)
"bool"
```

## Pistas

- Usa `isinstance(valor, int)`, `isinstance(valor, float)`, etc.
- **Importante**: verifica `bool` ANTES de `int`, porque `bool` es subclase de `int` en Python.

## ¿Como probar?

Hace clic en **Check** y verifica que los 6 tests pasen.