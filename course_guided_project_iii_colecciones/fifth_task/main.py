"""Paso 5: buscar productos."""


def buscar_producto(catalogo, nombre):
    """Busca un producto en el catalogo por nombre exacto.

    Args:
        catalogo (dict): diccionario {nombre: precio}.
        nombre (str): nombre a buscar.

    Returns:
        float: precio del producto, o None si no existe.
    """
    # TODO: retorna catalogo.get(nombre) o None si no existe
    return None


def buscar_productos_por_precio(catalogo, precio_max):
    """Busca productos cuyo precio es <= precio_max.

    Args:
        catalogo (dict): diccionario {nombre: precio}.
        precio_max (float): precio maximo.

    Returns:
        list: lista de nombres de productos que cumplen.
    """
    # TODO: retorna una lista con los nombres cuyo precio <= precio_max
    return []


if __name__ == "__main__":
    ejemplo = {"Cuaderno": 1.50, "Lapiz": 0.50, "Borrador": 0.75, "Regla": 2.00}
    print(f"Buscar Cuaderno: {buscar_producto(ejemplo, 'Cuaderno')}")
    print(f"Productos baratos (<= 1.0): {buscar_productos_por_precio(ejemplo, 1.0)}")
