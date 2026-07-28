# Reto: comparar dos versiones de codigo

En esta actividad vas a implementar un comparador basico de versiones de codigo, una habilidad util para revisar cambios generados por IA.

## Objetivo

Lee dos versiones de codigo separadas por una linea vacia desde stdin, comparalas linea por linea y reporta las diferencias.

## Formato de entrada

```
version1_linea1
version1_linea2
...
<linea vacia>
version2_linea1
version2_linea2
...
```

## Salida esperada

Una lista de diferencias: para cada linea diferente, mostrar la linea de la version 1 (o "(no existe)") y la linea de la version 2.

## Pistas

- Divide el input por linea vacia (\n\n).
- Itera ambas listas en paralelo.
- Si las lineas difieren, anotalo.

## ¿Como probar?

Hace clic en **Check**.