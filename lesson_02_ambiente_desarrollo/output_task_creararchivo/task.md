# Reto: crear un archivo desde terminal

En la LECCION 2 aprendiste a navegar por la terminal y a ejecutar programas Python. En este mini-reto, vas a simular la creacion de un archivo leyendo su nombre desde la entrada estandar.

## Objetivo

Tu programa debe:

1. Leer un **nombre de archivo** desde stdin.
2. Imprimir un mensaje con el formato: `Archivo creado: <nombre>`

## Ejemplo

Si la entrada es:

```
notas.txt
```

La salida debe ser:

```
Archivo creado: notas.txt
```

## Pistas

- Para leer una linea de texto: `input()`.
- Para imprimir: `print("Archivo creado:", nombre)` o usa f-string.

## ¿Como probar?

Hace clic en **Check** y el plugin va a comparar tu salida con la salida esperada usando el archivo `tests/output.txt`.
