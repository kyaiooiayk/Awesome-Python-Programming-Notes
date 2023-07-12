#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#General-rules" data-toc-modified-id="General-rules-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>General rules</a></span></li><li><span><a href="#Four-options" data-toc-modified-id="Four-options-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Four options</a></span><ul class="toc-item"><li><span><a href="#Positional-arguments" data-toc-modified-id="Positional-arguments-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Positional arguments</a></span></li><li><span><a href="#Mix-positional-and-default-arguments" data-toc-modified-id="Mix-positional-and-default-arguments-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Mix positional and default arguments</a></span></li><li><span><a href="#Arbitrary-positional-arguments" data-toc-modified-id="Arbitrary-positional-arguments-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Arbitrary positional arguments</a></span></li><li><span><a href="#Arbitrary-keyword-arguments" data-toc-modified-id="Arbitrary-keyword-arguments-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Arbitrary keyword arguments</a></span></li></ul></li><li><span><a href="#Using-*-between-arguments" data-toc-modified-id="Using-*-between-arguments-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Using <code>*</code> between arguments</a></span><ul class="toc-item"><li><span><a href="#Positional-only-parameters" data-toc-modified-id="Positional-only-parameters-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Positional only parameters</a></span></li><li><span><a href="#Keyword-only-arguments" data-toc-modified-id="Keyword-only-arguments-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Keyword only arguments</a></span></li><li><span><a href="#Mix" data-toc-modified-id="Mix-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Mix</a></span></li></ul></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Function arguments and all the available options
#
# </font>
# </div>

# # General rules
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Default arguments shoudl follow non-default arguments.
# - Keyword arguments should follow positional arguments.
# - All the keyword arguments passed must match one of the argumetns accepted by the function and their order is not important.
# - No argument should receive a value more than once.
# - Default arguments are optional arguments.
#
# </font>
# </div>

# # Four options
# <hr style = "border:2px solid black" ></hr>

# ## Positional arguments

# - With and withouth lambda function

# In[1]:


(lambda x, y, z: x + y + z)(1, 2, 3)


# In[9]:


def fun_1(x, y, z):
    print(x + y + z)


fun_1(1, 2, 3)


# ## Mix positional and default arguments

# In[10]:


(lambda x, y, z=3: x + y + z)(1, 2)


# In[12]:


def fun_1(x, y, z=3):
    print(x + y + z)


fun_1(1, 2, 3)
fun_1(1, 2)


# In[3]:


(lambda x, y, z=3: x + y + z)(1, y=2)


# In[14]:


def fun_1(x, y, z=3):
    print(x + y + z)


fun_1(1, y=2)


# ## Arbitrary positional arguments

# In[4]:


(lambda *args: sum(args))(1, 2, 3)


# In[25]:


def fun_1(*args):
    x, y, z = args
    print(x + y + z)


fun_1(1, 2, 3)


# ## Arbitrary keyword arguments

# In[26]:


(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)


# In[45]:


def fun_1(*kwarg):
    x, y, z = kwarg
    print(x + y + z)


fun_1(1, 2, 3)


def fun_1(*dummy):
    x, y, z = dummy
    print(x + y + z)


fun_1(1, 2, 3)


# # Using `*` between arguments
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - By default, arguments may be passed to a Python function either by position or explicitly by keyword. For **readability** and performance, it makes sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword.
#
# - To do so python allows you to use `/` and `*` which are optional. If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function:
#     - positional-only
#     - positional-or-keyword
#     - keyword-only
#
# </font>
# </div>

# ## Positional only parameters

# <div class="alert alert-info">
# <font color=black>
#
# - Positional-only parameters are placed before a `/` (forward-slash) in the function definition.
# - The `/` is used to logically separate the positional-only parameters from the rest of the parameters.
# - Parameters following the `/` may be positional-or-keyword or keyword-only.
#
# </font>
# </div>

# In[3]:


def add(a, b, /, c, d):
    return a + b + c + d


# In[4]:


print(add(3, 4, 5, 6))


# In[5]:


print(add(3, 4, c=1, d=2))


# In[6]:


# This will throw you an eror!
print(add(3, b=4, c=1, d=2))


# ## Keyword only arguments

# <div class="alert alert-info">
# <font color=black>
#
# - To mark parameters as keyword-only, place an `*` in the arguments list just before the first keyword-only parameter.
#
# </font>
# </div>

# In[7]:


def add(a, b, *, c, d):
    return a + b + c + d


# In[8]:


print(add(3, 4, c=1, d=2))


# In[10]:


# This will throw you an eror!
print(add(3, 4, 1, d=2))


# ## Mix

# <div class="alert alert-info">
# <font color=black>
#
# - In the below-given example, the function add has all three arguments
#     - `a,b` positional only arguments
#     - `c` positional or keyword arguments
#     - `d` keyword-only arguments
#
# </font>
# </div>

# In[11]:


def add(a, b, /, c, *, d):
    return a + b + c + d


# In[12]:


print(add(3, 4, 1, d=2))


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-danger">
# <font color=black>
#
# - Use **positional-only** if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning.
# - Use **positional-only** if you want to enforce the order of the arguments when the function is called.
# - Use **keyword-only** when names have meaning and the function definition is more understandable by being explicit with names.
# - Use **keyword-only** when you want to prevent users from relying on the position of the argument being passed.
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - [*args and **kwargs in Python](https://www.geeksforgeeks.org/args-kwargs-python/)
# - [`*` and `/` in between function arguments](https://levelup.gitconnected.com/5-types-of-arguments-in-python-function-definition-e0e2a2cafd29)
# - [5 Types of Arguments in Python Function Definitions](https://levelup.gitconnected.com/5-types-of-arguments-in-python-function-definition-e0e2a2cafd29)
#
# </font>
# </div>

# In[ ]:
