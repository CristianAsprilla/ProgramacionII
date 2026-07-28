import unittest
from main import es_primo


class TestEsPrimo(unittest.TestCase):

    def test_dos_es_primo(self):
        self.assertTrue(es_primo(2))

    def test_tres_es_primo(self):
        self.assertTrue(es_primo(3))

    def test_siete_es_primo(self):
        self.assertTrue(es_primo(7))

    def test_diez_no_es_primo(self):
        self.assertFalse(es_primo(10))

    def test_uno_no_es_primo(self):
        self.assertFalse(es_primo(1))

    def test_cero_no_es_primo(self):
        self.assertFalse(es_primo(0))

    def test_cuatro_no_es_primo(self):
        self.assertFalse(es_primo(4))

    def test_trece_es_primo(self):
        self.assertTrue(es_primo(13))