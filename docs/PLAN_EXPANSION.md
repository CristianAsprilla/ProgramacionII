# Plan de expansión masiva + aleatorización + pruebas de escritorio

## Diagnóstico actual

- **84 tasks** en 15 lecciones (promedio 5.6)
- 32 edu, 16 output, 21 quiz, 15 theory
- **L9 y L10 son las más débiles** (4 tasks cada una)
- **Quizzes mal distribuidos**: 10/21 tienen la respuesta correcta en la posición 0 (48% del total)
- **Pocas pruebas de escritorio** (trazar código y predecir salida)

## Objetivo

Cada lección debe tener **10 prácticos** (sin contar el theory), distribuidos en:
- **4-5 edu** (ejercicios para implementar funciones)
- **2-3 output** (ejercicios de entrada/salida con stdin/stdout)
- **3-4 quiz** (preguntas de opción múltiple, con pruebas de escritorio)

Total estimado: **15 lecciones × 10 = 150 prácticos** + 15 theory = **165 tasks**.

## Aleatorización de respuestas correctas

Estrategia: para cada quiz, asegurar que la posición de la respuesta correcta siga una distribución balanceada:
- 25% en posición 0
- 25% en posición 1
- 25% en posición 2
- 25% en posición 3

Para los 21 quizzes actuales, reorganizar las opciones para que la distribución sea ~5 por posición. Para los nuevos, generar la posición con `random.randint(0, 3)` pero fija en el YAML (porque la aleatoriedad en el YAML no es posible, solo la posición final).

## Pruebas de escritorio

Una "prueba de escritorio" es un quiz donde se muestra un fragmento de código y se pregunta:
- ¿Qué imprime este código?
- ¿Cuál es el valor de la variable X después de ejecutar Y?
- ¿Qué retorna esta función con estos argumentos?

Esto es CRÍTICO para aprender a programar porque enseña a **rastrear el flujo de ejecución**.

**Plan:** al menos **1 prueba de escritorio por lección** (15 pruebas de escritorio nuevas), con 4 opciones de respuesta.

## Plan lección por lección

Para llegar a 10 prácticos por lección necesito agregar entre 2-6 prácticos a cada una. La distribución final será:

| Lección | Actual | Agregar | Final |
|---|---|---|---|
| 1 Historia | 6 (1 edu + 0 out + 4 quiz) | + 1 out + 3 edu + 1 quiz | 11 |
| 2 Ambiente | 6 (1 edu + 3 out + 1 quiz) | + 2 edu + 2 quiz | 11 |
| 3 Elementos | 5 (2 edu + 1 out + 1 quiz) | + 2 edu + 2 quiz | 10 |
| 4 Variables | 5 (2 edu + 1 out + 1 quiz) | + 2 edu + 1 out + 1 quiz | 10 |
| 5 Operadores | 5 (2 edu + 2 out + 0 quiz) | + 3 quiz + 1 edu | 10 |
| 6 If/elif | 6 (2 edu + 1 out + 2 quiz) | + 2 edu + 1 quiz | 10 |
| 7 Bucles | 5 (2 edu + 2 out + 0 quiz) | + 3 quiz + 1 edu | 10 |
| 8 Funciones | 6 (3 edu + 0 out + 2 quiz) | + 2 edu + 1 out + 1 quiz | 11 |
| 9 Subrutinas | 4 (2 edu + 1 out + 0 quiz) | + 3 edu + 2 quiz | 10 |
| 10 IA | 4 (1 edu + 0 out + 2 quiz) | + 2 edu + 2 quiz + 1 out | 10 |
| 11 Arreglos 1D | 7 (3 edu + 1 out + 2 quiz) | + 1 edu + 1 out + 1 quiz | 10 |
| 12 Arreglos 2D | 6 (3 edu + 1 out + 1 quiz) | + 2 edu + 1 quiz | 10 |
| 13 Listas | 6 (3 edu + 1 out + 1 quiz) | + 2 edu + 1 quiz | 10 |
| 14 Pilas | 6 (2 edu + 1 out + 2 quiz) | + 1 edu + 2 quiz | 10 |
| 15 Diccionarios | 7 (3 edu + 1 out + 2 quiz) | + 1 edu + 1 quiz | 10 |

