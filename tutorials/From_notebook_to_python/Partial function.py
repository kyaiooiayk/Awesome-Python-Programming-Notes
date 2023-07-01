#!/usr/bin/env python
# coding: utf-8

# # Introduction

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Python partial function
# 
# </font>
# </div>

# # Import modules

# In[3]:


from functools import partial


# # Theory

# <div class="alert alert-info">
# <font color=black>
# 
# - **Partial functions** allow one to derive a function with x parameters to a function with fewer parameters and fixed values set for the more limited function.
# 
# </font>
# </div>

# # Example

# <div class="alert alert-info">
# <font color=black>
# 
# - We are going to create a function that multiplies two numbers.
# - We then want to create a function that always multipluies y by 1, but we don't want to rewrite another function, insetad we'd like to use what we have.
# - **IMPORTANT:** the default values will start replacing variables from the left. 
#     
# </font>
# </div>

# In[4]:


def multiply(x,y):
        print("x has value:", x)
        print("y has value:", y)
        return x * y


# In[9]:


multiply(3,3)


# In[6]:


pf_1 = partial(multiply,2)


# In[7]:


pf_1(3)


# In[15]:


pf_1(1)


# <div class="alert alert-info">
# <font color=black>
# 
# - We can also fix both arguments at the same time
# 
# </font>
# </div>

# In[8]:


pf_2 = partial(multiply, 2,2)


# In[20]:


pf_2()


# # References

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://www.learnpython.org/en/Partial_functions
# 
# </font>
# </div>

# In[ ]:




