#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#History" data-toc-modified-id="History-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>History</a></span></li><li><span><a href="#What-is-OOP?" data-toc-modified-id="What-is-OOP?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>What is OOP?</a></span></li><li><span><a href="#Class,-attribute-&amp;-method" data-toc-modified-id="Class,-attribute-&amp;-method-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Class, attribute &amp; method</a></span></li><li><span><a href="#High-level-of-what-OOP-really-is" data-toc-modified-id="High-level-of-what-OOP-really-is-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>High-level of what OOP really is</a></span></li><li><span><a href="#Technical-aspects-of-OOP" data-toc-modified-id="Technical-aspects-of-OOP-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Technical aspects of OOP</a></span></li><li><span><a href="#Four-major-principles-of-object-orientation" data-toc-modified-id="Four-major-principles-of-object-orientation-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Four major principles of object-orientation</a></span><ul class="toc-item"><li><span><a href="#Data-Abstraction-=-Data-Encapsulation-+-Data-Hiding" data-toc-modified-id="Data-Abstraction-=-Data-Encapsulation-+-Data-Hiding-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>Data Abstraction = Data Encapsulation + Data Hiding</a></span></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# **What?** Object-Oriented Programming (OOP) in Python
#
# </font>
# </div>

# # History
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - The first programming language to use objects was Simula 67. As the name implies, **Simula 67** was introduced in the year 1967.
# - A major breakthrough for object-oriented programming came with the programming language **Smalltalk** in the 1970s.
#
# </font>
# </div>

# # What is OOP?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-info">
# <font color=black>
#
# - OOP stands for Object-oriented programming.
# - It is a **programming paradigm** that provides means of structuring a program by bundling related data, properties and behaviors into individual objects.
# - This is in constrast with another common programming paradigm: **procedural programming**. This structures a program like a recipe in that it provides a set of steps, in the form of functions and code blocks, that flow sequentially in order to complete a task.
# - Object Oriented Programming (OOP) is a programming paradigm based on the concept of "objects" that can contain data and code. The data is often implemented as attributes. Functions implement the associated code for the data and are usually referred to in object oriented jargon as **methods**. In OOP, computer programs are designed by being made up of objects that interact with each other via the methods.
#
# </font>
# </div>

# ![image.png](attachment:image.png)

# # Class, attribute & method
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - **Classes** are templates to create objects to avoid recreating them from scratch.
# - Classes define objects in terms of attributes and behaviors.
# - **Attributes** represents properties of an entity. It captures the current state of the entity.
# - **Methods** represents the behavior of the entity.
#
# </font>
# </div>

# # High-level of what OOP really is
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - OOPs has many technical aspects but from a way very high level, many of these aspects can be summarized by two generals goals in software engineering:
#     - **Reusability**: concepts like inheritance and polymorphism improve code reusability and increase the efficiency and productivity of the programmer. They also simplify code maintenance.
#     - **Nonredundancy**: avoiding double implementation effort and reducing debugging and testing
#
# </font>
# </div>

# # Technical aspects of OOP
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
# - **Abstraction**: the use of attributes and methods allows building abstract, flexible models of objects, with a focus on what is relevant and neglecting what is not needed.
# - **Modularity** implies the possibility of breaking code down into multiple modules which are then linked to form the complete codebase.
# - **Inheritance** refers to the concept that one class can inherit attributes and meth‐ ods from another class.
# - **Aggregation** refers to the case in which an object is at least partly made up of multiple other objects that might exist independently.
# - **Composition** is similar to aggregation, but here the single objects cannot exist independently of each other.
# - **Polymorphism** can take on multiple forms. Of particular importance in a Python context is what is called duck typing. This refers to the fact that standard operations can be implemented on many different classes and their instances without knowing exactly what object one is dealing with.
# - **Encapsulation** refers to the approach of making data within a class accessible only via public methods. This approach might avoid unintended effects by sim‐ ply working with and possibly changing attribute values.
#
# </font>
# </div>

# # Four major principles of object-orientation
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#
#
# - Encapsulation
# - Data Abstraction
# - Polymorphism
# - Inheritance
#
# </font>
# </div>

# ## Data Abstraction = Data Encapsulation + Data Hiding

# <div class="alert alert-info">
# <font color=black>
#
# - Data Abstraction, Data Encapsulation and Information Hiding are often confused while talking about OOP.
# - However, there is a difference and here is the relationship: **abstraction = encapsulation + hiding**.
# - Essentially abstraction is present, iff hiding and encapsulation is used.
# - Encapsulation is seen as the bundling of data with the methods that operate on that data. Information hiding on the other hand is the principle that some internal information or data is "hidden", so that it can't be accidentally changed. Data encapsulation via methods doesn't necessarily mean that the data is hidden. You might be capable of accessing and seeing the data anyway, but using the methods is recommended.
# - Encapsulation is often accomplished by providing two kinds of methods for attributes: The methods for retrieving or accessing the values of attributes are called getter methods. Getter methods do not change the values of attributes, they just return the values. The methods used for changing the values of attributes are called setter methods. **Attention**: there is a more pythonic way to achieve the same with `@property`.
#
# </font>
# </div>

# ![image.png](attachment:image.png)

# In[4]:


class Robot:
    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am ", self.name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


# In[5]:


x = Robot()
x.set_name("Henry")
x.say_hi()
y = Robot()
y.set_name(x.get_name())
print(y.get_name())


# In[6]:


# what if we'd like to avoid something like this?
x = Robot()
x.set_name(-44)
x.say_hi()
y = Robot()
y.set_name(x.get_name())
print(y.get_name())


# In[57]:


class Robot:
    def __init__(self, name=None):
        # the underscore means is "private" and protected
        # keep in mind that in python nothing is really private!
        self._name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am ", self.name)
        else:
            print("Hi, I am a robot without a name")

    # This is essentially the getter method
    @property
    def name(self):
        print("getter")
        return self._name

    @name.setter
    def name(self, new_name):
        print("setter")
        if type(new_name) == str:
            self._name = new_name
        else:
            raise Exception("Please enter a name not a number! Robots are also human!")

    @name.deleter
    def name(self):
        print("deleter")
        del self._name


# In[59]:


x = Robot()
x.name = "Henry"
x.say_hi()
x.name


# In[60]:


x = Robot()
x.name = 44
x.say_hi()
x.name


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-block alert-warning">
# <font color=black>
#
# - https://realpython.com/python3-object-oriented-programming/
# - https://github.com/yhilpisch/py4fi2nd/blob/master/code/ch06/06_object_orientation.ipynb
# - Hilpisch, Yves. Python for finance: mastering data-driven finance. O'Reilly Media, 2018.
# - [Object-Oriented Programming in Python](https://python-textbok.readthedocs.io/en/1.0/)
# - https://python-course.eu/oop/
# - [Back to the Machine Learning fundamentals: How to write Pipeline for Model deployment (Part 2/3)](https://ivannardini.medium.com/back-to-the-machine-learning-fundamentals-how-to-write-code-for-model-deployment-part-2-3-9632d5a43f98)
# - https://github.com/pyGuru123/Python-design-Patterns
#
# </font>
# </div>

# # Requirements
# <hr style = "border:2px solid black" ></hr>

# In[20]:


get_ipython().run_line_magic("load_ext", "watermark")
get_ipython().run_line_magic("watermark", "-v -iv")
