#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Idendity-is-always-implies-equality-==?" data-toc-modified-id="Idendity-is-always-implies-equality-==?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Idendity <code>is</code> always implies equality <code>==</code>?</a></span></li><li><span><a href="#References" data-toc-modified-id="References-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Equality vs. identity
# 
# </font>
# </div>

# 
# # Idendity `is` always implies equality `==`?
# <hr style = "border:2px solid black" ></hr>

# - This oddity occurs, because Python keeps an array of small integer objects (i.e., integers between -5 and 256.
# - This is because the specific implementation of python based on Cypython reuses objects for small integers 

# In[8]:


a = 1
b = 1
print('a is b', bool(a is b))
True

c = 999
d = 999
print('c is d', bool(c is d))


# - This is in fact a CPython artifact and **must not necessarily be true** in all implementations of Python!
# - So the take home message is: always use "==" for equality, "is" for identity!
# - This example demonstrates that this applies  indeed for integers in the range in -5 to 256:

# In[9]:


print('256 is 257-1', 256 is 257-1)
print('257 is 258-1', 257 is 258 - 1)
print('-5 is -6+1', -5 is -6+1)
print('-7 is -6-1', -7 is -6-1)


# In[10]:


a = 'hello world!'
b = 'hello world!'
print('a is b,', a is b)
print('a == b,', a == b)


# We would think that identity would always imply equality, but this is not always true, as we can see in the next example:

# In[11]:


a = float('nan')
print('a is a,', a is a)
print('a == a,', a == a)


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/not_so_obvious_python_stuff.ipynb?create=1
# - https://docs.python.org/2/c-api/int.html#PyInt_FromLong
# - http://python.net/%7Egoodger/projects/pycon/2007/idiomatic/handout.html#other-languages-have-variables
#     
# </font>
# </div>

# In[ ]:




