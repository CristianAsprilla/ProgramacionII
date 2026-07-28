# Comparar código generado con tu propio criterio

Cuando le pides código a una IA generativa, el primer paso sano es **contar** cuántas líneas útiles te devolvió, ignorando líneas vacías y comentarios. Eso te ayuda a comparar dos propuestas (por ejemplo, una escrita por ti y otra generada por el asistente) y a detectar respuestas infladas con texto que no aporta lógica.

Implementa `contar_lineas_codigo(texto)`. Una línea cuenta como código si:

1. Tiene algún carácter distinto de espacios o saltos de línea (no está vacía).
2. **No** comienza con `#` después de eliminar espacios al inicio (no es un comentario).

El texto puede venir como un solo string con saltos de línea (`\n`). Divídelo con `texto.splitlines()` y revisa cada línea.