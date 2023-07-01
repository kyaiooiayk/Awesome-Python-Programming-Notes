#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Import-modules" data-toc-modified-id="Import-modules-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Import modules</a></span></li><li><span><a href="#Without-status-bar" data-toc-modified-id="Without-status-bar-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Without status bar</a></span></li><li><span><a href="#tqdm-to-show-status-bar" data-toc-modified-id="tqdm-to-show-status-bar-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>tqdm to show status bar</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** How to show status bar
# 
# </font>
# </div>

# # Import modules

# In[9]:


from tqdm import tqdm


# # Without status bar

# In[10]:


a = []
import numpy as np
b = np.linspace(0,10,int(1.e2))

for dummy in b:
    a.append(dummy)
print(a)


# # tqdm to show status bar

# In[12]:


a = []
import numpy as np
b = np.linspace(0,10,int(1.e7))

for dummy in tqdm(b, desc = "Reading and appending"):
    a.append(dummy)
print(a[:10])


# # References

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - https://www.kdnuggets.com/2021/08/data-scientist-guide-efficient-coding-python.html
# 
# </font>
# </div>

# In[ ]:




