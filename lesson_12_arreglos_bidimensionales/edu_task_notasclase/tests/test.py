import unittest
from main import promedio_estudiantes


class PruebasPromedioEstudiantes(unittest.TestCase):
    def test_matriz_de_ejemplo(self):
        matriz = [
            [4.5, 4.0, 4.8],
            [3.9, 4.2, 4.6],
            [5.0, 4.7, 4.9],
        ]
        resultado = promedio_estudiantes(matriz)
        self.assertEqual(len(resultado), 3)
        self.assertAlmostEqual(resultado[0], 4.4333, places=3)
        self.assertAlmostEqual(resultado[1], 4.2333, places=3)
        self.assertAlmostEqual(resultado[2], 4.8666, places=3)

    def test_un_solo_estudiante(self):
        self.assertAlmostEqual(promedio_estudiantes([[5.0, 4.0, 3.0]])[0], 4.0)

    def test_dos_estudiantes(self):
        matriz = [
            [3.0, 3.0, 3.0],
            [5.0, 5.0, 5.0],
        ]
        resultado = promedio_estudiantes(matriz)
        self.assertEqual(len(resultado), 2)
        self.assertAlmostEqual(resultado[0], 3.0)
        self.assertAlmostEqual(resultado[1], 5.0)