#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#dis-module-in-python" data-toc-modified-id="dis-module-in-python-2"><span class="toc-item-num">2&nbsp;&nbsp;</span><code>dis</code> module in python</a></span></li><li><span><a href="#Basics" data-toc-modified-id="Basics-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Basics</a></span><ul class="toc-item"><li><span><a href="#Feeding-a-module" data-toc-modified-id="Feeding-a-module-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Feeding a module</a></span></li><li><span><a href="#Feeding-a-function" data-toc-modified-id="Feeding-a-function-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Feeding a function</a></span></li><li><span><a href="#Feeding-a-class" data-toc-modified-id="Feeding-a-class-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Feeding a class</a></span></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Disassembling python bytecode
#
# </font>
# </div>

# # `dis` module in python
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - In Python, the dis module allows disassembly of Python code into the individual instructions executed by the Python interpreter (usually cPython as this is the most popular implementation) for each line.
#
# - This is useful for analysing and fine-tuning your code.
#
# </font>
# </div>

# In[11]:


dir(dis)


# # Basics
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The main method will use is `dis.dis`.
# - It takes either a function, method, class, module, code string, generator or byte sequence of raw bytecode and prints the disassembly of that code object to stdout.
# - In the case of a class, it will disassemble each method (also static and class methods).
# - For a module, it disassembles all functions in that module.
# - The columns returned are the following:
#     - The original line of code the disassembly is referencing.
#     - The address of the bytecode instruction.
#     - The name of the instruction.
#     - The index of the argument in the code block’s name and constant table.
#     - The human-friendly mapping from the argument index (4) to the actual value or name being referenced
#
# </font>
# </div>

# ## Feeding a module

# In[8]:


import dis, numpy

dis.dis(numpy)


# ## Feeding a function

# In[12]:


def bar():
    x = 5
    y = 7
    z = x + y
    return z


dis.dis(bar)


# ## Feeding a class

# In[14]:


class Foo(object):
    def __init__(self):
        pass

    def foo(self, x):
        return x + 1


dis.dis(Foo)


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/not_so_obvious_python_stuff.ipynb?create=1
# - http://www.goldsborough.me/python/low-level/2016/10/04/00-31-30-disassembling_python_bytecode/
#
# </font>
# </div>

# In[ ]:
