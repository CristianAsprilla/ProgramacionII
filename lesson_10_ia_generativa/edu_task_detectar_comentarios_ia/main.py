"""Detecta si un codigo tiene comentarios redundantes tipicos de IA."""


def tiene_comentarios_redundantes(codigo):
    """Detecta comentarios redundantes tipicos de codigo generado por IA.

    Args:
        codigo (str): codigo fuente.

    Returns:
        bool: True si tiene comentarios redundantes, False en caso contrario.
    """
    # TODO: detecta patrones como 'esta funcion...' o 'ahora retornamos...'
    return False


if __name__ == "__main__":
    ejemplo_ia = """# Esta funcion suma dos numeros
def suma(a, b):
    # Ahora retornamos el resultado
    return a + b"""
    print(tiene_comentarios_redundantes(ejemplo_ia))  # True

    ejemplo_humano = """def suma(a, b):
    return a + b"""
    print(tiene_comentarios_redundantes(ejemplo_humano))  # False