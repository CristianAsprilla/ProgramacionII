# Ejercicio: verificar version de Python

El curso usa caracteristicas de Python 3.10 o superior (como `match/case`). Por eso, es importante poder verificar si la version instalada es compatible.

## Objetivo

Implementa `es_version_compatible(version_info)` que reciba una tupla `(major, minor, micro)` y retorne `True` si Python es 3.10 o superior.

## Ejemplos

```python
>>> es_version_compatible((3, 10, 0))
True

>>> es_version_compatible((3, 9, 9))
False

>>> es_version_compatible((3, 12, 1))
True
```

## Pistas

- La tupla tiene 3 elementos: (major, minor, micro).
- Extrae major y minor: `major, minor, _ = version_info`.
- Compara: `(major, minor) >= (3, 10)`.
- Para Python 2, major es 2.

## ¿Como probar?

Hace clic en **Check** y verifica que los 6 tests pasen.