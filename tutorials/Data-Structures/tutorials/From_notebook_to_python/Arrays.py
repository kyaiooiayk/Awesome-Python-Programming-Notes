#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Data-structures" data-toc-modified-id="Data-structures-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Data structures</a></span></li><li><span><a href="#Arrays" data-toc-modified-id="Arrays-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Arrays</a></span></li><li><span><a href="#array.array-vs.-numpy.array" data-toc-modified-id="array.array-vs.-numpy.array-4"><span class="toc-item-num">4&nbsp;&nbsp;</span><code>array.array</code> vs. <code>numpy.array</code></a></span></li><li><span><a href="#When-arrays-are-used-over-a-list-in-Python" data-toc-modified-id="When-arrays-are-used-over-a-list-in-Python-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>When arrays are used over a list in Python</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Data structure: arrays
#
# </font>
# </div>

# # Data structures
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - A data structure is a storage that is used to store and organize data. It is a way of arranging data on a computer so that it can be accessed and updated efficiently.
# - A data structure is not only used for organizing the data. It is also used for processing, retrieving, and storing data.
#
# </font>
# </div>

# ![image.png](attachment:image.png)

# # Arrays
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - An array is a collection of items stored at contiguous memory locations.
# - The idea is to store multiple items of the same type together.
# - This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).
# - Each element can be uniquely identified by their index in the array (in a similar way as you could identify your friends by the step on which they were on in the above example).
#
# </font>
# </div>

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# # `array.array` vs. `numpy.array`
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - **Built-in array** module defines an object type which can efficiently represent an array of basic values: characters, integers, floating point numbers. Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is constrained. This means objects stored in the array are of a homogeneous(same) type. Type of objects to be stored in an array (built-in) is determined by typecode. Type codes are single characters. In array module `array(typecode [, initializer])` returns an array. Where initializer is optional, and if provided it must be a list, string or iterable.
#
# - **Numpy module** in python is generally used for matrix and array computations. While using the numpy module, built-in function ‘array’ is used to create an array. A prototype of array function is `array(object, dtype = None, copy = True, order = ‘K’, subok = False, ndmin = 0)`.
#
# </font>
# </div>

# In[14]:


import array as built_in

array1 = built_in.array("i")
array1.append(1)
array1.append(2)
array1.append(3)
print(array1)


# In[15]:


print(array1.typecode)
print(array1.itemsize)


# In[7]:


# if we try to append a float an error is thrown
array1.append(2.0)


# In[8]:


# Withouth providing the type explicitly
import numpy

array1 = numpy.array([1, 2, 3])
print(array1)


# In[9]:


# Providing the type explicitly
import numpy

array1 = numpy.array([1, 2, 3], int)
print(array1, type(array1[0]))


# In[11]:


# Providing the type explicitly
import numpy

array1 = numpy.array([1.1, 2, 3], int)
print(array1, type(array1[0]))


# <div class="alert alert-info">
# <font color=black>
#
# - Here floating point data was typecasted into int, with loss of data after the decimal point, when desired data type of array was int.
# - This is the major difference between the built-in array module and numpy array. A built-in array is quite strict about the storage of objects in itself. It permits only that type of data to be stored in itself, which has been specified strictly by the typecode. We could not store float value when typecode specified that, int data has to be stored in the built-in array. However numpy array is a bit tolerant or lenient in that matter, it will upcast or downcast and try to store the data at any cost. (Float was converted to int, even if that resulted in loss of data after decimal)
#
# </font>
# </div>

# # When arrays are used over a list in Python
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - We use arrays over lists in python as it requires less memory.
# - Arrays are faster than the list in python.
# - Arrays can directly handle arithmetic operations while lists cannot. So we use arrays over lists.
# - Arrays are preferred over lists for a longer sequence of data items.
#
# </font>
# </div>

# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - [Data Structures](https://www.geeksforgeeks.org/data-structures/?ref=shm)
# - [Array Data Structure](https://www.geeksforgeeks.org/array-data-structure/?ref=ghm)
# - [What is Array?](https://www.geeksforgeeks.org/what-is-array/)
# - [array.array versus numpy.array](https://stackoverflow.com/questions/111983/array-array-versus-numpy-array)
#
# </font>
# </div>

# In[ ]:
