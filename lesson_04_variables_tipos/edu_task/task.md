Ahora que conoces **variables**, **constantes** y **tipos de datos**, vamos a
usarlos en un programa concreto.

### Ejercicio

Vas a implementar la función `datos_rectangulo(base, altura)` declarada en
`main.py`. La función debe:

1. Recibir dos números: `base` y `altura` (en metros).
2. Calcular:
 - **Área** = `base * altura`
 - **Perímetro** = `2 * (base + altura)`
3. Devolver un **diccionario** con dos claves: `"area"` y `"perimetro"`.

#### Pista

```python
return {"area": ..., "perimetro": ...}
```

#### Ejemplo

```python
datos_rectangulo(8.5, 4.2)
# -> {"area": 35.7, "perimetro": 25.4}
```

#### Tests

`tests/test.py` ejecuta casos de prueba con `unittest`. Vas a poder verificar
tu solución con el botón *Check*.