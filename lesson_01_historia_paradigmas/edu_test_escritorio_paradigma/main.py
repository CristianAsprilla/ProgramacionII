"""Prueba de escritorio: predice el output de un fragmento de codigo."""


def predecir_output(codigo, lenguaje="python"):
    """Predice el output o paradigma de un fragmento de codigo.

    Args:
        codigo (str): codigo fuente.
        lenguaje (str): lenguaje de programacion (por defecto python).

    Returns:
        str: descripcion del output esperado o paradigma detectado.
    """
    # Detecta POO
    if "class " in codigo and ("self" in codigo or "__init__" in codigo):
        return "poo: el codigo define una clase"
    # Detecta funcional
    if any(kw in codigo for kw in ("lambda ", "map(", "filter(", "reduce(")):
        return "funcional: usa funciones de orden superior"
    # Detecta condicionales
    if "if " in codigo and "else" in codigo:
        return "imperativo con control de flujo"
    # Detecta bucles
    if "for " in codigo or "while " in codigo:
        return "imperativo con bucle"
    # Default
    return "imperativo"


if __name__ == "__main__":
    print(predecir_output("x = 1"))
    print(predecir_output("class Coche:\n    def arrancar(self):"))
    print(predecir_output("numeros = list(map(lambda x: x*2, [1,2,3]))"))
