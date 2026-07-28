# Quiz de escritorio: refactorizacion

## Pregunta

Observa este codigo redundante:

```python
precio1 = 100
precio2 = 200
precio3 = 50
total = (precio1 + precio2 + precio3) * 1.07
print(total)

otro_total = (50 + 30 + 20) * 1.07
print(otro_total)
```

¿Cual es la mejor forma de refactorizarlo?

## Pista

La refactorizacion busca hacer el codigo mas legible y mantenible. Extraer logica repetida a una funcion nombrada es la mejor practica.