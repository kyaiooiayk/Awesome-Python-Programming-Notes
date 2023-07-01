#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Don't-use-mutable-objects-as-default-arguments-for-functions!" data-toc-modified-id="Don't-use-mutable-objects-as-default-arguments-for-functions!-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Don't use mutable objects as default arguments for functions!</a></span></li><li><span><a href="#References" data-toc-modified-id="References-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Don't use mutable objects as default arguments
#
# </font>
# </div>

# # Don't use mutable objects as default arguments for functions!
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Don't use mutable objects (e.g., dictionaries, lists, sets, etc.) as default arguments for functions!
# - You might expect that a new list is created every time when we call the function without providing an argument for the default parameter, but this is not the case: **Python will create the mutable object (default parameter) the first time the function is defined - not when it is called**.
#
# </font>
# </div>

# In[15]:


def append_to_list(value, def_list=[]):
    def_list.append(value)
    return def_list


my_list = append_to_list(1)
print(my_list)

my_other_list = append_to_list(2)
print(my_other_list)


# <div class="alert alert-info">
# <font color=black>
#
# - Another good example showing that demonstrates that default arguments are created when the function is created (**and not when it is called!**)
#
# </font>
# </div>

# In[16]:


import time


def report_arg(my_default=time.time()):
    print(my_default)


report_arg()

time.sleep(5)

report_arg()


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/not_so_obvious_python_stuff.ipynb?create=1
# - http://docs.python-guide.org/en/latest/writing/gotchas/
#
# </font>
# </div>

# In[ ]:
