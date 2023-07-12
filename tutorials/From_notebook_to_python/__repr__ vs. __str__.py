#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-the-difference?" data-toc-modified-id="What-is-the-difference?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is the difference?</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#References" data-toc-modified-id="References-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** `__repr__` vs. `__str__` methods
#
# </font>
# </div>

# # What is the difference?

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - They both represent the object but the `__repr__` method tells you more.
# - So much more that you can also reconstruct the object based on that information.
# - Also Python interpreter sessions use `__repr__` to inspect objects.
# - `__str__` should have a readable output.
#
# </font>
# </div>

# # Example #1

# In[27]:


import numpy as np


class Tensor(object):
    def __init__(self, data):
        """__init__ method
        Given a list, tunrs it into an array
        """
        self.data = np.array(data)

    def __add__(self, other):
        """__add__ method
        Add two tensor together
        """
        return Tensor(self.data + other.data)

    def __repr__(self):
        print("calling __repr__")
        """__repr__ method
        Returns the object representation in string format.
        Retunrs and official string representation of the object,
        which can be ised to construt the object again.
        """
        return str(self.data.__repr__())

    def __str__(self):
        print("calling __str__")
        """
        Returns the string representation of the object. This method is called
        when print() or str() function is invoked on an object. Retunrs a 
        human-redeable string format.
        """
        return str(self.data.__str__())


# In[28]:


x = Tensor([1, 2, 3, 4, 5])


# In[29]:


x


# In[30]:


repr(x)


# In[31]:


str(x)


# In[32]:


print(x)


# # References

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - https://www.journaldev.com/22460/python-str-repr-functions
#
# </font>
# </div>

# In[ ]:
