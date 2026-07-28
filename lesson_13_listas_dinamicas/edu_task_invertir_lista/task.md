# Ejercicio: invertir una lista sin reverse()

En esta actividad vas a invertir una lista **sin usar** los metodos built-in `reverse()` ni `reversed()`. El objetivo es que implementes la logica manualmente.

## Objetivo

Implementa `invertir_lista(lista)` que retorne una **nueva** lista invertida, sin modificar la original.

## Ejemplos

```python
>>> invertir_lista([1, 2, 3, 4])
[4, 3, 2, 1]

>>> invertir_lista(["a", "b", "c"])
["c", "b", "a"]
```

## Pistas

- Podes usar slicing: `lista[::-1]` (la forma mas pythonica).
- O con bucle: crear una lista nueva, recorrer la original en reverso, agregar cada elemento.
- O recursivo.

## ¿Como probar?

Hace clic en **Check** y verifica que los 6 tests pasen (incluyendo uno que verifica que NO uses `reverse()`).