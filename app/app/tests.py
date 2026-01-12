"""
Sample tests for app
"""

from django.test import SimpleTestCase
from . import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding two numbers together"""
        res = calc.add(5, 6)

        return self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting two numbers"""
        res = calc.subtract(10, 5)

        return self.assertEqual(res, 5)


"""
this is simple test case
where we are testing our calc module
we are using SimpleTestCase
which dont require database
assertEqual is used to check if the result is equal to the expected value

"""
