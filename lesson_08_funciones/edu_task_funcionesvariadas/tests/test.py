import unittest
from math import pi
from main import area_circulo, fahrenheit_a_celsius


class TestFuncionesVariadas(unittest.TestCase):
    def test_area_circulo(self):
        self.assertAlmostEqual(area_circulo(1), pi)
        self.assertAlmostEqual(area_circulo(2), 4 * pi)
        self.assertAlmostEqual(area_circulo(0), 0)

    def test_area_circulo_negativo(self):
        with self.assertRaises(ValueError):
            area_circulo(-1)

    def test_fahrenheit_a_celsius(self):
        self.assertAlmostEqual(fahrenheit_a_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_a_celsius(212), 100)
        self.assertAlmostEqual(fahrenheit_a_celsius(100), (100 - 32) * 5 / 9)
        self.assertAlmostEqual(fahrenheit_a_celsius(-40), -40)


if __name__ == "__main__":
    unittest.main()