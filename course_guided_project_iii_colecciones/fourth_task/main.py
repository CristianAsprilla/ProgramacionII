"""Paso 4: matriz de ventas y menu final del programa.

Este paso integra TODO lo construido en los pasos anteriores
en un sistema completo de inventario para la tiendita.
"""

# Importamos todo lo de los pasos anteriores
from first_task.main import agregar_producto, buscar_producto, actualizar_stock
from second_task.main import registrar_operacion, ver_historial
from third_task.main import apilar_operacion, deshacer

# Matriz 4x3: filas = trimestres (Trim I, II, III, total), columnas = productos.
ventas = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


def registrar_venta(ventas, trimestre, producto_idx, cantidad):
    """Registra una venta en la matriz.

    Args:
        ventas (list): matriz 4x3 de ventas.
        trimestre (int): 0=I, 1=II, 2=III (0-2, NO la fila de total).
        producto_idx (int): 0, 1 o 2 (columna del producto).
        cantidad (int): cantidad vendida.
    """
    # TODO: suma la cantidad a la celda correspondiente y recalcula la fila de total (indice 3)
    pass


def generar_reporte(ventas, catalogo):
    """Genera un reporte de ventas por producto.

    Args:
        ventas (list): matriz 4x3 de ventas.
        catalogo (dict): catalogo de productos (para nombres).

    Returns:
        str: reporte formateado con ventas totales por producto.
    """
    # TODO: genera un texto con las ventas totales por producto
    return ""


def mostrar_menu():
    """Muestra el menu principal de la tiendita."""
    # TODO: imprime las opciones del menu (1-6)
    pass


def ejecutar_opcion(opcion, catalogo, ventas, historial, pila):
    """Ejecuta la opcion elegida.

    Args:
        opcion (str): opcion del 1 al 6.
        catalogo (dict): catalogo.
        ventas (list): matriz de ventas.
        historial (list): historial.
        pila (list): pila de undo.

    Returns:
        bool: True si el usuario quiere salir, False si no.
    """
    # TODO: implementa la logica del menu usando las funciones de pasos anteriores:
    # 1=agregar producto, 2=actualizar stock, 3=registrar venta, 4=reporte, 5=deshacer, 6=salir
    return False


def main():
    """Funcion principal del programa."""
    # TODO: muestra el menu en bucle y procesa las opciones hasta que el usuario salga
    pass


if __name__ == "__main__":
    main()
