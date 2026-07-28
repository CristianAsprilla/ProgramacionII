# Lección 15: Diccionarios

Un **diccionario** almacena datos en pares **clave: valor**. La clave identifica un dato y el
valor contiene la información asociada. Es parecido a buscar un nombre en una agenda: no
recorres todas las páginas, sino que usas el nombre como clave.

## Declaración y acceso

```python
estudiante = {
    "nombre": "María",
    "grado": 11,
    "promedio": 4.6,
}

print(estudiante["nombre"])
print(estudiante["promedio"])
```

Las claves deben ser únicas. Si asignas un valor a una clave que ya existe, actualizas ese
valor. Acceder con `diccionario[clave]` produce `KeyError` si la clave no existe; `get` permite
usar un valor alternativo:

```python
print(estudiante.get("correo", "No registrado"))
```

## Métodos principales

| Método | Uso | Propósito |
|---|---|---|
| `keys()` | `agenda.keys()` | Obtiene las claves |
| `values()` | `agenda.values()` | Obtiene los valores |
| `items()` | `agenda.items()` | Obtiene pares clave-valor |
| `get()` | `agenda.get("Ana")` | Consulta sin error si falta la clave |
| `update()` | `agenda.update(otra)` | Agrega o actualiza varios pares |
| `pop()` | `agenda.pop("Ana")` | Elimina una clave y devuelve su valor |

También puedes agregar o cambiar un dato con asignación directa:

```python
agenda = {}
agenda["Ana"] = "6000-1234"
agenda.update({"Luis": "6000-5678"})
telefono = agenda.pop("Ana")
```

Usa `pop` solo cuando estés seguro de que la clave existe o proporciona un valor
predeterminado, por ejemplo `agenda.pop("Ana", None)`.

## Iteración

Para recorrer las claves:

```python
for nombre in agenda:
    print(nombre)
```

Para recorrer claves y valores al mismo tiempo:

```python
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")
```

## Aplicaciones

- **Agenda de contactos:** el nombre puede ser la clave y el teléfono, el valor.
- **Contador de frecuencia:** guardar cuántas veces aparece cada palabra.
- **Configuración:** asociar opciones como `"idioma"`, `"tema"` o `"notificaciones"` con sus
  valores.

Un diccionario es especialmente útil cuando buscamos por una etiqueta conocida, mientras que
una lista es conveniente cuando nos importa mantener una secuencia de posiciones.

**Idea clave:** los diccionarios organizan la información para encontrarla, actualizarla y
recorrerla mediante claves.
