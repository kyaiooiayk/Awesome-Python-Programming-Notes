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

## Unit Testing vs. Functional Testing
- Unit tests isolate and test individual code units to verify they function as intended. You use unit testing to verify that specific system behaviors produce the intended results.
- You use functional testing to check the functionalities of the entire system and ensure different components work together as intended. Its purpose is to check an entire application, including its hardware, networking infrastructure, front-end UI, and the back-end database.
- Unit tests point to a specific issue that requires fixing. Since functional testing checks the entire application, it mainly indicates a general issue without pointing out a specific problem.
***

## General templates
- This is just a template with all the necessary imports, comments and some code to refresh someone's knowledge on unittesting.
- A testcase is created by subclassing `unittest.TestCase`. Essentialy the class `TestSum` inherits from the `TestCase` class.
- All the following methods start with a `test_`. This naming convention informs the test runner about which methods represent a test.
- While unittesting it is acceptable to use long and descriptive names for testing function.

```python
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
```python
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
```python
def test_upper(self):
    """
    Test if method upper() works correctly.
    """
    self.assertEqual('foo'.upper(), 'FOO')
```

**assertTrue** & **assertFalse**
```python
def test_isupper(self):
    """
    Test if a string has all letters in capital
    """
    self.assertTrue('FOO'.isupper())
    self.assertFalse('Foo'.isupper())
```

**assertRaises**
- `assertRaises()` to verify that a specific exception gets raised.
```python
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
```python
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

**Checking numpy array equality with a tollerance**
```python
a=np.array([1,2])
a=np.array([1.0001,2.0001])
np.testing.assert_array_almost_equal(a, b, decimal=9)
```
***

**Checking list equality**
```python
a = ["1","2"]
b = ["1","2"]
self.assertListEqual(a, b)
```
***

**Checking for `sys.exit()`**
- Suppose the code is designed to exit like this: `sys.exit()`; this can be tested as:

```python
with self.assertRaises(SystemExit):
    your_method()
```
- Suppose the code is designed to exit like this: `sys.exit("Error")`; this can be tested as:
```python
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

```python
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

## Mocking
- A mock object substitutes and imitates a real object within a testing environment.
- **It is used in this scenario**: if your code makes HTTP requests to external services, then your tests execute predictably only so far as the services are behaving as you expected. Sometimes, a temporary change in the behavior of these external services can cause intermittent failures within your test suite. But that would not be a problem of your code, yet the test fails!
- Replacing the actual request with a mock object would allow you to simulate external service outages and successful responses in a predictable way. This is what mocking in python does.
- Beware of overusing mock objects! It’s easy to take advantage of the power of Python mock objects and mock so much that you actually decrease the value of your tests.
***

## Coverage
- Coverage measurement is typically used to gauge the effectiveness of tests. It can show which parts of your code are being exercised by tests, and which are not. Test coverage is a ratio between the number of lines executed by at least one test case and the total number of lines of the code base.
- Install it with: `pip install coverage`
- Navigate to your test folder and run: `python -m coverage run -m unittest`
- To generate the coverage report: `python -m coverage report`
- To generate the coverage report in HTML format: `python -m coverage html` Use this file to check what you are missing.
- The test coverage is often used to assess the quality of a test suite. If the test coverage is low e.g., 5%, it is an indicator that you’re not testing enough. However, the reverse may not be true. For example, 100% test coverage is not a guarantee that you have a good test suite. In other words, a test suite with high coverage can still be of poor quality.
***

## Available tutorials
- [Unittesting a string method](https://github.com/kyaiooiayk/Python-Programming/blob/main/tutorials/Unittesting/tutorials/example_1.py)
- [Unittesting an addition method](https://github.com/kyaiooiayk/Python-Programming/blob/main/tutorials/Unittesting/tutorials/Simple_unit_check.py)
- [Unittesting an addition failing method](https://github.com/kyaiooiayk/Python-Programming/blob/main/tutorials/Unittesting/tutorials/Simple_unit_check_one_failed.py)
- [How it is used in practice](https://github.com/kyaiooiayk/Python-Programming/tree/main/tutorials/Unittesting/tutorials/How%20it%20is%20used%20in%20practice)
***

## References
- [Unittesting benefits](https://dzone.com/articles/top-8-benefits-of-unit-testing)
- [Tests, DocTests, UnitTests](https://python-course.eu/advanced-python/tests-doctest-unittest.php)
- [Python mocking](https://realpython.com/python-mock-library/)
- [Test coverage](https://coverage.readthedocs.io/en/7.0.5/)
- [Unit vs. functional testing](https://brightsec.com/blog/unit-testing-vs-functional-testing/)
***