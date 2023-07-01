#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-a-Modules?" data-toc-modified-id="What-is-a-Modules?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is a Modules?</a></span></li><li><span><a href="#Designing-and-Writing-Modules" data-toc-modified-id="Designing-and-Writing-Modules-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Designing and Writing Modules</a></span></li><li><span><a href="#Module-used-as-a-script" data-toc-modified-id="Module-used-as-a-script-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Module used as a script</a></span></li><li><span><a href="#Kinds-of-Modules" data-toc-modified-id="Kinds-of-Modules-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Kinds of Modules</a></span></li><li><span><a href="#Module-Search-Path" data-toc-modified-id="Module-Search-Path-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Module Search Path</a></span></li><li><span><a href="#Content-of-a-Module" data-toc-modified-id="Content-of-a-Module-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Content of a Module</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Modules
# 
# </font>
# </div>

# # What is a Modules?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Every file, which has the file extension .py and consists of proper Python code, can be seen or is a module! 
# - There is no special syntax required to make such a file a module. 
# - A module can contain arbitrary objects, for example files, classes or attributes. 
# - All those objects can be accessed after an import. There are different ways to import a modules.
# 
# </font>
# </div>

# # Designing and Writing Modules
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - A module in Python is just a file containing Python definitions and statements. The module name is moulded out of the file name by removing the suffix `.py`. 
# - For example, if the file name is `fibonacci.py`, the module name is `fibonacci`.
# 
# </font>
# </div>

# In[2]:


import fibonacci
fibonacci.fib(7)


# # Module used as a script
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `__name__` is a variable defined for each script that defines whether the script is being run as the main module or it is being run as an imported module.
# 
# - So it's possible to program different behaviour into a module for the two cases:
#     - As a module or
#     - As a script.
#  
# </font>
# </div>

# In[4]:


# If it is imported, the code in the if block will not be executed:
from fibonacci import fib


# In[7]:


# If it is run as a script, we get the following output:
get_ipython().system('python fibonacci.py 3')


# # Kinds of Modules
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - There are different kind of modules:
#     - Those written in Python
#     - They have the suffix: .py
#     - Dynamically linked C modules
#     - Suffixes are: .dll, .pyd, .so, .sl, ...
#     - C-Modules linked with the Interpreter
# - It's possible to get a complete list of these modules with `sys.builtin_module_names`
# 
# 
# </font>
# </div>

# In[8]:


import sys
sys.builtin_module_names


# # Module Search Path
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - If you import a module, let's say "import xyz", the interpreter searches for this module in the following locations and in the order given:
# 
#     - The directory of the top-level file, i.e. the file being executed.
#     - The directories of PYTHONPATH, if this global environment variable of your operating system is set.
#     - standard installation path Linux/Unix e.g. in /usr/lib/python3.5. 
# 
# - It's possible to find out where a module is located after it has been imported append `.file` or using dunder method `__file__`.
# - The `file` attribute doesn't always exist. This is the case with modules which are statically linked C libraries.
#     
#     
# </font>
# </div>

# In[18]:


import fibonacci
fibonacci.__file__


# In[11]:


import numpy
numpy.__file__


# In[12]:


import math
math.__file__


# # Content of a Module
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - With the built-in function `dir()` and the name of the module as an argument, you can list all valid attributes and methods for that module.
# - Calling `dir()` without an argument, a list with the names in the current **local scope** is returned.
# - It's possible to get a list of the Built-in functions, exceptions, and other objects by importing the `builtins` module.
# 
# </font>
# </div>

# In[19]:


import math
dir(math)


# In[20]:


import math
cities = ["New York", "Toronto", "Berlin", "Washington", "Amsterdam", "Hamburg"]
dir()


# In[21]:


import builtins
dir(builtins)


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://python-course.eu/python-tutorial/modules-and-modular-programming.php
# 
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[22]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv')


# In[ ]:




