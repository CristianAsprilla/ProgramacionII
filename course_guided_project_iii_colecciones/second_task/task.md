# Paso 2: Historial de operaciones (lista dinámica)

En este paso vas a implementar un **historial** de todas las operaciones que se
hacen sobre el catálogo. Esto te servirá en el Paso 3 para implementar
"deshacer" (undo).

## Estructura del historial

El historial es una **lista dinámica** donde cada elemento es un diccionario
con la forma:

```python
{
    "tipo": "agregar",            # o "actualizar", "eliminar", etc.
    "detalles": {                 # datos específicos de la operación
        "nombre": "Cuaderno",
        "precio": 2.5,
        "stock": 20,
    },
    # Opcional: un campo extra con la fecha/hora para auditoría
}
```

## Funciones a implementar

### `registrar_operacion(historial, tipo, detalles)`

Agrega un nuevo diccionario a la lista `historial` con los campos
`"tipo"` y `"detalles"`. Opcionalmente puedes agregar un campo
`"timestamp"` con `datetime.now().isoformat()`.

```python
>>> historial = []
>>> registrar_operacion(historial, "agregar", {"nombre": "Cuaderno"})
>>> historial
[{'tipo': 'agregar', 'detalles': {'nombre': 'Cuaderno'}}]
```

### `ver_historial(historial)`

Devuelve un `str` listo para imprimir:

- Si está vacío: `"Sin operaciones todavía."`
- Si tiene operaciones: una por línea, numerada, mostrando el tipo y los
  detalles más importantes (al menos el `nombre`).

## Pistas

- Para agregar: `historial.append({...})`.
- Para formatear: usa `enumerate` o un contador manual.
- El test verifica que el **tipo** de la operación aparezca en el texto
  formateado, así que usa un formato claro (ej. `"1. agregar - Cuaderno"`).

## ¿Cómo probar?

Hacé clic en **Check** y verifica que pasan los 4 tests.
