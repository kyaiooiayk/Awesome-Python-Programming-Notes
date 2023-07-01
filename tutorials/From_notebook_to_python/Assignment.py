#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Is-Python-pass-by-value?" data-toc-modified-id="Is-Python-pass-by-value?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Is Python pass-by-value?</a></span></li><li><span><a href="#Is-Python-pass-by-reference?" data-toc-modified-id="Is-Python-pass-by-reference?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Is Python pass-by-reference?</a></span></li><li><span><a href="#Python-is-pass-by-assignment" data-toc-modified-id="Python-is-pass-by-assignment-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Python is pass-by-assignment</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Assignment
#
# </font>
# </div>

# # Is Python pass-by-value?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - In the pass-by-value model, when you call a function with a set of arguments, the data is copied into the function. This means that you can modify the arguments however you please and that you won’t be able to alter the state of the program outside the function.
#
# - This is not what Python does, Python does not use the pass-by-value model.
#
# </font>
# </div>

# In[3]:


def clearly_not_pass_by_value(my_list):
    my_list[0] = 42


l = [1, 2, 3]
clearly_not_pass_by_value(l)
print(l)
## [42, 2, 3]


# # Is Python pass-by-reference?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - In a true pass-by-reference model, the called function gets access to the variables of the callee!
#
# - Sometimes, it can look like that’s what Python does, but Python does not use the pass-by-reference model.
#
# - If Python used a pass-by-reference model, the function would’ve managed to completely change the value of l outside the function, but that’s not what happened, as we can see.
#
# - Pascal programming laguage implements a pass-by-reference model.
#
# </font>
# </div>

# In[4]:


def not_pass_by_reference(my_list):
    my_list = [42, 73, 0]


l = [1, 2, 3]
not_pass_by_reference(l)
print(l)


# # Python is pass-by-assignment
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - When we call a function, each of the parameters of the function is assigned to the object they were passed
# in. In essence, each parameter now becomes a new nickname to the objects that were given in.
#
# - In the example below, when we call foo with the argument 5, it’s as if we were doing bar = 5 at the beginning of the function.
#
# - Immediately after that, we have bar = 3. This means “take the nickname”bar” and point it at the integer 3”.
#
# - Python **doesn’t care** that bar, as a nickname (as a variable name) had already been used. It is now pointing at that 3!
#
# </font>
# </div>

# In[6]:


def foo(bar):
    bar = 3
    return bar


foo(5)


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - [Whirlwind Tour of Python](http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp)
# - https://mathspp.com/blog/pydonts
#
# </font>
# </div>

# In[ ]:
