import unittest
from main import frecuencia_palabras
class Pruebas(unittest.TestCase):
 def test_repetidas(self): self.assertEqual(frecuencia_palabras("hola mundo hola"),{"hola":2,"mundo":1})
 def test_vacio(self): self.assertEqual(frecuencia_palabras(""),{})
