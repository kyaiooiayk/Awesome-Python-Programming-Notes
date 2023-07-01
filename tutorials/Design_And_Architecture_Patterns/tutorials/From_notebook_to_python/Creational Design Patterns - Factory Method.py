#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Creational-Design-Patterns" data-toc-modified-id="Creational-Design-Patterns-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Creational Design Patterns</a></span></li><li><span><a href="#Factory-Method" data-toc-modified-id="Factory-Method-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Factory Method</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example</a></span></li><li><span><a href="#Without-factory-method" data-toc-modified-id="Without-factory-method-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Without factory method</a></span></li><li><span><a href="#With-factory-method" data-toc-modified-id="With-factory-method-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>With factory method</a></span></li><li><span><a href="#Another-simple-example" data-toc-modified-id="Another-simple-example-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Another simple example</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Design Patterns - Factory Method
#
# </font>
# </div>

# # Creational Design Patterns
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - **Creational Design Patterns** are about class instantiation or the object instantiation.
#     - [x] Factory Method
#     - [ ] Abstract Factory Method
#     - [ ] Builder Method
#     - [ ] Prototype Method
#     - [ ] Singleton Method
#
# </font>
# </div>

# # Factory Method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - **Factory method is a creational design pattern which solves the problem of creating product objects without specifying their concrete classes.**
# - Factory Method is a Creational Design Pattern that allows an interface or a class to create an object, but lets subclasses decide which class or object to instantiate.
# - Using the Factory method, we have the best ways to create an object. Here, objects are created without exposing the logic to the client, and for creating the new type of object, the client uses the same common interface.
#
# </font>
# </div>

# # Example
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Suppose we have created an app whose main purpose is to translate one language into another and currently our app works with 10 languages only. Now our app has become widely popular among people but the demand has grown suddenly to include 5 more languages.
# -It’s a piece of great news! only for the owner not for the developers. They have to change the whole code because now most part of the code is coupled with the existing languages only and that’s why developers have to make changes to the entire codebase which is really a difficult task to do.
#
# </font>
# </div>

# # Without factory method
# <hr style = "border:2px solid black" ></hr>

# In[2]:


# Python Code for Object Oriented Concepts without using Factory method


class FrenchLocalizer:

    """it simply returns the french version"""

    def __init__(self):
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette",
        }

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class SpanishLocalizer:
    """it simply returns the spanish version"""

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta", "cycle": "ciclo"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg


# In[3]:


# main method to call others
f = FrenchLocalizer()
e = EnglishLocalizer()
s = SpanishLocalizer()

# list of strings
message = ["car", "bike", "cycle"]

for msg in message:
    print(f.localize(msg))
    print(e.localize(msg))
    print(s.localize(msg))


# # With factory method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Its solution is to replace the straightforward object construction calls with calls to the special factory method.
# - Actually, there will be no difference in the object creation but they are being called within the factory method.
#
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[4]:


# Python Code for factory method it comes under the creational Design Pattern
def Factory(language="English"):
    """Factory Method"""

    # Create a dictionary
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    # Use the key to retrieve info from dic and return
    return localizers[language]()


# In[5]:


f = Factory("French")
e = Factory("English")
s = Factory("Spanish")

message = ["car", "bike", "cycle"]

for msg in message:
    print(f.localize(msg))
    print(e.localize(msg))
    print(s.localize(msg))


# # Another simple example
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Factory encapsulates object creation. **It is an object specialising in creating other objects**. Factory solves the following problem:
#     - When its uncertain what type of objects we are going to use at runtime.
#     - When the application needs to decide what classes to be used at runtime.
# - Let's suppose our pet shop sells dogs currently. Now we need to add a new pet i.e, a cat, here is how we can solve this by using the factory  method.
#
# </font>
# </div>

# In[2]:


class Dog:
    """A simple dog class"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "woof!"


class Cat:
    """A simple cat class"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "meow!"


# In[3]:


def get_pet(pet="dog"):
    """The Factory Method"""

    pets = dict(dog=Dog("Sheru"), cat=Cat("Kitty"))
    return pets[pet]


# In[4]:


print(get_pet("dog").speak())
print(get_pet("cat").speak())


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-danger">
# <font color=black>
#
# - **Advantages**:
#     - You avoid tight coupling between the creator and the concrete products.
#     - Single Responsibility Principle. You can move the product creation code into one place in the program, making the code easier to support.
#     - Open/Closed Principle. You can introduce new types of products into the program without breaking existing client code.
# - **Disadvantages**:
#     - The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern.
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - [Factory Method](https://www.geeksforgeeks.org/factory-method-python-design-patterns/)
# - [Factory Method in Python](https://refactoring.guru/design-patterns/factory-method/python/example#example-0)
# - [The Factory Method Pattern and Its Implementation in Python](https://realpython.com/factory-method-python/)
# - https://github.com/pyGuru123/Python-design-Patterns/tree/main/Creational%20Pattern
#
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[6]:


get_ipython().run_line_magic("load_ext", "watermark")
get_ipython().run_line_magic("watermark", "-v -iv -m")


# In[ ]:
