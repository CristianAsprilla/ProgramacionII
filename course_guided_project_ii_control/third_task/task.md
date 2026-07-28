# Paso 3: El menú interactivo

¡Último paso! Ya tienes todas las funciones. Ahora falta **conectarlas** en un
menú que se repite hasta que el usuario decida salir.

## Funciones a implementar

### `ejecutar_opcion(opcion, notas)`

Esta función recibe la opción elegida (como string) y la lista de notas. Debe
hacer lo siguiente:

| Opción | Acción |
|---|---|
| `"1"` | Pedir una nota por `input()`, intentar agregarla con `agregar_nota`. Mostrar mensaje de éxito o error. |
| `"2"` | Imprimir `listar_notas(notas)`. |
| `"3"` | Mostrar el promedio (manejar `None`). |
| `"4"` | Mostrar la nota máxima y la mínima (manejar `None`). |
| `"5"` | Devolver `False` (señal de que el programa debe terminar). |
| otra | Mostrar un mensaje de "opción no válida". |

**Importante**: la función debe **devolver `False` solo cuando la opción sea `"5"`**.
En todos los demás casos, devolvé `True` para mantener el programa corriendo.

### `main()`

Es el bucle principal. Algo como:

```python
def main():
    while True:
        opcion = mostrar_menu()
        if not ejecutar_opcion(opcion, notas):
            break
    print("¡Hasta luego!")
```

## Pistas

- Para el `match/case` en `ejecutar_opcion`:
  ```python
  match opcion:
      case "1":
          ...
      case "5":
          return False
      case _:
          print("Opción no válida.")
  ```
- Para convertir el input a número: `float(input("..."))`.
- Cuidado: `input()` puede fallar si el usuario escribe letras; puedes usar
  `try/except` para capturar el `ValueError` y avisar.

## ¿Cómo probar?

Hacé clic en **Check** y verifica que pasan los 4 tests. Cuando esté todo
verde, ejecutá el archivo (`python main.py`) y prueba las 5 opciones.
