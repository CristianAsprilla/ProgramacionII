"""Retorna el nombre del tipo de un valor como string."""


def tipo_variable(valor):
    """Retorna el nombre del tipo de un valor.

    Args:
        valor: cualquier valor de Python.

    Returns:
        str: 'int', 'float', 'str', 'bool', 'list' u 'otro'.
    """
    # TODO: detecta el tipo y retorna el nombre como string
    return "otro"


if __name__ == "__main__":
    print(tipo_variable(5))            # int
    print(tipo_variable(3.14))         # float
    print(tipo_variable("hola"))       # str
    print(tipo_variable(True))         # bool
    print(tipo_variable([1, 2, 3]))    # list
    print(tipo_variable((1, 2)))       # otro