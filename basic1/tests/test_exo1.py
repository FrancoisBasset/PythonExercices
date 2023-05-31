import unittest
from basic1.utils import get_twinkle_text

class TestExo1(unittest.TestCase):
    def setUp(self):
        self.text = get_twinkle_text()

    def test_is_instance(self):
        self.assertIsInstance(self.text, str)

    def test_is_greater(self):
        self.assertGreater(len(self.text), 0)

    def test_equals_6_lines(self):
        self.assertEqual(self.text.count("\n"), 5)
