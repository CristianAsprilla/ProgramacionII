# Paso 2: Promedio, nota máxima y nota mínima

¡Excelente! Ya puedes agregar y listar notas. Ahora vamos a hacer cálculos
sobre la lista.

## Funciones a implementar

### `calcular_promedio(notas)`

Devuelve el **promedio** de las notas (float) o `None` si la lista está vacía.

```python
>>> calcular_promedio([80, 90, 100])
90.0
>>> calcular_promedio([])
None
```

### `nota_maxima(notas)`

Devuelve la **nota más alta** o `None` si la lista está vacía.

```python
>>> nota_maxima([80, 90, 100, 95])
100
>>> nota_maxima([])
None
```

### `nota_minima(notas)`

Devuelve la **nota más baja** o `None` si la lista está vacía.

```python
>>> nota_minima([80, 90, 100, 95])
80
>>> nota_minima([])
None
```

## Pistas

- Para el promedio: `sum(notas) / len(notas)`. Cuidado con la **división por
  cero** cuando la lista está vacía (devolvé `None`).
- Para máximo y mínimo puedes usar las funciones built-in `max()` y `min()`,
  o hacerlo con un `for` si quieres practicar.
- Manejá el caso de lista vacía devolviendo `None`.

## ¿Cómo probar?

Hacé clic en **Check** y verifica que pasan los 10 tests.
