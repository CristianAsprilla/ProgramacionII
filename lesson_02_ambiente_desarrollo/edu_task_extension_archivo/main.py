"""Extractor de extension de archivo."""


def extension(nombre_archivo):
    """Extrae la extension de un nombre de archivo.

    Args:
        nombre_archivo (str): nombre del archivo (con o sin extension).

    Returns:
        str: la extension sin el punto, o string vacio si no tiene.
    """
    # Busca el ultimo punto en el string
    idx = nombre_archivo.rfind(".")
    # Sin punto o punto al final (despues de rfind)
    if idx == -1 or idx == len(nombre_archivo) - 1:
        return ""
    return nombre_archivo[idx + 1:]


if __name__ == "__main__":
    print(f"'documento.pdf': {extension('documento.pdf')}")
    print(f"'README': {extension('README')}")
    print(f"'datos.csv': {extension('datos.csv')}")
    print(f"'archivo.': {extension('archivo.')}")
