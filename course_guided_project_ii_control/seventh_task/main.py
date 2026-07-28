"""Paso 7: guardar y cargar notas desde un archivo."""


def guardar_notas(notas, ruta_archivo):
    """Guarda una lista de notas en un archivo de texto, una por linea.

    Args:
        notas (list): lista de notas (floats).
        ruta_archivo (str): ruta del archivo donde guardar.
    """
    # TODO: abre el archivo en modo escritura y escribe cada nota en una linea
    pass


def cargar_notas(ruta_archivo):
    """Carga notas desde un archivo de texto, una por linea.

    Args:
        ruta_archivo (str): ruta del archivo a leer.

    Returns:
        list: lista de notas (floats).
    """
    # TODO: abre el archivo en modo lectura, lee cada linea, conviertela a float, y retorna la lista
    return []


if __name__ == "__main__":
    ejemplo = [4.5, 3.8, 5.0, 2.5]
    guardar_notas(ejemplo, "/tmp/notas.txt")
    cargadas = cargar_notas("/tmp/notas.txt")
    print(f"Cargadas: {cargadas}")
