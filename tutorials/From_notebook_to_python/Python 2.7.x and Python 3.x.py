#!/usr/bin/env python
# coding: utf-8

# # Python 2.7.x and Python 3.x

# <br>
# Many beginning Python users are wondering with which version of Python they should start. My answer to this question is usually something along the lines "just go with the version your favorite tutorial was written in, and check out the differences later on."
# 
# But what if you are starting a new project and have the choice to pick? I would say there is currently no "right" or "wrong" as long as both Python 2.7.x and Python 3.x support the libraries that you are planning to use. However, it is worthwhile to have a look at the major differences between those two most popular versions of Python to avoid common pitfalls when writing the code for either one of them, or if you are planning to port your project.

# ### The `__future__` module

# Python 3.x introduced some Python 2-incompatible keywords and features that can be imported via the in-built `__future__` module in Python 2. It is recommended to use `__future__` imports it if you are planning Python 3.x support for your code. For example, if we want Python 3.x's integer division behavior in Python 2, we can import it via
# 
#     from __future__ import division
#     
# More features that can be imported from the `__future__` module are listed in the table below:

# <table>
# <tr><th class="head">feature</th>
# <th class="head">optional in</th>
# <th class="head">mandatory in</th>
# <th class="head">effect</th>
# </tr>
# 
# <tr><td>nested_scopes</td>
# <td>2.1.0b1</td>
# <td>2.2</td>
# <td><a href="http://www.python.org/dev/peps/pep-0227"><strong>PEP 227</strong></a>:
# <em>Statically Nested Scopes</em></td>
# </tr>
# <tr><td>generators</td>
# <td>2.2.0a1</td>
# <td>2.3</td>
# <td><a href="http://www.python.org/dev/peps/pep-0255"><strong>PEP 255</strong></a>:
# <em>Simple Generators</em></td>
# </tr>
# <tr><td>division</td>
# <td>2.2.0a2</td>
# <td>3.0</td>
# <td><a href="http://www.python.org/dev/peps/pep-0238"><strong>PEP 238</strong></a>:
# <em>Changing the Division Operator</em></td>
# </tr>
# <tr><td>absolute_import</td>
# <td>2.5.0a1</td>
# <td>3.0</td>
# <td><a href="http://www.python.org/dev/peps/pep-0328"><strong>PEP 328</strong></a>:
# <em>Imports: Multi-Line and Absolute/Relative</em></td>
# </tr>
# <tr><td>with_statement</td>
# <td>2.5.0a1</td>
# <td>2.6</td>
# <td><a href="http://www.python.org/dev/peps/pep-0343"><strong>PEP 343</strong></a>:
# <em>The &#8220;with&#8221; Statement</em></td>
# </tr>
# <tr><td>print_function</td>
# <td>2.6.0a2</td>
# <td>3.0</td>
# <td><a href="http://www.python.org/dev/peps/pep-3105"><strong>PEP 3105</strong></a>:
# <em>Make print a function</em></td>
# </tr>
# <tr><td>unicode_literals</td>
# <td>2.6.0a2</td>
# <td>3.0</td>
# <td><a href="http://www.python.org/dev/peps/pep-3112"><strong>PEP 3112</strong></a>:
# <em>Bytes literals in Python 3000</em></td>
# </tr>
# </table>
# <br>
# <center>(Source: [https://docs.python.org/2/library/__future__.html](https://docs.python.org/2/library/__future__.html#module-__future__))</center>

# In[1]:


from platform import python_version


# ## The print function

# [[back to the section-overview](#Sections)]

# Very trivial, and the change in the print-syntax is probably the most widely known change, but still it is worth mentioning: Python 2's print statement has been replaced by the `print()` function, meaning that we have to wrap the object that we want to print in parantheses. 
# 
# Python 2 doesn't have a problem with additional parantheses, but in contrast, Python 3 would raise a `SyntaxError` if we called the print function the Python 2-way without the parentheses.  
# 

# #### Python 2

# In[3]:


print 'Python', python_version()
print 'Hello, World!'
print('Hello, World!')
print "text", ; print 'print more text on the same line'


# <br>

# #### Python 3

# In[2]:


print('Python', python_version())
print('Hello, World!')

print("some text,", end="") 
print(' print more text on the same line')


