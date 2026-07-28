import unittest
from main import agregar_producto, buscar_producto, actualizar_stock


class TestAgregarProducto(unittest.TestCase):

    def setUp(self):
        self.catalogo = {}

    def test_agregar_producto_nuevo(self):
        resultado = agregar_producto(self.catalogo, "Cuaderno", 2.5, 20)
        self.assertTrue(resultado)
        self.assertIn("Cuaderno", self.catalogo)
        self.assertEqual(self.catalogo["Cuaderno"]["precio"], 2.5)
        self.assertEqual(self.catalogo["Cuaderno"]["stock"], 20)

    def test_agregar_producto_duplicado(self):
        agregar_producto(self.catalogo, "Cuaderno", 2.5, 20)
        resultado = agregar_producto(self.catalogo, "Cuaderno", 3.0, 10)
        self.assertFalse(resultado, msg="Producto duplicado debe devolver False")
        # El producto original debe quedar igual
        self.assertEqual(self.catalogo["Cuaderno"]["precio"], 2.5)
        self.assertEqual(self.catalogo["Cuaderno"]["stock"], 20)


class TestBuscarProducto(unittest.TestCase):

    def setUp(self):
        self.catalogo = {"Cuaderno": {"precio": 2.5, "stock": 20}}

    def test_buscar_existente(self):
        resultado = buscar_producto(self.catalogo, "Cuaderno")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["precio"], 2.5)

    def test_buscar_inexistente(self):
        resultado = buscar_producto(self.catalogo, "Lapiz")
        self.assertIsNone(resultado)


class TestActualizarStock(unittest.TestCase):

    def setUp(self):
        self.catalogo = {"Cuaderno": {"precio": 2.5, "stock": 20}}

    def test_sumar_stock(self):
        self.assertTrue(actualizar_stock(self.catalogo, "Cuaderno", 5))
        self.assertEqual(self.catalogo["Cuaderno"]["stock"], 25)

    def test_restar_stock(self):
        self.assertTrue(actualizar_stock(self.catalogo, "Cuaderno", -3))
        self.assertEqual(self.catalogo["Cuaderno"]["stock"], 17)

    def test_producto_inexistente(self):
        self.assertFalse(actualizar_stock(self.catalogo, "Lapiz", 5))
