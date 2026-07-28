"""Paso 2: historial de operaciones (lista dinamica)."""


# Importamos las funciones del paso 1
from first_task.main import agregar_producto, buscar_producto, actualizar_stock


def registrar_operacion(historial, tipo, detalles):
    """Registra una operacion en el historial.

    Args:
        historial (list): lista del historial.
        tipo (str): tipo de operacion ("agregar", "actualizar", etc).
        detalles (dict): detalles especificos de la operacion.
    """
    # TODO: agrega al historial un diccionario con las claves:
    # 'tipo' (str), 'detalles' (dict), 'timestamp' (str, usa datetime.now().isoformat())
    pass


def ver_historial(historial):
    """Devuelve un texto con todas las operaciones del historial.

    Args:
        historial (list): lista del historial.

    Returns:
        str: texto con las operaciones, una por linea.
    """
    # TODO: si historial esta vacio, retorna "Sin operaciones todavia."
    # Si no, retorna un string con cada operacion formateada
    return ""


if __name__ == "__main__":
    cat = {}
    agregar_producto(cat, "Cuaderno", 1.50, 10)
    hist = []
    registrar_operacion(hist, "agregar", {"producto": "Cuaderno"})
    print(ver_historial(hist))
