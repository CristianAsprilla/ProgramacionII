# Paso 8: alertas de stock

En este paso vas a implementar funciones de **alertas** para la tiendita: detectar productos sin stock o con stock bajo.

## Objetivo

### `productos_sin_stock(stock)`

Retorna nombres con stock <= 0.

### `productos_stock_bajo(stock, minimo=5)`

Retorna tuplas (nombre, cantidad) para stock < minimo.

### `alerta_reabastecimiento(stock, minimo=5)`

Retorna un mensaje formateado. Si no hay productos con stock bajo, retorna "Todo en orden". Si hay, retorna:

```
Reabastecer:
- Cuaderno (stock: 2)
- Lapiz (stock: 3)
```

## Pistas

- Para el mensaje, usa `"\n".join(f"- {nombre} (stock: {cantidad})" for ...)`.
- Si la lista de stock bajo esta vacia, retorna "Todo en orden" sin mas.

## ¿Como probar?

Hace clic en **Check** y verifica que los 6 tests pasen.
