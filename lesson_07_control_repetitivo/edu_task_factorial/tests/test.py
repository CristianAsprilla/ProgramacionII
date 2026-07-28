import unittest
from main import factorial_iterativo


class TestFactorialIterativo(unittest.TestCase):
    def test_casos_base(self):
        self.assertEqual(factorial_iterativo(0), 1)
        self.assertEqual(factorial_iterativo(1), 1)

    def test_valores_intermedios(self):
        self.assertEqual(factorial_iterativo(5), 120)
        self.assertEqual(factorial_iterativo(6), 720)
        self.assertEqual(factorial_iterativo(10), 3628800)

    def test_negativo(self):
        with self.assertRaises(ValueError):
            factorial_iterativo(-1)
        with self.assertRaises(ValueError):
            factorial_iterativo(-100)


if __name__ == "__main__":
    unittest.main()