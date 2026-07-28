import unittest
from main import main


class TestMain(unittest.TestCase):

    def test_main_es_llamable(self):
        self.assertTrue(callable(main))
