"""
What? Simple example on how to run unittest in python

The crux of each test is a call to assertEqual() to check for an expected result;
    - assertTrue() or assertFalse() to verify a condition;
    - assertRaises() to verify that a specific exception gets raised.


These methods are used instead of the assert statement so the test runner can
accumulate all test results and produce a report.

How to run:
===========
Option #1) python example_1.py
Option #2) python example_1.py -v -> enable a higher level of verbosity

References: https://docs.python.org/3/library/unittest.html
"""


import unittest


class TestStringMethods(unittest.TestCase):
    """
    A testcase is created by subclassing unittest.TestCase.
    Essentialy the class TestStringMethod inherits from the
    TestCase class.

    All the following methods start with a "test".
    This naming convention informs the test runner about which
    methods represent tests.
    """

    def test_upper(self):
        """
        Test if method upper() works correctly.
        """
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        """
        Test if a string has all letters in capital
        """
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        """
        Check if the split method fails when the separator
        is not a string. Here we'll use 2 which is an integer
        """
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])

        """
        The line below would check that s.split fails when
        the separator is not a string
        """
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
