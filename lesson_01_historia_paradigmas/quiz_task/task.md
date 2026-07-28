¡Muy bien! Ahora un pequeño *quiz* para verificar que los conceptos principales
sobre paradigmas quedaron claros.

### Pregunta

observa los siguientes fragmentos de código. ¿A qué **paradigma de programación**
pertenece cada uno?

```python
# Fragmento A
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x * x, numeros))
print(cuadrados)
```

```python
# Fragmento B
class Estudiante:
 def __init__(self, nombre):
 self.nombre = nombre
 self.notas = []

 def agregar_nota(self, nota):
 self.notas.append(nota)
```

```python
# Fragmento C
total = 0
for i in range(1, 11):
 total = total + i
print(total)
```

Selecciona la opción que **mejor describe** la combinación de paradigmas presentes en
el **Fragmento A**:
