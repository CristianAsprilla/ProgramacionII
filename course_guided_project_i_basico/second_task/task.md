# Paso 2: Crear la tarjeta completa

¡Bien, ya tienes el saludo! Ahora vamos a **expandir** el programa para construir la
tarjeta de presentación completa.

## Objetivo

En `main.py` ya tienes tu función `crear_saludo` (del paso anterior) y una función
nueva `crear_tarjeta(...)` que está vacía. Tu trabajo es implementar
`crear_tarjeta` para que devuelva un texto formateado con los datos del estudiante.

La función recibe estos parámetros:

| Parámetro | Tipo | Descripción |
|---|---|---|
| `nombre` | `str` | Nombre del estudiante |
| `edad` | `int` | Edad |
| `carrera` | `str` | Carrera que estudia |
| `trimestre` | `int` | Trimestre actual (1, 2 o 3) |
| `promedio` | `float` | Promedio de notas |
| `materias` | `int` | Cantidad de materias inscritas |

## Ejemplo de salida esperada

```
========================================
   TARJETA DE PRESENTACIÓN DEL ESTUDIANTE
========================================
Nombre:           María
Edad:             17 años
Programa:        Bachillerato Tecnico
Trimestre actual: III
Promedio de notas: 92.5
Materias inscritas: 6
========================================
¡Éxito en tu trimestre!
```

## Pistas

- El parámetro `trimestre` viene como número (1, 2, 3). Para mostrar "I", "II" o "III"
  puedes usar una lista `["I", "II", "III"][trimestre - 1]` o un `if/elif/else`.
- Usá `\n` para los saltos de línea dentro del string.
- No te preocupes por alinear las columnas con espacios exactos: los tests
  verifican que los **datos** estén, no el formato pixel-perfect.

## ¿Cómo probar?

Hacé clic en **Check** y verifica que pasan los 5 tests. Si todos pasan, ¡tu
tarjeta de presentación está lista!
