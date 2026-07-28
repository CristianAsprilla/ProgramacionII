import unittest
from main import mediana


class PruebasMediana(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertIsNone(mediana([]))

    def test_un_elemento(self):
        self.assertEqual(mediana([4.8]), 4.8)

    def test_dos_elementos(self):
        self.assertAlmostEqual(mediana([3.0, 5.0]), 4.0)

    def test_cantidad_impar(self):
        self.assertAlmostEqual(mediana([4.0, 4.5, 5.0]), 4.5)

    def test_cantidad_par(self):
        self.assertAlmostEqual(mediana([3.0, 4.0, 4.5, 5.0]), 4.25)

    def test_no_ordenadas(self):
        self.assertAlmostEqual(mediana([5.0, 3.0, 4.0, 4.5]), 4.25)