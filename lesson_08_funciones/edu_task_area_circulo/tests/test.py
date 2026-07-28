import unittest
from main import area_circulo


class TestAreaCirculo(unittest.TestCase):

    def test_radio_1(self):
        self.assertAlmostEqual(area_circulo(1), 3.14159, places=4)

    def test_radio_2(self):
        # area = pi * 4 = 12.56636
        self.assertAlmostEqual(area_circulo(2), 12.56636, places=4)

    def test_radio_0(self):
        self.assertEqual(area_circulo(0), 0.0)

    def test_radio_5(self):
        # area = pi * 25 = 78.5398
        self.assertAlmostEqual(area_circulo(5), 78.5398, places=3)

    def test_retorna_numero(self):
        self.assertIsInstance(area_circulo(3), float)