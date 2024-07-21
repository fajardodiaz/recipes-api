"""
Sample tests
"""
from django.test import SimpleTestCase

from . import  calc

class CalcTests(SimpleTestCase):
    """
    Test the calc module
    """

    def test_add(self):
        res = calc.add(1,2)
        self.assertEqual(res, 3)

    def test_subtract(self):
        res = calc.subtract(1,2)
        self.assertEqual(res, -1)