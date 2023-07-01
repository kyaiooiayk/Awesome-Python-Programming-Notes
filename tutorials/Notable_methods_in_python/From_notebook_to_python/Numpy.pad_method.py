#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Motivation" data-toc-modified-id="Motivation-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Motivation</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#References" data-toc-modified-id="References-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** `numpy.pad()` method
# 
# </font>
# </div>

# # Motivation
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - `np.pad` is used to artificially change the shappe of a matrix.
# - An image can be represented via matrix or a tensor more precisely.
# - Padding describes the addition of zeros to the *border of matrix*.
# - Say you have an image of dimension `(28,28,1)` and you'd like to turn it into a `(32,32,1)`, you can do it by adding zeros all around it.
# 
# </font>
# </div>

# In[1]:


import numpy as np


# # Example #1
# <hr style="border:2px solid black"> </hr>

# In[2]:


# Create a tensor
z = np.arange(12).reshape(3,2,2)
print(z.shape)
print(z)


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - The pad_width argument to np.pad works like this: ((axis 1 pad before, axis 1 pad after), ...)
# - So if you want to pad 1 pixel on each side you should do ((0,0), (1,1), (1,1)). 
# 
# </font>
# </div>

# In[3]:


z = np.pad(z, ((0,0),(1,1),(1,1)), 'constant')
print(z.shape)
# (3, 4, 4)
print(z)


# In[4]:


# as an example, take a look at the second "image"
print(z[1])


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - https://stackoverflow.com/questions/61309432/padding-mnist-images-from-28-28-1-to-32-32-1
#     
# </font>
# </div>

# In[ ]:




