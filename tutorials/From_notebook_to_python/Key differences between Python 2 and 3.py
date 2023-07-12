#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span><ul class="toc-item"><li><span><a href="#Key-differences-between-Python-2-and-3" data-toc-modified-id="Key-differences-between-Python-2-and-3-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Key differences between Python 2 and 3</a></span><ul class="toc-item"><li><span><a href="#Overview---Key-differences-between-Python-2-and-3" data-toc-modified-id="Overview---Key-differences-between-Python-2-and-3-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Overview - Key differences between Python 2 and 3</a></span></li><li><span><a href="#Unicode..." data-toc-modified-id="Unicode...-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Unicode...</a></span><ul class="toc-item"><li><span><a href="#Python-2:" data-toc-modified-id="Python-2:-1.1.2.1"><span class="toc-item-num">1.1.2.1&nbsp;&nbsp;</span>Python 2:</a></span></li><li><span><a href="#Python-3:" data-toc-modified-id="Python-3:-1.1.2.2"><span class="toc-item-num">1.1.2.2&nbsp;&nbsp;</span>Python 3:</a></span></li></ul></li><li><span><a href="#The-print-statement" data-toc-modified-id="The-print-statement-1.1.3"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>The print statement</a></span></li><li><span><a href="#Integer-division" data-toc-modified-id="Integer-division-1.1.4"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>Integer division</a></span></li><li><span><a href="#xrange()" data-toc-modified-id="xrange()-1.1.5"><span class="toc-item-num">1.1.5&nbsp;&nbsp;</span><code>xrange()</code></a></span></li><li><span><a href="#Raising-exceptions" data-toc-modified-id="Raising-exceptions-1.1.6"><span class="toc-item-num">1.1.6&nbsp;&nbsp;</span>Raising exceptions</a></span></li><li><span><a href="#Handling-exceptions" data-toc-modified-id="Handling-exceptions-1.1.7"><span class="toc-item-num">1.1.7&nbsp;&nbsp;</span>Handling exceptions</a></span></li><li><span><a href="#The-next()-function-and-.next()-method" data-toc-modified-id="The-next()-function-and-.next()-method-1.1.8"><span class="toc-item-num">1.1.8&nbsp;&nbsp;</span>The <code>next()</code> function and <code>.next()</code> method</a></span></li><li><span><a href="#In-Python-3.x-for-loop-variables-don't-leak-into-the-global-namespace-anymore" data-toc-modified-id="In-Python-3.x-for-loop-variables-don't-leak-into-the-global-namespace-anymore-1.1.9"><span class="toc-item-num">1.1.9&nbsp;&nbsp;</span>In Python 3.x for-loop variables don't leak into the global namespace anymore</a></span></li><li><span><a href="#Python-3.x-prevents-us-from-comparing-unorderable-types" data-toc-modified-id="Python-3.x-prevents-us-from-comparing-unorderable-types-1.1.10"><span class="toc-item-num">1.1.10&nbsp;&nbsp;</span>Python 3.x prevents us from comparing unorderable types</a></span></li></ul></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Key differences between Python 2 and 3
#     
# </font>
# </div>

# 
# ## Key differences between Python 2 and 3
# 
# 

# There are some good articles already that are summarizing the differences between Python 2 and 3, e.g.,  
# - [https://wiki.python.org/moin/Python2orPython3](https://wiki.python.org/moin/Python2orPython3)
# - [https://docs.python.org/3.0/whatsnew/3.0.html](https://docs.python.org/3.0/whatsnew/3.0.html)
# - [http://python3porting.com/differences.html](http://python3porting.com/differences.html)
# - [https://docs.python.org/3/howto/pyporting.html](https://docs.python.org/3/howto/pyporting.html)  
# etc.
# 
# But it might be still worthwhile, especially for Python newcomers, to take a look at some of those!
# (Note: the the code was executed in Python 3.4.0 and Python 2.7.5 and copied from interactive shell sessions.)

# ### Overview - Key differences between Python 2 and 3

# 
# 
# - [Unicode](#unicode)
# - [The print statement](#print)
# - [Integer division](#integer_div)
# - [xrange()](#xrange)
# - [Raising exceptions](#raising_exceptions)
# - [Handling exceptions](#handling_exceptions)
# - [next() function and .next() method](#next_next)
# - [Loop variables and leaking into the global scope](#loop_leak)
# - [Comparing unorderable types](#compare_unorder)

# ### Unicode...

# 
# #### Python 2: 
# We have ASCII `str()` types, separate `unicode()`, but no `byte` type
# #### Python 3: 
# Now, we finally have Unicode (utf-8) `str`ings, and 2 byte classes: `byte` and `bytearray`s

# In[ ]:


#############
# Python 2  #
#############

>>> type(unicode('is like a python3 str()'))
<type 'unicode'>

>>> type(b'byte type does not exist')
<type 'str'>

>>> 'they are really' + b' the same'
'they are really the same'

>>> type(bytearray(b'bytearray oddly does exist though'))
<type 'bytearray'>

#############
# Python 3
#############

>>> print('strings are now utf-8 \u03BCnico\u0394é!')
strings are now utf-8 μnicoΔé!


>>> type(b' and we have byte types for storing data')
<class 'bytes'>

>>> type(bytearray(b'but also bytearrays for those who prefer them over strings'))
<class 'bytearray'>

>>> 'string' + b'bytes for data'
Traceback (most recent call last):s
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'bytes' object to str implicitly


# ### The print statement

# Very trivial, but this change makes sense, Python 3 now only accepts `print`s with proper parentheses - just like the other function calls ...

