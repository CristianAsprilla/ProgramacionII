"""Paso 3: el menu interactivo.

Este paso integra las funciones de los pasos anteriores en un menu
que el usuario controla desde la terminal.
"""

# Importamos todo lo del paso 1 y paso 2
from first_task.main import agregar_nota, listar_notas
from second_task.main import calcular_promedio, nota_maxima, nota_minima


def mostrar_menu():
    """Muestra el menu de opciones al usuario.

    Returns:
        None: solo imprime.
    """
    # TODO: imprime el menu con las opciones: 1=agregar, 2=listar, 3=promedio, 4=max/min, 5=salir
    pass


def ejecutar_opcion(opcion, notas):
    """Ejecuta la opcion elegida por el usuario.

    Args:
        opcion (str): opcion elegida (1-5).
        notas (list): lista de notas global.

    Returns:
        bool: True si el usuario quiere salir, False si no.
    """
    # TODO: usa match/case (o if/elif) para manejar las 5 opciones.
    # 1: pide una nota por input() y agregala. 2: muestra la lista.
    # 3: muestra el promedio. 4: muestra max y min. 5: retorna True.
    return False


def main():
    """Funcion principal del programa."""
    # TODO: muestra el menu en bucle, lee la opcion del usuario, ejecutala,
    # y termina solo cuando el usuario elija la opcion de salir
    pass


if __name__ == "__main__":
    main()
