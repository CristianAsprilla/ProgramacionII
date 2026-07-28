# Lección 12: Arreglos bidimensionales (matrices)

Una lista anidada es una lista cuyos elementos son otras listas. Esta estructura representa
un **arreglo bidimensional**, también llamado **matriz**, porque organiza los datos en filas y
columnas.

## Declaración e inicialización

Podemos representar las notas de varias estudiantes en varias asignaturas así:

```python
notas = [
    [4.5, 4.0, 4.8],
    [3.9, 4.2, 4.6],
    [5.0, 4.7, 4.9],
]
```

Esta matriz tiene tres filas y tres columnas. Cada fila puede verse como una lista
autónoma. También podemos construir una matriz vacía y agregar filas con `append`:

```python
matriz = []
matriz.append([1, 2, 3])
matriz.append([4, 5, 6])
```

Para crear una matriz rectangular de ceros, una comprensión de listas evita compartir la
misma fila por accidente:

```python
filas = 3
columnas = 4
matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
```

## Acceso con doble índice

El primer índice indica la fila y el segundo indica la columna. Los índices comienzan en cero:

```python
print(notas[0][1])  # Fila 0, columna 1: 4.0
notas[1][2] = 4.7   # Cambia la fila 1, columna 2
```

La expresión `notas[i][j]` significa: primero busca la fila `i` y después el elemento `j`
dentro de esa fila. Un índice inválido produce `IndexError`.

## Recorrido con `for` anidados

Para visitar cada elemento usamos un ciclo para las filas y otro para las columnas:

```python
for fila in notas:
    for valor in fila:
        print(valor)
```

Si necesitamos posiciones, podemos usar `range` dos veces:

```python
for i in range(len(notas)):
    for j in range(len(notas[i])):
        print(f"notas[{i}][{j}] = {notas[i][j]}")
```

## Sumas importantes

- **Suma de una fila:** `sum(matriz[i])`.
- **Suma de una columna:** recorrer las filas y acumular `matriz[i][j]`.
- **Diagonal principal:** en una matriz cuadrada, son las posiciones donde fila y columna
  coinciden: `matriz[0][0]`, `matriz[1][1]`, `matriz[2][2]`, etc.

La suma de la diagonal principal de una matriz cuadrada puede escribirse así:

```python
suma = 0
for i in range(len(matriz)):
    suma += matriz[i][i]
```

## Ejemplo contextualizado

Una tabla de temperaturas de tres días en tres momentos puede ser una matriz. La suma de una
columna permite comparar un mismo momento del día, mientras que la suma de una fila resume un
día. En el reto de esta lección trabajarás con una matriz de notas de `3 x 3` y calcularás su
diagonal principal.

**Idea clave:** una matriz es una lista de listas; para recorrer todos sus datos normalmente
necesitas un `for` externo y un `for` interno.
