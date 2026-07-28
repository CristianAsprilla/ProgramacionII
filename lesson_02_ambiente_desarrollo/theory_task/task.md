# Lección 2: Ambiente de desarrollo: instalación y configuración de Python

Antes de escribir programas más serios, necesitamos un **ambiente de desarrollo** en
nuestra computadora. En esta lección vas a aprender a:

1. Instalar **Python** en tu sistema operativo.
2. Elegir un **IDE** (entorno de desarrollo integrado) — te recomendamos **PyCharm** o
 **VS Code**.
3. Escribir y ejecutar tu **primer programa** en Python.
4. Trabajar con la **terminal** y el gestor de paquetes **`pip`**.

---

## 1. ¿Qué es Python y por qué lo usamos en este curso?

Python es un lenguaje de programación creado por **Guido van Rossum** en 1991. Sus
dos grandes ventajas son:

- **Legibilidad**: el código se lee casi como inglés.
- **Versatilidad**: sirve para educación, ciencia de datos, automatización, web,
 inteligencia artificial, etc.

> 🐍 En este curso vamos a usar **Python 3.10 o superior**. Asegurate de no instalar
> Python 2 (ya está obsoleto).

---

## 2. Instalación de Python

### En Windows

1. Entrá a [python.org/downloads](https://www.python.org/downloads/).
2. Descargá la última versión estable (3.10+).
3. **MUY IMPORTANTE**: en la primera pantalla del instalador, marca la casilla
 *“Add Python to PATH”* antes de hacer clic en *Install Now*.
4. verifica la instalación abriendo una terminal (`cmd` o `PowerShell`) y escribiendo:

```bash
python --version
```

Deberías ver algo como `Python 3.12.4` (el número exacto puede variar).

### En macOS

macOS trae una versión vieja de Python preinstalada, pero te conviene instalar una
versión nueva. Las dos formas más fáciles:

- **Instalador oficial**: igual que en Windows, desde
 [python.org/downloads](https://www.python.org/downloads/).
- **Homebrew** (recomendado si ya lo usás):

```bash
brew install python
```

### En Linux (Ubuntu / Debian)

Python suele venir preinstalado, pero es mejor instalar la versión oficial:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

> 💡 **Tip Panamá**: si vas al laboratorio del colegio y no puedes instalar nada,
> puedes usar [python.org/shell](https://www.python.org/shell/) para probar
> fragmentos de código desde el navegador.

---

## 3. Elegir un IDE

Un **IDE** (Integrated Development Environment) es el programa donde vas a escribir
código. Te recomendamos uno de estos dos:

### PyCharm (Community Edition) — recomendado para empezar

- Hecho por JetBrains (la empresa detrás de IntelliJ).
- Versión **Community** gratuita y de código abierto.
- Incluye autocompletado, depurador, integración con Git y soporte para Python.
- Descarga: [jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download/)

### VS Code — liviano y muy popular

- Editor de Microsoft, gratuito y extensible.
- Instalás la extensión **“Python”** de Microsoft y listo.
- Descarga: [code.visualstudio.com](https://code.visualstudio.com/)

> 🆚 ¿Cuál elegir? Si nunca programaste, **PyCharm Community** es más amigable.
> Si quieres algo liviano o ya usás VS Code para otras materias, **VS Code** está perfecto.

---

## 4. Tu primer programa: "Hola, mundo"

Una vez que tengas Python instalado y un IDE listo, crea un archivo llamado
`hola.py` con este contenido:

```python
# Mi primer programa en Python
print("Hola, mundo!")
```

### Ejecutarlo desde el IDE

En PyCharm: clic derecho sobre el archivo → *Run 'hola'*.
En VS Code: abre el archivo y presioná el botón ▶️ arriba a la derecha.

### Ejecutarlo desde la terminal

abre una terminal en la carpeta donde guardaste `hola.py` y escribí:

```bash
python hola.py
```

Deberías ver en pantalla:

```
Hola, mundo!
```

En algunas computadoras (sobre todo Linux y macOS) puede ser necesario usar
`python3` en vez de `python`:

```bash
python3 hola.py
```

---

## 5. La terminal y `pip`

### Comandos básicos de terminal

| Acción | Windows (cmd) | macOS / Linux |
|---|---|---|
| Ver carpeta actual | `cd` | `pwd` |
| Listar archivos | `dir` | `ls` |
| Cambiar de carpeta | `cd Carpeta` | `cd Carpeta` |
| Crear carpeta | `mkdir nueva` | `mkdir nueva` |

No te preocupes si nunca usaste la terminal: la vamos a usar poco a poco, sobre
todo para instalar paquetes.

### ¿Qué es `pip`?

`pip` es el **gestor de paquetes** de Python. Te permite instalar librerías extra
hechas por la comunidad. Viene incluido cuando instalás Python desde
[python.org](https://www.python.org/).

Por ejemplo, para instalar la librería `requests` (útil para hacer pedidos a
servidores web):

```bash
pip install requests
```

Para ver qué tienes instalado:

```bash
pip list
```

### Ambientes virtuales (venv)

Cuando un proyecto crece, es buena práctica aislar sus dependencias en un
**ambiente virtual**. Se crean con:

```bash
python -m venv mi_entorno
```

En esta materia todavía no los vamos a usar mucho, pero es bueno que sepas que
existen. Los retomaremos más adelante.

---

## 6. Verificar tu instalación

Antes de seguir, abre una terminal y ejecuta estos comandos para verificar que
todo esté en orden:

```bash
python --version
pip --version
```

Si ambos responden con un número de versión, tu ambiente está listo. En la próxima
actividad (un *output task*) vas a escribir un programa que muestre información
sobre tu instalación de Python usando el módulo `sys`.

---

### 📚 Para profundizar

- [Tutorial oficial de Python (en español)](https://docs.python.org/es/3/tutorial/index.html)
- [Guía de instalación oficial](https://wiki.python.org/moin/BeginnersGuide)
- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/)
- [Visual Studio Code](https://code.visualstudio.com/)

<div class="hint" title="¿Qué archivos puedes ver?">

En esta lección teórica todos los archivos del proyecto están disponibles para
examinar. En lecciones prácticas vas a ver menos archivos porque algunos
contendrán los tests del ejercicio.

</div>