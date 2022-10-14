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
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
if __name__ == "__main__": 
    doctest.testmod()