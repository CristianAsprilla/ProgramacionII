# Analizá identificadores en código

Los identificadores son los nombres que usamos para variables, funciones y otros elementos del programa. Python aplica reglas claras: un identificador no puede comenzar con un número, no puede usar guiones medios y tampoco puede ser una palabra reservada como `class`.

## Tu tarea

lee varias líneas desde la entrada estándar. En cada línea hay una asignación, por ejemplo `mi_variable = 1`. Tomá la parte que aparece antes del signo `=` y revisa si es un identificador válido de Python.

Para cada nombre imprime una línea con uno de estos formatos exactos:

```text
válido: nombre
inválido: nombre
```

puedes apoyarte en `str.isidentifier()` y en `keyword.iskeyword()`. La salida debe conservar los acentos de las etiquetas `válido` e `inválido`.

### Ejemplo

Con la entrada del archivo de pruebas:

```text
mi_variable = 1
2var = 2
_valor = 3
class = 4
```

la salida esperada es:

```text
válido: mi_variable
inválido: 2var
válido: _valor
inválido: class
```
