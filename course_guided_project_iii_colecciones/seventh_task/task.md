# Paso 7: estadisticas del catalogo

En este paso vas a implementar funciones de **estadisticas** sobre el catalogo.

## Objetivo

### `valor_total_catalogo(catalogo)`

Suma de todos los precios. `0` si esta vacio.

### `precio_promedio(catalogo)`

Promedio de precios. `0` si esta vacio.

### `cantidad_productos(catalogo)`

Cantidad de productos (len del diccionario).

### `resumen_catalogo(catalogo)`

Retorna un dict con:
- `cantidad`: int
- `valor_total`: float
- `precio_promedio`: float
- `mas_caro`: nombre (str) del mas caro
- `mas_barato`: nombre (str) del mas barato

## Pistas

- `sum(catalogo.values())` para valor total.
- Para el promedio: cuida el caso vacio.
- Para los extremos: `max(catalogo, key=catalogo.get)` y `min(catalogo, key=catalogo.get)`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 8 tests pasen.
