import unittest
from convert import str_to_float

class TestStrToFloat(unittest.TestCase):

    def test_valid_float_strings1(self):
        self.assertEqual(str_to_float("123.45"), 123.45)
    def test_valid_float_strings2(self):
        self.assertEqual(str_to_float("abc"), None)

