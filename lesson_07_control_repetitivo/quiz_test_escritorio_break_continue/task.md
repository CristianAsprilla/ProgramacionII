# Quiz de escritorio: continue

## Pregunta

¿Que imprime este codigo?

```python
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i, end=" ")
```

## Pista

`continue` salta a la siguiente iteracion sin ejecutar el resto del bloque. Si `i` es par (`i % 2 == 0`), se ejecuta `continue` y no se imprime.