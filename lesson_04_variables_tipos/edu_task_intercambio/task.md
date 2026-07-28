# Intercambiá dos variables

En Python puedes intercambiar valores sin crear una variable temporal. La expresión `a, b = b, a` usa una tupla para conservar ambos valores y asignarlos en el orden nuevo.

## Tu tarea

implementa `intercambiar(a, b)`. La función debe devolver una **tupla** con `b` en la primera posición y `a` en la segunda:

```python
intercambiar(3, 8) # (8, 3)
intercambiar(-4, 7) # (7, -4)
intercambiar("Colón", "Panamá") # ("Panamá", "Colón")
```

No cambies los valores originales fuera de la función; simplemente devuelve el par intercambiado. Los tests incluyen números positivos, números negativos y textos relacionados con nuestro país.
