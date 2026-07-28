def factorial_iterativo(n: int) -> int:
    """Calcula n! usando un ciclo, sin recursión.

    Por definición:
    - factorial_iterativo(0) == 1
    - factorial_iterativo(1) == 1
    - factorial_iterativo(5) == 120
    - factorial_iterativo(10) == 3628800

    Si n es negativo, lanzar ValueError con el mensaje
    "N debe ser no negativo".
    """
    # TODO: calcula n! con un ciclo (for o while), sin recursión
    return 1


if __name__ == "__main__":
    # Ejemplo rápido: 5! debería imprimir 120
    print(factorial_iterativo(5))