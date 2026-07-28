"""Paso 7: estadisticas del catalogo."""


def valor_total_catalogo(catalogo):
    """Calcula el valor total del catalogo (suma de todos los precios).

    Args:
        catalogo (dict): diccionario {nombre: precio}.

    Returns:
        float: suma de todos los precios.
    """
    # TODO: retorna sum(catalogo.values())
    return 0.0


def precio_promedio(catalogo):
    """Calcula el precio promedio de los productos.

    Args:
        catalogo (dict): diccionario {nombre: precio}.

    Returns:
        float: precio promedio, o 0 si el catalogo esta vacio.
    """
    # TODO: si el catalogo esta vacio retorna 0. Si no, retorna valor_total / cantidad
    return 0.0


def cantidad_productos(catalogo):
    """Cuenta cuantos productos tiene el catalogo.

    Args:
        catalogo (dict): diccionario {nombre: precio}.

    Returns:
        int: cantidad de productos.
    """
    # TODO: retorna len(catalogo)
    return 0


def resumen_catalogo(catalogo):
    """Genera un resumen completo del catalogo.

    Args:
        catalogo (dict): diccionario {nombre: precio}.

    Returns:
        dict: con keys 'cantidad', 'valor_total', 'precio_promedio', 'mas_caro', 'mas_barato'.
    """
    # TODO: integra las funciones anteriores. 'mas_caro' y 'mas_barato' son los NOMBRES (strings)
    return {}


if __name__ == "__main__":
    ejemplo = {"Cuaderno": 1.50, "Lapiz": 0.50, "Borrador": 0.75, "Regla": 2.00}
    print(f"Resumen: {resumen_catalogo(ejemplo)}")
