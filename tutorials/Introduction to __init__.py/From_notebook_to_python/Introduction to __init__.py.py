#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Option-#1---turn-your-folder-into-a-package" data-toc-modified-id="Option-#1---turn-your-folder-into-a-package-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Option #1 - turn your folder into a package</a></span></li><li><span><a href="#Option-#2---use-directly-__import__" data-toc-modified-id="Option-#2---use-directly-__import__-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Option #2 - use directly <code>__import__</code></a></span></li><li><span><a href="#Some-style-rules" data-toc-modified-id="Some-style-rules-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Some style rules</a></span></li><li><span><a href="#Shorten-the-notation" data-toc-modified-id="Shorten-the-notation-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Shorten the notation</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Introduction to `__init__.py`
#
# </font>
# </div>

# In[ ]:


get_ipython().system("ls")


# In[ ]:


get_ipython().system("ls my_sum")


# # Option #1 - turn your folder into a package
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - By adding the `__init__.py` we are turning our folder into a package.
# - This means we are able to use the syntax from import something
# - Inside the `__init__.py` file there is a sum function.
# - We'll now import it and give it a spin!
#
# </font>
# </div>

# In[ ]:


from my_sum import sum


# In[ ]:


sum([1, 2])


# # Option #2 - use directly `__import__`
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - What if you do not want to make a folder a package?
# - Python offer an alternative using the built-in `__import__()` function.
# - This is also useful if your filename **collides** with any standard library packages.
# - For example, math.py would collide with the math module.
#
# </font>
# </div>

# In[ ]:


target = __import__("my_sum")
sum1 = target.sum


# In[ ]:


sum1([1, 2])


# # Some style rules
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Do not put too much code in `__init__.py`. When projects grow in size, there may be subpackages all nested in a deep directory. In this case, calling `__init__.py` will cause calling all `__init__.py`files met while traversing the tree.
# - Thus, it is good practice to leave the `__init__.py` as empty as possible when there is no need to share the code.
#
# </font>
# </div>

# # Shorten the notation
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - You can use `__init__.py` to shorten your API.
# - Let’s say that the most important method of your code, `foo`, is found in the `Foo_package` module.
# - You can allow the users to import it as from your_package `from Foo_package import foo` instead of `from Foo_packaged import foo`, by simply adding: `from .Foo import foo`
#
# </font>
# </div>

# In[1]:


from Foo_package import foo


# In[2]:


foo


# In[5]:


from Foo_package.Foo import foo as foo1


# In[6]:


foo1


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - [How to build your first python package](https://towardsdatascience.com/how-to-build-your-first-python-package-6a00b02635c9)
#
# </font>
# </div>

# In[ ]:
