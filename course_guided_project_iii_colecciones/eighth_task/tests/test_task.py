import unittest
from main import productos_sin_stock, productos_stock_bajo, alerta_reabastecimiento


class TestAlertas(unittest.TestCase):

    def test_sin_stock(self):
        stock = {"A": 0, "B": 5, "C": -1, "D": 10}
        resultado = productos_sin_stock(stock)
        self.assertEqual(set(resultado), {"A", "C"})

    def test_sin_stock_vacio(self):
        self.assertEqual(productos_sin_stock({}), [])

    def test_stock_bajo(self):
        stock = {"A": 3, "B": 10, "C": 4, "D": 100}
        resultado = productos_stock_bajo(stock, minimo=5)
        self.assertEqual(set(resultado), {("A", 3), ("C", 4)})

    def test_stock_bajo_minimo_custom(self):
        stock = {"A": 3, "B": 10, "C": 8}
        resultado = productos_stock_bajo(stock, minimo=9)
        self.assertEqual(set(resultado), {("A", 3), ("C", 8)})

    def test_alerta_sin_problemas(self):
        self.assertEqual(alerta_reabastecimiento({"A": 100}), "Todo en orden")

    def test_alerta_con_problemas(self):
        stock = {"A": 2, "B": 100}
        mensaje = alerta_reabastecimiento(stock, minimo=5)
        self.assertIn("A", mensaje)
        self.assertNotIn("B", mensaje)
