import unittest
from main import ordenar_por_precio, producto_mas_caro, producto_mas_barato


class TestOrdenar(unittest.TestCase):

    def test_ordenar_ascendente(self):
        resultado = ordenar_por_precio({"A": 3, "B": 1, "C": 2})
        self.assertEqual(resultado, [("B", 1), ("C", 2), ("A", 3)])

    def test_ordenar_descendente(self):
        resultado = ordenar_por_precio({"A": 3, "B": 1, "C": 2}, descendente=True)
        self.assertEqual(resultado, [("A", 3), ("C", 2), ("B", 1)])

    def test_mas_caro(self):
        catalogo = {"A": 1, "B": 5, "C": 3}
        self.assertEqual(producto_mas_caro(catalogo), "B")

    def test_mas_caro_vacio(self):
        self.assertIsNone(producto_mas_caro({}))

    def test_mas_barato(self):
        catalogo = {"A": 1, "B": 5, "C": 3}
        self.assertEqual(producto_mas_barato(catalogo), "A")

    def test_mas_barato_vacio(self):
        self.assertIsNone(producto_mas_barato({}))
