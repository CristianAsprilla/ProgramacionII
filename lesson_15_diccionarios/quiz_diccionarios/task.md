# Quiz: acceso e iteración de diccionarios

Observa el siguiente programa:

```python
datos = {
    "curso": "Programación II",
    "grado": 11,
    "activo": True,
}

print(datos["curso"])
print(datos.get("docente", "Pendiente"))
print(list(datos.keys()))
```

¿Cuál es la salida del programa? Selecciona una sola opción. Recuerda que `get` devuelve el
valor alternativo cuando una clave no existe y que `keys()` recorre las claves en el orden en
que fueron insertadas.
