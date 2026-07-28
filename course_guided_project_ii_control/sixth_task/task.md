# Paso 6: clasificar el desempeno

En este paso vas a clasificar el promedio segun la escala del colegio.

## Objetivo

### `clasificar_desempeno(promedio)`

| Promedio | Clasificacion |
|---|---|
| >= 4.5 | "Excelente" |
| >= 4.0 | "Muy bueno" |
| >= 3.5 | "Bueno" |
| >= 3.0 | "Suficiente" |
| < 3.0 | "Insuficiente" |

### `resumen_desempeno(notas)`

Retorna un diccionario con:

| Clave | Valor |
|---|---|
| `promedio` | promedio de las notas (float) |
| `max` | nota maxima |
| `min` | nota minima |
| `clasificacion` | string de `clasificar_desempeno` |
| `aprobado` | True si promedio >= 3.0, False si no |

## Pistas

- Para `clasificar_desempeno`: usa `if/elif/else` en orden de mayor a menor.
- Para `resumen_desempeno`: reutiliza `calcular_promedio`, o recalcula aqui con `sum(notas)/len(notas)`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 8 tests pasen.
