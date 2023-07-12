#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#From-2.x-to-3.x-new-class-definition" data-toc-modified-id="From-2.x-to-3.x-new-class-definition-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>From 2.x to 3.x new class definition</a></span></li><li><span><a href="#class()-vs.-class-vs.-class(object)" data-toc-modified-id="class()-vs.-class-vs.-class(object)-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>class() vs. class vs. class(object)</a></span></li><li><span><a href="#How-about-compatibility?" data-toc-modified-id="How-about-compatibility?-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>How about compatibility?</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** From 2.x to 3.x new class definition
#
# </font>
# </div>

# # From 2.x to 3.x new class definition
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Old class style are generally referred to as classical class. A classical class is any class that does not inherit form `object`. However, old classic class have been removed in python 3.x.
#
#
# - In short:
#     - **New-style classes** inherit from object, or from another new-style class.
#     - **Old-style classes** don't.
#
#
# </font>
# </div>

# In[1]:


class NewStyleClass(object):
    pass


class AnotherNewStyleClass(NewStyleClass):
    pass


# In[2]:


class OldStyleClass:
    pass


# In[3]:


dir(NewStyleClass)


# In[4]:


dir(AnotherNewStyleClass)


# In[5]:


dir(OldStyleClass)


# In[6]:


print(type(NewStyleClass))
print(type(AnotherNewStyleClass))
print(type(OldStyleClass))


# # class() vs. class vs. class(object)
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - `class A: pass` and `class A(): pass` are strictly equivalent.
# - The first means **A doesn't inherit of any parent class** and the second means **A inherits of no parent class**.
# - That's quite similar to not is and is not
#
# </font>
# </div>

# # How about compatibility?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - In 3.X, the inheritance of `object` is **automatically** assumed (meaning that we've got no way to not inherit `object` in 3.X).
# - For the **backward compatibility reason**, it is not bad to keep `class(object)` there though.
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python
# - https://www.sololearn.com/Discuss/2181707/python-difference-between-defining-a-class-with-and-without-empty-parentheses
#
# </font>
# </div>

# In[ ]:
