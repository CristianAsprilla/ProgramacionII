import unittest
from main import (
    agregar_contacto,
    buscar_contacto,
    eliminar_contacto,
    listar_contactos,
)


class PruebasAgenda(unittest.TestCase):
    def test_agregar_y_buscar(self):
        agenda = {}
        agregar_contacto(agenda, "Ana", "6000-1234")
        self.assertEqual(buscar_contacto(agenda, "Ana"), "6000-1234")
        self.assertIsNone(buscar_contacto(agenda, "Carlos"))

    def test_actualizar_contacto(self):
        agenda = {"Ana": "6000-1234"}
        agregar_contacto(agenda, "Ana", "6999-0000")
        self.assertEqual(agenda["Ana"], "6999-0000")

    def test_eliminar_contacto(self):
        agenda = {"Ana": "6000-1234"}
        self.assertTrue(eliminar_contacto(agenda, "Ana"))
        self.assertEqual(agenda, {})
        self.assertFalse(eliminar_contacto(agenda, "Ana"))

    def test_listar_ordenado(self):
        agenda = {"Luis": "6000-5678", "Ana": "6000-1234"}
        self.assertEqual(
            listar_contactos(agenda),
            [("Ana", "6000-1234"), ("Luis", "6000-5678")],
        )
