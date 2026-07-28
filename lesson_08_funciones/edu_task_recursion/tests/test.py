import unittest
from main import fibonacci_recursivo


class TestFibonacciRecursivo(unittest.TestCase):
    def test_casos_base(self):
        self.assertEqual(fibonacci_recursivo(0), 0)
        self.assertEqual(fibonacci_recursivo(1), 1)

    def test_valores_intermedios(self):
        self.assertEqual(fibonacci_recursivo(2), 1)
        self.assertEqual(fibonacci_recursivo(3), 2)
        self.assertEqual(fibonacci_recursivo(5), 5)
        self.assertEqual(fibonacci_recursivo(10), 55)

    def test_negativo(self):
        with self.assertRaises(ValueError):
            fibonacci_recursivo(-1)


if __name__ == "__main__":
    unittest.main()