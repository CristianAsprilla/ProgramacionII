Ya conoces las **palabras reservadas** (keywords) de Python. Ahora vamos a
usarlas en un programa.

### Ejercicio

Vas a implementar la función `contar_palabras_reservadas(lineas)` que está
declarada en `main.py`. La función debe:

1. Recibir una **lista de strings** (cada elemento es una línea de código o
 texto).
2. Devolver un **entero** con la **cantidad total** de palabras reservadas
 que aparecen en todas las líneas.

#### Detalles importantes

- Una palabra reservada cuenta **cada vez que aparece**. Si en una línea hay
 `for i in range(10):`, se cuentan `for` **e** `in` (es decir, 2).
- **NO** cuentes substrings: `informacion` no debe contar como `in`. Solo
 cuenta la palabra completa.
- Las keywords disponibles están en `keyword.kwlist` (ya importado en el
 archivo).
- Si la lista está vacía, devuelve `0`.

#### Pista: ¿cómo lo implementarías?

puedes recorrer cada línea, dividirla en palabras (por ejemplo, usando
`linea.split()`) y verificar si cada palabra está en `keyword.kwlist`.

#### Ejemplo

```python
lineas = [
 "for i in range(10):", # for, in -> 2
 "if x > 0 and y < 10:", # if, and -> 2
 "print('Hola, mundo')", # -> 0
 "return resultado", # return -> 1
]
# Resultado esperado: 5
```

#### Tests

`tests/test.py` ejecuta casos de prueba con `unittest`. Vas a poder verificar
tu solución con el botón *Check*. Si los tests no pasan, revisa tu lógica y
volvé a intentarlo.