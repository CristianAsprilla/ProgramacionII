def contar_lineas_codigo(texto: str) -> int:
    """Cuenta cuántas líneas de un texto son código real.

    Una línea cuenta como código si NO está vacía y NO es un comentario
    (no empieza con '#', posiblemente con espacios antes).

    Ejemplos:
    >>> contar_lineas_codigo("a = 1\\n# comentario\\nb = 2")
    2
    >>> contar_lineas_codigo("# solo comentario\\n\\n   # otro")
    0
    >>> contar_lineas_codigo("print('hola')\\n")
    1
    """
    # TODO: recorre las líneas del texto y devuelve cuántas NO son vacías ni comentarios
    return 0


if __name__ == "__main__":
    ejemplo = "def sumar(a, b):\n    return a + b\n\n# esto es un comentario\nresultado = sumar(3, 4)\n"
    print(contar_lineas_codigo(ejemplo))