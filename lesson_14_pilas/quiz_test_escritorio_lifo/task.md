# Quiz de escritorio: comportamiento LIFO

## Pregunta

¿Que imprime este codigo?

```python
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila.pop())
```

## Pista

En una pila LIFO (Last In, First Out), `pop()` quita el **ultimo** elemento agregado, que fue el `3`.