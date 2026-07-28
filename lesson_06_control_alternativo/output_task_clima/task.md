# Estado del clima en Panamá con match/case

En Panamá tenemos cuatro estaciones del año bien marcadas: **lluviosa** (mayo–noviembre), **seca** (diciembre–abril), y dos transiciones cortas llamadas **transición_1** y **transición_2** en algunos reportes climáticos.

Implementa un programa en `main.py` que lea un código numérico (1, 2, 3 o 4) desde la entrada estándar y muestre el nombre de la estación usando `match`/`case`.

| Código | Estación     |
|--------|--------------|
| 1      | `Seca`       |
| 2      | `Lluviosa`   |
| 3      | `Lluvioso`   |
| 4      | `Soleado`    |

Si el código está fuera de 1–4, imprime `Código inválido`.

Por ejemplo, para la entrada `3` la salida debe ser:

```
Lluvioso
```

> Tip: usa `match`/`case` (introducido en Python 3.10) y un caso `_` para el manejo por defecto.
