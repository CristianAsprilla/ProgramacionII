import unittest
from main import analizar_notas


class PruebasAnalizarNotas(unittest.TestCase):
    def test_promedio_y_maxima(self):
        promedio, maxima = analizar_notas([4.0, 4.5, 5.0])
        self.assertAlmostEqual(promedio, 4.5)
        self.assertEqual(maxima, 5.0)

    def test_notas_decimales(self):
        promedio, maxima = analizar_notas([3.2, 4.1, 3.7, 4.0])
        self.assertAlmostEqual(promedio, 3.75)
        self.assertEqual(maxima, 4.1)

    def test_una_nota(self):
        promedio, maxima = analizar_notas([4.8])
        self.assertEqual(promedio, 4.8)
        self.assertEqual(maxima, 4.8)
