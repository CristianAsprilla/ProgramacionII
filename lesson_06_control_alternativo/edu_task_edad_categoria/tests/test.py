import unittest
from main import clasificar_edad


class TestClasificarEdad(unittest.TestCase):

    def test_nino(self):
        self.assertEqual(clasificar_edad(0), "nino")
        self.assertEqual(clasificar_edad(5), "nino")
        self.assertEqual(clasificar_edad(12), "nino")

    def test_adolescente(self):
        self.assertEqual(clasificar_edad(13), "adolescente")
        self.assertEqual(clasificar_edad(15), "adolescente")
        self.assertEqual(clasificar_edad(17), "adolescente")

    def test_adulto(self):
        self.assertEqual(clasificar_edad(18), "adulto")
        self.assertEqual(clasificar_edad(30), "adulto")
        self.assertEqual(clasificar_edad(64), "adulto")

    def test_adulto_mayor(self):
        self.assertEqual(clasificar_edad(65), "adulto mayor")
        self.assertEqual(clasificar_edad(80), "adulto mayor")

    def test_limites(self):
        # 12 es nino (inclusive)
        self.assertEqual(clasificar_edad(12), "nino")
        # 13 es adolescente
        self.assertEqual(clasificar_edad(13), "adolescente")
        # 64 es adulto
        self.assertEqual(clasificar_edad(64), "adulto")
        # 65 es adulto mayor
        self.assertEqual(clasificar_edad(65), "adulto mayor")