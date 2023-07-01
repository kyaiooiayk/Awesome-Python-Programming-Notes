#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Structural-Design-Patterns" data-toc-modified-id="Structural-Design-Patterns-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Structural Design Patterns</a></span></li><li><span><a href="#Composite-Method" data-toc-modified-id="Composite-Method-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Composite Method</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Example</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Structural Design Patterns - Composite Method
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
#     - [ ] Bridge Method
#     - [x] Composite Method
#     - [ ] Decorator Method
#     - [ ] Facade Method
#     - [ ] Proxy Method
#     - [ ] FlyWeight Method
# 
# </font>
# </div>

# # Composite Method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - **Lets you compose objects into tree structures and then work with these structures as if they were individual objects.**
# - A composite design pattern maintains a tree data structure.
# - The problem here is to build a recursive tree data structure so that an element of the tree can have subelements.
#     
# </font>
# </div>

# # Example
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
# 
# - Here the scenerio is creating menu and submenu items, which can have further submenu items.
# - The solution consists of 3 major elements
# - `Component`: An abstract class
# - `Child`: A concrete class inherits from the component
# - `Composite`: A concrete class which also inherits from component. The composite class maintains child objects by ading and removing them to a tree data structure.
#     
# </font>
# </div>

# In[1]:


class Component:
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


# In[2]:


class Child(Component):
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we are going to store the name of the child item
        self.name = args[0]

    def component_function(self):
        # Print the name of the child item here
        print('{}'.format(self.name))


# In[3]:


class Composite(Component):
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we store name of the composite object
        self.name = args[0]

        # This is where we keep our child items
        self.children = []

    def append_child(self, child):
        """Method to add a new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """Method to remove a child item"""
        self.children.remove(child)

    def component_function(self):
        # Print the name of the composite object
        print('{}'.format(self.name))

        # Iterate through the child objects and initiate their component
        for child in self.children:
            child.component_function()


# In[4]:


# Build a composite submenu 1
sub1 = Composite("submenu1")

# Create new child submenu 11
sub11 = Child("submenu 11")
# Create new child submenu 12
sub12 = Child("submenu 12")


# In[5]:


# Add the submenu 11 to submenu 1
sub1.append_child(sub11)

# Add the submenu 12 to submenu 1
sub1.append_child(sub12)


# In[6]:


# Build a top level composite menu
top = Composite("topmenu")

# build a submenu 2 that is not a composite
sub2 = Child("submenu 2")

# Add submenu 1 and submenu 2 to top menu
top.append_child(sub1)
top.append_child(sub2)

# Testing top menu
top.component_function()


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-danger">
# <font color=black>
# 
# - **Advantages**:
#     - You can work with complex tree structures more conveniently: use polymorphism and recursion to your advantage.
#     - Open/Closed Principle. You can introduce new element types into the app without breaking the existing code, which now works with the object tree.
# - **Disadvantages**:
#     - It might be difficult to provide a common interface for classes whose functionality differs too much. In certain scenarios, you’d need to overgeneralize the component interface, making it harder to comprehend.
#     
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - [Composite method](https://www.geeksforgeeks.org/composite-method-python-design-patterns/)
# - [Composite in Python](https://refactoring.guru/design-patterns/composite)
# - https://github.com/pyGuru123/Python-design-Patterns/blob/main/Structural%20Pattern/composite.py
#     
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[7]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv -m')


# In[ ]:




