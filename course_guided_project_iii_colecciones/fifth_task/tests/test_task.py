import unittest
from main import buscar_producto, buscar_productos_por_precio


class TestBuscar(unittest.TestCase):

    def test_buscar_existe(self):
        catalogo = {"Cuaderno": 1.50, "Lapiz": 0.50}
        self.assertEqual(buscar_producto(catalogo, "Cuaderno"), 1.50)

    def test_buscar_no_existe(self):
        catalogo = {"Cuaderno": 1.50}
        self.assertIsNone(buscar_producto(catalogo, "Borrador"))

    def test_buscar_vacio(self):
        self.assertIsNone(buscar_producto({}, "Cualquiera"))

    def test_por_precio(self):
        catalogo = {"A": 1.0, "B": 2.0, "C": 0.5, "D": 3.0}
        resultado = buscar_productos_por_precio(catalogo, 1.0)
        self.assertEqual(set(resultado), {"A", "C"})
