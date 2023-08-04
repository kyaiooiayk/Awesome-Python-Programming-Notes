#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-with-in-Python?" data-toc-modified-id="What-is-with-in-Python?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is <code>with</code> in Python?</a></span></li><li><span><a href="#Three-ways-to-write-in-a-file" data-toc-modified-id="Three-ways-to-write-in-a-file-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Three ways to write in a file</a></span></li><li><span><a href="#How-it-works" data-toc-modified-id="How-it-works-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>How it works</a></span></li><li><span><a href="#Clean-up-folder" data-toc-modified-id="Clean-up-folder-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Clean-up folder</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** `with` statement
# 
# </font>
# </div>

# # What is `with` in Python?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - In Python, with statement is used in exception handling to make the code cleaner and much more readable.
# - It simplifies the management of common resources like file streams. 
# - The with statement is popularly used with file streams, as shown above and with Locks, sockets, subprocesses and telnets etc.
#     
# </font>
# </div>

# # Three ways to write in a file
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - An exception during the file.write() call in the first implementation can prevent the file from closing properly which may introduce several bugs in the code, i.e. many changes in files do not go into effect until the file is properly closed.
# 
# </font>
# </div>

# In[1]:


# Without using with statement
file = open('file_1.txt', 'w')
file.write('hello world !')
file.close()


# <div class="alert alert-info">
# <font color=black>
#     
# - The second approach in the above example takes care of all the exceptions but the code seems to be too cluttered.
#     
# </font>
# </div>

# In[2]:


# Without using with statement
file = open('file_2.txt', 'w')
try:
    file.write('hello world')
finally:
    file.close()


# <div class="alert alert-info">
# <font color=black>
#     
# - Notice that unlike the first two implementations, there is no need to call `file.close()` when using with statement.
# - Using the with statement makes the code compact and much more readable. 
# - Thus, with statement helps avoiding bugs and leaks by ensuring that a resource is properly released when the code using the resource is completely executed. 
# 
# </font>
# </div>

# In[3]:


# Using with statement
with open('file_3.txt', 'w') as file:
    file.write('hello world !')


# # How it works
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - To use with statement in user defined objects you only need to add the dunder methods `__enter__()` and `__exit__()` in the object methods.
# 
# </font>
# </div>

# In[4]:


class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, *args):
        self.file.close()


# <div class="alert alert-info">
# <font color=black>
#     
# - The with statement takes the object instance that implements the context manager interface as an argument.
# - It will execute the code in the object for the beginning of the block, e.g. the `__enter__()` method and return an instance of an object that can be assigned.
# 
# </font>
# </div>

# ```python
# # execute the context manager, calls __enter__()
# with object as o:
#     # the main block...
# # end of the context manager, calls __exit__()
# ```

# In[5]:


# Using with statement with MessageWriter
with MessageWriter('file_4.txt') as xfile:
    xfile.write('hello world')


# <div class="alert alert-info">
# <font color=black>
# 
# - A class based context manager as shown above is not the only way to support the with statement in user defined objects.
# - The `contextlib` module provides a few more abstractions built upon the basic context manager interface.
# 
# </font>
# </div>

# In[6]:


from contextlib import contextmanager


class MessageWriter(object):
    def __init__(self, filename):
        self.file_name = filename

    @contextmanager
    def open_file(self):
        try:
            file = open(self.file_name, 'w')
            yield file
        finally:
            file.close()


# In[7]:


# usage
message_writer = MessageWriter('file_5.txt')
with message_writer.open_file() as my_file:
    my_file.write('hello world')


# # Clean-up folder
# <hr style = "border:2px solid black" ></hr>

# In[8]:


get_ipython().system('rm file_1.txt')
get_ipython().system('rm file_2.txt')
get_ipython().system('rm file_3.txt')
get_ipython().system('rm file_4.txt')
get_ipython().system('rm file_5.txt')


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [`with` statement in Python](https://www.geeksforgeeks.org/with-statement-in-python/)
# - [What is a context manager?](https://superfastpython.com/thread-context-manager/)
#     
# </font>
# </div>

# In[ ]:




