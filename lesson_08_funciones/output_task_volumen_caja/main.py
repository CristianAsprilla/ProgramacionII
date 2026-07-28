"""Calcula el volumen de una caja (ortoedro)."""


def volumen_caja(largo, ancho, alto):
    """Calcula el volumen de una caja.

    Args:
        largo (float): dimension largo.
        ancho (float): dimension ancho.
        alto (float): dimension alto.

    Returns:
        float: volumen.
    """
    # TODO: calcula el volumen como largo * ancho * alto
    return 0.0


if __name__ == "__main__":
    print(volumen_caja(2, 3, 4))  # 24
    print(volumen_caja(1, 1, 1))  # 1
    print(volumen_caja(0, 5, 10)) # 0