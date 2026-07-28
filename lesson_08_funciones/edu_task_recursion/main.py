def fibonacci_recursivo(n: int) -> int:
    """Devuelve el n-ésimo número de Fibonacci usando recursión.

    Definición:
    - fibonacci_recursivo(0) == 0
    - fibonacci_recursivo(1) == 1
    - fibonacci_recursivo(n) == fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

    Ejemplo: fibonacci_recursivo(10) == 55

    Si n es negativo, lanzar ValueError con el mensaje
    "N debe ser no negativo".
    """
    # TODO: implementa la versión recursiva (caso base + caso recursivo)
    return 0


if __name__ == "__main__":
    # Ejemplo: el décimo número de Fibonacci es 55
    print(fibonacci_recursivo(10))