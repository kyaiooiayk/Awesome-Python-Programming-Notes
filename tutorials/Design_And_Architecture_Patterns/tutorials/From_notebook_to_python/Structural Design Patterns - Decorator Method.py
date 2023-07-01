#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Structural-Design-Patterns" data-toc-modified-id="Structural-Design-Patterns-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Structural Design Patterns</a></span></li><li><span><a href="#Decorator-Method" data-toc-modified-id="Decorator-Method-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Decorator Method</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Structural Design Patterns - Decorator Method
#
# </font>
# </div>

# # Structural Design Patterns
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - **Structural Design Patterns** are used to establish relation between software components in particular settings.
#     - [ ] Adapter Method
#     - [ ] Bridge Method
#     - [ ] Composite Method
#     - [x] Decorator Method
#     - [ ] Facade Method
#     - [ ] Proxy Method
#     - [ ] FlyWeight Method
#
# </font>
# </div>

# # Decorator Method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - **Lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.**
# - Decorator pattern allows adding new features to an object without changing their structures.
# - Here the problem is to add new features to the object without subclassing.
# - In python we can additional features to a function using the inbuilt decorator
#
# </font>
# </div>

# # Example
# <hr style = "border:2px solid black" ></hr>

# In[20]:


def hello_world_original():
    """The original function not decorated"""
    return "Hello World!"


# In[21]:


hello_world_original()


# In[22]:


hello_world_original.__name__


# In[23]:


hello_world_original.__doc__


# In[28]:


from functools import wraps


def make_blink(function):
    """Defines the decorator"""

    # This makes the decorator transparent in terms of its name and doctstring

    @wraps(function)
    # Define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()

        # Add new functionality to the function being decorated.
        return "<blink>" + ret + "</blink>"

    return decorator


@make_blink
def hello_world():
    """The original function decorated"""
    return "Hello World!"


# In[29]:


hello_world()


# In[30]:


hello_world.__name__


# In[31]:


hello_world.__doc__


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-danger">
# <font color=black>
#
# - **Advantages**:
#     - You can extend an object’s behaviour without making a new subclass.
#     - You can add or remove responsibilities from an object at runtime.
#     - You can combine several behaviors by wrapping an object into multiple decorators.
#     - Single Responsibility Principle. You can divide a monolithic class that implements many possible variants of behavior into several smaller classes.
# - **Disadvantages**:
#     - It’s hard to remove a specific wrapper from the wrappers stack.
#     - It’s hard to implement a decorator in such a way that its behavior doesn’t depend on the order in the decorators stack.
#     - The initial configuration code of layers might look pretty ugly.
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - [Decorator method](https://www.geeksforgeeks.org/decorator-method-python-design-patterns/)
# - [Decorator in Python](https://refactoring.guru/design-patterns/decorator)
# - https://github.com/pyGuru123/Python-design-Patterns/blob/main/Structural%20Pattern/decorator.py
# - [Function decoration notes](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/Decorations/Function%20decorators.ipynb)
#
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[7]:


get_ipython().run_line_magic("load_ext", "watermark")
get_ipython().run_line_magic("watermark", "-v -iv -m")


# In[ ]:
