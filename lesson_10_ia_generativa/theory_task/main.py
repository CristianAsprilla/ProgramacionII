# Antes de aceptar código generado, pruébalo con casos normales y extremos.
def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