# In[3]:


print 'Hello, World!'


# **Note:**
# 
# Printing "Hello, World" above  via Python 2 looked quite "normal". However, if we have multiple objects inside the parantheses, we will create a tuple, since `print` is a "statement" in Python 2, not a function call.

# In[2]:


print 'Python', python_version()
print('a', 'b')
print 'a', 'b'


# <br>
# <br>

# ## Integer division

# [[back to the section-overview](#Sections)]

# This change is particularly dangerous if you are porting code, or if you are executing Python 3 code in Python 2, since the change in integer-division behavior can often go unnoticed (it doesn't raise a `SyntaxError`).  
# So, I still tend to use a `float(3)/2` or `3/2.0` instead of a `3/2` in my Python 3 scripts to save the Python 2 guys some trouble (and vice versa, I recommend a `from __future__ import division` in your Python 2 scripts).

# #### Python 2

# In[4]:


print 'Python', python_version()
print '3 / 2 =', 3 / 2
print '3 // 2 =', 3 // 2
print '3 / 2.0 =', 3 / 2.0
print '3 // 2.0 =', 3 // 2.0


# <br>

# #### Python 3

# In[4]:


print('Python', python_version())
print('3 / 2 =', 3 / 2)
print('3 // 2 =', 3 // 2)
print('3 / 2.0 =', 3 / 2.0)
print('3 // 2.0 =', 3 // 2.0)


# <br>
# <br>

# ## Unicode

# [[back to the section-overview](#Sections)]

# Python 2 has ASCII `str()` types, separate `unicode()`, but no `byte` type.  
# 
# Now, in Python 3, we finally have Unicode (utf-8) `str`ings, and 2 byte classes: `byte` and `bytearray`s.

# #### Python 2

# In[2]:


print 'Python', python_version()


# In[3]:


print type(unicode('this is like a python3 str type'))


# In[4]:


print type(b'byte type does not exist')


# In[5]:


print 'they are really' + b' the same'


# In[7]:


print type(bytearray(b'bytearray oddly does exist though'))


# <br>

# #### Python 3

# In[6]:


print('Python', python_version())
print('strings are now utf-8 \u03BCnico\u0394é!')


# In[8]:


print('Python', python_version(), end="")
print(' has', type(b' bytes for storing data'))


# In[11]:


print('and Python', python_version(), end="")
print(' also has', type(bytearray(b'bytearrays')))


# In[13]:


'note that we cannot add a string' + b'bytes for data'


# <br>
# <br>

# ## xrange

# [[back to the section-overview](#Sections)]

#  
# The usage of `xrange()` is very popular in Python 2.x for creating an iterable object, e.g., in a for-loop or list/set-dictionary-comprehension.  
# The behavior was quite similar to a generator (i.e., "lazy evaluation"), but here the xrange-iterable is not exhaustible - meaning, you could iterate over it infinitely.  
# 
# 
# Thanks to its "lazy-evaluation", the advantage of the regular `range()` is that `xrange()` is generally faster if you have to iterate over it only once (e.g., in a for-loop). However, in contrast to 1-time iterations, it is not recommended if you repeat the iteration multiple times, since the generation happens every time from scratch!  
# 
# In Python 3, the `range()` was implemented like the `xrange()` function so that a dedicated `xrange()` function does not exist anymore (`xrange()` raises a `NameError` in Python 3).

# In[5]:


import timeit

n = 10000
def test_range(n):
    return for i in range(n):
        pass
    
def test_xrange(n):
    for i in xrange(n):
        pass    


# <br>

# #### Python 2

# In[6]:


print 'Python', python_version()

print '\ntiming range()'
get_ipython().run_line_magic('timeit', 'test_range(n)')

print '\n\ntiming xrange()'
get_ipython().run_line_magic('timeit', 'test_xrange(n)')


# <br>

# #### Python 3

# In[7]:


print('Python', python_version())

print('\ntiming range()')
get_ipython().run_line_magic('timeit', 'test_range(n)')


# In[5]:


print(xrange(10))


# <a id='contains'></a>
# <br>
# <br>
# 

# ### The `__contains__` method for `range` objects in Python 3

# Another thing worth mentioning is that `range` got a "new" `__contains__` method in Python 3.x (thanks to [Yuchen Ying](https://github.com/yegle), who pointed this out).  The `__contains__` method can speedup "look-ups" in Python 3.x `range` significantly for integer and Boolean types.
# 

# In[3]:


x = 10000000


# In[4]:


def val_in_range(x, val):
    return val in range(x)


# In[5]:


def val_in_xrange(x, val):
    return val in xrange(x)


# In[7]:


print('Python', python_version())
assert(val_in_range(x, x/2) == True)
assert(val_in_range(x, x//2) == True)
get_ipython().run_line_magic('timeit', 'val_in_range(x, x/2)')
get_ipython().run_line_magic('timeit', 'val_in_range(x, x//2)')


# Based on the `timeit` results above, you see that the execution for the "look up" was about 60,000 faster when it was of an integer type rather than a float. However, since Python 2.x's `range` or `xrange` doesn't have a `__contains__` method, the "look-up speed" wouldn't be that much different for integers or floats:

# <br>

# In[6]:


print 'Python', python_version()
assert(val_in_xrange(x, x/2.0) == True)
assert(val_in_xrange(x, x/2) == True)
assert(val_in_range(x, x/2) == True)
assert(val_in_range(x, x//2) == True)
get_ipython().run_line_magic('timeit', 'val_in_xrange(x, x/2.0)')
get_ipython().run_line_magic('timeit', 'val_in_xrange(x, x/2)')
get_ipython().run_line_magic('timeit', 'val_in_range(x, x/2.0)')
get_ipython().run_line_magic('timeit', 'val_in_range(x, x/2)')


# <br>

# Below the "proofs" that the `__contain__` method wasn't added to Python 2.x yet:

# In[8]:


print('Python', python_version())
range.__contains__


# In[7]:


print 'Python', python_version()
range.__contains__


# In[8]:


print 'Python', python_version()
xrange.__contains__


# <br>
# <br>

# #### Note about the speed differences in Python 2 and 3

# Some people pointed out the speed difference between Python 3's `range()` and Python2's `xrange()`. Since they are implemented the same way one would expect the same speed. However the difference here just comes from the fact that Python 3 generally tends to run slower than Python 2. 

# In[3]:


def test_while():
    i = 0
    while i < 20000:
        i += 1
    return


# In[4]:


print('Python', python_version())
get_ipython().run_line_magic('timeit', 'test_while()')


# In[6]:


print 'Python', python_version()
get_ipython().run_line_magic('timeit', 'test_while()')


# <br>
# <br>

# ## Raising exceptions

# [[back to the section-overview](#Sections)]

# 
# 
# Where Python 2 accepts both notations, the 'old' and the 'new' syntax, Python 3 chokes (and raises a `SyntaxError` in turn) if we don't enclose the exception argument in parentheses:

# #### Python 2

# In[7]:


print 'Python', python_version()


# In[8]:


raise IOError, "file error"


# In[9]:


raise IOError("file error")


# <br>

# #### Python 3

# In[9]:


print('Python', python_version())


# In[10]:


raise IOError, "file error"


# The proper way to raise an exception in Python 3:

# In[11]:


print('Python', python_version())
raise IOError("file error")


# <br>
# <br>

# ## Handling exceptions

# [[back to the section-overview](#Sections)]

# Also the handling of exceptions has slightly changed in Python 3. In Python 3 we have to use the "`as`" keyword now

# #### Python 2

# In[10]:


print 'Python', python_version()
try:
    let_us_cause_a_NameError
except NameError, err:
    print err, '--> our error message'


# <br>

# #### Python 3

# In[12]:


print('Python', python_version())
try:
    let_us_cause_a_NameError
except NameError as err:
    print(err, '--> our error message')


# <br>
# <br>

# <a id='The-next-function-and-next-method'></a>

# ## The next() function and .next() method

# [[back to the section-overview](#Sections)]

# Since `next()` (`.next()`) is such a commonly used function (method), this is another syntax change (or rather change in implementation) that is worth mentioning: where you can use both the function and method syntax in Python 2.7.5, the `next()` function is all that remains in Python 3 (calling the `.next()` method raises an `AttributeError`).

# #### Python 2

# In[11]:


print 'Python', python_version()

my_generator = (letter for letter in 'abcdefg')

next(my_generator)
my_generator.next()


# <br>

# #### Python 3

# In[13]:


print('Python', python_version())

my_generator = (letter for letter in 'abcdefg')

next(my_generator)


# In[14]:


my_generator.next()


# <br>
# <br>

# ## For-loop variables and the global namespace leak

# [[back to the section-overview](#Sections)]

# Good news is: In Python 3.x for-loop variables don't leak into the global namespace anymore!
# 
# This goes back to a change that was made in Python 3.x and is described in [What’s New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html) as follows:
# 
# "List comprehensions no longer support the syntactic form `[... for var in item1, item2, ...]`. Use `[... for var in (item1, item2, ...)]` instead. Also note that list comprehensions have different semantics: they are closer to syntactic sugar for a generator expression inside a `list()` constructor, and in particular the loop control variables are no longer leaked into the surrounding scope."

# #### Python 2

# In[12]:


print 'Python', python_version()

i = 1
print 'before: i =', i

print 'comprehension: ', [i for i in range(5)]

print 'after: i =', i


# <br>

# #### Python 3

# In[15]:


print('Python', python_version())

i = 1
print('before: i =', i)

print('comprehension:', [i for i in range(5)])

print('after: i =', i)


# <br>
# <br>

# ## Comparing unorderable types

# [[back to the section-overview](#Sections)]

# Another nice change in Python 3 is that a `TypeError` is raised as warning if we try to compare unorderable types.

# #### Python 2

# In[2]:


print 'Python', python_version()
print "[1, 2] > 'foo' = ", [1, 2] > 'foo'
print "(1, 2) > 'foo' = ", (1, 2) > 'foo'
print "[1, 2] > (1, 2) = ", [1, 2] > (1, 2)


# <br>

# #### Python 3

# In[16]:


print('Python', python_version())
print("[1, 2] > 'foo' = ", [1, 2] > 'foo')
print("(1, 2) > 'foo' = ", (1, 2) > 'foo')
print("[1, 2] > (1, 2) = ", [1, 2] > (1, 2))


# <br>
# <br>

# <a id='Parsing-user-inputs-via-input'></a>

# ## Parsing user inputs via input()

# [[back to the section-overview](#Sections)]

# Fortunately, the `input()` function was fixed in Python 3 so that it always stores the user inputs as `str` objects. In order to avoid the dangerous behavior in Python 2 to read in other types than `strings`, we have to use `raw_input()` instead.

# #### Python 2

# <div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">Python <span style="color: #6600EE; font-weight: bold">2.7</span><span style="color: #333333">.</span><span style="color: #0000DD; font-weight: bold">6</span> 
# [GCC <span style="color: #6600EE; font-weight: bold">4.0</span><span style="color: #333333">.</span><span style="color: #0000DD; font-weight: bold">1</span> (Apple Inc<span style="color: #333333">.</span> build <span style="color: #0000DD; font-weight: bold">5493</span>)] on darwin
# Type <span style="background-color: #fff0f0">&quot;help&quot;</span>, <span style="background-color: #fff0f0">&quot;copyright&quot;</span>, <span style="background-color: #fff0f0">&quot;credits&quot;</span> <span style="color: #000000; font-weight: bold">or</span> <span style="background-color: #fff0f0">&quot;license&quot;</span> <span style="color: #008800; font-weight: bold">for</span> more information<span style="color: #333333">.</span>
# 
# <span style="color: #333333">&gt;&gt;&gt;</span> my_input <span style="color: #333333">=</span> <span style="color: #007020">input</span>(<span style="background-color: #fff0f0">&#39;enter a number: &#39;</span>)
# 
# enter a number: <span style="color: #0000DD; font-weight: bold">123</span>
# 
# <span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">type</span>(my_input)
# <span style="color: #333333">&lt;</span><span style="color: #007020">type</span> <span style="background-color: #fff0f0">&#39;int&#39;</span><span style="color: #333333">&gt;</span>
# 
# <span style="color: #333333">&gt;&gt;&gt;</span> my_input <span style="color: #333333">=</span> raw_input(<span style="background-color: #fff0f0">&#39;enter a number: &#39;</span>)
# 
# enter a number: <span style="color: #0000DD; font-weight: bold">123</span>
# 
# <span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">type</span>(my_input)
# <span style="color: #333333">&lt;</span><span style="color: #007020">type</span> <span style="background-color: #fff0f0">&#39;str&#39;</span><span style="color: #333333">&gt;</span>
# </pre></div>
# 

# <br>

# #### Python 3

# <!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">Python <span style="color: #6600EE; font-weight: bold">3.4</span><span style="color: #333333">.</span><span style="color: #0000DD; font-weight: bold">1</span> 
# [GCC <span style="color: #6600EE; font-weight: bold">4.2</span><span style="color: #333333">.</span><span style="color: #0000DD; font-weight: bold">1</span> (Apple Inc<span style="color: #333333">.</span> build <span style="color: #0000DD; font-weight: bold">5577</span>)] on darwin
# Type <span style="background-color: #fff0f0">&quot;help&quot;</span>, <span style="background-color: #fff0f0">&quot;copyright&quot;</span>, <span style="background-color: #fff0f0">&quot;credits&quot;</span> <span style="color: #000000; font-weight: bold">or</span> <span style="background-color: #fff0f0">&quot;license&quot;</span> <span style="color: #008800; font-weight: bold">for</span> more information<span style="color: #333333">.</span>
# 
# <span style="color: #333333">&gt;&gt;&gt;</span> my_input <span style="color: #333333">=</span> <span style="color: #007020">input</span>(<span style="background-color: #fff0f0">&#39;enter a number: &#39;</span>)
# 
# enter a number: <span style="color: #0000DD; font-weight: bold">123</span>
# 
# <span style="color: #333333">&gt;&gt;&gt;</span> <span style="color: #007020">type</span>(my_input)
# <span style="color: #333333">&lt;</span><span style="color: #008800; font-weight: bold">class</span> <span style="color: #FF0000; background-color: #FFAAAA">&#39;</span><span style="color: #BB0066; font-weight: bold">str</span><span style="background-color: #fff0f0">&#39;&gt;</span>
# </pre></div>
# 

# <br>
# <br>

# ## Returning iterable objects instead of lists

# [[back to the section-overview](#Sections)]

# As we have already seen in the [`xrange`](#xrange) section, some functions and methods return iterable objects in Python 3 now  - instead of lists in Python 2.  
# 
# Since we usually iterate over those only once anyway, I think this change makes a lot of sense to save memory. However, it is also possible - in contrast to generators - to iterate over those multiple times if needed, it is aonly not so efficient.
# 
# And for those cases where we really need the `list`-objects, we can simply convert the iterable object into a `list` via the `list()` function.

# #### Python 2

# In[2]:


print 'Python', python_version() 

print range(3) 
print type(range(3))


# #### Python 3

# In[7]:


print('Python', python_version())

print(range(3))
print(type(range(3)))
print(list(range(3)))


# <br>

# **Some more commonly used functions and methods that don't return lists anymore in Python 3:**
# 
# - `zip()`
# 
# - `map()`
# 
# - `filter()`
# 
# - dictionary's `.keys()` method
# 
# - dictionary's `.values()` method
# 
# - dictionary's `.items()` method
# 

# <br>
# <br>

# ## Banker's Rounding

# [[back to the section-overview](#Sections)]

# Python 3 adopted the now standard way of rounding decimals when it results in a tie (.5) at the last significant digits. Now, in Python 3, decimals are rounded to the nearest even number.  Although it's an inconvenience for code portability, it's supposedly a better way of rounding compared to rounding up as it avoids the bias towards large numbers. For more information, see the excellent Wikipedia articles and paragraphs:
# - [https://en.wikipedia.org/wiki/Rounding#Round_half_to_even](https://en.wikipedia.org/wiki/Rounding#Round_half_to_even)
# - [https://en.wikipedia.org/wiki/IEEE_floating_point#Roundings_to_nearest](https://en.wikipedia.org/wiki/IEEE_floating_point#Roundings_to_nearest)

# #### Python 2

# In[5]:


print 'Python', python_version()


# In[6]:


round(15.5)


# In[7]:


round(16.5)


# #### Python 3

# In[4]:


print('Python', python_version())


# In[5]:


round(15.5)


# In[6]:


round(16.5)


# # References
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/key_differences_between_python_2_and_3.ipynb?create=1

# In[ ]:




