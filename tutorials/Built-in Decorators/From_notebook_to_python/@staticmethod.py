#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Class-Decorators" data-toc-modified-id="Class-Decorators-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Class Decorators</a></span></li><li><span><a href="#@staticmethod" data-toc-modified-id="@staticmethod-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>@staticmethod</a></span></li><li><span><a href="#Example-#1" data-toc-modified-id="Example-#1-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Example #1</a></span></li><li><span><a href="#Example-#2" data-toc-modified-id="Example-#2-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Example #2</a></span></li><li><span><a href="#Syntactic-sugar" data-toc-modified-id="Syntactic-sugar-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Syntactic sugar</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** @staticmethod
#
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


import time


# # Class Decorators
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - `@property` is the pythonic way to introduce attributes is to make them public, and not introduce getters and setters to retrieve or change them.
# - `@classmethod` is used to add additional constructor to the class.
# - `@staticmethod` is used to attach functions to classes so people won't misuse them in wrong places.
#
# </font>
# </div>

# # @staticmethod
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - The purpose of **@staticmethod** is to attach functions to classes.
# - We do this to improve the **findability** of the function and to make sure that people are using the function in the appropriate context.
# - Behind the scenes Python simply enforces the access restrictions by not passing in the `self` or the `cls` argument when a static method gets called using the dot syntax. This confirms that static methods can neither access the object instance state nor the class state. They work like regular functions but belong to the clas’s (and every instance’s) namespace.
#
# </font>
# </div>

# # Example #1
# <hr style = "border:2px solid black" ></hr>

# In[4]:


class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        print("__init__ method is called")

    # Alternate constructor
    @classmethod
    def today(cls):
        print("called WITHOUTH instantiation via @static method")
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    # the logic belongs with the date class
    @staticmethod
    def show_tomorrow_date():
        print("called ONLY AFTER instantiation")
        t = time.localtime()
        return t.tm_year, t.tm_mon, t.tm_mday + 1


# In[5]:


a = Date
a.show_tomorrow_date()


# In[6]:


Date.show_tomorrow_date()


# # Example #2
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Normal attributes are added under `__init__` and these are called instance or object attributes, but there are some attributes that hold for all instance. So we can further abstarct it and make a class attribute.
# - Class attribuets are different from instance attributes.
#
# </font>
# </div>

# In[1]:


class Car(object):
    # This is a class attribute
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod
    def make_car_sound():
        print("Vrummmmm!")


# In[2]:


polo = Car("WV", "Polo")


# In[3]:


polo.__dir__()


# In[5]:


dir(Car)


# <div class="alert alert-info">
# <font color=black>
#
# - Since we know wheels is a class attribute we can also access it via the class name directly without needing an instance.
# - However, class instance method can access class attributes via `self` as well.
# - Having said that, there is a class methods that do not have access to `self.` This is called a **static method**.
#
# </font>
# </div>

# In[ ]:


print(polo.wheels)
print(Car.wheels)


# In[ ]:


polo.make


# In[ ]:


polo.model


# <div class="alert alert-info">
# <font color=black>
#
# - Static methods like class attributes do not need a class instance (object) to be called.
# - Thus static methods do not have a `self` parameter. In python this is done using `@staticmethod` decorator.
# - Please note that `make_car_sound` does not give you access to `self`.
# - On a more intuitive side, the car make always the same sound regardless of the brands (not strictly true, but you get the drift.)
#
# </font>
# </div>

# In[ ]:


Car.make_car_sound()


# In[ ]:


polo.make_car_sound()


# # Syntactic sugar
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The decorator syntax is merely **syntactic sugar**, the following two function definitions are semantically equivalent
# - The same concept exists for classes, but is less comonly used.
#
# ```
# def f(...):
#     ...
# f = staticmethod(f)
#
# # Is equivalent to
# @staticmethod
# def f(...)
#     ...
# ```
#
# </font>
# </div>

# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-danger">
# <font color=black>
#
# - `@classmethod` it is a class decorator with access to `self`; it provides another way to construct the class.
# - `@staticmethod` it is a class decorator without access to `self`; it provides a mechanism to attached method to class (hence improving the findability) and it allows to protect the method usage.
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - http://nbviewer.jupyter.org/github/ethen8181/machine-learning/blob/master/python/class.ipynb
# - [Python Tutorials: Python @property](http://www.programiz.com/python-programming/property)
# - [Onlines Python Course Notes: Properties vs. Getters and Setters](http://www.python-course.eu/python3_properties.php)
# - https://realpython.com/instance-class-and-static-methods-demystified/
#
# </font>
# </div>
