import unittest
from main import factorial_modular


class TestFactorialModular(unittest.TestCase):

    def test_cero(self):
        self.assertEqual(factorial_modular(0), 1)

    def test_uno(self):
        self.assertEqual(factorial_modular(1), 1)

    def test_dos(self):
        self.assertEqual(factorial_modular(2), 2)

    def test_tres(self):
        self.assertEqual(factorial_modular(3), 6)

    def test_cinco(self):
        self.assertEqual(factorial_modular(5), 120)

    def test_diez(self):
        self.assertEqual(factorial_modular(10), 3628800)