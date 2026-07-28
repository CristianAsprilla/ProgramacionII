# Quiz de escritorio: acceso a diccionario

## Pregunta

¿Que imprime este codigo?

```python
d = {"nombre": "Ana", "edad": 17}
print(d["edad"])
```

## Pista

`d["edad"]` accede al valor asociado a la clave `"edad"`. Como previamente `d["edad"] = 17`, devuelve `17`. A diferencia de `d.get("edad")`, esto lanza KeyError si la clave no existe.