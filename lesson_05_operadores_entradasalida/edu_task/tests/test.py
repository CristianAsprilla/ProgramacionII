import unittest
from main import calcular_imc, clasificar_imc


class TestCalcularIMC(unittest.TestCase):

    def test_imc_normal(self):
        # 70 / 1.75^2 = 22.857... -> 22.86
        self.assertAlmostEqual(calcular_imc(70, 1.75), 22.86, places=2)

    def test_imc_bajo_peso(self):
        # 50 / 1.75^2 = 16.326... -> 16.33
        self.assertAlmostEqual(calcular_imc(50, 1.75), 16.33, places=2)

    def test_imc_sobrepeso(self):
        # 85 / 1.70^2 = 29.41
        self.assertAlmostEqual(calcular_imc(85, 1.70), 29.41, places=2)

    def test_imc_obesidad(self):
        # 120 / 1.70^2 = 41.52
        self.assertAlmostEqual(calcular_imc(120, 1.70), 41.52, places=2)


class TestClasificarIMC(unittest.TestCase):

    def test_bajo_peso(self):
        self.assertEqual(clasificar_imc(17.0), "Bajo peso")
        self.assertEqual(clasificar_imc(18.4), "Bajo peso")

    def test_normal(self):
        self.assertEqual(clasificar_imc(18.5), "Normal")
        self.assertEqual(clasificar_imc(22.5), "Normal")
        self.assertEqual(clasificar_imc(24.9), "Normal")

    def test_sobrepeso(self):
        self.assertEqual(clasificar_imc(25.0), "Sobrepeso")
        self.assertEqual(clasificar_imc(29.9), "Sobrepeso")

    def test_obesidad(self):
        self.assertEqual(clasificar_imc(30.0), "Obesidad")
        self.assertEqual(clasificar_imc(45.0), "Obesidad")
