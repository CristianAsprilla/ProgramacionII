import unittest
from main import buscar_nota, contar_notas_en_rango


class TestBuscar(unittest.TestCase):

    def test_buscar_existe(self):
        self.assertEqual(buscar_nota([1, 2, 3, 4], 3), 2)

    def test_buscar_no_existe(self):
        self.assertEqual(buscar_nota([1, 2, 3], 5), -1)

    def test_buscar_primera_ocurrencia(self):
        self.assertEqual(buscar_nota([1, 2, 3, 2, 1], 2), 1)

    def test_contar_rango(self):
        self.assertEqual(contar_notas_en_rango([1, 2, 3, 4, 5], 2, 4), 3)

    def test_contar_vacio(self):
        self.assertEqual(contar_notas_en_rango([], 0, 100), 0)
