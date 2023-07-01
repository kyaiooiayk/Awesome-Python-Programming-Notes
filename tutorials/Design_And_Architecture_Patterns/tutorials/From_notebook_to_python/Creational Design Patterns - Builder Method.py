#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Creational-Design-Patterns" data-toc-modified-id="Creational-Design-Patterns-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Creational Design Patterns</a></span></li><li><span><a href="#Builder-Method" data-toc-modified-id="Builder-Method-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Builder Method</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example</a></span></li><li><span><a href="#Without-builder-method" data-toc-modified-id="Without-builder-method-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Without builder method</a></span></li><li><span><a href="#With-builder-method" data-toc-modified-id="With-builder-method-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>With builder method</a></span></li><li><span><a href="#Another-example" data-toc-modified-id="Another-example-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Another example</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Creational Design Patterns - Builder Method
#
# </font>
# </div>

# # Creational Design Patterns
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - **Creational Design Patterns** are about class instantiation or the object instantiation.
#     - [ ] Factory Method
#     - [ ] Abstract Factory Method
#     - [x] Builder Method
#     - [ ] Prototype Method
#     - [ ] Singleton Method
#
# </font>
# </div>

# # Builder Method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - **Builder is a creational design pattern that lets you construct complex objects step by step.**
# - Builder Method is a Creation Design Pattern which aims to “Separate the construction of a complex object from its representation so that the same construction process can create different representations.”
# - It allows you to construct complex objects step by step. Here using the same construction code, we can produce different types and representations of the object easily.
# - It is basically designed to provide flexibility to the solutions to various object creation problems in object-oriented programming.
#
# </font>
# </div>

# # Example
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Imagine you want to join one of the elite batches of GeeksforGeeks.
# - So, you will go there and ask about the Fee structure, timings available, and batches about the course you want to join.
# - After looking at the system, they will tell you about the courses, their Fee structures, timings available and batches.
#
# </font>
# </div>

# # Without builder method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Unexperienced developers will create a separate and unique class for each and every course.
# - Then they will create separate object instantiation for each and every class although which is not required every time.
# - The main problem will arise when new courses will be added and developers have to add new classes as well because their code is not much flexible.
#
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[3]:


# concrete course
class DSA():

    """Class for Data Structures and Algorithms"""

    def Fee(self):
        self.fee = 8000

    def available_batches(self):
        self.batches = 5

    def __str__(self):
        return "DSA"

# concrete course


class SDE():

    """Class for Software development Engineer"""

    def Fee(self):
        self.fee = 10000

    def available_batches(self):
        self.batches = 4

    def __str__(self):
        return "SDE"

# concrete course


class STL():

    """class for Standard Template Library of C++"""

    def Fee(self):
        self.fee = 5000

    def available_batches(self):
        self.batches = 7

    def __str__(self):
        return "STL"


# In[5]:


sde = SDE() # object for SDE
dsa = DSA() # object for DSA
stl = STL() # object for STL

print(f'Name of Course: {sde} and its Fee: {sde.Fee}')
print(f'Name of Course: {stl} and its Fee: {stl.Fee}')
print(f'Name of Course: {dsa} and its Fee: {dsa.Fee}')


# # With builder method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Our final end product should be able to build any course.
# - We have to go through many steps before choosing a particular course such as finding details about the courses, syllabus, fee structure, timings, and batches.
#
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[6]:


# Abstract course
class Course:

    def __init__(self):
        self.Fee()
        self.available_batches()

    def Fee(self):
        raise NotImplementedError

    def available_batches(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)


class ComplexCourse:

    def __repr__(self):
        return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)

# Complex course


class Complexcourse(ComplexCourse):

    def Fee(self):
        self.fee = 7000

    def available_batches(self):
        self.batches = 6

# construct course


def construct_course(cls):

    course = cls()
    course.Fee()
    course.available_batches()

    return course  # return the course object


# In[9]:


dsa = DSA()  # object for DSA course
sde = SDE()  # object for SDE course
stl = STL()  # object for STL course

complex_course = construct_course(Complexcourse)
print(complex_course)

# Another example
<hr style = "border:2px solid black" ></hr>
# # Another example
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - A builder is a solution to an antipattern called as telescoping constructor. An antipattern is the opposite of best practice that we want to avoid. It occurs when a dev tries to create a complex object using a excessive number of constructors.
# - The Builder design pattern tries to solve this problem by dividing the process in 4 roles (divide & conquer strategy):
#     - **Director**: in charge of actually building the product
#     - **Abstract Builder**: provides all the necessary interfaces required to build the product
#     - **Concrete Builder**: inherits from abstract builder and implements the details of the interface
#     - **Product**: represents the object being built.
# - Builder pattern does not rely on polymorphism unlike factory and abstract factory.
#
# </font>
# </div>

# In[4]:


# Here our objectibve is to build a car object and
# its details.

class Director():
    """Director"""

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder:
    """Abstract Builder"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    """Concrete Builder"""

    def add_model(self):
        self.car.model = "SkyLark"

    def add_tires(self):
        self.car.tires = "Regular Tires"

    def add_engine(self):
        self.car.engine = "Turbo Engine"


class Car():
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return "{} | {} | {}".format(self.model, self.tires, self.engine)


# In[5]:


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()


# In[7]:


# I am not sure is working properly here!
print(car)


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-danger">
# <font color=black>
#
# - **Advantages**:
#     - You can construct objects step-by-step, defer construction steps or run steps recursively.
#     - You can reuse the same construction code when building various representations of products.
#     - Single Responsibility Principle. You can isolate complex construction code from the business logic of the product.
# - **Disadvantages**:
#     - The overall complexity of the code increases since the pattern requires creating multiple new classes.
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - [Builder Method](https://refactoring.guru/design-patterns/builder)
# - [Builder in Python](https://refactoring.guru/design-patterns/builder/python/example#lang-features)
# - https://github.com/pyGuru123/Python-design-Patterns/tree/main/Creational%20Pattern
#
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[1]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv -m')


# In[ ]:
