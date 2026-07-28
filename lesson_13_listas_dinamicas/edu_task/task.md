# Práctica: lista de compras

Implementa cuatro funciones para administrar una lista de compras. Las funciones reciben una
lista y deben comportarse así:

- `agregar_producto(lista, producto)`: agrega `producto` al final de la lista.
- `eliminar_producto(lista, producto)`: elimina la primera coincidencia y devuelve `True`.
  Si el producto no está, devuelve `False` y deja la lista sin cambios.
- `buscar_producto(lista, producto)`: devuelve `True` si el producto aparece y `False` en caso
  contrario.
- `listar_productos(lista)`: devuelve una copia de la lista, sin modificar la original.

Ejemplo de uso:

```python
compras = []
agregar_producto(compras, "arroz")
agregar_producto(compras, "plátano")
print(buscar_producto(compras, "arroz"))  # True
eliminar_producto(compras, "arroz")
print(listar_productos(compras))         # ["plátano"]
```

No necesitas crear un menú ni leer datos. Concéntrate en las funciones y en las operaciones de
listas. La lista puede contener productos repetidos; al eliminar, quita solo la primera
coincidencia.
