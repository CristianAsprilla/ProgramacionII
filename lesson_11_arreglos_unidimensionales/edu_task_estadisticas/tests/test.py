import unittest
from main import estadisticas
class Pruebas(unittest.TestCase):
    def test_vacia(self): self.assertEqual(estadisticas([]), {"minima":0,"maxima":0,"suma":0,"promedio":0})
    def test_uno(self): self.assertEqual(estadisticas([4]), {"minima":4,"maxima":4,"suma":4,"promedio":4})
    def test_varias(self): self.assertEqual(estadisticas([3,5,4]), {"minima":3,"maxima":5,"suma":12,"promedio":4})
