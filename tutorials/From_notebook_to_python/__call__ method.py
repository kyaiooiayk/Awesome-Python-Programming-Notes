#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Definition" data-toc-modified-id="Definition-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Definition</a></span></li><li><span><a href="#_-call-_-vs.-_-init-_" data-toc-modified-id="_-call-_-vs.-_-init-_-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>_ <em>call</em> _ vs. _ <em>init</em> _</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#Example-#3" data-toc-modified-id="Example-#3-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Example #3</a></span></li><li><span><a href="#Example-#4" data-toc-modified-id="Example-#4-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Example #4</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** `__call__` method
# 
# </font>
# </div>

# # Definition
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - `__call__` is a built-in method which enables to write classes where the instances behave like functions and can be called like a function.
# - In practice: `object()` is shorthand for `object.__call__()`
# 
# </font>
# </div>

# # _ _call_ _ vs. _ _init_ _
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - `__init__()` is properly defined as Class Constructor which builds an instance of a class, whereas `__call__` makes such a instance callable as a function and therefore can be modifiable.
# - Technically `__init__` is called once by `__new__` when object is created, so that it can be initialised
# - But there are many scenarios where you might want to redefine your object, say you are done with your object, and may find a need for a new object. With `__call__` you can redefine the same object as if it were new.
# 
# </font>
# </div>

# # Example #1
# <hr style="border:2px solid black"> </hr>

# In[2]:


class Example():
    def __init__(self):
        print("Instance created")
    
    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method __call__")


# In[5]:


e = Example()


# In[8]:


e.__init__()


# In[9]:


e.__call__()


# # Example #2
# <hr style="border:2px solid black"> </hr>

# In[10]:


class Product():
    def __init__(self):
        print("Instance created")
    
    # Defining __call__ method
    def __call__(self, a, b):
        print("Instance is called via special method __call__")
        print(a*b)


# In[11]:


p = Product()


# In[13]:


p.__init__()


# In[15]:


# Is being call like if p was a function
p(2,3)


# In[14]:


# The cell above is equivalent to this call
p.__call__(2,3)


# # Example #3
# <hr style="border:2px solid black"> </hr>

# In[33]:


class Stuff(object):
    def __init__(self, x, y, Range):
        super(Stuff, self).__init__()
        self.x = x
        self.y = y
        self.Range = Range
    
    def __call__(self, x, y):
        self.x = x
        self.y = y
        print("__call__ with (%d, %d)" % (self.x, self.y))
    
    def __del__(self, x, y):
        del self.x
        del self.y
        del self.Range       
        


# In[34]:


s = Stuff(1, 2, 3)


# In[35]:


s.x


# In[36]:


s(7,8)


# In[37]:


s.x


# # Example #4
# <hr style="border:2px solid black"> </hr>

# In[2]:


class Sum():
    def __init__(self, x, y):        
        self.x = x
        self.y = y        
        print("__init__ with (%d, %d)" % (self.x, self.y))
    
    def __call__(self, x, y):
        self.x = x
        self.y = y        
        print("__call__ with (%d, %d)" % (self.x, self.y))
    
    def sum(self):
        return self.x + self.y        


# In[5]:


sum_1 = Sum(2,2)
sum_1.sum()


# In[12]:


sum_1 = Sum(2,2)
sum_1(3,3)


# In[17]:


sum_1 = Sum(2,2)
# This is equivalent to
sum_1.__call__(3,3)


# In[14]:


# You can also do this
sum_1 = Sum(2,2)(3,3)


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - https://www.geeksforgeeks.org/__call__-in-python/
# 
# </font>
# </div>

# In[ ]:




