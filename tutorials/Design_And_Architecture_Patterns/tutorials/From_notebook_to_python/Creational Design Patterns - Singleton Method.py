#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Creational-Design-Patterns" data-toc-modified-id="Creational-Design-Patterns-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Creational Design Patterns</a></span></li><li><span><a href="#Singleton-Method" data-toc-modified-id="Singleton-Method-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Singleton Method</a></span></li><li><span><a href="#Naive-singleton-implementation" data-toc-modified-id="Naive-singleton-implementation-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Naive singleton implementation</a></span></li><li><span><a href="#Thread-safe-implementation" data-toc-modified-id="Thread-safe-implementation-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Thread-safe implementation</a></span></li><li><span><a href="#Another-simple-example" data-toc-modified-id="Another-simple-example-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Another simple example</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Creational Design Patterns - Singleton Method
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
#     - [ ] Builder Method
#     - [ ] Prototype Method
#     - [x] Singleton Method
#
# </font>
# </div>

# # Singleton Method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - **Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.**
# - The singleton pattern is a design pattern that restricts the instantiation of a class to one object.
# - A lot of developers consider the Singleton pattern an **antipattern**. That’s why its usage is on the decline in Python code.
#
# </font>
# </div>

# # Naive singleton implementation
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - It’s pretty easy to implement a sloppy Singleton. You just need to hide the constructor and implement a static creation method.
# - The same class behaves incorrectly in a multithreaded environment. Multiple threads can call the creation method simultaneously and get several instances of Singleton class.
# - See file named `singleton_naive.py`
#
# </font>
# </div>

# In[17]:


get_ipython().system("python singleton_naive_implementation.py")


# # Thread-safe implementation
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - To fix the problem, you have to synchronize threads during the first creation of the Singleton object.
# - See file named `thread_safe_singleton_implementation.py`
#
# </font>
# </div>

# In[19]:


get_ipython().system("python thread_safe_singleton_implementation.py")


# # Another simple example
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - Singleton is used when you want to allow *only one object* to be created from a class. Its an object oriented way of providing global variables.
# - In python community, a **borg** is a term which allows creation of multiple instances but they all share same state, unlike singleton.
# - Lets say there's a need of keeping cache of information shared by multiple objects, it can be done either keeping the information in a singleton or sharing it under borg object.
#
# </font>
# </div>

# In[3]:


class Borg:
    """The Borg design pattern"""

    _shared_data = {}  # Attribute dictionary

    def __init__(self):
        # All the objects of the borg will share
        # the same dict thus making it act like a
        # global variable.
        self.__dict__ = self._shared_data


class Singleton(Borg):
    """The Singleton design pattern class"""

    def __init__(self, **kwargs):
        super(Borg, self).__init__()
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data)


# In[4]:


# Create a singleton object and add our first acronym
s1 = Singleton(HTTP="Hyper Text Transfer Protocol")
print(s1)

# Create anothe singleton object and add ANOTHER acronym
s2 = Singleton(SMTP="Simple Mail Transfer Protocol")
print(s2)


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-danger">
# <font color=black>
#
# - **Advantages**:
#     - Initializations: An object created by the Singleton method is initialized only when it is requested for the first time.
#     - Access to the object: We got global access to the instance of the object.
#     - Count of instances: In singleton, method classes can’t have more than one instance
# - **Disadvantages**:
#     - Multithread Environment: It’s not easy to use the singleton method in a multithread environment, because we have to take care that the multithread wouldn’t create a singleton object several times.
#     - Single responsibility principle: As the Singleton method is solving two problems at a single time, it doesn’t follow the single responsibility principle.
#     - Unit testing process: As they introduce the global state to the application, it makes the unit testing very hard.
#
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - [Singleton Method](https://www.geeksforgeeks.org/singleton-method-python-design-patterns/)
# - [Singleton in Python](https://refactoring.guru/design-patterns/singleton/python/example#example-1)
# - https://github.com/pyGuru123/Python-design-Patterns/tree/main/Creational%20Pattern
#
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[1]:


get_ipython().run_line_magic("load_ext", "watermark")
get_ipython().run_line_magic("watermark", "-v -iv -m")


# In[ ]:
