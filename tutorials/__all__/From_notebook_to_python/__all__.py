#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Definition" data-toc-modified-id="Definition-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Definition</a></span></li><li><span><a href="#What-if-_-all-_-is-not-used?" data-toc-modified-id="What-if-_-all-_-is-not-used?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>What if _ <em>all</em> _ is not used?</a></span></li><li><span><a href="#What-to-do-if-you-do-not-want-to-use-_-all-_?" data-toc-modified-id="What-to-do-if-you-do-not-want-to-use-_-all-_?-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>What to do if you do not want to use _ <em>all</em> _?</a></span></li><li><span><a href="#_-init-_-and-_-all-_?" data-toc-modified-id="_-init-_-and-_-all-_?-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>_ <em>init</em> _ and _ <em>all</em> _?</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# 
# **What?** `__all__`
# 
# 

# # Definition
# <hr style="border:2px solid black"> </hr>

# 
# - `__all__ = [string#1, sreing#2, ...]` allows to explictly tell python what variables get exported from a module when this syntax `from <module> import *` is used.
# - It declares the semantically "public" names from a module. If there is a name in `__all__`, users are expected to use it, and they can have the expectation that it will not change.
# 
# 

# In[1]:


get_ipython().system('ls')


# In[5]:


# Let is print on screen what inside foo.py
get_ipython().system('cat foo.py')


# In[2]:


from foo import *


# In[3]:


print(bar)
print(baz)


# In[4]:


# The following will trigger an exception, as "waz" is not exported by the module
print(waz)


# # What if _ _all_ _ is not used?
# <hr style="border:2px solid black"> </hr>

# 
# - If `__all__` is not used then the default behaviour is recovered.
# - The **dafault** behaviour of `import *` is to import all symbols that do not begin with an underscore, from the given namespace.
# - `__all__` affects the `from <module> import *` behavior **only**!
# 
# 

# In[7]:


from foo_1 import *


# In[2]:


get_ipython().system('cat foo_1.py')


# In[ ]:


# This means that you'll not be able to access directly these: waz, bar, baz


# In[4]:


print(baz)


# In[5]:


print(bar)


# In[8]:


print(baz)


# # What to do if you do not want to use _ _all_ _?
# <hr style="border:2px solid black"> </hr>

# 
# -  Members that are not mentioned in `__all__` are still accessible from outside the module and can be imported with from `<module> import <member>`.
# 
# 

# In[1]:


from foo_1 import waz,bar,baz


# In[2]:


print(waz)


# In[3]:


print(bar)


# In[5]:


print(baz)


# # _ _init_ _ and _ _all_ _?
# <hr style="border:2px solid black"> </hr>

# 
# -  The `__init__.py` files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path.
# 
# - `__init__.py` can be left empty, but it can also execute initialization code for the package or set the `__all__` variable.
# 
# 

# # Conclusions
# <hr style="border:2px solid black"> </hr>

# 
# - Remember that `__all__` affects only the `from <module> import *` syntax only.
# - The syntax `import *` is not recommended anyway so it is up to you to decide how to use it.
# - **This sounds a bit confusion! ?** The confusion comes from the fact that are modules designed to be used with `import *`. A good hint if this is the case is the presence of `__all__` or names starting with underscore in the module’s code.
#     
# 

# # References
# <hr style="border:2px solid black"> </hr>

# 
# - https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python
# 
# 

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[1]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv')


# In[ ]:




