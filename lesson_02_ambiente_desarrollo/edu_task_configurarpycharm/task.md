# Configurá tu ambiente de trabajo

Antes de comenzar a programar conviene verificar que el intérprete y el IDE sean compatibles. PyCharm permite crear proyectos, elegir un intérprete y ejecutar los archivos desde un mismo lugar.

## Tu tarea

implementa `validar_version_python(version_info)`. La función debe devolver:

- `True` cuando la versión sea Python 3.10 o posterior.
- `False` cuando sea Python 3.9, Python 2.7 o cualquier versión anterior.

`version_info` se recibe como una tupla, por ejemplo `(3, 10, 0)`. En la ejecución normal su valor predeterminado es `sys.version_info`; el parámetro facilita probar varias versiones sin cambiar la computadora.

### Recordatorio para PyCharm

1. abre PyCharm y selecciona **Nuevo proyecto**.
2. Elige una carpeta para el proyecto.
3. Selecciona un intérprete de Python 3.10 o superior.
4. Confirmá la creación y ejecuta `main.py`.

Los tests incluyen una versión mínima compatible, una versión 3.9 y una versión 2.7. usa la comparación de versiones, no una comparación de textos.
