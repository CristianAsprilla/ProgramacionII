import unittest
from main import datos_rectangulo


class TestCase(unittest.TestCase):

    def test_area_y_perimetro_basicos(self):
        # Rectangulo 8.5 x 4.2
        # area = 8.5 * 4.2 = 35.7
        # perimetro = 2 * (8.5 + 4.2) = 2 * 12.7 = 25.4
        resultado = datos_rectangulo(8.5, 4.2)
        self.assertAlmostEqual(
            resultado["area"],
            35.7,
            msg="Area incorrecta para rectangulo 8.5 x 4.2",
        )
        self.assertAlmostEqual(
            resultado["perimetro"],
            25.4,
            msg="Perimetro incorrecto para rectangulo 8.5 x 4.2",
        )

    def test_cuadrado(self):
        # Un cuadrado de 5 x 5 tiene area 25 y perimetro 20
        resultado = datos_rectangulo(5, 5)
        self.assertAlmostEqual(resultado["area"], 25)
        self.assertAlmostEqual(resultado["perimetro"], 20)

    def test_rectangulo_con_base_decimal(self):
        # Rectangulo 3 x 10.5
        # area = 3 * 10.5 = 31.5
        # perimetro = 2 * (3 + 10.5) = 27.0
        resultado = datos_rectangulo(3, 10.5)
        self.assertAlmostEqual(resultado["area"], 31.5)
        self.assertAlmostEqual(resultado["perimetro"], 27.0)

    def test_retorna_diccionario(self):
        resultado = datos_rectangulo(2, 3)
        self.assertIsInstance(resultado, dict, msg="Debe devolver un dict")
        self.assertIn("area", resultado)
        self.assertIn("perimetro", resultado)

    def test_valores_enteros(self):
        # Rectangulo 10 x 20
        # area = 200, perimetro = 60
        resultado = datos_rectangulo(10, 20)
        self.assertAlmostEqual(resultado["area"], 200)
        self.assertAlmostEqual(resultado["perimetro"], 60)
