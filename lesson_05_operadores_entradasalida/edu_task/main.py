"""Calculadora de IMC (Índice de Masa Corporal).

Fórmulas:
- IMC = peso / (altura ** 2)
- Clasificación:
    * < 18.5: Bajo peso
    * 18.5 <= IMC < 25: Normal
    * 25 <= IMC < 30: Sobrepeso
    * >= 30: Obesidad
"""


def calcular_imc(peso, altura):
    """Calcula el índice de masa corporal.

    Args:
    peso (float): peso en kilogramos.
    altura (float): altura en metros.

    Returns:
    float: el IMC redondeado a 2 decimales.
    """
    # TODO: calcula el IMC y devolvelo redondeado a 2 decimales con round()
    return 0.0


def clasificar_imc(imc):
    """Devuelve la categoría del IMC según los rangos de la OMS.

    Args:
    imc (float): el IMC calculado.

    Returns:
    str: "Bajo peso", "Normal", "Sobrepeso" u "Obesidad".
    """
    # TODO: implementa los rangos con if/elif/else
    return ""


if __name__ == '__main__':
    print(calcular_imc(70, 1.75))
    print(clasificar_imc(22.86))
