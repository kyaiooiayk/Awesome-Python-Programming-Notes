#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-encapsulation?" data-toc-modified-id="What-is-encapsulation?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is encapsulation?</a></span></li><li><span><a href="#Public,-Private,-Protected" data-toc-modified-id="Public,-Private,-Protected-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Public, Private, Protected</a></span></li><li><span><a href="#Class-Decorators" data-toc-modified-id="Class-Decorators-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Class Decorators</a></span><ul class="toc-item"><li><span><a href="#@Property" data-toc-modified-id="@Property-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>@Property</a></span></li><li><span><a href="#@classmethod-and-@staticmethod" data-toc-modified-id="@classmethod-and-@staticmethod-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>@classmethod and @staticmethod</a></span></li></ul></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Public, Private, Protected attributes
#
# </font>
# </div>

# # What is encapsulation?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Encapsulation is seen as the bundling of data with the methods that operate on that data.
# - It is often accomplished by providing two kinds of methods for attributes.
# - The methods for retrieving or accessing the values of attributes are called **getter methods**. Getter methods do not change the values of attributes, they just return the values.
# - The methods used for changing the values of attributes are called **setter methods**.
# - There is a difference and here is the relationship: abstraction = encapsulation + hiding. Essentially abstraction is present, iff hiding and encapsulation is used.
#
# </font>
# </div>

# # Public, Private, Protected
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

# In[1]:


class A:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"


instantiationOfA = A()


# In[2]:


print(instantiationOfA.public)
print(instantiationOfA._protected)
print(instantiationOfA._A__private)


# <div class="alert alert-info">
# <font color=black>
#
# - Whenever we assign or retrieve any object attribute Python searches it in the object's `__dict__` dictionary
# - When the Python compiler sees a private attribute, it actually transforms the actual name to `_[Class name]__[private attribute name]`.
# - **In practice** it is more common to use public and protected attribute,
#
# </font>
# </div>

# In[3]:


print(instantiationOfA.__dict__)


# # Class Decorators
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - `@property` The Pythonic way to introduce attributes is to make them public, and not introduce getters and setters to retrieve or change them.
# - `@classmethod` To add additional constructor to the class.
# - `@staticmethod` To attach functions to classes so people won't misuse them in wrong places.
#
# </font>
# </div>

# ## @Property

# <div class="alert alert-info">
# <font color=black>
#
# - Let's assume one day we decide to make a class that could store the temperature in degree Celsius. The temperature will be a private method, so our end-users won't have direct access to it.
#
# - The class will also implement a method to convert the temperature into degree Fahrenheit. And we also want to implement a value constraint to the temperature, so that it cannot go below -273 degree Celsius. One way of doing this is to define a getter and setter interfaces to manipulate it.
#
# </font>
# </div>

# In[4]:


class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")

        self._temperature = value


# In[5]:


# c = Celsius(-277) # this returns an error
c = Celsius(37)
c.get_temperature()


# <div class="alert alert-info">
# <font color=black>
#
# - Instead of that, now the **property** way.
# - Where we define the `@property` and the `@[attribute name].setter`.
#
# </font>
# </div>

# In[6]:


class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # have access to the value like it is an attribute instead of a method
    @property
    def temperature(self):
        return self._temperature

    # like accessing the attribute with an extra layer of error checking
    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")

        print("Setting value")
        self._temperature = value


# In[7]:


c = Celsius(37)

# much easier to access then the getter, setter way
print(c.temperature)

# note that you can still access the private attribute
# and violate the temperature checking,
# but then it's the users fault not yours
c._temperature = -300
print(c._temperature)

# accessing the attribute will return the ValueError error
# c.temperature = -300


# ## @classmethod and @staticmethod

# <div class="alert alert-info">
# <font color=black>
#
# - `@classmethods` create alternative constructors for the class.
# - An example of this behavior is there are different ways to construct a dictionary.
#
# </font>
# </div>

# In[8]:


print(dict.fromkeys(["raymond", "rachel", "mathew"]))


# In[9]:


import time


class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


# Primary
a = Date(2012, 12, 21)
print(a.__dict__)

# Alternate
b = Date.today()
print(b.__dict__)


# The `cls` is critical, as it is an object that holds the class itself. This makes them work with inheritance.

# In[10]:


class NewDate(Date):
    pass


# Creates an instance of Date (cls=Date)
c = Date.today()
print(c.__dict__)

# Creates an instance of NewDate (cls=NewDate)
d = NewDate.today()
print(d.__dict__)


# The purpose of **@staticmethod** is to attach functions to classes. We do this to improve the findability of the function and to make sure that people are using the function in the appropriate context.

# In[11]:


class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    # the logic belongs with the date class
    @staticmethod
    def show_tomorrow_date():
        t = time.localtime()
        return t.tm_year, t.tm_mon, t.tm_mday + 1


# In[12]:


Date.show_tomorrow_date()


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-danger">
# <font color=black>
#
# | Naming | Type | Meaning |
# | ---- | ---- | ------- |
# | `name`| Public | Attribute can be freely used inside or outside a class definition |
# |`_name`| Protected | Attribute should not be used outside the class definition, unless inside a subclass definition |
# |`__name`| Private| Attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes, except inside the class definition itself |
#
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - http://nbviewer.jupyter.org/github/ethen8181/machine-learning/blob/master/python/class.ipynb
# - [Python Tutorials: Python @property](http://www.programiz.com/python-programming/property)
# - [Onlines Python Course Notes: Properties vs. Getters and Setters](http://www.python-course.eu/python3_properties.php)
# - https://python-course.eu/oop/object-oriented-programming.php
#
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[13]:


get_ipython().run_line_magic("load_ext", "watermark")
get_ipython().run_line_magic("watermark", "-v -iv")
