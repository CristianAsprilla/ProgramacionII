"""Categoriza lenguajes segun su ano de creacion."""


def categoria_por_ano(ano):
    """Clasifica un lenguaje segun su ano de creacion.

    Args:
        ano (int): ano de creacion del lenguaje.

    Returns:
        str: 'antiguo' (antes de 1990), 'moderno' (1990-2010),
                                                    'reciente' (despues de 2010).
    """
    # TODO: implementa la clasificacion segun el rango del ano
    return ""


if __name__ == "__main__":
    print(f"1972 -> {categoria_por_ano(1972)}")  # antiguo
    print(f"2000 -> {categoria_por_ano(2000)}")  # moderno
    print(f"2015 -> {categoria_por_ano(2015)}")  # reciente