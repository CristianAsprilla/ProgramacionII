# Ejercicio: Calculadora de IMC

En este ejercicio vas a implementar una **calculadora de Índice de Masa
Corporal (IMC)** y una función que **clasifica** el resultado según los
rangos de la OMS.

## La fórmula

```
IMC = peso / altura²
```

Por ejemplo, una persona de 70 kg y 1.75 m tiene un IMC de:

```
IMC = 70 / (1.75 * 1.75) = 22.86
```

## Funciones a implementar

### `calcular_imc(peso, altura)`

- Recibe `peso` (float, en kg) y `altura` (float, en metros).
- Devuelve el IMC **redondeado a 2 decimales** usando `round()`.

```python
>>> calcular_imc(70, 1.75)
22.86
```

### `clasificar_imc(imc)`

Devuelve un `str` con la categoría según estos rangos:

| Rango | Categoría |
|---|---|
| `IMC < 18.5` | `"Bajo peso"` |
| `18.5 <= IMC < 25` | `"Normal"` |
| `25 <= IMC < 30` | `"Sobrepeso"` |
| `IMC >= 30` | `"Obesidad"` |

```python
>>> clasificar_imc(22.86)
"Normal"
>>> clasificar_imc(31.5)
"Obesidad"
```

## Pistas

- Para el IMC: `imc = peso / (altura ** 2)` y `return round(imc, 2)`.
- Para clasificar usa `if/elif/else` con los rangos en orden.
- Si el IMC está **exactamente** en el límite (por ejemplo, 18.5), debe
 caer en la categoría "Normal", no en "Bajo peso".

## ¿Cómo probar?

Hacé clic en **Check** y verifica que pasan los 8 tests.
