def agregar_producto(lista, producto):
    # INICIO DE LA IMPLEMENTACIÓN
    lista.append(producto)
    # FIN DE LA IMPLEMENTACIÓN


def eliminar_producto(lista, producto):
    # INICIO DE LA IMPLEMENTACIÓN
    if producto in lista:
        lista.remove(producto)
        # TODO: implementa las funciones de la lista (agregar, buscar, ordenar)
        return True
    return False
    # FIN DE LA IMPLEMENTACIÓN


def buscar_producto(lista, producto):
    # INICIO DE LA IMPLEMENTACIÓN
    return producto in lista
    # FIN DE LA IMPLEMENTACIÓN


def listar_productos(lista):
    # INICIO DE LA IMPLEMENTACIÓN
    return lista.copy()
    # FIN DE LA IMPLEMENTACIÓN


if __name__ == "__main__":
    compras = []
    agregar_producto(compras, "arroz")
    agregar_producto(compras, "leche")
    print("Productos:", listar_productos(compras))