# In[ ]:


# Python 2
print 'Hello, World!'
Hello, World!
print('Hello, World!')
Hello, World!

# Python 3
print('Hello, World!')
Hello, World!
print 'Hello, World!'
  File "<stdin>", line 1
    print 'Hello, World!'
                        ^
SyntaxError: invalid syntax


# And if we want to print the output of 2 consecutive print functions on the same line, you would use a comma in Python 2, and a `end=""` in Python 3:

# In[ ]:


# Python 2
print "line 1", ; print 'same line'
line 1 same line

# Python 3
print("line 1", end="") ; print (" same line")
line 1 same line


# ### Integer division

# This is a pretty dangerous thing if you are porting code, or executing Python 3 code in Python 2 since the change in integer-division behavior can often go unnoticed.  
# So, I still tend to use a `float(3)/2` or `3/2.0` instead of a `3/2` in my Python 3 scripts to save the Python 2 guys some trouble ... (PS: and vice versa, you can `from __future__ import division` in your Python 2 scripts).

# In[ ]:


# Python 2
3 / 2
1
3 // 2
1
3 / 2.0
1.5
3 // 2.0
1.0

# Python 3
3 / 2
1.5
3 // 2
1
3 / 2.0
1.5
3 // 2.0
1.0


# ### `xrange()`

#  
# `xrange()` was pretty popular in Python 2.x if you wanted to create an iterable object. The behavior was quite similar to a generator ('lazy evaluation'), but you could iterate over it infinitely. The advantage was that it was generally faster than `range()` (e.g., in a for-loop) - not if you had to iterate over the list multiple times, since the generation happens every time from scratch!  
# In Python 3, the `range()` was implemented like the `xrange()` function so that a dedicated `xrange()` function does not exist anymore.

# In[ ]:


# Python 2
>> > python - m timeit 'for i in range(1000000):' ' pass'
10 loops, best of 3: 66 msec per loop

> python - m timeit 'for i in xrange(1000000):' ' pass'
10 loops, best of 3: 27.8 msec per loop

# Python 3
>> > python3 - m timeit 'for i in range(1000000):' ' pass'
10 loops, best of 3: 51.1 msec per loop

>> > python3 - m timeit 'for i in xrange(1000000):' ' pass'
Traceback(most recent call last):
    File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/timeit.py", line 292, in main
    x = t.timeit(number)
    File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/timeit.py", line 178, in timeit
    timing = self.inner(it, self.timer)
    File "<timeit-src>", line 6, in inner
    for i in xrange(1000000):
NameError: name 'xrange' is not defined


# ### Raising exceptions

# 
# 
# Where Python 2 accepts both notations, the 'old' and the 'new' way, Python 3 chokes (and raises a `SyntaxError` in turn) if we don't enclose the exception argument in parentheses:

# In[ ]:


# Python 2
raise IOError, "file error"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: file error
raise IOError("file error")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: file error

    
# Python 3    
raise IOError, "file error"
  File "<stdin>", line 1
    raise IOError, "file error"
                 ^
SyntaxError: invalid syntax
raise IOError("file error")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: file error


# ### Handling exceptions

# 
# 
# Also the handling of exceptions has slightly changed in Python 3. Now, we have to use the `as` keyword!

# In[ ]:


# Python 2
try:
    blabla
except NameError, err:
    print err, '--> our error msg'

name 'blabla' is not defined --> our error msg

# Python 3
try:
    blabla
except NameError as err:
    print(err, '--> our error msg')

name 'blabla' is not defined --> our error msg


# ### The `next()` function and `.next()` method

# 
# 
# Where you can use both function and method in Python 2.7.5, the `next()` function is all that remains in Python 3!

# In[ ]:


# Python 2
my_generator = (letter for letter in 'abcdefg')
my_generator.next()
'a'
next(my_generator)
'b'

# Python 3
my_generator = (letter for letter in 'abcdefg')
next(my_generator)
'a'
my_generator.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'generator' object has no attribute 'next'


# ### In Python 3.x for-loop variables don't leak into the global namespace anymore

# This goes back to a change that was made in Python 3.x and is described in [What’s New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html) as follows:
# 
# *"List comprehensions no longer support the syntactic form `[... for var in item1, item2, ...]`. Use `[... for var in (item1, item2, ...)]` instead. Also note that list comprehensions have different semantics: they are closer to syntactic sugar for a generator expression inside a `list()` constructor, and in particular the loop control variables are no longer leaked into the surrounding scope."*

# In[ ]:


from platform import python_version
print 'This code cell was executed in Python', python_version()
'This code cell was executed in Python 2.7.6'
i = 1
print [i for i in range(5)]
'[0, 1, 2, 3, 4]'
print i, '-> i in global'
'4 -> i in global'


# In[61]:


get_ipython().run_cell_magic('python3', '', "from platform import python_version\nprint('This code cell was executed in Python', python_version())\n\ni = 1\nprint([i for i in range(5)])\nprint(i, '-> i in global')\n")


# ### Python 3.x prevents us from comparing unorderable types

# In[101]:


from platform import python_version
print 'This code cell was executed in Python', python_version()
'This code cell was executed in Python 2.7.6'
print [1, 2] > 'foo'
'False'
print (1, 2) > 'foo'
'True'
print [1, 2] > (1, 2)
'False'


# In[67]:


from platform import python_version
print('This code cell was executed in Python', python_version())

print([1, 2] > 'foo')
print((1, 2) > 'foo')
print([1, 2] > (1, 2))


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/not_so_obvious_python_stuff.ipynb?create=1
# 
# </font>
# </div>
