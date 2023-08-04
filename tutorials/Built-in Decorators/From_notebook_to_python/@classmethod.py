#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Class-decorators" data-toc-modified-id="Class-decorators-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Class decorators</a></span></li><li><span><a href="#@classmethod" data-toc-modified-id="@classmethod-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>@classmethod</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Example</a></span><ul class="toc-item"><li><span><a href="#Class-definition-with-@classmethod" data-toc-modified-id="Class-definition-with-@classmethod-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Class definition with <code>@classmethod</code></a></span></li><li><span><a href="#Class-instantiation-via-object" data-toc-modified-id="Class-instantiation-via-object-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Class instantiation via object</a></span></li><li><span><a href="#Class-instantiation-via-@classmethod" data-toc-modified-id="Class-instantiation-via-@classmethod-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Class instantiation via <code>@classmethod</code></a></span></li><li><span><a href="#Updating-the-job-dynamically" data-toc-modified-id="Updating-the-job-dynamically-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Updating the job dynamically</a></span></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** @classmethod
# 
# </font>
# </div>

# # Class decorators
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - `@property` is the pythonic way to introduce attributes is to make them public, and not introduce getters and setters to retrieve or change them.
# - `@classmethod` is used to add an additional constructor to the class.
# - `@staticmethod` is used to attach functions to classes so people won't misuse them in wrong places.
# 
# </font>
# </div>

# # @classmethod
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - `@classmethod` is bound to a class rather than an object.
# - Class methods can be called with a class **or** with an object. 
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


from datetime import date


# # Example
# <hr style = "border:2px solid black" ></hr>

# ## Class definition with `@classmethod`

# In[14]:


class Person:
    def __init__(self, name, age):
        """
        This will create the object by name and age
        """
        self.name = name
        self.age = age
        self.dummy = 3
        print("__init__ method is called")

    """
    This will create the object by name and year
    """
    @classmethod
    def fromBirthYear(cls, name, year):
        print("class method is called")
        # keep the construct the same, name, age
        return cls(name, date.today().year - year)

    def display(self):
        print("Name : ", self.name, "Age : ", self.age)


# ## Class instantiation via object

# In[15]:


person = Person('mayank', 21)
person.display()


# ## Class instantiation via `@classmethod`

# In[16]:


#
person1 = Person.fromBirthYear('mayank', 2000)
person1.display()

# The result is the same


# ## Updating the job dynamically

# In[18]:


# called by the class
person1 = Person('just something', 1000)
person1.display()


# In[19]:


# called by the object
person2 = person1.fromBirthYear('mayank', 2000)
person2.display()


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - https://www.geeksforgeeks.org/classmethod-in-python/
# 
# </font>
# </div>

# In[ ]:




