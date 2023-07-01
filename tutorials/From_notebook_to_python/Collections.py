#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-are-they?" data-toc-modified-id="What-are-they?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What are they?</a></span></li><li><span><a href="#Counter" data-toc-modified-id="Counter-3"><span class="toc-item-num">3&nbsp;&nbsp;</span><code>Counter</code></a></span></li><li><span><a href="#OrderedDict" data-toc-modified-id="OrderedDict-4"><span class="toc-item-num">4&nbsp;&nbsp;</span><code>OrderedDict</code></a></span></li><li><span><a href="#DefaultDict" data-toc-modified-id="DefaultDict-5"><span class="toc-item-num">5&nbsp;&nbsp;</span><code>DefaultDict</code></a></span></li><li><span><a href="#ChainMap" data-toc-modified-id="ChainMap-6"><span class="toc-item-num">6&nbsp;&nbsp;</span><code>ChainMap</code></a></span></li><li><span><a href="#NamedTuple" data-toc-modified-id="NamedTuple-7"><span class="toc-item-num">7&nbsp;&nbsp;</span><code>NamedTuple</code></a></span></li><li><span><a href="#Deque" data-toc-modified-id="Deque-8"><span class="toc-item-num">8&nbsp;&nbsp;</span><code>Deque</code></a></span></li><li><span><a href="#UserDict" data-toc-modified-id="UserDict-9"><span class="toc-item-num">9&nbsp;&nbsp;</span><code>UserDict</code></a></span></li><li><span><a href="#UserList" data-toc-modified-id="UserList-10"><span class="toc-item-num">10&nbsp;&nbsp;</span><code>UserList</code></a></span></li><li><span><a href="#UserString" data-toc-modified-id="UserString-11"><span class="toc-item-num">11&nbsp;&nbsp;</span><code>UserString</code></a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-12"><span class="toc-item-num">12&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-13"><span class="toc-item-num">13&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Collections
#
# </font>
# </div>

# # What are they?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Collections provide different types of containers.
# - A Container is an object that is used to store different objects and provide a way to access the contained objects and iterate over them.
# - Some of the most known built-in containers are Tuple, List, Dictionary, but there are more and they reside inside the `collections` module:
#     - `Counters`
#     - `OrderedDict`
#     - `DefaultDict`
#     - `ChainMap`
#     - `NamedTuple`
#     - `DeQue`
#     - `UserDict`
#     - `UserList`
#     - `UserString`
#
# </font>
# </div>

# # `Counter`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - A counter is a sub-class of the dictionary.
# - It is used to keep the count of the elements in an iterable in the form of an unordered dictionary where the key represents the element in the iterable and value represents the count of that element in the iterable.
# - Syntax: `class collections.Counter([iterable-or-mapping])`
#
# </font>
# </div>

# In[1]:


from collections import Counter


# In[2]:


# Initialised with sequence of items
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))


# In[4]:


# Initialised with dictionary
print(Counter({'A': 3, 'B': 5, 'C': 2}))


# In[5]:


# Initialised with keyword arguments
print(Counter(A=3, B=5, C=2))


# # `OrderedDict`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - An OrderedDict is also a sub-class of dictionary but unlike dictionary, it **remembers** the order in which the keys were inserted.
# - While deleting and re-inserting the same key will push the key to the last to maintain the order of insertion of the key.
#
# </font>
# </div>

# In[6]:


from collections import OrderedDict


# In[14]:


print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items():
    print(key, value)

# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items():
    print(key, value)


# In[11]:


print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items():
    print(key, value)


# # `DefaultDict`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - A `DefaultDict` is also a sub-class to dictionary.
# - It is used to provide some default values for the key that does not exist and never raises a KeyError.
#
# </font>
# </div>

# In[18]:


from collections import defaultdict


# In[21]:


# Dictionary with values as int
d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

for i in L:

    d[str(i)] = i

print(d)


# In[23]:


# Dictionary with values as list
d = defaultdict(list)

for i in range(5):
    d[str(i)].append(i)

print("Dictionary with values as list:")
print(d)


# # `ChainMap`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - A `ChainMap` encapsulates many dictionaries into a single unit and returns a list of dictionaries.
# - Syntax: `class collections.ChainMap(dict1, dict2)`
#
# </font>
# </div>

# In[24]:


from collections import ChainMap


d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)

print(c)


# In[25]:


import collections

# initializing dictionaries
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
dic3 = {'f': 5}

# initializing ChainMap
chain = collections.ChainMap(dic1, dic2)

