import unittest
from main import (
    agregar_producto,
    buscar_producto,
    eliminar_producto,
    listar_productos,
)


class PruebasListaCompras(unittest.TestCase):
    def test_agregar_y_listar(self):
        compras = []
        agregar_producto(compras, "arroz")
        agregar_producto(compras, "plátano")
        self.assertEqual(compras, ["arroz", "plátano"])
        self.assertEqual(listar_productos(compras), ["arroz", "plátano"])

    def test_buscar_producto(self):
        compras = ["arroz", "leche"]
        self.assertTrue(buscar_producto(compras, "leche"))
        self.assertFalse(buscar_producto(compras, "café"))

    def test_eliminar_producto(self):
        compras = ["arroz", "leche", "arroz"]
        self.assertTrue(eliminar_producto(compras, "arroz"))
        self.assertEqual(compras, ["leche", "arroz"])
        self.assertFalse(eliminar_producto(compras, "sal"))
        self.assertEqual(compras, ["leche", "arroz"])

    def test_listar_devuelve_una_copia(self):
        compras = ["pan"]
        listado = listar_productos(compras)
        listado.append("queso")
        self.assertEqual(compras, ["pan"])
