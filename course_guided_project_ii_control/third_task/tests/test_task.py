import unittest
from main import (
    agregar_nota, listar_notas, calcular_promedio,
    nota_maxima, nota_minima, ejecutar_opcion
)


class TestIntegracion(unittest.TestCase):

    def test_agregar_y_listar(self):
        notas = []
        agregar_nota(notas, 80)
        agregar_nota(notas, 90)
        self.assertEqual(len(notas), 2)
        self.assertIn("80", listar_notas(notas))
        self.assertIn("90", listar_notas(notas))

    def test_promedio_con_agregadas(self):
        notas = []
        agregar_nota(notas, 100)
        agregar_nota(notas, 80)
        self.assertEqual(calcular_promedio(notas), 90.0)
        self.assertEqual(nota_maxima(notas), 100)
        self.assertEqual(nota_minima(notas), 80)


class TestEjecutarOpcion(unittest.TestCase):

    def test_opcion_salir_devuelve_false(self):
        # La opción 5 debe hacer que el programa termine.
        self.assertFalse(ejecutar_opcion("5", []))

    def test_opcion_invalida_no_termina(self):
        # Una opción inválida no debe hacer que el programa termine.
        self.assertNotEqual(ejecutar_opcion("99", []), False)
