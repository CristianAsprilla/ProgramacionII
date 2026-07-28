import unittest
from main import validar_nombre, validar_edad, pedir_nombre_valido


class TestValidar(unittest.TestCase):

    def test_nombre_valido(self):
        self.assertTrue(validar_nombre("Maria"))
        self.assertTrue(validar_nombre("  Juan  "))

    def test_nombre_invalido(self):
        self.assertFalse(validar_nombre(""))
        self.assertFalse(validar_nombre(" "))
        self.assertFalse(validar_nombre("A"))

    def test_edad_valida(self):
        self.assertTrue(validar_edad(17))
        self.assertTrue(validar_edad(5))
        self.assertTrue(validar_edad(100))

    def test_edad_invalida(self):
        self.assertFalse(validar_edad(0))
        self.assertFalse(validar_edad(4))
        self.assertFalse(validar_edad(101))
        self.assertFalse(validar_edad(-5))
