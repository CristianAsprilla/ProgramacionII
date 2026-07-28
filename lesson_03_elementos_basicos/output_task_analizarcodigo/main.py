"""Analizador inicial de identificadores en líneas de código."""

import keyword
import sys


def identificar(identificador):
    """Devuelve si un texto puede usarse como identificador de Python."""
    # TODO: completa la validación.
    # identifica los identificadores válidos vs inválidos en el código
    return False


if __name__ == "__main__":
    for linea in sys.stdin:
        identificador = linea.split("=", 1)[0].strip()
        if identificar(identificador):
            print(f"válido: {identificador}")
        else:
            print(f"inválido: {identificador}")
