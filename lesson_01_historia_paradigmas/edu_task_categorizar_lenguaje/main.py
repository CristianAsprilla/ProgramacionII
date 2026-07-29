"""Categoriza lenguajes de programacion por ano de creacion."""


def categoria_por_ano(ano):
    """Categoriza un lenguaje segun su ano de creacion.

    Args:
        ano (int): ano de creacion del lenguaje.

    Returns:
        str: "antiguo" si ano < 1990, "moderno" si 1990 <= ano <= 2010,
             "reciente" si ano > 2010.
    """
    if ano < 1990:
        return "antiguo"
    elif ano <= 2010:
        return "moderno"
    else:
        return "reciente"


if __name__ == "__main__":
    print(f"1958 (Lisp): {categoria_por_ano(1958)}")
    print(f"1990 (Python): {categoria_por_ano(1990)}")
    print(f"2010 (Go): {categoria_por_ano(2010)}")
    print(f"2014 (Swift): {categoria_por_ano(2014)}")
    print(f"2020 (Julia): {categoria_por_ano(2020)}")
