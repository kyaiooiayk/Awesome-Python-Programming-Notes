#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-super()?" data-toc-modified-id="What-is-super()?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is super()?</a></span></li><li><span><a href="#Base-class" data-toc-modified-id="Base-class-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Base class</a></span></li><li><span><a href="#Derived-class-withouth-super()" data-toc-modified-id="Derived-class-withouth-super()-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Derived class withouth super()</a></span></li><li><span><a href="#Derived-class-with-super()" data-toc-modified-id="Derived-class-with-super()-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Derived class with super()</a></span></li><li><span><a href="#Comparison" data-toc-modified-id="Comparison-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Comparison</a></span></li><li><span><a href="#Multiple-Inheritance-Overview" data-toc-modified-id="Multiple-Inheritance-Overview-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Multiple Inheritance Overview</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Super()
# 
# </font>
# </div>

# # What is super()?

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - While Python isn’t purely an object-oriented language, it’s flexible enough and powerful enough to allow you to build your applications using the object-oriented paradigm. 
# - One of the ways in which Python achieves this is by supporting inheritance, which it does with `super()`. 
# 
# </font>
# </div>

# # Base class

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - We are going to create a base class.
# - Its methods will be inherited by a derived class.
# 
# </font>
# </div>

# In[14]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# # Derived class withouth super()

# In[15]:


class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


# # Derived class with super()

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - We are jsut adding a `_m` to distinguish the classes from the previous case.
# - The `_m_v2` is to account for the Python 3, the `super(Square, self)` call is EQUIVALENT to the parameterless `super()` call. The first parameter refers to the subclass Square, while the second parameter refers to a Square object which, in this case, is self
# 
# </font>
# </div>

# In[16]:


# Here we declare that the Square class inherits from the Rectangle class
class Square_m(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


# In[17]:


# Here we declare that the Square class inherits from the Rectangle class
class Square_m_v2(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


# # Comparison

# In[18]:


rectangle = Rectangle(2,4)
print("Rectangle area", rectangle.area())


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - Nothing special in this call, but the code, however, doesn’t reflect that relationship and thus has code that is essentially **repeated**. 
# - What if we can reuse the code written in the `Rectangle` class in the `Square` class. 
# 
# </font>
# </div>

# In[19]:


square = Square(4)
print("Square area (withouth super)", square.area())


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - Here, you’ve used `super()` to call the `__init__()` of the Rectangle class, allowing you to use it in the Square class without repeating code. 
# - The Square class inherited the `.area()` method from the Rectangle class.
# 
# </font>
# </div>

# In[20]:


square_m = Square_m(4)
print("Square area (with super)", square_m.area())


# In[21]:


square_m = Square_m_v2(4)
print("Square area (with super but how we used to do in python 2.x)", square_m.area())


# # Multiple Inheritance Overview 

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - In addition to single inheritance, Python supports multiple inheritance, in which a subclass can inherit from multiple superclasses that don’t necessarily inherit from each other (also known as sibling classes). 
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[22]:


class Triangle_SC1:
    """
    Superclass No1
    """
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print("Using area from square_C1")
        return 0.5 * self.base * self.height


# In[23]:


class Square_SC2:
    """
    Superclass No2
    """
    def __init__(self, length):
        self.length = length

    def area(self):
        print("Using area from square_C2")        
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - The problem, though, is that both superclasses (Triangle and Square) define a .area(). 
# - The **method resolution order (or MRO)** tells Python how to search for inherited methods. 
# - This comes in handy when you’re using super() because the MRO tells you exactly where Python will look for a method you’re calling with super() and in what order.
#  
# </font>
# </div>

# In[24]:


class RightPyramid(Square_SC2, Triangle_SC1):
    """
    The signature of the class is important.
    Writing (Square, Triangle) is not the same as (Triangle, Square)
    """
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


# In[25]:


RightPyramid.__mro__


# In[26]:


pyramid = RightPyramid(2, 4)
pyramid.area()


# # References

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - https://realpython.com/python-super/ 
# 
# </font>
# </div>

# In[ ]:




