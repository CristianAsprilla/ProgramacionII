import unittest
from main import extension


class TestExtension(unittest.TestCase):

    def test_extension_simple(self):
        self.assertEqual(extension("documento.pdf"), "pdf")

    def test_extension_python(self):
        self.assertEqual(extension("script.py"), "py")

    def test_extension_csv(self):
        self.assertEqual(extension("datos.csv"), "csv")

    def test_sin_extension_retorna_vacio(self):
        self.assertEqual(extension("README"), "")

    def test_extension_con_mayusculas(self):
        # Case-sensitive: preservamos las mayusculas
        self.assertEqual(extension("foto.PNG"), "PNG")

    def test_archivo_con_punto_al_final_no_tiene_extension(self):
        # 'archivo.' no tiene extension
        self.assertEqual(extension("archivo."), "")

    def test_multiples_puntos_usa_el_ultimo(self):
        # 'datos.backup.tar.gz' -> 'gz'
        self.assertEqual(extension("datos.backup.tar.gz"), "gz")