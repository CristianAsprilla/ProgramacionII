# Práctica: promedio de notas por estudiante (matriz)

En el colegio de Panama, las notas de la clase de undécimo grado se almacenan en una
**matriz** (lista de listas). Cada fila representa a una estudiante y cada columna, a una
materia. Las notas están en escala **1.0 a 5.0** y el mínimo aprobatorio es **3.0**.

## Lo que tienes que hacer

Completa la función `promedio_estudiantes(notas)` para que reciba una matriz donde:

- Cada fila interna corresponde a un estudiante.
- Cada columna corresponde a una materia.

La función debe devolver una **lista** con el promedio de notas de cada estudiante, en el mismo
orden en que aparecen las filas.

Ejemplos:

```python
matriz = [
    [4.5, 4.0, 4.8],   # estudiante 1
    [3.9, 4.2, 4.6],   # estudiante 2
    [5.0, 4.7, 4.9],   # estudiante 3
]
promedio_estudiantes(matriz)
# [4.4333..., 4.2333..., 4.8666...]
```

No imprimas nada dentro de la función; devuelve la lista con `return`. Puedes usar
`sum(fila)`, `len(fila)` o un recorrido manual.