#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Overwriting" data-toc-modified-id="Overwriting-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Overwriting</a></span></li><li><span><a href="#Overloading-=-Overriding" data-toc-modified-id="Overloading-=-Overriding-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Overloading = Overriding</a></span></li><li><span><a href="#Operator-overloading" data-toc-modified-id="Operator-overloading-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Operator overloading</a></span></li><li><span><a href="#Overload-operator-in-pandas" data-toc-modified-id="Overload-operator-in-pandas-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Overload operator in pandas</a></span></li><li><span><a href="#But-how-an-operator-overloading-work?" data-toc-modified-id="But-how-an-operator-overloading-work?-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>But how an operator overloading work?</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Overwriting vs. Overloading vs. Overriding
# 
# </font>
# </div>

# # Imports
# <hr style="border:2px solid black"> </hr>

# In[2]:


import numpy


# # Overwriting
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - If we overwrite a function, the original function will be gone. 
# - The function will be redefined. 
# - This process has nothing to do with object orientation or inheritance.
# 
# </font>
# </div>

# In[1]:


def f(x):
    return x + 2
f(3)


# In[3]:


# By using the same funciton name the previous one will be gone
def f(x):
    return x + 3
f(3)


# # Overloading = Overriding
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - It is possible to simulate the overloading behavious of C++ in Python.
# - This is done with a default parameter.
# - Essentially we are changing function behaviour.
# - The `*` operator can be used as a more general apporach for a family of functions with 1,2,3 or more parameters.
# 
# </font>
# </div>

# In[6]:


def F(n, m = None):
    if m:
        return n + m + 1
    else:
        return n + 1
print(F(3), F(3, 2))    


# In[9]:


def F(*x):
    if len(x) == 1:
        return x[0]+-1
    if len(x) == 2:
        return x[0]+x[1]+1
    else:
        return x[0]+x[1]+x[2]+1
print(F(3), F(3, 2), F(1,2,3))  


# # Operator overloading
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - Operator overloading is a feature in Python that allows the same operator to have different meaning according to the context is called.
# - **An example?** For example, the **+** operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.
# - **In practice?** The designers of lists decided that adding them to numbers wasn't allowed. The designers of numpy arrays went a different way (adding the number to each element of the array).
# 
# </font>
# </div>

# In[1]:


# The expression. below throws an error
[3, 4, 1, 2, 2, 1] + 10


# In[6]:


# The exppression below will not throw an error instead!
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)
print(rolls + 10)


# # Overload operator in pandas
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - The example above features something like 5 different overloaded operators.  
# - Get the rows with population over 1m in South America
# 
# </font>
# </div>

# In[ ]:


df[(df['population'] > 10**6) & (df['continent'] == 'South America')]


# # But how an operator overloading work?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - When Python programmers want to define how operators behave on their types, they do so by implementing methods with special names beginning and ending with 2 underscores such as
# - This is also valid for our **+** operator. 
# - The way it is implemented internally is via __add__.
# 
# </font>
# </div>

# In[7]:


dir(list)


# In[8]:


a = [1,2]
b = [2,3]


# In[9]:


a + b


# In[10]:


a.__add__(b) 


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - https://www.programiz.com/python-programming/operator-overloading 
# - https://www.kaggle.com/colinmorris/working-with-external-libraries
#     
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[1]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv -m')


# In[ ]:




