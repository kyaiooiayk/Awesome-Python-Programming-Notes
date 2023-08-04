#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Built-In-data-structures" data-toc-modified-id="Built-In-data-structures-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Built-In data structures</a></span></li><li><span><a href="#Lists" data-toc-modified-id="Lists-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Lists</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#List-indexing-and-slicing" data-toc-modified-id="List-indexing-and-slicing-3.0.1"><span class="toc-item-num">3.0.1&nbsp;&nbsp;</span>List indexing and slicing</a></span></li></ul></li></ul></li><li><span><a href="#Tuples" data-toc-modified-id="Tuples-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Tuples</a></span></li><li><span><a href="#Dictionaries" data-toc-modified-id="Dictionaries-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Dictionaries</a></span><ul class="toc-item"><li><span><a href="#Hash-collision" data-toc-modified-id="Hash-collision-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Hash collision</a></span></li></ul></li><li><span><a href="#Sets" data-toc-modified-id="Sets-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Sets</a></span></li><li><span><a href="#Frozensets" data-toc-modified-id="Frozensets-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Frozensets</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Lists, sets, frozensets, dictionaries and tuples
# 
# </font>
# </div>

# # Built-In data structures
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# 
# | Type Name | Example                   |Description                            |
# |-----------|---------------------------|---------------------------------------|
# | ``list``  | ``[1, 2, 3]``             | Ordered collection                    |
# | ``tuple`` | ``(1, 2, 3)``             | Immutable ordered collection          |
# | ``dict``  | ``{'a':1, 'b':2, 'c':3}`` | Unordered (key,value) mapping         |
# | ``set``   | ``{1, 2, 3}``             | Unordered collection of unique values |
# 
# 
# </font>
# </div>

# # Lists
# <hr style = "border:2px solid black" ></hr>

# - Lists are the basic *ordered* and *mutable* data collection type in Python.
# - They can be defined with comma-separated values between square brackets; for example, here is a list of the first several prime numbers:

# In[1]:


L = [2, 3, 5, 7]


# Lists have a number of useful properties and methods available to them.
# Here we'll take a quick look at some of the more common and useful ones:

# In[2]:


# Length of a list
len(L)


# In[3]:


# Append a value to the end
L.append(11)
L


# In[4]:


# Addition concatenates lists
L + [13, 17, 19]


# In[5]:


# sort() method sorts in-place
L = [2, 5, 1, 6, 3, 4]
L.sort()
L


# In addition, there are many more built-in list methods; they are well-covered in Python's [online documentation](https://docs.python.org/3/tutorial/datastructures.html).
# 
# While we've been demonstrating lists containing values of a single type, one of the powerful features of Python's compound objects is that they can contain objects of *any* type, or even a mix of types. For example:

# In[6]:


L = [1, 'two', 3.14, [0, 3, 5]]


# This flexibility is a consequence of Python's dynamic type system.
# Creating such a mixed sequence in a statically-typed language like C can be much more of a headache!
# We see that lists can even contain other lists as elements.
# Such type flexibility is an essential piece of what makes Python code relatively quick and easy to write.
# 
# So far we've been considering manipulations of lists as a whole; another essential piece is the accessing of individual elements.
# This is done in Python via *indexing* and *slicing*, which we'll explore next.

# ### List indexing and slicing
# Python provides access to elements in compound types through *indexing* for single elements, and *slicing* for multiple elements.
# As we'll see, both are indicated by a square-bracket syntax.
# Suppose we return to our list of the first several primes:

# In[7]:


L = [2, 3, 5, 7, 11]


# Python uses *zero-based* indexing, so we can access the first and second element in using the following syntax:

# In[8]:


L[0]


# In[9]:


L[1]


# Elements at the end of the list can be accessed with negative numbers, starting from -1:

# In[10]:


L[-1]


# In[11]:


L[-2]


# You can visualize this indexing scheme this way:

# ![List Indexing Figure](fig/list-indexing.png)

# Here values in the list are represented by large numbers in the squares; list indices are represented by small numbers above and below.
# In this case, ``L[2]`` returns ``5``, because that is the next value at index ``2``.

# Where *indexing* is a means of fetching a single value from the list, *slicing* is a means of accessing multiple values in sub-lists.
# It uses a colon to indicate the start point (inclusive) and end point (non-inclusive) of the sub-array.
# For example, to get the first three elements of the list, we can write:

# In[12]:


L[0:3]


# Notice where ``0`` and ``3`` lie in the preceding diagram, and how the slice takes just the values between the indices.
# If we leave out the first index, ``0`` is assumed, so we can equivalently write:

# In[13]:


L[:3]


# Similarly, if we leave out the last index, it defaults to the length of the list.
# Thus, the last three elements can be accessed as follows:

