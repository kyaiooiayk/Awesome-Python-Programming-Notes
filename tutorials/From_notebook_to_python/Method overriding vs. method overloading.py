#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Function-vs.-method" data-toc-modified-id="Function-vs.-method-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Function vs. method</a></span></li><li><span><a href="#Polymorphism-and-Inheritance" data-toc-modified-id="Polymorphism-and-Inheritance-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Polymorphism and Inheritance</a></span></li><li><span><a href="#Method-overloading-vs.-overriding" data-toc-modified-id="Method-overloading-vs.-overriding-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Method overloading vs. overriding</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Method overriding vs. method overloading
#
# </font>
# </div>

# # Function vs. method
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Methods are functions that are bundled with objects.
# - Formally, methods are attributes of objects that are callable (i.e., can be called as functions)
#
# </font>
# </div>

# # Polymorphism and Inheritance
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Like in other programming languages, the child classes in Python also inherit methods and attributes from the parent class. We can redefine certain methods and attributes specifically to fit the child class, which is known as **Method Overriding**.
# - Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.
# - Here, we can see that the methods such as `__str__()`, which have not been overridden in the child classes, are used from the parent class.
# - Due to polymorphism, the Python interpreter automatically recognizes that the `fact()` method for object a(Square class) is overridden. So, it uses the one defined in the child class.
# - On the other hand, since the fact() method for object b isn't overridden, it is used from the Parent Shape class.
#
# </font>
# </div>

# In[9]:


from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())


# # Method overloading vs. overriding
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Like in other programming languages, the child classes in Python also inherit methods and attributes from the parent class. We can redefine certain methods and attributes specifically to fit the child class, which is known as **Method Overriding**.
# - **Method Overloading**, a way to create multiple methods with the same name but different arguments, is not possible in Python.
#
# </font>
# </div>

# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - [Polymorphism in Python](https://www.programiz.com/python-programming/polymorphism)
# - [Polymorphism tutorial](https://github.com/kyaiooiayk/Awesome-Python-Programming-Notes/blob/main/tutorials/GitHub_MD_rendering/Polymorphism.ipynb)
#
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[6]:


get_ipython().run_line_magic("load_ext", "watermark")
get_ipython().run_line_magic("watermark", "-v -iv -m")


# In[ ]:
