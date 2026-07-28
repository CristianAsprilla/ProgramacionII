# Paso 5: buscar y contar notas

En este paso vas a implementar funciones de **busqueda** sobre la lista de notas.

## Objetivo

### `buscar_nota(notas, valor)`

Busca el primer indice donde aparece `valor` en `notas`. Retorna `-1` si no esta.

```python
>>> buscar_nota([3.5, 5.0, 4.2, 2.8], 4.2)
2
>>> buscar_nota([3.5, 5.0, 4.2], 1.0)
-1
```

### `contar_notas_en_rango(notas, minimo, maximo)`

Cuenta cuantas notas estan en el rango `[minimo, maximo]` (inclusivo).

```python
>>> contar_notas_en_rango([1, 2, 3, 4, 5], 2, 4)
3
```

## Pistas

- Para `buscar_nota`: usa un bucle `for i, n in enumerate(notas)`.
- Para `contar_notas_en_rango`: usa `sum(1 for n in notas if minimo <= n <= maximo)`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 5 tests pasen.
