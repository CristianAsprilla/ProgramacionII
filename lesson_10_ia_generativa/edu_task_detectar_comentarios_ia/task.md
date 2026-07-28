# Ejercicio: detectar comentarios redundantes de IA

El codigo generado por IA a veces incluye comentarios innecesarios como "Esta funcion hace X" o "Ahora retornamos Y". En esta actividad vas a detectarlos.

## Objetivo

Implementa `tiene_comentarios_redundantes(codigo)` que retorne `True` si el codigo tiene comentarios que parecen generados por IA.

## Patrones a detectar

| Patron | Ejemplo |
|--------|---------|
| "esta funcion" / "esta clase" / "este metodo" | "# Esta funcion suma dos numeros" |
| "ahora retornamos" / "ahora hacemos" | "# Ahora retornamos el resultado" |
| "el siguiente codigo" | "# El siguiente codigo hace X" |

## Pistas

- Convierte el codigo a minusculas antes de buscar.
- Cuenta los patrones detectados. Si hay al menos 1, retorna True.
- Comentarios utiles (ej: "# Algoritmo de Euclides") NO son redundantes.

## ¿Como probar?

Hace clic en **Check** y verifica que los 5 tests pasen.