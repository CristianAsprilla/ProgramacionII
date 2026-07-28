"""Verificador de version de Python."""


def es_version_compatible(version_info):
    """Determina si una version de Python es compatible con el curso.

    Args:
        version_info (tuple): tupla (major, minor, micro).

    Returns:
        bool: True si es >= 3.10, False en caso contrario.
    """
    # TODO: extrae major y minor, retorna True si >= 3.10
    return False


if __name__ == "__main__":
    print(es_version_compatible((3, 12, 0)))  # True
    print(es_version_compatible((3, 9, 0)))   # False
    print(es_version_compatible((3, 10, 1)))  # True