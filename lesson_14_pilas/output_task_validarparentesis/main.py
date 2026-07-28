# TODO Lee una expresión con paréntesis, corchetes y llaves; usa una pila para
# verificar que estén balanceados. Imprime "Balanceado" o "No balanceado".
import sys


def validar(expresion):
    pila = []
    pares = {")": "(", "]": "[", "}": "{"}
    aperturas = set(pares.values())

    for caracter in expresion:
        if caracter in aperturas:
            pila.append(caracter)
        elif caracter in pares:
            if not pila or pila.pop() != pares[caracter]:
                return False
    return not pila


def main():
    entrada = sys.stdin.read()
    # Tomar la primera línea no vacía
    for linea in entrada.splitlines():
        if linea.strip():
            expresion = linea
            break
    else:
        expresion = ""
    if validar(expresion):
        print("Balanceado")
    else:
        print("No balanceado")


if __name__ == "__main__":
    main()