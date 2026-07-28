import unittest
from main import contar_comentarios


class TestContarComentarios(unittest.TestCase):

    def test_codigo_sin_comentarios(self):
        codigo = "x = 5\ny = 10\nprint(x)"
        self.assertEqual(contar_comentarios(codigo), 0)

    def test_una_linea_de_comentario(self):
        codigo = "# hola mundo\nx = 5"
        self.assertEqual(contar_comentarios(codigo), 1)

    def test_multiples_comentarios(self):
        codigo = "# primero\nx = 5\n# segundo\ny = 10\n# tercero"
        self.assertEqual(contar_comentarios(codigo), 3)

    def test_codigo_vacio(self):
        self.assertEqual(contar_comentarios(""), 0)

    def test_solo_comentarios(self):
        codigo = "# solo comentarios\n# mas comentarios"
        self.assertEqual(contar_comentarios(codigo), 2)