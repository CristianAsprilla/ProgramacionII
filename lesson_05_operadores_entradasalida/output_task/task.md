# Ejercicio: Saludo personalizado

En este ejercicio vas a escribir un programa que **lee datos del usuario**
desde la consola y muestra un saludo con formato.

## Lo que tiene que hacer tu programa

1. Leer un **nombre** (string) por stdin.
2. Leer una **edad** (entero) por stdin.
3. Imprimir un saludo con el formato:

```
¡Hola <nombre>! tienes <edad> años.
```

## Ejemplo de ejecución

Si la entrada es:

```
María
17
```

La salida debe ser:

```
¡Hola María! tienes 17 años.
```

## Pistas

- Para leer un string: `input()`.
- Para leer un entero: `int(input())`.
- Para el formato: usa una f-string como `f"¡Hola {nombre}! tienes {edad} años."`.

## ¿Cómo probar?

Hacé clic en **Check** y el plugin va a comparar tu salida con la salida
esperada usando el archivo `tests/output.txt`.
