import unittest
from main import Pila, parentesis_balanceados


class PruebasPila(unittest.TestCase):
    def test_pila_nueva_esta_vacia(self):
        pila = Pila()
        self.assertTrue(pila.esta_vacia())
        self.assertIsNone(pila.cima())
        self.assertIsNone(pila.desapilar())

    def test_operaciones_lifo(self):
        pila = Pila()
        pila.apilar("primero")
        pila.apilar("segundo")
        self.assertFalse(pila.esta_vacia())
        self.assertEqual(pila.cima(), "segundo")
        self.assertEqual(pila.desapilar(), "segundo")
        self.assertEqual(pila.cima(), "primero")
        self.assertEqual(pila.desapilar(), "primero")
        self.assertTrue(pila.esta_vacia())


class PruebasParentesis(unittest.TestCase):
    def test_expresiones_balanceadas(self):
        self.assertTrue(parentesis_balanceados("a * (b + [c - d])"))
        self.assertTrue(parentesis_balanceados("sin({x + y} / [z])"))
        self.assertTrue(parentesis_balanceados("sin simbolos"))

    def test_expresiones_no_balanceadas(self):
        self.assertFalse(parentesis_balanceados("([)]"))
        self.assertFalse(parentesis_balanceados("(a + b"))
        self.assertFalse(parentesis_balanceados("a + b)"))
