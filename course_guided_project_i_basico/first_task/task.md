# Paso 1: Crear la función de saludo

En este primer paso vas a implementar la función `crear_saludo(nombre, edad)` que
se usará como base para tu tarjeta de presentación.

## Objetivo

La función debe recibir un `nombre` (texto) y una `edad` (número entero), y
**devolver un saludo personalizado** que contenga ambos datos.

## Ejemplo de comportamiento esperado

```python
>>> crear_saludo("María", 17)
"¡Hola María! Tenés 17 años. Bienvenido al Bachillerato Tecnico de Panama."
```

## Pistas

- Usá una **f-string** (`f"..."`) para concatenar el nombre y la edad de forma
  legible.
- El saludo no tiene que ser exactamente igual al ejemplo, pero **debe mencionar
  el nombre y la edad** (esto es lo que verifican los tests).
- Mantenelo corto: una sola línea de texto es suficiente.

## ¿Cómo probar?

Hacé clic en el botón **Check** cuando hayas escrito tu solución. Los tests
asegurarán que el saludo contiene tu nombre y tu edad.
