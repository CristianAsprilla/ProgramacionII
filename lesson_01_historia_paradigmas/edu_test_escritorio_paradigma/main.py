"""Predice el output de fragmentos de codigo por paradigma."""


def predecir_output(codigo, lenguaje):
    """Predice que imprime un fragmento segun su paradigma.

    Args:
        codigo (str): codigo fuente.
        lenguaje (str): "python", "javascript" o "rust".

    Returns:
        str: descripcion del output esperado.
    """
    # TODO: analiza el codigo y predice el output segun el paradigma
    # Si ves "class" es POO, "lambda" es funcional, etc.
    return ""


if __name__ == "__main__":
    # Ejemplo: este codigo es POO
    codigo = "class Coche:\n    def arrancar(self):\n        print('Arrancando')"
    print(predecir_output(codigo, "python"))