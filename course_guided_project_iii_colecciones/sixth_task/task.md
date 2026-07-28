# Paso 6: ordenar el catalogo

En este paso vas a implementar funciones para **ordenar** el catalogo por precio y encontrar el mas caro/barato.

## Objetivo

### `ordenar_por_precio(catalogo, descendente=False)`

Retorna una lista de tuplas `(nombre, precio)` ordenada por precio.

### `producto_mas_caro(catalogo)` y `producto_mas_barato(catalogo)`

Retornan el nombre del producto mas caro / mas barato, o `None` si el catalogo esta vacio.

## Pistas

- `sorted(catalogo.items(), key=lambda item: item[1], reverse=descendente)`.
- `max(catalogo, key=catalogo.get)` retorna la clave con el valor maximo.
- `min(catalogo, key=catalogo.get)` retorna la clave con el valor minimo.

## ¿Como probar?

Hace clic en **Check** y verifica que los 6 tests pasen.
