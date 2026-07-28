# Reto: detectar y convertir tipos

## Objetivo

Lee un numero desde stdin. Si es un entero (sin punto decimal), imprime `Es int: <valor>`. Si tiene punto decimal, imprime `Es float: <valor>`.

## Ejemplo

Si la entrada es:

```
3.14
```

La salida debe ser:

```
Es float: 3.14
```

Y si la entrada es `5`, la salida es `Es int: 5`.

## Pistas

- Lee la linea con `input()`.
- Verifica si tiene punto: `if "." in linea:`.
- Si tiene punto, parsea con `float(linea)`; sino, con `int(linea)`.

## ¿Como probar?

Hace clic en **Check**.