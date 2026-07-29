def area_circulo(radio: float) -> float:
    """Calcula el área de un círculo de radio dado.

    Fórmula: área = π × radio²
    Ejemplo: area_circulo(2) ≈ 12.566...

    Si el radio es negativo, lanzar ValueError con el mensaje
    "El radio no puede ser negativo".
    """
    # TODO: devuelve π × radio² (importa math o usa la constante)
    return 0.0


def fahrenheit_a_celsius(f: float) -> float:
    """Convierte una temperatura en Fahrenheit a Celsius.

    Fórmula: celsius = (f - 32) × 5/9
    Ejemplo: fahrenheit_a_celsius(32) == 0
                                                    fahrenheit_a_celsius(212) == 100
    """
    # TODO: aplica la fórmula y devuelve el resultado en Celsius
    return 0.0


if __name__ == "__main__":
    print(f"Área del círculo de radio 3: {area_circulo(3):.2f}")
    print(f"100 °F en Celsius: {fahrenheit_a_celsius(100):.2f}")