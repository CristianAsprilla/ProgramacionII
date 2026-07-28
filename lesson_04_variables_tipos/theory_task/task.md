# Lección 4: Variables, constantes y tipos de datos

Ahora que conoces los identificadores, es hora de empezar a **guardar
información** en nuestro programa. Para eso usamos **variables** y
**constantes**, y cada una tiene asociado un **tipo de dato**.

---

## 1. ¿Qué es una variable?

Una **variable** es un nombre que apunta a un valor guardado en la memoria.
puedes pensarla como una **caja con una etiqueta**: la etiqueta es el
identificador y el contenido es el valor.

```python
edad = 17
nombre = "Carlos"
```

Decimos que `edad` "vale" `17` y que `nombre` "vale" `"Carlos"`. La asignación
se hace con el signo `=`.

> 📌 En Python **no hace falta declarar** el tipo de la variable de antemano:
> el intérprete lo deduce del valor que le asignás. Esto se llama **tipado
> dinámico**.

```python
edad = 17 # Python deduce que edad es int
edad = "diecisiete" # ahora edad pasa a ser str (esto es válido)
```

---

## 2. ¿Qué es una constante?

Una **constante** es un valor que **no debería cambiar** durante la ejecución
del programa. Python no tiene constantes "de verdad" (como otros lenguajes),
pero por **convención** las escribimos en **UPPER_SNAKE_CASE** para que todos
los programadores sepan "no tocar esto".

```python
PI = 3.14159
MAX_INTENTOS = 3
NOTA_APROBACION = 71 # minimo para aprobar en Panama
ITBMS = 0.07 # 7% en Panama
```

La **convención** es solo una sugerencia: técnicamente puedes modificar el
valor, pero no lo hagas. Cuando veas nombres en mayúsculas con guiones bajos,
tratálos como si fueran sagrados 🙏.

---

## 3. Tipos de datos básicos (primitivos)

Python trae varios tipos de datos ya incorporados. Estos son los que más vas
a usar en este trimestre:

### Numéricos

| Tipo | Descripción | Ejemplo |
|---|---|---|
| `int` | Números enteros (sin parte decimal) | `-5`, `0`, `17`, `2026` |
| `float` | Números con parte decimal | `3.14`, `-0.5`, `2.0` |
| `complex` | Números complejos (raro en este curso) | `1 + 2j` |

### Texto

| Tipo | Descripción | Ejemplo |
|---|---|---|
| `str` | Cadena de caracteres | `"Hola"`, `'Panama'` |

### Lógicos

| Tipo | Descripción | Ejemplo |
|---|---|---|
| `bool` | Verdadero o Falso | `True`, `False` |

### ¿Cómo saber el tipo de una variable?

usa la función `type()`:

```python
edad = 17
print(type(edad)) # <class 'int'>

nombre = "Ana"
print(type(nombre)) # <class 'str'>

promedio = 88.5
print(type(promedio)) # <class 'float'>

aprobado = True
print(type(aprobado)) # <class 'bool'>
```

> 💡 En Python todo es un **objeto**. Los tipos "básicos" son en realidad
> clases (`int`, `str`, `bool`), pero por ahora piensa en ellos como tipos
> primitivos.

---

## 4. Asignación de variables

La forma más simple de asignar es con `=`:

```python
cantidad_estudiantes = 30
```

Pero Python trae atajos muy útiles: los **operadores de asignación
compuestos**. Sirven para modificar el valor de una variable en el lugar.

| Operador | Equivalente a | Ejemplo | Resultado |
|---|---|---|---|
| `=` | (asignación simple) | `x = 5` | `x` vale `5` |
| `+=` | `x = x + n` | `x = 5; x += 3` | `x` vale `8` |
| `-=` | `x = x - n` | `x = 5; x -= 2` | `x` vale `3` |
| `*=` | `x = x * n` | `x = 5; x *= 4` | `x` vale `20` |
| `/=` | `x = x / n` | `x = 10; x /= 4` | `x` vale `2.5` |
| `%=` | `x = x % n` | `x = 10; x %= 3` | `x` vale `1` |
| `**=` | `x = x ** n` | `x = 2; x **= 3` | `x` vale `8` |
| `//=` | `x = x // n` | `x = 10; x //= 3` | `x` vale `3` |

### Asignación múltiple

En una sola línea puedes asignar el mismo valor a varias variables:

```python
a = b = c = 0
```

O asignar varios valores distintos al mismo tiempo:

```python
nombre, edad, promedio = "Ana", 17, 88.5
```

Esto se llama **desempaquetado de tuplas** y es muy útil cuando una función
devuelve varios valores.

---

## 5. Ejemplo integrado: área de un rectángulo

```python
# Constantes geometricas
PI = 3.14159
ITBMS = 0.07

# Variables del problema
base = 8.5 # metros
altura = 4.2 # metros

# Calculos usando operadores de asignacion
area = base * altura
perimetro = 2 * (base + altura)

# Mostrar resultados
print(f"Base: {base} m")
print(f"Altura: {altura} m")
print(f"Area: {area} m^2")
print(f"Perimetro: {perimetro} m")
```

Salida:

```
Base: 8.5 m
Altura: 4.2 m
Area: 35.7 m^2
Perimetro: 25.4 m
```

fíjate cómo:

- `base` y `altura` son variables (snake_case, pueden cambiar).
- `PI` e `ITBMS` son constantes (UPPER_SNAKE_CASE, no deberían cambiar).
- Usamos `*` y `+` (los vamos a ver en detalle en la Lección 5) para calcular
 el área y el perímetro.
- Los `f-strings` (formato `f"..."`) sirven para incrustar variables dentro
 de un texto.

---

## 6. Buenas prácticas

1. **Nombres descriptivos**: `edad_usuario` es mejor que `x`.
2. **Constantes en mayúsculas**: `PI`, `MAX_INTENTOS`.
3. **Una variable por línea** (evitá `a = b = c = 0` salvo que sea muy claro).
4. **No reutilices nombres** para cosas distintas en el mismo programa.
5. Si una variable guarda un valor monetario (balboas en Panamá, dólares),
 sé claro con eso: `precio_en_balboas`.

---

### 📚 Para profundizar

- [Variables y tipos en Python (documentación oficial)](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
- [PEP 8 — Naming conventions](https://peps.python.org/pep-0008/#naming-conventions)
- [Operadores de asignación](https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements)

<div class="hint" title="¿Qué archivos puedes ver?">

En esta lección teórica todos los archivos del proyecto están disponibles
para examinar. En la siguiente actividad (un *edu task*) vas a calcular el
área y el perímetro de un rectángulo. Después, en un *output task*, vas a
leer un número entero y mostrar su tipo.

</div>