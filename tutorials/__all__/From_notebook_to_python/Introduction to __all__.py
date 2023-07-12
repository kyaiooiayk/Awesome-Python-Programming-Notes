#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-does-__all__-do?" data-toc-modified-id="What-does-__all__-do?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What does <code>__all__</code> do?</a></span></li><li><span><a href="#No-__all__-in-__init__.py" data-toc-modified-id="No-__all__-in-__init__.py-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>No <code>__all__</code> in <code>__init__.py</code></a></span></li><li><span><a href="#__all__-in-the-__init_all.py" data-toc-modified-id="__all__-in-the-__init_all.py-4"><span class="toc-item-num">4&nbsp;&nbsp;</span><code>__all__</code> in the <code>__init_all.py</code></a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?**  What does `__all__`: do?
#
# </font>
# </div>

# # What does `__all__` do?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - In its simplest case, the `__init__.py` file is an empty file. However, it is also used to set up imports and this can be controlled by the variable `__all__`.
# - Essentially `__all__` will the interpreter what to import when the wild card `import *` is used.
#
# </font>
# </div>

# # No `__all__` in `__init__.py`
# <hr style="border:2px solid black"> </hr>

# In[1]:


from Foo_no_all import *


# In[2]:


# Will trow an error
foo.a


# In[5]:


# To access the file foo we need to import it directly
from Foo_no_all import foo


# In[6]:


foo.a


# # `__all__` in the `__init_all.py`
# <hr style="border:2px solid black"> </hr>

# In[7]:


from Foo import *


# In[8]:


foo.a


# In[9]:


foo1.a


# In[10]:


foo2.a


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - [What is __init__.py? : A guide](https://careerkarma.com/blog/what-is-init-py/)
# - [Why can I import successfully without __init__.py?](https://stackoverflow.com/questions/37974843/why-can-i-import-successfully-without-init-py)
#
# </font>
# </div>

# In[ ]:
