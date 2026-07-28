"""Paso 5: validar los datos del estudiante.

NOTA: Este paso es independiente. Asume que ya tienes las
funciones leer_nombre() y leer_edad() del paso 3, pero
NO las copia aqui. Podes usarlas si las importas.
"""


def validar_nombre(nombre):
    """Valida que un nombre no este vacio y tenga al menos 2 caracteres.

    Args:
        nombre (str): nombre a validar.

    Returns:
        bool: True si es valido, False si no.
    """
    # TODO: retorna True si el nombre tiene al menos 2 caracteres y no es solo espacios
    return False


def validar_edad(edad):
    """Valida que una edad este en el rango esperado (5-100).

    Args:
        edad (int): edad a validar.

    Returns:
        bool: True si esta en rango, False si no.
    """
    # TODO: retorna True si la edad esta entre 5 y 100 (inclusivo)
    return False


def pedir_nombre_valido():
    """Pide el nombre al usuario hasta que ingrese uno valido.

    Returns:
        str: nombre valido.
    """
    # TODO: usa un bucle while con validar_nombre para insistir hasta tener nombre valido
    return ""


if __name__ == "__main__":
    nombre = pedir_nombre_valido()
    print(f"Hola {nombre}!")
