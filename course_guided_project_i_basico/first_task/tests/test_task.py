import unittest
from main import crear_saludo


class TestCrearSaludo(unittest.TestCase):

    def test_saludo_con_nombre_y_edad(self):
        resultado = crear_saludo("María", 17)
        self.assertIn("María", resultado, msg="El saludo debe incluir el nombre")
        self.assertIn("17", resultado, msg="El saludo debe incluir la edad")

    def test_saludo_con_otro_nombre(self):
        resultado = crear_saludo("Carlos", 18)
        self.assertIn("Carlos", resultado)
        self.assertIn("18", resultado)

    def test_saludo_no_vacio(self):
        resultado = crear_saludo("Ana", 16)
        self.assertTrue(len(resultado) > 0, msg="El saludo no puede estar vacío")
