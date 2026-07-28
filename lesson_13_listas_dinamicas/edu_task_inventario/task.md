# Práctica: inventario de la tiendita escolar del Bachillerato Tecnico

Imagina que en el colegio de Panama hay una tiendita administrada por estudiantes
de 11° grado. Cada producto tiene un **nombre**, un **precio** en balboas (B/.) y un
**stock** disponible.

## Representación de los datos

Cada producto se guarda en un diccionario con tres claves:

```python
{"nombre": "Cuaderno", "precio": 2.50, "stock": 30}
```

El inventario completo es una **lista** de diccionarios.

## Lo que tienes que hacer

Implementa las cuatro funciones siguientes:

1. `agregar_producto(nombre, precio, stock)`: agrega un producto nuevo al inventario.
   Si ya existe un producto con ese `nombre`, actualiza su precio y stock (no se duplican
   productos en la lista).

2. `vender(nombre, cantidad)`: descuenta `cantidad` del `stock` del producto. Devuelve
   `True` si la venta se realizó; devuelve `False` si no hay suficiente stock o el producto
   no existe. La cantidad vendida debe ser positiva.

3. `stock_actual(nombre)`: devuelve el stock actual del producto o `None` si no existe.

4. `listar_inventario()`: devuelve una **copia** de la lista de productos (no la lista
   original, para que cambios externos no afecten al inventario).

Ejemplos de uso:

```python
agregar_producto("Cuaderno", 2.50, 30)
agregar_producto("Lápiz", 0.50, 100)
vender("Cuaderno", 5)         # True, ahora stock = 25
vender("Cuaderno", 1000)      # False, no hay stock suficiente
stock_actual("Lápiz")         # 100
```

No imprimas nada dentro de las funciones; devuelve los valores con `return`. Recorre la
lista con un `for` y modifica el diccionario del producto cuando lo encuentres.