# In[14]:


L[-3:]


# Finally, it is possible to specify a third integer that represents the step size; for example, to select every second element of the list, we can write:

# In[15]:


L[::2]  # equivalent to L[0:len(L):2]


# A particularly useful version of this is to specify a negative step, which will reverse the array:

# In[16]:


L[::-1]


# Both indexing and slicing can be used to set elements as well as access them.
# The syntax is as you would expect:

# In[17]:


L[0] = 100
print(L)


# In[18]:


L[1:3] = [55, 56]
print(L)


# # Tuples
# <hr style = "border:2px solid black" ></hr>

# - Tuples are in many ways similar to lists, but they are defined with parentheses rather than square brackets:

# In[19]:


t = (1, 2, 3)


# They can also be defined without any brackets at all:

# In[20]:


t = 1, 2, 3
print(t)


# Like the lists discussed before, tuples have a length, and individual elements can be extracted using square-bracket indexing:

# In[21]:


len(t)


# In[22]:


t[0]


# The main distinguishing feature of tuples is that they are *immutable*: this means that once they are created, their size and contents cannot be changed:

# In[23]:


t[1] = 4


# In[24]:


t.append(4)


# Tuples are often used in a Python program; a particularly common case is in functions that have multiple return values.
# For example, the ``as_integer_ratio()`` method of floating-point objects returns a numerator and a denominator; this dual return value comes in the form of a tuple:

# In[25]:


x = 0.125
x.as_integer_ratio()


# These multiple return values can be individually assigned as follows:

# In[26]:


numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)


# # Dictionaries
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - Dictionaries are extremely flexible mappings of keys to values, and form the basis of much of Python's internal implementation.
# - They can be created via a comma-separated list of ``key:value`` pairs within curly braces.
# - Items are accessed and set via the indexing syntax used for lists and tuples, except here the index is not a zero-based order but valid key in the dictionary
#     
# </font>
# </div>   

# In[27]:


numbers = {'one':1, 'two':2, 'three':3}


# In[28]:


# Access a value via the key
numbers['two']


# New items can be added to the dictionary using indexing as well:

# In[29]:


# Set a new key:value pair
numbers['ninety'] = 90
print(numbers)


# <div class="alert alert-info">
# <font color=black>
#     
# - Keep in mind that dictionaries do not maintain any sense of order for the input parameters; this is by design.
# - This lack of ordering allows dictionaries to be implemented very efficiently, so that random element access is very fast, **regardless of the size of the dictionary** (if you're curious how this works, read about the concept of a *hash table*).
# 
# </font>
# </div>

# ## Hash collision

# <div class="alert alert-info">
# <font color=black>
#     
# - Hash collisiton happen when two objects have the same jash key. A normal working condition would check for this and find another hask key for this. Hash collisions are unavoidable.Collisions will happen in general, because there are infinite possible hashable values and finite hash codes. 
# 
# </font>
# </div>

# # Sets
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - `set` contains unordered collections of unique items.
# - They are defined much like lists and tuples, except they use the curly brackets of dictionaries
# 
# </font>
# </div>

# In[30]:


primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}


# In[31]:


# union: items appearing in either
primes | odds      # with an operator
primes.union(odds) # equivalently with a method


# In[32]:


# intersection: items appearing in both
primes & odds             # with an operator
primes.intersection(odds) # equivalently with a method


# In[33]:


# difference: items in primes but not in odds
primes - odds           # with an operator
primes.difference(odds) # equivalently with a method


# In[34]:


# symmetric difference: items appearing in only one set
primes ^ odds                     # with an operator
primes.symmetric_difference(odds) # equivalently with a method


# # Frozensets
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - While you can create a set with the built-in `set` or through the `{}` notation, frozensets can only be created through their respective built-in.
# 
# - `frozensets` can be created out of other sets or out of any iterable, much like sets.
# 
# - When printed, frozensets **display** the indication that they are frozen.
# 
# - Sets are mutable but frozensets are not.
# 
# </font>
# </div>

# In[3]:


groceries = {'cheese', 'milk', 'chocolate'}
groceries


# In[4]:


frozenset(groceries)


# In[5]:


frozenset(['cheese', 'milk', 'chocolate'])


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - [Whirlwind Tour of Python](http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp)
# - https://mathspp.com/blog/pydonts
# - https://docs.python.org/3/library/stdtypes.html
# - https://stackoverflow.com/questions/63910315/whats-the-difference-between-a-hashmap-and-a-hashtable-in-python
# - https://stackoverflow.com/questions/114830/is-a-python-dictionary-an-example-of-a-hash-table
#     
# </font>
# </div>

# In[ ]:




