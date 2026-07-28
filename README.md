# Programación II — Currículo MEDUCA

[![official project](https://jb.gg/badges/official.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Curso de **Programación II** del **Bachillerato Técnico** de Panamá, alineado con la planificación didáctica anual del **MEDUCA** (Ministerio de Educación de Panamá), grado 11°. Apto para cualquier colegio del país.

Este repositorio fue creado a partir del [template oficial de JetBrains Academy](https://github.com/JetBrains-Academy/python-course-template) y personalizado para el programa de la asignatura, con contenidos, ejercicios y ejemplos adaptados al contexto educativo panameño y al currículo del MEDUCA.

## 📚 Sobre el curso

El curso sigue la planificación oficial del MEDUCA en tres trimestres, con 15 lecciones y 3 proyectos guiados.

### Trimestre I — Introducción al lenguaje y estructuras básicas
1. Historia y paradigmas de los lenguajes de programación.
2. Ambiente de desarrollo: instalación y configuración de Python.
3. Elementos básicos: comentarios, identificadores y palabras reservadas.
4. Variables, constantes y tipos de datos.
5. Operadores, expresiones y sentencias de entrada/salida.
- **Proyecto Guiado I**: Tarjeta de presentación del estudiante.

### Trimestre II — Estructuras de control y subprogramas
6. Estructuras alternativas: `if / elif / else`, `match / case`.
7. Sentencias repetitivas: `for`, `while`.
8. Funciones: definición, parámetros y retorno.
9. Subrutinas y modularización.
10. (Bonus) IA generativa de código: uso crítico.
- **Proyecto Guiado II**: Calculadora de notas con menú.

### Trimestre III — Arreglos y estructuras de datos abstractas
11. Arreglos unidimensionales (listas).
12. Arreglos bidimensionales (matrices).
13. Listas dinámicas.
14. Pilas (LIFO).
15. Diccionarios.
- **Proyecto Guiado III**: Sistema de inventario de la tiendita escolar.

## 🎯 Competencias del MEDUCA trabajadas

- **#2 Pensamiento lógico-matemático**: razonamiento, algorítmica y resolución de problemas.
- **#4 Tratamiento de la información y competencia digital**: uso de herramientas y pensamiento crítico sobre la IA.
- **#7 Aprender a aprender**: estrategias cognitivas, metacognitivas y autonomía.

## 🧰 Estructura del repositorio

```text
.
├── course-info.yaml                             # Metadata del curso
├── README.md                                    # Este archivo
├── requirements.txt                             # Dependencias de Python
├── Plan Anual - Programación - 11 - 2026.docx  # Planificación didáctica del MEDUCA
├── PLAN.md                                      # Plan de arquitectura del curso
│
├── lesson_01_historia_paradigmas/               # Trimestre I
├── lesson_02_ambiente_desarrollo/
├── lesson_03_elementos_basicos/
├── lesson_04_variables_tipos/
├── lesson_05_operadores_entradasalida/
├── course_guided_project_i_basico/              # Proyecto guiado I
│
├── lesson_06_control_alternativo/               # Trimestre II
├── lesson_07_control_repetitivo/
├── lesson_08_funciones/
├── lesson_09_subrutinas/
├── lesson_10_ia_generativa/
├── course_guided_project_ii_control/            # Proyecto guiado II
│
├── lesson_11_arreglos_unidimensionales/         # Trimestre III
├── lesson_12_arreglos_bidimensionales/
├── lesson_13_listas_dinamicas/
├── lesson_14_pilas/
├── lesson_15_diccionarios/
└── course_guided_project_iii_colecciones/       # Proyecto guiado III
```

### Estructura típica de una lección

```text
lesson_NN_slug/
├── lesson-info.yaml         # Nombre y orden de las tasks
├── theory_task/             # Lección teórica (lectura)
│   ├── task-info.yaml
│   ├── task.md
│   └── main.py
├── edu_task/                # Ejercicio con tests
│   ├── task-info.yaml
│   ├── task.md
│   ├── main.py              # Con placeholders para el estudiante
│   └── tests/
│       ├── __init__.py
│       └── test.py
├── quiz_task/               # Quiz de opción múltiple
│   ├── task-info.yaml
│   ├── task.md
│   └── main.py
└── output_task/             # Ejercicio con validación stdin/stdout
    ├── task-info.yaml
    ├── task.md
    ├── main.py
    └── tests/
        ├── input.txt
        └── output.txt
```

## 🚀 Requisitos

- Python 3.10 o superior.
- PyCharm Educational o el plugin de JetBrains Academy instalado en tu IDE de JetBrains.
- Ver `requirements.txt` para las dependencias específicas de cada lección.

## 📖 Documentación

- Plugin JetBrains Academy: [https://plugins.jetbrains.com/plugin/10081-jetbrains-academy](https://plugins.jetbrains.com/plugin/10081-jetbrains-academy)
- Guía para creadores de cursos: [Educator start guide](https://plugins.jetbrains.com/plugin/10081-jetbrains-academy/docs/educator-start-guide.html)
- Documentación oficial de Python: [https://www.python.org/es/](https://www.python.org/es/)

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

## ✍️ Autoría y créditos

**Material base:** El presente curso se basa en el [template oficial de JetBrains Academy](https://github.com/JetBrains-Academy/python-course-template), publicado bajo licencia MIT por **JetBrains s.r.o.** (Copyright 2023). El template provee la estructura pedagógica, las plantillas de archivos, el sistema de tests y el flujo del plugin JBA.

**Adaptación y contenidos:** La personalización al currículo del Ministerio de Educación de Panamá (MEDUCA), la localización lingüística (vocabulario panameño, escala 1.0-5.0, uso de ITBMS en lugar de IVA, ejemplos del bachillerato técnico panameño), la creación de las 15 lecciones y los 3 proyectos guiados, y la redacción de los ejercicios, son obra de **Cristian Asprilla** (Copyright 2026).

**Licenciamiento:** El material se distribuye bajo licencia MIT. Esto significa que cualquier colegio de Panamá puede usar, adaptar y redistribuir el contenido manteniendo el reconocimiento tanto a JetBrains Academy como autor del material base como al adaptador (Cristian Asprilla) por la personalización al currículo panameño. Ver `LICENSE` para los términos completos.

**Reconocimiento a JetBrains:** Por la creación y mantenimiento del plugin JetBrains Academy y por publicar el template oficial que sirvió como base para este curso, sin el cual la autoría de esta obra pedagógica no habría sido posible.