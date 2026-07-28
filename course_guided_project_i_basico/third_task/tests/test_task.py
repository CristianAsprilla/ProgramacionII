import unittest
from main import leer_nombre, leer_edad


class TestLeerEntrada(unittest.TestCase):

    def test_leer_nombre_existe(self):
        self.assertTrue(callable(leer_nombre))

    def test_leer_edad_existe(self):
        self.assertTrue(callable(leer_edad))

    def test_leer_nombre_retorna_string(self):
        resultado = leer_nombre()
        self.assertIsInstance(resultado, str)
