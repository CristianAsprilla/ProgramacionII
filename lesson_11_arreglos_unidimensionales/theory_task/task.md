# Lección 11: Arreglos unidimensionales

En esta lección aprenderás a guardar y procesar varios valores relacionados usando una
**lista** de Python. En muchos lenguajes estas colecciones se llaman arreglos o vectores;
en Python, la lista es la herramienta que usamos normalmente para representar un arreglo.

## ¿Qué es un arreglo unidimensional?

Un arreglo unidimensional es una secuencia de elementos organizados en una sola dirección.
Por ejemplo, las notas de una estudiante de undécimo grado pueden guardarse así:

```python
notas = [4.5, 4.0, 4.8, 3.9]
```

En Python no se declara por separado el tipo ni el tamaño. La lista se crea al escribir sus
elementos entre corchetes. También puede empezar vacía:

```python
notas = []
notas.append(4.5)
notas.append(4.0)
```

A diferencia de un arreglo de tamaño fijo de lenguajes como C o Java, una lista de Python
puede crecer o reducirse durante la ejecución. Además, puede contener valores de distintos
tipos, aunque en un mismo problema suele ser más claro mantener elementos del mismo tipo.

## Acceso por índice

Los índices comienzan en **0**. En la lista `notas`, `notas[0]` es `4.5` y `notas[2]` es
`4.8`. El índice `-1` representa el último elemento:

```python
print(notas[0])   # Primera nota
print(notas[-1])  # Última nota
notas[1] = 4.3   # Actualiza la segunda nota
```

Un índice fuera de los límites produce `IndexError`, por eso conviene conocer el tamaño con
`len(notas)` antes de acceder a una posición calculada.

## Recorrido con `for`

Para procesar todos los elementos podemos recorrer la lista directamente:

```python
for nota in notas:
    print(f"Nota: {nota}")
```

Si necesitas la posición, usa `range(len(notas))`:

```python
for indice in range(len(notas)):
    print(indice, notas[indice])
```

## Operaciones básicas

| Operación | Ejemplo | Qué hace |
|---|---|---|
| Agregar al final | `notas.append(4.7)` | Añade un elemento |
| Insertar | `notas.insert(1, 4.2)` | Inserta en un índice |
| Eliminar por valor | `notas.remove(4.2)` | Quita la primera coincidencia |
| Extraer por índice | `nota = notas.pop()` | Quita y devuelve el último elemento |
| Tamaño | `len(notas)` | Cuenta elementos |
| Ordenar | `notas.sort()` | Ordena la misma lista |
| Buscar pertenencia | `4.5 in notas` | Devuelve `True` o `False` |

`remove` produce un error si el valor no aparece; antes puedes comprobar `if valor in lista`.
`pop` también puede recibir un índice, por ejemplo `notas.pop(0)`.

## Ejemplo contextualizado

Si una lista contiene los tiempos de llegada (en minutos) de un equipo a la escuela, podemos
ordenarlos y verificar si alguien llegó en 20 minutos:

```python
tiempos = [25, 18, 22, 20]
tiempos.sort()
print(tiempos)
print(20 in tiempos)
```

**Idea clave:** una lista permite agrupar datos, acceder a cada posición, recorrerlos y
aplicar operaciones de edición sin administrar manualmente un bloque fijo de memoria.
