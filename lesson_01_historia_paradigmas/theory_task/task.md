# Lección 1: Historia y paradigmas de los lenguajes de programación

¡Bienvenido a **Programación II**! Antes de escribir una sola línea de código, vale la pena
preguntarse: ¿de dónde vienen los lenguajes de programación y por qué existen tantos?

En esta lección vamos a recorrer dos ideas fundamentales:

1. Una mirada rápida a la **historia** de los lenguajes de programación.
2. Los **paradigmas** de programación, que son las distintas formas en que podemos
 pensar y organizar la solución a un problema.

---

## 1. Una historia muy breve

La programación tal como la conocemos es relativamente joven. Estos son algunos hitos
que cualquier programador debería reconocer:

### Los orígenes

- **Ada Lovelace (1843)**: considerada la primera programadora de la historia. Escribió
 lo que se considera el primer algoritmo pensado para ser ejecutado por una máquina
 (la máquina analítica de Charles Babbage).
- **Plankalkül (1948)**: creado por Konrad Zuse, es considerado el primer lenguaje de
 programación de alto nivel, aunque nunca se implementó en su época.

### La era de los lenguajes "clásicos"

- **FORTRAN (1957)**: uno de los primeros lenguajes de alto nivel usados masivamente,
 pensado para cálculos científicos.
- **LISP (1958)**: introduce ideas que hoy asociamos con la programación funcional.
- **COBOL (1959)**: muy usado en sistemas bancarios y administrativos; sus descendientes
 todavía corren en muchos bancos.
- **BASIC (1964)**: creado para que estudiantes aprendieran a programar de forma
 sencilla y marcó la entrada de mucha gente al mundo de la programación.
- **C (1972)**: diseñado por Dennis Ritchie en los laboratorios Bell. Su influencia es
 enorme: el propio Python, el sistema operativo Unix y muchísimas bases de software
 moderno están escritos en C o en lenguajes "estilo C".

### La era moderna

- **C++ (1985)**: añade Programación Orientada a Objetos a C.
- **Java (1995)**: populariza la idea de "escribir una vez, ejecutar en cualquier lugar"
 con la máquina virtual.
- **Python (1991)**: creado por Guido van Rossum con un enfoque claro en la
 **legibilidad**. Hoy es uno de los lenguajes más usados en educación, ciencia de
 datos, automatización y desarrollo web.
- **JavaScript (1995)**: creado en diez días, se convirtió en el lenguaje de la web.
- **Kotlin (2011)**: lenguaje moderno que se usa como alternativa a Java, especialmente
 en Android.

> 💡 Fíjate en un patrón: cada lenguaje nuevo suele intentar **resolver un problema**
> que su antecesor no resolvía bien. Python quiso ser más legible que C, Kotlin quiso
> ser más seguro que Java, BASIC quiso ser más sencillo que FORTRAN.

---

## 2. Paradigmas de programación

Un *paradigma* es una forma de pensar y estructurar la solución a un problema. No son
"estilos" que se eligen por gusto: cada uno tiene herramientas que se adaptan mejor a
ciertos tipos de problemas.

### Imperativo (o procedural)

- El programa se describe como una **secuencia de instrucciones** que cambian el estado
 de la memoria.
- Lenguajes: **C, Pascal, BASIC**.
- Ejemplo mental: una receta de cocina paso a paso.

```c
int total = 0;
for (int i = 1; i <= 10; i++) {
 total = total + i;
}
```

### Orientado a Objetos (POO)

- Organiza el código en **objetos** que tienen datos (atributos) y comportamientos
 (métodos).
- Lenguajes: **Java, C++, Python, Kotlin**.
- Ejemplo mental: modelar un problema como entidades del mundo real (un `Estudiante`,
 un `Curso`, una `Nota`).

```python
class Estudiante:
 def __init__(self, nombre):
 self.nombre = nombre
 self.notas = []

 def agregar_nota(self, nota):
 self.notas.append(nota)
```

### Funcional

- El programa se construye **componiendo funciones**, evitando cambiar el estado
 siempre que sea posible.
- Lenguajes: **Haskell, Lisp, Erlang**, y características funcionales presentes en
 Python y JavaScript.
- Ejemplo mental: una línea de ensamblaje donde cada función transforma datos.

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x * x, numeros))
```

### Lógico (declarativo)

- Describes **qué quieres** que se cumpla, no los pasos para conseguirlo. El motor
 resuelve los detalles.
- Lenguajes: **Prolog**.
- Se usa en inteligencia artificial, sistemas expertos y reglas de negocio.

### Otros paradigmas importantes

- **Scripting**: pensado para automatizar tareas (Python, Bash, JavaScript).
- **Reactivo**: para manejar flujos de eventos en tiempo real (Kotlin Flow, RxJS).
- **Multi-paradigma**: muchos lenguajes modernos te dejan mezclar paradigmas.
 **Python** es un buen ejemplo: puedes programar de forma imperativa, funcional o
 con objetos en el mismo archivo.

---

## 3. ¿Por qué importa esto en Programación II?

Porque cuando elegimos un lenguaje (o un paradigma) **estamos eligiendo una forma de
pensar**. En este curso usaremos **Python**, que es multi-paradigma, pero los conceptos
que aprendas aquí te servirán cuando más adelante trabajes con Java, C++ o cualquier
otro lenguaje.

En la siguiente actividad (un *quiz*) vas a poner a prueba qué tan claros te quedaron
los conceptos de paradigmas.

---

### 📚 Para profundizar

- [Historia de los lenguajes de programación](https://es.wikipedia.org/wiki/Historia_de_los_lenguajes_de_programaci%C3%B3n)
- [Paradigma de programación](https://es.wikipedia.org/wiki/Paradigma_de_programaci%C3%B3n)
- Documentación oficial de Python: [python.org](https://www.python.org/)

<div class="hint" title="¿Qué archivos puedes ver?">

En esta lección teórica todos los archivos del proyecto están disponibles para
examinar. En lecciones prácticas verás menos archivos porque algunos contendrán
los tests del ejercicio.

</div>
