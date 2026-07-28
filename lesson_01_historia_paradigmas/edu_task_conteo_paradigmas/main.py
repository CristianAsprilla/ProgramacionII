"""Cuenta paradigmas de programacion en una lista de lenguajes."""


def contar_paradigmas(lenguajes):
    """Cuenta cuantos lenguajes hay por cada paradigma.

    Args:
        lenguajes (list): lista de tuplas (lenguaje, paradigma).

    Returns:
        dict: diccionario con el conteo por paradigma.
    """
    # TODO: crea un diccionario vacio, recorre la lista y cuenta por paradigma
    conteo = {}
    return conteo


if __name__ == "__main__":
    ejemplo = [
        ("Python", "multiparadigma"),
        ("Haskell", "funcional"),
        ("C", "imperativo"),
        ("Python", "multiparadigma"),
    ]
    print(contar_paradigmas(ejemplo))
