# Calculadora de IMC

El **Índice de Masa Corporal (IMC)** se calcula dividiendo el peso (en kg) entre la altura al cuadrado (en metros). Es una referencia rápida que usan los nutricionistas, por ejemplo en los centros de salud de Panamá, para clasificar el estado nutricional de una persona.

Implementa `evaluar_imc(peso, altura)` para que devuelva un string con la categoría correcta:

| IMC | Categoría |
|---|---|
| menor a 18.5 | `"Bajo peso"` |
| entre 18.5 y 24.9 | `"Normal"` |
| entre 25 y 29.9 | `"Sobrepeso"` |
| 30 o más | `"Obesidad"` |

Conserva las validaciones: altura `<= 0` debe lanzar `ValueError("La altura debe ser mayor a 0")` y peso `< 0` debe lanzar `ValueError("El peso no puede ser negativo")`. Recuerda que `elif` te permite encadenar rangos sin repetir comparaciones.