import unittest
from main import clasificar_nota_colegio


class TestClasificarNotaColegio(unittest.TestCase):
    def test_excelente(self):
        self.assertEqual(clasificar_nota_colegio(5.0), "Excelente")
        self.assertEqual(clasificar_nota_colegio(4.7), "Excelente")
        self.assertEqual(clasificar_nota_colegio(4.5), "Excelente")

    def test_muy_bueno(self):
        self.assertEqual(clasificar_nota_colegio(4.4), "Muy bueno")
        self.assertEqual(clasificar_nota_colegio(4.2), "Muy bueno")
        self.assertEqual(clasificar_nota_colegio(4.0), "Muy bueno")

    def test_bueno(self):
        self.assertEqual(clasificar_nota_colegio(3.9), "Bueno")
        self.assertEqual(clasificar_nota_colegio(3.7), "Bueno")
        self.assertEqual(clasificar_nota_colegio(3.5), "Bueno")

    def test_minimo_aprobatorio(self):
        self.assertEqual(clasificar_nota_colegio(3.4), "Mínimo aprobatorio")
        self.assertEqual(clasificar_nota_colegio(3.2), "Mínimo aprobatorio")
        self.assertEqual(clasificar_nota_colegio(3.0), "Mínimo aprobatorio")

    def test_reprobado(self):
        self.assertEqual(clasificar_nota_colegio(2.9), "Reprobado")
        self.assertEqual(clasificar_nota_colegio(1.0), "Reprobado")

    def test_fuera_de_rango_alto(self):
        with self.assertRaises(ValueError):
            clasificar_nota_colegio(5.1)

    def test_fuera_de_rango_bajo(self):
        with self.assertRaises(ValueError):
            clasificar_nota_colegio(0.5)
        with self.assertRaises(ValueError):
            clasificar_nota_colegio(-1.0)


if __name__ == "__main__":
    unittest.main()
