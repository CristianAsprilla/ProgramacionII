# Subrutinas y modularización

Una **subrutina** es un bloque reutilizable. Tradicionalmente, un procedimiento realiza una acción sin devolver un resultado y una función sí devuelve uno. En Python ambos se escriben con `def`; un procedimiento suele retornar `None`.

```python
def mostrar_total(total: float) -> None:
    print(f"Total: B/. {total:.2f}")

def sumar(a: float, b: float) -> float:
    return a + b
```

## Parámetros y objetos

Python comparte referencias a objetos con la función. Reasignar un parámetro no cambia la variable externa, pero modificar un objeto mutable, como una lista, sí puede observarse afuera.

```python
def agregar(lista, dato):
    lista.append(dato)  # modifica el mismo objeto
```

## Módulos y paquetes

Un archivo `.py` es un módulo. Podemos usar `import geometria` o `from geometria import area_circulo`. Un paquete organiza varios módulos en una carpeta, normalmente con `__init__.py`. Evita `from modulo import *`: hace menos claro el origen de cada nombre.

Separar responsabilidades facilita probar, reutilizar y corregir el código. Al terminar podrás distribuir un programa entre módulos y entender qué ocurre al pasar objetos como argumentos.
