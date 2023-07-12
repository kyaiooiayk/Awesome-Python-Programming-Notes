#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Definitions" data-toc-modified-id="Definitions-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Definitions</a></span></li><li><span><a href="#Positional-arguments" data-toc-modified-id="Positional-arguments-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Positional arguments</a></span><ul class="toc-item"><li><span><a href="#Exaxmple-#1" data-toc-modified-id="Exaxmple-#1-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Exaxmple #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Example #2</a></span></li></ul></li><li><span><a href="#Keyword-arguments" data-toc-modified-id="Keyword-arguments-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Keyword arguments</a></span><ul class="toc-item"><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Example #2</a></span></li></ul></li><li><span><a href="#Partial-unpacking" data-toc-modified-id="Partial-unpacking-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Partial unpacking</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** args and kwargs
#
# </font>
# </div>

# # Definitions
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Python has a very convenient "keyword argument unpacking syntax" (often referred to as **"splat"-operators**). This is particularly useful, if we want to define a function that can take a arbitrary number of input arguments.
# - There are two of them:
#     - `*args`   is used for specifying an unknown number of *positional* arguments.
#     - `**kwargs` is used for specifying an unknown number of *keyword*    arguments. Double star allows us to pass through keyword arguments (and any number of them)
#
# </font>
# </div>

# # Positional arguments
# <hr style="border:2px solid black"> </hr>

# ## Exaxmple #1

# In[2]:


def example_args(*dummy):
    for a in dummy:
        print(a)


# In[3]:


example_args([1, 2, 3, 4])


# In[4]:


example_args([1, 2, 3, 4, 5], [1, 2])


# ## Example #2

# In[1]:


def a_func(*args):
    print("type of args:", type(args))
    print("args contents:", args)
    print("1st argument:", args[0])


a_func(0, 1, "a", "b", "c")


# # Keyword arguments
# <hr style="border:2px solid black"> </hr>

# ## Example #1

# In[24]:


def example_kargs(**dummy):
    for key, values in dummy.items():
        print(key, values)


# In[26]:


example_kargs(a=3, b=1)


# In[27]:


example_kargs(a=3, b=1, c=3)


# ## Example #2

# In[2]:


def b_func(**kwargs):
    print("type of kwargs:", type(kwargs))
    print("kwargs contents: ", kwargs)
    print("value of argument a:", kwargs["a"])


b_func(a=1, b=2, c=3, d=4)


# # Partial unpacking
# <hr style="border:2px solid black"> </hr>

# In[3]:


val1, *vals = [1, 2, 3, 4, 5]
print("val1:", val1)
print("vals:", vals)


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://www.kdnuggets.com/2021/08/data-scientist-guide-efficient-coding-python.html
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/not_so_obvious_python_stuff.ipynb?create=1
#
# </font>
# </div>
