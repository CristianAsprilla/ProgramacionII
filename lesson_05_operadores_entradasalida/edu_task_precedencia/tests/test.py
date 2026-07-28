import unittest
from main import calcular_expresion


class TestCalcularExpresion(unittest.TestCase):

    def test_uno_dos_tres(self):
        # 1 + 2 * 3 = 1 + 6 = 7 (multiplicacion primero)
        self.assertEqual(calcular_expresion(1, 2, 3), 7)

    def test_cinco_uno_cuatro(self):
        # 5 + 1 * 4 = 5 + 4 = 9
        self.assertEqual(calcular_expresion(5, 1, 4), 9)

    def test_diez_dos_tres(self):
        # 10 + 2 * 3 = 10 + 6 = 16
        self.assertEqual(calcular_expresion(10, 2, 3), 16)

    def test_ceros(self):
        self.assertEqual(calcular_expresion(0, 0, 0), 0)

    def test_negativos(self):
        # -1 + 2 * 3 = -1 + 6 = 5
        self.assertEqual(calcular_expresion(-1, 2, 3), 5)