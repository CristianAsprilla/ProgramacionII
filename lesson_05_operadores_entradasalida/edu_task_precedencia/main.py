"""Evalua expresiones respetando la precedencia de operadores."""


def calcular_expresion(a, b, c):
    """Calcula el resultado de la expresion a + b * c.

    Args:
        a (int): primer operando.
        b (int): segundo operando.
        c (int): tercer operando.

    Returns:
        int: resultado respetando la precedencia (* antes que +).
    """
    # TODO: respeta la precedencia: multiplicacion antes que suma
    return 0


if __name__ == "__main__":
    print(calcular_expresion(1, 2, 3))   # 1 + 2*3 = 7
    print(calcular_expresion(5, 1, 4))   # 5 + 1*4 = 9
    print(calcular_expresion(0, 0, 0))   # 0