import unittest
from main import primos_hasta


class TestPrimosHasta(unittest.TestCase):

    def test_hasta_10(self):
        self.assertEqual(primos_hasta(10), [2, 3, 5, 7])

    def test_hasta_20(self):
        self.assertEqual(primos_hasta(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_hasta_30(self):
        self.assertEqual(primos_hasta(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_hasta_1(self):
        self.assertEqual(primos_hasta(1), [])

    def test_hasta_2(self):
        self.assertEqual(primos_hasta(2), [2])

    def test_hasta_100_conteo(self):
        # Hay 25 primos hasta 100
        self.assertEqual(len(primos_hasta(100)), 25)