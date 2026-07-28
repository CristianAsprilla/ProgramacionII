# Una lista puede representar una pila.
pila = []
pila.append("acción: escribir")
pila.append("acción: borrar")

print("Cima:", pila[-1])
print("Deshacer:", pila.pop())
print("Pila restante:", pila)
