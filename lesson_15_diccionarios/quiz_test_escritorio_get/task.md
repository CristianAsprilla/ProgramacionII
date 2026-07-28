# Quiz de escritorio: dict.get

## Pregunta

¿Que imprime este codigo?

```python
d = {"nombre": "Ana", "edad": 17}
print(d.get("ciudad"))
```

## Pista

A diferencia de `d["ciudad"]` (que lanza `KeyError`), `d.get("ciudad")` retorna `None` si la clave no existe. Es una forma segura de acceder al diccionario.