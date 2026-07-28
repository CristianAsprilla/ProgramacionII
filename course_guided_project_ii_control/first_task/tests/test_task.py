import unittest
from main import agregar_nota, listar_notas


class TestAgregarNota(unittest.TestCase):

    def setUp(self):
        self.notas = []

    def test_agregar_nota_valida(self):
        resultado = agregar_nota(self.notas, 85)
        self.assertTrue(resultado, msg="Una nota válida debe devolverse True")
        self.assertEqual(self.notas, [85], msg="La nota debe estar en la lista")

    def test_agregar_nota_cero(self):
        self.assertTrue(agregar_nota(self.notas, 0))
        self.assertEqual(self.notas, [0])

    def test_agregar_nota_cien(self):
        self.assertTrue(agregar_nota(self.notas, 100))
        self.assertEqual(self.notas, [100])

    def test_rechazar_nota_negativa(self):
        self.assertFalse(agregar_nota(self.notas, -5))
        self.assertEqual(self.notas, [], msg="Una nota inválida no debe agregarse")

    def test_rechazar_nota_mayor_100(self):
        self.assertFalse(agregar_nota(self.notas, 150))
        self.assertEqual(self.notas, [])


class TestListarNotas(unittest.TestCase):

    def test_lista_vacia(self):
        resultado = listar_notas([])
        # Acepta cualquier frase que indique que no hay notas
        self.assertIn("no", resultado.lower())

    def test_lista_con_notas(self):
        resultado = listar_notas([80, 90, 100])
        self.assertIn("80", resultado)
        self.assertIn("90", resultado)
        self.assertIn("100", resultado)
