import unittest
from main import ventas_por_mes, mejor_dia, promedio_diario


class TestReporte(unittest.TestCase):

    def test_ventas_por_mes(self):
        matriz = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        self.assertEqual(ventas_por_mes(matriz), [120, 150, 180])

    def test_ventas_por_mes_4x3(self):
        matriz = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]]
        self.assertEqual(ventas_por_mes(matriz), [220, 260, 300])

    def test_mejor_dia(self):
        matriz = [[10, 20], [100, 50], [30, 40]]
        self.assertEqual(mejor_dia(matriz), 1)

    def test_mejor_dia_empate_primero(self):
        matriz = [[50, 50], [50, 50]]
        self.assertEqual(mejor_dia(matriz), 0)

    def test_mejor_dia_vacio(self):
        self.assertEqual(mejor_dia([]), -1)

    def test_promedio_diario(self):
        matriz = [[10, 20], [30, 40]]
        # promedio diario = promedio de los promedios de cada dia = (15 + 35) / 2 = 25
        self.assertEqual(promedio_diario(matriz), 25.0)

    def test_promedio_diario_vacio(self):
        self.assertEqual(promedio_diario([]), 0.0)
