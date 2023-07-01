#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Conditional-else" data-toc-modified-id="Conditional-else-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Conditional else</a></span></li><li><span><a href="#Completion-else" data-toc-modified-id="Completion-else-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Completion else</a></span><ul class="toc-item"><li><span><a href="#try-except" data-toc-modified-id="try-except-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span><code>try-except</code></a></span></li><li><span><a href="#while-loop" data-toc-modified-id="while-loop-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span><code>while-loop</code></a></span></li><li><span><a href="#for-loop" data-toc-modified-id="for-loop-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span><code>for-loop</code></a></span></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Conditional else and completion else
#
# </font>
# </div>

# # Conditional else
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - It is **either** the code under the `if` clause that is executed, **or** the code under the `else` block, but not both.
# - If the condition of the `if` clause evaluates to `True`, the `if`-block is exectured, and if it evaluated to `False`, it is the `else` block.
#
# </font>
# </div>

# In[2]:


# conditional else
a_list = [1, 2]
if a_list[0] == 1:
    print("Hello, World!")
else:
    print("Bye, World!")


# In[3]:


# conditional else
a_list = [1, 2]
if a_list[0] == 2:
    print("Hello, World!")
else:
    print("Bye, World!")


# # Completion else
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - **In contrast** to the **either...or*** situation that we know from the conditional `else`, the completion `else` is executed if a code block id finished.
# - In the code above, we can see that the code under the **`else`-clause is only executed if the `try-block` was executed without encountering an error, i.e., if the `try`-block is "complete".**
# - The same rule applies to the "completion" `else` in `while`- and `for`-loops, which you can confirm in the following samples below.
#
# </font>
# </div>

# ## `try-except`

# In[4]:


a_list = [1, 2]

try:
    print("first element:", a_list[0])
except IndexError:
    print("raised IndexError")
else:
    print("no error in try-block")


# In[5]:


try:
    print("third element:", a_list[2])
except IndexError:
    print("raised IndexError")
else:
    print("no error in try-block")


# ## `while-loop`

# In[6]:


i = 0
while i < 2:
    print(i)
    i += 1
else:
    print("in else")


# In[7]:


i = 0
while i < 2:
    print(i)
    i += 1
    break
else:
    print("completed while-loop")


# ## `for-loop`

# In[8]:


for i in range(2):
    print(i)
else:
    print("completed for-loop")


# In[9]:


for i in range(2):
    print(i)
    break
else:
    print("completed for-loop")


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/not_so_obvious_python_stuff.ipynb?create=1
#
# </font>
# </div>

# In[ ]:
