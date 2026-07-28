import unittest
from main import filtrar_pares


class TestFiltrarPares(unittest.TestCase):

    def test_lista_mixta(self):
        self.assertEqual(filtrar_pares([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_solo_impares(self):
        self.assertEqual(filtrar_pares([1, 3, 5]), [])

    def test_lista_vacia(self):
        self.assertEqual(filtrar_pares([]), [])

    def test_con_negativos(self):
        self.assertEqual(filtrar_pares([0, -2, -3, 4]), [0, -2, 4])

    def test_solo_pares(self):
        self.assertEqual(filtrar_pares([2, 4, 6]), [2, 4, 6])

    def test_no_modifica_original(self):
        original = [1, 2, 3]
        filtrar_pares(original)
        self.assertEqual(original, [1, 2, 3])