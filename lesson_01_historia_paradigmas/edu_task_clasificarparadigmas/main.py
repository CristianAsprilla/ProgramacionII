"""Clasificador de paradigmas de programacion.

Detecta el paradigma de un fragmento de codigo basandose en palabras clave.
"""


def clasificar_paradigma(codigo):
    """Clasifica un fragmento de codigo en un paradigma de programacion.

    Args:
        codigo (str): fragmento de codigo a analizar.

    Returns:
        str: "imperativo", "funcional", "poo" u "orientado a objetos"
             segun las palabras clave encontradas.
    """
    # Detecta POO primero (class + self o def __init__)
    if "class " in codigo and ("self" in codigo or "__init__" in codigo):
        return "poo"
    # Detecta funcional (lambda, map, filter, reduce)
    if any(kw in codigo for kw in ("lambda ", "map(", "filter(", "reduce(")):
        return "funcional"
    # Detecta imperativo (for, while, if, asignacion)
    if any(kw in codigo for kw in ("for ", "while ", "if ", "=")):
        return "imperativo"
    return "imperativo"


if __name__ == "__main__":
    ejemplo1 = "x = 5\nfor i in range(10):\n    print(i)"
    ejemplo2 = "numeros = [1, 2, 3]\ncuadrados = list(map(lambda n: n*n, numeros))"
    ejemplo3 = "class Perro:\n    def ladrar(self):\n        print('Guau!')"

    print(f"Ejemplo 1 es: {clasificar_paradigma(ejemplo1)}")
    print(f"Ejemplo 2 es: {clasificar_paradigma(ejemplo2)}")
    print(f"Ejemplo 3 es: {clasificar_paradigma(ejemplo3)}")
