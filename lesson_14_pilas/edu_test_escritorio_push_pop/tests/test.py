import unittest
from main import simular_pila


class TestSimularPila(unittest.TestCase):

    def test_solo_push(self):
        ops = ["push 1", "push 2", "push 3"]
        self.assertEqual(simular_pila(ops), [1, 2, 3])

    def test_solo_pop(self):
        ops = ["pop"]
        self.assertEqual(simular_pila(ops), [])

    def test_push_y_pop(self):
        ops = ["push 1", "push 2", "pop"]
        self.assertEqual(simular_pila(ops), [1])

    def test_mezcla(self):
        ops = ["push 1", "push 2", "push 3", "pop", "push 4"]
        # [1] -> [1,2] -> [1,2,3] -> [1,2] -> [1,2,4]
        self.assertEqual(simular_pila(ops), [1, 2, 4])

    def test_pila_vacia(self):
        self.assertEqual(simular_pila([]), [])

    def test_valor_pop(self):
        # El pop quita el ultimo push (LIFO)
        ops = ["push 10", "push 20", "pop"]
        self.assertEqual(simular_pila(ops), [10])