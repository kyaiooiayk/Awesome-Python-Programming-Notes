#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Data-structures" data-toc-modified-id="Data-structures-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Data structures</a></span></li><li><span><a href="#What-is-a-Stack?" data-toc-modified-id="What-is-a-Stack?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>What is a Stack?</a></span></li><li><span><a href="#Stack-implemented-in-python" data-toc-modified-id="Stack-implemented-in-python-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Stack implemented in python</a></span></li><li><span><a href="#Stack-implementation-from-scratch" data-toc-modified-id="Stack-implementation-from-scratch-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Stack implementation from scratch</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Data structure: stacks
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

# # What is a Stack?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - A stack is an array or list structure of function calls and parameters used in modern computer programming and CPU architecture.
# - The stack is also known as "Last In First Out (LIFO)". The one at the bottom was the first one put down but when you are picking up plates from the stack it is the last one you get to.
# - When a function is called, the address of the next instruction is pushed onto the stack. 
# - When the function exits, the address is popped off the stack and execution continues at that address. 
# 
# </font>
# </div>

# # Stack implemented in python
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Stack is a data structure where the last element added is the first element retrieved -> **last-in, first-out**. 
# - List can be very easily used as stacked.
# 
# </font>
# </div>

# In[2]:


stack = [1,2,3]
stack.append(4)
stack.append(5)
stack


# In[3]:


# the first to be removed is the the last that was added
stack.pop()


# In[4]:


stack


# # Stack implementation from scratch
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - A stack is an array or list structure of function calls and parameters used in modern computer programming and CPU architecture.
# - The stack is also known as **"Last In First Out (LIFO)"**. The one at the bottom was the first one put down but when you are picking up plates from the stack it is the last one you get to.
# - When a function is called, the address of the next instruction is pushed onto the stack. 
# - When the function exits, the address is popped off the stack and execution continues at that address. 
# - **What are they used for?** This concept is used for evaluating expressions and syntax parsing, scheduling algortihms/routines, etc. 
#   
# </font>
# </div>

# In[2]:


class Stack:
    """
    Last In First Out (LIFO)
    creates a new stack that is empty,
    assumes that the end of the list will hold 
    the top element of the stack
    
    References
    ----------
    https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        For sequences, (strings, lists, tuples), 
        use the fact that empty sequences are false
        http://stackoverflow.com/questions/53513/best-way-to-check-if-a-list-is-empty
        """
        return not self.items

    def push(self, item):
        """adds a new item to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        """
        removes the top item from the stack,
        popping an empty stack (list) will result in an error
        """
        return self.items.pop()

    def peek(self):
        """returns the top item from the stack but does not remove it"""
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# In[6]:


s = Stack()
print(s.is_empty())
s.push(4)
s.push(5)
print(s.is_empty())
print(s.pop())
print(s.peek())


# <div class="alert alert-info">
# <font color=black>
# 
# - Stacks can be implemented using lists in Python. 
# - When you add elements to a stack, it is known as a push operation, whereas when you remove or delete an element it is called a pop operation
# 
# </font>
# </div

# In[8]:


# Bottom -> 1 -> 2 -> 3 -> 4 -> 5 (Top)
stack = [1,2,3,4,5] 
stack.append(6) # Bottom -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 (Top)
print(stack)

stack.pop() # Bottom -> 1 -> 2 -> 3 -> 4 -> 5 (Top)
stack.pop() # Bottom -> 1 -> 2 -> 3 -> 4 (Top)
print(stack)


# Write a function rev_string(mystr) that uses a stack to reverse the characters in a string.

# In[4]:


def rev_string(string):
    s = Stack()
    for char in string:
        s.push(char)

    rev_str = ''
    while not s.is_empty():
        rev_str += s.pop()

    return rev_str

test = 'apple'    
rev_string(test)


# Check for balance parenthesis.

# In[5]:


def match(top, char):
    if top == '[' and char == ']':
        return True
    
    if top == '{' and char == '}':
        return True
    
    if top == '(' and char == ')':
        return True
    
    return False

def check_paren(text):
    """confirm balance parenthesis in operations"""
    # define the set of opening
    # and closing brackets
    opens = '([{'
    close = ')]}'
    
    s = Stack()
    balanced = True
    for char in text:
        if char in opens:
            s.push(char)

        if char in close:
            # if a closing bracket appeared
            # without a opening bracket
            if s.is_empty():
                balanced = False
                break
            else:
                # if there is a mismatch between the
                # closing and opening bracket
                top = s.pop()
                if not match(top, char):
                    balanced = False
                    break

    if balanced and s.is_empty():
        return True
    else:
        return False


# In[6]:


test1 = '{{([][])}()}'
balanced = check_paren(test1)
print(balanced)

test2 = '{test}'
balanced = check_paren(test2)
print(balanced)

test3 = ']'
balanced = check_paren(test3)
print(balanced)


# Convert numbers into binary representation.

# In[7]:


def convert_binary(num):
    """assumes positive number is given"""
    s = Stack()
    while num > 0:
        remainder = num % 2
        s.push(remainder)
        num = num // 2

    binary_str = ''
    while not s.is_empty():
        binary_str += str(s.pop())
        
    return binary_str


# In[8]:


num = 42
binary_str = convert_binary(num)
binary_str


# Convert operators from infix to postfix.

# In[9]:


import string

def infix_to_postfix(formula):
    """assume input formula is space-delimited"""
    s = Stack()
    output = [] 
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    operand = string.digits + string.ascii_uppercase
    
    for token in formula.split():
        if token in operand:
            output.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            top = s.pop()
            while top != '(':
                output.append(top)
                top = s.pop()
        else:
            while (not s.is_empty()) and prec[s.peek()] > prec[token]:
                top = s.pop()
                output.append(top)
            s.push(token)

    while not s.is_empty():
        top = s.pop()
        output.append(top)
    
    postfix = ' '.join(output)
    return postfix


# In[10]:


formula = 'A + B * C'
output = infix_to_postfix(formula)
output


# In[11]:


formula = '( A + B ) * C'
output = infix_to_postfix(formula)
output


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
# - https://www.thoughtco.com/definition-of-stack-in-programming-958162 
# 
# </font>
# </div>

# In[ ]:




