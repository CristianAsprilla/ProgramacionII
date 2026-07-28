import unittest
from main import calcular_promedio, nota_maxima, nota_minima


class TestCalcularPromedio(unittest.TestCase):

    def test_promedio_lista_vacia(self):
        self.assertIsNone(calcular_promedio([]),
                          msg="Lista vacía debe devolver None")

    def test_promedio_un_solo_elemento(self):
        self.assertEqual(calcular_promedio([85]), 85)

    def test_promedio_varios(self):
        self.assertEqual(calcular_promedio([80, 90, 100]), 90.0)

    def test_promedio_decimales(self):
        resultado = calcular_promedio([85, 92])
        self.assertIsNotNone(resultado)
        self.assertAlmostEqual(resultado, 88.5)


class TestNotaMaxima(unittest.TestCase):

    def test_maxima_lista_vacia(self):
        self.assertIsNone(nota_maxima([]))

    def test_maxima_un_solo_elemento(self):
        self.assertEqual(nota_maxima([85]), 85)

    def test_maxima_varios(self):
        self.assertEqual(nota_maxima([80, 90, 100, 95]), 100)


class TestNotaMinima(unittest.TestCase):

    def test_minima_lista_vacia(self):
        self.assertIsNone(nota_minima([]))

    def test_minima_un_solo_elemento(self):
        self.assertEqual(nota_minima([85]), 85)

    def test_minima_varios(self):
        self.assertEqual(nota_minima([80, 90, 100, 95]), 80)
