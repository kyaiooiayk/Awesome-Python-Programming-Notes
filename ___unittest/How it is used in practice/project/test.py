"""
There are many behaviors in sum() you could check, such as:

    Can it sum a list of whole numbers (integers)?
    Can it sum a tuple or set?
    Can it sum a list of floats?
    What happens when you provide it with a bad value, such as a single integer or a string?
    What happens when one of the values is negative?

Reference: https://realpython.com/python-testing/
"""

import unittest
from fractions import Fraction


# my_sum here represents the package
# essentially the folder
from my_sum import sum


class TestSum(unittest.TestCase):
    
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        # Assertition = validates the output against a known response.
        self.assertEqual(result, 6)
        
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        This is just an example to show what will happens if
        the test fails.
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)
        
    def test_bad_type(self):
        """
        This test case will now only pass if sum(data) raises a TypeError. 
        You can replace TypeError with any exception type you choose.
        """
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)


if __name__ == '__main__':
    unittest.main()
