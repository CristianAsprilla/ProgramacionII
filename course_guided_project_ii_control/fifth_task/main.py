"""Paso 5: buscar una nota."""


def buscar_nota(notas, valor):
    """Busca el primer indice donde aparece una nota con el valor dado.

    Args:
        notas (list): lista de notas.
        valor (float): valor a buscar.

    Returns:
        int: indice de la primera ocurrencia, o -1 si no se encuentra.
    """
    # TODO: recorre la lista y retorna el indice de la primera ocurrencia, o -1 si no
    return -1


def contar_notas_en_rango(notas, minimo, maximo):
    """Cuenta cuantas notas estan en el rango [minimo, maximo].

    Args:
        notas (list): lista de notas.
        minimo (float): valor minimo (inclusivo).
        maximo (float): valor maximo (inclusivo).

    Returns:
        int: cantidad de notas en el rango.
    """
    # TODO: cuenta cuantas notas cumplen minimo <= nota <= maximo
    return 0


if __name__ == "__main__":
    ejemplo = [3.5, 5.0, 4.2, 2.8, 4.9, 5.0]
    print(f"Buscar 5.0: indice {buscar_nota(ejemplo, 5.0)}")
    print(f"Notas entre 4.0 y 5.0: {contar_notas_en_rango(ejemplo, 4.0, 5.0)}")
