# Ejercicio: contar paradigmas

En esta actividad vas a usar un diccionario para agrupar y contar lenguajes segun su paradigma. Esto es una aplicacion practica de la estructura `dict` que aprendiste en lecciones anteriores.

## Objetivo

Implementa `contar_paradigmas(lenguajes)` que reciba una lista de tuplas `(nombre, paradigma)` y retorne un diccionario con el conteo por paradigma.

## Ejemplo

```python
>>> datos = [
...     ("Python", "multi-paradigma"),
...     ("C", "imperativo"),
...     ("Haskell", "funcional"),
... ]
>>> contar_paradigmas(datos)
{"multi-paradigma": 1, "imperativo": 1, "funcional": 1}
```

## Pistas

- Recorre la lista con `for`.
- Si el paradigma ya esta en el dict, incrementa; si no, inicializa en 1.
- Podes usar `dict.get(clave, 0)` para inicializar.

## ¿Como probar?

Hace clic en **Check** y verifica que los 5 tests pasen.