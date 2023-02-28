# Test-driven Development (TDD)
***

## Introduction
- In the previous chapters, we tested functions, which we had already been finished. What about testing code you haven't yet written? You think that this is not possible? It is not only possible, it is the underlying idea of test-driven development. In the extreme case, you define tests before you start coding the actual source code. The program developer writes an automated test case which defines the desired "behaviour" of a function. This test case will - that's the idea behind the approach - initially fail, because the code has still to be written.

- The major problem or difficulty of this approach is the task of writing suitable tests. Naturally, the perfect test would check all possible inputs and validate the output. Of course, this is generally not always feasible.

- The first step is to write a draft like this (create a file called `fibonacci_test.py`):

```python
import doctest
def fib(n):
    """ 
    Calculates the n-th Fibonacci number iteratively 
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10) 
    55
    >>> fib(15)
    610
    >>> 
    """
    return 0
if __name__ == "__main__": 
    doctest.testmod()
```

- Then a `python fibonacci_test.py` will none except one.
- Now we have to keep on writing and changing the code for the function fib until it passes the test.
- This test approach is a method of software development, which is called test-driven development.
***

## References
- https://python-course.eu/advanced-python/tests-doctest-unittest.php
***