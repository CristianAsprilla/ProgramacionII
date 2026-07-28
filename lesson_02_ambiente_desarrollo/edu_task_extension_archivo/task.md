# Ejercicio: extraer extension de archivo

En esta actividad vas a implementar una funcion util para el manejo de archivos, una habilidad practica para cualquier programa.

## Objetivo

Implementa `extension(nombre_archivo)` que reciba el nombre de un archivo (como string) y retorne la extension sin el punto.

## Ejemplos

```python
>>> extension("documento.pdf")
"pdf"

>>> extension("README")
""

>>> extension("datos.csv")
"csv"
```

## Pistas

- Busca el **ultimo** punto en el string con `rfind('.')`.
- Si no hay punto, retorna `""`.
- Si el punto esta al final (ej: `"archivo."`), no hay extension → retorna `""`.
- Para extraer: `nombre_archivo[indice_punto + 1:]`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 7 tests pasen.