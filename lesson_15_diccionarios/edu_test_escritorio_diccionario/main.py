"""Simula inserciones y accesos en un diccionario."""


def simular_diccionario(operaciones):
    """Simula operaciones sobre un diccionario.

    Args:
        operaciones (list): lista de operaciones, cada una es:
            - un string "set clave valor" para insertar
            - un string "get clave" para obtener valor

    Returns:
        list: lista de valores obtenidos en cada operacion 'get'.
    """
    # TODO: simula las operaciones y retorna la lista de gets
    return []


if __name__ == "__main__":
    ops = ["set nombre Ana", "set edad 17", "get nombre", "get ciudad"]
    # nombre -> "Ana", edad -> "17", nombre -> "Ana", ciudad -> None (no existe)
    print(simular_diccionario(ops))  # ["Ana", None]