# Reto: ordenar la linea de tiempo de los lenguajes

En esta actividad vas a leer varios anos desde la entrada estandar (uno por linea, hasta leer la palabra FIN) y los vas a ordenar de menor a mayor.

## Objetivo

Tu programa debe:

1. Leer lineas desde stdin hasta encontrar "FIN".
2. Convertir cada linea a entero (representa un ano).
3. Ordenarlos de menor a mayor.
4. Imprimir los anos separados por coma y espacio.

## Ejemplo

Si la entrada es:

```
1991
1972
1958
FIN
```

La salida debe ser:

```
1958, 1972, 1991
```

## Pistas

- Podes usar `int(linea.strip())` para convertir cada ano a entero.
- Podes usar una lista para ir guardando los anos.
- Cuando leas la palabra "FIN" (case-sensitive), terminas la lectura.
- Para ordenar: `lista.sort()` o `sorted(lista)`.
- Para imprimir: `", ".join(str(x) for x in lista)`.

## ¿Como probar?

Hace clic en **Check** y el plugin compara tu salida con el archivo `tests/output.txt`.