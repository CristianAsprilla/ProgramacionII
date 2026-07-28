import unittest

from main import intercambiar


class TestIntercambiar(unittest.TestCase):

    def test_intercambia_numeros_positivos(self):
        self.assertEqual(intercambiar(3, 8), (8, 3))

    def test_intercambia_un_numero_negativo(self):
        self.assertEqual(intercambiar(-4, 7), (7, -4))

    def test_intercambia_dos_numeros_negativos(self):
        self.assertEqual(intercambiar(-2, -9), (-9, -2))

    def test_intercambia_textos_y_devuelve_una_tupla(self):
        resultado = intercambiar("Colón", "Panamá")
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(resultado, ("Panamá", "Colón"))


if __name__ == "__main__":
    unittest.main()
