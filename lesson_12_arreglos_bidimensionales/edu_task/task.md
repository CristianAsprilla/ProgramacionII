# Práctica: diagonal principal de una matriz

Recibe una matriz cuadrada de `3 x 3` representada como una lista anidada y completa la función
`suma_diagonal_principal(matriz)`.

La función debe sumar únicamente los elementos cuya fila y columna tienen el mismo índice:
`matriz[0][0] + matriz[1][1] + matriz[2][2]`.

Ejemplo:

```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = suma_diagonal_principal(matriz)
# resultado es 15
```

Devuelve la suma; no la imprimas dentro de la función. Puedes usar un ciclo `for` y acceder a
cada elemento con doble índice. Las pruebas también incluyen otros tamaños de matrices
cuadradas para comprobar que tu solución no dependa de números escritos a mano.
