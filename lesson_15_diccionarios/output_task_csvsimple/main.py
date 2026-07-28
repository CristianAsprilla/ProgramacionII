# TODO Lee registros nombre,edad y muestra la persona mayor.
import sys
personas=[]
for linea in sys.stdin:
 linea=linea.strip()
 if linea:
  nombre,edad=linea.split(","); personas.append((nombre,int(edad)))
if personas: print(f"Persona mayor: {max(personas,key=lambda p:p[1])[0]}")
