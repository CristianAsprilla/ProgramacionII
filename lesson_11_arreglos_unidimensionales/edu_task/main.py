def analizar_notas(notas):
    # INICIO DE LA IMPLEMENTACIÓN
    suma = sum(notas)
    promedio = suma / len(notas)
    nota_maxima = max(notas)
    resultado = (promedio, nota_maxima)
    # FIN DE LA IMPLEMENTACIÓN
    # TODO: implementa el calculo del promedio retornando el resultado
    return resultado


if __name__ == "__main__":
    notas = [4.5, 4.0, 4.8, 3.9]
    promedio, maxima = analizar_notas(notas)
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota máxima: {maxima:.2f}")
