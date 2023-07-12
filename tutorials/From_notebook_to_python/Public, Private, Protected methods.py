#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Public,-Private,-Protected-attributes" data-toc-modified-id="Public,-Private,-Protected-attributes-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Public, Private, Protected attributes</a></span></li><li><span><a href="#Public,-Private,-Protected-methods" data-toc-modified-id="Public,-Private,-Protected-methods-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Public, Private, Protected methods</a></span></li><li><span><a href="#References" data-toc-modified-id="References-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Public, Private, Protected methods
#
# </font>
# </div>

# # Public, Private, Protected attributes
# <hr style = "border:2px solid black" ></hr>

# ![image.png](attachment:image.png)

# <div class="alert alert-info">
# <font color=black>
#
# There are two ways to restrict the access to class attributes:
#
# 1. **protected**. First, we can prefix an attribute name with a leading underscore "_". It tells users of the class not to use this attribute unless, somebody writes a subclass.
# 2. **private**. Second, we can prefix an attribute name with two leading underscores "__". The attribute is now inaccessible and invisible from outside. It's neither possible to read nor write to those attributes except inside of the class definition itself.
#
# </font>
# </div>

# # Public, Private, Protected methods
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Who has not stumbled across this quote "we are all consenting adults here" in the Python community, yet? Unlike in other languages like C++, we can't really protect class methods from being used outside the class (i.e., by the API user).
# - All we can do is indicate methods as private to make clear that they are not to be used outside the class, but it really is up to the class user, since "we are all consenting adults here"!
# - So, when we want to mark a class method as private, we can put a single underscore in front of it.
# - If we additionally want to avoid name clashes with other classes that might use the same method names, we can prefix the name with a double-underscore to invoke the name mangling.
# - This doesn't prevent the class users to access this class member though, but they have to know the trick and also know that it is at their own risk...
#
# </font>
# </div>

# In[1]:


class my_class:
    def public_method(self):
        print("Hello public world!")

    def __private_method(self):
        print("Hello private world!")

    def call_private_method_in_class(self):
        self.__private_method()


# In[2]:


my_instance = my_class()


# In[3]:


dir(my_instance)


# In[4]:


my_instance.public_method()
my_instance._my_class__private_method()
my_instance.call_private_method_in_class()


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://nbviewer.org/github/rasbt/python_reference/blob/master/tutorials/not_so_obvious_python_stuff.ipynb?create=1
#
#
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[5]:


get_ipython().run_line_magic("load_ext", "watermark")
get_ipython().run_line_magic("watermark", "-v -iv")
