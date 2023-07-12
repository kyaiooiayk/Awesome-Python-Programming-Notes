#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Creational-Design-Patterns" data-toc-modified-id="Creational-Design-Patterns-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Creational Design Patterns</a></span></li><li><span><a href="#Abstract-Method" data-toc-modified-id="Abstract-Method-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Abstract Method</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example</a></span></li><li><span><a href="#Without-abstract-method" data-toc-modified-id="Without-abstract-method-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Without abstract method</a></span></li><li><span><a href="#With-abstract-method" data-toc-modified-id="With-abstract-method-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>With abstract method</a></span></li><li><span><a href="#Another-simple-example" data-toc-modified-id="Another-simple-example-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Another simple example</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Design Patterns - Abstarct Method
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
#     - [x] Abstract Factory Method
#     - [ ] Builder Method
#     - [ ] Prototype Method
#     - [ ] Singleton Method
#
# </font>
# </div>

# # Abstract Method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - **Abstract factory method is a creational design pattern that allows you to produce the families of related objects without specifying their concrete classes.**
# - Using the abstract factory method, we have the easiest ways to produce a similar type of many objects.
# - It provides a way to encapsulate a group of individual factories. Basically, here we try to abstract the creation of the objects depending on the logic, business, platform choice, etc.
#
# </font>
# </div>

# # Example
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Suppose you have to create a program that return all the Courses available, their Fee structure, their timings, and other important things. They will simply look at their system and will give you all the information you required. Looks simple? Think about the developers how they make the system so organized and how their website is so lubricative.
# - Developers will make unique classes for each course which will contain its properties like Fee structure, timings, and other things. But how they will call them and how will they instantiate their objects?
# - Here arises the problem, suppose initially there are only 3-4 courses available at GeeksforGeeks, but later they added 5 new courses. So, we have to manually instantiate their objects which is not a good thing according to the developer’s side.
#
# </font>
# </div>

# # Without abstract method
# <hr style = "border:2px solid black" ></hr>

# ![image.png](attachment:image.png)

# In[2]:


class DSA:

    """Class for Data Structure and Algorithms"""

    def price(self):
        return 11000

    def __str__(self):
        return "DSA"


class STL:

    """Class for Standard Template Library"""

    def price(self):
        return 8000

    def __str__(self):
        return "STL"


class SDE:

    """Class for Software Development Engineer"""

    def price(self):
        return 15000

    def __str__(self):
        return "SDE"


# In[3]:


sde = SDE()  # object for SDE class
dsa = DSA()  # object for DSA class
stl = STL()  # object for STL class

print(f"Name of the course is {sde} and its price is {sde.price()}")
print(f"Name of the course is {dsa} and its price is {dsa.price()}")
print(f"Name of the course is {stl} and its price is {stl.price()}")


# # With abstract method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Its solution is to replace the straightforward object construction calls with calls to the special abstract factory method.
# - Please note that, there will be **no difference** in the object creation but they are being called within the factory method.
# - Now we will create a unique class whose name is Course_At_GFG which will handle all the object instantiation automatically. Now, we don’t have to worry about how many courses we are adding after some time.
#
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[4]:


import random


class Course_At_GFG:

    """GeeksforGeeks portal for courses"""

    def __init__(self, courses_factory=None):
        """course factory is out abstract factory"""

        self.course_factory = courses_factory

    def show_course(self):
        """creates and shows courses using the abstract factory"""

        course = self.course_factory()

        print(f"We have a course named {course}")
        print(f"its price is {course.price()}")


# In[9]:


def random_course():
    """A random class for choosing the course"""

    return random.choice([SDE, STL, DSA])()


# In[10]:


course = Course_At_GFG(random_course)

for i in range(5):
    course.show_course()


# # Another simple example
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Abstract factory builds on the factory pattern. Abstract factory is useful when the user expects to receive a family of multiple related objects but doesn't have to know what fammily it is until runtime.
# - A factory returns a single object whereas a abstract factory return two or multiple related objects, like dog and dog food in our example
# - Abstract factory creates objects while concrete factories are often singletons.
#
# </font>
# </div>

# In[2]:


# Abstract Factory : pet factory
# Concrete Factory : dog factory and cat factory
# Concrete Product : Dog and dog food, Cat and cat food


class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        "Returns a Dog object"
        return Dog()

    def get_food(self):
        "Returns a Dog food object"
        return "Dog Food"


class Cat:
    """One of the objects to be returned"""

    def speak(self):
        return "meow!"

    def __str__(self):
        return "Cat"


class CatFactory:
    """Concrete Factory"""

    def get_pet(self):
        "Returns a Cat object"
        return Cat()

    def get_food(self):
        "Returns a Cat food object"
        return "Cat Food"


# In[3]:


class PetStore:
    """PetStore houses our abstract factory"""

    def __init__(self, pet_factory=None):
        """pet_factory is our abstract factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects returned"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is {}".format(pet))
        print("Our pet says {}".format(pet.speak()))
        print("Its food is {}".format(pet_food))


# In[4]:


# Create a concrete factory
factory1 = DogFactory()
factory2 = CatFactory()

# Create a pet store  housinf our abstract factory
shop = PetStore(factory1)

# Invoke the utility method to show the details of our method
shop.show_pet()


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-danger">
# <font color=black>
#
# - **Advantages**:
#     - This pattern is particularly useful when the client doesn’t know exactly what type to create.
#     - It is easy to introduce new variants of the products without breaking the existing client code.
#     - Products which we are getting from the factory are surely compatible with each other.
# - **Disadvantages**:
#     - Our simple code may become complicated due to the existence of a lot of classes.
#     - We end up with a huge number of small files i.e, cluttering of files.
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - [Abstact Factory Method](https://www.geeksforgeeks.org/abstract-factory-method-python-design-patterns/)
# - [Abstract Factory in Python](https://refactoring.guru/design-patterns/abstract-factory/python/example#example-0)
# - [Trying to make sense of abstract factory pattern in Python](https://stackoverflow.com/questions/41949514/trying-to-make-sense-of-abstract-factory-pattern-in-python)
#
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[1]:


get_ipython().run_line_magic("load_ext", "watermark")
get_ipython().run_line_magic("watermark", "-v -iv -m")


# In[ ]:
