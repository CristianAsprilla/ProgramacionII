import unittest
from main import evaluar_imc


class TestIMC(unittest.TestCase):
    def test_bajo_peso(self):
        # IMC = 50 / (1.70^2) ≈ 17.30 -> Bajo peso
        self.assertEqual(evaluar_imc(50, 1.70), "Bajo peso")

    def test_normal(self):
        # IMC = 70 / (1.75^2) ≈ 22.86 -> Normal
        self.assertEqual(evaluar_imc(70, 1.75), "Normal")
        # Límite inferior de Normal
        self.assertEqual(evaluar_imc(46.5, 1.60), "Normal")

    def test_sobrepeso(self):
        # IMC = 80 / (1.70^2) ≈ 27.68 -> Sobrepeso
        self.assertEqual(evaluar_imc(80, 1.70), "Sobrepeso")
        # Límite inferior de Sobrepeso
        self.assertEqual(evaluar_imc(72.25, 1.70), "Sobrepeso")

    def test_obesidad(self):
        # IMC = 100 / (1.70^2) ≈ 34.60 -> Obesidad
        self.assertEqual(evaluar_imc(100, 1.70), "Obesidad")
        # Límite inferior de Obesidad
        self.assertEqual(evaluar_imc(86.7, 1.70), "Obesidad")

    def test_altura_invalida(self):
        with self.assertRaises(ValueError):
            evaluar_imc(70, 0)
        with self.assertRaises(ValueError):
            evaluar_imc(70, -1.5)

    def test_peso_invalido(self):
        with self.assertRaises(ValueError):
            evaluar_imc(-5, 1.70)


if __name__ == "__main__":
    unittest.main()