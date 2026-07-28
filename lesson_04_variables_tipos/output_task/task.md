Ya manejamos **variables** y **tipos de datos**. Ahora vamos a leer
información del usuario usando la entrada estándar (`stdin`).

### Ejercicio

Escribí un programa en `main.py` que:

1. **Lea un número entero** desde `stdin` (la entrada estándar, usando `input()`).
2. **Imprima** dos líneas:
 - En la primera: el **tipo** del valor leído (tiene que ser `int`).
 - En la segunda: el **doble** del número.

#### Pista

`input()` siempre devuelve un `str`. Para obtener un `int` usa
`int(input())`. El nombre del tipo lo puedes sacar con `type(x).__name__`.

#### Ejemplo

Si la entrada es:

```
42
```

La salida debe ser:

```
Tipo: int
Doble: 84
```

> 💡 **Tip**: la función `type(x)` devuelve un objeto `type`. Si quieres el
> nombre como cadena (por ejemplo `"int"`), usa `type(x).__name__`.