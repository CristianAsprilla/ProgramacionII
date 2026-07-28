import unittest
from main import es_identificador_valido


class TestEsIdentificadorValido(unittest.TestCase):

    def test_nombre_simple_valido(self):
        self.assertTrue(es_identificador_valido("edad"))

    def test_nombre_con_digitos_valido(self):
        self.assertTrue(es_identificador_valido("edad2"))
        self.assertTrue(es_identificador_valido("x1"))

    def test_underscore_inicial_valido(self):
        self.assertTrue(es_identificador_valido("_privado"))
        self.assertTrue(es_identificador_valido("__dunder"))

    def test_empieza_con_digito_invalido(self):
        self.assertFalse(es_identificador_valido("2edad"))

    def test_guion_medio_invalido(self):
        self.assertFalse(es_identificador_valido("mi-variable"))

    def test_espacio_invalido(self):
        self.assertFalse(es_identificador_valido("mi variable"))

    def test_string_vacio_invalido(self):
        self.assertFalse(es_identificador_valido(""))

    def test_caracteres_especiales_invalido(self):
        self.assertFalse(es_identificador_valido("var!"))