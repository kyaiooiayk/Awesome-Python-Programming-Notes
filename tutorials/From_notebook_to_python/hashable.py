#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Why-hashing?" data-toc-modified-id="Why-hashing?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Why hashing?</a></span></li><li><span><a href="#Built-In-data-structures" data-toc-modified-id="Built-In-data-structures-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Built-In data structures</a></span></li><li><span><a href="#Hash-table-vs.-hashmap" data-toc-modified-id="Hash-table-vs.-hashmap-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Hash table vs. hashmap</a></span></li><li><span><a href="#To-be-(hashable)-or-not-to-be" data-toc-modified-id="To-be-(hashable)-or-not-to-be-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>To be (hashable) or not to be</a></span></li><li><span><a href="#Lists" data-toc-modified-id="Lists-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Lists</a></span></li><li><span><a href="#Tuples" data-toc-modified-id="Tuples-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Tuples</a></span></li><li><span><a href="#Sets" data-toc-modified-id="Sets-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Sets</a></span></li><li><span><a href="#Frozensets" data-toc-modified-id="Frozensets-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Frozensets</a></span></li><li><span><a href="#References" data-toc-modified-id="References-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Hashable
# 
# </font>
# </div>

# # Why hashing?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - A hash function takes a group of characters (called a key) and maps it to a value of a certain length (called a hash value or hash). 
# - The hash value is representative of the original string of characters, but is normally smaller than the original.
# - **Motivation?** Hashing is done for indexing and locating items in databases because it is easier to find the shorter hash value than the longer string.
# - **Essentially**: Hashing is used with a database to enable items to be retrieved more quickly.
# - Hash tables or hash maps in Python are implemented through the built-in dictionary data type.
#     
# </font>
# </div>

# # Built-In data structures
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# -  Python also has several built-in compound types
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

# # Hash table vs. hashmap
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Where does the confusion come from? In normal programming jargon, a hash map and a hash table are the same thing. However in Java's collection types hashmaps are synchronised so they can only be operated on by one task/function at a time while hashtables can be operated on by multiple threads at once.
# 
# | Hash table | Hash map   |
# |-----------|---------------------------|
# | synchronised | non-synchronised |
# | fast | slow |
# |Allows one null key and more than one null values | Does not allows null keys or values |
# 
# - Python's dict type is more analogous (if we really want to forcely them against Java collections) to HashMap (in that it doesn't inherently provide any synchronization guarantees). If you want synchronization, you need to handle it yourself (threading.Lock with a with statement makes this pretty easy).
#     
# </font>
# </div>

# # To be (hashable) or not to be
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - An object that is hashable is an object for which a hash can be computed, hence, hash-able.
# 
# - A hash is an integer that the built-in function hash computes to help with fast operations with dictionaries,
# e.g. key lookups.
# 
# - The built-in function knows how to work with some types of objects, and not with others. The built-in function
# hash dictates what can and cannot be a dictionary key: if it is hashable, it can be a dictionary key; if it isn’t hashable, it cannot be a dictionary key.
#     
# </font>
# </div>

# # Lists
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `lists` are mutable and **unhashable**, and hence they cannot be dictionary keys. 
# 
# - Attempting to use a list as a dictionary key raises an error.
# 
#     
# </font>
# </div>

# In[1]:


d = {}
d[[1, 2, 3]] = 73


# # Tuples
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `tuples` is immutable, and immutable objects can generally be made **hashable**. 
# 
# - A tuple can be used as a dictionary key.
#     
# </font>
# </div>

# In[2]:


d = {}
d[(1, 2, 3)] = 73
d


# # Sets
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `sets` are mutable so they are  **unhashable**. 
# - A set cannot be a dictionary key.
#     
# </font>
# </div>

# In[4]:


d = {}
groceries = {'cheese', 'milk', 'chocolate'}
d[groceries] = 73       


# # Frozensets
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `frozensets` are not mutable so they are **hashable**.
# 
# </font>
# </div>

# In[7]:


groceries = {'cheese', 'milk', 'chocolate'}
d[frozenset(groceries)] = 73
d


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - https://mathspp.com/blog/pydonts
# - https://www.techopedia.com/definition/19744/hash-function 
# - https://stackoverflow.com/questions/63910315/whats-the-difference-between-a-hashmap-and-a-hashtable-in-python
#     
# </font>
# </div>

# In[ ]:




