#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Minimal-class-design" data-toc-modified-id="Minimal-class-design-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Minimal class design</a></span></li><li><span><a href="#Defining-a-class" data-toc-modified-id="Defining-a-class-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Defining a class</a></span></li><li><span><a href="#Dynamic-attributes" data-toc-modified-id="Dynamic-attributes-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Dynamic attributes</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Class construction
# 
# </font>
# </div>

# # Minimal class design
# <hr style = "border:2px solid black" ></hr>

# In[1]:


class Robot:
    pass


x = Robot()
y = Robot()
y2 = y
print(y == y2)
print(y == x)


# # Defining a class
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - A class is like a **blueprint** for creating an object.
# - By creating a class you render your code more manageable and more maintainable.
# - While the class is the blueprint, an **instance** is an object that is built from a class and **contains real data**.
# - Put another way, a class is like a form or questionnaire. An instance is like a form that has been filled out with information.
# 
# 
# - You can give `.__init__()` any number of parameters, but the first parameter will always be a variable called self. 
# - When a new class instance is created, the instance is automatically passed to the `self` parameter in .__init__() so that new attributes can be defined on the object.
# 
# 
# - Attributes created in .__init__() are called **instance attributes**.
# - Attributes created outside .__init__() are called **class attributes**.
# - Use class attributes to define properties that should have the same value for every class instance. Use instance attributes for properties that vary from one instance to another.
# 
# </font>
# </div>

# In[1]:


class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Creates an instance attribute called name and assigns to it the value of the name parameter.
        self.name = name
        # Creates an instance attribute called age and assigns to it the value of the age parameter.
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - Creating a new object from a class is called **instantiating** an object.
# - This funny-looking string of letters and numbers is a memory address that indicates where the Dog object is stored in your computer’s memory
# 
# </font>
# </div>

# In[2]:


Dog("Pingo", 3)


# In[3]:


a = Dog("Pingo", 3)
b = Dog("Pingo", 3)
# This returns falso because the two object are different meaning stored at two difference place even if we
# instantiated them with the same parameters.
a == b


# In[4]:


Pingo = Dog("Pingo", 3)


# In[5]:


dir(Pingo)


# In[6]:


print(Pingo.name)
print(Pingo.age)
print(Pingo.species)


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - Although the attributes are guaranteed to exist, their values can be changed **dynamically**.
# 
# </font>
# </div>

# In[7]:


Pingo.age = 8
print(Pingo.age)


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - You can decided what gets printed by defining a special instance method called `.__str__()`. 
# - This message is called directly by the function `print`.
# - So instead of getting a strangle looking memory address we get a nice string.
# - **Dunder** methods because they begin and end with double underscores. There are many dunder methods that you can use to customize classes in Python. 
# 
# </font>
# </div>

# In[8]:


# Look what happens if we do not use paranthesis
print(Pingo.__str__)
print(Pingo.__str__())


# In[9]:


print(Pingo)


# # Dynamic attributes
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - As you'll learn in python many things are possible but generally there is only one best pythonic way  of doing it. This is also true for attributes.
# - Attributes can be created in two ways:
#     
#     - Attributes are created inside a class definition via dunder method `__init__` and this is the pythonic way of doing it. This will also take the name object attribute as they come from a formal object created via a class instantiation.
#     - However, attribute can also be created dynamically for existing instances of a class. We do this by joining an arbitrary name to the instance name, separated by a dot `.`. This is not the way to properly create instance. Hence, it is possible to assign attributes to most class instances, but this has nothing to do with defining classes.  attributes. 
#     
# </font>
# </div>
# 

# In[4]:


class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name):
        # Creates an instance attribute called name and assigns to it the value of the name parameter.
        self.name = name

# Instantiate class
a = Dog("Pingo")
# Get object attribute
print(a.name)
print(a.__dict__)


# In[5]:


class Dog:
    pass

# Instantiate class
a.name = "Pingo"
# Get object attribute
print(a.name)
print(a.__dict__)


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - https://realpython.com/python3-object-oriented-programming/
# - https://github.com/yhilpisch/py4fi2nd/blob/master/code/ch06/06_object_orientation.ipynb
# - Hilpisch, Yves. Python for finance: mastering data-driven finance. O'Reilly Media, 2018.
# - [Object-Oriented Programming in Python](https://python-textbok.readthedocs.io/en/1.0/)
# 
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[20]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv')

