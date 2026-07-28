def evaluar_imc(peso: float, altura: float) -> str:
    """Calcula el Índice de Masa Corporal y devuelve la categoría.

    El IMC se obtiene dividiendo el peso (en kg) entre la altura (en metros)
    elevada al cuadrado. Las categorías siguen la clasificación de la OMS:

    - IMC < 18.5            -> "Bajo peso"
    - 18.5 <= IMC < 25     -> "Normal"
    - 25   <= IMC < 30     -> "Sobrepeso"
    - IMC >= 30            -> "Obesidad"

    Si la altura es 0 o negativa, lanzar ValueError con el mensaje
    "La altura debe ser mayor a 0". Si el peso es negativo, lanzar
    ValueError con el mensaje "El peso no puede ser negativo".
    """
    # TODO: calcula el IMC y devuelve la categoría según los rangos de la OMS
    return ""


if __name__ == "__main__":
    # Ejemplo de uso: una persona de 70 kg y 1.75 m debería caer en "Normal"
    print(evaluar_imc(70, 1.75))