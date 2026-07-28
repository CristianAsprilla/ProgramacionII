import unittest
from main import suma_diagonal_secundaria


class TestSumaDiagonalSecundaria(unittest.TestCase):

    def test_matriz_3x3(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # 3 + 5 + 7 = 15
        self.assertEqual(suma_diagonal_secundaria(m), 15)

    def test_matriz_2x2(self):
        m = [[1, 2], [3, 4]]
        # 2 + 3 = 5
        self.assertEqual(suma_diagonal_secundaria(m), 5)

    def test_matriz_4x4(self):
        m = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
        # 4 + 7 + 10 + 13 = 34
        self.assertEqual(suma_diagonal_secundaria(m), 34)

    def test_matriz_1x1(self):
        self.assertEqual(suma_diagonal_secundaria([[7]]), 7)