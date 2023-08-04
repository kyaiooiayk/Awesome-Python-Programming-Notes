#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Data-structures" data-toc-modified-id="Data-structures-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Data structures</a></span></li><li><span><a href="#Queue-implementation-in-python" data-toc-modified-id="Queue-implementation-in-python-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Queue implementation in python</a></span></li><li><span><a href="#Priority-queue" data-toc-modified-id="Priority-queue-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Priority queue</a></span></li><li><span><a href="#Queue-implementation-from-scratch" data-toc-modified-id="Queue-implementation-from-scratch-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Queue implementation from scratch</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Data structure: queues
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

# # Queue implementation in python
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - **Stack** was last-in first-out.
# - **Queue** is the opposite of stack, meaning first-in first-out.
# - List are not **efficiently** used as a queue, because all the other elements have to be shifted by one.
# - To implement a queue use `collections.deque` which was designed to have fast append and pops from both ends.
# 
# </font>
# </div>

# In[2]:


from collections import deque
a = ["Eric", "John", "Michael"]
queue = deque(a)
queue.append("Terry")
print(queue)
queue.append("Graham")
print(queue)
print(queue.popleft())


# In[3]:


# Removes the right-most element
print(queue.pop())
print(queue)


# # Priority queue
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - We can think of priority queue as a modified queue: instead of retrieving the next element by insertion time, it retrieves the highest-priority element. The priority of individual elements is decided by the ordering applied to their keys.
# 
# - Priority queues are commonly used for dealing with scheduling problems. High-priority tasks on the system should take precedence over lower-priority tasks. By organizing pending tasks in a priority queue that uses the task urgency as the key, the task scheduler can allow the highest-priority tasks to run first.
# 
# - Let’s take a look at how we can implement priority queues in Python using built-in data structures or data structures that ship with Python’s standard library.
# 
# </font>
# </div>

# In[1]:


from queue import PriorityQueue

q = PriorityQueue()
q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while not q.empty():
    # note that apart from returning
    # the item from the queue, it will
    # also remove it from the queue
    next_item = q.get()
    print(next_item)


# <div class="alert alert-info">
# <font color=black>
# 
# As we can infer from the output, prioriy queue stores the elements by its priority, in this case the first element in the tuple. After from sorting primitive types such as integers, we can also sort objects that we've defined. To perform sorting on custom objects we need to implement the dunder methods for all 6 comparisons.
# 
# | Operator | Method     |
# |----------|------------|
# | ==       | ``__eq__`` |
# | !=       | ``__ne__`` |
# | <        | ``__le__`` |
# | <=       | ``__le__`` |
# | >        | ``__gt__`` |
# | >=       | ``__ge__`` |
# 
# </font>
# </div>

# In[2]:


class Skill:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        
    def __eq__(self, other):
        return self.priority == other.priority

    def __ne__(self, other):
        return self.priority != other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __ge__(self, other):
        return self.priority >= other.priority

    def __repr__(self):
        return '{}: {}'.format(self.description, self.priority)


# In[3]:


q = PriorityQueue()
q.put(Skill(5, 'R'))
q.put(Skill(10, 'Python'))
q.put(Skill(1, 'Java'))

while not q.empty():
    next_item = q.get()
    print(next_item)


# # Queue implementation from scratch
# <hr style="border:2px solid black"> </hr>

# Following the material, [Online book: What is a Queue?](http://interactivepython.org/runestone/static/pythonds/BasicDS/WhatIsaQueue.html)

# In[12]:


class Queue:
    """
    First In First Out (FIFO)
    assume rear is at position 0 in the list,
    so the last element of the list is the front
    """

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not self.items
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)


# In[13]:


q = Queue()
q.enqueue(4)
q.enqueue(3)
q.enqueue(10)

# 4 is the first one added, hence it's the first
# one that gets popped
print(q.dequeue())
print(q.size())


# > From [Python Documentation: Using Lists as Queues](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues)
# >
# > Although the queue functionality can be implemented using a list, it is not efficient for this  purpose. Because doing inserts or pops from the beginning of a list is slow (all of the other elements have to be shifted by one).
# 
# We instead use `deque`. It is designed to have fast appends and pops from both ends.
# 
# Implement the palindrome checker to check if a given word is a palindrom. A palindrome is a string that reads the same forward and backward, e.g. radar.

# In[14]:


from collections import deque

def check_palindrome(word):
    equal = True
    queue = deque([token for token in word])
    while len(queue) > 1 and equal:
        first = queue.popleft()
        last = queue.pop()
        if first != last:
            equal = False

    return equal


# In[15]:


test = 'radar'
check_palindrome(test)


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://www.thoughtco.com/definition-of-stack-in-programming-958162 
# - https://runestone.academy/runestone/books/published/pythonds/BasicDS/WhatisaStack.html
# - https://github.com/ethen8181/machine-learning/blob/master/python/algorithms/basic_data_structure.ipynb
# - https://www.datacamp.com/community/tutorials/data-structures-python
# - [Data Structures](https://www.geeksforgeeks.org/data-structures/?ref=shm)
#     
# </font>
# </div>

# In[ ]:




