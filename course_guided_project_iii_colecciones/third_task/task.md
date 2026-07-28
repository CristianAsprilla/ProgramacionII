# Paso 3: Pila para deshacer (undo)

¡Ya casi! Ahora vas a implementar el sistema de **deshacer** (undo) usando una
**pila** (estructura LIFO: *Last In, First Out*).

## ¿Cómo funciona una pila?

Pensá en una pila de platos: el último que apilás es el primero que sacás.
En Python, una **lista** funciona perfectamente como pila si usas solo dos
operaciones:

- `pila.append(x)` para **apilar**.
- `pila.pop()` para **desapilar** (y devuelve el elemento).

## Funciones a implementar

### `apilar_operacion(pila, operacion)`

Agrega la `operacion` a la `pila`. La operación tiene que tener toda la
información necesaria para revertirse después (por ejemplo, para un
"agregar" necesitas saber qué producto se agregó; para un "actualizar",
qué delta se aplicó).

```python
>>> pila = []
>>> apilar_operacion(pila, {"tipo": "agregar", "nombre": "Cuaderno"})
>>> pila
[{'tipo': 'agregar', 'nombre': 'Cuaderno'}]
```

### `deshacer(catalogo, pila)`

Saca la última operación de la pila y la **revierte** sobre el catálogo.

| Tipo de operación | Reversa |
|---|---|
| `"agregar"` | Eliminar el producto del catálogo. |
| `"actualizar"` con delta `d` | Volver a aplicar `-d` al stock. |

Devuelve un `str` con un mensaje de lo que se deshizo, o `None` si la pila
estaba vacía.

```python
>>> catalogo = {"Cuaderno": {"precio": 2.5, "stock": 20}}
>>> pila = [{"tipo": "agregar", "nombre": "Cuaderno"}]
>>> deshacer(catalogo, pila)
"Se deshizo: agregar Cuaderno"
>>> catalogo
{}
```

## Pistas

- Para la operación "agregar", al deshacer usa `del catalogo[nombre]` o
  `catalogo.pop(nombre)`.
- Para "actualizar", simplemente aplicá el delta opuesto: si guardaste
  `delta=-5`, al deshacer sumá `5` al stock.
- Usá `match/case` o `if/elif` para distinguir el tipo de operación.

## ¿Cómo probar?

Hacé clic en **Check** y verifica que pasan los 5 tests.
