"""Paso 4: calcular IMC y categoria."""


def calcular_imc(peso_kg, altura_m):
    """Calcula el IMC (indice de masa corporal).

    Args:
        peso_kg (float): peso en kilogramos.
        altura_m (float): altura en metros.

    Returns:
        float: el IMC redondeado a 2 decimales.
    """
    # TODO: calcula IMC = peso / altura^2 y redondea a 2 decimales
    return 0.0


def categoria_imc(imc):
    """Clasifica el IMC en una categoria.

    Args:
        imc (float): el IMC calculado.

    Returns:
        str: 'bajo peso', 'normal', 'sobrepeso' u 'obesidad'.
    """
    # TODO: retorna la categoria segun el IMC (< 18.5 bajo, < 25 normal, < 30 sobrepeso, >= 30 obesidad)
    return ""


if __name__ == "__main__":
    imc = calcular_imc(70, 1.75)
    print(f"IMC: {imc} ({categoria_imc(imc)})")
