import unittest
import math
from basic1.utils import get_circle_area

class TestExo4(unittest.TestCase):
    def test_correct_results(self):
        results = [
            (1.1, 3.8013271108436504),
            (1, 3.141592653589793),
            (1, math.pi),
            (2, 12.566370614359172)
        ]

        for n, result in results:
            self.assertEqual(get_circle_area(n), result)
