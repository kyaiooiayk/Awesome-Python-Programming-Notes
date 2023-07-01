#!/usr/bin/env python
# coding: utf-8

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Sequence slicing
# 
# </font>
# </div>

# # Sequence definition
# <hr style="border:2px solid black"> </hr>

# In[1]:


s = 'Slicing is easy!'


# In[2]:


s


# # [start:stop:step]
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The default value of the step parameter is `Z`
# 
# </font>
# </div>

# In[3]:


s[2:14:2]


# In[4]:


# equivalent to this as well
s[2:14][::2]


# # step-only
# <hr style="border:2px solid black"> </hr>

# In[5]:


s[::2]


# # `slice` built-in function
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The syntax `[start:stop:step]` is just syntactic sugar for `slice(start, stop, step)`.
# 
# </font>
# </div>

# In[7]:


sl = slice(1, 12, 3)


# In[8]:


sl.start


# In[9]:


sl.stop


# In[10]:


sl.step


# In[13]:


# Normally we'll do this
s[1:15:2]


# In[15]:


# but we could also do this
sl=slice(1,15,2)
s[sl]


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://mathspp.com/blog/pydonts
# 
# </font>
# </div>

# In[ ]:




