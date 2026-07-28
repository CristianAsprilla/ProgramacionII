import unittest
from main import invertir_lista


class TestInvertirLista(unittest.TestCase):

    def test_lista_normal(self):
        self.assertEqual(invertir_lista([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_lista_vacia(self):
        self.assertEqual(invertir_lista([]), [])

    def test_un_elemento(self):
        self.assertEqual(invertir_lista([5]), [5])

    def test_strings(self):
        self.assertEqual(invertir_lista(["a", "b", "c"]), ["c", "b", "a"])

    def test_no_modifica_original(self):
        original = [1, 2, 3]
        invertir_lista(original)
        self.assertEqual(original, [1, 2, 3])

    def test_no_usa_reverse(self):
        # Verifica que el codigo no use reverse() ni reversed()
        import pathlib
        source = pathlib.Path(__file__).parent.joinpath("main.py").read_text()
        self.assertNotIn(".reverse()", source.replace(" ", ""))
        self.assertNotIn("reversed(", source)