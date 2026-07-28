"""Valida si un string puede usarse como identificador en Python."""


def es_identificador_valido(nombre):
    """Determina si un string es un identificador Python valido.

    Args:
        nombre (str): el nombre a validar.

    Returns:
        bool: True si es identificador valido, False en caso contrario.
    """
    # TODO: valida que el string siga las reglas de identificador Python
    return False


if __name__ == "__main__":
    print(es_identificador_valido("edad"))           # True
    print(es_identificador_valido("edad2"))          # True
    print(es_identificador_valido("_privado"))       # True
    print(es_identificador_valido("2edad"))          # False (empieza con digito)
    print(es_identificador_valido("class"))          # False (es keyword)
    print(es_identificador_valido("mi-variable"))    # False (guion medio)