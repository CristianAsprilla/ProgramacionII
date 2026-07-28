import unittest
from main import fibonacci
class TestFibonacci(unittest.TestCase):
    def test_series(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])
    def test_negativo(self):
        with self.assertRaises(ValueError): fibonacci(-1)
if __name__ == "__main__": unittest.main()
