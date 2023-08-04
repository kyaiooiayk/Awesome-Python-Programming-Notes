#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-a-singly-linked-list?" data-toc-modified-id="What-is-a-singly-linked-list?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is a singly linked list?</a></span></li><li><span><a href="#Create-a-node" data-toc-modified-id="Create-a-node-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Create a node</a></span></li><li><span><a href="#Create-a-singly-linked-list" data-toc-modified-id="Create-a-singly-linked-list-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Create a singly linked list</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Linked list
# 
# </font>
# </div>

# # What is a singly linked list?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer.
# - Python **does not** have linked lists in its standard library, but this can be implemented using the concept of nodes.
# - We are goign to concentrate on a type of linked lists known as **singly linked lists** where there is only one link between any two data elements. 
# - Here we are going to create such a list along with some additional methods to insert, update and remove elements from the list.
# - **Why?** Linked lists are often used because of their efficient insertion and deletion. They can be used to implement stacks, queues, and other abstract data types.
# 
# </font>
# </div>

# # Create a node
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - Each node contains a value and a reference (also known as a pointer) to the next node. 
# - The last node, has a reference equal to `None`, it means the list is at its end. 
# 
# </font>
# </div>

# In[1]:


class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None

# Create 3 nodes
e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")


# In[6]:


e2.data_val


# In[8]:


e2.next_val == None


# # Create a singly linked list
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Singly linked lists can be traversed in only forward direction starting form the first data element.
# - We simply print the value of the next data element by assigning the pointer of the next node to the current data element.
# 
# </font>
# </div>

# In[11]:


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.data_val)
            printval = printval.next_val


list_ = SLinkedList()
list_.headval = e1
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list_.headval.next_val = e2

# Link second Node to third node
e2.next_val = e3

list_.listprint()


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm?key=node
# 
# </font>
# </div>

# In[ ]:




