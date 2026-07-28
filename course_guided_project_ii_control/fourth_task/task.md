# Paso 4: ordenar las notas

En este paso vas a anadir una funcion para **ordenar las notas** (de menor a mayor o de mayor a menor).

## Objetivo

### `ordenar_notas(notas, descendente=False)`

Retorna una **nueva** lista con las notas ordenadas.

```python
>>> ordenar_notas([5, 2, 8, 1, 9])
[1, 2, 5, 8, 9]

>>> ordenar_notas([5, 2, 8, 1, 9], descendente=True)
[9, 8, 5, 2, 1]
```

## Pistas

- `sorted(lista, reverse=descendente)` retorna una nueva lista ordenada sin modificar la original.
- Si usas `.sort()` modifica la lista original, eso **no** es lo que queremos.

## ¿Como probar?

Hace clic en **Check** y verifica que los 4 tests pasen.
