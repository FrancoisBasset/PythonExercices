import unittest
from basic1.utils import get_python_version

class TestExo2(unittest.TestCase):
    def setUp(self):
        self.version = get_python_version()

    def test_is_instance_of_str(self):
        self.assertIsInstance(self.version, str)

    def test_contains_dot(self):
        self.assertIn(".", self.version)

    def test_equals_3_11_3(self):
        self.assertEqual(self.version, "3.11.3")
