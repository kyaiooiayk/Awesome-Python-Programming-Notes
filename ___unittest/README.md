# How to unittest your python code
***

## Why Unit Test your code?
- **Safe refactoring** When you add more and more features to a software, you sometimes need to change old design and code. However, changing already-tested code is both risky and costly. If we have unit tests in place, then we can proceed for refactoring confidently.
- **Better code quality** Writing tests before actual coding makes you think harder about the problem. It exposes the edge cases and makes you write better code. 
- **Finds Software Bugs Early** Issues are found at an early stage. Since unit testing is carried out by developers who test individual code before integration, issues can be found very early and can be resolved then and there without impacting the other pieces of the code. This includes both bugs in the programmer’s implementation and flaws or missing parts of the specification for the unit.
- **Facilitates Changes and Simplifies Integration** Unit testing allows the programmer to refactor code or upgrade system libraries at a later date and make sure the module still works correctly. Unit tests detect changes that may break a design contract. They help with maintaining and changing the code.
- **Provides Documentation** Unit testing provides documentation of the system. Developers looking to learn what functionality is provided by a unit and how to use it can look at the unit tests to gain a basic understanding of the unit’s interface (API).
- **Debugging Process** Unit testing helps simplify the debugging process. If a test fails, then only the latest changes made in the code need to be debugged.
- **Design** Writing the test first forces you to think through your design and what it must accomplish before you write the code. This not only keeps you focused; it makes you create better designs. Testing a piece of code forces you to define what that code is responsible for. If you can do this easily, that means the code’s responsibility is well-defined and therefore that it has high cohesion.
***

## General templates
- This is just a template with all the necessary imports, comments and some code to refresh someone's knowledge on unittesting. 
- A testcase is created by subclassing `unittest.TestCase`. Essentialy the class `TestSum` inherits from the `TestCase` class.
- All the following methods start with a `test_`. This naming convention informs the test runner about which methods represent a test.
- While unittesting it is acceptable to use long and descriptive names for testing function.

```
# some_name_test.py
import unittest

class TestSum(unittest.TestCase):

    def test_sum_list(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
```
```
# This an alternative way of testing the same
def test_sum_list():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    """
    Let's write an faulse statement.
    """
    assert sum((1, 2, 5)) == 5, "Should be 6"

if __name__ == "__main__":
    test_sum_list()
    test_sum_tuple()
    print("Everything passed")
```

- You have 4 options to run the test:
    - **Option #1**: `python some_name_test.py`
    - **Option #2**: `python -m unittest some_name_test`
    - **Option #3**: `python -m unittest -v some_name_test`
    - **Option #4**: `python -m unittest discover`
***

## Templates
**assertEqual**
```
def test_upper(self):
    """
    Test if method upper() works correctly.
    """
    self.assertEqual('foo'.upper(), 'FOO')
```

**assertTrue** & **assertFalse**
```
def test_isupper(self):
    """
    Test if a string has all letters in capital
    """
    self.assertTrue('FOO'.isupper())
    self.assertFalse('Foo'.isupper())
```

**assertRaises**
- `assertRaises()` to verify that a specific exception gets raised.
```
def test_split(self):
    """
    Check if the split method fails when the separator
    is not a string. Here we'll use 2 which is an integer
    and therefore cannot be spit
    """
    s = 'hello world'
    self.assertEqual(s.split(), ['hello', 'world'])

    with self.assertRaises(TypeError):
        s.split(2)
```

- Exit from Python is implemented by raising the `SystemExit` exception [Reference](https://stackoverflow.com/questions/15672151/is-it-possible-for-a-unit-test-to-assert-that-a-method-calls-sys-exit)
```
if framework.lower() in ["pytorch", "pt"]:
    self._build_PT()
elif framework.lower() in ["keras", "k"]:
    self._build_K()
else:
    self.logger.error(" ")
    self.logger.error(
        "Framework" + str(self.framework) + " NOT recognised!")
    self.logger.error(" ")
    # Exit program
    M.sys.exit()

# This can be unittest like this
with self.assertRaises(SystemExit):
    your_method()
```

**Checking numpy array equality**
- If you want an exact match: `assertTrue(numpy.testing.assert_array_equal(arr1, arr2))`
- If you want a match up to a certain tolerance: `assertTrue(np.linalg.norm(arr1 - arr2) < 1e-6)`
- [Ref](https://stackoverflow.com/questions/3302949/best-way-to-assert-for-numpy-array-equality)

***

**Checking for `sys.exit()`**
- Suppose the code is designed to exit like this: `sys.exit()`; this can be tested as:

```
with self.assertRaises(SystemExit):
    your_method()
```    
- Suppose the code is designed to exit like this: `sys.exit("Error")`; this can be tested as:
```
with self.assertRaises(SystemExit) as cm:
    your_method()

self.assertEqual(cm.exception.code, "Error")
```

[Ref](https://stackoverflow.com/questions/15672151/is-it-possible-for-a-unit-test-to-assert-that-a-method-calls-sys-exit)
***

## Special topic
- Image comparison tests end up bring more trouble than they are worth.
- This is especially the case if you want to run continuous integration across multiple systems (like TravisCI) that may have slightly different fonts or available drawing backends. It can be a lot of work to keep the tests passing even when the functions work perfectly correctly. Furthermore, testing this way requires keeping images in your git repository, which can quickly lead to repository bloat if you're changing the code often.
- A better approach could be to (1) assume matplotlib is going to actually draw the figure correctly, and (2) run numerical tests against the data returned by the plotting functions.
- [Reference](https://stackoverflow.com/questions/27948126/how-can-i-write-unit-tests-against-code-that-uses-matplotlib)

```
# Say you want to test a simple function like this:
import numpy as np
import matplotlib.pyplot as plt
def plot_square(x, y):
    y_squared = np.square(y)
    return plt.plot(x, y_squared)

# Your unit test might then look like
def test_plot_square1():
    x, y = [0, 1, 2], [0, 1, 2]
    line, = plot_square(x, y)
    x_plot, y_plot = line.get_xydata().T
    np.testing.assert_array_equal(y_plot, np.square(y))

# Or, equivalently,
def test_plot_square2():
    f, ax = plt.subplots()
    x, y = [0, 1, 2], [0, 1, 2]
    plot_square(x, y)
    x_plot, y_plot = ax.lines[0].get_xydata().T
    np.testing.assert_array_equal(y_plot, np.square(y))

```
***

## References
- [Unittesting benefits](https://dzone.com/articles/top-8-benefits-of-unit-testing)
