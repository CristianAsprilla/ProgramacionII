import unittest
from main import evaluar_posfija
class Pruebas(unittest.TestCase):
    def test_suma(self): self.assertEqual(evaluar_posfija("3 4 +"),7)
    def test_dos(self): self.assertEqual(evaluar_posfija("3 4 + 2 *"),14)
    def test_tres(self): self.assertEqual(evaluar_posfija("5 1 2 + 4 * + 3 -"),14)
