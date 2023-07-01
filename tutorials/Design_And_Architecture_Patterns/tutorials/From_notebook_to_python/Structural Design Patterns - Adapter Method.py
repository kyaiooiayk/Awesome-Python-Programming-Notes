#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Structural-Design-Patterns" data-toc-modified-id="Structural-Design-Patterns-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Structural Design Patterns</a></span></li><li><span><a href="#Adapter-Method" data-toc-modified-id="Adapter-Method-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Adapter Method</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Structural Design Patterns - Adapter Method
# 
# </font>
# </div>

# # Structural Design Patterns
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - **Structural Design Patterns** are used to establish relation between software components in particular settings.
#     - [x] Adapter Method
#     - [ ] Bridge Method
#     - [ ] Composite Method
#     - [ ] Decorator Method
#     - [ ] Facade Method
#     - [ ] Proxy Method
#     - [ ] FlyWeight Method
# 
# </font>
# </div>

# # Adapter Method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - **Allows objects with incompatible interfaces to collaborate.**
# - The Adapter pattern converts interface of a class to another the client is expecting.
# - The problem  we are trying to solve here is when that interfaces are incompatible between the client and the server.
#     
# </font>
# </div>

# # Example
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - The scenario here is that we have two methods speak_korean() for korean and speak_english() for english. The client expects to use a single method speak() for both.
# - The solution is to use the Adapter pattern which translates between the two methods for the client.
#     
# </font>
# </div>

# In[1]:


class Korean:
    """Korean Speaker"""

    def __init__(self):
        self.name = "korean"

    def speak_korean(self):
        return "An-neyong!"


class British:
    """English Speaker"""

    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello!"


# In[2]:


class Adapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, object, **adapted_method):
        self._object = object

        # Add a new dictionary which eastablishes the mapping between
        # generic method and individual methods.
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply returns the rest of the attributes"""
        return getattr(self._object, attr)


# In[3]:


# List to store speaker objects
objects = []

# Korean Speaker Object
korean = Korean()

# English Speaker Object
british = British()

# Append the objects to objects list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says {}".format(obj.name, obj.speak()))


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-danger">
# <font color=black>
# 
# - **Advantages**:
#     - Single Responsibility Principle. You can separate the interface or data conversion code from the primary business logic of the program.
#     - Open/Closed Principle. You can introduce new types of adapters into the program without breaking the existing client code, as long as they work with the adapters through the client interface.
# - **Disadvantages**:
#     - The overall complexity of the code increases because you need to introduce a set of new interfaces and classes. Sometimes it’s simpler just to change the service class so that it matches the rest of your code.
# 
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - [Adapter method](https://www.geeksforgeeks.org/adapter-method-python-design-patterns/)
# - [Adapter in Python](https://refactoring.guru/design-patterns/adapter/python/example#example-1)
# - https://github.com/pyGuru123/Python-design-Patterns/tree/main/Structural%20Pattern
#     
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[1]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv -m')


# In[ ]:




