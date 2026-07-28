import unittest
from main import directorio_programa


class TestDirectorioPrograma(unittest.TestCase):

    def test_retorna_un_diccionario(self):
        resultado = directorio_programa()
        self.assertIsInstance(resultado, dict, msg="Debe devolver un dict")

    def test_tiene_clave_carrera(self):
        resultado = directorio_programa()
        self.assertIn("carrera", resultado, msg="Debe tener la clave 'carrera'")

    def test_tiene_clave_instituto(self):
        resultado = directorio_programa()
        self.assertIn("instituto", resultado, msg="Debe tener la clave 'instituto'")

    def test_tiene_clave_modalidad(self):
        resultado = directorio_programa()
        self.assertIn("modalidad", resultado, msg="Debe tener la clave 'modalidad'")

    def test_tiene_clave_duracion(self):
        resultado = directorio_programa()
        self.assertIn("duracion", resultado, msg="Debe tener la clave 'duracion'")

    def test_diccionario_no_vacio(self):
        resultado = directorio_programa()
        self.assertGreater(len(resultado), 0, msg="El diccionario no debe estar vacio")