"""Extrae la extension de un nombre de archivo."""


def extension(nombre_archivo):
    """Retorna la extension de un nombre de archivo.

    Args:
        nombre_archivo (str): nombre del archivo (ej: 'foto.png').

    Returns:
        str: extension sin el punto, o '' si no tiene extension.
    """
    # TODO: busca el ultimo punto y retorna lo que esta despues
    return ""


if __name__ == "__main__":
    print(extension("documento.pdf"))       # pdf
    print(extension("foto.PNG"))            # PNG
    print(extension("script.py"))           # py
    print(extension("README"))              # ''
    print(extension("datos.csv"))           # csv