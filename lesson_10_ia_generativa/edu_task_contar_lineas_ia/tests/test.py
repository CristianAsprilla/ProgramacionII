import unittest
from main import contar_lineas_codigo


class TestContarLineasCodigo(unittest.TestCase):

    def test_solo_codigo(self):
        codigo = "x = 5\ny = 10\nprint(x + y)"
        self.assertEqual(contar_lineas_codigo(codigo), 3)

    def test_con_comentarios(self):
        codigo = "# hola\nx = 5\n# mundo\ny = 10"
        self.assertEqual(contar_lineas_codigo(codigo), 2)

    def test_con_lineas_vacias(self):
        codigo = "x = 1\n\ny = 2\n"
        self.assertEqual(contar_lineas_codigo(codigo), 2)

    def test_codigo_vacio(self):
        self.assertEqual(contar_lineas_codigo(""), 0)

    def test_solo_comentarios(self):
        codigo = "# solo comentarios\n# nada mas"
        self.assertEqual(contar_lineas_codigo(codigo), 0)