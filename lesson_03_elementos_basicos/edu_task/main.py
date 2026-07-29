import keyword


def contar_palabras_reservadas(lineas):
    """
    Cuenta cuantas palabras reservadas de Python aparecen en una lista de
    cadenas de texto.

    Parametros:
    lineas (list[str]): lista de strings a analizar.

    Retorna:
    int: cantidad de palabras reservadas encontradas en total,
    contando apariciones repetidas.
    """
    # TODO: implementa la logica aqui
    # TODO: cuenta las palabras reservadas usando el modulo keyword
    return 0


if __name__ == '__main__':
    ejemplo = [
    "for i in range(10):",
    "if numero > 0 and numero < 100:",
    "print('Hola, mundo')",
    "return total",
    ]
    print(contar_palabras_reservadas(ejemplo))