import unittest
from main import es_primo, lista_primos


class TestPrimos(unittest.TestCase):
    def test_es_primo_verdaderos(self):
        for n in (2, 3, 5, 7, 11, 13, 17, 19, 23):
            self.assertTrue(es_primo(n), f"se esperaba que {n} fuera primo")

    def test_es_primo_falsos(self):
        for n in (0, 1, 4, 6, 8, 9, 10, 12, 25):
            self.assertFalse(es_primo(n), f"se esperaba que {n} NO fuera primo")

    def test_lista_primos(self):
        self.assertEqual(lista_primos(1), [])
        self.assertEqual(lista_primos(2), [2])
        self.assertEqual(lista_primos(10), [2, 3, 5, 7])
        self.assertEqual(lista_primos(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


if __name__ == "__main__":
    unittest.main()