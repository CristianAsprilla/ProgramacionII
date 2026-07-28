"""Guía breve para crear un proyecto de Python en PyCharm.

Para crear un proyecto en PyCharm, abre el programa, elige «Nuevo proyecto»,
selecciona Python como lenguaje, escogé un intérprete de Python 3.10 o superior
y confirmá con «Crear». Después puedes agregar un archivo main.py y ejecutarlo
con el botón de ejecución.
"""

import sys


def validar_version_python(version_info=sys.version_info):
 """Indica si la versión recibida es compatible con el curso."""
 # TODO: validá que sys.version_info >= (3, 10)
 return False


if __name__ == "__main__":
 print(validar_version_python())
