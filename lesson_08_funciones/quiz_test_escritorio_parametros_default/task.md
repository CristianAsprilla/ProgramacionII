# Quiz de escritorio: parametros por defecto

## Pregunta

¿Que imprime este codigo?

```python
def saludar(nombre="Maria"):
    print("Hola, " + nombre)

saludar("Ana")
```

## Pista

Cuando llamas a una funcion con argumento, ese argumento **reemplaza** al valor por defecto. `saludar("Ana")` usa `"Ana"`, no `"Maria"`.