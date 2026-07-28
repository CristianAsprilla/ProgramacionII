import unittest
from main import es_version_compatible


class TestEsVersionCompatible(unittest.TestCase):

    def test_python_3_10_es_compatible(self):
        self.assertTrue(es_version_compatible((3, 10, 0)))

    def test_python_3_11_es_compatible(self):
        self.assertTrue(es_version_compatible((3, 11, 5)))

    def test_python_3_12_es_compatible(self):
        self.assertTrue(es_version_compatible((3, 12, 1)))

    def test_python_3_9_no_es_compatible(self):
        self.assertFalse(es_version_compatible((3, 9, 9)))

    def test_python_2_7_no_es_compatible(self):
        self.assertFalse(es_version_compatible((2, 7, 18)))

    def test_python_3_8_no_es_compatible(self):
        self.assertFalse(es_version_compatible((3, 8, 10)))