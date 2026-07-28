# Paso 5: buscar productos

En este paso vas a anadir funciones de **busqueda** al catalogo.

## Objetivo

### `buscar_producto(catalogo, nombre)`

Busca un producto por nombre exacto. Retorna el precio o `None`.

### `buscar_productos_por_precio(catalogo, precio_max)`

Retorna una lista de nombres cuyo precio es <= `precio_max`.

## Pistas

- `dict.get(clave)` retorna `None` si la clave no existe.
- Para la busqueda por precio: list comprehension: `[nombre for nombre, precio in catalogo.items() if precio <= precio_max]`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 4 tests pasen.
