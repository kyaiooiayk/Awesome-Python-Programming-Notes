#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#collections" data-toc-modified-id="collections-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>collections</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** collections
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


from collections import OrderedDict


# # collections
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.
#     
# </font>
# </div>

# # Example #1
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Get rid of duplicates in a list of integers.
# 
# </font>
# </div>

# In[4]:


items = [1, 2, 0, 1, 3, 2]
OrderedDict.fromkeys(items)


# In[5]:


type(OrderedDict.fromkeys(items))


# In[6]:


list(OrderedDict.fromkeys(items))


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [How do I remove duplicates from a list, while preserving order?](https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order)
# 
# </font>
# </div>

# In[ ]:




