import unittest
from main import crear_tarjeta


class TestCrearTarjeta(unittest.TestCase):

    def test_incluye_nombre(self):
        resultado = crear_tarjeta("María", 17, "BTI - Panamá", 3, 92.5, 6)
        self.assertIn("María", resultado, msg="La tarjeta debe incluir el nombre")

    def test_incluye_edad(self):
        resultado = crear_tarjeta("María", 17, "BTI - Panamá", 3, 92.5, 6)
        self.assertIn("17", resultado, msg="La tarjeta debe incluir la edad")

    def test_incluye_promedio(self):
        resultado = crear_tarjeta("María", 17, "BTI - Panamá", 3, 92.5, 6)
        self.assertIn("92.5", resultado, msg="La tarjeta debe incluir el promedio")

    def test_incluye_materias(self):
        resultado = crear_tarjeta("María", 17, "BTI - Panamá", 3, 92.5, 6)
        self.assertIn("6", resultado, msg="La tarjeta debe incluir la cantidad de materias")

    def test_tarjeta_no_vacia(self):
        resultado = crear_tarjeta("Ana", 16, "BTI", 1, 85.0, 5)
        self.assertTrue(len(resultado) > 0, msg="La tarjeta no puede estar vacía")
