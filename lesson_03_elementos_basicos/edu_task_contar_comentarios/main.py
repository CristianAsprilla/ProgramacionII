"""Cuenta lineas de comentarios en un fragmento de codigo."""


def contar_comentarios(codigo):
    """Cuenta las lineas que son comentarios (empiezan con #).

    Args:
        codigo (str): codigo fuente como string multilinea.

    Returns:
        int: cantidad de lineas que son comentarios.
    """
    # TODO: cuenta las lineas que empiezan con #
    return 0


if __name__ == "__main__":
    ejemplo = """# esto es un comentario
x = 5
# otro comentario
y = 10"""
    print(contar_comentarios(ejemplo))  # deberia ser 2