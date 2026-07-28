import unittest
from main import tipo_variable


class TestTipoVariable(unittest.TestCase):

    def test_int(self):
        self.assertEqual(tipo_variable(5), "int")
        self.assertEqual(tipo_variable(0), "int")
        self.assertEqual(tipo_variable(-10), "int")

    def test_float(self):
        self.assertEqual(tipo_variable(3.14), "float")
        self.assertEqual(tipo_variable(0.0), "float")
        self.assertEqual(tipo_variable(-2.5), "float")

    def test_str(self):
        self.assertEqual(tipo_variable("hola"), "str")
        self.assertEqual(tipo_variable(""), "str")

    def test_bool(self):
        self.assertEqual(tipo_variable(True), "bool")
        self.assertEqual(tipo_variable(False), "bool")

    def test_list(self):
        self.assertEqual(tipo_variable([1, 2]), "list")
        self.assertEqual(tipo_variable([]), "list")

    def test_otros(self):
        self.assertEqual(tipo_variable((1, 2)), "otro")
        self.assertEqual(tipo_variable({1: 2}), "otro")
        self.assertEqual(tipo_variable(None), "otro")