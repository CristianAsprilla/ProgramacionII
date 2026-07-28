import unittest
from main import contar_lineas_codigo


class TestContarLineas(unittest.TestCase):
    def test_solo_codigo(self):
        texto = "a = 1\nb = 2\nprint(a + b)\n"
        self.assertEqual(contar_lineas_codigo(texto), 3)

    def test_con_comentarios(self):
        texto = "a = 1\n# comentario\nb = 2\n"
        self.assertEqual(contar_lineas_codigo(texto), 2)

    def test_solo_comentarios_y_vacias(self):
        texto = "# solo comentario\n\n   # otro comentario\n"
        self.assertEqual(contar_lineas_codigo(texto), 0)

    def test_indentacion_antes_de_comentario(self):
        texto = "def f():\n    # comentario indentado\n    return 1\n"
        # la línea con '#' está indentada pero sigue siendo comentario
        self.assertEqual(contar_lineas_codigo(texto), 2)

    def test_codigo_con_comentario_inline(self):
        texto = "x = 5  # variable inicial\nx += 1\n"
        # las líneas con comentario inline después del código cuentan como código
        self.assertEqual(contar_lineas_codigo(texto), 2)

    def test_texto_vacio(self):
        self.assertEqual(contar_lineas_codigo(""), 0)
        self.assertEqual(contar_lineas_codigo("\n\n\n"), 0)


if __name__ == "__main__":
    unittest.main()