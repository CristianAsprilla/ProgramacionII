"""Cuenta lineas de codigo excluyendo comentarios y lineas vacias."""


def contar_lineas_codigo(codigo):
    """Cuenta lineas que tienen codigo real (no comentarios ni vacias).

    Args:
        codigo (str): codigo fuente multilinea.

    Returns:
        int: cantidad de lineas con codigo.
    """
    # TODO: cuenta lineas que no son comentarios ni vacias
    return 0


if __name__ == "__main__":
    ejemplo = """# Comentario
x = 5
y = 10
print(x + y)"""
    print(contar_lineas_codigo(ejemplo))