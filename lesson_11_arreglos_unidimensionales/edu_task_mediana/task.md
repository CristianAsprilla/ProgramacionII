# Práctica: mediana de notas

En el colegio de Panama las notas se manejan en escala de **1.0 a 5.0** (3.0 es el
mínimo aprobatorio). En este ejercicio vas a implementar una función que calcule la **mediana**
de una lista de notas.

## ¿Qué es la mediana?

La mediana es el valor que queda en el centro cuando los datos están ordenados de menor a
mayor:

- Si la cantidad de notas es **impar**, la mediana es el valor que está justo en la posición
  central.
- Si la cantidad de notas es **par**, la mediana es el **promedio de los dos valores centrales**.
- Si la lista está vacía, devuelve `None`.

## Lo que tienes que hacer

Completa la función `mediana(notas)` para que:

1. Devuelva `None` si la lista está vacía.
2. Ordene las notas (puedes usar `sorted(notas)`) y calcule la mediana según la cantidad de
   elementos.

Ejemplos:

```python
mediana([4.0, 4.5, 5.0])        # 4.5 (la nota central)
mediana([3.0, 4.0, 4.5, 5.0])   # 4.25 (promedio de 4.0 y 4.5)
mediana([])                     # None
mediana([4.8])                  # 4.8
```

No imprimas nada dentro de la función; devuelve el resultado con `return`. Puedes usar
operaciones de listas, `sorted` y `len`.