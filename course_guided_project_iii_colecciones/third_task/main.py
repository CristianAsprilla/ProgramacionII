"""Paso 3: pila para deshacer (undo)."""


# Importamos las funciones de los pasos anteriores
from first_task.main import agregar_producto, buscar_producto, actualizar_stock
from second_task.main import registrar_operacion, ver_historial


def apilar_operacion(pila, operacion):
    """Apila una operacion en la pila de undo.

    Args:
        pila (list): pila de operaciones.
        operacion (dict): operacion a apilar.
    """
    # TODO: usa append() para agregar la operacion a la pila
    pass


def deshacer(pila, catalogo, historial):
    """Deshace la ultima operacion.

    Args:
        pila (list): pila de operaciones.
        catalogo (dict): catalogo de productos.
        historial (list): historial de operaciones.

    Returns:
        dict: la operacion deshecha, o None si la pila esta vacia.
    """
    # TODO: si la pila esta vacia, retorna None.
    # Si no, saca la ultima operacion (pop) y reviertela en el catalogo.
    # Si fue "agregar", elimina el producto.
    # Si fue "actualizar", restaura el stock anterior.
    return None


if __name__ == "__main__":
    pila = []
    cat = {"Cuaderno": {"precio": 1.50, "stock": 10}}
    apilar_operacion(pila, {"tipo": "agregar", "producto": "Cuaderno", "precio": 1.50, "stock": 10})
    op = deshacer(pila, cat, [])
    print(f"Deshecho: {op}")