**Total nuevos prácticos: ~75** distribuidos en 15 lecciones.

## Lista detallada de prácticos nuevos por lección

### Lección 1 (Historia) — agregar 5
- `output_task_lineatiempo_codigo` (output): lee eventos de stdin y los ordena cronológicamente
- `edu_task_categorizar_lenguaje` (edu): función `categoria_por_año(año)` que retorna "antiguo" o "moderno"
- `edu_task_conteo_paradigmas` (edu): cuenta cuántas veces aparece cada paradigma en una lista de lenguajes
- `edu_test_escritorio_paradigma` (edu con test de escritorio): predice el output de fragmentos de cada paradigma
- `quiz_test_escritorio_basico` (quiz con test de escritorio): "¿Qué imprime `print('Hola' + 'Mundo')`?" → "HolaMundo"

### Lección 2 (Ambiente) — agregar 5
- `edu_task_version_python` (edu): función que parsea `sys.version_info` y retorna "compatible" o "incompatible"
- `edu_task_extension_archivo` (edu): función que retorna la extensión de un nombre de archivo
- `quiz_test_escritorio_print` (quiz con test de escritorio)
- `quiz_test_escritorio_input` (quiz con test de escritorio)
- `quiz_paths_terminal` (quiz de conceptos)

### Lección 3 (Comentarios) — agregar 5
- `edu_task_contar_comentarios` (edu): cuenta líneas de comentarios en un fragmento
- `edu_task_validar_identificador` (edu): función que valida si un string es identificador válido de Python
- `quiz_test_escritorio_keywords` (quiz con test de escritorio): muestra código con keywords y pregunta qué hace
- `quiz_keywords_dificiles` (quiz de conceptos)
- `quiz_estilo_codigo` (quiz sobre PEP 8)

### Lección 4 (Variables y tipos) — agregar 5
- `edu_task_tipo_variable` (edu): función que retorna el tipo de un valor como string
- `output_task_conversion` (output): convierte entre int/float/str
- `quiz_test_escritorio_tipos` (quiz con test de escritorio)
- `quiz_test_escritorio_fstring` (quiz con test de escritorio)
- `quiz_constantes` (quiz de conceptos)

### Lección 5 (Operadores) — agregar 5
- `edu_task_precedencia` (edu): evalúa una expresión respetando precedencia
- `quiz_test_escritorio_aritmetica` (quiz con test de escritorio): `2 + 3 * 4 - 1` = ?
- `quiz_test_escritorio_comparacion` (quiz con test de escritorio)
- `quiz_test_escritorio_logicos` (quiz con test de escritorio)
- `quiz_precedencia` (quiz de conceptos)

### Lección 6 (If/elif) — agregar 4
- `edu_task_edad_categoria` (edu): clasifica edad en rangos
- `edu_test_escritorio_ternario` (edu con test de escritorio): predice el output de expresiones condicionales
- `quiz_test_escritorio_if` (quiz con test de escritorio)
- `quiz_test_escritorio_match` (quiz con test de escritorio): match/case en Python 3.10+

### Lección 7 (Bucles) — agregar 5
- `edu_task_suma_hasta_n` (edu): suma de 1 a N
- `quiz_test_escritorio_for` (quiz con test de escritorio): predice iteraciones
- `quiz_test_escritorio_while` (quiz con test de escritorio)
- `quiz_test_escritorio_break_continue` (quiz con test de escritorio)
- `quiz_bucles_infinitos` (quiz de conceptos)

### Lección 8 (Funciones) — agregar 5
- `edu_task_area_circulo` (edu): π × r²
- `output_task_volumen_caja` (output): lee dimensiones y calcula volumen
- `quiz_test_escritorio_return` (quiz con test de escritorio)
- `quiz_test_escritorio_parametros_default` (quiz con test de escritorio)
- `quiz_test_escritorio_recursion` (quiz con test de escritorio)

### Lección 9 (Subrutinas) — agregar 6
- `edu_task_es_primo` (edu): función que verifica si un número es primo
- `edu_task_lista_primos` (edu): lista de primos hasta N
- `edu_task_factorial_modular` (edu): factorial usando recursión
- `quiz_test_escritorio_import` (quiz con test de escritorio)
- `quiz_modulos_python` (quiz de conceptos)
- `quiz_biblioteca_estandar` (quiz de conceptos)

