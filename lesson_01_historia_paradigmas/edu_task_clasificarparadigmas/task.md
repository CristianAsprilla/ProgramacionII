# Ejercicio: clasificar paradigmas de programacion

En la Lección 1 viste que existen distintos **paradigmas de programacion**: imperativo, funcional, orientado a objetos, entre otros. En este ejercicio vas a implementar una funcion que detecta el paradigma de un fragmento de codigo basandose en palabras clave.

## Objetivo

Implementa `clasificar_paradigma(codigo)` que reciba un string con codigo Python y devuelva el paradigma detectado.

## Palabras clave para detectar

| Paradigma | Palabras clave a buscar |
|-----------|------------------------|
| Imperativo | `for`, `while`, `if`, `=` (asignacion) |
| Funcional | `lambda`, `map`, `filter`, `reduce` |
| POO (Orientado a Objetos) | `class`, `self`, `def __init__` |

## Ejemplos

```python
>>> clasificar_paradigma("x = 5\\nfor i in range(10):\\n    print(i)")
"imperativo"

>>> clasificar_paradigma("list(map(lambda n: n*n, [1,2,3]))")
"funcional"

>>> clasificar_paradigma("class Perro:\\n    def ladrar(self):\\n        print('Guau!')")
"poo"
```

## Pistas

- Podes usar el operador `in` para verificar si una palabra aparece en el codigo.
- Si el codigo contiene `class` o `self`, probablemente es POO.
- Si contiene `lambda` o `map`, es funcional.
- Si solo tiene asignaciones, bucles y condicionales, es imperativo.

## ¿Como probar?

Hace clic en **Check** y verifica que los 4 tests pasen.
