# Paso 1: Catálogo de productos con diccionarios

En este primer paso vas a implementar las funciones básicas para gestionar el
catálogo de productos de la tiendita.

## Estructura del catálogo

El catálogo es un **diccionario** donde:

- Cada **clave** es el nombre del producto (por ejemplo, `"Cuaderno"`).
- Cada **valor** es otro diccionario con `"precio"` y `"stock"`.

Ejemplo:

```python
catalogo = {
    "Cuaderno": {"precio": 2.5, "stock": 20},
    "Lapiz":    {"precio": 0.5, "stock": 100},
    "Borrador": {"precio": 0.75, "stock": 50},
}
```

## Funciones a implementar

### `agregar_producto(catalogo, nombre, precio, stock)`

- Si el `nombre` **ya existe** en el catálogo, devolvé `False` (no se pisa).
- Si no existe, agrega `{"precio": precio, "stock": stock}` y devolvé `True`.

### `buscar_producto(catalogo, nombre)`

- Devolvé el diccionario interno con precio y stock.
- Si el producto no existe, devolvé `None`.

### `actualizar_stock(catalogo, nombre, cantidad)`

- Si el producto **no existe**, devolvé `False`.
- Si existe, sumá `cantidad` al stock actual (puede ser negativo para restar)
  y devolvé `True`.

## Pistas

- Para saber si una clave existe: `if nombre in catalogo:`.
- Para agregar: `catalogo[nombre] = {"precio": ..., "stock": ...}`.
- Para buscar: `catalogo.get(nombre)` (devuelve `None` si no existe).
- Para actualizar: `catalogo[nombre]["stock"] += cantidad`.

## ¿Cómo probar?

Hacé clic en **Check** y verifica que pasan los 8 tests.
