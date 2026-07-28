# Calculadora simple

Los operadores aritméticos permiten construir herramientas útiles a partir de entradas pequeñas. En esta práctica vas a reunir suma, resta, multiplicación y división en una sola función.

## Tu tarea

implementa `calcular(a, b, operacion)`, que recibe dos números y una cadena con una de estas operaciones:

- `"suma"`
- `"resta"`
- `"multiplicacion"`
- `"division"`

devuelve el resultado correspondiente. Para mantener un comportamiento claro, cuando se intente dividir entre cero devuelve `None`. Si recibís otro nombre de operación, lanzá `ValueError`.

Ejemplos:

```python
calcular(8, 5, "suma") # 13
calcular(8, 5, "resta") # 3
calcular(8, 5, "multiplicacion") # 40
calcular(8, 5, "division") # 1.6
calcular(8, 0, "division") # None
```

Los tests comprueban las cuatro operaciones, la división por cero y el manejo de una operación desconocida.
