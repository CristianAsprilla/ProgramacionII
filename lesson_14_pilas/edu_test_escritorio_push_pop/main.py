"""Simula operaciones de pila (LIFO)."""


def simular_pila(operaciones):
    """Simula operaciones sobre una pila y retorna el estado final.

    Args:
        operaciones (list): lista de operaciones, cada una es:
            - un string "push X" para apilar X
            - un string "pop" para desapilar

    Returns:
        list: estado final de la pila (de base a tope).
    """
    # TODO: simula la pila procesando las operaciones en orden
    return []


if __name__ == "__main__":
    ops = ["push 1", "push 2", "push 3", "pop", "push 4"]
    # Pila: [1, 2, 3] -> push 4 = [1, 2, 3, 4]
    # push 2: [1, 2] -> push 3: [1, 2, 3] -> pop: [1, 2] -> push 4: [1, 2, 4]
    print(simular_pila(ops))  # [1, 2, 4]