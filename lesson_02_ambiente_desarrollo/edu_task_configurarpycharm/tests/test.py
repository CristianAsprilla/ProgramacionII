import unittest

from main import validar_version_python


class TestValidarVersionPython(unittest.TestCase):

    def test_python_3_10_y_posteriores_son_compatibles(self):
        self.assertTrue(validar_version_python((3, 10, 0)))
        self.assertTrue(validar_version_python((3, 12, 4)))

    def test_python_3_9_no_es_compatible(self):
        self.assertFalse(validar_version_python((3, 9, 9)))

    def test_python_2_7_no_es_compatible(self):
        self.assertFalse(validar_version_python((2, 7, 18)))


if __name__ == "__main__":
    unittest.main()
