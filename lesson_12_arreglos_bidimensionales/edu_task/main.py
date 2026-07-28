def suma_diagonal_principal(matriz):
    # INICIO DE LA IMPLEMENTACIÓN
    suma = 0
    for indice in range(len(matriz)):
        suma += matriz[indice][indice]
    # FIN DE LA IMPLEMENTACIÓN
    # TODO: implementa la suma de todos los elementos retornando el total
    return suma


if __name__ == "__main__":
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Suma de la diagonal: {suma_diagonal_principal(matriz)}")
