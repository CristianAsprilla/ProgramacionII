# Lección 13: Listas dinámicas

Las listas de Python son **estructuras dinámicas**: su cantidad de elementos puede cambiar
mientras el programa está funcionando. Esto es útil cuando no sabemos de antemano cuántos
productos comprará una familia, cuántas personas asistirán a una actividad o cuántos datos
llegarán desde el teclado.

## Frente a los arreglos estáticos

En un arreglo estático de tamaño fijo, como algunos arreglos de C o Java, se reserva espacio
para una cantidad determinada de elementos. Para guardar más datos hay que crear otra
estructura. En cambio, una lista de Python administra su capacidad automáticamente y permite
agregar o quitar elementos con métodos sencillos.

```python
compras = []
compras.append("arroz")
compras.append("frijoles")
```

La lista crece después de cada `append`. Sigue siendo importante controlar los datos que recibe
el programa: que un producto no esté vacío, que un elemento exista antes de eliminarlo y que el
orden tenga sentido para la persona usuaria.

## Operaciones avanzadas

| Método | Ejemplo | Resultado |
|---|---|---|
| `append` | `compras.append("leche")` | Agrega un elemento al final |
| `extend` | `compras.extend(["pan", "café"])` | Agrega todos los elementos de otra lista |
| `insert` | `compras.insert(0, "agua")` | Inserta en una posición |
| `remove` | `compras.remove("pan")` | Elimina la primera coincidencia |
| `pop` | `ultimo = compras.pop()` | Elimina y devuelve un elemento |
| `clear` | `compras.clear()` | Vacía la lista |
| `copy` | `respaldo = compras.copy()` | Crea una copia independiente |

`remove` genera `ValueError` si el elemento no existe, por lo que puedes comprobar primero
`if producto in compras`. `pop(indice)` permite extraer una posición específica.

## Comprensiones de listas

Una comprensión de listas crea una lista nueva de manera compacta. Por ejemplo, para obtener
los productos escritos en mayúsculas:

```python
productos = ["arroz", "leche", "pan"]
mayusculas = [producto.upper() for producto in productos]
```

También puedes filtrar elementos:

```python
precios = [1.25, 4.50, 2.00, 8.75]
precios_mayores = [precio for precio in precios if precio > 4]
```

Para empezar, identifica siempre tres cosas: la lista original, la operación aplicada a cada
elemento y la condición opcional.

## Diseñar operaciones con funciones

Separar cada acción en una función hace que el programa sea más fácil de probar y mantener.
Una lista de compras puede tener funciones para **agregar**, **eliminar**, **buscar** y
**listar** productos. Las funciones reciben la lista como parámetro y la modifican o devuelven
información sobre ella.

**Idea clave:** una lista dinámica no solo guarda datos; también ofrece operaciones para que el
programa se adapte a una cantidad cambiante de información.
