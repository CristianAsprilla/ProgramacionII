import unittest
from main import factorial
class TestFactorial(unittest.TestCase):
    def test_valores(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(8), 40320)
    def test_negativo(self):
        with self.assertRaises(ValueError): factorial(-2)
if __name__ == "__main__": unittest.main()