# printing chainMap
print("All the ChainMap contents are : ")
print(chain)

# using new_child() to add new dictionary
chain1 = chain.new_child(dic3)

# printing chainMap
print("Displaying new ChainMap : ")
print(chain1)


# # `NamedTuple`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - A `NamedTuple` returns a tuple object with names for each position which the ordinary tuples lack. For example, consider a tuple names student where the first element represents name, second represents name and the third element represents the DOB.
# - Suppose for calling name instead of remembering the index position you can actually call the element by using the name argument, then it will be really easy for accessing tuples element. This functionality is provided by the NamedTuple.
#
# - `Syntax: class collections.namedtuple(typename, field_names)`
#
# </font>
# </div>

# In[26]:


from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)


# In[27]:


# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# initializing iterable
li = ['Manjeet', '19', '411997']

# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is : ")
print(Student._make(li))

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is : ")
print(S._asdict())


# # ` Deque`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - `Deque` (Doubly Ended Queue) is the optimised list for quicker append and pop operations from both sides of the container. It provides O(1) time complexity for append and pop operations as compared to list with O(n) time complexity.
# - Elements in deque can be inserted from both ends. To insert the elements from right `append()` method is used and to insert the elements from the left `appendleft()` method is used.
# - Elements can also be removed from the deque from both the ends. To remove elements from right use `pop()` method and to remove elements from the left use `popleft()` method.
# - Syntax: `class collections.deque(list)`
#
# </font>
# </div>

# In[29]:


from collections import deque

# Declaring deque
queue = deque(['name', 'age', 'DOB'])

print(queue)


# In[30]:


# initializing deque
de = deque([1, 2, 3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("The deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("The deque after appending at left is : ")
print(de)b


# In[31]:


# initializing deque
de = deque([6, 1, 2, 3, 4])

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print("The deque after deleting from right is : ")
print(de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print("The deque after deleting from left is : ")
print(de)


# # `UserDict`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - `UserDict` is a dictionary-like container that acts as a wrapper around the dictionary objects.
# - This container is used when someone wants to create their own dictionary with some modified or new functionality.
# - `Syntax: class collections.UserDict([initialdata])`
#
# </font>
# </div>

# In[34]:


from collections import UserDict


# Creating a Dictionary where
# deletion is not allowed
class MyDict(UserDict):

    # Function to stop deletion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from
    # dictionary
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop popitem
    # from Dictionary
    def popitem(self, s=None):
        raise RuntimeError("Deletion not allowed")


# In[35]:


# Driver's code
d = MyDict({'a': 1,
            'b': 2,
            'c': 3})

d.pop(1)


# # `UserList`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - `UserList` is a list like container that acts as a wrapper around the list objects. This is useful when someone wants to create their own list with some modified or additional functionality.
# - Syntax: `class collections.UserList([list])`
#
# </font>
# </div>

# In[36]:


from collections import UserList


# Creating a List where
# deletion is not allowed
class MyList(UserList):

    # Function to stop deletion
    # from List
    def remove(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from
    # List
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")


# In[37]:


# Driver's code
L = MyList([1, 2, 3, 4])

print("Original List")

# Inserting to List"
L.append(5)
print("After Insertion")
print(L)

# Deleting From List
L.remove()


# # `UserString`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - `UserString` is a string like container and just like UserDict and UserList it acts as a wrapper around string objects. It is used when someone wants to create their own strings with some modified or additional functionality.
# - `Syntax: class collections.UserString(seq)`
#
# </font>
# </div>

# In[40]:


from collections import UserString

# Creating a Mutable String
class Mystring(UserString):

    # Function to append to
    # string
    def append(self, s):
        self.data += s

    # Function to remove from
    # string
    def remove(self, s):
        self.data = self.data.replace(s, "")


# In[41]:


# Driver's code
s1 = Mystring("Geeks")
print("Original String:", s1.data)

# Appending to string
s1.append("s")
print("String After Appending:", s1.data)

# Removing from string
s1.remove("e")
print("String after Removing:", s1.data)


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-danger">
# <font color=black>
#
# - Write readable and explicit code using `namedtuple`
# - Build efficient queues and stacks using `deque`
# - Count objects efficiently using `Counter`
# - Handle missing dictionary keys with `defaultdict`
# - Remember the insertion order of keys with `OrderedDict`
# - Chain multiple dictionaries in a single view with `ChainMap`
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://realpython.com/python-collections-module/
# - https://www.geeksforgeeks.org/python-collections-module/
#
# </font>
# </div>

# In[ ]:
