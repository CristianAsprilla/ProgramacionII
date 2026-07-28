# TODO: lee el nombre desde stdin y muestra un saludo usando f-string
if __name__ == '__main__':
 numero = 0 # lee el número entero desde stdin
 tipo = type(numero).__name__
 doble = numero * 2 # imprime el tipo y el doble del número
 print(f"Tipo: {tipo}")
 print(f"Doble: {doble}")