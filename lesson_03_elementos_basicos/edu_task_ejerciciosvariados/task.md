# Ejercicios variados de texto e identificadores

En esta práctica vas a resolver dos funciones pequeñas. Separar un problema en funciones ayuda a probar cada idea por separado y a encontrar errores más rápido.

## 1. Contar vocales

implementa `contar_vocales(texto)`. Debe devolver cuántas vocales aparecen en la cadena, sin distinguir mayúsculas y minúsculas. cuenta `a`, `e`, `i`, `o`, `u` y sus versiones acentuadas; también puedes considerar `ü` como vocal. Las consonantes, los espacios y los números no se cuentan.

Por ejemplo, `contar_vocales("Panamá")` debe devolver `3`.

## 2. Revisar el inicio de un identificador

implementa `empieza_con_guión_bajo(identificador)`. Debe devolver `True` si el texto comienza con `_` y `False` en cualquier otro caso. Una cadena vacía no comienza con guión bajo.

Ejemplos:

```python
empieza_con_guión_bajo("_nota") # True
empieza_con_guión_bajo("__privado") # True
empieza_con_guión_bajo("nota") # False
```

Los tests cubren palabras con mayúsculas, acentos, cadenas sin vocales y varios identificadores.
