"""Paso 8: alertas de stock."""


def productos_sin_stock(stock):
    """Encuentra productos con stock 0 o negativo.

    Args:
        stock (dict): diccionario {nombre: cantidad}.

    Returns:
        list: lista de nombres de productos sin stock.
    """
    # TODO: retorna los nombres cuyo stock <= 0
    return []


def productos_stock_bajo(stock, minimo=5):
    """Encuentra productos con stock menor a un minimo.

    Args:
        stock (dict): diccionario {nombre: cantidad}.
        minimo (int): cantidad minima (por defecto 5).

    Returns:
        list: lista de tuplas (nombre, cantidad) de productos con stock bajo.
    """
    # TODO: retorna tuplas (nombre, cantidad) para los que tienen cantidad < minimo
    return []


def alerta_reabastecimiento(stock, minimo=5):
    """Genera un mensaje de alerta para reabastecer productos.

    Args:
        stock (dict): diccionario {nombre: cantidad}.
        minimo (int): cantidad minima (por defecto 5).

    Returns:
        str: mensaje formateado con los productos que necesitan reabastecimiento.
    """
    # TODO: si no hay productos con stock bajo, retorna "Todo en orden"
    # Si hay, retorna un mensaje con cada producto en una linea
    return ""


if __name__ == "__main__":
    ejemplo = {"Cuaderno": 0, "Lapiz": 3, "Borrador": 10, "Regla": 0}
    print(alerta_reabastecimiento(ejemplo))
