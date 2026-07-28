from math import pi


def area_circulo(radio: float) -> float:
    """Calcula el área de un círculo."""
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    return pi * radio ** 2


def area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo."""
    if base < 0 or altura < 0:
        raise ValueError("Las medidas no pueden ser negativas")
    return base * altura
