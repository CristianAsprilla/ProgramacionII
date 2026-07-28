import unittest
from main import valor_total_catalogo, precio_promedio, cantidad_productos, resumen_catalogo


class TestEstadisticas(unittest.TestCase):

    def test_valor_total(self):
        self.assertEqual(valor_total_catalogo({"A": 1, "B": 2, "C": 3}), 6)

    def test_valor_total_vacio(self):
        self.assertEqual(valor_total_catalogo({}), 0)

    def test_promedio(self):
        self.assertEqual(precio_promedio({"A": 1, "B": 2, "C": 3}), 2)

    def test_promedio_vacio(self):
        self.assertEqual(precio_promedio({}), 0)

    def test_cantidad(self):
        self.assertEqual(cantidad_productos({"A": 1, "B": 2}), 2)

    def test_cantidad_vacio(self):
        self.assertEqual(cantidad_productos({}), 0)

    def test_resumen_keys(self):
        resumen = resumen_catalogo({"A": 1, "B": 2})
        for k in ["cantidad", "valor_total", "precio_promedio", "mas_caro", "mas_barato"]:
            self.assertIn(k, resumen)

    def test_resumen_valores(self):
        resumen = resumen_catalogo({"A": 1, "B": 2, "C": 3})
        self.assertEqual(resumen["cantidad"], 3)
        self.assertEqual(resumen["valor_total"], 6)
        self.assertEqual(resumen["precio_promedio"], 2)
        self.assertEqual(resumen["mas_caro"], "C")
        self.assertEqual(resumen["mas_barato"], "A")
