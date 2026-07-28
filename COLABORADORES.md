# Guia para colaboradores del curso

Este curso de **Programacion II** sigue el curriculo del **MEDUCA** (Ministerio de Educacion de Panama) para grado 11. Esta guia explica como adaptarlo a tu colegio o contexto.

## Indice

1. [Como abrir el curso](#como-abrir-el-curso)
2. [Como personalizarlo](#como-personalizarlo)
3. [Como agregar una leccion nueva](#como-agregar-una-leccion-nueva)
4. [Como agregar un ejercicio a una leccion existente](#como-agregar-un-ejercicio-a-una-leccion-existente)
5. [Como distribuir el curso](#como-distribuir-el-curso)
6. [Estructura interna](#estructura-interna)
7. [Convenciones del curso](#convenciones-del-curso)
8. [Solucion de problemas](#solucion-de-problemas)

## Como abrir el curso

### Requisitos

- **PyCharm Educational** (Community o Professional) o PyCharm Community + plugin JetBrains Academy.
- Python 3.10 o superior.
- Git (para clonar el repo).

### Pasos

1. Clona el repositorio:
   ```bash
   git clone <url-del-repo>
   cd ProgramacionII
   ```
2. Abre PyCharm y selecciona **File → Open**.
3. Selecciona la carpeta `ProgramacionII` que acabas de clonar.
4. PyCharm detectara automaticamente que es un curso del plugin JetBrains Academy.
5. Espera a que el plugin indexe las lecciones (1-2 minutos).
6. En el menu **Course** veras las 15 lecciones y los 3 proyectos guiados.

### Si PyCharm no detecta el curso

Esto pasa cuando el cache del plugin se desincroniza:

1. Cierra PyCharm.
2. Borra los caches del plugin:
   ```bash
   rm -rf .idea/frameworkLessonHistoryCC
   rm -f .idea/.author_contents_storage_db*
   rm -rf .remember .coursecreator/*.zip
   ```
3. Vuelve a abrir PyCharm.

## Como personalizarlo

### Cambiar el nombre del curso o colegio

Edita `course-info.yaml`:

```yaml
type: marketplace
title: "Programacion II - Tu Colegio Aqui"
language: Spanish
summary: "Tu descripcion personalizada del curso..."
```

El campo `title` aparece en PyCharm cuando los estudiantes abren el curso.

### Cambiar el logo

Reemplaza los archivos `academy_logo.png` y `academy_logo_dark.png` dentro de cada leccion. Manten las mismas dimensiones para evitar problemas de visualizacion.

### Cambiar la planificacion didactica

Edita el archivo `Plan Anual - Programacion - 11 - 2026.docx` con tu propia planificacion. El plugin JBA lo usa como referencia del programa pero no afecta el contenido del curso.

### Cambiar escalas de notas

El curso usa la escala **1.0 a 5.0** (sistema del MEDUCA). Si quieres usar otra escala:

1. En cada `lesson-info.yaml` cambia el nombre del `custom_name`.
2. En cada `task.md` busca "escala del colegio" y actualiza las referencias.
3. En los `tests/test.py` cambia los valores esperados.

## Como agregar una leccion nueva

### Pasos

1. Crea una carpeta `lesson_NN_slug/` siguiendo el patron de las existentes.
2. Dentro crea:
   - `lesson-info.yaml` con la metadata.
   - `theory_task/` con la teoria.
   - `edu_task/` con ejercicios.
   - `quiz_task/` con preguntas.
   - `output_task/` (opcional) con ejercicios de entrada/salida.
3. Agrega el slug al `course-info.yaml` bajo `content:` en la posicion correcta.

### Plantilla de `lesson-info.yaml`

```yaml
custom_name: "Leccion NN: Titulo descriptivo"
content:
  - theory_task
  - edu_task
  - quiz_task
  - output_task  # si tienes uno
```

### Plantilla de `task-info.yaml`

Para **theory**:
```yaml
type: theory
custom_name: "Titulo del task"
files:
  - name: main.py
    visible: true
```

Para **edu** (ejercicio con tests):
```yaml
type: edu
custom_name: "Titulo del ejercicio"
files:
  - name: main.py
    visible: true
    placeholders:
      - offset: 100
        length: 50
        placeholder_text: "# TODO: implementa la funcion"
  - name: tests/test.py
    visible: false
  - name: tests/__init__.py
    visible: false
    propagatable: false
```

Para **quiz** (pregunta multiple):
```yaml
type: choice
is_multiple_choice: false
options:
  - text: "Opcion A"
    is_correct: false
  - text: "Opcion B"
    is_correct: true
  - text: "Opcion C"
    is_correct: false
  - text: "Opcion D"
    is_correct: false
message_correct: "Feedback positivo en espanol"
message_incorrect: "Feedback de ayuda en espanol"
files:
  - name: main.py
    visible: true
custom_name: "Titulo del quiz"
local_check: true
```

Para **output** (ejercicio con stdin/stdout):
```yaml
type: output
custom_name: "Titulo del reto"
files:
  - name: main.py
    visible: true
    placeholders:
      - offset: 100
        length: 50
        placeholder_text: "# TODO: tu implementacion"
  - name: tests/output.txt
    visible: false
  - name: tests/input.txt
    visible: false
```

## Como agregar un ejercicio a una leccion existente

1. Crea una carpeta `lesson_NN/edu_task_nombre_descriptivo/` o similar.
2. Copia la estructura de otro edu_task existente.
3. Personaliza `main.py`, `task.md`, `task-info.yaml` y `tests/test.py`.
4. Agrega el nombre de la nueva carpeta al `lesson-info.yaml` de la leccion.

## Como distribuir el curso

### Opcion A: Como archivo ZIP (mas facil)

1. En PyCharm: **Course → Export course to ZIP**.
2. Se genera `programacion-ii-medu-ca.zip` (o similar).
3. Comparte el ZIP por email, USB, intranet, etc.
4. El receptor debe:
   - Abrir PyCharm con el plugin JBA instalado.
   - **Course → Import course from ZIP**.
   - Seleccionar el archivo.

### Opcion B: Como repositorio Git

1. Sube el repo a GitHub, GitLab, Bitbucket, etc.
2. Comparte la URL.
3. Los receptores pueden clonar y abrirlo en PyCharm.

### Opcion C: Marketplace publico

Si quieres que aparezca en el catalogo publico de cursos de JetBrains:

1. Verifica que `course-info.yaml` cumple los requisitos de marketplace.
2. Sube el repo a GitHub con tag `marketplace-ready`.
3. Aplica via https://plugins.jetbrains.com/marketplace
4. JetBrains revisara y publicara el curso.

## Estructura interna

```
ProgramacionII/
├── course-info.yaml             # Metadata global del curso
├── README.md                     # Documentacion para estudiantes
├── COLABORADORES.md              # Esta guia
├── LICENSE                       # Licencia MIT
├── requirements.txt              # Dependencias Python
├── Plan Anual...docx             # Planificacion del MEDUCA
│
├── lesson_01_historia_paradigmas/         # 15 lecciones
├── lesson_02_ambiente_desarrollo/
├── ...                                  # una por leccion
├── lesson_15_diccionarios/
│
├── course_guided_project_i_basico/        # 3 proyectos guiados
├── course_guided_project_ii_control/
├── course_guided_project_iii_colecciones/
│
└── docs/                                  # Documentacion interna (no del curso)
    ├── PLAN.md
    ├── PLAN_DENSIDAD.md
    ├── PLAN_LOCALIZACION.md
    └── PLAN_EXPANSION.md
```

## Convenciones del curso

### Idioma

- **Espanol castellano neutro**, sin voseo argentino ("implementa", no "implementá").
- **Tuteo**: usa "tú" (no "vos") para las instrucciones.
- **Terminos locales**: usa terminos panameños (ITBMS en vez de IVA, "colegio" generico, etc.).

### Escala de notas

- **1.0 a 5.0** con **3.0** como minimo aprobatorio.
- En contextos universitarios se puede adaptar a 0-100, pero el colegio usa 1-5.

### Nombramiento de archivos

- `lesson_NN_slug_en_espanol/` con snake_case.
- `slug` legible en espanol, sin acentos.
- Ejemplo: `lesson_03_elementos_basicos/`.

### Custom names

- Siempre en espanol descriptivo.
- NUNCA uses "Theory task", "Edu task", "Output task", "Quiz task".

### Tests

- Cada `edu_task` debe tener `tests/test.py` con al menos 3 tests.
- Cada `output_task` debe tener `tests/input.txt` y `tests/output.txt`.
- Los archivos `tests/input.txt` y `tests/output.txt` deben terminar con `\n`.

## Solucion de problemas

### "Preview course" sale vacio

1. Cierra PyCharm completamente.
2. Borra caches:
   ```bash
   rm -rf .idea/frameworkLessonHistoryCC
   rm -f .idea/.author_contents_storage_db*
   rm -rf .remember .coursecreator/*.zip
   ```
3. Vuelve a abrir PyCharm.

### Los placeholders aparecen en blanco

El plugin necesita que el `offset` y `length` en `task-info.yaml` coincidan exactamente con la posicion del `# TODO` en `main.py`. Para recalcular:

1. Abre `main.py` y busca el `# TODO:`.
2. Cuenta la posicion exacta (caracteres desde el inicio del archivo).
3. Actualiza `offset` y `length` en `task-info.yaml`.

### "lesson-info.yaml" no encontrado

Asegurate de que el archivo existe en la raiz de cada carpeta `lesson_NN_*` con el formato:

```yaml
custom_name: "..."
content:
  - task_name_1
  - task_name_2
```

### Tests no se ejecutan

Verifica que existe `tests/__init__.py` (puede estar vacio) en cada `edu_task` y `output_task`.

### Placeholder incorrecto / identificador Python con tilde

Los identificadores Python NO pueden tener acentos. Si traduces "guion bajo" en un nombre de funcion, el codigo no compilara.

Para evitar esto, el script de localizacion mantiene identificadores sin tilde pero usa tildes en strings, comentarios y docstrings.

## Recursos utiles

- Plugin JetBrains Academy: https://plugins.jetbrains.com/plugin/10081-jetbrains-academy
- Guia oficial para creadores: https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/educator-start-guide.html
- Documentacion de Python: https://www.python.org/es/
- Template oficial: https://github.com/JetBrains-Academy/python-course-template

---

**Mantenedor:** cualquier colegio o docente puede usar, modificar y redistribuir este curso bajo la licencia MIT.

Si encuentras errores o quieres mejorar el curso, eres bienvenido a hacer cambios y compartir tus mejoras.