### Lección 10 (IA generativa) — agregar 6
- `edu_task_contar_lineas_ia` (edu): cuenta líneas de código generado por IA
- `edu_task_detectar_comentarios_ia` (edu): detecta si código tiene comentarios sospechosos
- `output_task_comparar_versiones` (output): lee 2 versiones y compara
- `quiz_test_escritorio_prompt` (quiz con test de escritorio)
- `quiz_test_escritorio_refactorizacion` (quiz con test de escritorio)
- `quiz_etica_ia` (quiz de conceptos)

### Lección 11 (Arreglos 1D) — agregar 3
- `edu_task_suma_elementos` (edu): suma de elementos
- `output_task_invertir_lista` (output): invierte una lista
- `quiz_test_escritorio_listas` (quiz con test de escritorio): predice resultado de operaciones con listas

### Lección 12 (Arreglos 2D) — agregar 4
- `edu_task_suma_diagonal_secundaria` (edu): suma diagonal inversa
- `edu_task_transponer_matriz` (edu): función que transpone una matriz
- `quiz_test_escritorio_matriz` (quiz con test de escritorio)
- `quiz_test_escritorio_matriz_anidada` (quiz con test de escritorio)

### Lección 13 (Listas) — agregar 4
- `edu_task_invertir_lista` (edu): invierte sin `reverse()`
- `edu_task_filtrar_pares` (edu): filtra números pares
- `quiz_test_escritorio_append` (quiz con test de escritorio)
- `quiz_test_escritorio_slice` (quiz con test de escritorio)

### Lección 14 (Pilas) — agregar 4
- `edu_test_escritorio_push_pop` (edu con test de escritorio): simula operaciones
- `quiz_test_escritorio_lifo` (quiz con test de escritorio)
- `quiz_test_escritorio_desapilar` (quiz con test de escritorio)
- `quiz_cuando_usar_pila` (quiz de conceptos)

### Lección 15 (Diccionarios) — agregar 3
- `edu_test_escritorio_diccionario` (edu con test de escritorio)
- `quiz_test_escritorio_dict` (quiz con test de escritorio)
- `quiz_test_escritorio_get` (quiz con test de escritorio)

## Resumen de distribución final esperada

Cada lección: **10-11 prácticos** (algunos 10, algunos 11) más 1 theory = 11-12 tasks.

- edu: ~50-60 (muchos más)
- output: ~25-30
- quiz: ~50-60 (con pruebas de escritorio)
- theory: 15
- **Total estimado: 150-160 tasks**

## Aleatorización de respuestas correctas

Para los 21 quizzes actuales, redistribuir las opciones para que la respuesta correcta esté uniformemente en posiciones 0, 1, 2, 3. Estrategia:
1. Ver la posición actual de la respuesta correcta.
2. Si la posición 0 está sobrecargada, mover la opción correcta a la posición menos usada.
3. Mover las otras opciones correspondientemente.
4. Mantener el texto de la opción correcta en su lugar, solo cambiar la posición.

Para los ~75 nuevos quizzes, asegurar que la posición inicial ya esté balanceada.

## Distribución de trabajo

- **Agente 1** (Trim I, lecciones 1-5): 25 prácticos nuevos + aleatorización de quizzes existentes en L1-L5
- **Agente 2** (Trim II, lecciones 6-10): 26 prácticos nuevos + aleatorización de quizzes existentes en L6-L10
- **Agente 3** (Trim III, lecciones 11-15): 18 prácticos nuevos + aleatorización de quizzes existentes en L11-L15

Yo me encargo de:
- Verificar que la aleatorización quedó bien
- Validar que todos los prácticos compilan y los tests pasan
- Actualizar los `lesson-info.yaml` y `course-info.yaml`

## Riesgos

1. **Volumen:** 75 nuevos prácticos es mucho. Si los agentes no completan todos, terminamos como en la ronda anterior.
2. **Calidad:** con tanto volumen, hay riesgo de contenido genérico. Hay que insistir en ejemplos contextualizados a Panamá.
3. **Pruebas de escritorio:** son más complejas de generar bien (código correcto, distractores plausibles). Voy a dar templates específicos para que los agentes las hagan bien.
