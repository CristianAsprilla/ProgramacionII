"""Paso 2: crear la tarjeta completa de presentacion."""


# Importamos la funcion del paso 1 para usarla aqui
from first_task.main import crear_saludo


def crear_tarjeta(nombre, edad, carrera, trimestre, promedio, materias):
    """Crea la tarjeta de presentacion completa del estudiante.

    Args:
        nombre (str): nombre del estudiante.
        edad (int): edad.
        carrera (str): carrera que estudia.
        trimestre (int): trimestre actual (1, 2 o 3).
        promedio (float): promedio de notas (escala 1.0-5.0).
        materias (int): cantidad de materias inscritas.

    Returns:
        str: texto formateado con la tarjeta de presentacion.
    """
    # TODO: implementa la tarjeta completa. Usa crear_saludo() para el saludo inicial.
    # Muestra todos los datos en lineas separadas, con encabezado y pie.
    # Para el promedio, muestra una estrella (*) si >= 4.5
    return ""


if __name__ == "__main__":
    print(crear_tarjeta("Maria", 17, "Bachillerato Tecnico", 1, 4.8, 6))
