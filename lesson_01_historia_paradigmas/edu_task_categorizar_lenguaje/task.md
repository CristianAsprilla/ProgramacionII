# Ejercicio: categorizar lenguajes por epoca

En esta actividad vas a clasificar lenguajes de programacion segun su ano de creacion, una habilidad util para entender la evolucion del software.

## Objetivo

Implementa la funcion `categoria_por_ano(ano)` que retorna un string segun estas reglas:

| Rango | Categoria |
|-------|-----------|
| Antes de 1990 | "antiguo" |
| 1990 a 2010 (inclusive) | "moderno" |
| Despues de 2010 | "reciente" |

## Ejemplos

```python
>>> categoria_por_ano(1972)  # C
"antiguo"

>>> categoria_por_ano(1995)  # Java
"moderno"

>>> categoria_por_ano(2020)  # reciente
"reciente"
```

## Pistas

- Usa `if`, `elif` y `else` para evaluar los rangos.
- 1990 y 2010 son **inclusivos** en el rango "moderno".
- Compara con `<` y `>=`.

## ¿Como probar?

Hace clic en **Check** y verifica que los 5 tests pasen.