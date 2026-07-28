# Funciones: definición, parámetros y retorno

Una función agrupa una tarea reutilizable. Se define con `def`; sus parámetros reciben datos y `return` entrega un resultado.

```python
def calcular_itbms(precio: float) -> float:
    """Calcula el 7 % de ITBMS de un precio."""
    return precio * 0.07
```

La cadena entre comillas triples es un **docstring**: explica el propósito. Los *type hints* (`float`, `-> float`) documentan tipos y ayudan al IDE, aunque Python no los obliga durante la ejecución.

Los argumentos pueden enviarse por posición (`saludar("Luis", "Buenos días")`) o por nombre (`saludar(saludo="Hola", nombre="Luis")`). Un parámetro puede tener valor predeterminado, pero los parámetros sin valor deben aparecer primero.

Una función `lambda` representa una expresión corta y anónima:

```python
doble = lambda numero: numero * 2
print(doble(5))
```

Prefiere `def` cuando la lógica necesite varias líneas o documentación. Al terminar podrás diseñar funciones claras, invocarlas de distintas formas y devolver resultados.
