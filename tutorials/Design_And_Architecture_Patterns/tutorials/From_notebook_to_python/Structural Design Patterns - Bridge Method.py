#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Structural-Design-Patterns" data-toc-modified-id="Structural-Design-Patterns-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Structural Design Patterns</a></span></li><li><span><a href="#Bridge-Method" data-toc-modified-id="Bridge-Method-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Bridge Method</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Structural Design Patterns - Bridge Method
# 
# </font>
# </div>

# # Structural Design Patterns
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - **Structural Design Patterns** are used to establish relation between software components in particular settings.
#     - [ ] Adapter Method
#     - [x] Bridge Method
#     - [ ] Composite Method
#     - [ ] Decorator Method
#     - [ ] Facade Method
#     - [ ] Proxy Method
#     - [ ] FlyWeight Method
# 
# </font>
# </div>

# # Bridge Method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - **Lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.**
# - Bridge patten helps untangle a complicated class hierarchy
# - The problem here is that there are two unrelated, parallel abstractions. One is implementation specific and other is implementation independent.
#     
# </font>
# </div>

# # Example
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - The scenario involves implementation-independent circle abstraction and implementation-dependent circle abstraction.
# - The second abstraction involves how to draw a circle, while the first one involves defining the properties of the circle and scaling it.
# - The solution tries to separate the abstraction into two different class hierarchies.
#     
# </font>
# </div>

# In[1]:


class DrawingAPIOne:
    """Implementation-specific abstraction : concrete class 1"""

    def draw_circle(self, x, y, radius):
        print("API 1 drawing a curcle at ({}, {}) with radius {}".format(x, y, radius))


class DrawingAPITwo:
    """Implementation-specific abstraction : concrete class 2"""

    def draw_circle(self, x, y, radius):
        print("API 2 drawing a curcle at ({}, {}) with radius {}".format(x, y, radius))


# In[2]:


class Circle:
    """Implementation-independent abstraction"""

    def __init__(self, x, y, radius, drawing_api):
        """Initialize the necessary attributes"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation specific absratction taken crae of by another"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """Implementation-independent"""
        self._radius *= percent


# In[3]:


circle1 = Circle(1, 2, 3, DrawingAPIOne())
circle1.draw()

circle2 = Circle(1, 2, 3, DrawingAPITwo())
circle2.draw()


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-danger">
# <font color=black>
# 
# - **Advantages**:
#     - You can create platform-independent classes and apps.
#     - The client code works with high-level abstractions. It isn’t exposed to the platform details.
#     - Open/Closed Principle. You can introduce new abstractions and implementations independently from each other.
#     - Single Responsibility Principle. You can focus on high-level logic in the abstraction and on platform details in the implementation.
# - **Disadvantages**:
#     - You might make the code more complicated by applying the pattern to a highly cohesive class.
#     
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - [Bridge method](https://www.geeksforgeeks.org/bridge-method-python-design-patterns/)
# - [Bridge in Python](https://refactoring.guru/design-patterns/bridge)
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




