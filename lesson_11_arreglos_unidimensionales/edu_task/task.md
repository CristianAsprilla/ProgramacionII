# Práctica: promedio y nota máxima

En un centro educativo de Panamá se registran las notas de un grupo en un vector (una lista)
de Python. Tu tarea es completar la función `analizar_notas(notas)`.

La función recibe una lista no vacía de números y debe devolver una tupla con dos valores, en
este orden:

1. El promedio de todas las notas.
2. La nota máxima del vector.

Por ejemplo:

```python
promedio, maxima = analizar_notas([4.0, 4.5, 5.0])
# promedio es 4.5 y maxima es 5.0
```

Usa operaciones de listas y, si quieres, funciones incorporadas como `sum`, `len` y `max`.
No imprimas dentro de la función: los resultados deben devolverse con `return`. La lista que
recibas tendrá al menos una nota.
