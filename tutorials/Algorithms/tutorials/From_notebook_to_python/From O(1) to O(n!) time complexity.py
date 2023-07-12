#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Overview-of-big-O-complexity" data-toc-modified-id="Overview-of-big-O-complexity-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Overview of big-O complexity</a></span></li><li><span><a href="#Constant-time-complexity:-O(1)" data-toc-modified-id="Constant-time-complexity:-O(1)-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Constant time complexity: <code>O(1)</code></a></span></li><li><span><a href="#Linear-time-complexity:-O(n)" data-toc-modified-id="Linear-time-complexity:-O(n)-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Linear time complexity: <code>O(n)</code></a></span></li><li><span><a href="#Quadratic-time-complexity:-O(n^2)" data-toc-modified-id="Quadratic-time-complexity:-O(n^2)-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Quadratic time complexity: <code>O(n^2)</code></a></span></li><li><span><a href="#Quasilinear-time:-O(n-log-n)" data-toc-modified-id="Quasilinear-time:-O(n-log-n)-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Quasilinear time: <code>O(n log n)</code></a></span></li><li><span><a href="#Exponential-time-complexity:-O(2^n)" data-toc-modified-id="Exponential-time-complexity:-O(2^n)-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Exponential time complexity: <code>O(2^n)</code></a></span></li><li><span><a href="#Factorial-time-complexity:-O(n!)" data-toc-modified-id="Factorial-time-complexity:-O(n!)-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Factorial time complexity: <code>O(n!)</code></a></span></li><li><span><a href="#References" data-toc-modified-id="References-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** From O(1) to O(n!) time complexity
#
# </font>
# </div>

# # Overview of big-O complexity
# <hr style="border:2px solid black"> </hr>

# ![image.png](attachment:image.png)

# # Constant time complexity: `O(1)`
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The time complexity of a function (or set of statements) is considered as `O(1)` if it doesn’t contain a loop, recursion, and call to any other non-constant time function.
# - An algorithm is said to have a constant time when it is not dependent on the input data `n`. No matter the size of the input data, the running time will always be the same.
#
# </font>
# </div>

# In[1]:


def get_first(data):
    """
    Independently of the input data size, it will
    always have the same running time since it only gets
    the first value from the list.
    """
    return data[0]


data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
print(get_first(data))


# # Linear time complexity: `O(n)`
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - An algorithm is said to have a linear time complexity when the running time increases at most linearly with the size of the input data.
# - This is the best possible time complexity when the algorithm must examine all values in the input data.
#
# </font>
# </div>

# In[2]:


data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
for value in data:
    print(value)


# In[3]:


def linear_search(data, value):
    """
    Find the position of an element in an unsorted list.
    We need to look at all values in the list to find the
    value we are looking for.
    """
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError("Value not found in the list")


data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
print(linear_search(data, 7))


# # Quadratic time complexity: `O(n^2)`
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - An algorithm is said to have a quadratic time complexity when it needs to perform a linear time operation for each value in the input data.
#
# </font>
# </div>

# In[4]:


data = [1, 2, 3]
for x in data:
    for y in data:
        print(x, y)


# # Quasilinear time: `O(n log n)`
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Keep in mind that: `O(log n) * O(n) = O(n log n)`
# - An algorithm is said to have a quasilinear time complexity when each operation in the input data have a logarithm time complexity. It is commonly seen in sorting algorithms (e.g. mergesort, timsort, heapsort).
#
# </font>
# </div>

# In[5]:


for value in data1:
    """
    Suppose we have an algorithm called binary search
    For example: for each value in the data1 (O(n)) use the binary search (O(log n))
    to search the same value in data2.

    """
    result.append(binary_search(data2, value))


# In[ ]:


def foo(x):
    """
    This algorithm returns once for each element in the list O(n)
    It then also implements a bisection search O(log n)
    Therefore, it's O(n log n)
    """
    n = len(x)
    print(x)
    if n <= 1:
        print("return")
        return 17
    return foo(x[: n // 2]) + foo(x[n // 2 :])


foo([1, 2, 3, 4, 5, 6, 7, 8])


# # Exponential time complexity: `O(2^n)`
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - An algorithm is said to have an exponential time complexity when the growth doubles with each addition to the input data set.
# - This kind of time complexity is usually seen in brute-force algorithms.
#
# </font>
# </div>

# In[ ]:


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(4)


# # Factorial time complexity: `O(n!)`
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - An algorithm is said to have a factorial time complexity when it grows in a factorial way based on the size of the input data.
# ```
# 2! = 2 x 1 = 2
# 3! = 3 x 2 x 1 = 6
# 4! = 4 x 3 x 2 x 1 = 24
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# 6! = 6 x 5 x 4 x 3 x 2 x 1 = 720
# 7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 5.040
# 8! = 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 40.320
# ```
#
# </font>
# </div>

# In[ ]:


def heap_permutation(data, n):
    """
    A great example of an algorithm which has a factorial
    time complexity is the Heap’s algorithm, which is used
    for generating all possible permutations of n objects.
    """
    if n == 1:
        print(data)
        return

    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n - 1] = data[n - 1], data[i]
        else:
            data[0], data[n - 1] = data[n - 1], data[0]


data = [1, 2, 3]
heap_permutation(data, len(data))


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - [Understanding time complexity with Python examples](https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7)
#
# </font>
# </div>

# In[ ]:
