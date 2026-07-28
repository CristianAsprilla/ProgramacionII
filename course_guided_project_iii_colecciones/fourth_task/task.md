# Paso 4: Matriz de ventas y menú final

¡Último paso del curso! Ahora vas a cerrar el proyecto integrando una **matriz
de ventas** y el **menú principal** que conecta todas las funciones.

## Estructura de la matriz de ventas

Una **matriz 4x3** (lista de listas) con esta forma:

```
              Prod 0   Prod 1   Prod 2
Trim I          [v,      v,        v]
Trim II         [v,      v,        v]
Trim III        [v,      v,        v]
Total anual     [v,      v,        v]
```

- Las **3 primeras filas** son los trimestres 1, 2 y 3.
- La **cuarta fila** es el total anual (se actualiza automáticamente).
- Las **columnas** son los productos del catálogo.

## Funciones a implementar

### `registrar_venta(ventas, indice_producto, trimestre, cantidad)`

Suma `cantidad` a la celda del producto y trimestre dados, y también a la
celda del total anual.

```python
>>> ventas = [[0, 0, 0]] * 3 + [[0, 0, 0]]
>>> registrar_venta(ventas, 0, 1, 5)
>>> ventas[0][0]
5
>>> ventas[3][0]
5
```

### `generar_reporte(ventas, catalogo)`

Devuelve un `str` con el reporte formateado, por ejemplo:

```
Reporte de ventas (unidades)
                Cuaderno   Lapiz   Borrador
Trim I               5         0         0
Trim II              3         0         0
Trim III             2         0         0
Total              10         0         0
```

### `ejecutar_opcion(opcion)` y `main()`

Conectá todo en el menú:

| Opción | Acción |
|---|---|
| `"1"` | Pedir nombre, precio, stock; agregar producto; apilar la op. |
| `"2"` | Pedir nombre; buscar y mostrar. |
| `"3"` | Pedir nombre y delta; actualizar stock; apilar la op. |
| `"4"` | Llamar a `deshacer()` y mostrar el mensaje. |
| `"5"` | Imprimir el reporte. |
| `"6"` | Devolver `False`. |

## Pistas

- Para el `match/case`, fíjate en el patrón del Proyecto II.
- Para `main()`, usa `while True` con un `if not ejecutar_opcion(...): break`.
- El test verifica que `ejecutar_opcion("6")` devuelva `False` y que una
  opción inválida **no** termine el programa.

## ¿Cómo probar?

Hacé clic en **Check** y verifica que pasan los 7 tests. Cuando esté todo
verde, ejecutá `python main.py` y prueba todas las opciones del menú.
