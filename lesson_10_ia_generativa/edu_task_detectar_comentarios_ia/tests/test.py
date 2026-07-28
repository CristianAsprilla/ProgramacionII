import unittest
from main import tiene_comentarios_redundantes


class TestTieneComentariosRedundantes(unittest.TestCase):

    def test_codigo_con_comentario_ia(self):
        codigo = "# Esta funcion suma dos numeros\ndef suma(a, b):\n    return a + b"
        self.assertTrue(tiene_comentarios_redundantes(codigo))

    def test_codigo_sin_comentarios(self):
        codigo = "def suma(a, b):\n    return a + b"
        self.assertFalse(tiene_comentarios_redundantes(codigo))

    def test_codigo_con_comentario_util(self):
        codigo = "# Algoritmo de Euclides para MCD\ndef mcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a"
        # No es patron IA, es comentario util
        self.assertFalse(tiene_comentarios_redundantes(codigo))

    def test_patron_ahora_retornamos(self):
        codigo = "# Ahora retornamos el resultado\ndef f():\n    return 1"
        self.assertTrue(tiene_comentarios_redundantes(codigo))

    def test_codigo_vacio(self):
        self.assertFalse(tiene_comentarios_redundantes(""))