#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Unpacking" data-toc-modified-id="Unpacking-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Unpacking</a></span></li><li><span><a href="#References" data-toc-modified-id="References-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert k alert-warning">
# <font color=black>
# 
# **What?** * unpacking
# 
# </font>
# </div>

# # Unpacking
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - When we operate on a list of parameters, we often need to extract the content of the list **as individual arguments instead of** a collection when passing them into functions.
# - Luckily, the * operator can help us to unpack lists and tuples 
# 
# </font>
# </div>

# In[1]:


a = [1,3,3]


# In[2]:


[i for i in a]


# In[8]:


[*a]


# In[3]:


print(a)


# In[5]:


print(len(a))


# In[4]:


print(*a)


# In[7]:


print(len([*a]))


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://github.com/QuantEcon/lecture-python-programming.notebooks/blob/master/python_advanced_features.ipynb
#     
# </font>
# </div>

# In[ ]:




