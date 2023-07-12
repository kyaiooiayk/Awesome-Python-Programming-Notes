#!/usr/bin/env python
# coding: utf-8

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Declaring private variables
#
# </font>
# </div>

# # Private class and variable
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - A private class or variable is indcated with a preceding underscore `_`.
# - However, of course, Python does not supports truly private.
# - So we can not force something in python to be stricly private. In fact,  one can call it directly from other modules.
# - The underscore is then used as an indication to programmer to consider it as private.
# - So sometimes we say it **weak internal use indicator**.
#
# </font>
# </div>

# In[17]:


class _Base:
    """private class"""

    _hidden_factor = 2  # private variable

    def __init__(self, price):
        self._price = price

    def _double_price(self):
        """private method"""
        return self._price * self._hidden_factor

    def get_double_price(self):
        """global method"""
        return self._double_price()


# In[18]:


obj = _Base(100)


# In[20]:


obj._hidden_factor


# In[21]:


obj._double_price()


# In[24]:


obj.get_double_price()


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc
#
# </font>
# </div>

# In[ ]:
