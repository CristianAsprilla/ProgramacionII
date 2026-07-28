# Lección 14: Pilas (LIFO)

Una **pila** es una estructura de datos en la que el último elemento que entra es el primero
que sale. Esta regla se conoce como **LIFO**, por sus siglas en inglés: *Last In, First Out*
(último en entrar, primero en salir).

Imagina una pila de platos en el comedor de Panamá: colocas un plato arriba y, normalmente,
tomas primero el plato que está arriba. No puedes retirar cómodamente uno del medio sin mover
los demás.

## Operaciones de una pila

- **push**: colocar un elemento en la cima.
- **pop**: quitar y devolver el elemento de la cima.
- **peek**: consultar la cima sin quitarla.
- **is_empty**: comprobar si no hay elementos.

En Python podemos usar una lista como pila. `append` funciona como `push` y `pop()` sin
argumentos quita el último elemento:

```python
pila = []
pila.append("primero")
pila.append("segundo")
print(pila[-1])  # peek: segundo
print(pila.pop())  # pop: segundo
print(pila.pop())  # pop: primero
print(len(pila) == 0)  # is_empty: True
```

Antes de usar `pop` o consultar la cima, conviene comprobar si la pila está vacía. Así evitamos
intentar retirar un elemento que no existe.

## Aplicaciones

### Deshacer acciones

Un editor puede guardar cada acción en una pila. Al elegir **deshacer**, extrae la última
acción y revierte ese cambio. Si se desea rehacer, puede usarse una segunda pila.

### Historial de navegación

Cada página visitada se apila. El botón «atrás» extrae la página actual y muestra la anterior.

### Paréntesis balanceados

Para validar una expresión, se apilan los símbolos de apertura `(`, `[`, `{`. Al encontrar un
símbolo de cierre, se compara con la cima: debe ser su apertura correspondiente. Si no coincide,
la expresión no está balanceada. Al terminar, la pila debe quedar vacía.

Por ejemplo, `a * (b + [c - d])` está balanceada, mientras que `([)]` no lo está porque el
cierre `)` no corresponde a la apertura que está en la cima.

**Idea clave:** una pila restringe el acceso a un extremo, la cima, y esa restricción hace que
las operaciones LIFO sean claras y útiles.
