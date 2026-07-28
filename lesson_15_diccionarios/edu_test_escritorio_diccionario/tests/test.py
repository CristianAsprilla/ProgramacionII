import unittest
from main import simular_diccionario


class TestSimularDiccionario(unittest.TestCase):

    def test_solo_set(self):
        ops = ["set a 1", "set b 2"]
        self.assertEqual(simular_diccionario(ops), [])

    def test_solo_get_existente(self):
        ops = ["get a"]
        # sin set previo, retorna None
        self.assertEqual(simular_diccionario(ops), [None])

    def test_set_y_get(self):
        ops = ["set nombre Ana", "get nombre"]
        self.assertEqual(simular_diccionario(ops), ["Ana"])

    def test_mezcla(self):
        ops = ["set nombre Ana", "set edad 17", "get nombre", "get ciudad"]
        # ciudad no existe, retorna None
        self.assertEqual(simular_diccionario(ops), ["Ana", None])

    def test_valores_enteros(self):
        ops = ["set x 10", "get x"]
        self.assertEqual(simular_diccionario(ops), [10])

    def test_sobreescribir(self):
        ops = ["set x 1", "set x 2", "get x"]
        self.assertEqual(simular_diccionario(ops), [2])