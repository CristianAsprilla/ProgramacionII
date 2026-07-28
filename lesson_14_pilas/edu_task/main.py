class Pila:
    def __init__(self):
        self.elementos = []

    # INICIO DE LA IMPLEMENTACIÓN
    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            # TODO: implementa los metodos de la clase Pila
            return None
        return self.elementos.pop()

    def cima(self):
        if self.esta_vacia():
            return None
        return self.elementos[-1]

    def esta_vacia(self):
        return len(self.elementos) == 0
    # FIN DE LA IMPLEMENTACIÓN


def parentesis_balanceados(expresion):
    pila = Pila()
    parejas = {")": "(", "]": "[", "}": "{"
    }
    aperturas = set(parejas.values())

    for caracter in expresion:
        if caracter in aperturas:
            pila.apilar(caracter)
        elif caracter in parejas:
            if pila.esta_vacia() or pila.desapilar() != parejas[caracter]:
                return False
    return pila.esta_vacia()


if __name__ == "__main__":
    print(parentesis_balanceados("a * (b + [c - d])"))
    print(parentesis_balanceados("([)]"))
