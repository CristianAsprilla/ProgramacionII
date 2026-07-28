"""Paso 6: integrar todo en una sola aplicacion.

Este paso importa todas las funciones de los pasos anteriores
y las conecta en un programa interactivo completo.
"""

# Importamos las funciones de los pasos anteriores
from first_task.main import crear_saludo
from second_task.main import crear_tarjeta
from third_task.main import leer_nombre, leer_edad
from fourth_task.main import calcular_imc, categoria_imc
from fifth_task.main import pedir_nombre_valido, validar_edad


def main():
    """Punto de entrada principal del programa."""
    # TODO: integra los pasos anteriores. Pide nombre con validacion, edad con validacion,
    # peso y altura, calcula IMC, categoria, y muestra la tarjeta completa
    pass


if __name__ == "__main__":
    main()
