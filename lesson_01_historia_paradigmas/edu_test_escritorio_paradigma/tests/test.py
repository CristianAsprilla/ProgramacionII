import unittest
from main import predecir_output


class TestPredecirOutput(unittest.TestCase):

    def test_retorna_string(self):
        resultado = predecir_output("x = 1", "python")
        self.assertIsInstance(resultado, str)
        self.assertTrue(len(resultado) > 0)

    def test_detecta_poo(self):
        codigo = "class Coche:\n    def arrancar(self):\n        print('Arrancando')"
        resultado = predecir_output(codigo, "python").lower()
        self.assertTrue("poo" in resultado or "objeto" in resultado,
                        msg=f"Resultado {resultado!r} no contiene 'poo' ni 'objeto'")

    def test_detecta_funcional(self):
        codigo = "numeros = list(map(lambda x: x*2, [1,2,3]))"
        resultado = predecir_output(codigo, "python").lower()
        self.assertIn("funcional", resultado)

    def test_detecta_imperativo(self):
        codigo = "x = 5\nfor i in range(x):\n    print(i)"
        resultado = predecir_output(codigo, "python").lower()
        self.assertIn("imperativo", resultado)