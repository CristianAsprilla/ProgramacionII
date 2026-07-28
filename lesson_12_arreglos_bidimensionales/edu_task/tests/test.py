import unittest
from main import suma_diagonal_principal


class PruebasDiagonalPrincipal(unittest.TestCase):
    def test_matriz_de_ejemplo(self):
        matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(suma_diagonal_principal(matriz), 15)

    def test_matriz_de_notas(self):
        matriz = [[4.5, 4.0, 4.8], [3.9, 4.2, 4.6], [5.0, 4.7, 4.9]]
        self.assertAlmostEqual(suma_diagonal_principal(matriz), 13.6)

    def test_matriz_de_una_celda(self):
        self.assertEqual(suma_diagonal_principal([[7]]), 7)
