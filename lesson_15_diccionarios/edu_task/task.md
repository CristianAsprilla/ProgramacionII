# Práctica: agenda de contactos

Implementa una agenda de contactos usando un diccionario. Escribe estas funciones:

- `agregar_contacto(agenda, nombre, telefono)`: guarda o actualiza el teléfono asociado con
  `nombre`.
- `buscar_contacto(agenda, nombre)`: devuelve el teléfono usando `get`; si no existe, debe
  devolver `None`.
- `eliminar_contacto(agenda, nombre)`: elimina el contacto y devuelve `True`. Si no existe,
  devuelve `False`.
- `listar_contactos(agenda)`: devuelve una lista de tuplas `(nombre, telefono)` ordenada
  alfabéticamente por nombre.

Ejemplo:

```python
agenda = {}
agregar_contacto(agenda, "Ana", "6000-1234")
agregar_contacto(agenda, "Luis", "6000-5678")
print(buscar_contacto(agenda, "Ana"))  # 6000-1234
print(listar_contactos(agenda))        # [("Ana", "6000-1234"), ("Luis", "6000-5678")]
```

No necesitas crear un menú ni leer datos. Practica `get`, `pop`, `items` y la actualización de
valores mediante una clave.
