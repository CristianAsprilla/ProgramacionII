# TODO Lee tareas hasta FIN y muestra cuántas se registraron.
import sys
tareas=[]
for linea in sys.stdin:
    tarea=linea.strip()
    if tarea == "FIN": break
    if tarea: tareas.append(tarea)
print(f"Total de tareas: {len(tareas)}")
