import unittest
from main import clasificar_desempeno, resumen_desempeno


class TestClasificar(unittest.TestCase):

    def test_excelente(self):
        self.assertEqual(clasificar_desempeno(4.8), "Excelente")

    def test_muy_bueno(self):
        self.assertEqual(clasificar_desempeno(4.2), "Muy bueno")

    def test_bueno(self):
        self.assertEqual(clasificar_desempeno(3.7), "Bueno")

    def test_suficiente(self):
        self.assertEqual(clasificar_desempeno(3.2), "Suficiente")

    def test_insuficiente(self):
        self.assertEqual(clasificar_desempeno(2.5), "Insuficiente")

    def test_resumen_aprobado(self):
        resumen = resumen_desempeno([4, 4, 4])
        self.assertTrue(resumen["aprobado"])
        self.assertEqual(resumen["clasificacion"], "Muy bueno")

    def test_resumen_reprobado(self):
        resumen = resumen_desempeno([2, 2, 2])
        self.assertFalse(resumen["aprobado"])
        self.assertEqual(resumen["clasificacion"], "Insuficiente")

    def test_resumen_keys(self):
        resumen = resumen_desempeno([4, 5, 3])
        for k in ["promedio", "max", "min", "clasificacion", "aprobado"]:
            self.assertIn(k, resumen)
