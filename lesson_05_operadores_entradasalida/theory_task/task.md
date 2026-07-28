# Lección 5: Operadores, expresiones y sentencias de E/S

En las lecciones anteriores viste cómo declarar variables y qué tipos básicos
existen. Ahora vamos a **usarlas**: vas a aprender los **operadores** de
Python y cómo **leer y escribir datos** desde la consola.

## 1. Operadores aritméticos

Python trae los operadores matemáticos clásicos:

| Operador | Significado | Ejemplo | Resultado |
|---|---|---|---|
| `+` | Suma | `7 + 3` | `10` |
| `-` | Resta | `7 - 3` | `4` |
| `*` | Multiplicación | `7 * 3` | `21` |
| `/` | División (devuelve float) | `7 / 3` | `2.3333...` |
| `//` | División entera | `7 // 3` | `2` |
| `%` | Módulo (resto) | `7 % 3` | `1` |
| `**` | Potencia | `2 ** 8` | `256` |

Ejemplo en Python:

```python
a, b = 17, 5
print(a + b) # 22
print(a // b) # 3
print(a % b) # 2
print(a ** b) # 1419857
```

> 💡 **Tip**: si alguna vez viste el símbolo `%` en una página web, no es lo
> mismo: en una URL es parte de la dirección, en Python es el operador resto.

## 2. Operadores relacionales

Sirven para **comparar** valores. Siempre devuelven un `bool` (`True` o
`False`):

| Operador | Significado | Ejemplo | Resultado |
|---|---|---|---|
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Distinto de | `5 != 3` | `True` |
| `<` | Menor que | `3 < 5` | `True` |
| `>` | Mayor que | `5 > 3` | `True` |
| `<=` | Menor o igual | `5 <= 5` | `True` |
| `>=` | Mayor o igual | `3 >= 5` | `False` |

⚠️ **Cuidado**: `=` (un solo igual) es **asignación**, no comparación.
Para comparar, siempre son **dos iguales** `==`.

## 3. Operadores lógicos

Combinan condiciones y devuelven un `bool`:

| Operador | Significado | Ejemplo | Resultado |
|---|---|---|---|
| `and` | Y lógico | `True and False` | `False` |
| `or` | O lógico | `True or False` | `True` |
| `not` | Negación | `not True` | `False` |

```python
edad = 17
tiene_id = True
puede_entrar = edad >= 18 and tiene_id
print(puede_entrar) # False
```

## 4. Expresiones

Una **expresión** es cualquier combinación de valores, variables y operadores
que produce un resultado. Ejemplos:

```python
area = base * altura # expresión aritmética
es_mayor = edad >= 18 # expresión relacional
puede_votar = es_mayor and tiene_id # expresión lógica
```

## 5. Sentencias de entrada: `input()`

`input()` lee una línea de texto desde la consola. **Siempre devuelve un
string**, así que si necesitas un número tienes que convertirlo:

```python
nombre = input("¿Cómo te llamás? ") # str
edad = int(input("¿Cuántos años tienes? ")) # int
altura = float(input("Tu altura en metros: ")) # float
```

## 6. Sentencias de salida: `print()`

`print()` muestra texto en la consola. Tiene varios parámetros útiles:

- `sep`: separador entre los argumentos (por defecto es un espacio).
- `end`: carácter final (por defecto es un salto de línea `\n`).
- **f-strings**: la forma moderna de formatear texto.

```python
nombre = "María"
edad = 17
print(f"Hola {nombre}, tienes {edad} años.")
print("A", "B", "C", sep="-") # A-B-C
print("Línea 1", end=" ")
print("Línea 2") # Línea 1 Línea 2
```

## Aplicación: el Índice de Masa Corporal (IMC)

Un ejemplo clásico que combina todo lo anterior:

```python
peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu IMC es {imc:.2f}")
```

> En la siguiente tarea vas a implementar **exactamente** este programa.
