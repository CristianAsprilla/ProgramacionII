# Paso 7: guardar y cargar notas

En este paso vas a implementar la **persistencia**: guardar las notas a un archivo y cargarlas de vuelta.

## Objetivo

### `guardar_notas(notas, ruta_archivo)`

Guarda cada nota en una linea del archivo.

### `cargar_notas(ruta_archivo)`

Lee cada linea del archivo y la convierte a float. Si el archivo no existe, retorna lista vacia.

## Pistas

- `open(ruta, "w")` para escribir, `open(ruta, "r")` para leer.
- Para escribir: `archivo.write(f"{nota}\\n")` en un bucle.
- Para leer: `return [float(linea.strip()) for linea in open(ruta)]`.
- Para el caso de archivo inexistente: `try/except FileNotFoundError`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 3 tests pasen.
