#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Iterators" data-toc-modified-id="Iterators-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Iterators</a></span></li><li><span><a href="#enumerate" data-toc-modified-id="enumerate-3"><span class="toc-item-num">3&nbsp;&nbsp;</span><code>enumerate</code></a></span></li><li><span><a href="#zip" data-toc-modified-id="zip-4"><span class="toc-item-num">4&nbsp;&nbsp;</span><code>zip</code></a></span></li><li><span><a href="#map" data-toc-modified-id="map-5"><span class="toc-item-num">5&nbsp;&nbsp;</span><code>map</code></a></span></li><li><span><a href="#filter" data-toc-modified-id="filter-6"><span class="toc-item-num">6&nbsp;&nbsp;</span><code>filter</code></a></span></li><li><span><a href="#reduce" data-toc-modified-id="reduce-7"><span class="toc-item-num">7&nbsp;&nbsp;</span><code>reduce</code></a></span></li><li><span><a href="#Iterators-as-function-arguments" data-toc-modified-id="Iterators-as-function-arguments-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Iterators as function arguments</a></span></li><li><span><a href="#Why-there-is-no-unzip-method-in-python?" data-toc-modified-id="Why-there-is-no-unzip-method-in-python?-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Why there is no <code>unzip</code> method in python?</a></span></li><li><span><a href="#Specialized-Iterators:-itertools" data-toc-modified-id="Specialized-Iterators:-itertools-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Specialized Iterators: itertools</a></span></li><li><span><a href="#References" data-toc-modified-id="References-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Built-in iterators
#
# </font>
# </div>

# # Iterators
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - `range` is not a list, but an **iterator**.
#
# </font>
# </div>

# In[2]:


for i in range(10):
    # end = " " allows use to print in a single row
    print(i, end=" ")


# <div class="alert alert-info">
# <font color=black>
#
# - When you write something like `for val in L`, the Python interpreter checks whether it has an iterator interface, which you can check yourself with the built-in iter function:
# - It is this iterator object that provides the functionality required by the `for` loop.
# - The `iter` object is a container that gives you access to the next object for as long as it's valid, which can be seen with the built-in function `next`,
#
#
# - **What is the purpose of all of this?**
#     - It allows Python to treat things as lists that are *not actually lists*.
#     - The benefit of the iterator indirection is that the full list is **never** explicitly created! **Save in memory**.
#
# </font>
# </div>

# In[3]:


for value in [2, 4, 6, 8, 10]:
    # do some operation
    print(value + 1, end=" ")


# In[4]:


iter([2, 4, 6, 8, 10])


# In[5]:


I = iter([2, 4, 6, 8, 10])


# In[6]:


print(next(I))


# In[7]:


print(next(I))


# In[8]:


print(next(I))


# <div class="alert alert-info">
# <font color=black>
#
# - The most common example of this **indirect iteration** is the `range()` function in Python 3
# - This returns not a list, but a special `range()` object:
#
# </font>
# </div>

# In[9]:


range(10)


# In[9]:


# range, like a list, exposes an iterator:
iter(range(10))


# In[10]:


# so Python knows to treat it as if it's a list:
for i in range(10):
    print(i, end=" ")


# <div class="alert alert-info">
# <font color=black>
#
# - The benefit of the iterator indirection is that **the full list is never explicitly created!**
# - We can see this by doing a range calculation that would **exahust** our system memory if we actually instantiated it (note that in Python 2, ``range`` creates a list, so running the following will not lead to good things!):
#
# </font>
# </div>

# In[11]:


# This is one trillion!
N = 10**12
for i in range(N):
    if i >= 10:
        break
    print(i, end=", ")


# In[12]:


# Python's itertools library contains a count function that acts as an infinite range:
from itertools import count

for i in count():
    if i >= 10:
        # Use a break otherwise it will never finish
        break
    print(i, end=", ")


# # `enumerate`
# <hr style = "border:2px solid black" ></hr>

# In[12]:


# Work but it is not very pythonic
L = [2, 4, 6, 8, 10]
for i in range(len(L)):
    print(i, L[i])


# In[13]:


# The pythonic way of doing it
for i, val in enumerate(L):
    print(i, val)


# # `zip`
# <hr style = "border:2px solid black" ></hr>

# In[27]:


L = [2, 4, 6, 8, 10]
R = [3, 6, 9, 12, 15]
# zip zips together iterables
for lval, rval in zip(L, R):
    print(lval, rval)


# <div class="alert alert-info">
# <font color=black>
#
# - The ``map`` and ``filter`` functions, along with the ``reduce`` function (which lives in Python's ``functools`` module) are fundamental components of the **functional programming**.
# - This style, which, while not a dominant programming style in the Python world, has its outspoken proponents.
#
# </font>
# </div>

# # `map`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The map iterator takes a function and applies it to the values in an iterator.
#
# - Find the first 10 square numbers.
#
# </font>
# </div>

# In[16]:


def square(x):
    return x**2


for val in map(square, range(10)):
    print(val, end=" ")


# # `filter`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The filter iterator looks similar, except it only passes-through values  for which the filter function evaluates to True:
# - Find values up to 10 for which x % 2 is zero
#
# </font>
# </div>

# In[17]:


def is_even(x):
    return x % 2 == 0


for val in filter(is_even, range(10)):
    print(val, end=" ")


# # `reduce`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - `reduce` is a tool that is typically associated with functional programming, which is a programming paradigm.
#
# - In a short sentence, reduce takes an iterable and a binary function (a function that takes two arguments), and then uses that binary function to boil the iterable down to a single value.
#
# - A concrete example is the function `sum` which is a reduction.
#
# - Keep in mind that part of what a reduction does is taking an iterable and reducing it to a single value.
#
# </font>
# </div>

# In[3]:


sum(range(10))


# In[4]:


from functools import reduce
import operator

reduce(operator.add, range(10))


# In[1]:


from math import prod

prod(range(1, 11))


# In[5]:


reduce(operator.mul, range(1, 11))


# In[6]:


#  Now, say that you want to access the nested 42 through a series of successive
#  key accesses that you have in a list:
d = {"one": {2: {"c": {4: 42}}}}
keys = ["one", 2, "c", 4]

val = d
for key in keys:
    val = val[key]
val


# ![image.png](attachment:image.png)

# In[7]:


reduce(dict.get, keys, d)


# # Iterators as function arguments
# <hr style = "border:2px solid black" ></hr>

# In[18]:


# *args syntax works not just with sequences, but with any iterator:
print(*range(10))


# <div class="alert alert-info">
# <font color=black>
#
# - This means that problem like the one before "find values up to 10 for which x % 2 is zero" can be reduced down to
#
# </font>
# </div>

# In[19]:


print(*map(lambda x: x**2, range(10)))


# # Why there is no `unzip` method in python?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Because the opposite of `zip()` is `zip()`!
# - The key is that `zip()` can zip-together any number of iterators or sequences.
#
# </font>
# </div>

# In[19]:


L1 = (1, 2, 3, 4)
L2 = ("a", "b", "c", "d")


# In[23]:


z = zip(L1, L2)
print(*z)


# In[22]:


z = zip(L1, L2)
new_L1, new_L2 = zip(*z)
print(new_L1, new_L2)


# # Specialized Iterators: itertools
# <hr style = "border:2px solid black" ></hr>

# In[24]:


from itertools import permutations

p = permutations(range(3))
print(*p)


# In[24]:


from itertools import combinations

c = combinations(range(4), 2)
print(*c)


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - [Whirlwind Tour of Python](http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp)
#
# </font>
# </div>
