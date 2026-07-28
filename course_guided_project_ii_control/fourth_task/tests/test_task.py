import unittest
from main import ordenar_notas


class TestOrdenarNotas(unittest.TestCase):

    def test_ascendente(self):
        resultado = ordenar_notas([5, 2, 8, 1, 9])
        self.assertEqual(resultado, [1, 2, 5, 8, 9])

    def test_descendente(self):
        resultado = ordenar_notas([5, 2, 8, 1, 9], descendente=True)
        self.assertEqual(resultado, [9, 8, 5, 2, 1])

    def test_lista_vacia(self):
        self.assertEqual(ordenar_notas([]), [])

    def test_un_elemento(self):
        self.assertEqual(ordenar_notas([5]), [5])
