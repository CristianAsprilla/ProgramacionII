import unittest
import os
import tempfile
from main import guardar_notas, cargar_notas


class TestPersistencia(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt")
        self.tmp.close()
        self.ruta = self.tmp.name

    def tearDown(self):
        if os.path.exists(self.ruta):
            os.unlink(self.ruta)

    def test_guardar_y_cargar(self):
        notas = [4.5, 3.8, 5.0, 2.5]
        guardar_notas(notas, self.ruta)
        resultado = cargar_notas(self.ruta)
        self.assertEqual(resultado, notas)

    def test_archivo_vacio(self):
        guardar_notas([], self.ruta)
        resultado = cargar_notas(self.ruta)
        self.assertEqual(resultado, [])

    def test_cargar_archivo_no_existe(self):
        resultado = cargar_notas("/tmp/no_existe_archivo_xyz.txt")
        self.assertEqual(resultado, [])
