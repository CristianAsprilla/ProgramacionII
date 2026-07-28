import unittest
from main import (
    agregar_producto,
    inventario,
    listar_inventario,
    stock_actual,
    vender,
)


def reiniciar_inventario():
    inventario.clear()


class PruebasInventario(unittest.TestCase):
    def setUp(self):
        reiniciar_inventario()

    def test_agregar_y_stock(self):
        agregar_producto("Cuaderno", 2.50, 30)
        self.assertEqual(stock_actual("Cuaderno"), 30)
        self.assertEqual(len(inventario), 1)

    def test_agregar_duplicado_actualiza(self):
        agregar_producto("Cuaderno", 2.50, 30)
        agregar_producto("Cuaderno", 2.75, 50)
        self.assertEqual(len(inventario), 1)
        self.assertEqual(stock_actual("Cuaderno"), 50)
        self.assertEqual(inventario[0]["precio"], 2.75)

    def test_vender_ok(self):
        agregar_producto("Lápiz", 0.50, 100)
        self.assertTrue(vender("Lápiz", 10))
        self.assertEqual(stock_actual("Lápiz"), 90)

    def test_vender_sin_stock(self):
        agregar_producto("Goma", 0.75, 5)
        self.assertFalse(vender("Goma", 10))
        self.assertEqual(stock_actual("Goma"), 5)

    def test_vender_inexistente(self):
        self.assertFalse(vender("Nada", 1))

    def test_stock_inexistente(self):
        self.assertIsNone(stock_actual("Nada"))

    def test_listar_devuelve_copia(self):
        agregar_producto("Regla", 1.00, 20)
        listado = listar_inventario()
        listado.clear()
        self.assertEqual(len(inventario), 1)