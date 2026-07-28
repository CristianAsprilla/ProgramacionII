import unittest
from main import registrar_operacion, ver_historial


class TestRegistrarOperacion(unittest.TestCase):

    def test_agrega_una_operacion(self):
        historial = []
        registrar_operacion(historial, "agregar", {"nombre": "Cuaderno"})
        self.assertEqual(len(historial), 1)
        self.assertEqual(historial[0]["tipo"], "agregar")
        self.assertEqual(historial[0]["detalles"]["nombre"], "Cuaderno")

    def test_multiples_operaciones(self):
        historial = []
        registrar_operacion(historial, "agregar", {"nombre": "A"})
        registrar_operacion(historial, "actualizar", {"nombre": "B", "delta": 5})
        self.assertEqual(len(historial), 2)
        self.assertEqual(historial[1]["tipo"], "actualizar")


class TestVerHistorial(unittest.TestCase):

    def test_historial_vacio(self):
        resultado = ver_historial([])
        self.assertIn("no", resultado.lower())

    def test_historial_con_operaciones(self):
        historial = [
            {"tipo": "agregar", "detalles": {"nombre": "Cuaderno"}},
            {"tipo": "actualizar", "detalles": {"nombre": "Lapiz", "delta": -3}},
        ]
        resultado = ver_historial(historial)
        self.assertIn("Cuaderno", resultado)
        self.assertIn("Lapiz", resultado)
        self.assertIn("agregar", resultado.lower())
        self.assertIn("actualizar", resultado.lower())
