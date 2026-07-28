# Sentencias repetitivas

Un ciclo repite instrucciones. `while` continúa mientras su condición sea verdadera; asegúrate de modificar la variable de control para evitar un ciclo infinito.

```python
cuenta = 3
while cuenta > 0:
    print(cuenta)
    cuenta -= 1
```

`for` recorre elementos. `range(inicio, fin, paso)` genera enteros sin incluir `fin`: `range(1, 6)` produce del 1 al 5.

```python
for estacion in range(1, 4):
    print("Estación", estacion)
```

`break` termina el ciclo; `continue` salta a la próxima vuelta. Úsalos con intención, porque demasiados saltos dificultan seguir el programa.

```python
for numero in range(1, 10):
    if numero == 7:
        break
    if numero % 2 == 0:
        continue
    print(numero)
```

Los ciclos pueden anidarse. Por ejemplo, uno recorre filas y otro columnas; el ciclo interno se completa por cada vuelta del externo.

Al terminar podrás escoger entre `while` y `for`, controlar un ciclo y resolver secuencias numéricas.
