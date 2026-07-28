# Paso 4: IMC y categoria de salud

En este paso vas a anadir informacion de salud a la tarjeta. Implementa dos funciones que calculan el IMC y clasifican el resultado.

## Objetivo

### `calcular_imc(peso_kg, altura_m)`

Calcula el IMC: `IMC = peso / altura^2`. Redondea a 2 decimales con `round()`.

```python
>>> calcular_imc(70, 1.75)
22.86
```

### `categoria_imc(imc)`

Clasifica el IMC en una categoria segun la OMS:

| Rango | Categoria |
|---|---|
| IMC < 18.5 | `bajo peso` |
| 18.5 <= IMC < 25 | `normal` |
| 25 <= IMC < 30 | `sobrepeso` |
| IMC >= 30 | `obesidad` |

## Pistas

- Usa `round(valor, 2)` para el IMC.
- Usa `if/elif/else` para la categoria.
- Cuidado con el orden de las comparaciones (de menor a mayor).

## ¿Como probar?

Hace clic en **Check** y verifica que los 6 tests pasen.
