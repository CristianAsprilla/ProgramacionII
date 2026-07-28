import unittest
from main import calcular_imc, categoria_imc


class TestIMC(unittest.TestCase):

    def test_imc_normal(self):
        self.assertAlmostEqual(calcular_imc(70, 1.75), 22.86, places=2)

    def test_imc_bajo(self):
        self.assertAlmostEqual(calcular_imc(50, 1.70), 17.30, places=2)

    def test_categoria_bajo(self):
        self.assertEqual(categoria_imc(17.0), "bajo peso")

    def test_categoria_normal(self):
        self.assertEqual(categoria_imc(22.0), "normal")

    def test_categoria_sobrepeso(self):
        self.assertEqual(categoria_imc(27.0), "sobrepeso")

    def test_categoria_obesidad(self):
        self.assertEqual(categoria_imc(33.0), "obesidad")
