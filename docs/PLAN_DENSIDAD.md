# Plan de densidad de práctica — Programación II

## Principio
- **Cada lección debe tener 3-5 actividades prácticas** (edu/output/quiz combinados)
- **No solo teoría + 1 ejercicio** — eso no da tiempo de consolidar
- **Densidad por complejidad**: temas simples (1, 2) → 3 prácticos; temas densos (8, 13, 14) → 4-5 prácticos
- **Lección completa** debería cubrir 1 clase de 45 min × 2-3 semanas

## Plan lección por lección (versión expandida)

### TRIMESTRE I — Introducción

| Lección | Temas | Prácticos nuevos | Total prácticos después |
|---|---|---|---|
| **1** Historia y paradigmas | Solo lectura + 1 quiz | + 1 quiz diagnóstico, + 1 quiz histórico | 3 (theory + 2 quiz) |
| **2** Ambiente de desarrollo | 1 output actual | + 1 output (hola mundo), + 1 edu (configurar IDE) | 4 |
| **3** Comentarios, identificadores, keywords | 1 edu + 1 quiz | + 1 output (analizar código), + 1 edu (ejercicios variados) | 5 |
| **4** Variables y tipos | 1 edu + 1 output | + 1 edu (intercambio de variables), + 1 quiz (tipos) | 5 |
| **5** Operadores y E/S | 1 edu + 1 output | + 1 edu (calculadora simple), + 1 output (formateo) | 5 |

### TRIMESTRE II — Control y funciones

| Lección | Temas | Prácticos nuevos | Total |
|---|---|---|---|
| **6** If/elif/match | 1 edu + 1 quiz | + 1 edu (calculadora de IMC con if), + 1 quiz (trazar código) | 4 |
| **7** For/while | 1 edu + 1 output | + 1 edu (factorial iterativo), + 1 output (patrón de asteriscos) | 5 |
| **8** Funciones | 1 edu + 1 quiz | + 1 edu (múltiples funciones), + 1 quiz (parámetros), + 1 edu (recursión) | 5 |
| **9** Subrutinas y módulos | 1 edu | + 1 edu (importar y reusar), + 1 output (script con módulos) | 4 |
| **10** IA generativa | 1 quiz | + 1 edu (comparar código IA vs propio), + 1 quiz (buenas prácticas) | 4 |

### TRIMESTRE III — Colecciones

| Lección | Temas | Prácticos nuevos | Total |
|---|---|---|---|
| **11** Arreglos 1D | 1 edu + 1 output | + 1 edu (estadísticas: min, max, suma), + 1 quiz (indexing) | 5 |
| **12** Arreglos 2D | 1 edu | + 1 edu (suma por filas/columnas), + 1 output (transpuesta) | 4 |
| **13** Listas dinámicas | 1 edu | + 1 edu (operaciones combinadas), + 1 output (lista de tareas) | 4 |
| **14** Pilas | 1 edu | + 1 edu (evaluador de expresiones), + 1 quiz (LIFO/FIFO) | 4 |
| **15** Diccionarios | 1 edu + 1 quiz | + 1 edu (frecuencia de palabras), + 1 output (CSV simple) | 5 |

## Resumen

- **Actividades prácticas nuevas a crear: ~36**
- Cada actividad = 1 task-info.yaml + 1 task.md + 1 main.py con placeholder + 1 tests/test.py (o input.txt/output.txt)
- **Distribución**: Agente 1 (Trim I) = ~12 prácticos, Agente 2 (Trim II) = ~12, Agente 3 (Trim III) = ~12
- **3 subagentes en paralelo** = mismo tiempo que 1 agente trabajando todo (~10-15 min)

## Lo que NO cambia
- Los `theory_task` actuales se mantienen
- Los `lesson-info.yaml` se actualizan para incluir los nuevos prácticos
- Los proyectos guiados NO se tocan (ya están completos)
- `course-info.yaml` no cambia (solo lista las lecciones, no las tasks)
