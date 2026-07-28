import unittest
from main import contar_paradigmas


class TestContarParadigmas(unittest.TestCase):

    def test_retorna_diccionario(self):
        resultado = contar_paradigmas([])
        self.assertIsInstance(resultado, dict)

    def test_cuenta_un_paradigma(self):
        datos = [("Python", "multi-paradigma")]
        resultado = contar_paradigmas(datos)
        self.assertEqual(resultado.get("multi-paradigma"), 1)

    def test_cuenta_varios_paradigmas(self):
        datos = [
            ("C", "imperativo"),
            ("Java", "poo"),
            ("Python", "multi-paradigma"),
            ("Haskell", "funcional"),
        ]
        resultado = contar_paradigmas(datos)
        self.assertEqual(resultado.get("imperativo"), 1)
        self.assertEqual(resultado.get("poo"), 1)
        self.assertEqual(resultado.get("multi-paradigma"), 1)
        self.assertEqual(resultado.get("funcional"), 1)

    def test_cuenta_multiples_del_mismo(self):
        datos = [
            ("Python", "multi-paradigma"),
            ("JavaScript", "multi-paradigma"),
            ("Ruby", "multi-paradigma"),
        ]
        resultado = contar_paradigmas(datos)
        self.assertEqual(resultado.get("multi-paradigma"), 3)

    def test_lista_vacia_retorna_dict_vacio(self):
        resultado = contar_paradigmas([])
        self.assertEqual(resultado, {})