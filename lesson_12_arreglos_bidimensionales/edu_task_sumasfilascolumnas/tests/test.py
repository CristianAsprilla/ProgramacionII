import unittest
from main import suma_fila, suma_columna
class Pruebas(unittest.TestCase):
 m=[[1,2,3],[4,5,6],[7,8,9]]
 def test_filas(self): self.assertEqual(suma_fila(self.m,0),6); self.assertEqual(suma_fila(self.m,2),24)
 def test_columnas(self): self.assertEqual(suma_columna(self.m,0),12); self.assertEqual(suma_columna(self.m,2),18)
