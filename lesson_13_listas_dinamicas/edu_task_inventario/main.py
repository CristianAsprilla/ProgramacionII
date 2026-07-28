# Inventario de la tiendita escolar del Bachillerato Tecnico
# Cada producto se representa con un diccionario:
#   {"nombre": str, "precio": float, "stock": int}

inventario = []


def agregar_producto(nombre, precio, stock):
    # TODO Agrega un producto nuevo al inventario (verifica que el nombre no exista).
    pass


def vender(nombre, cantidad):
    # TODO Descuenta la cantidad vendida del stock del producto.
    # Devuelve True si se pudo vender, False si no hay suficiente stock.
    pass


def stock_actual(nombre):
    # TODO Devuelve el stock actual del producto o None si no existe.
    pass


def listar_inventario():
    # TODO Devuelve una copia de la lista de productos del inventario.
    pass