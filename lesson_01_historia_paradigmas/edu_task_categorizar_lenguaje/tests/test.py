import unittest
from main import categoria_por_ano


class TestCategoriaPorAno(unittest.TestCase):

    def test_antiguo_antes_de_1990(self):
        self.assertEqual(categoria_por_ano(1958), "antiguo")
        self.assertEqual(categoria_por_ano(1972), "antiguo")
        self.assertEqual(categoria_por_ano(1989), "antiguo")

    def test_moderno_entre_1990_y_2010(self):
        self.assertEqual(categoria_por_ano(1990), "moderno")
        self.assertEqual(categoria_por_ano(2000), "moderno")
        self.assertEqual(categoria_por_ano(2010), "moderno")

    def test_reciente_despues_de_2010(self):
        self.assertEqual(categoria_por_ano(2011), "reciente")
        self.assertEqual(categoria_por_ano(2020), "reciente")

    def test_limite_inferior_1990_es_moderno(self):
        # 1990 inclusive va a moderno
        self.assertEqual(categoria_por_ano(1990), "moderno")

    def test_limite_superior_2010_es_moderno(self):
        # 2010 inclusive va a moderno, recien 2011 es reciente
        self.assertEqual(categoria_por_ano(2010), "moderno")