import unittest

from main import contar_vocales, empieza_con_guion_bajo


class TestContarVocales(unittest.TestCase):

    def test_cuenta_vocales_de_una_palabra(self):
        self.assertEqual(contar_vocales("computadora"), 5)

    def test_no_distingue_mayusculas_y_cuenta_acento(self):
        self.assertEqual(contar_vocales("Panamá"), 3)

    def test_cadena_sin_vocales_o_vacia(self):
        self.assertEqual(contar_vocales("rhythms 123"), 0)
        self.assertEqual(contar_vocales(""), 0)


class TestEmpiezaConGuionBajo(unittest.TestCase):

    def test_identificador_con_un_guion_bajo(self):
        self.assertTrue(empieza_con_guion_bajo("_nota"))

    def test_identificador_con_dos_guiones_bajos(self):
        self.assertTrue(empieza_con_guion_bajo("__privado"))

    def test_identificadores_que_no_comienzan_con_guion_bajo(self):
        self.assertFalse(empieza_con_guion_bajo("nota"))
        self.assertFalse(empieza_con_guion_bajo(""))


if __name__ == "__main__":
    unittest.main()
