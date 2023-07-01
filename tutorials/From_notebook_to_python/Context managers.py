#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-it?" data-toc-modified-id="What-is-it?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is it?</a></span></li><li><span><a href="#with" data-toc-modified-id="with-3"><span class="toc-item-num">3&nbsp;&nbsp;</span><code>with</code></a></span></li><li><span><a href="#Implementing-a-Context-Manager-as-a-Class" data-toc-modified-id="Implementing-a-Context-Manager-as-a-Class-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Implementing a Context Manager as a Class</a></span></li><li><span><a href="#Implementing-a-Context-Manager-as-a-Generator" data-toc-modified-id="Implementing-a-Context-Manager-as-a-Generator-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Implementing a Context Manager as a Generator</a></span></li><li><span><a href="#Folder-clean-up" data-toc-modified-id="Folder-clean-up-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Folder clean-up</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Context managers
#
# </font>
# </div>

# # What is it?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Context managers allow you to allocate and release resources precisely when you want to.
# - Suppose you have two related operations which you’d like to execute as a pair, with a block of code in between. Context managers allow you to do specifically that.
#
# </font>
# </div>

# # `with`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The above code opens the file, writes some data to it and then closes it.
# - **If an error occurs** while writing the data to the file, it tries to close it.
# - What follows is an example that tries to explain how `with` simplifies the code and make it safer.
# - While comparing it to the first example, we can see that a lot of boilerplate code is eliminated just by using `with`.
# - The main advantage of using a `with` statement is that it makes sure our file is closed **without paying attention to how the nested block exits**. In fact, as you may recall, `finally` is executed regardless of how the `try` statement exits, with or without an error.
#
# </font>
# </div>

# In[2]:


with open("some_file.txt", "w") as opened_file:
    opened_file.write("Hello!")


# In[3]:


# This equivalent to the following boiler plate code
file = open("some_file.txt", "w")
try:
    file.write("Hello!")
finally:
    file.close()


# # Implementing a Context Manager as a Class
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - At the very least a context manager has an `__enter__` and `__exit__` method defined.
# - Just by defining these two dunder methods we can use our new class in a `with` statement.
#
# </font>
# </div>

# In[7]:


class MyFile(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


# In[8]:


with MyFile("demo.txt", "w") as opened_file:
    opened_file.write("Hello kyaiooiayk!")


# # Implementing a Context Manager as a Generator
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - We can also implement Context Managers using decorators and generators.
# - Python has a contextlib module for this very purpose. Instead of a class, we can implement a Context Manager using a generator function.
#
# </font>
# </div>

# In[13]:


from contextlib import contextmanager


@contextmanager
def open_file(name):
    f = open(name, "w")
    try:
        yield f
    finally:
        f.close()


# In[14]:


with open_file("some_file.txt") as f:
    f.write("hello kyaiooiayk!")


# # Folder clean-up
# <hr style = "border:2px solid black" ></hr>

# In[15]:


get_ipython().system("rm some_file.txt")
get_ipython().system("rm demo.txt")


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://book.pythontips.com/en/latest/context_managers.html
#
# </font>
# </div>

# In[ ]:
