import unittest
from main import clasificar_paradigma


class TestClasificarParadigma(unittest.TestCase):

    def test_detecta_imperativo(self):
        codigo = "x = 5\nfor i in range(10):\n    print(i)"
        resultado = clasificar_paradigma(codigo).lower()
        self.assertIn("imperativo", resultado)

    def test_detecta_funcional(self):
        codigo = "numeros = [1, 2, 3]\nresultado = list(map(lambda n: n*n, numeros))"
        resultado = clasificar_paradigma(codigo).lower()
        self.assertIn("funcional", resultado)

    def test_detecta_poo(self):
        codigo = "class Perro:\n    def ladrar(self):\n        print('Guau!')"
        resultado = clasificar_paradigma(codigo).lower()
        self.assertTrue(
            "poo" in resultado or "objeto" in resultado,
            msg=f"Resultado '{resultado}' no contiene 'poo' ni 'objeto'",
        )

    def test_retorna_string(self):
        resultado = clasificar_paradigma("x = 1")
        self.assertIsInstance(resultado, str)
        self.assertTrue(len(resultado) > 0)
