from geometria import area_circulo, area_rectangulo


def resumen_areas(radio: float, base: float, altura: float) -> tuple[float, float]:
    """Devuelve las áreas de un círculo y un rectángulo."""
    circulo = area_circulo(radio)
    rectangulo = area_rectangulo(base, altura)
    # TODO: implementa los calculos de areas y retorna la tupla (circulo, rectangulo)
    return circulo, rectangulo


if __name__ == "__main__":
    area_c, area_r = resumen_areas(3, 5, 4)
    print(f"Área del círculo: {area_c:.2f}")
    print(f"Área del rectángulo: {area_r:.2f}")
