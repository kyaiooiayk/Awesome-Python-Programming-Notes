#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Technical-aspects-of-OOP" data-toc-modified-id="Technical-aspects-of-OOP-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Technical aspects of OOP</a></span></li><li><span><a href="#What-is-polymorphism?" data-toc-modified-id="What-is-polymorphism?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>What is polymorphism?</a></span></li><li><span><a href="#Polymorphism-on-operator" data-toc-modified-id="Polymorphism-on-operator-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Polymorphism on operator</a></span></li><li><span><a href="#Polymorphism-on-function" data-toc-modified-id="Polymorphism-on-function-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Polymorphism on function</a></span></li><li><span><a href="#Polymorphism-on-class" data-toc-modified-id="Polymorphism-on-class-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Polymorphism on class</a></span></li><li><span><a href="#Polymorphism-and-Inheritance" data-toc-modified-id="Polymorphism-and-Inheritance-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Polymorphism and Inheritance</a></span></li><li><span><a href="#Method-overloading-vs.-overriding" data-toc-modified-id="Method-overloading-vs.-overriding-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Method overloading vs. overriding</a></span></li><li><span><a href="#References" data-toc-modified-id="References-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Polymorphism
# 
# </font>
# </div>

# # Technical aspects of OOP
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - [ ] **Abstraction**: the use of attributes and methods allows building abstract, flexible models of objects, with a focus on what is relevant and neglecting what is not needed.
# - [ ] **Modularity** implies the possibility of breaking code down into multiple modules which are then linked to form the complete codebase. 
# - [ ] **Inheritance** refers to the concept that one class can inherit attributes and meth‐ ods from another class.
# - [ ] **Aggregation** refers to the case in which an object is at least partly made up of multiple other objects that might exist independently.  
# - [ ] **Composition** is similar to aggregation, but here the single objects cannot exist independently of each other.
# - [x] **Polymorphism** can take on multiple forms. Of particular importance in a Python context is what is called duck typing. This refers to the fact that standard operations can be implemented on many different classes and their instances without knowing exactly what object one is dealing with.
# - [ ] **Encapsulation** refers to the approach of making data within a class accessible only via public methods. This approach might avoid unintended effects by sim‐ ply working with and possibly changing attribute values.
#     
# </font>
# </div>

# # What is polymorphism?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Polymorphism can take on multiple forms. Of particular importance in a Python context is what is called duck typing. This refers to the fact that standard operations can be implemented on many different classes and their instances without knowing exactly what object one is dealing with.
# - It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.
#     
# </font>
# </div>

# # Polymorphism on operator
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The operator `+` can be used to carry out different operations for distinct data types. 
# - For integer data types, `+` operator is used to perform arithmetic addition operation.
# - For string data types, + operator is used to perform concatenation.
#     
# </font>
# </div>

# In[1]:


num1 = 1
num2 = 2
print(num1+num2)


# In[2]:


str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)


# # Polymorphism on function
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - There are some functions in Python which are compatible to run with multiple data types.
# - One such function is the `len()` function. It can run with many data types in Python.
# - Here, we can see that many data types such as string, list, tuple, set, and dictionary can work with the len() function. However, we can see that it returns **specific** information about **specific** data types.  
#     
# </font>
# </div>

# ![image-2.png](attachment:image-2.png)

# In[4]:


print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))


# # Polymorphism on class
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - We can use the concept of polymorphism while creating class methods as Python allows different classes to have methods with the same name.
# - We can then later generalize calling these methods by disregarding the object we are working with. 
# - Here, we have created two classes Cat and Dog. They share a similar structure and have the same method names `info()` and `make_sound()`.
# - However, notice that we have not created a common superclass or linked the classes together in any way. Even then, we can pack these two different objects into a tuple and iterate through it using a common `animal` variable. - It is possible due to polymorphism.
#     
# </font>
# </div>

# In[5]:


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(
            f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(
            f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


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
        return pi*self.radius**2


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
#     
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[6]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv -m')


# In[ ]:




