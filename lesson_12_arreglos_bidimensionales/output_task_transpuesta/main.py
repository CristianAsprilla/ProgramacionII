# TODO Lee tres filas y muestra la matriz transpuesta.
import sys
filas=[list(map(int,l.split())) for l in sys.stdin if l.strip()]
for col in range(3): print(" ".join(str(filas[f][col]) for f in range(3)))
