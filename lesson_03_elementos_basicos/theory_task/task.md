# Lección 3: Comentarios, identificadores y palabras reservadas

Ya tienes Python instalado y puedes ejecutar tu primer programa. Ahora vamos a
empezar a escribir código con **calidad**: usando **comentarios**, eligiendo
buenos **identificadores** y conociendo las **palabras reservadas** que no
puedes usar como nombres de variables.

---

## 1. Comentarios

Un **comentario** es texto que el intérprete de Python ignora. Sirve para
explicar qué hace el código, a tú mismo o a alguien que lo lea después.

### Comentarios de una línea: `#`

Empiezan con el símbolo `#` y van hasta el final de la línea.

```python
# Esto es un comentario
print("Hola") # Esto también es un comentario, al final de una línea
```

Los comentarios son útiles para:

- Explicar **por qué** se hace algo (no *qué* hace — para eso está el código).
- Desactivar temporalmente una línea de código mientras probás algo.
- Dejar notas para tu equipo o para tu yo del futuro.

### Docstrings: `"""..."""`

Un **docstring** es una cadena de texto (generalmente entre triple comillas
dobles) que se coloca justo al inicio de un módulo, función o clase para
documentarlo.

```python
def area_rectangulo(base, altura):
 """
 Calcula el area de un rectangulo.

 Parametros:
 base (float): la base del rectangulo.
 altura (float): la altura del rectangulo.

 Retorna:
 float: el area (base * altura).
 """
 return base * altura
```

Los docstrings tienen tres ventajas:

1. Sirven de documentación oficial (aparecen en herramientas como `help()`).
2. Los IDEs los usan para mostrarte ayuda mientras escribís código.
3. Pueden ser leídos por generadores automáticos de documentación.

> 💡 **Tip**: escribí docstrings para todas las funciones que declares. Es un
> hábito profesional que te va a servir en el bachillerato **y** en la
> universidad.

---

## 2. Identificadores

Un **identificador** es el nombre que le das a una variable, función, clase o
módulo. En Python hay reglas **obligatorias** y **convenciones** recomendadas.

### Reglas obligatorias

1. Puede contener letras (a–z, A–Z), dígitos (0–9) y el guión bajo (`_`).
2. **No puede empezar con un dígito**.

 ```python
 nombre = "Ana" # correcto
 _contador = 0 # correcto
 2do_trimestre = 11 # ERROR: empieza con digito
 ```

3. **No puede ser una palabra reservada** (las vemos en la próxima sección).
4. Distingue mayúsculas de minúsculas: `Nota` y `nota` son identificadores
 diferentes.

### Convenciones recomendadas (PEP 8)

- **snake_case** para variables y funciones: `nota_final`, `calcular_promedio`.
- **PascalCase** (o **CapWords**) para clases: `Estudiante`, `NotaMensual`.
- **UPPER_SNAKE_CASE** para constantes: `PI = 3.14159`, `MAX_INTENTOS = 3`.
- Nombres descriptivos: preferí `edad_usuario` sobre `x` cuando `x` represente
 una edad.

> 🇨🇦 — perdón, **🇵🇦 Panamá**: en este curso vamos a usar **nombres en
> español** siempre que tenga sentido (`promedio`, `nota`, `lista_estudiantes`),
> porque te ayuda a leer el código como si fuera una receta en tu idioma.
> También aceptamos la nomenclatura estándar en inglés cuando es la forma más
> natural (`for i in range(...)`).

---

## 3. Palabras reservadas (keywords)

Python reserva una lista de palabras para usos especiales del lenguaje. **No
puedes usarlas como nombres de variables, funciones ni clases**.

La lista completa en Python 3.10+ es:

```
False None True and as
assert async await break case
class continue def del elif
else except finally for from
global if import in is
lambda match nonlocal not or
pass raise return try while
with yield
```

(Algunas — `case`, `match` — aparecieron en Python 3.10 con la sentencia
`match`.)

### ¿Cómo saber si una palabra es reservada?

usa el módulo `keyword`:

```python
import keyword
print(keyword.kwlist) # imprime la lista completa
print(keyword.iskeyword("for")) # True
print(keyword.iskeyword("nota")) # False
```

### ¿Qué pasa si intento usar una palabra reservada?

```python
for = 5 # SyntaxError: no se puede asignar a 'for'
class = "A" # SyntaxError
```

Python te avisa con un `SyntaxError` antes de ejecutar el programa.

---

## 4. Ejemplos integrados

```python
# Calculo del promedio de tres notas (escala del colegio (1.0 a 5.0): 1.0 a 5.0)
NOTA_MINIMA = 1.0
NOTA_MAXIMA = 5.0
PROMEDIO_APROBACION = 3.0  # minimo aprobatorio en el colegio

def calcular_promedio(nota1, nota2, nota3):
 """Calcula el promedio simple de tres notas (escala 1.0-5.0)."""
 return (nota1 + nota2 + nota3) / 3

def aprobo(promedio):
 """Devuelve True si el promedio alcanza el minimo de aprobacion."""
 return promedio >= PROMEDIO_APROBACION

# Programa principal
nota_matematica = 4.5
nota_programacion = 4.8
nota_ingles = 4.0

promedio = calcular_promedio(nota_matematica, nota_programacion, nota_ingles)
print(f"Tu promedio es {promedio:.2f}")
```

> 📌 **Nota sobre escalas de calificación:** en el colegio de Panama se
> usa la escala **1.0 a 5.0**, donde 3.0 es el mínimo aprobatorio. Las
> universidades suelen trabajar con escala **0 a 100**. En este curso usaremos la
> escala del colegio.

Fijate en:

- `calcular_promedio` y `aprobo` son **funciones** (snake_case).
- `NOTA_MINIMA`, `NOTA_MAXIMA`, `PROMEDIO_APROBACION` son **constantes**
 (UPPER_SNAKE_CASE).
- Cada función tiene un **docstring**.
- Los nombres son **descriptivos** y están en español.

---

## 5. Buenas prácticas y errores comunes

| ❌ Mal | ✅ Bien |
|---|---|
| `n=5` | `numero_estudiantes = 5` |
| `x = input()` | `nombre = input("Nombre: ")` |
| `if = 10` | `numero = 10` |
| `def MIFUNCION():` | `def mi_funcion():` |
| Sin comentarios ni docstrings | Una línea por bloque lógico |

---

### 📚 Para profundizar

- [PEP 8 — Guía de estilo para código Python (en español)](https://peps.python.org/pep-0008/)
- [Docstrings en Python (realpython.com)](https://realpython.com/documenting-python-code/)
- [Lista oficial de keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)

<div class="hint" title="¿Qué archivos puedes ver?">

En esta lección teórica todos los archivos del proyecto están disponibles para
examinar. En la siguiente actividad (un *edu task*) vas a tener que escribir
código para contar cuántas palabras reservadas aparecen en una lista de líneas.

</div>