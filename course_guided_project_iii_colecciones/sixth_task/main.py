"""Paso 6: ordenar el catalogo."""


def ordenar_por_precio(catalogo, descendente=False):
    """Ordena el catalogo por precio.

    Args:
        catalogo (dict): diccionario {nombre: precio}.
        descendente (bool): si True, de mayor a menor.

    Returns:
        list: lista de tuplas (nombre, precio) ordenada por precio.
    """
    # TODO: usa sorted() con key=lambda item: item[1] y reverse=descendente
    return []


def producto_mas_caro(catalogo):
    """Encuentra el producto mas caro del catalogo.

    Args:
        catalogo (dict): diccionario {nombre: precio}.

    Returns:
        str: nombre del producto mas caro, o None si el catalogo esta vacio.
    """
    # TODO: si el catalogo esta vacio retorna None. Si no, retorna el nombre con mayor precio
    return None


def producto_mas_barato(catalogo):
    """Encuentra el producto mas barato del catalogo.

    Args:
        catalogo (dict): diccionario {nombre: precio}.

    Returns:
        str: nombre del producto mas barato, o None si el catalogo esta vacio.
    """
    # TODO: si el catalogo esta vacio retorna None. Si no, retorna el nombre con menor precio
    return None


if __name__ == "__main__":
    ejemplo = {"Cuaderno": 1.50, "Lapiz": 0.50, "Borrador": 0.75, "Regla": 2.00}
    print(f"Orden ascendente: {ordenar_por_precio(ejemplo)}")
    print(f"Mas caro: {producto_mas_caro(ejemplo)}")
    print(f"Mas barato: {producto_mas_barato(ejemplo)}")
