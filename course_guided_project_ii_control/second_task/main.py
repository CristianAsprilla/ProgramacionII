"""Paso 2: calculos estadisticos sobre notas."""


# Importamos las funciones del paso 1
from first_task.main import agregar_nota, listar_notas


def calcular_promedio(notas):
    """Calcula el promedio de las notas.

    Args:
        notas (list): lista de notas.

    Returns:
        float: el promedio, o None si la lista esta vacia.
    """
    # TODO: si la lista esta vacia, retorna None. Si no, retorna la suma dividido por la cantidad
    return None


def nota_maxima(notas):
    """Retorna la nota maxima.

    Args:
        notas (list): lista de notas.

    Returns:
        float: la nota maxima, o None si la lista esta vacia.
    """
    # TODO: si la lista esta vacia, retorna None. Si no, retorna max(notas)
    return None


def nota_minima(notas):
    """Retorna la nota minima.

    Args:
        notas (list): lista de notas.

    Returns:
        float: la nota minima, o None si la lista esta vacia.
    """
    # TODO: si la lista esta vacia, retorna None. Si no, retorna min(notas)
    return None


if __name__ == "__main__":
    ejemplo = [4.5, 3.8, 5.0, 2.5]
    agregar_nota(ejemplo, 4.0)
    print(f"Notas: {listar_notas(ejemplo)}")
    print(f"Promedio: {calcular_promedio(ejemplo)}")
    print(f"Maxima: {nota_maxima(ejemplo)}")
    print(f"Minima: {nota_minima(ejemplo)}")
