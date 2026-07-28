# TODO: lee los numeros y calcula el promedio de la lista
import sys


entrada = sys.stdin.read().strip()
n = int(entrada) if entrada else 0
pares = [str(2 * indice) for indice in range(n)]
print(" ".join(pares))
