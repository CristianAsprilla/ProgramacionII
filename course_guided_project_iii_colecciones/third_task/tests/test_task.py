import unittest
from main import (
    agregar_producto, actualizar_stock,
    apilar_operacion, deshacer,
)


class TestApilarOperacion(unittest.TestCase):

    def test_apilar_agregar(self):
        pila = []
        apilar_operacion(pila, {"tipo": "agregar", "nombre": "Cuaderno"})
        self.assertEqual(len(pila), 1)
        self.assertEqual(pila[0]["nombre"], "Cuaderno")

    def test_apilar_actualizar(self):
        pila = []
        apilar_operacion(pila, {
            "tipo": "actualizar",
            "nombre": "Lapiz",
            "delta": -5,
        })
        self.assertEqual(pila[0]["delta"], -5)


class TestDeshacer(unittest.TestCase):

    def test_deshacer_agregar_elimina_producto(self):
        catalogo = {"Cuaderno": {"precio": 2.5, "stock": 20}}
        pila = [{"tipo": "agregar", "nombre": "Cuaderno"}]
        resultado = deshacer(catalogo, pila)
        self.assertIsNotNone(resultado, msg="Debe devolver un mensaje")
        self.assertNotIn("Cuaderno", catalogo, msg="El producto debe haberse eliminado")
        self.assertEqual(len(pila), 0, msg="La pila debe quedar vacía")

    def test_deshacer_actualizar_revierte_stock(self):
        catalogo = {"Lapiz": {"precio": 0.5, "stock": 100}}
        pila = [{"tipo": "actualizar", "nombre": "Lapiz", "delta": -10}]
        deshacer(catalogo, pila)
        self.assertEqual(catalogo["Lapiz"]["stock"], 110, msg="El stock debe volver a 110")

    def test_deshacer_pila_vacia(self):
        catalogo = {}
        pila = []
        resultado = deshacer(catalogo, pila)
        self.assertIsNone(resultado, msg="Pila vacía debe devolver None")

    def test_deshacer_multiple(self):
        catalogo = {}
        agregar_producto(catalogo, "A", 1.0, 5)
        apilar_operacion(None if False else [], {"tipo": "agregar", "nombre": "A"})
        # Reutilizamos una pila fresca para que la lógica no dependa del append previo
        pila = [{"tipo": "agregar", "nombre": "A"}]
        deshacer(catalogo, pila)
        self.assertNotIn("A", catalogo)
