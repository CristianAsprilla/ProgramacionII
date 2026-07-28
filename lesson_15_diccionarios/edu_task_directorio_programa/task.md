# Ejercicio: directorio del programa academico

En esta actividad vas a aplicar lo aprendido sobre **diccionarios** para representar informacion estructurada de un programa academico.

## Objetivo

Implementa la funcion `directorio_programa()` que devuelva un diccionario con datos basicos de un programa de **Bachillerato Tecnico** de Panama.

## Claves requeridas

El diccionario devuelto debe tener al menos estas 4 claves:

| Clave | Valor esperado (ejemplo) |
|-------|--------------------------|
| `carrera` | `"Bachillerato Tecnico"` |
| `instituto` | `"Colegio Panama"` |
| `modalidad` | `"Cientifico-tecnologica"` |
| `duracion` | `"3 anos"` |

## Ejemplo de uso

```python
>>> directorio_programa()
{'carrera': 'Bachillerato Tecnico', 'instituto': 'Colegio Panama',
 'modalidad': 'Cientifico-tecnologica', 'duracion': '3 anos'}
```

## Pistas

- Podes usar la sintaxis `{"clave": "valor", ...}` para crear el diccionario.
- Todos los valores son strings.
- Podes agregar mas claves si queres (ciudad, lema, etc.) pero las 4 indicadas son obligatorias.

## ¿Como probar?

Hace clic en **Check** y verifica que los 6 tests pasen.