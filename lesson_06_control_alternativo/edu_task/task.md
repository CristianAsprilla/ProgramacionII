# Clasificador de notas del colegio

Los **colegios de Panamá** evalúan con una escala de **1.0 a 5.0**, donde **3.0 es el mínimo aprobatorio**. Completa `clasificar_nota_colegio(nota)` para que reciba una nota (float) entre 1.0 y 5.0 y devuelva el descriptor correcto:

| Rango | Descriptor |
|---|---|
| `4.5 ≤ nota ≤ 5.0` | `"Excelente"` |
| `4.0 ≤ nota < 4.5` | `"Muy bueno"` |
| `3.5 ≤ nota < 4.0` | `"Bueno"` |
| `3.0 ≤ nota < 3.5` | `"Mínimo aprobatorio"` |
| `nota < 3.0` | `"Reprobado"` |

> Nota: esta función representa la escala del colegio (1.0–5.0). En la universidad la escala es 0–100; si ves ejemplos con ese rango en otro material, son de nivel universitario, no del Bachillerato Tecnico.

Conserva la validación: una nota fuera del rango 1.0–5.0 debe lanzar `ValueError("La nota debe estar entre 1.0 y 5.0")`.
