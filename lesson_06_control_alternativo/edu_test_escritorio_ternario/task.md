# Ejercicio: prueba de escritorio del operador ternario

En Python, el operador ternario permite elegir entre dos valores segun una condicion: `valor_true if condicion else valor_false`. En esta actividad vas a implementar esa logica en una funcion.

## Objetivo

Implementa `evaluar_ternario(condicion, valor_true, valor_false)` que retorne `valor_true` si la condicion es `True`, sino `valor_false`.

## Ejemplos

```python
>>> evaluar_ternario(True, "mayor", "menor")
"mayor"

>>> evaluar_ternario(5 > 3, 1, 0)
1
```

## Pistas

- En Python: `valor_true if condicion else valor_false`.
- En funcion: `return valor_true if condicion else valor_false`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 5 tests pasen.