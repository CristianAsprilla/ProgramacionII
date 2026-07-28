import unittest
from math import pi
from geometria import area_circulo, area_rectangulo
from main import resumen_areas
class TestGeometria(unittest.TestCase):
    def test_areas(self):
        self.assertAlmostEqual(area_circulo(2), 4 * pi)
        self.assertEqual(area_rectangulo(5, 4), 20)
        self.assertEqual(resumen_areas(1, 2, 3), (pi, 6))
    def test_negativos(self):
        with self.assertRaises(ValueError): area_circulo(-1)
        with self.assertRaises(ValueError): area_rectangulo(2, -1)
if __name__ == "__main__": unittest.main()
