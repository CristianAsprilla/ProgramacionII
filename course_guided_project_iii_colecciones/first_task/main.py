"""Sistema de inventario de la tiendita escolar.

Paso 1: catálogo de productos con diccionarios.
"""

# El catálogo: diccionario donde cada clave es el nombre del producto
# y el valor es otro diccionario con su precio y stock.
catalogo = {}


def agregar_producto(catalogo, nombre, precio, stock):
    """Agrega un producto nuevo al catálogo.

    Args:
        catalogo (dict): diccionario de productos.
        nombre (str): nombre del producto (clave única).
        precio (float): precio unitario.
        stock (int): cantidad en inventario.

    Returns:
        bool: True si se agregó, False si el nombre ya existía.
    """
    # TODO: si el nombre ya está en el catálogo, devolvé False.
    # Si no, agrega {"precio": precio, "stock": stock} y devolvé True.
    return False


def buscar_producto(catalogo, nombre):
    """Busca un producto por nombre.

    Returns:
        dict | None: diccionario con precio y stock, o None si no existe.
    """
    # TODO: usa catalogo.get(nombre) y devolvé el resultado.
    return None


def actualizar_stock(catalogo, nombre, cantidad):
    """Cambia el stock de un producto (puede ser positivo o negativo).

    Args:
        catalogo (dict): diccionario de productos.
        nombre (str): nombre del producto.
        cantidad (int): cambio a aplicar (puede ser negativo para restar).

    Returns:
        bool: True si se actualizó, False si el producto no existe.
    """
    # TODO: si el producto no existe, devolvé False. Si existe,
    # modificá catalogo[nombre]["stock"] sumandole 'cantidad'.
    return False


if __name__ == '__main__':
    agregar_producto(catalogo, "Cuaderno", 2.5, 20)
    print(buscar_producto(catalogo, "Cuaderno"))
