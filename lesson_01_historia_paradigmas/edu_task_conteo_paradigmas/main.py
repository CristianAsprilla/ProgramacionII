"""Cuenta lenguajes por paradigma."""


def contar_paradigmas(lenguajes):
    """Cuenta cuantos lenguajes hay por cada paradigma.

    Args:
        lenguajes (list): lista de tuplas (nombre, paradigma).

    Returns:
        dict: diccionario con paradigma como clave y conteo como valor.
    """
    conteo = {}
    for nombre, paradigma in lenguajes:
        conteo[paradigma] = conteo.get(paradigma, 0) + 1
    return conteo


if __name__ == "__main__":
    datos = [
        ("C", "imperativo"),
        ("Java", "poo"),
        ("Python", "multi-paradigma"),
        ("Haskell", "funcional"),
    ]
    print(contar_paradigmas(datos))
