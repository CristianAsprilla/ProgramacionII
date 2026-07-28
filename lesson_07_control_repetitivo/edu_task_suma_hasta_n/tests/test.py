import unittest
from main import suma_hasta_n


class TestSumaHastaN(unittest.TestCase):

    def test_n_5(self):
        # 1 + 2 + 3 + 4 + 5 = 15
        self.assertEqual(suma_hasta_n(5), 15)

    def test_n_10(self):
        # 1 + 2 + ... + 10 = 55
        self.assertEqual(suma_hasta_n(10), 55)

    def test_n_1(self):
        self.assertEqual(suma_hasta_n(1), 1)

    def test_n_0(self):
        # La suma de 0 numeros es 0
        self.assertEqual(suma_hasta_n(0), 0)

    def test_n_100(self):
        # 1 + 2 + ... + 100 = 5050 (famosa suma de Gauss)
        self.assertEqual(suma_hasta_n(100), 5050)