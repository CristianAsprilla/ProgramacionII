import unittest
from main import filtrar_mayores, duplicar
class Pruebas(unittest.TestCase):
 def test_filtrar(self): self.assertEqual(filtrar_mayores([1,4,6,2],3),[4,6])
 def test_duplicar(self): self.assertEqual(duplicar([1,2]),[1,1,2,2])
