#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-encapsulation?" data-toc-modified-id="What-is-encapsulation?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is encapsulation?</a></span></li><li><span><a href="#Class-Decorators" data-toc-modified-id="Class-Decorators-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Class Decorators</a></span></li><li><span><a href="#@Property" data-toc-modified-id="@Property-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>@Property</a></span><ul class="toc-item"><li><span><a href="#Method-#1---getter-&amp;-setter" data-toc-modified-id="Method-#1---getter-&amp;-setter-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Method #1 - getter &amp; setter</a></span></li><li><span><a href="#Method-#2---@property" data-toc-modified-id="Method-#2---@property-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Method #2 - @property</a></span></li><li><span><a href="#Comparison" data-toc-modified-id="Comparison-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Comparison</a></span></li></ul></li><li><span><a href="#@classmethod" data-toc-modified-id="@classmethod-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>@classmethod</a></span></li><li><span><a href="#@staticmethod" data-toc-modified-id="@staticmethod-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>@staticmethod</a></span></li><li><span><a href="#Comparing-@static,classmethod-and-normal-method" data-toc-modified-id="Comparing-@static,classmethod-and-normal-method-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Comparing @static,classmethod and normal method</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Class decorators
#
# </font>
# </div>

# # What is encapsulation?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Encapsulation is seen as the bundling of data with the methods that operate on that data.
# - It is often accomplished by providing two kinds of methods for attributes
# - The methods for retrieving or accessing the values of attributes are called **getter methods**. Getter methods do not change the values of attributes, they just return the values.
# - The methods used for changing the values of attributes are called **setter methods**.
#
# </font>
# </div>

# # Class Decorators
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - There are three types of class decorators:
#     - `@property` The Pythonic way to introduce attributes is to make them public, and not introduce getters and setters to retrieve or change them.
#     - `@classmethod` To add additional constructor to the class.
#     - `@staticmethod` To attach functions to classes so people won't misuse them in wrong places.
#
# </font>
# </div>

# # @Property
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Let's create a class that stores the temperature in degree Celsius.
# - The temperature will be a "private method", so our end-users won't have direct access to it.
# - The class will also implement a method to convert the temperature into degree Fahrenheit.
# - We also want to implement a value constraint to the temperature, so that it cannot go below -273 degree Celsius.
#
#
# - We have two way of doing this:
#     - One way of doing this is to define a getter and setter interfaces to manipulate it.
#     - The other way is to to use `@property`
#
# </font>
# </div>

# ## Method #1 - getter & setter

# In[6]:


class Celsius_v1:
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


# ## Method #2 - @property

# In[9]:


class Celsius_v2:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # Give access to the value like it is an attribute instead of a method
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


# ## Comparison

# In[25]:


c = Celsius_v1(37)
print("Setter-Getter method :", c.get_temperature())

cc = Celsius_v2(37)
# much easier to access then the getter, setter way
print("@property            :", cc.temperature)


# In[26]:


c = Celsius_v1(-300)
print(c.get_temperature())


# In[33]:


# accessing the attribute will return the ValueError error.
# But look at the error call. the code does much less calls
cc.temperature = -300


# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Note that you can still access the private attribute and violate the temperature checking,
# - However, it's the users fault not yours
#
# </font>
# </div>

# In[34]:


c._temperature = -300
print(c._temperature)

cc._temperature = -300
print(cc._temperature)


# <div class="alert alert-block alert-info">
# <font color=black>
#
# - In conclusion why should we have to use ` @property`?
#     - It simplifies the typing from `obj.get_temperature()` to `obj.temperature`
#     - it simplified the typing from `obj.set_temperature(val)` to `obj.temperature = val`.
#
#
# - Also, not using ` @property` can cause problems while dealing with hundreds of thousands of lines of codes.
# - The update was not backwards compatible. This is where`  @property` comes to rescue.
#
# </font>
# </div>

# # @classmethod
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - `@classmethod` create alternative constructors for the class.
# - An example of this behavior is the different ways to construct a dictionary.
# - The `cls` is critical, as it is an object that holds the class itself. This makes them work with inheritance.
#
# </font>
# </div>

# In[7]:


print(dict.fromkeys(["raymond", "rachel", "mathew"]))


# In[14]:


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
        print("@classmethod")
        print("Class name", cls.__name__)
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


# In[17]:


# Primary
a = Date(2012, 12, 21)
print(a.__dict__)


# In[18]:


# Alternate
b = Date.today()
print(b.__dict__)


# In[9]:


class NewDate(Date):
    pass


# Creates an instance of Date (cls=Date)
c = Date.today()
print(c.__dict__)

# Creates an instance of NewDate (cls=NewDate)
d = NewDate.today()
print(d.__dict__)


# # @staticmethod
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - The purpose of **@staticmethod** is to attach functions to classes.
# - We do this to improve the findability of the function and to make sure that people are using the function in the appropriate context.
# - Behind the scenes Python simply enforces the access restrictions by not passing in the self or the cls argument when a static method gets called using the dot syntax. This confirms that static methods can neither access the object instance state nor the class state. They work like regular functions but belong to the class’s (and every instance’s) namespace.
#
#
# </font>
# </div>

# In[18]:


class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        print("primary constructor")
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        print("alternative constructor")
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    # The logic belongs with the date class
    @staticmethod
    def show_tomorrow_date():
        print("static method")
        t = time.localtime()
        return t.tm_year, t.tm_mon, t.tm_mday + 1


# In[24]:


data = Date(2000, 1, 1)
print(data.__dict__)


# In[28]:


Date.today()


# In[29]:


import time

Date.show_tomorrow_date()


# In[30]:


# This example shows how thed method cannot be accessed via the object!
a = Date
a.show_tomorrow_date()


# # Comparing @static,classmethod and normal method
# <hr style="border:2px solid black"> </hr>

# In[11]:


class MyClass:
    def method(self):
        """
        Instance methods need a class insance and
        can access the instance through self
        """
        return "Instance methods called", self

    def classmethod(cls):
        """
        Class methods don't need a class instance.
        They can't access the instance self but
        they have access to the class itseld via cls.
        """
        return "Class method called", cls

    @staticmethod
    def staticmethod():
        """
        Static method don't have access to cls or self.
        They work like regular functions but belong to
        the class's namespace.
        """
        return "Static method called"


# In[12]:


# All method types can be called on a class instance
obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())


# In[14]:


# Calling method and classmethod fails if we only have the class object
MyClass.method()


# In[16]:


MyClass.classmethod()


# In[17]:


MyClass.staticmethod()


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - http://nbviewer.jupyter.org/github/ethen8181/machine-learning/blob/master/python/class.ipynb
# - [Python Tutorials: Python @property](http://www.programiz.com/python-programming/property)
# - [Onlines Python Course Notes: Properties vs. Getters and Setters](http://www.python-course.eu/python3_properties.php)
#
# </font>
# </div>

# In[ ]:
