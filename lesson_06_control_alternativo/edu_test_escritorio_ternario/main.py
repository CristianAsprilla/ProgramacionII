"""Predice el output de expresiones condicionales (operador ternario)."""


def evaluar_ternario(condicion, valor_true, valor_false):
    """Evalua una expresion ternaria.

    Args:
        condicion (bool): la condicion.
        valor_true: lo que retorna si la condicion es True.
        valor_false: lo que retorna si la condicion es False.

    Returns:
        el valor correspondiente segun la condicion.
    """
    # TODO: retorna valor_true si condicion es True, sino valor_false
    return None


if __name__ == "__main__":
    print(evaluar_ternario(True, "mayor", "menor"))     # mayor
    print(evaluar_ternario(5 > 3, 1, 0))                 # 1
    print(evaluar_ternario(5 < 3, "si", "no"))            # no