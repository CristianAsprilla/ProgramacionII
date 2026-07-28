"""Paso 6: clasificar las notas segun desempeno."""


def clasificar_desempeno(promedio):
    """Clasifica un promedio segun la escala del colegio (1.0-5.0).

    Args:
        promedio (float): promedio de notas (entre 1.0 y 5.0).

    Returns:
        str: 'Excelente', 'Muy bueno', 'Bueno', 'Suficiente' o 'Insuficiente'.
    """
    # TODO: clasifica segun el promedio (>= 4.5 Excelente, >= 4.0 Muy bueno, >= 3.5 Bueno, >= 3.0 Suficiente, < 3.0 Insuficiente)
    return ""


def resumen_desempeno(notas):
    """Genera un resumen completo del desempeno del estudiante.

    Args:
        notas (list): lista de notas.

    Returns:
        dict: con keys 'promedio', 'max', 'min', 'clasificacion', 'aprobado'.
    """
    # TODO: calcula el promedio, max, min, y usa clasificar_desempeno. 'aprobado' es True si promedio >= 3.0
    return {}


if __name__ == "__main__":
    ejemplo = [4.5, 3.8, 5.0, 2.5, 4.0]
    print(f"Notas: {ejemplo}")
    print(f"Resumen: {resumen_desempeno(ejemplo)}")
