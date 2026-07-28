# Ejercicio: clasificar edad en categoria

Una operacion comun en programas es clasificar valores en rangos. En esta actividad vas a implementar una funcion que clasifica edades en categorias.

## Objetivo

Implementa `clasificar_edad(edad)` que retorne:

| Edad | Categoria |
|------|-----------|
| 0-12 (inclusive) | "nino" |
| 13-17 (inclusive) | "adolescente" |
| 18-64 (inclusive) | "adulto" |
| 65 o mas | "adulto mayor" |

## Ejemplos

```python
>>> clasificar_edad(8)
"nino"

>>> clasificar_edad(15)
"adolescente"

>>> clasificar_edad(30)
"adulto"

>>> clasificar_edad(70)
"adulto mayor"
```

## Pistas

- Usa `if`, `elif` y `else`.
- Los limites son **inclusivos**: 12 es "nino", 13 es "adolescente".

## ¿Como probar?

Hace clic en **Check** y verifica que los 5 tests pasen.