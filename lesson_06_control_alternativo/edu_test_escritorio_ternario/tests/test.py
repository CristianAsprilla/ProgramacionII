import unittest
from main import evaluar_ternario


class TestEvaluarTernario(unittest.TestCase):

    def test_condicion_true(self):
        self.assertEqual(evaluar_ternario(True, "mayor", "menor"), "mayor")

    def test_condicion_false(self):
        self.assertEqual(evaluar_ternario(False, "mayor", "menor"), "menor")

    def test_con_expresion(self):
        self.assertEqual(evaluar_ternario(5 > 3, "A", "B"), "A")
        self.assertEqual(evaluar_ternario(5 < 3, "A", "B"), "B")

    def test_con_numeros(self):
        self.assertEqual(evaluar_ternario(True, 1, 0), 1)
        self.assertEqual(evaluar_ternario(False, 1, 0), 0)

    def test_con_strings(self):
        self.assertEqual(evaluar_ternario(10 == 10, "igual", "diferente"), "igual")