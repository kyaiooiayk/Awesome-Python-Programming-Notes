#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Data-structures" data-toc-modified-id="Data-structures-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Data structures</a></span></li><li><span><a href="#Unordered-Linked-List" data-toc-modified-id="Unordered-Linked-List-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Unordered Linked List</a></span></li><li><span><a href="#Ordered-(Linked)List" data-toc-modified-id="Ordered-(Linked)List-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Ordered (Linked)List</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Data structure: linked list
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

# # Unordered Linked List
# <hr style="border:2px solid black"> </hr>
#

# In[16]:


class Node:
    """
    node must contain the list item itself (data)
    node must hold a reference that points to the next node
    """

    def __init__(self, initdata):
        # None will denote the fact that there is no next node
        self._data = initdata
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, newdata):
        self._data = newdata

    def set_next(self, newnext):
        self._next = newnext


# In[17]:


class UnorderedList:
    def __init__(self):
        """
        we need identify the position for the first node,
        the head, When the list is first initialized
        it has no nodes
        """
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        """
        takes data, initializes a new node with the given data
        and add it to the list, the easiest way is to
        place it at the head of the list and
        point the new node at the old head
        """
        node = Node(item)
        node.set_next(self.head)
        self.head = node
        return self

    def size(self):
        """
        traverse the linked list and keep a count
        of the number of nodes that occurred
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        """
        goes through the entire list to check
        and see there's a matched value
        """
        found = False
        current = self.head
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def delete(self, item):
        """
        traverses the list in the same way that search does,
        but this time we keep track of the current node and the previous node.
        When delete finally arrives at the node it wants to delete,
        it looks at the previous node and resets that previous node’s pointer
        so that, rather than pointing to the soon-to-be-deleted node,
        it will point to the next node in line;
        this assumes item is in the list
        """
        found = False
        previous = None
        current = self.head
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        # note this assumes the item is in the list,
        # if not we'll have to write another if else statement
        # here to handle it
        if previous is None:
            # handle cases where the first item is deleted,
            # i.e. where we are modifying the head
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return self

    def __repr__(self):
        value = []
        current = self.head
        while current is not None:
            data = str(current.get_data())
            value.append(data)
            current = current.get_next()

        return "[" + ", ".join(value) + "]"


# In[18]:


mylist = UnorderedList()
mylist.add(31)
mylist.add(17)
mylist.add(91)
mylist.delete(17)
print(mylist.search(35))
mylist


# # Ordered (Linked)List
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - As the name suggests, compared to unordered linkedlist, the elements will always be ordered for a ordered linked list.
# - The `is_empty` and `size` method are exactly the same as the unordered linkedlist as they don't have anything to do with the actual item in the list.
#
# </font>
# </div>

# In[19]:


class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        """
        takes data, initializes a new node with the given data
        and add it to the list while maintaining relative order
        """

        # stop when the current node is larger than the item
        stop = False
        previous = None
        current = self.head
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        # check whether it will be added to the head
        # or somewhether in the middle and handle
        # both cases
        node = Node(item)
        if previous is None:
            node.set_next(self.head)
            self.head = node
        else:
            previous.set_next(node)
            node.set_next(current)

        return self

    def search(self, item):
        """
        goes through the entire list to check
        and see there's a matched value, but
        we can stop if the current node's value
        is greater than item since the list is sorted
        """
        stop = False
        found = False
        current = self.head
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def __repr__(self):
        value = []
        current = self.head
        while current is not None:
            data = str(current.get_data())
            value.append(data)
            current = current.get_next()

        return "[" + ", ".join(value) + "]"


# In[20]:


mylist = OrderedList()
mylist.add(17)
mylist.add(77)
mylist.add(31)
print(mylist.search(31))
mylist


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://www.thoughtco.com/definition-of-stack-in-programming-958162
# - https://runestone.academy/runestone/books/published/pythonds/BasicDS/WhatisaStack.html
# - https://github.com/ethen8181/machine-learning/blob/master/python/algorithms/basic_data_structure.ipynb
# - https://www.datacamp.com/community/tutorials/data-structures-python
# - [Implementing an Ordered List](http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganOrderedList.html)
# - [Online book: Lists](http://interactivepython.org/runestone/static/pythonds/BasicDS/Lists.html)
# - [Blog: Implementing a Singly Linked List in Python](https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/#)
#
# </font>
# </div>

# In[ ]:
