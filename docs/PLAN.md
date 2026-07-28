# Plan de arquitectura del curso — Programación II (Panamá)

## Convenciones globales

- **Nombre de carpeta de lección**: `lesson_NN_slug_en_espanol` (snake_case, slug legible)
- **Cada lección** tiene su `lesson-info.yaml` con `custom_name` en español
- **Cada tarea** tiene `task-info.yaml` + `task.md` + (opcional) `main.py` + `tests/`
- **Idioma**: 100% español en `task.md` y mensajes al usuario
- **Comentarios en código**: español
- **Naming en español**: variables y funciones simples en español para bachiller (ej. `nota`, `sumar`), pero acepta nomenclatura estándar en inglés
- **Lenguaje**: Python 3.10+
- **Tests**: `unittest` framework

## Estructura de lessons (excluye proyectos guiados)

### Trimestre I — Introducción y Estructuras básicas

| # | Carpeta | Nombre | Tipo de contenido |
|---|---|---|---|
| 1 | `lesson_01_historia_paradigmas` | Historia y paradigmas de los lenguajes de programación | theory + quiz |
| 2 | `lesson_02_ambiente_desarrollo` | Ambiente de desarrollo: instalación y configuración de Python | theory + output |
| 3 | `lesson_03_elementos_basicos` | Comentarios, identificadores y palabras reservadas | theory + edu + quiz |
| 4 | `lesson_04_variables_tipos` | Variables, constantes y tipos de datos | theory + edu + output |
| 5 | `lesson_05_operadores_entradasalida` | Operadores, expresiones y sentencias de E/S | theory + edu + output |

### Trimestre II — Estructuras de control y Subprogramas

| # | Carpeta | Nombre | Tipo de contenido |
|---|---|---|---|
| 6 | `lesson_06_control_alternativo` | Estructuras de control alternativas (if, elif, else, switch/match) | theory + edu + quiz |
| 7 | `lesson_07_control_repetitivo` | Sentencias repetitivas (for, while) | theory + edu + output |
| 8 | `lesson_08_funciones` | Funciones: definición, parámetros y retorno | theory + edu + quiz |
| 9 | `lesson_09_subrutinas` | Subrutinas y modularización | theory + edu |
| 10 | `lesson_10_ia_generativa` | IA generativa de código: uso crítico | theory + quiz |

### Trimestre III — Arreglos y Estructuras de datos abstractas

| # | Carpeta | Nombre | Tipo de contenido |
|---|---|---|---|
| 11 | `lesson_11_arreglos_unidimensionales` | Arreglos unidimensionales | theory + edu + output |
| 12 | `lesson_12_arreglos_bidimensionales` | Arreglos bidimensionales (matrices) | theory + edu |
| 13 | `lesson_13_listas_dinamicas` | Listas dinámicas | theory + edu |
| 14 | `lesson_14_pilas` | Pilas (LIFO) | theory + edu |
| 15 | `lesson_15_diccionarios` | Diccionarios | theory + edu + quiz |

## Proyectos guiados

| Trim | Carpeta | Nombre | Tasks |
|---|---|---|---|
| I | `course_guided_project_i_basico` (ya existe con demo) | Proyecto guiado I: Datos del estudiante | theory + first_task + second_task |
| II | `course_guided_project_ii_control` | Proyecto guiado II: Calculadora completa | theory + 3 tasks |
| III | `course_guided_project_iii_colecciones` | Proyecto guiado III: Sistema de notas | theory + 4 tasks |

## Tipos de tarea

- **theory**: `task-info.yaml` con `type: theory`, `task.md` con texto formateado en español
- **quiz**: `task-info.yaml` con `type: choice`, `is_multiple_choice`, `options` (4 opciones), `message_correct`/`message_incorrect`
- **edu**: `task-info.yaml` con `type: edu`, `main.py` con placeholders, `tests/test.py` con `unittest`
- **output**: `task-info.yaml` con `type: output`, `main.py` que lee stdin y escribe stdout, `tests/input.txt` + `tests/output.txt`

## Formato del lesson-info.yaml

```yaml
custom_name: "Lección N: Nombre en español"
content:
  - theory_task
  - edu_task
  - quiz_task
```

## Esquema de archivos por tarea

```
lesson_NN_slug/
├── lesson-info.yaml
├── theory_task/
│   ├── task-info.yaml
│   ├── task.md
│   └── main.py (vacío o con ejemplo)
├── edu_task/
│   ├── task-info.yaml
│   ├── task.md
│   ├── main.py (con placeholders)
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test.py
├── quiz_task/
│   ├── task-info.yaml
│   ├── task.md
│   └── main.py
└── output_task/
    ├── task-info.yaml
    ├── task.md
    ├── main.py
    └── tests/
        ├── input.txt
        └── output.txt
```

## Reglas críticas que TODO agente debe respetar

1. **NO** traducir contenido en inglés del template que ya existe en `lesson_01_*` — esa lección ya está en español.
2. **NO** tocar `course-info.yaml`, `README.md`, `LICENSE`, ni el plan anual.
3. **NO** crear las carpetas que estén reservadas para otros agentes (ver tabla arriba).
4. Cada tarea DEBE tener un `task-info.yaml` válido.
5. Cada `lesson-info.yaml` debe tener `custom_name` en español y referenciar las tareas correctas.
6. Los `task.md` en español rioplatense neutro (vos/usted — usa "tú" con estudiantes, ya que son adolescentes pero el tono debe ser respetuoso; usar "podés", "querés", "imprimí" cuando aplique).

## Estado actual

- ✅ `lesson_01_historia_paradigmas` — Armada en español (theory + quiz)
- ✅ `course_guided_project_i_basico` — Existe con contenido demo del template
- 🔄 Pendiente: lecciones 2-5 (Agente 1), 6-10 (Agente 2), 11-15 (Agente 3)
- 🔄 Pendiente: proyectos guiados II y III
- 🔄 Pendiente: actualizar `course-info.yaml` con todas las lecciones
