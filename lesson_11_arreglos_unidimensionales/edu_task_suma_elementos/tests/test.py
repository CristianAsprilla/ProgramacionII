import unittest
from main import sumar_elementos


class TestSumarElementos(unittest.TestCase):

    def test_lista_normal(self):
        self.assertEqual(sumar_elementos([1, 2, 3, 4]), 10)

    def test_lista_vacia(self):
        self.assertEqual(sumar_elementos([]), 0)

    def test_un_elemento(self):
        self.assertEqual(sumar_elementos([5]), 5)

    def test_negativos(self):
        self.assertEqual(sumar_elementos([-1, -2, -3]), -6)

    def test_floats(self):
        self.assertAlmostEqual(sumar_elementos([1.5, 2.5]), 4.0)