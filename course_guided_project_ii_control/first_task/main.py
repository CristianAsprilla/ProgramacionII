"""Calculadora de notas con menú.

Funciones básicas del paso 1: agregar y listar notas.
"""

# Lista global de notas. La usaremos mientras el programa esté corriendo.
notas = []


def agregar_nota(notas, nota):
    """Agrega una nota a la lista si está en el rango válido (0-100).

    Args:
        notas (list[float]): lista de notas existentes.
        nota (float): nota a agregar (entre 0 y 100).

    Returns:
        bool: True si la nota se agregó, False si estaba fuera de rango.
    """
    # TODO: implementa la validación (0 <= nota <= 100) y el append a la lista
    return False


def listar_notas(notas):
    """Devuelve una lista formateada con todas las notas.

    Args:
        notas (list[float]): lista de notas.

    Returns:
        str: texto listo para imprimir con todas las notas numeradas.
    """
    # TODO: si la lista está vacía devolvé "No hay notas todavía."
    # Si no, devolvé un string con cada nota en una línea numerada.
    return ""


if __name__ == '__main__':
    print(listar_notas(notas))
