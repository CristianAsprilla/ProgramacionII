import unittest

from main import calcular


class TestCalculadoraSimple(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(calcular(8, 5, "suma"), 13)

    def test_resta(self):
        self.assertEqual(calcular(8, 5, "resta"), 3)

    def test_multiplicacion(self):
        self.assertEqual(calcular(8, 5, "multiplicacion"), 40)

    def test_division(self):
        self.assertAlmostEqual(calcular(8, 5, "division"), 1.6)

    def test_division_por_cero_devuelve_none(self):
        self.assertIsNone(calcular(8, 0, "division"))

    def test_operacion_desconocida_lanza_error(self):
        with self.assertRaises(ValueError):
            calcular(8, 5, "potencia")


if __name__ == "__main__":
    unittest.main()
