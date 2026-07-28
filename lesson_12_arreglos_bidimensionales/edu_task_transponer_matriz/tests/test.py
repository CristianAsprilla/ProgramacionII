import unittest
from main import transponer


class TestTransponer(unittest.TestCase):

    def test_2x3(self):
        m = [[1, 2, 3], [4, 5, 6]]
        resultado = transponer(m)
        self.assertEqual(resultado, [[1, 4], [2, 5], [3, 6]])

    def test_3x2(self):
        m = [[1, 4], [2, 5], [3, 6]]
        resultado = transponer(m)
        self.assertEqual(resultado, [[1, 2, 3], [4, 5, 6]])

    def test_cuadrada_2x2(self):
        m = [[1, 2], [3, 4]]
        resultado = transponer(m)
        self.assertEqual(resultado, [[1, 3], [2, 4]])

    def test_1x3(self):
        m = [[1, 2, 3]]
        resultado = transponer(m)
        self.assertEqual(resultado, [[1], [2], [3]])

    def test_fila_a_columna(self):
        # 1xN a Nx1
        resultado = transponer([[5, 10, 15]])
        self.assertEqual(resultado, [[5], [10], [15]])