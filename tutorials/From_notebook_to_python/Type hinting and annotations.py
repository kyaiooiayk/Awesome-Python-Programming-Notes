#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-are-function-annotations?" data-toc-modified-id="What-are-function-annotations?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What are function annotations?</a></span></li><li><span><a href="#Difference-btw-type-hinting-and-annotation?" data-toc-modified-id="Difference-btw-type-hinting-and-annotation?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Difference btw type hinting and annotation?</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#Example-#3" data-toc-modified-id="Example-#3-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Example #3</a></span></li><li><span><a href="#Example-#4" data-toc-modified-id="Example-#4-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Example #4</a></span></li><li><span><a href="#Example-#5" data-toc-modified-id="Example-#5-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Example #5</a></span></li><li><span><a href="#Example-of-various-annotations" data-toc-modified-id="Example-of-various-annotations-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Example of various annotations</a></span><ul class="toc-item"><li><span><a href="#Union-and-|" data-toc-modified-id="Union-and-|-9.1"><span class="toc-item-num">9.1&nbsp;&nbsp;</span><code>Union</code> and <code>|</code></a></span></li><li><span><a href="#Optional" data-toc-modified-id="Optional-9.2"><span class="toc-item-num">9.2&nbsp;&nbsp;</span><code>Optional</code></a></span></li></ul></li><li><span><a href="#List-vs.-list-in-type-hinting" data-toc-modified-id="List-vs.-list-in-type-hinting-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>List vs. <code>list</code> in type hinting</a></span></li><li><span><a href="#References" data-toc-modified-id="References-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-12"><span class="toc-item-num">12&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Function annotation
# 
# </font>
# </div>

# # What are function annotations?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Before we start keep in mind that:
#     - **Static typed** — performs type checking at compile-time and requires datatype declarations.
#     - **Dynamic typed** — performs type checking at runtime and does not require datatype declarations.
# - Function annotations are covered in PEP 3107 and they allow you to attach a metadata string to various types of object.
# - They are generally used to attach metadata to functions describing their parameters and return values.
# - The symbol `->` marks the return function annotation.
# - The main way to add type hints is using annotations.
#     
# </font>
# </div>

# # Difference btw type hinting and annotation?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - In Python, type hinting and annotations are similar concepts that are used to indicate the types of variables or the return types of functions. However, there is a **subtle difference** between the two.
#     - **Type hinting** refers to the practice of indicating the type of a variable or the return type of a function using the `->` syntax
#     - **Annotations**, on the other hand, refer to the use of the `:` symbol. 
# 
# </font>
# </div>

# # Example #1
# <hr style = "border:2px solid black" ></hr>

# In[2]:


def kinetic_energy(m: 'in KG', v: 'in M/S') -> 'Joules':
    return 1/2*m*v**2


# In[3]:


kinetic_energy


# In[5]:


dir(kinetic_energy)


# In[4]:


kinetic_energy.__annotations__


# <div class="alert alert-info">
# <font color=black>
# 
# - Annotations are dictionaries, so you can do this 
# 
# </font>
# </div>

# In[3]:


'{:,} {}'.format(kinetic_energy(12, 30),
                 kinetic_energy.__annotations__['return'])


# # Example #2
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - You can also have a python data structure rather than just a string:
# 
# </font>
# </div>

# In[4]:


rd = {'type': float, 'units': 'Joules',
      'docstring': 'Given mass and velocity returns kinetic energy in Joules'}


def f() -> rd:
    pass


# In[5]:


f.__annotations__['return']['type']


# In[6]:


f.__annotations__['return']['units']


# In[7]:


f.__annotations__['return']['docstring']


# # Example #3
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - You can use function attributes to validate called values:
# 
# </font>
# </div>

# In[1]:


def validate(func, locals):
    for var, test in func.__annotations__.items():
        value = locals[var]
        try:
            pr = test.__name__+': '+test.__docstring__
        except AttributeError:
            pr = test.__name__
        msg = '{}=={}; Test: {}'.format(var, value, pr)
        assert test(value), msg


def between(lo, hi):
    def _between(x):
        return lo <= x <= hi
    _between.__docstring__ = 'must be between {} and {}'.format(lo, hi)
    return _between


def f(x: between(3, 10), y: lambda _y: isinstance(_y, int)):
    validate(f, locals())
    print(x, y)


# In[2]:


f(2,2)


# In[3]:


f(3,2.1)


# # Example #4
# <hr style = "border:2px solid black" ></hr>

# In[4]:


import math

def circumference(radius: float) -> float:
    return 2 * math.pi * radius


# In[5]:


circumference.__annotations__


# # Example #5
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Now, if we were to enter an incorrect arguments, what would happen?
# - In reality, nothing of significance — remember, Python does not enforce our type annotations.
# - Instead, they are used by third-party IDEs and linters. So, an erroneous annotation will be highlighted by our third-party tool — acting as an early warning system that our logic isn’t quite right.
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[9]:


def add(x: int, y: int) -> int:
    return x + y


# In[10]:


add(7, 4)


# In[11]:


add("7", "4")


# # Example of various annotations
# <hr style = "border:2px solid black" ></hr>

# ## `Union` and `|`

# - Allow a set of different types for a single assignment.

# In[15]:


from typing import Union
def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


# In[16]:


# Available from python 3.10
def add(x: int | float, y: int | float) -> int | float:
    return x + y


# ## `Optional`

# - When we define a function with optional parameters, we can specify this using the Optional type. 

# # List vs. `list` in type hinting
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - In Python, List and list both refer to the built-in list class, but there is a difference in how they are used.
# - `List` is used as a type hint to indicate that the function returns a list. Type hints were introduced in Python 3.5 and are used to indicate the type of a variable or the return type of a function. They are optional and do not affect the execution of the code. It is used to make the code more readable and also for the tools like IDEs, linters, type checkers etc to provide better suggestions, error messages etc.
# - `list` is used as a return type of the function, it means that the function should return an object of the built-in list class.
#     
# </font>
# </div>

# In[8]:


from typing import List
def a() -> List:
    return [1, 2, 3]
a


# In[9]:


def a() -> list:
    return [1, 2, 3]
a


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions
# - https://www.python.org/dev/peps/pep-3107/
# - https://realpython.com/lessons/annotations/
# - https://towardsdatascience.com/type-annotations-in-python-d90990b172dc
# - [Type hints cheatsheet 1](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
# - [type hints cheatsheet 2](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
#     
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[2]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv -m')


# In[ ]:




