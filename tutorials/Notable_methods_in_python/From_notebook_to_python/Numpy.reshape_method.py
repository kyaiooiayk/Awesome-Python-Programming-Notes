#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Motivation" data-toc-modified-id="Motivation-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Motivation</a></span></li><li><span><a href="#Generate-some-data" data-toc-modified-id="Generate-some-data-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Generate some data</a></span></li><li><span><a href="#-1-behviour" data-toc-modified-id="-1-behviour-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>-1 behviour</a></span></li><li><span><a href="#Multidimensional-array-=-tensor" data-toc-modified-id="Multidimensional-array-=-tensor-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Multidimensional array = tensor</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** `numpy.reshape()` method
# 
# </font>
# </div>

# # Motivation

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - While working with tensor and in particular while working with RNNs and LSTMs model one of the most used method is `reshape`.
# - Hence it is paramount to understand how it works.
# 
# </font>
# </div>

# # Generate some data

# In[2]:


import numpy as np
# 10 rows and 2 columns
a = np.zeros((10, 2))


# In[3]:


a


# In[6]:


a.shape


# In[36]:


# Each of the 10 entry has a matrix of 4x4
b = np.random.random((10, 4, 4))


# In[37]:


b


# In[44]:


b.shape


# # -1 behviour

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - It simply means that it is an unknown dimension and we want numpy to figure it out. 
# - If we say `a.reshape(-1,1)` we are saying we'd like to have a new array with 1 column and we are asking numpy to figure it out what the the number of rows will be.
# - One one shape can be inferred.
# - **How does numpy inferred the shape?** `inferred shape = length of flattened array / the sum of given shapes.`
# - This means that something like this `a.reshape(-1,-1)` is **NOT** allowed.
# 
# </font>
# </div>

# In[4]:


a.reshape(-1,1)


# In[ ]:


# This is an alternative syntax, totally equivalent but a bit more long
np.reshape(a, (-1,1))


# In[9]:


a.reshape(-1,1).shape


# In[14]:


# Just checking the shape. ndarray are n-dimensional array
type(a.reshape(-1,1))


# In[11]:


# This is not allowed!
a.reshape(-1,-1)


# In[8]:


a.reshape(-1,)


# In[12]:


a.reshape(-1,).shape


# In[13]:


# Just checking the type
type(a.reshape(-1,))


# In[20]:





# # Multidimensional array = tensor

# In[38]:


b.shape


# In[40]:


b


# In[39]:


# Here we want array with only one column. 
# The number of rows will be 10*4*4 = 160
b.reshape(-1,1)


# In[41]:


# As you can see the number of rows are as we predicted them
b.reshape(-1,1).shape


# In[42]:


# Here we say we'd like to have each entrued organised by 2x2 matrices
# The number of entries is inferred by reshape method
b.reshape(-1,2,2)


# In[43]:


b.reshape(-1,2,2).shape


# In[49]:


# You can compare the first row the the unchange array
print(b[0])
# with the first rwo of the reshaped array to see how they were organised
print(b.reshape(-1,2,2)[:4])


# # Conclusions

# <div class="alert alert-danger">
# <font color=black>
# 
# - The number of elements in the final array is same as that of the initial array or data frame.
# - Input `-1` allows for the user laziness thus numpy will figure it our based on what you provide as input: No of rows or columns.
# 
# </font>
# </div>

# # References

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
# - https://stackoverflow.com/questions/18691084/what-does-1-mean-in-numpy-reshape
# - https://www.mikulskibartosz.name/numpy-reshape-explained/
# 
# </font>
# </div>

# In[ ]:




