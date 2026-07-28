import unittest
from main import (
    registrar_venta, generar_reporte, ejecutar_opcion,
)


class TestRegistrarVenta(unittest.TestCase):

    def test_registrar_venta_trim1(self):
        ventas = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        registrar_venta(ventas, 0, 1, 5)
        self.assertEqual(ventas[0][0], 5)
        # El total (fila 3) también debe haberse incrementado
        self.assertEqual(ventas[3][0], 5)

    def test_registrar_venta_trim2(self):
        ventas = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        registrar_venta(ventas, 1, 2, 10)
        self.assertEqual(ventas[1][1], 10)
        self.assertEqual(ventas[3][1], 10)

    def test_registrar_venta_acumula(self):
        ventas = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        registrar_venta(ventas, 0, 1, 3)
        registrar_venta(ventas, 0, 1, 7)
        self.assertEqual(ventas[0][0], 10)
        self.assertEqual(ventas[3][0], 10)


class TestGenerarReporte(unittest.TestCase):

    def test_reporte_no_vacio_con_datos(self):
        ventas = [[5, 0, 0], [3, 0, 0], [2, 0, 0], [10, 0, 0]]
        catalogo = {"Cuaderno": {"precio": 2.5, "stock": 20}}
        reporte = generar_reporte(ventas, catalogo)
        self.assertIsInstance(reporte, str)
        self.assertTrue(len(reporte) > 0)
        self.assertIn("10", reporte, msg="El reporte debe mostrar el total 10")


class TestEjecutarOpcion(unittest.TestCase):

    def test_opcion_salir_devuelve_false(self):
        self.assertFalse(ejecutar_opcion("6"))

    def test_opcion_invalida_no_termina(self):
        self.assertNotEqual(ejecutar_opcion("99"), False)
